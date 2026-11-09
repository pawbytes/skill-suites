#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10"]
# ///
"""Layout frames for PawBytes Graphics Suite: validate layout.json, write greybox wireframes,
scaffold design HTML, and tile renders into a contact sheet.

A frame is one canvas: a piece (p01, s03, front) at a placement (instagram-feed-portrait).
Element boxes are [x, y, w, h] fractions of the trim (the finished piece). On print, image
and shape elements that touch an edge run on into the bleed by themselves.

Type sizes come from the placement class's body floor and the style lock's scale ratio
(`size`: display, headline, title, subhead, body, small; role defaults otherwise), or an
explicit `size_px` (`size_pt` on print). Greyboxes use them too, so a wireframe that
overflows predicts a design that overflows: cut copy or grow the box.

Subcommands:
  validate LAYOUT [--copy concept/copy.json] [--assets imagery/assets.json] [--project DIR]
  schema                              the layout.json shape: keys, roles, size steps
  greybox  LAYOUT --out-dir DIR [--copy F] [--lock style/style-lock.json] [--frame ID]
  scaffold LAYOUT --frame ID --out compose/<frame>/design.html [--copy F] [--assets F]
           [--lock F] [--tokens style/tokens.css] [--project DIR]
  sheet    PNG [PNG ...] --out sheet.png [--cols 4] [--width 1600]

Paths inside layout.json, copy.json and assets.json are project-relative; --project
(default: the folder above the layout's folder) resolves them.

Output: JSON on stdout. `validate` exits 1 with problems. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import specs  # noqa: E402  (bundled beside this script)

ROLES = {"eyebrow", "headline", "subhead", "body", "bullets", "cta", "fine_print", "logo", "image", "shape", "badge"}
TEXT_ROLES = {"eyebrow", "headline", "subhead", "body", "bullets", "cta", "fine_print", "badge"}
KEEP_INSIDE = TEXT_ROLES | {"logo"}
ROLE_SIZE = {"headline": "headline", "subhead": "subhead", "body": "body", "bullets": "body", "cta": "subhead",
             "eyebrow": "small", "fine_print": "small", "badge": "small"}
STEPS = {"display": 4, "headline": 3, "title": 2, "subhead": 1, "body": 0, "small": -1}
GREY = {"headline": "#1f6feb", "subhead": "#8250df", "body": "#57606a", "bullets": "#57606a", "cta": "#cf222e",
        "eyebrow": "#9a6700", "fine_print": "#6e7781", "logo": "#1a7f37", "image": "#bf8700", "shape": "#8c959f",
        "badge": "#bc4c00"}


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def read_json(path: Path | None) -> dict | None:
    if not path:
        return None
    if not path.is_file():
        raise Fail(f"no such file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Fail(f"{path} is not valid JSON: {exc}")


def copy_value(copy: dict | None, ref: str | None):
    if not copy or not ref or "." not in ref:
        return None
    piece_id, field = ref.split(".", 1)
    for piece in copy.get("pieces", []):
        if piece.get("id") == piece_id:
            return piece.get(field)
    return None


def geometry(entry: dict) -> dict:
    w, h, bleed = specs.canvas_px(entry)
    return {"w": w, "h": h, "bleed": bleed, "trim_w": w - 2 * bleed, "trim_h": h - 2 * bleed,
            "meta": f"{entry['w_mm']}x{entry['h_mm']}mm" if entry["unit"] == "mm" else f"{entry['w']}x{entry['h']}",
            "bleed_meta": f"{entry['bleed_mm']}mm" if entry["unit"] == "mm" and entry.get("bleed_mm") else None}


def box_px(el: dict, g: dict) -> list[float]:
    x, y, w, h = el["box"]
    left, top = g["bleed"] + x * g["trim_w"], g["bleed"] + y * g["trim_h"]
    right, bottom = left + w * g["trim_w"], top + h * g["trim_h"]
    if g["bleed"] and el.get("role") in ("image", "shape"):  # full-bleed art runs into the bleed
        left = 0 if x <= 0.001 else left
        top = 0 if y <= 0.001 else top
        right = g["w"] if x + w >= 0.999 else right
        bottom = g["h"] if y + h >= 0.999 else bottom
    return [left, top, right - left, bottom - top]


def type_px(el: dict, entry: dict, data: dict, ratio: float) -> float:
    if el.get("size_px"):
        return float(el["size_px"])
    if el.get("size_pt"):
        return float(el["size_pt"]) / 0.75
    cls = specs.class_rules(entry, data)
    if entry["unit"] == "mm":
        base = cls["body_pt"] / 0.75
        floor = cls["min_pt"] / 0.75
    else:
        scale = (entry["w"] / cls["ref_width"]) if cls.get("ref_width") else 1.0
        base, floor = cls["body_px"] * scale, cls["min_px"] * scale
    step = STEPS.get(el.get("size") or ROLE_SIZE.get(el.get("role"), "body"), 0)
    return round(max(floor, base * ratio ** step), 1)


def validate(layout: dict, copy: dict | None, assets: dict | None, data: dict) -> tuple[list[str], list[str]]:
    problems, warns = [], []
    frames = layout.get("frames")
    if not isinstance(frames, list) or not frames:
        return ["layout.json needs a non-empty `frames` list"], []
    seen = set()
    for fr in frames:
        fid = fr.get("id") or "?"
        if fid in seen:
            problems.append(f"frame id '{fid}' is used twice")
        seen.add(fid)
        try:
            pid, entry = specs.resolve(fr.get("placement", ""), data)
        except specs.Fail as exc:
            problems.append(f"{fid}: {exc}")
            continue
        if fr.get("placement") != pid:
            warns.append(f"{fid}: placement '{fr.get('placement')}' resolves to '{pid}'; write the id")
        g = geometry(entry)
        rect = specs.safe_rect(entry, data)
        ids, texts, has_headline = set(), [], False
        for el in fr.get("elements", []):
            eid = el.get("id") or "?"
            where = f"{fid}/{eid}"
            if eid in ids:
                problems.append(f"{where}: element id used twice in the frame")
            ids.add(eid)
            if el.get("role") not in ROLES:
                problems.append(f"{where}: role '{el.get('role')}' is not one of {', '.join(sorted(ROLES))}")
                continue
            box = el.get("box")
            if not (isinstance(box, list) and len(box) == 4 and all(isinstance(v, (int, float)) for v in box)):
                problems.append(f"{where}: box must be [x, y, w, h] fractions")
                continue
            x, y, w, h = box
            if min(x, y) < -0.001 or w <= 0 or h <= 0 or x + w > 1.001 or y + h > 1.001:
                problems.append(f"{where}: box {box} leaves the frame (fractions 0..1, x+w and y+h <= 1)")
                continue
            px = box_px(el, g)
            if el["role"] in KEEP_INSIDE:
                l, t, r, b = rect
                if px[0] < l - 1 or px[1] < t - 1 or px[0] + px[2] > r + 1 or px[1] + px[3] > b + 1:
                    problems.append(f"{where}: {el['role']} crosses the {pid} safe zone "
                                    f"(keep inside x {l / g['w']:.3f}-{r / g['w']:.3f}, y {t / g['h']:.3f}-{b / g['h']:.3f})")
            if el["role"] == "headline":
                has_headline = True
            if el["role"] in TEXT_ROLES:
                texts.append((eid, px))
                if not el.get("text") and not el.get("copy"):
                    problems.append(f"{where}: text element needs `copy` (piece.field) or `text`")
                elif el.get("copy") and copy is not None and not copy_value(copy, el["copy"]):
                    problems.append(f"{where}: copy '{el['copy']}' is missing or empty in copy.json")
            if el["role"] in ("image", "logo") and not (el.get("asset") or el.get("src")):
                warns.append(f"{where}: {el['role']} has no `asset` (imagery picks it) or `src`")
            if assets is not None and el.get("asset") and el["asset"] not in assets.get("assets", {}):
                problems.append(f"{where}: asset '{el['asset']}' is not picked in imagery/assets.json")
        if not has_headline:
            warns.append(f"{fid}: no headline element; the hook needs a home")
        for i, (a_id, a) in enumerate(texts):
            for b_id, b in texts[i + 1:]:
                if a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]:
                    warns.append(f"{fid}: text boxes {a_id} and {b_id} overlap")
    if copy:
        placed = {el.get("copy") for fr in frames for el in fr.get("elements", [])}
        for piece in copy.get("pieces", []):
            for field in ("headline", "subhead", "body", "cta", "fine_print"):
                if piece.get(field) and f"{piece['id']}.{field}" not in placed:
                    warns.append(f"copy {piece['id']}.{field} is not placed in any frame")
    return problems, warns


def _ratio(lock: dict | None) -> float:
    try:
        return float((lock or {}).get("type", {}).get("scale") or 1.333)
    except (TypeError, ValueError):
        return 1.333


def _text_html(el: dict, copy: dict | None) -> str:
    value = el.get("text") if el.get("text") is not None else copy_value(copy, el.get("copy"))
    if value is None:
        value = f"[{el.get('copy') or el.get('role')}]"
    if isinstance(value, list):
        return "<ul>" + "".join(f"<li>{html.escape(str(v))}</li>" for v in value) + "</ul>"
    return html.escape(str(value)).replace("\n", "<br>")


def _frame(layout: dict, frame_id: str) -> dict:
    for fr in layout.get("frames", []):
        if fr.get("id") == frame_id:
            return fr
    raise Fail(f"no frame '{frame_id}' in layout; frames are {[f.get('id') for f in layout.get('frames', [])]}")


def _pos(px: list[float]) -> str:
    return f"left:{px[0]:.2f}px;top:{px[1]:.2f}px;width:{px[2]:.2f}px;height:{px[3]:.2f}px"


def greybox_html(fr: dict, entry: dict, data: dict, copy: dict | None, lock: dict | None) -> str:
    g = geometry(entry)
    ratio = _ratio(lock)
    rect = specs.safe_rect(entry, data)
    parts = []
    for el in fr.get("elements", []):
        px = box_px(el, g)
        role = el.get("role", "shape")
        color = GREY.get(role, "#8c959f")
        label = f"<span class=lbl>{html.escape(el.get('id', role))} · {role}</span>"
        if role in TEXT_ROLES:
            size = type_px(el, entry, data, ratio)
            align = el.get("align", "left")
            parts.append(f'<div class="el txt" data-role="{role}" data-id="{html.escape(el.get("id", role))}" '
                         f'style="{_pos(px)};font-size:{size}px;text-align:{align};border-color:{color}">'
                         f'{_text_html(el, copy)}</div>')
            parts.append(f'<div class="tag" style="left:{px[0]:.1f}px;top:{px[1]:.1f}px;color:{color}">{label}</div>')
        else:
            parts.append(f'<div class="el box" style="{_pos(px)};border-color:{color};background:{color}22">'
                         f'{label}<span class=asset>{html.escape(str(el.get("asset") or el.get("src") or ""))}</span></div>')
    safe = (f'<div class="safe" style="left:{rect[0]:.1f}px;top:{rect[1]:.1f}px;'
            f'width:{rect[2] - rect[0]:.1f}px;height:{rect[3] - rect[1]:.1f}px"></div>')
    trim = ""
    if g["bleed"]:
        trim = (f'<div class="trim" style="left:{g["bleed"]:.1f}px;top:{g["bleed"]:.1f}px;'
                f'width:{g["trim_w"]:.1f}px;height:{g["trim_h"]:.1f}px"></div>')
    bleed_meta = f'<meta name="bleed" content="{g["bleed_meta"]}">' if g["bleed_meta"] else ""
    lbl_px = max(10, round(g["w"] / 90))
    return f"""<!doctype html><html><head><meta charset="utf-8"><meta name="canvas" content="{g['meta']}">{bleed_meta}
<meta name="placement" content="{html.escape(fr.get('placement', ''))}"><meta name="frame" content="{html.escape(fr.get('id', ''))}">
<title>{html.escape(fr.get('id', ''))} greybox</title>
<style>
html,body{{margin:0;padding:0;width:{g['w']:.2f}px;height:{g['h']:.2f}px;overflow:hidden}}
body{{position:relative;background:#f6f8fa;font-family:Arial,Helvetica,sans-serif;color:#24292f}}
.el{{position:absolute;box-sizing:border-box;border:2px dashed;overflow:hidden}}
.txt{{line-height:1.15;font-weight:700;overflow-wrap:break-word}}
.txt[data-role=body],.txt[data-role=bullets],.txt[data-role=fine_print]{{font-weight:400;line-height:1.35}}
.txt ul{{margin:0;padding-left:1.1em}}
.tag{{position:absolute;transform:translateY(-100%);font-size:{lbl_px}px;white-space:nowrap}}
.box .lbl,.box .asset{{display:block;padding:4px 6px;font-size:{lbl_px}px}}
.safe{{position:absolute;outline:2px solid #2da44e;outline-offset:0;pointer-events:none}}
.trim{{position:absolute;outline:1px solid #cf222e;pointer-events:none}}
</style></head><body>
{''.join(parts)}
{safe}{trim}
</body></html>
"""


def _rel(target: Path, start: Path) -> str:
    return Path(os.path.relpath(target, start)).as_posix()


def scaffold_html(fr: dict, entry: dict, data: dict, copy: dict | None, assets: dict | None, lock: dict | None,
                  tokens: Path | None, out_path: Path, project: Path) -> str:
    g = geometry(entry)
    ratio = _ratio(lock)
    base = out_path.parent
    rules, parts = [], []
    for el in fr.get("elements", []):
        px = box_px(el, g)
        eid = el.get("id") or el.get("role")
        role = el.get("role", "shape")
        sel = f'[data-id="{eid}"]'
        css = [_pos(px)]
        if role in TEXT_ROLES:
            css.append(f"font-size:{type_px(el, entry, data, ratio)}px")
            if el.get("align"):
                css.append(f"text-align:{el['align']}")
            body = _text_html(el, copy)
            parts.append(f'<div class="el" data-role="{role}" data-id="{html.escape(eid)}">{body}</div>')
        elif role in ("image", "logo"):
            src = el.get("src")
            if el.get("asset") and assets and el["asset"] in assets.get("assets", {}):
                src = assets["assets"][el["asset"]].get("path")
            src_attr = _rel(project / src, base) if src else ""
            fit = el.get("fit", "cover" if role == "image" else "contain")
            focal = el.get("focal") or [0.5, 0.5]
            css.append(f"object-fit:{fit};object-position:{focal[0] * 100:.0f}% {focal[1] * 100:.0f}%")
            alt = html.escape(el.get("alt", ""))
            parts.append(f'<img class="el" data-role="{role}" data-id="{html.escape(eid)}" src="{src_attr}" alt="{alt}">')
        else:
            fill = el.get("fill", "accent")
            css.append(f"background:{fill if str(fill).startswith('#') else f'var(--{fill})'}")
            if el.get("radius") is not None:
                css.append(f"border-radius:{el['radius']}px")
            parts.append(f'<div class="el" data-role="shape" data-id="{html.escape(eid)}"></div>')
        rules.append(f"{sel}{{{';'.join(css)}}}")
    link = f'<link rel="stylesheet" href="{_rel(tokens, base)}">' if tokens else ""
    bleed_meta = f'<meta name="bleed" content="{g["bleed_meta"]}">' if g["bleed_meta"] else ""
    return f"""<!doctype html>
<html lang="{html.escape((copy or {}).get('language', 'en'))}"><head><meta charset="utf-8">
<meta name="canvas" content="{g['meta']}">{bleed_meta}
<meta name="placement" content="{html.escape(fr.get('placement', ''))}"><meta name="frame" content="{html.escape(fr.get('id', ''))}">
<title>{html.escape(fr.get('id', ''))}</title>
{link}
<style>
html,body{{margin:0;padding:0;width:{g['w']:.2f}px;height:{g['h']:.2f}px;overflow:hidden}}
body{{position:relative}}
.el{{position:absolute;box-sizing:border-box;margin:0}}
/* positions from layout/layout.json ({fr.get('pattern', 'custom')}); refine type, colour and treatment below */
{chr(10).join(rules)}
</style></head><body>
{chr(10).join(parts)}
</body></html>
"""


def coverage(layout: dict, manifest: dict, copy: dict | None, data: dict) -> tuple[list[str], list[str]]:
    """Every copy piece has a frame at every project placement, with the <piece>--<placement> id."""
    problems, warns = [], []
    placements = [specs.resolve(p, data)[0] for p in manifest.get("placements", [])]
    pieces = [p["id"] for p in (copy or {}).get("pieces", [])]
    have = {(fr.get("piece"), fr.get("placement")) for fr in layout.get("frames", [])}
    for fr in layout.get("frames", []):
        want = f"{fr.get('piece')}--{fr.get('placement')}"
        if fr.get("id") != want:
            problems.append(f"frame id '{fr.get('id')}' should be '{want}' (exports and folders are named from it)")
        if fr.get("placement") not in placements:
            warns.append(f"{fr.get('id')}: placement {fr.get('placement')} is not in the project's placements "
                         "(add it with production.py set placements=...)")
    for piece in pieces:
        for pid in placements:
            if (piece, pid) not in have:
                problems.append(f"no frame for piece {piece} at {pid}")
    return problems, warns


def cmd_validate(a) -> None:
    data = specs.load()
    layout = read_json(Path(a.layout))
    copy = read_json(Path(a.copy) if a.copy else None)
    problems, warns = validate(layout, copy, read_json(Path(a.assets) if a.assets else None), data)
    if a.project:
        p2, w2 = coverage(layout, read_json(Path(a.project) / "production.json"), copy, data)
        problems, warns = problems + p2, warns + w2
    out({"ok": not problems, "problems": problems, "warnings": warns}, 0 if not problems else 1)


def cmd_greybox(a) -> None:
    data = specs.load()
    layout = read_json(Path(a.layout))
    copy = read_json(Path(a.copy) if a.copy else None)
    lock = read_json(Path(a.lock) if a.lock else None)
    dest = Path(a.out_dir)
    dest.mkdir(parents=True, exist_ok=True)
    written = []
    for fr in layout.get("frames", []):
        if a.frame and fr.get("id") != a.frame:
            continue
        _, entry = specs.resolve(fr.get("placement", ""), data)
        path = dest / f"{fr['id']}.html"
        path.write_text(greybox_html(fr, entry, data, copy, lock), encoding="utf-8")
        written.append(str(path))
    if not written:
        raise Fail("no frames written; check --frame")
    out({"ok": True, "written": written, "next": "render each with render.py render <html> --measure, then "
         "qc.py design <measure> --placement <id>"})


def cmd_scaffold(a) -> None:
    data = specs.load()
    layout_path = Path(a.layout)
    layout = read_json(layout_path)
    project = Path(a.project) if a.project else layout_path.resolve().parent.parent
    fr = _frame(layout, a.frame)
    _, entry = specs.resolve(fr.get("placement", ""), data)
    dest = Path(a.out)
    if dest.exists() and not a.force:
        raise Fail(f"{dest} exists; scaffold writes a starting point only (pass --force to replace it)")
    dest.parent.mkdir(parents=True, exist_ok=True)
    text = scaffold_html(fr, entry, data, read_json(Path(a.copy) if a.copy else None),
                         read_json(Path(a.assets) if a.assets else None), read_json(Path(a.lock) if a.lock else None),
                         Path(a.tokens).resolve() if a.tokens else None, dest.resolve(), project.resolve())
    dest.write_text(text, encoding="utf-8")
    out({"ok": True, "out": str(dest), "frame": fr["id"], "placement": fr.get("placement")})


SCHEMA_DOC = {
    "frames": [{"id": "<piece>--<placement>", "piece": "p01", "placement": "instagram-feed-portrait",
                "pattern": "free text: the composition idea",
                "elements": [{"id": "headline", "role": "headline", "box": [0.07, 0.08, 0.86, 0.24],
                              "copy": "p01.headline", "size": "headline", "align": "left"},
                             {"id": "hero", "role": "image", "box": [0, 0.45, 1, 0.55], "asset": "hero",
                              "fit": "cover", "focal": [0.5, 0.4]},
                             {"id": "panel", "role": "shape", "box": [0, 0.8, 1, 0.2], "fill": "accent"}]}],
    "box": "[x, y, w, h] fractions of the trim; image and shape boxes touching an edge run into print bleed",
    "roles": sorted(ROLES),
    "text": "copy: '<piece>.<field>' from copy.json, or text: a literal string",
    "images": "asset: a name imagery picks in assets.json, or src: a project-relative file; fit cover|contain; "
              "focal [x, y]",
    "sizes": {"size": list(STEPS), "size_px": "explicit CSS px", "size_pt": "explicit points (print)"},
    "optional": ["align", "note", "fill (palette role or #hex)", "radius", "alt"],
}


def cmd_sheet(a) -> None:
    from PIL import Image, ImageDraw

    imgs = [(Path(p), Image.open(p).convert("RGB")) for p in a.pngs]
    cols = max(1, min(a.cols, len(imgs)))
    cell = a.width // cols
    thumbs = []
    for path, im in imgs:
        t = im.copy()
        t.thumbnail((cell - 24, cell * 3))
        thumbs.append((path, t))
    rows = [thumbs[i:i + cols] for i in range(0, len(thumbs), cols)]
    heights = [max(t.height for _, t in r) + 40 for r in rows]
    sheet = Image.new("RGB", (a.width, sum(heights) + 12), "#eaeef2")
    draw = ImageDraw.Draw(sheet)
    y = 12
    for r, rh in zip(rows, heights):
        for i, (path, t) in enumerate(r):
            x = i * cell + 12
            sheet.paste(t, (x, y))
            draw.text((x, y + t.height + 6), path.stem[:40], fill="#24292f")
        y += rh
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    sheet.save(a.out)
    out({"ok": True, "out": a.out, "tiles": len(imgs)})


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("validate")
    s.add_argument("layout")
    s.add_argument("--copy")
    s.add_argument("--assets")
    s.add_argument("--project", help="also check every copy piece has a frame at every project placement")
    s.set_defaults(fn=cmd_validate)
    s = sub.add_parser("schema")
    s.set_defaults(fn=lambda a: out({"ok": True, **SCHEMA_DOC}))
    s = sub.add_parser("greybox")
    s.add_argument("layout")
    s.add_argument("--out-dir", required=True)
    s.add_argument("--copy")
    s.add_argument("--lock")
    s.add_argument("--frame")
    s.set_defaults(fn=cmd_greybox)
    s = sub.add_parser("scaffold")
    s.add_argument("layout")
    s.add_argument("--frame", required=True)
    s.add_argument("--out", required=True)
    s.add_argument("--copy")
    s.add_argument("--assets")
    s.add_argument("--lock")
    s.add_argument("--tokens")
    s.add_argument("--project")
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_scaffold)
    s = sub.add_parser("sheet")
    s.add_argument("pngs", nargs="+")
    s.add_argument("--out", required=True)
    s.add_argument("--cols", type=int, default=4)
    s.add_argument("--width", type=int, default=1600)
    s.set_defaults(fn=cmd_sheet)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, specs.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
