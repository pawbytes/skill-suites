#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Resolve where a PawBytes suite keeps its files, and migrate a legacy tree to paw-suites/.

Every suite writes to `{project-root}/paw-suites/<suite>/`. Older releases wrote to
`{project-root}/.pawbytes/<suite>-suites/` with a different layout inside. The suite's
`assets/layout.json` describes both: `root`, `legacy_root`, ordered `rules` mapping a
legacy path to its new path, and the `config_keys` that held the old folders.

Subcommands (all print JSON):
  detect                      mode: fresh | new | legacy | both, the root to use, and
                              `overrides`: config folder keys set to a custom path (a key
                              still holding the old or new default is not an override)
  locate PATH [--write]       absolute path for PATH (new-layout, relative to the suite root);
                              in legacy mode, the matching file in the legacy tree
  plan                        dry run of a migration: moves, duplicates, conflicts, config edits
  apply                       perform the migration: move files, never overwrite, rewrite paths
                              inside moved text files, update config, leave MOVED.md behind
  index                       regenerate {root}/README.md: one table per `items` glob in the
                              layout, a row per item folder with its title, `Status:` and
                              `Next:` lines (from the item's README.md) and last change date

Rule patterns are `/`-separated. In `from`: `*` (or a segment glob like `*.md`) matches
one segment and is captured as {1}, {2}, ... left to right; a final `**` matches the
remaining segments as {rest}. `to` uses those captures as whole segments. `to: null`
leaves the file where it is; a `to` starting with `/` is relative to the project root
instead of the suite root. Unmatched paths keep their relative path.

Exit codes: 0 ok, 1 bad input, 2 runtime error.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import shutil
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".csv", ".html", ".txt", ".toml"}
MARKER = "MOVED.md"
PATH_CHARS = r"[A-Za-z0-9_.{}\-/]+"


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))
    sys.exit(code)


def fail(msg: str, code: int = 1) -> None:
    out({"ok": False, "error": msg}, code)


# ---------------------------------------------------------------- rules


def _norm(rel: str) -> str:
    rel = rel.replace("\\", "/")
    rel = re.sub(r"/+", "/", rel).strip("/")
    return "" if rel == "." else rel


class Rule:
    def __init__(self, src: str, dst: str | None):
        self.src = _norm(src).split("/") if _norm(src) else []
        self.dst = dst
        self.absolute = bool(dst) and dst.startswith("/")
        self.wild = [i for i, s in enumerate(self.src) if "*" in s and s != "**"]
        if "**" in self.src[:-1]:
            raise ValueError(f"'**' may only end a pattern: {src}")

    def match(self, segs: list[str]) -> dict | None:
        pat = self.src
        tail = bool(pat) and pat[-1] == "**"
        head = pat[:-1] if tail else pat
        if len(segs) < len(head) or (not tail and len(segs) != len(head)):
            return None
        caps: dict[str, str] = {}
        n = 0
        for p, s in zip(head, segs):
            if "*" in p:
                if not fnmatch.fnmatchcase(s, p):
                    return None
                n += 1
                caps[str(n)] = s
            elif p != s:
                return None
        caps["rest"] = "/".join(segs[len(head):]) if tail else ""
        return caps

    def apply(self, caps: dict) -> str:
        dst = self.dst.lstrip("/") if self.absolute else self.dst
        res = re.sub(r"\{(\w+)\}", lambda m: caps.get(m.group(1), m.group(0)), dst)
        return _norm(res)

    def inverse(self) -> "Rule | None":
        """The new->legacy rule, or None when this rule cannot be reversed."""
        if self.dst is None or self.absolute:
            return None
        dsegs = _norm(self.dst).split("/") if _norm(self.dst) else []
        pat, mapping = [], {}
        k = 0
        for i, seg in enumerate(dsegs):
            m = re.fullmatch(r"\{(\w+)\}", seg)
            if m and m.group(1) == "rest":
                if i != len(dsegs) - 1:
                    return None
                pat.append("**")
            elif m:
                k += 1
                pat.append("*")
                mapping[str(k)] = m.group(1)
            elif "{" in seg:
                return None
            else:
                pat.append(seg)
        back = []
        for i, seg in enumerate(self.src):
            if seg == "**":
                back.append("{rest}")
            elif "*" in seg:
                orig = str(self.wild.index(i) + 1)
                new_idx = next((nk for nk, ov in mapping.items() if ov == orig), None)
                if new_idx is None:
                    return None
                back.append("{" + new_idx + "}")
            else:
                back.append(seg)
        r = Rule("/".join(pat), "/".join(back))
        return r


class Layout:
    def __init__(self, data: dict, project_root: Path):
        for key in ("suite", "root"):
            if key not in data:
                raise ValueError(f"layout.json lacks '{key}'")
        self.data = data
        self.project = project_root
        self.root = project_root / _norm(data["root"])
        self.legacy = project_root / _norm(data["legacy_root"]) if data.get("legacy_root") else None
        self.rules = [Rule(r["from"], r.get("to")) for r in data.get("rules", [])]
        self.rules.append(Rule("**", "{rest}"))
        self.inverse = [r for r in (x.inverse() for x in self.rules) if r]

    def forward(self, rel: str) -> tuple[Path | None, Rule]:
        """Legacy relative path -> new absolute path (None = stays put)."""
        segs = _norm(rel).split("/") if _norm(rel) else []
        for rule in self.rules:
            caps = rule.match(segs)
            if caps is None:
                continue
            if rule.dst is None:
                return None, rule
            target = rule.apply(caps)
            return (self.project / target if rule.absolute else self.root / target), rule
        raise AssertionError("catch-all rule missing")

    def backward(self, rel: str) -> list[Path]:
        """New relative path -> candidate legacy paths, in rule order."""
        segs = _norm(rel).split("/") if _norm(rel) else []
        seen, cands = set(), []
        for rule in self.inverse:
            caps = rule.match(segs)
            if caps is not None:
                p = self.legacy / rule.apply(caps)
                if p not in seen:
                    seen.add(p)
                    cands.append(p)
        return cands


# ---------------------------------------------------------------- state


def legacy_files(lay: Layout) -> list[Path]:
    if not lay.legacy or not lay.legacy.is_dir():
        return []
    return sorted(p for p in lay.legacy.rglob("*") if p.is_file() and p.relative_to(lay.legacy).as_posix() != MARKER)


def config_overrides(lay: Layout, config_path: Path | None) -> dict:
    """Config folder keys set to a custom path. Old and new defaults do not count: older
    setups wrote the legacy default into config verbatim, and it must not pin the suite there."""
    keys = lay.data.get("config_keys") or []
    section_name = lay.data.get("config_section")
    if not keys or not section_name or not config_path or not config_path.is_file():
        return {}
    try:
        import yaml

        cfg = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    section = cfg.get(section_name) if isinstance(cfg, dict) else None
    if not isinstance(section, dict):
        return {}
    found = {}
    for spec in keys:
        for key in {spec["key"], spec.get("new_key") or spec["key"]}:
            cur = section.get(key)
            if not isinstance(cur, str) or not cur.strip():
                continue
            path = _resolve_token(cur, lay.project)
            defaults = {_resolve_token(spec[k], lay.project) for k in ("legacy", "new") if spec.get(k)}
            if path not in defaults:
                found[key] = str(path)
    return found


def detect(lay: Layout, config_path: Path | None = None) -> dict:
    has_new = lay.root.is_dir() and any(lay.root.iterdir())
    files = legacy_files(lay)
    movable = [f for f in files if lay.forward(f.relative_to(lay.legacy).as_posix())[0] is not None]
    has_legacy = bool(movable)
    mode = "both" if has_new and has_legacy else "new" if has_new else "legacy" if has_legacy else "fresh"
    root = lay.legacy if mode == "legacy" else lay.root
    res = {"ok": True, "suite": lay.data["suite"], "mode": mode, "root": str(root),
           "new_root": str(lay.root), "legacy_root": str(lay.legacy) if lay.legacy else None,
           "legacy_files": len(movable), "overrides": config_overrides(lay, config_path)}
    if mode in ("legacy", "both"):
        res["hint"] = ("Legacy files found. Migrate with the setup skill, or "
                       "`paw-paths.py plan` then `apply`.")
    return res


def locate(lay: Layout, rel: str, write: bool) -> dict:
    mode = detect(lay)["mode"]
    new = lay.root / _norm(rel)
    if mode in ("new", "fresh") or not lay.legacy:
        return {"ok": True, "mode": mode, "path": str(new)}
    cands = lay.backward(rel)
    if mode == "both":
        if new.exists() or write:
            return {"ok": True, "mode": mode, "path": str(new)}
        hit = next((c for c in cands if c.exists()), None)
        return {"ok": True, "mode": mode, "path": str(hit or new)}
    hit = next((c for c in cands if c.exists()), None)
    path = hit or (cands[0] if cands else lay.legacy / _norm(rel))
    return {"ok": True, "mode": mode, "path": str(path)}


# ---------------------------------------------------------------- migration


def _same(a: Path, b: Path) -> bool:
    return a.stat().st_size == b.stat().st_size and a.read_bytes() == b.read_bytes()


def _resolve_token(value: str, project: Path) -> Path:
    p = Path(value.replace("{project-root}", str(project))).expanduser()
    return (p if p.is_absolute() else project / p).resolve()


def config_edits(lay: Layout, config_path: Path) -> tuple[dict, list[dict]]:
    keys = lay.data.get("config_keys") or []
    section_name = lay.data.get("config_section")
    if not keys or not section_name or not config_path.is_file():
        return {}, []
    import yaml

    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    section = cfg.get(section_name)
    if not isinstance(section, dict):
        return cfg, []
    edits = []
    for spec in keys:
        key, new_key = spec["key"], spec.get("new_key") or spec["key"]
        if key not in section:
            continue
        cur = section[key]
        is_default = isinstance(cur, str) and spec.get("legacy") and \
            _resolve_token(cur, lay.project) == _resolve_token(spec["legacy"], lay.project)
        value = spec["new"] if is_default else cur
        if value != cur or new_key != key:
            edits.append({"section": section_name, "key": key, "new_key": new_key, "from": cur, "to": value})
    return cfg, edits


def build_plan(lay: Layout, config_path: Path) -> dict:
    moves, dupes, conflicts, kept = [], [], [], []
    claimed: dict[Path, Path] = {}  # destination -> legacy source already moving there
    for f in legacy_files(lay):
        rel = f.relative_to(lay.legacy).as_posix()
        dest, _ = lay.forward(rel)
        entry = {"from": str(f), "to": str(dest)}
        if dest is None:
            kept.append(rel)
        elif dest in claimed:
            (dupes if _same(f, claimed[dest]) else conflicts).append(entry)
        elif dest.exists():
            (dupes if dest.is_file() and _same(f, dest) else conflicts).append(entry)
        else:
            claimed[dest] = f
            moves.append(entry)
    _, edits = config_edits(lay, config_path)
    return {"ok": True, "suite": lay.data["suite"], "legacy_root": str(lay.legacy) if lay.legacy else None,
            "new_root": str(lay.root), "moves": moves, "duplicates": dupes, "conflicts": conflicts,
            "kept": kept, "config": edits,
            "summary": f"{len(moves)} to move, {len(dupes)} already there, {len(conflicts)} conflicts, "
                       f"{len(kept)} kept, {len(edits)} config edits"}


def _link_pattern(lay: Layout) -> re.Pattern | None:
    if not lay.legacy:
        return None
    legacy_rel = _norm(lay.data["legacy_root"])
    # A left boundary keeps `paw-design-system` or `src/design-system` from matching a bare
    # one-segment root; a dotted root like `.pawbytes/x` may follow `/` in absolute paths.
    boundary = r"(?<![\w.\-])" if "/" in legacy_rel else r"(?<![\w.\-/])"
    return re.compile(boundary + r"(?:\{project-root\}/)?" + re.escape(legacy_rel) + r"(?![\w\-])(/" + PATH_CHARS + r")?")


def rewrite_text(lay: Layout, text: str) -> str:
    pat = _link_pattern(lay)
    if pat is None:
        return text
    new_root_rel = _norm(lay.data["root"])

    def sub(m: re.Match) -> str:
        prefix = "{project-root}/" if m.group(0).startswith("{project-root}/") else ""
        tail = m.group(1) or ""
        trail = "/" if tail.endswith("/") else ""
        rel = _norm(tail)
        if not rel:
            return prefix + new_root_rel + trail
        dest, _ = lay.forward(rel)
        if dest is None:
            return m.group(0)
        target = os.path.relpath(dest, lay.project).replace("\\", "/")
        return prefix + target + trail

    return pat.sub(sub, text)


def _prune(d: Path) -> None:
    for sub in sorted((p for p in d.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        try:
            sub.rmdir()
        except OSError:
            pass


def apply(lay: Layout, config_path: Path) -> dict:
    plan = build_plan(lay, config_path)
    moved = []
    for m in plan["moves"]:
        src, dst = Path(m["from"]), Path(m["to"])
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        moved.append(dst)
    for d in plan["duplicates"]:
        Path(d["from"]).unlink()
    rewritten = []
    for dst in moved:
        if dst.suffix.lower() in TEXT_SUFFIXES:
            try:
                text = dst.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            new = rewrite_text(lay, text)
            if new != text:
                dst.write_text(new, encoding="utf-8")
                rewritten.append(str(dst))
    cfg, edits = config_edits(lay, config_path)
    if edits:
        import yaml

        section = cfg[lay.data["config_section"]]
        for e in edits:
            if e["new_key"] != e["key"]:
                section.pop(e["key"], None)
            section[e["new_key"]] = e["to"]
        config_path.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")
    if lay.legacy and lay.legacy.is_dir():
        _prune(lay.legacy)
        left = [c["from"] for c in plan["conflicts"]] + plan["kept"]
        lines = [f"# Moved to `{_norm(lay.data['root'])}/`", "",
                 f"The {lay.data['suite']} suite now keeps its files in `{_norm(lay.data['root'])}/`.",
                 "This folder is no longer read once it holds nothing but this note."]
        if plan["conflicts"]:
            lines += ["", "## Not moved (a different file already exists at the new path)", ""]
            lines += [f"- `{Path(c['from']).relative_to(lay.legacy).as_posix()}` -> `{c['to']}`" for c in plan["conflicts"]]
        if plan["kept"]:
            lines += ["", "## Kept here on purpose", ""] + [f"- `{k}`" for k in plan["kept"]]
        lay.legacy.mkdir(parents=True, exist_ok=True)
        (lay.legacy / MARKER).write_text("\n".join(lines) + "\n", encoding="utf-8")
        plan["left_in_legacy"] = left
    plan.update({"applied": True, "rewritten": rewritten, "config": edits})
    return plan


# ---------------------------------------------------------------- index


def _item_meta(folder: Path) -> dict:
    meta = {"title": folder.name, "status": "", "next": ""}
    readme = folder / "README.md"
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if s.startswith("# ") and meta["title"] == folder.name:
                meta["title"] = s[2:].strip()
            low = s.lower().lstrip("-* ").replace("**", "")
            for key in ("status", "next"):
                if low.startswith(key + ":") and not meta[key]:
                    meta[key] = s.split(":", 1)[1].strip().strip("*").strip()
    files = [p for p in folder.rglob("*") if p.is_file()]
    newest = max((p.stat().st_mtime for p in files), default=folder.stat().st_mtime)
    from datetime import datetime

    meta["updated"] = datetime.fromtimestamp(newest).strftime("%Y-%m-%d")
    meta["_ts"] = newest
    return meta


def build_index(lay: Layout, root: Path) -> dict:
    title = lay.data.get("title") or f"PawBytes {lay.data['suite']}"
    lines = [f"# {title}", "",
             "Generated by `paw-paths.py index`; edit the items' own README.md files, not this one.", ""]
    counts = {}
    for glob in lay.data.get("items", []):
        rows = []
        for item in sorted(p for p in root.glob(glob) if not p.name.startswith(("_", ".")) and p.name != "README.md"):
            rel = item.relative_to(root).as_posix()
            if item.is_dir():
                m = _item_meta(item)
                rows.append((m["_ts"], f"| [{m['title']}]({rel}/) | {m['status']} | {m['next']} | {m['updated']} |"))
            else:
                from datetime import datetime

                ts = item.stat().st_mtime
                rows.append((ts, f"| [{item.name}]({rel}) |  |  | {datetime.fromtimestamp(ts):%Y-%m-%d} |"))
        heading = (glob.split("/")[0] if "/" in glob else lay.data["suite"]).replace("-", " ").title()
        lines += [f"## {heading}", ""]
        if rows:
            lines += ["| Item | Status | Next | Updated |", "|---|---|---|---|"]
            lines += [r for _, r in sorted(rows, key=lambda x: -x[0])]
        else:
            lines.append("_Nothing yet._")
        lines.append("")
        counts[glob] = len(rows)
    extras = [p.name for p in sorted(root.iterdir()) if p.is_dir() and p.name.startswith("_")] if root.is_dir() else []
    if extras:
        lines += ["## Internal", ""] + [f"- [`{n}/`]({n}/)" for n in extras] + [""]
    root.mkdir(parents=True, exist_ok=True)
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8")
    return {"ok": True, "path": str(root / "README.md"), "items": counts}


# ---------------------------------------------------------------- cli


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project-root", default=".", help="project root (default: working directory)")
    ap.add_argument("--layout", help="layout.json (default: ../assets/layout.json beside this script)")
    ap.add_argument("--config", help="config.yaml (default: {project-root}/.pawbytes/config/config.yaml)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("detect")
    loc = sub.add_parser("locate")
    loc.add_argument("path", help="new-layout path relative to the suite root")
    loc.add_argument("--write", action="store_true", help="the path is about to be written")
    sub.add_parser("plan")
    sub.add_parser("apply")
    sub.add_parser("index")
    a = ap.parse_args()

    project = Path(a.project_root).expanduser().resolve()
    layout_path = Path(a.layout) if a.layout else Path(__file__).resolve().parent.parent / "assets" / "layout.json"
    if not layout_path.is_file():
        fail(f"layout not found: {layout_path}")
    try:
        lay = Layout(json.loads(layout_path.read_text(encoding="utf-8")), project)
    except (ValueError, json.JSONDecodeError) as e:
        fail(f"bad layout {layout_path}: {e}")
    config_path = Path(a.config) if a.config else project / ".pawbytes" / "config" / "config.yaml"

    try:
        if a.cmd == "detect":
            out(detect(lay, config_path))
        if a.cmd == "locate":
            out(locate(lay, a.path, a.write))
        if a.cmd == "plan":
            out(build_plan(lay, config_path))
        if a.cmd == "apply":
            out(apply(lay, config_path))
        if a.cmd == "index":
            d = detect(lay)
            if d["mode"] == "legacy":
                out({"ok": True, "skipped": "legacy mode: the index is built after migration"})
            out(build_index(lay, lay.root))
    except OSError as e:
        fail(f"{type(e).__name__}: {e}", 2)


if __name__ == "__main__":
    main()
