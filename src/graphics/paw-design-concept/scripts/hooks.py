#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Hook catalog for PawBytes Graphics Suite: headline formulas, visual hooks, carousel patterns.

Reads ../assets/hooks.json.

Subcommands:
  list     [--kind headline|visual] [--goal G] [--format F]
  show     ID                         one headline or visual hook in full
  suggest  --goal G --format F [--n 5]  ranked headline and visual hooks for this brief
  carousel                            arc, cover patterns, swipe cues, closers
  lint     TEXT --format F [--goal G] headline checks: word band, case, number, question cover,
                                      filler openers, browse-weak phrases

Goals: awareness, engagement, conversion, event, announcement.
Formats: post, carousel-cover, poster, banner, thumbnail, story, flyer.

Output: JSON on stdout; `lint` exits 1 when a check fails. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "assets" / "hooks.json"
GOALS = ["awareness", "engagement", "conversion", "event", "announcement"]
FORMATS = ["post", "carousel-cover", "poster", "banner", "thumbnail", "story", "flyer"]
EVIDENCE_RANK = {"strong": 2, "mixed": 1, "practice": 1}
# headline word bands per format: (min, max); from the 2026-11 research (OOH <=7, carousel covers 6-10 ...)
WORD_BAND = {"post": (3, 10), "carousel-cover": (6, 10), "poster": (2, 7), "banner": (2, 8),
             "thumbnail": (2, 7), "story": (2, 8), "flyer": (2, 8)}
FILLER_OPENERS = ("tips for", "some ", "a few ", "things about", "everything you need", "welcome to", "check out")
BROWSE_WEAK = ("secret", "trick", "hack")


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def load() -> dict:
    if not CATALOG.is_file():
        raise Fail(f"hook catalog not found at {CATALOG}")
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def ids(data: dict | None = None) -> dict[str, str]:
    data = data or load()
    return {**{h["id"]: "headline" for h in data["headline"]}, **{v["id"]: "visual" for v in data["visual"]}}


def lint(text: str, fmt: str, goal: str | None = None) -> dict:
    fails, warns, notes = [], [], []
    words = re.findall(r"[\w'’%$€£#-]+", text)
    lo, hi = WORD_BAND.get(fmt, (2, 10))
    n = len(words)
    if n > hi:
        fails.append(f"{n} words; a {fmt} headline works at {lo}-{hi}. Cut words rather than shrinking type")
    elif n < lo:
        warns.append(f"{n} words; {fmt} headlines usually carry {lo}-{hi}")
    letters = [c for c in text if c.isalpha()]
    if letters and sum(c.isupper() for c in letters) / len(letters) > 0.8 and n > 2:
        warns.append("all caps: caps covers underperformed and Google display asks for sentence case; "
                     "use caps for a short kicker, not the headline")
    has_number = bool(re.search(r"\d", text))
    if fmt in ("carousel-cover", "thumbnail") and not has_number:
        notes.append("no numeral; covers with an honest number did better (use '7', not 'seven')")
    if fmt == "carousel-cover" and text.strip().endswith("?"):
        warns.append("question covers underperformed on carousels; state the promise instead")
    low = text.lower().strip()
    if low.startswith(FILLER_OPENERS):
        warns.append("opens with filler; put the information-carrying words first")
    if any(w in low for w in BROWSE_WEAK) and fmt in ("banner", "post", "story"):
        notes.append("'secret/trick/hack' lost clicks in browse placements; fine in search or saves content")
    if goal == "event" and not re.search(r"\b(mon|tue|wed|thu|fri|sat|sun)[a-z]*\b", low):
        notes.append("event headline without a weekday; keep the date unambiguous on the asset")
    return {"text": text, "format": fmt, "words": n, "band": [lo, hi], "has_number": has_number,
            "ok": not fails, "fails": fails, "warns": warns, "notes": notes}


def _match(entry: dict, goal: str | None, fmt: str | None) -> bool:
    return (not goal or goal in entry.get("goals", [])) and (not fmt or fmt in entry.get("formats", []))


def cmd_list(a) -> None:
    data = load()
    res = {}
    for kind in ("headline", "visual"):
        if a.kind and a.kind != kind:
            continue
        res[kind] = [{"id": e["id"], "name": e["name"], **({"template": e["template"]} if kind == "headline"
                     else {"device": e["device"]})} for e in data[kind] if _match(e, a.goal, a.format)]
    out({"ok": True, "defaults": data["defaults"], **res})


def cmd_show(a) -> None:
    data = load()
    for kind in ("headline", "visual"):
        for e in data[kind]:
            if e["id"] == a.id:
                out({"ok": True, "kind": kind, **e})
    raise Fail(f"no hook '{a.id}'; run `hooks.py list`")


def cmd_suggest(a) -> None:
    data = load()

    def score(e: dict) -> int:
        s = (3 if a.goal in e.get("goals", []) else 0) + (3 if a.format in e.get("formats", []) else 0)
        return s + EVIDENCE_RANK.get(e.get("evidence", "practice"), 0)

    head = sorted((e for e in data["headline"] if _match(e, None, a.format) or _match(e, a.goal, None)),
                  key=score, reverse=True)[: a.n]
    vis = sorted((e for e in data["visual"] if _match(e, None, a.format) or _match(e, a.goal, None)),
                 key=lambda e: (a.goal in e["goals"]) + (a.format in e["formats"]), reverse=True)[: a.n]
    out({"ok": True, "goal": a.goal, "format": a.format, "defaults": data["defaults"],
         "headline": [{"id": e["id"], "template": e["template"], "example": e["example"], "use_when": e["use_when"],
                       "pitfall": e["pitfall"], "evidence": e["evidence"]} for e in head],
         "visual": [{"id": e["id"], "device": e["device"], "works_when": e["works_when"],
                     "backfires_when": e["backfires_when"]} for e in vis]})


def cmd_lint(a) -> None:
    res = lint(a.text, a.format, a.goal)
    out({"ok": res["ok"], **res}, 0 if res["ok"] else 1)


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("list")
    s.add_argument("--kind", choices=["headline", "visual"])
    s.add_argument("--goal", choices=GOALS)
    s.add_argument("--format", choices=FORMATS)
    s.set_defaults(fn=cmd_list)
    s = sub.add_parser("show")
    s.add_argument("id")
    s.set_defaults(fn=cmd_show)
    s = sub.add_parser("suggest")
    s.add_argument("--goal", required=True, choices=GOALS)
    s.add_argument("--format", required=True, choices=FORMATS)
    s.add_argument("--n", type=int, default=5)
    s.set_defaults(fn=cmd_suggest)
    s = sub.add_parser("carousel")
    s.set_defaults(fn=lambda a: out({"ok": True, **load()["carousel"]}))
    s = sub.add_parser("lint")
    s.add_argument("text")
    s.add_argument("--format", required=True, choices=FORMATS)
    s.add_argument("--goal", choices=GOALS)
    s.set_defaults(fn=cmd_lint)
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
