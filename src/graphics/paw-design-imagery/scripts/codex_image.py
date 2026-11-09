#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate images with the Codex CLI's built-in image tool, for projects whose config sets
`design.image_provider: codex-cli` (no per-image cost; uses the user's Codex account).

Codex runs read-only and is told not to save anything: this script copies the newest PNG
from Codex's own folder (~/.codex/generated_images/<thread_id>/) to --out. Letting Codex
save files itself wrote wrong files under parallel jobs and hung re-encoding base64, so
jobs run one at a time (a machine-wide lock) with a timeout.

Prompts come from a file, never the command line, because long prompts break shell quoting.

Subcommands:
  find                                 locate codex (design.codex_path, $CODEX_PATH, PATH, the Windows app folder)
  run --prompt @file.txt --out PATH [--ref IMG ...] [--aspect 2:3] [--timeout 600]
      [--project DIR --stage S] [--codex PATH]
  batch JOBS.tsv [--timeout 600] [--project DIR --stage S]
      one job per line: name <TAB> prompt-file <TAB> out-path <TAB> ref1;ref2;...

With --project, the stage gate is checked first and relative paths resolve under the project.
An existing --out is moved to candidates/ beside it, never overwritten. Beside every output
goes <out-stem>.json: provider, prompt, refs (in order), thread id, takes, seconds.

Exit codes: 0 ok; 1 blocked by the gate, timed out, or no image produced; 2 error.
Output: one JSON object on stdout.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import production  # noqa: E402  (bundled beside this script)

GEN = Path.home() / ".codex" / "generated_images"
# Shared with paw-vid on purpose: two suites picking "the newest PNG" at once would swap outputs.
LOCK = Path.home() / ".codex" / ".pawvid-image.lock"
ASPECTS = {"1:1": "1024x1024", "2:3": "1024x1536", "3:2": "1536x1024", "9:16": "1024x1536",
           "16:9": "1536x1024", "4:5": "1024x1536", "3:4": "1024x1536", "4:3": "1536x1024",
           "1.91:1": "1536x1024", "2.39:1": "1536x1024", "21:9": "1536x1024"}

HEADER = ("Use your built-in image generation tool to create ONE image{refs}. {size}highest quality. "
          "Do NOT save, copy, convert or re-encode the image and do not write any files or run any "
          "commands: just generate it once and then finish.\n\nIMAGE PROMPT:\n")


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def config_codex_path(start: Path | None = None) -> str | None:
    """design.codex_path (or any suite's codex_path) from the nearest .pawbytes/config (user file first); a plain line scan, no YAML library."""
    here = (start or Path.cwd()).resolve()
    fallback = None
    for folder in [here, *here.parents]:
        for name in ("config.user.yaml", "config.yaml"):
            cfg = folder / ".pawbytes" / "config" / name
            if not cfg.is_file():
                continue
            section = None
            for line in cfg.read_text(encoding="utf-8-sig").splitlines():
                if line and not line[0].isspace() and line.rstrip().endswith(":"):
                    section = line.strip()[:-1]
                key, _, val = line.strip().partition(":")
                if key == "codex_path":
                    val = val.split(" #", 1)[0].strip().strip("'\"")
                    if val and section == "design":
                        return val
                    fallback = fallback or val or None
    return fallback


def find_codex(explicit: str | None = None, start: Path | None = None) -> Path:
    candidates = [explicit, config_codex_path(start), os.environ.get("CODEX_PATH"), shutil.which("codex")]
    local = os.environ.get("LOCALAPPDATA")
    if local:
        found = sorted(glob.glob(os.path.join(local, "OpenAI", "Codex", "bin", "*", "codex.exe")),
                       key=os.path.getmtime, reverse=True)
        candidates += found
    for c in candidates:
        if c and Path(c).is_file():
            return Path(c)
    raise Fail("codex not found: install the Codex CLI or set design.codex_path / $CODEX_PATH to codex(.exe)")


def _resolve(path: str, project: Path | None) -> Path:
    p = Path(path)
    if not p.is_absolute() and project is not None:
        return project / p
    return p


class image_lock:
    def __init__(self, timeout: float):
        self.timeout = timeout

    def __enter__(self):
        LOCK.parent.mkdir(parents=True, exist_ok=True)
        deadline = time.time() + self.timeout
        while True:
            try:
                fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                return self
            except FileExistsError:
                try:
                    if time.time() - LOCK.stat().st_mtime > self.timeout + 60:
                        LOCK.unlink(missing_ok=True)
                        continue
                except FileNotFoundError:
                    continue
                if time.time() > deadline:
                    raise Fail("another Codex image job is running; jobs run one at a time")
                time.sleep(2)

    def __exit__(self, *exc):
        LOCK.unlink(missing_ok=True)
        return False


def _prompt_text(raw: str, project: Path | None) -> str:
    if not raw.startswith("@"):
        raise Fail("--prompt takes @file.txt; long prompts break shell quoting")
    src = _resolve(raw[1:], project)
    if not src.is_file():
        raise Fail(f"prompt file not found: {src}")
    return src.read_text(encoding="utf-8-sig").strip()


def generate(codex: Path, prompt: str, refs: list[Path], dest: Path, aspect: str | None,
             timeout: int) -> dict:
    missing = [str(r) for r in refs if not r.is_file()]
    if missing:
        raise Fail(f"reference images not found: {missing}")
    size = f"{ASPECTS[aspect]} ({aspect}), " if aspect in ASPECTS else ""
    order = "; ".join(f"image {i + 1} = {r.name}" for i, r in enumerate(refs))
    head = HEADER.format(refs=f", using the attached reference images in order ({order})" if refs else "",
                         size=size)
    cmd = [str(codex), "exec", "--skip-git-repo-check", "-s", "read-only", "-c", 'approval_policy="never"',
           "--json"]
    for r in refs:
        cmd += ["-i", str(r)]
    cmd.append("-")
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, input=head + prompt + "\n", capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout)
        log, rc = proc.stdout + proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as exc:
        log = (exc.stdout or "") if isinstance(exc.stdout, str) else ""
        rc = "timeout"
    thread = None
    for line in log.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        thread = ev.get("thread_id") or (ev.get("msg") or {}).get("thread_id") or thread
        if thread:
            break
    images = sorted((GEN / thread).glob("*.png"), key=lambda p: p.stat().st_mtime) if thread else []
    record = {"provider": "codex-cli", "prompt": prompt, "refs": [str(r) for r in refs], "aspect": aspect,
              "thread_id": thread, "takes": len(images), "seconds": round(time.time() - t0, 1), "exit": rc,
              "at": datetime.now(timezone.utc).replace(microsecond=0).isoformat()}
    if not images:
        record["log_tail"] = log[-1500:]
        return record
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        cand = dest.parent / "candidates"
        cand.mkdir(exist_ok=True)
        shutil.move(str(dest), cand / f"{dest.stem}-{datetime.now().strftime('%Y%m%d-%H%M%S')}{dest.suffix}")
    shutil.copyfile(images[-1], dest)
    record["file"] = str(dest)
    sidecar = dest.with_suffix(".json")
    tmp = sidecar.with_name(f".{sidecar.name}.tmp")
    tmp.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, sidecar)
    return record


def _gate(project: Path | None, stage: str | None) -> None:
    if project is None:
        return
    if not stage:
        raise Fail("--project needs --stage so the gate is checked")
    reasons = production.stage_gate(project, stage)
    if reasons:
        out({"ok": False, "blocked": True, "stage": stage, "reasons": reasons}, 1)


def cmd_find(a) -> None:
    out({"ok": True, "codex": str(find_codex(a.codex)), "generated_images": str(GEN)})


def cmd_run(a) -> None:
    project = Path(a.project) if a.project else None
    _gate(project, a.stage)
    codex = find_codex(a.codex, project)
    prompt = _prompt_text(a.prompt, project)
    refs = [_resolve(r, project) for r in a.ref or []]
    with image_lock(a.timeout):
        rec = generate(codex, prompt, refs, _resolve(a.out, project), a.aspect, a.timeout)
    if "file" not in rec:
        out({"ok": False, "error": "Codex produced no image", **rec}, 1)
    out({"ok": True, **rec})


def cmd_batch(a) -> None:
    project = Path(a.project) if a.project else None
    _gate(project, a.stage)
    codex = find_codex(a.codex, project)
    jobs = []
    for n, line in enumerate(_resolve(a.jobs, project).read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            raise Fail(f"jobs line {n}: expected name<TAB>prompt-file<TAB>out[<TAB>refs;...]")
        jobs.append(parts + [""] * (4 - len(parts)))
    results = []
    for name, prompt_file, dest, refs in jobs:
        refs_l = [_resolve(r, project) for r in refs.split(";") if r.strip()]
        try:
            with image_lock(a.timeout):
                rec = generate(codex, _prompt_text("@" + prompt_file, project), refs_l,
                               _resolve(dest, project), a.aspect, a.timeout)
            ok = "file" in rec
            if not ok:
                rec["error"] = f"Codex produced no image (exit {rec.get('exit')})"
        except Fail as exc:
            rec, ok = {"error": str(exc)}, False
        results.append({"name": name, "ok": ok, **{k: rec.get(k) for k in ("file", "seconds", "takes", "error",
                                                                          "exit", "log_tail")}})
        print(f"{name}: {'ok' if ok else 'FAILED'}", file=sys.stderr, flush=True)
    failed = [r["name"] for r in results if not r["ok"]]
    out({"ok": not failed, "results": results, "failed": failed}, 1 if failed else 0)


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("find", help="locate the codex executable")
    s.add_argument("--codex")
    s.set_defaults(fn=cmd_find)
    for name, fn in (("run", cmd_run), ("batch", cmd_batch)):
        s = sub.add_parser(name)
        if name == "run":
            s.add_argument("--prompt", required=True, help="@file.txt with the image prompt")
            s.add_argument("--out", required=True)
            s.add_argument("--ref", action="append", help="reference image, repeatable; order is cited in the prompt")
        else:
            s.add_argument("jobs", help="TSV: name, prompt file, out path, refs separated by ;")
        s.add_argument("--aspect", choices=list(ASPECTS))
        s.add_argument("--timeout", type=int, default=600)
        s.add_argument("--project")
        s.add_argument("--stage", choices=production.STAGES)
        s.add_argument("--codex")
        s.set_defaults(fn=fn)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, production.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # exit 1 means blocked; an unexpected failure must not look like one
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
