#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10"]
# ///
"""Quality checks for PawBytes Graphics Suite renders against their placement spec.

`design` checks a render.py measure file: canvas size, text, logo and CTA inside the safe
rect, keep-clear areas, contrast behind text, type sizes against the placement class floors,
overflowing text, fonts that fell back, word budget and text coverage.
`file` adds the exported file itself: format, pixel size (or PDF page size), file-size cap,
and the 1px border display ads need on white or black backgrounds.
`project` runs `file` over every export in {project}/deliver/<placement>/ and writes
deliver/qc.json.

Subcommands:
  design  MEASURE.json [--placement ID]   (default: the placement recorded in the measure file)
  file    FILE --placement ID [--measure MEASURE.json]   (default: <file-stem>.measure.json)
  project --project DIR

Output: JSON with fails (block delivery) and warns (show the user). Exit 0 when nothing
fails, 1 when something does, 2 on errors (JSON on stderr).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import specs  # noqa: E402  (bundled beside this script)

KEEP_INSIDE_ROLES = {"logo", "cta", "badge"}
BODY_ROLES = {"body", "bullets", "subhead"}
HEADLINE_ROLES = {"headline"}
FORMAT_OF = {".png": "png", ".jpg": "jpg", ".jpeg": "jpg", ".pdf": "pdf", ".webp": "webp", ".gif": "gif"}


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def _name(el: dict) -> str:
    return el.get("id") or el.get("role") or "element"


def _inside(box: list[float], rect: list[float], tol: float = 1.0) -> bool:
    x, y, w, h = box
    left, top, right, bottom = rect
    return x >= left - tol and y >= top - tol and x + w <= right + tol and y + h <= bottom + tol


def _overlap(a: list[float], b: list[float]) -> bool:
    return a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]


def check_design(measure: dict, pid: str, entry: dict, data: dict) -> tuple[list[str], list[str]]:
    fails, warns = [], []
    rules = data["rules"]
    cls = specs.class_rules(entry, data)
    canvas = measure.get("canvas", {})
    w, h, _ = specs.canvas_px(entry)
    css = canvas.get("css_px") or canvas.get("viewport") or [0, 0]
    if entry["unit"] == "mm":
        trim = canvas.get("trim") or [0, 0]
        if canvas.get("unit") != "mm" or abs(trim[0] - entry["w_mm"]) > 0.5 or abs(trim[1] - entry["h_mm"]) > 0.5:
            fails.append(f"canvas is {trim} {canvas.get('unit')}, {pid} is {entry['w_mm']}x{entry['h_mm']}mm")
        if abs(canvas.get("bleed_mm", 0) - entry.get("bleed_mm", 0)) > 0.2:
            fails.append(f"bleed is {canvas.get('bleed_mm', 0)}mm, {pid} needs {entry.get('bleed_mm')}mm per side")
    elif abs(css[0] - w) > 1 or abs(css[1] - h) > 1:
        fails.append(f"canvas is {css[0]:g}x{css[1]:g}, {pid} is {w:g}x{h:g}")

    rect = specs.safe_rect(entry, data)
    keep_clear = specs.exclusions(entry)
    elements = measure.get("elements", [])
    texts = [e for e in elements if e.get("is_text")]
    scale = (w / cls["ref_width"]) if cls.get("ref_width") else 1.0
    for el in elements:
        if not (el.get("is_text") or el.get("role") in KEEP_INSIDE_ROLES):
            continue
        if not _inside(el["box"], rect):
            fails.append(f"{_name(el)} crosses the safe zone of {pid} (safe rect {[round(v) for v in rect]}, "
                         f"box {[round(v) for v in el['box']]})")
        for ex in keep_clear:
            if _overlap(el["box"], ex):
                warns.append(f"{_name(el)} sits in a keep-clear area of {pid} ({entry.get('notes', '')[:80]})")
    for el in texts:
        if el.get("overflow"):
            fails.append(f"{_name(el)} overflows its box; text is clipped or spills")
        c = el.get("contrast")
        if c is None:
            if el.get("contrast_note"):
                warns.append(f"{_name(el)}: contrast not measurable ({el['contrast_note']})")
        elif c["p05"] < rules["contrast"]["fail_below"]:
            fails.append(f"{_name(el)} contrast {c['p05']}:1 at its worst 5% (needs {rules['contrast']['warn_below']}:1, "
                         f"fails below {rules['contrast']['fail_below']}:1); add a scrim, panel or move it")
        elif c["p05"] < rules["contrast"]["warn_below"]:
            warns.append(f"{_name(el)} contrast {c['p05']}:1 at its worst 5%, under {rules['contrast']['warn_below']}:1")
        size = el.get("min_font_size") or el.get("font_size")
        if size is None:
            continue
        if entry["unit"] == "mm":
            pt = size * 0.75
            if pt < cls["min_pt"]:
                fails.append(f"{_name(el)} is {pt:.1f}pt; print text needs {cls['min_pt']}pt "
                             f"({cls['min_pt_reversed']}pt reversed out of dark)")
            elif el.get("role") in BODY_ROLES and pt < cls["body_pt"]:
                warns.append(f"{_name(el)} body text is {pt:.1f}pt; {cls['body_pt']}pt+ reads comfortably in hand")
            continue
        floor = cls["min_px"] * scale
        if size < floor - 0.5:
            fails.append(f"{_name(el)} is {size:g}px; nothing on {pid} should be under {floor:.0f}px")
        elif el.get("role") in BODY_ROLES and size < cls["body_px"] * scale - 0.5:
            warns.append(f"{_name(el)} is {size:g}px; body text on {pid} reads best at {cls['body_px'] * scale:.0f}px+")
        elif el.get("role") in HEADLINE_ROLES and size < cls["headline_px"] * scale - 0.5:
            warns.append(f"headline is {size:g}px; on {pid} aim for {cls['headline_px'] * scale:.0f}px+ "
                         "(cut words before shrinking type)")
    for fam in measure.get("fonts_missing", []):
        fails.append(f"font '{fam}' did not load and fell back; check tokens.css imports or the network")
    words = sum(e.get("words", 0) for e in texts)
    if cls.get("max_words") and words > cls["max_words"]:
        warns.append(f"{words} words on the canvas; the {entry['class']} budget is {cls['max_words']}")
    if entry["platform"] in ("meta-ads", "google-display") and w * h:
        area = sum(e["box"][2] * e["box"][3] for e in texts) / (w * h)
        if area > 0.2:
            warns.append(f"text boxes cover {area:.0%} of the ad; under ~20% tends to perform better"
                         + ("; Google responsive display images disallow overlaid text over 20%"
                            if pid.startswith("gads-rda") else ""))
    return fails, warns


def pdf_page_mm(path: Path) -> tuple[float, float] | None:
    m = re.search(rb"/MediaBox\s*\[\s*([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s*\]", path.read_bytes())
    if not m:
        return None
    x0, y0, x1, y1 = (float(v) for v in m.groups())
    return (x1 - x0) * 25.4 / 72, (y1 - y0) * 25.4 / 72


def edge_needs_border(img) -> bool:
    """True when the outer 1px ring is almost all near-white or near-black (display ads need a border)."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    px = rgb.load()
    ring = [px[x, 0] for x in range(w)] + [px[x, h - 1] for x in range(w)]
    ring += [px[0, y] for y in range(h)] + [px[w - 1, y] for y in range(h)]
    light = sum(1 for r, g, b in ring if min(r, g, b) >= 245)
    dark = sum(1 for r, g, b in ring if max(r, g, b) <= 10)
    return max(light, dark) / len(ring) > 0.9


def check_file(path: Path, pid: str, entry: dict, data: dict, measure_path: Path | None) -> dict:
    fails, warns = [], []
    if not path.is_file():
        raise Fail(f"no such file: {path}")
    fmt = FORMAT_OF.get(path.suffix.lower())
    allowed = {f.split("-")[0] for f in entry.get("formats", [])}
    if fmt not in allowed:
        (warns if entry["unit"] == "mm" and fmt in ("png", "jpg") else fails).append(
            f"{path.name} is {fmt}; {pid} takes {', '.join(entry.get('formats', []))}")
    kb = path.stat().st_size / 1024
    if entry.get("max_kb") and kb > entry["max_kb"]:
        fails.append(f"{path.name} is {kb:.0f} KB; {pid} caps files at {entry['max_kb']} KB")
    if pid == "youtube-thumbnail" and kb > 2048:
        warns.append(f"{kb:.0f} KB is over 2 MB; phone uploads of thumbnails are capped at 2 MB")
    if fmt == "pdf":
        size = pdf_page_mm(path)
        if entry["unit"] == "mm" and size:
            want = (entry["w_mm"] + 2 * entry.get("bleed_mm", 0), entry["h_mm"] + 2 * entry.get("bleed_mm", 0))
            if abs(size[0] - want[0]) > 0.6 or abs(size[1] - want[1]) > 0.6:
                fails.append(f"PDF page is {size[0]:.1f}x{size[1]:.1f}mm; {pid} with bleed is "
                             f"{want[0]:.1f}x{want[1]:.1f}mm")
        if entry.get("color") == "cmyk":
            warns.append("PDF is RGB (Chromium); convert to CMYK PDF/X-4 for press, or confirm the printer converts")
    elif fmt in ("png", "jpg", "webp", "gif"):
        from PIL import Image

        with Image.open(path) as img:
            iw, ih = img.size
            if entry["unit"] == "mm":
                dpi = entry.get("dpi", 300)
                want = [(entry[k] + 2 * entry.get("bleed_mm", 0)) / 25.4 * dpi for k in ("w_mm", "h_mm")]
                if abs(iw - want[0]) > 3 or abs(ih - want[1]) > 3:
                    warns.append(f"{iw}x{ih}px is not {pid} at {dpi} dpi with bleed ({want[0]:.0f}x{want[1]:.0f}); "
                                 "press files should be the PDF")
            else:
                ratio = iw / entry["w"]
                if abs(ratio - round(ratio)) > 0.01 or abs(ih - entry["h"] * round(ratio)) > 1 or round(ratio) < 1:
                    fails.append(f"{iw}x{ih}px; {pid} is {entry['w']}x{entry['h']} (or an exact multiple)")
            if entry.get("border_on_light_or_dark_bg") and edge_needs_border(img):
                fails.append("white or black edge with no border; display ads need a 1px contrasting border")
    m_path = measure_path or path.with_name(path.stem + ".measure.json")
    if m_path.is_file():
        f2, w2 = check_design(json.loads(m_path.read_text(encoding="utf-8")), pid, entry, data)
        fails += f2
        warns += w2
    else:
        warns.append(f"no measure file ({m_path.name}); render with --measure to check text, contrast and safe zones")
    return {"file": str(path), "placement": pid, "kb": round(kb, 1), "ok": not fails, "fails": fails, "warns": warns}


def cmd_design(a) -> None:
    data = specs.load()
    measure = json.loads(Path(a.measure).read_text(encoding="utf-8"))
    placement = a.placement or (measure.get("canvas") or {}).get("placement")
    if not placement:
        raise Fail('no placement: pass --placement, or render HTML that carries <meta name="placement">')
    pid, entry = specs.resolve(placement, data)
    fails, warns = check_design(measure, pid, entry, data)
    out({"ok": not fails, "placement": pid, "fails": fails, "warns": warns}, 0 if not fails else 1)


def cmd_file(a) -> None:
    data = specs.load()
    pid, entry = specs.resolve(a.placement, data)
    res = check_file(Path(a.file), pid, entry, data, Path(a.measure) if a.measure else None)
    out(res, 0 if res["ok"] else 1)


def cmd_project(a) -> None:
    project = Path(a.project)
    deliver = project / "deliver"
    if not deliver.is_dir():
        raise Fail(f"no deliver/ folder in {project}")
    data = specs.load()
    results = []
    for folder in sorted(p for p in deliver.iterdir() if p.is_dir()):
        try:
            pid, entry = specs.resolve(folder.name, data)
        except specs.Fail:
            results.append({"file": str(folder), "ok": False, "fails": [f"folder '{folder.name}' is not a placement id"],
                            "warns": []})
            continue
        for f in sorted(folder.iterdir()):
            if f.suffix.lower() in FORMAT_OF and not f.name.endswith((".thumb.png", ".proof.png")):
                results.append(check_file(f, pid, entry, data, None))
    if not results:
        raise Fail(f"no exports under {deliver}/<placement>/")
    report = {"ok": all(r["ok"] for r in results), "files": len(results),
              "failed": [r["file"] for r in results if not r["ok"]], "results": results}
    (deliver / "qc.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    out({**report, "report": str(deliver / "qc.json")}, 0 if report["ok"] else 1)


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("design")
    s.add_argument("measure")
    s.add_argument("--placement")
    s.set_defaults(fn=cmd_design)
    s = sub.add_parser("file")
    s.add_argument("file")
    s.add_argument("--placement", required=True)
    s.add_argument("--measure")
    s.set_defaults(fn=cmd_file)
    s = sub.add_parser("project")
    s.add_argument("--project", required=True)
    s.set_defaults(fn=cmd_project)
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
