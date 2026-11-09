#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Graphic style catalog and style lock for PawBytes Graphics Suite.

Catalogs: ../assets/graphic-styles.json (looks) and ../assets/type-pairings.json (Google Fonts).
The lock, {project}/style/style-lock.json, is what every later stage reads; tokens.css turns it
into CSS variables and font imports that design HTML links.

Subcommands:
  list      [--fits GOAL] [--kind photo|illustration|3d|collage|type-only|screenshot]
  search    TEXT                       ids, names and aliases ("swiss", "y2k", "luxury")
  show      ID                         a style with its default pairing
  pairings  [--q TEXT]
  lock      --project DIR --style ID [--pairing ID] [--palette bg=#..,accent=#..]
            [--display "Family:700,800"] [--text "Family:400,600"] [--font-source google|local]
            [--font-file WEIGHT=brand/fonts/x.woff2 ...] [--scale 1.333] [--headline-case sentence]
            [--imagery-kind K] [--notes TEXT] [--reference PATH ...]
  validate  LOCK.json                  required fields, hex colours, palette contrast
  contrast  FG BG                      WCAG ratio of two hex colours
  css       --project DIR              write style/tokens.css from the lock
  tile      --project DIR [--headline TEXT]   write style/style-tile.html (render it with render.py)

`lock` refuses while the style gate is blocked (earlier stages not approved or skipped).
Output: JSON on stdout; `validate` exits 1 on problems. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import production  # noqa: E402  (bundled beside this script)

ASSETS = Path(__file__).resolve().parent.parent / "assets"
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
ROLES = ("bg", "ink", "accent", "muted", "on_accent")
PAIRS = (("ink", "bg", 4.5), ("on_accent", "accent", 4.5), ("muted", "bg", 3.0))
KINDS = ("photo", "illustration", "3d", "collage", "type-only", "screenshot")


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def catalog(name: str) -> dict:
    return json.loads((ASSETS / name).read_text(encoding="utf-8"))


def styles() -> list[dict]:
    return catalog("graphic-styles.json")["styles"]


def pairings() -> list[dict]:
    return catalog("type-pairings.json")["pairings"]


def find(items: list[dict], key: str, what: str) -> dict:
    for it in items:
        if it["id"] == key:
            return it
    raise Fail(f"no {what} '{key}'; run `styles.py {'search' if what == 'style' else 'pairings'}`")


def luminance(hexcol: str) -> float:
    h = hexcol.lstrip("#")
    vals = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in vals]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    return round((max(la, lb) + 0.05) / (min(la, lb) + 0.05), 2)


def validate_lock(lock: dict) -> tuple[list[str], list[str]]:
    problems, warns = [], []
    for key in ("style", "type", "palette", "imagery", "layout"):
        if key not in lock:
            problems.append(f"missing '{key}'")
    if problems:
        return problems, warns
    pal = lock["palette"]
    for role in ROLES:
        if not HEX.match(str(pal.get(role, ""))):
            problems.append(f"palette.{role} must be #RRGGBB, got {pal.get(role)!r}")
    for i, c in enumerate(pal.get("extra", [])):
        if not HEX.match(str(c)):
            problems.append(f"palette.extra[{i}] must be #RRGGBB, got {c!r}")
    if not problems:
        for fg, bg, need in PAIRS:
            r = ratio(pal[fg], pal[bg])
            if r < need:
                problems.append(f"{fg} on {bg} is {r}:1; needs {need}:1 (derive a darker or lighter tint, "
                                "and keep the brand hex for fills)")
    t = lock["type"]
    for slot in ("display", "text"):
        fam = (t.get(slot) or {})
        if not fam.get("family"):
            problems.append(f"type.{slot}.family is empty")
        if fam.get("source") == "local" and not fam.get("files"):
            problems.append(f"type.{slot} is local but lists no font files")
        if not fam.get("weights"):
            warns.append(f"type.{slot} lists no weights")
    try:
        if not 1.1 <= float(t.get("scale", 1.333)) <= 1.8:
            warns.append("type.scale outside 1.1-1.8; 1.25 dense, 1.333 general, 1.5 bold social, 1.618 posters")
    except (TypeError, ValueError):
        problems.append("type.scale must be a number")
    if lock["imagery"].get("kind") not in KINDS:
        problems.append(f"imagery.kind must be one of {', '.join(KINDS)}")
    return problems, warns


def _parse_family(value: str | None) -> tuple[str, list[int]] | None:
    if not value:
        return None
    fam, _, weights = value.partition(":")
    ws = [int(w) for w in re.split(r"[;,\s]+", weights) if w.strip()] if weights else [400, 700]
    return fam.strip(), ws


def cmd_lock(a) -> None:
    project = Path(a.project)
    reasons = production.stage_gate(project, "style")
    if reasons:
        out({"ok": False, "blocked": True, "stage": "style", "reasons": reasons}, 1)
    st = find(styles(), a.style, "style")
    pr = find(pairings(), a.pairing or st["pairing"], "pairing")
    palette = dict(st["palette"])
    palette["extra"] = list(palette.get("extra", []))
    if a.palette:
        for pair in a.palette.split(","):
            if "=" not in pair:
                raise Fail(f"--palette takes role=#hex pairs, got '{pair}'")
            k, v = pair.split("=", 1)
            k = k.strip()
            if k == "extra":
                palette["extra"].append(v.strip())
            elif k in ROLES:
                palette[k] = v.strip()
            else:
                raise Fail(f"palette role '{k}' is not one of {', '.join(ROLES)}, extra")
    type_block = {"display": dict(pr["display"]), "text": dict(pr["text"]), "pairing": pr["id"],
                  "scale": a.scale, "headline_case": a.headline_case or st.get("headline_case", "sentence"),
                  "caps_tracking_em": 0.06}
    for slot, value in (("display", a.display), ("text", a.text)):
        parsed = _parse_family(value)
        if parsed:
            type_block[slot] = {"family": parsed[0], "weights": parsed[1], "source": a.font_source}
    if a.font_file:
        files = {}
        for item in a.font_file:
            w, _, path = item.partition("=")
            files[w.strip()] = path.strip()
        for slot in ("display", "text"):
            if type_block[slot].get("source") == "local":
                type_block[slot]["files"] = {w: p for w, p in files.items()
                                             if int(w) in type_block[slot]["weights"]} or files
    imagery = dict(st["imagery"])
    if a.imagery_kind:
        imagery["kind"] = a.imagery_kind
    lock = {"style": {"id": st["id"], "name": st["name"]}, "type": type_block, "palette": palette,
            "imagery": imagery, "layout": dict(st["layout"]), "pitfalls": list(st.get("pitfalls", [])),
            "custom_notes": a.notes or "", "references": a.reference or [],
            "locked_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat()}
    problems, warns = validate_lock(lock)
    if problems:
        out({"ok": False, "problems": problems, "warnings": warns}, 1)
    dest = project / "style" / "style-lock.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tokens = write_css(project, lock)
    out({"ok": True, "lock": str(dest), "tokens": str(tokens), "warnings": warns,
         "contrast": {f"{fg}/{bg}": ratio(palette[fg], palette[bg]) for fg, bg, _ in PAIRS}})


def google_url(lock: dict) -> str | None:
    fams: dict[str, set[int]] = {}
    for slot in ("display", "text"):
        f = lock["type"][slot]
        if f.get("source", "google") == "google":
            fams.setdefault(f["family"], set()).update(int(w) for w in f.get("weights") or [400])
    if not fams:
        return None
    parts = [f"family={urllib.parse.quote_plus(name)}:wght@{';'.join(str(w) for w in sorted(ws))}"
             for name, ws in sorted(fams.items())]
    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=block"


def write_css(project: Path, lock: dict) -> Path:
    t, p, lay = lock["type"], lock["palette"], lock["layout"]
    lines = ["/* Generated by styles.py css from style-lock.json. Edit the lock, not this file. */"]
    url = google_url(lock)
    if url:
        lines.append(f"@import url('{url}');")
    for slot in ("display", "text"):
        f = t[slot]
        if f.get("source") == "local":
            for weight, path in (f.get("files") or {}).items():
                rel = Path("..") / path  # tokens.css sits in style/; font paths are project-relative
                fmt = {".woff2": "woff2", ".woff": "woff", ".ttf": "truetype", ".otf": "opentype"}.get(
                    Path(path).suffix.lower(), "woff2")
                lines.append(f"@font-face{{font-family:'{f['family']}';src:url('{rel.as_posix()}') format('{fmt}');"
                             f"font-weight:{weight};font-display:block}}")
    dw = max(t["display"].get("weights") or [700])
    tw = min(t["text"].get("weights") or [400])
    tws = max(t["text"].get("weights") or [600])
    extra = "".join(f"--extra-{i + 1}:{c};" for i, c in enumerate(p.get("extra", [])))
    case = {"upper": "uppercase", "sentence": "none", "as written": "none"}.get(t.get("headline_case"), "none")
    lines += [
        ":root{"
        f"--bg:{p['bg']};--ink:{p['ink']};--accent:{p['accent']};--muted:{p['muted']};--on-accent:{p['on_accent']};{extra}"
        f"--font-display:'{t['display']['family']}',system-ui,sans-serif;--font-text:'{t['text']['family']}',system-ui,sans-serif;"
        f"--w-display:{dw};--w-text:{tw};--w-strong:{tws};--scale:{t.get('scale', 1.333)};"
        f"--radius:{lay.get('corner_radius_px', 0)}px;--margin-pct:{lay.get('margin_pct', 6)};"
        f"--caps-tracking:{t.get('caps_tracking_em', 0.06)}em;--headline-case:{case}"
        "}",
        "body{background:var(--bg);color:var(--ink);font-family:var(--font-text);font-weight:var(--w-text);"
        "-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;font-kerning:normal}",
        "[data-role=headline]{font-family:var(--font-display);font-weight:var(--w-display);line-height:1.02;"
        f"letter-spacing:-0.015em;text-wrap:balance;text-transform:{case}}}",
        "[data-role=subhead]{font-weight:var(--w-strong);line-height:1.2;text-wrap:balance}",
        "[data-role=body],[data-role=bullets]{line-height:1.35;text-wrap:pretty}",
        "[data-role=bullets] ul{margin:0;padding-left:1.1em}",
        "[data-role=eyebrow]{text-transform:uppercase;letter-spacing:var(--caps-tracking);font-weight:var(--w-strong)}",
        "[data-role=cta]{display:flex;align-items:center;justify-content:center;background:var(--accent);"
        "color:var(--on-accent);font-weight:var(--w-strong);border-radius:var(--radius)}",
        "[data-role=fine_print]{color:var(--muted);line-height:1.3}",
        "[data-role=badge]{display:flex;align-items:center;justify-content:center;background:var(--ink);"
        "color:var(--bg);font-weight:var(--w-strong);border-radius:999px}",
    ]
    dest = project / "style" / "tokens.css"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


def _load_lock(project: Path) -> dict:
    path = project / "style" / "style-lock.json"
    if not path.is_file():
        raise Fail(f"no style lock at {path}; run `styles.py lock` first")
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_tile(a) -> None:
    project = Path(a.project)
    lock = _load_lock(project)
    write_css(project, lock)
    headline = a.headline
    copy_path = project / "concept" / "copy.json"
    if not headline and copy_path.is_file():
        copy = json.loads(copy_path.read_text(encoding="utf-8"))
        first = (copy.get("pieces") or [{}])[0]
        headline = (copy.get("hook") or {}).get("text") or first.get("headline")
        sub = first.get("subhead") or first.get("body") or ""
        cta = first.get("cta") or "Get started"
    else:
        sub, cta = "Supporting line in the text face, set at body size.", "Call to action"
    headline = headline or "The headline in the display face"
    p = lock["palette"]
    swatches = "".join(
        f'<div class="sw" style="background:{p[r]}"><b style="color:{p["ink"] if r != "ink" else p["bg"]}">'
        f'{r}<br>{p[r]}</b></div>' for r in ROLES) + "".join(
        f'<div class="sw" style="background:{c}"><b style="color:{p["ink"]}">extra<br>{c}</b></div>'
        for c in p.get("extra", []))
    pairs = " · ".join(f"{fg}/{bg} {ratio(p[fg], p[bg])}:1" for fg, bg, _ in PAIRS)
    t = lock["type"]
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><meta name="canvas" content="1600x1000">
<link rel="stylesheet" href="tokens.css">
<style>
html,body{{margin:0;width:1600px;height:1000px;overflow:hidden}}
body{{position:relative}}
.h{{position:absolute;left:96px;top:88px;width:1000px;font-size:96px}}
.s{{position:absolute;left:96px;top:420px;width:900px;font-size:40px}}
.c{{position:absolute;left:96px;top:560px;width:380px;height:96px;font-size:34px}}
.meta{{position:absolute;left:96px;bottom:72px;width:1000px;font-size:24px;color:var(--muted)}}
.pal{{position:absolute;right:96px;top:88px;width:340px;display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.sw{{height:120px;border-radius:var(--radius);display:flex;align-items:flex-end;padding:12px;box-sizing:border-box;
   outline:1px solid rgba(0,0,0,.08)}}
.sw b{{font:600 18px/1.2 var(--font-text)}}
</style></head><body>
<div class="h" data-role="headline" data-id="headline">{html.escape(headline)}</div>
<div class="s" data-role="body" data-id="body">{html.escape(sub)}</div>
<div class="c" data-role="cta" data-id="cta">{html.escape(cta)}</div>
<div class="meta" data-role="fine_print" data-id="meta">{html.escape(lock['style']['name'])} · {html.escape(t['display']['family'])}
 / {html.escape(t['text']['family'])} · scale {t.get('scale')} · {html.escape(pairs)}<br>
Imagery: {html.escape(lock['imagery'].get('kind', ''))}, {html.escape(lock['imagery'].get('treatment', ''))}</div>
<div class="pal">{swatches}</div>
</body></html>
"""
    dest = project / "style" / "style-tile.html"
    dest.write_text(doc, encoding="utf-8")
    out({"ok": True, "tile": str(dest), "next": "render.py render style/style-tile.html --measure; "
         "fonts_missing must be empty"})


def cmd_list(a) -> None:
    rows = [{"id": s["id"], "name": s["name"], "what": s["what"], "imagery": s["imagery"]["kind"],
             "pairing": s["pairing"], "fits": s["fits"]} for s in styles()
            if (not a.fits or a.fits in s["fits"]) and (not a.kind or s["imagery"]["kind"] == a.kind)]
    out({"ok": True, "styles": rows})


def cmd_search(a) -> None:
    q = a.text.lower()
    hits = [{"id": s["id"], "name": s["name"], "what": s["what"]} for s in styles()
            if q in s["id"] or q in s["name"].lower() or any(q in al for al in s["aliases"])
            or q in s["what"].lower()]
    out({"ok": True, "query": a.text, "styles": hits})


def cmd_show(a) -> None:
    st = find(styles(), a.id, "style")
    out({"ok": True, **st, "pairing_detail": find(pairings(), st["pairing"], "pairing")})


def cmd_pairings(a) -> None:
    q = (a.q or "").lower()
    out({"ok": True, "pairings": [p for p in pairings() if not q or q in json.dumps(p).lower()]})


def cmd_validate(a) -> None:
    lock = json.loads(Path(a.lock).read_text(encoding="utf-8"))
    problems, warns = validate_lock(lock)
    out({"ok": not problems, "problems": problems, "warnings": warns}, 0 if not problems else 1)


def cmd_contrast(a) -> None:
    for c in (a.fg, a.bg):
        if not HEX.match(c):
            raise Fail(f"colours must be #RRGGBB, got {c}")
    r = ratio(a.fg, a.bg)
    out({"ok": True, "ratio": r, "normal_text": r >= 4.5, "large_text": r >= 3.0})


def cmd_css(a) -> None:
    project = Path(a.project)
    out({"ok": True, "tokens": str(write_css(project, _load_lock(project)))})


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("list")
    s.add_argument("--fits")
    s.add_argument("--kind", choices=KINDS)
    s.set_defaults(fn=cmd_list)
    s = sub.add_parser("search")
    s.add_argument("text")
    s.set_defaults(fn=cmd_search)
    s = sub.add_parser("show")
    s.add_argument("id")
    s.set_defaults(fn=cmd_show)
    s = sub.add_parser("pairings")
    s.add_argument("--q")
    s.set_defaults(fn=cmd_pairings)
    s = sub.add_parser("lock")
    s.add_argument("--project", required=True)
    s.add_argument("--style", required=True)
    s.add_argument("--pairing")
    s.add_argument("--palette", help="role=#hex pairs, comma-separated; extra=#hex appends")
    s.add_argument("--display", help='brand display face, "Family:700,800"')
    s.add_argument("--text", help='brand text face, "Family:400,600"')
    s.add_argument("--font-source", choices=["google", "local"], default="google")
    s.add_argument("--font-file", action="append", help="WEIGHT=project-relative path, for local fonts")
    s.add_argument("--scale", type=float, default=1.333)
    s.add_argument("--headline-case", choices=["sentence", "upper", "as written"])
    s.add_argument("--imagery-kind", choices=KINDS)
    s.add_argument("--notes")
    s.add_argument("--reference", action="append")
    s.set_defaults(fn=cmd_lock)
    s = sub.add_parser("validate")
    s.add_argument("lock")
    s.set_defaults(fn=cmd_validate)
    s = sub.add_parser("contrast")
    s.add_argument("fg")
    s.add_argument("bg")
    s.set_defaults(fn=cmd_contrast)
    s = sub.add_parser("css")
    s.add_argument("--project", required=True)
    s.set_defaults(fn=cmd_css)
    s = sub.add_parser("tile")
    s.add_argument("--project", required=True)
    s.add_argument("--headline")
    s.set_defaults(fn=cmd_tile)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, production.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
