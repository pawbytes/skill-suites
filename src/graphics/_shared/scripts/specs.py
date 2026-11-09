#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Placement catalog for PawBytes Graphics Suite: sizes, safe zones, file caps, print bleed.

Reads ../assets/platform-specs.json (bundled beside this skill's scripts folder).
Ids are kebab-case (instagram-feed-portrait, iab-300x250, print-a3); loose names such
as "instagram", "leaderboard" or "a5" resolve through each entry's aliases.

Subcommands:
  list   [--class social|story|cover|web|thumbnail|display|print] [--q TEXT]
  show   ID                 entry plus its class rules and the safe rect in canvas units
  rules                     contrast thresholds, per-class text floors and word budgets

Output: JSON on stdout. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PX_PER_MM = 96 / 25.4
SPECS = Path(__file__).resolve().parent.parent / "assets" / "platform-specs.json"


class Fail(Exception):
    pass


def load() -> dict:
    if not SPECS.is_file():
        raise Fail(f"platform specs not found at {SPECS}")
    return json.loads(SPECS.read_text(encoding="utf-8"))


def resolve(name: str, data: dict | None = None) -> tuple[str, dict]:
    data = data or load()
    placements = data["placements"]
    key = (name or "").strip().lower()
    if key in placements:
        return key, placements[key]
    for pid, entry in placements.items():
        if key in entry.get("aliases", []):
            return pid, entry
    raise Fail(f"unknown placement '{name}'; run `specs.py list` (try --q {key.split('-')[0] or 'instagram'})")


def class_rules(entry: dict, data: dict | None = None) -> dict:
    data = data or load()
    return data["rules"]["classes"][entry["class"]]


def canvas_px(entry: dict) -> tuple[float, float, float]:
    """Canvas in CSS px as render.py lays it out: (width, height, bleed) including bleed."""
    if entry["unit"] == "mm":
        bleed = entry.get("bleed_mm", 0) * PX_PER_MM
        return entry["w_mm"] * PX_PER_MM + 2 * bleed, entry["h_mm"] * PX_PER_MM + 2 * bleed, bleed
    return float(entry["w"]), float(entry["h"]), 0.0


def safe_rect(entry: dict, data: dict | None = None) -> list[float]:
    """[left, top, right, bottom] in CSS px of the canvas that render.py measures.

    Platform safe zones where the catalog has them; otherwise the class margin, because a
    placement with no platform chrome still needs breathing room at the edge.
    """
    w, h, bleed = canvas_px(entry)
    if entry["unit"] == "mm":
        s = entry.get("safe_mm", 5) * PX_PER_MM
        sb = entry.get("safe_mm_bottom", entry.get("safe_mm", 5)) * PX_PER_MM
        return [bleed + s, bleed + s, w - bleed - s, h - bleed - sb]
    zone = entry.get("safe_zone")
    if zone:
        return [zone["left"], zone["top"], w - zone["right"], h - zone["bottom"]]
    margin = (class_rules(entry, data).get("margin_pct") or 0) / 100 * min(w, h)
    return [margin, margin, w - margin, h - margin]


def exclusions(entry: dict) -> list[list[float]]:
    """Extra keep-clear rects [x, y, w, h] in CSS px (timestamps, avatars)."""
    w, h, _ = canvas_px(entry)
    return [[x * w, y * h, ew * w, eh * h] for x, y, ew, eh in entry.get("exclusion", [])]


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def cmd_list(a) -> None:
    data = load()
    rows = []
    for pid, e in data["placements"].items():
        if a.cls and e["class"] != a.cls:
            continue
        hay = " ".join([pid, e["name"], e["platform"], *e.get("aliases", [])]).lower()
        if a.q and a.q.lower() not in hay:
            continue
        size = f"{e['w_mm']}x{e['h_mm']}mm" if e["unit"] == "mm" else f"{e['w']}x{e['h']}"
        rows.append({"id": pid, "name": e["name"], "class": e["class"], "size": size, "aspect": e["aspect"],
                     "max_kb": e.get("max_kb")})
    out({"ok": True, "updated": data["updated"], "verify": data["verify"], "placements": rows})


def cmd_show(a) -> None:
    data = load()
    pid, e = resolve(a.id, data)
    w, h, bleed = canvas_px(e)
    out({"ok": True, "id": pid, **e, "class_rules": class_rules(e, data),
         "canvas_css_px": [round(w, 2), round(h, 2)], "bleed_css_px": round(bleed, 2),
         "safe_rect_css_px": [round(v, 2) for v in safe_rect(e, data)],
         "canvas_meta": f"{e['w_mm']}x{e['h_mm']}mm" if e["unit"] == "mm" else f"{e['w']}x{e['h']}",
         "bleed_meta": f"{e['bleed_mm']}mm" if e["unit"] == "mm" else None})


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("list")
    s.add_argument("--class", dest="cls")
    s.add_argument("--q")
    s.set_defaults(fn=cmd_list)
    s = sub.add_parser("show")
    s.add_argument("id")
    s.set_defaults(fn=cmd_show)
    s = sub.add_parser("rules")
    s.set_defaults(fn=lambda a: out({"ok": True, **load()["rules"]}))
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except Fail as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
