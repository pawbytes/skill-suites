#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Production manifest for PawBytes Graphics Suite projects.

Owns {project}/production.json: stages, format profiles, placements, gates,
approvals, skips, budget and cost log. Every stage skill reads and writes project
state through this script so the gates mean the same thing everywhere.

Output: one JSON object on stdout. Errors: JSON on stderr, exit 2.
`gate`, `start`, `submit` and `approve` exit 1 (reasons on stdout) when earlier stages block
the stage. `approve` needs a submitted artifact. Changing an approved stage is `reopen`.

Subcommands:
  init      --root DIR --slug SLUG --title T --profile P [--placements a,b] [--pieces N]
            [--medium digital|print] [--budget 5] [--image-provider fal|codex-cli]
  list      --root DIR
  status    --project DIR
  gate      --project DIR STAGE
  start     --project DIR STAGE
  submit    --project DIR STAGE --artifact PATH [--note TEXT]
  approve   --project DIR STAGE [--note TEXT]
  skip      --project DIR STAGE --reason TEXT
  enable    --project DIR STAGE
  reopen    --project DIR STAGE [--note TEXT]
  set       --project DIR KEY=VALUE ...   (budget_usd, placements, pieces, medium, image_provider, title)
  ack-budget --project DIR --reason TEXT --cap-usd X   new spending cap the user accepted
  cost      --project DIR --stage S --endpoint E --usd X [--units N] [--request-id R] [--note T]
  profiles
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = 1
MANIFEST = "production.json"
STAGES = ["concept", "style", "layout", "imagery", "compose", "deliver"]
UNSKIPPABLE = {"compose"}  # the design itself; deliver exports it
PROVIDERS = ("fal", "codex-cli")

PROFILES: dict[str, dict] = {
    "social-post": {"medium": "digital", "placements": ["instagram-feed-portrait"], "pieces": 1},
    "carousel": {"medium": "digital", "placements": ["instagram-feed-portrait"], "pieces": 7},
    "story": {"medium": "digital", "placements": ["instagram-story"], "pieces": 1},
    "poster": {"medium": "print", "placements": ["print-a3"], "pieces": 1},
    "flyer": {"medium": "print", "placements": ["print-a5"], "pieces": 2},
    "banner": {"medium": "digital", "placements": ["web-hero-1920x1080"], "pieces": 1},
    "ad-set": {"medium": "digital", "placements": ["iab-300x250", "iab-728x90", "iab-300x600", "iab-320x50",
                                                   "meta-ads-feed-1x1", "meta-ads-stories-reels"], "pieces": 1},
    "thumbnail": {"medium": "digital", "placements": ["youtube-thumbnail"], "pieces": 1},
}

PROJECT_DIRS = ["brand", "concept", "style", "layout/wireframes", "imagery/source", "compose", "deliver", "fal"]


class Fail(Exception):
    pass


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


class manifest_lock:
    """Serialise read-modify-write of production.json across processes (parallel image jobs)."""

    def __init__(self, project: Path, timeout: float = 30.0):
        self.path = project / ".production.lock"
        self.timeout = timeout

    def __enter__(self):
        deadline = time.time() + self.timeout
        while True:
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                return self
            except FileExistsError:
                try:  # a lock older than the timeout belongs to a crashed process
                    if time.time() - self.path.stat().st_mtime > self.timeout:
                        self.path.unlink(missing_ok=True)
                        continue
                except FileNotFoundError:
                    continue
                if time.time() > deadline:
                    raise Fail(f"{self.path} is held by another process; retry in a moment")
                time.sleep(0.1)

    def __exit__(self, *exc):
        self.path.unlink(missing_ok=True)
        return False


def load(project: Path) -> dict:
    path = project / MANIFEST
    if not path.is_file():
        raise Fail(f"no {MANIFEST} in {project}; create the project with `production.py init`")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Fail(f"{path} is not valid JSON: {exc}")


def save(project: Path, data: dict) -> None:
    data["updated"] = now()
    data["spent_usd"] = round(sum(c.get("usd", 0) for c in data.get("costs", [])), 4)
    fd, tmp = tempfile.mkstemp(dir=project, prefix=".production.", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    for attempt in range(20):  # Windows refuses the replace while a reader holds the file open
        try:
            os.replace(tmp, project / MANIFEST)
            return
        except PermissionError:
            if attempt == 19:
                raise
            time.sleep(0.1)


def log(data: dict, event: str, stage: str | None = None, note: str | None = None) -> None:
    entry = {"at": now(), "event": event}
    if stage:
        entry["stage"] = stage
    if note:
        entry["note"] = note
    data.setdefault("history", []).append(entry)


def check_stage(stage: str) -> str:
    if stage not in STAGES:
        raise Fail(f"unknown stage '{stage}'; stages are {', '.join(STAGES)}")
    return stage


def effective_budget(data: dict) -> float | None:
    """The budget, or the cap the user acknowledged going over it to."""
    ack = data.get("budget_ack") or {}
    if ack.get("cap_usd") is not None:
        return ack["cap_usd"]
    return data.get("budget_usd")


def gate_reasons(data: dict, stage: str) -> list[str]:
    stages = data["stages"]
    reasons: list[str] = []
    if stages[stage]["status"] == "off":
        reasons.append(f"{stage} is off for this project; turn it on with `enable {stage}`")
    for prior in STAGES[: STAGES.index(stage)]:
        st = stages[prior]["status"]
        if st in ("off", "approved", "skipped"):
            continue
        reasons.append(f"{prior} is {st}; it must be approved or skipped first")
    return reasons


def next_stage(data: dict) -> str | None:
    for s in STAGES:
        if data["stages"][s]["status"] not in ("off", "approved", "skipped"):
            return s
    return None


def summary(data: dict, project: Path) -> dict:
    nxt = next_stage(data)
    return {
        "project": str(project), "slug": data["slug"], "title": data["title"], "profile": data["profile"],
        "medium": data.get("medium"), "placements": data.get("placements"), "pieces": data.get("pieces"),
        "image_provider": data.get("image_provider"),
        "budget_usd": data.get("budget_usd"), "spent_usd": data.get("spent_usd", 0),
        "budget_ack": data.get("budget_ack"),
        "stages": {s: data["stages"][s] for s in STAGES},
        "next_stage": nxt,
        "next_blocked_by": gate_reasons(data, nxt) if nxt else [],
        "done": nxt is None,
    }


def _placements(value: str) -> list[str]:
    items = [p.strip() for p in value.split(",") if p.strip()]
    if not items:
        raise Fail("placements must name at least one placement id")
    return items


def _pieces(value) -> int:
    try:
        n = int(value)
    except (TypeError, ValueError):
        raise Fail(f"pieces must be a whole number, got '{value}'")
    if not 1 <= n <= 20:
        raise Fail("pieces must be between 1 and 20 (Instagram and LinkedIn carousels top out at 20)")
    return n


def cmd_init(a) -> None:
    if a.profile not in PROFILES:
        raise Fail(f"unknown profile '{a.profile}'; profiles are {', '.join(PROFILES)}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", a.slug):
        raise Fail("slug must be lowercase letters, digits and hyphens")
    project = Path(a.root) / a.slug
    if (project / MANIFEST).exists():
        raise Fail(f"project already exists: {project}")
    prof = PROFILES[a.profile]
    medium = a.medium or prof["medium"]
    if medium not in ("digital", "print"):
        raise Fail("medium must be digital or print")
    project.mkdir(parents=True, exist_ok=True)
    for d in PROJECT_DIRS:
        (project / d).mkdir(parents=True, exist_ok=True)
    data = {
        "schema": SCHEMA, "slug": a.slug, "title": a.title, "profile": a.profile, "medium": medium,
        "placements": _placements(a.placements) if a.placements else list(prof["placements"]),
        "pieces": _pieces(a.pieces) if a.pieces is not None else prof["pieces"],
        "image_provider": a.image_provider,
        "budget_usd": a.budget, "budget_ack": None, "spent_usd": 0, "created": now(),
        "stages": {s: {"status": "pending"} for s in STAGES},
        "costs": [], "history": [],
    }
    log(data, "init", note=f"profile {a.profile}")
    save(project, data)
    out({"ok": True, **summary(data, project)})


def cmd_list(a) -> None:
    root = Path(a.root)
    projects = []
    if root.is_dir():
        for m in sorted(root.glob(f"*/{MANIFEST}")):
            try:
                data = json.loads(m.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                projects.append({"project": str(m.parent), "error": "unreadable manifest"})
                continue
            projects.append({"project": str(m.parent), "slug": data.get("slug"), "title": data.get("title"),
                             "profile": data.get("profile"), "next_stage": next_stage(data),
                             "updated": data.get("updated")})
    out({"ok": True, "root": str(root), "projects": projects})


def cmd_status(a) -> None:
    project = Path(a.project)
    out({"ok": True, **summary(load(project), project)})


def cmd_gate(a) -> None:
    data = load(Path(a.project))
    stage = check_stage(a.stage)
    reasons = gate_reasons(data, stage)
    out({"ok": not reasons, "stage": stage, "open": not reasons, "reasons": reasons}, 0 if not reasons else 1)


def transition(a, new_status: str, event: str, require_open: bool = False) -> None:
    project = Path(a.project)
    with manifest_lock(project):
        _transition(a, project, new_status, event, require_open)


def _transition(a, project: Path, new_status: str, event: str, require_open: bool) -> None:
    data = load(project)
    stage = check_stage(a.stage)
    entry = data["stages"][stage]
    if require_open or event in ("submit", "approve"):
        reasons = gate_reasons(data, stage)
        if reasons:
            out({"ok": False, "stage": stage, "reasons": reasons}, 1)
    if entry["status"] == "approved" and event in ("start", "submit"):
        raise Fail(f"{stage} is approved; use `reopen {stage}` so stages built on it are marked stale")
    if entry["status"] == "off" and new_status != "skipped":
        raise Fail(f"{stage} is off for this project; turn it on with `enable {stage}` first")
    if new_status == "approved" and not (entry["status"] == "awaiting_approval"
                                         or (entry["status"] == "stale" and entry.get("artifact"))):
        raise Fail(f"{stage} is {entry['status']}; submit an artifact before approving")
    if new_status == "skipped":
        if stage in UNSKIPPABLE:
            raise Fail(f"{stage} cannot be skipped: it is the design every export is made from")
        if entry["status"] == "off":
            raise Fail(f"{stage} is already off for this project")
    entry["status"] = new_status
    entry[f"{new_status}_at"] = now()
    if getattr(a, "artifact", None):
        entry["artifact"] = a.artifact
    note = getattr(a, "note", None) or getattr(a, "reason", None)
    if note:
        entry["note"] = note
    log(data, event, stage, note)
    save(project, data)
    out({"ok": True, "stage": stage, "status": new_status, "next_stage": next_stage(data)})


def cmd_reopen(a) -> None:
    project = Path(a.project)
    with manifest_lock(project):
        data = load(project)
        stage = check_stage(a.stage)
        if data["stages"][stage]["status"] == "off":
            raise Fail(f"{stage} is off; use `enable {stage}`")
        data["stages"][stage]["status"] = "in_progress"
        staled = []
        for later in STAGES[STAGES.index(stage) + 1:]:
            if data["stages"][later]["status"] in ("approved", "awaiting_approval", "in_progress"):
                data["stages"][later]["status"] = "stale"
                staled.append(later)
        log(data, "reopen", stage, a.note or (f"staled {', '.join(staled)}" if staled else None))
        save(project, data)
    out({"ok": True, "stage": stage, "status": "in_progress", "staled": staled})


def cmd_enable(a) -> None:
    project = Path(a.project)
    with manifest_lock(project):
        data = load(project)
        stage = check_stage(a.stage)
        if data["stages"][stage]["status"] not in ("off", "skipped"):
            raise Fail(f"{stage} is already {data['stages'][stage]['status']}")
        data["stages"][stage]["status"] = "pending"
        log(data, "enable", stage)
        save(project, data)
    out({"ok": True, "stage": stage, "status": "pending"})


def _number(key: str, value: str, allow_empty: bool = False):
    if value == "" and allow_empty:
        return None
    try:
        num = float(value)
    except ValueError:
        raise Fail(f"{key} must be a number, got '{value}'")
    if num <= 0:
        raise Fail(f"{key} must be positive, got {value}")
    return num


def cmd_set(a) -> None:
    project = Path(a.project)
    with manifest_lock(project):
        data = load(project)
        changed = {}
        for pair in a.pairs:
            if "=" not in pair:
                raise Fail(f"expected KEY=VALUE, got '{pair}'")
            key, value = pair.split("=", 1)
            if key == "budget_usd":
                data[key] = _number(key, value, allow_empty=True)
            elif key == "placements":
                data[key] = _placements(value)
            elif key == "pieces":
                data[key] = _pieces(value)
            elif key == "medium":
                if value not in ("digital", "print"):
                    raise Fail("medium must be digital or print")
                data[key] = value
            elif key == "image_provider":
                if value not in PROVIDERS:
                    raise Fail(f"image_provider must be one of {', '.join(PROVIDERS)}")
                data[key] = value
            elif key == "title":
                data[key] = value
            else:
                raise Fail(f"cannot set '{key}'; settable keys: budget_usd, placements, pieces, medium, "
                           "image_provider, title")
            changed[key] = data[key]
        log(data, "set", note=json.dumps(changed))
        save(project, data)
    out({"ok": True, "changed": changed})


def cmd_ack_budget(a) -> None:
    project = Path(a.project)
    with manifest_lock(project):
        data = load(project)
        data["budget_ack"] = {"at": now(), "reason": a.reason, "cap_usd": round(float(a.cap_usd), 4),
                              "spent_usd": data.get("spent_usd", 0)}
        log(data, "ack-budget", note=a.reason)
        save(project, data)
    out({"ok": True, "budget_ack": data["budget_ack"]})


def _append_cost(project: Path, stage: str, endpoint: str, usd: float, units=None, request_id=None,
                 note=None) -> tuple[dict, dict]:
    data = load(project)
    check_stage(stage)
    entry = {"at": now(), "stage": stage, "endpoint": endpoint, "usd": round(float(usd), 4)}
    if units is not None:
        entry["units"] = units
    if request_id:
        entry["request_id"] = request_id
    if note:
        entry["note"] = note
    data.setdefault("costs", []).append(entry)
    save(project, data)
    return data, entry


def cmd_cost(a) -> None:
    project = Path(a.project)
    with manifest_lock(project):
        data, entry = _append_cost(project, a.stage, a.endpoint, a.usd, a.units, a.request_id, a.note)
    out({"ok": True, "logged": entry, "spent_usd": data["spent_usd"], "budget_usd": data.get("budget_usd")})


def budget_check(project: Path, usd: float) -> list[str]:
    """Reasons a call costing `usd` must not run. Imported by fal.py."""
    data = load(project)
    budget = effective_budget(data)
    spent = sum(c.get("usd", 0) for c in data.get("costs", []))
    if budget is not None and spent + usd > budget:
        return [f"this call (~${usd:.2f}) takes spend ${spent:.2f} past budget ${budget:.2f}; "
                "raise the budget or record `ack-budget --reason --cap-usd`"]
    return []


def stage_gate(project: Path, stage: str) -> list[str]:
    """Gate reasons for a stage. Imported by fal.py and codex_image.py."""
    return gate_reasons(load(project), check_stage(stage))


def log_cost(project: Path, stage: str, endpoint: str, usd: float, units=None, request_id=None, note=None) -> float:
    """Append a cost entry and return spent_usd. Imported by fal.py."""
    with manifest_lock(project):
        data, _ = _append_cost(project, stage, endpoint, usd, units, request_id, note)
    return data["spent_usd"]


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init", help="create a project folder and manifest")
    s.add_argument("--root", required=True)
    s.add_argument("--slug", required=True)
    s.add_argument("--title", required=True)
    s.add_argument("--profile", required=True, choices=list(PROFILES))
    s.add_argument("--placements", help="comma-separated placement ids from platform-specs.json; first is the master")
    s.add_argument("--pieces", type=int, help="number of distinct pieces (carousel slides, flyer sides)")
    s.add_argument("--medium", choices=["digital", "print"])
    s.add_argument("--budget", type=float, help="fal.ai spend cap in USD")
    s.add_argument("--image-provider", choices=list(PROVIDERS),
                   help="this project's image provider; stages fall back to config design.image_provider when unset")
    s.set_defaults(fn=cmd_init)

    s = sub.add_parser("list", help="list projects under a root")
    s.add_argument("--root", required=True)
    s.set_defaults(fn=cmd_list)

    s = sub.add_parser("profiles", help="print format profiles")
    s.set_defaults(fn=lambda a: out({"ok": True, "stages": STAGES, "unskippable": sorted(UNSKIPPABLE),
                                     "profiles": PROFILES}))

    def proj(name, help_, fn, stage=True):
        s = sub.add_parser(name, help=help_)
        s.add_argument("--project", required=True)
        if stage:
            s.add_argument("stage")
        s.set_defaults(fn=fn)
        return s

    proj("status", "project status and next stage", cmd_status, stage=False)
    proj("gate", "exit 0 when STAGE may start, 1 with reasons", cmd_gate)
    proj("start", "mark STAGE in progress (gate must be open)",
         lambda a: transition(a, "in_progress", "start", require_open=True))
    s = proj("submit", "mark STAGE awaiting approval with its artifact",
             lambda a: transition(a, "awaiting_approval", "submit"))
    s.add_argument("--artifact", required=True)
    s.add_argument("--note")
    s = proj("approve", "record user approval of STAGE", lambda a: transition(a, "approved", "approve"))
    s.add_argument("--note")
    s = proj("skip", "record that the user skipped STAGE", lambda a: transition(a, "skipped", "skip"))
    s.add_argument("--reason", required=True)
    proj("enable", "turn on a stage that is off or was skipped", cmd_enable)
    s = proj("reopen", "reopen STAGE; downstream approvals become stale", cmd_reopen)
    s.add_argument("--note")

    s = sub.add_parser("set", help="change project settings")
    s.add_argument("--project", required=True)
    s.add_argument("pairs", nargs="+")
    s.set_defaults(fn=cmd_set)

    s = sub.add_parser("ack-budget", help="record the user's acceptance of a spending cap above the budget")
    s.add_argument("--project", required=True)
    s.add_argument("--reason", required=True)
    s.add_argument("--cap-usd", type=float, required=True, help="the total spend the user accepted")
    s.set_defaults(fn=cmd_ack_budget)

    s = sub.add_parser("cost", help="log a spend")
    s.add_argument("--project", required=True)
    s.add_argument("--stage", required=True)
    s.add_argument("--endpoint", required=True)
    s.add_argument("--usd", required=True, type=float)
    s.add_argument("--units", type=float)
    s.add_argument("--request-id")
    s.add_argument("--note")
    s.set_defaults(fn=cmd_cost)

    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except Fail as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # exit 1 means "blocked"; an unexpected failure must not look like one
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
