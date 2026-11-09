#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Validate a PawBytes Graphics Suite copy deck ({project}/concept/copy.json).

Checks the schema, the hook ids against the catalog, piece count against the project, that
every string in `mandatory` (legal lines, prices, dates, sponsor names) appears verbatim, and
the words each piece carries against its format's budget: what a viewer reads in the time a
feed, a street or a banner gives them. Headlines of single pieces, covers and fronts also go
through `hooks.py lint`.

Subcommands:
  validate COPY.json [--profile P | --project DIR]   (profile from production.json when --project)
  budgets                                           word budgets per profile and piece role

Output: JSON with fails and warns; exit 1 when something fails. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hooks  # noqa: E402  (bundled beside this script)

TEXT_FIELDS = ("eyebrow", "headline", "subhead", "body", "bullets", "cta")
ROLES = {"single", "cover", "body", "cta", "front", "back"}
# profile -> role -> (hook-lint format, warn above, fail above) total words on the piece, fine print excluded
BUDGETS = {
    "social-post": {"single": ("post", 35, 60)},
    "carousel": {"cover": ("carousel-cover", 15, 25), "body": (None, 30, 60), "cta": (None, 20, 40)},
    "story": {"single": ("story", 25, 40)},
    "poster": {"single": ("poster", 40, 70)},
    "flyer": {"front": ("flyer", 30, 50), "back": (None, 120, 200)},
    "banner": {"single": ("banner", 30, 45)},
    "ad-set": {"single": ("banner", 12, 20)},
    "thumbnail": {"single": ("thumbnail", 7, 12)},
}
WEAK_CTA = ("click here", "learn more", "submit", "read more", "find out more")


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def count(value) -> int:
    if not value:
        return 0
    if isinstance(value, list):
        return sum(count(v) for v in value)
    return len(re.findall(r"[\w'’%$€£#-]+", str(value)))


def validate(copy: dict, profile: str, pieces_expected: int | None) -> tuple[list[str], list[str], list[dict]]:
    fails, warns, lints = [], [], []
    catalog = hooks.load()
    known = hooks.ids(catalog)
    if not str(copy.get("proposition", "")).strip():
        fails.append("proposition is empty: one sentence the viewer must take away")
    if copy.get("goal") not in hooks.GOALS:
        fails.append(f"goal must be one of {', '.join(hooks.GOALS)}")
    hook = copy.get("hook") or {}
    if not hook.get("id"):
        warns.append("no headline hook recorded; pick one from `hooks.py suggest`")
    elif known.get(hook["id"]) != "headline" and hook["id"] != "custom":
        fails.append(f"hook id '{hook['id']}' is not a headline hook in the catalog (or 'custom')")
    vhook = copy.get("visual_hook") or {}
    if vhook.get("id") and known.get(vhook["id"]) != "visual" and vhook["id"] != "custom":
        fails.append(f"visual_hook id '{vhook['id']}' is not a visual hook in the catalog (or 'custom')")
    pieces = copy.get("pieces")
    text = " ".join(str(v) for p in (pieces or []) for f in (*TEXT_FIELDS, "fine_print")
                    for v in (p.get(f) if isinstance(p.get(f), list) else [p.get(f) or ""]))
    for line in copy.get("mandatory", []):
        if str(line) not in text:
            fails.append(f"mandatory copy missing verbatim: {line!r}")
    if not isinstance(pieces, list) or not pieces:
        fails.append("pieces must be a non-empty list")
        return fails, warns, lints
    if pieces_expected and len(pieces) != pieces_expected:
        warns.append(f"{len(pieces)} pieces in the deck; the project expects {pieces_expected} "
                     "(change it with production.py set pieces=N if the deck is right)")
    budgets = BUDGETS.get(profile, BUDGETS["social-post"])
    seen = set()
    for i, piece in enumerate(pieces):
        pid = piece.get("id") or f"#{i + 1}"
        if pid in seen:
            fails.append(f"piece id '{pid}' is used twice")
        seen.add(pid)
        role = piece.get("role")
        if role not in ROLES:
            fails.append(f"{pid}: role '{role}' is not one of {', '.join(sorted(ROLES))}")
            continue
        if role not in budgets:
            warns.append(f"{pid}: role '{role}' is unusual for a {profile} (expected {', '.join(budgets)})")
        fmt, warn_at, fail_at = budgets.get(role, (None, 35, 60))
        head = piece.get("headline")
        if not head and role != "back":
            warns.append(f"{pid}: no headline")
        if head and fmt:
            res = hooks.lint(str(head), fmt, copy.get("goal"))
            lints.append({"piece": pid, **res})
            fails += [f"{pid} headline: {m}" for m in res["fails"]]
            warns += [f"{pid} headline: {m}" for m in res["warns"]]
        elif head and role == "body" and count(head) > 8:
            warns.append(f"{pid}: body-slide headline has {count(head)} words; 8 or fewer scans")
        total = sum(count(piece.get(f)) for f in TEXT_FIELDS)
        if total > fail_at:
            fails.append(f"{pid}: {total} words; a {profile} {role} piece fails above {fail_at} (budget {warn_at})")
        elif total > warn_at:
            warns.append(f"{pid}: {total} words, over the {warn_at}-word budget for a {profile} {role} piece")
        cta = str(piece.get("cta") or "")
        if cta:
            if not 1 <= count(cta) <= 5:
                warns.append(f"{pid}: CTA '{cta}' has {count(cta)} words; 2-5, verb first")
            if cta.lower().strip(" .!") in WEAK_CTA:
                warns.append(f"{pid}: CTA '{cta}' is generic; name the outcome ('Get the checklist')")
        if any("*" in str(piece.get(f) or "") for f in TEXT_FIELDS) and not piece.get("fine_print"):
            warns.append(f"{pid}: an asterisk with no fine_print; the qualifier must sit on the same piece")
    if profile == "carousel":
        if pieces[0].get("role") != "cover":
            warns.append("carousel: the first piece should be the cover")
        if pieces[-1].get("role") != "cta":
            warns.append("carousel: the last piece should carry the single CTA")
    if profile in ("social-post", "story", "banner", "ad-set") and not any(p.get("cta") for p in pieces):
        warns.append(f"no CTA on a {profile}; fine for awareness, otherwise add one action")
    return fails, warns, lints


def cmd_validate(a) -> None:
    path = Path(a.copy)
    if not path.is_file():
        raise Fail(f"no such file: {path}")
    try:
        copy = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Fail(f"{path} is not valid JSON: {exc}")
    profile, expected = a.profile, None
    if a.project:
        manifest = Path(a.project) / "production.json"
        if manifest.is_file():
            data = json.loads(manifest.read_text(encoding="utf-8"))
            profile = profile or data.get("profile")
            expected = data.get("pieces")
    profile = profile or "social-post"
    if profile not in BUDGETS:
        raise Fail(f"unknown profile '{profile}'; profiles are {', '.join(BUDGETS)}")
    fails, warns, lints = validate(copy, profile, expected)
    out({"ok": not fails, "profile": profile, "fails": fails, "warns": warns, "headline_lint": lints},
        0 if not fails else 1)


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("validate")
    s.add_argument("copy")
    s.add_argument("--profile")
    s.add_argument("--project")
    s.set_defaults(fn=cmd_validate)
    s = sub.add_parser("budgets")
    s.set_defaults(fn=lambda a: out({"ok": True, "budgets": {p: {r: {"lint_format": v[0], "warn_above": v[1],
                                     "fail_above": v[2]} for r, v in roles.items()} for p, roles in BUDGETS.items()}}))
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, hooks.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
