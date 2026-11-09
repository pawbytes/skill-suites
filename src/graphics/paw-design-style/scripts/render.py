#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.45", "pillow>=10"]
# ///
"""Render PawBytes Graphics Suite design HTML to PNG, JPG or PDF with Playwright, and measure it.

The canvas comes from the HTML: <meta name="canvas" content="1080x1350"> (CSS px) or
content="297x420mm" for print, plus <meta name="bleed" content="3mm"> when the page is
authored at trim + bleed on every side. --canvas and --bleed override them. A
<meta name="placement"> (frames.py writes it) travels into the measure file, so qc.py
needs no --placement.

Measuring reads every element with a data-role attribute (data-id names it): its box in
canvas px, the smallest font size inside it, colour, word count, whether its text overflows
its box, whether the font it asks for actually rendered (a missing web font silently falls
back), and the contrast of its text against the pixels behind it (text hidden, background
sampled; p05 is the worst 5% of the box, median the typical). Gradient or clipped text
cannot be measured and is flagged.

Subcommands:
  render  HTML [--out PATH] [--format png|jpeg|pdf] [--scale S | --dpi 300] [--quality 90]
          [--max-kb N] [--measure] [--thumb 0.25] [--canvas WxH[mm]] [--bleed 3mm] [--wait-ms 0]
  measure HTML [--out JSON] [--canvas WxH[mm]] [--bleed 3mm]

PNG scale defaults to 1 for px canvases and to dpi/96 (300 dpi) for mm canvases. JPEG with
--max-kb steps quality down from --quality to 40 until the file fits; PNG over --max-kb is a
warning (try --format jpeg). PDF keeps text as vector type and is sized trim + bleed.

Output: JSON on stdout. Errors: JSON on stderr, exit 2. Missing browser: run
`uv run --with playwright python -m playwright install chromium`.
"""
from __future__ import annotations

import argparse
import io
import json
import re
import statistics
import sys
from pathlib import Path

PX_PER_MM = 96 / 25.4
TEXT_LESS_ROLES = {"image", "shape", "logo"}

MEASURE_JS = r"""
() => {
  const visibleText = (el) => {
    let min = Infinity;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const n = walker.currentNode;
      if (!n.textContent.trim()) continue;
      const cs = getComputedStyle(n.parentElement);
      if (cs.visibility === 'hidden' || cs.display === 'none') continue;
      min = Math.min(min, parseFloat(cs.fontSize));
    }
    return min === Infinity ? null : min;
  };
  const probe = document.createElement('canvas').getContext('2d');
  const sample = 'mmmmmmmmmmlliWWQ@#0123456789';
  const fontRenders = (family, weight) => {
    if (!family) return null;
    const generic = ['serif', 'sans-serif', 'monospace', 'cursive', 'fantasy', 'system-ui'];
    if (generic.includes(family)) return true;
    for (const base of ['monospace', 'serif']) {
      probe.font = `${weight} 72px ${base}`;
      const w0 = probe.measureText(sample).width;
      probe.font = `${weight} 72px "${family}", ${base}`;
      if (probe.measureText(sample).width !== w0) return true;
    }
    return false;
  };
  return [...document.querySelectorAll('[data-role]')].map((el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const text = (el.innerText || '').trim();
    const family = cs.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g, '');
    const role = el.dataset.role;
    const isText = text.length > 0 && !['image', 'shape', 'logo'].includes(role);
    return {
      id: el.dataset.id || null, role, box: [r.x, r.y, r.width, r.height],
      text: isText ? text : null, words: isText ? text.split(/\s+/).length : 0, chars: isText ? text.length : 0,
      font_size: isText ? parseFloat(cs.fontSize) : null, min_font_size: isText ? visibleText(el) : null,
      font_family: isText ? family : null, font_weight: isText ? cs.fontWeight : null,
      font_rendered: isText ? fontRenders(family, cs.fontWeight) : null,
      color: cs.color, clipped_text: cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text',
      line_height: cs.lineHeight, text_transform: cs.textTransform, letter_spacing: cs.letterSpacing,
      // tight display leading lets glyphs poke past the line box; a real overflow is most of a line
      overflow: el.scrollWidth > el.clientWidth + 2 ||
        el.scrollHeight > el.clientHeight + Math.max(2, 0.33 * parseFloat(cs.fontSize)),
      is_text: isText,
    };
  });
}
"""

HIDE_TEXT_CSS = """
[data-role]:not([data-role=image]):not([data-role=logo]),
[data-role]:not([data-role=image]):not([data-role=logo]) * {
  color: transparent !important; text-shadow: none !important; -webkit-text-stroke: 0 !important;
  text-decoration-color: transparent !important; caret-color: transparent !important;
}
"""


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def parse_canvas(value: str) -> dict:
    m = re.fullmatch(r"\s*([\d.]+)\s*[x×]\s*([\d.]+)\s*(mm|px)?\s*", value or "")
    if not m:
        raise Fail(f"canvas must look like 1080x1350 or 297x420mm, got '{value}'")
    w, h, unit = float(m.group(1)), float(m.group(2)), m.group(3) or "px"
    return {"w": w, "h": h, "unit": unit}


def parse_length_mm(value: str | None) -> float:
    if not value:
        return 0.0
    m = re.fullmatch(r"\s*([\d.]+)\s*(mm|in|px)?\s*", value)
    if not m:
        raise Fail(f"bleed must look like 3mm or 0.125in, got '{value}'")
    n, unit = float(m.group(1)), m.group(2) or "mm"
    return n * 25.4 if unit == "in" else n / PX_PER_MM if unit == "px" else n


def read_meta(html: str, name: str) -> str | None:
    for tag in re.findall(r"<meta\b[^>]*>", html, flags=re.I):
        if re.search(rf"name\s*=\s*['\"]{name}['\"]", tag, flags=re.I):
            m = re.search(r"content\s*=\s*['\"]([^'\"]*)['\"]", tag, flags=re.I)
            if m:
                return m.group(1)
    return None


def canvas_for(html_path: Path, canvas: str | None, bleed: str | None) -> dict:
    """Canvas geometry: CSS px viewport (trim + bleed) and the trim/bleed split."""
    html = html_path.read_text(encoding="utf-8", errors="replace")
    c = parse_canvas(canvas or read_meta(html, "canvas") or "")
    bleed_mm = parse_length_mm(bleed if bleed is not None else read_meta(html, "bleed"))
    if c["unit"] == "px" and bleed_mm:
        raise Fail("bleed applies to mm (print) canvases only")
    if c["unit"] == "mm":
        trim_w, trim_h = c["w"] * PX_PER_MM, c["h"] * PX_PER_MM
        bleed_px = bleed_mm * PX_PER_MM
    else:
        trim_w, trim_h, bleed_px = c["w"], c["h"], 0.0
    vw, vh = trim_w + 2 * bleed_px, trim_h + 2 * bleed_px
    return {"placement": read_meta(html, "placement"), "frame": read_meta(html, "frame"), "unit": c["unit"], "trim": [c["w"], c["h"]], "bleed_mm": round(bleed_mm, 3),
            "css_px": [round(vw, 3), round(vh, 3)], "bleed_px": round(bleed_px, 3),
            "viewport": [max(1, round(vw)), max(1, round(vh))]}


def luminance(rgb: tuple[int, int, int]) -> float:
    def ch(v: int) -> float:
        s = v / 255
        return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(l1: float, l2: float) -> float:
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def parse_css_color(value: str) -> tuple[tuple[int, int, int], float] | None:
    m = re.match(r"rgba?\(([^)]+)\)", value or "")
    if not m:
        return None
    parts = [p for p in re.split(r"[\s,/]+", m.group(1).strip()) if p]
    try:
        rgb = tuple(int(round(float(p))) for p in parts[:3])
        alpha = float(parts[3]) if len(parts) > 3 else 1.0
    except ValueError:
        return None
    return rgb, alpha  # type: ignore[return-value]


def box_contrast(img, box: list[float], text_rgb: tuple[int, int, int]) -> dict | None:
    x, y, w, h = box
    left, top = max(0, int(x)), max(0, int(y))
    right, bottom = min(img.width, int(x + w)), min(img.height, int(y + h))
    if right <= left or bottom <= top:
        return None
    region = img.crop((left, top, right, bottom)).convert("RGB")
    step = max(1, int(((right - left) * (bottom - top) / 40000) ** 0.5))
    if step > 1:
        region = region.resize((max(1, region.width // step), max(1, region.height // step)))
    lt = luminance(text_rgb)
    pixels = region.get_flattened_data() if hasattr(region, "get_flattened_data") else region.getdata()
    ratios = sorted(contrast(lt, luminance(px)) for px in pixels)
    p05 = ratios[max(0, int(len(ratios) * 0.05) - 1)]
    return {"p05": round(p05, 2), "median": round(statistics.median(ratios), 2), "min": round(ratios[0], 2)}


def _browser(p):
    try:
        return p.chromium.launch()
    except Exception as exc:  # noqa: BLE001
        if "Executable doesn't exist" in str(exc) or "playwright install" in str(exc):
            raise Fail("Chromium for Playwright is missing; run "
                       "`uv run --with playwright python -m playwright install chromium`")
        raise


def _open(p, html_path: Path, geo: dict, scale: float, wait_ms: int):
    browser = _browser(p)
    page = browser.new_page(viewport={"width": geo["viewport"][0], "height": geo["viewport"][1]},
                            device_scale_factor=scale)
    page.emulate_media(media="screen")
    try:
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle", timeout=45000)
    except Exception as exc:  # noqa: BLE001  slow font CDN: render what loaded, measure will flag fonts
        if "Timeout" not in type(exc).__name__ and "Timeout" not in str(exc):
            raise
    # images first, then fonts: fonts.ready can resolve before late content asks for a face
    page.evaluate("""() => Promise.all([...document.images].map((i) => i.complete ? 1 :
        new Promise((r) => { i.onload = i.onerror = r; })))""")
    page.evaluate("document.fonts.ready.then(() => true)")
    broken = page.evaluate("() => [...document.images].filter((i) => !i.naturalWidth).map((i) => i.getAttribute('src'))")
    if broken:
        raise Fail(f"images failed to load: {broken}; paths in design HTML resolve from the HTML file's folder")
    if wait_ms:
        page.wait_for_timeout(wait_ms)
    return browser, page


def _measure(page, geo: dict) -> dict:
    from PIL import Image

    elements = page.evaluate(MEASURE_JS)
    page.add_style_tag(content=HIDE_TEXT_CSS)
    page.wait_for_timeout(50)
    shot = page.screenshot(type="png", scale="css", animations="disabled", clip={"x": 0, "y": 0, "width": geo["viewport"][0],
                                                          "height": geo["viewport"][1]})
    bg = Image.open(io.BytesIO(shot)).convert("RGB")
    for el in elements:
        el["box"] = [round(v, 2) for v in el["box"]]
        if not el["is_text"]:
            continue
        parsed = parse_css_color(el["color"])
        if el.pop("clipped_text", False) or not parsed or parsed[1] == 0:
            el["contrast"] = None
            el["contrast_note"] = "gradient, clipped or transparent text; check by eye"
            continue
        el["contrast"] = box_contrast(bg, el["box"], parsed[0])
    for el in elements:
        el.pop("clipped_text", None)
    fonts_missing = sorted({e["font_family"] for e in elements if e["is_text"] and e["font_rendered"] is False})
    return {"canvas": geo, "elements": elements, "fonts_missing": fonts_missing}


def default_scale(geo: dict, scale: float | None, dpi: float | None) -> float:
    if scale:
        return scale
    if geo["unit"] == "mm":
        return (dpi or 300) / 96
    return 1.0


def render_file(html_path: Path, dest: Path | None = None, fmt: str = "png", scale: float | None = None,
                dpi: float | None = None, quality: int = 90, max_kb: float | None = None, measure: bool = False,
                thumb: float | None = None, canvas: str | None = None, bleed: str | None = None,
                wait_ms: int = 0) -> dict:
    """Render one design file; importable by export.py. Returns the result dict."""
    from PIL import Image
    from playwright.sync_api import sync_playwright

    html_path = Path(html_path)
    if not html_path.is_file():
        raise Fail(f"no such file: {html_path}")
    geo = canvas_for(html_path, canvas, bleed)
    dest = Path(dest) if dest else html_path.with_suffix({"png": ".png", "jpeg": ".jpg", "pdf": ".pdf"}[fmt])
    dest.parent.mkdir(parents=True, exist_ok=True)
    scale = default_scale(geo, scale, dpi)
    result = {"ok": True, "html": str(html_path), "out": str(dest), "format": fmt, "canvas": geo, "warnings": []}
    with sync_playwright() as p:
        browser, page = _open(p, html_path, geo, scale if fmt != "pdf" else 1, wait_ms)
        try:
            if fmt == "pdf":
                if geo["unit"] == "mm":
                    size = {"width": f"{geo['trim'][0] + 2 * geo['bleed_mm']}mm",
                            "height": f"{geo['trim'][1] + 2 * geo['bleed_mm']}mm"}
                else:
                    size = {"width": f"{geo['viewport'][0]}px", "height": f"{geo['viewport'][1]}px"}
                page.add_style_tag(content="@page { margin: 0 } html, body { margin: 0 }")
                page.pdf(path=str(dest), print_background=True, margin={"top": "0", "right": "0",
                         "bottom": "0", "left": "0"}, **size)
                result["page_size"] = size
            else:
                png = page.screenshot(type="png", full_page=False, animations="disabled")
                img = Image.open(io.BytesIO(png))
                result["px"] = [img.width, img.height]
                result["scale"] = round(scale, 4)
                if fmt == "png":
                    dest.write_bytes(png)
                else:
                    rgb = img.convert("RGB")
                    q = quality
                    while True:
                        buf = io.BytesIO()
                        rgb.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
                        if not max_kb or buf.tell() <= max_kb * 1024 or q <= 40:
                            break
                        q -= 5
                    dest.write_bytes(buf.getvalue())
                    result["quality"] = q
                if thumb:
                    t = img.resize((max(1, round(img.width * thumb)), max(1, round(img.height * thumb))),
                                   Image.LANCZOS)
                    tpath = dest.with_name(dest.stem + ".thumb.png")
                    t.save(tpath)
                    result["thumb"] = str(tpath)
            if measure:
                m = _measure(page, geo)
                mpath = dest.with_name(dest.stem + ".measure.json")
                mpath.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")
                result["measure"] = str(mpath)
                result["fonts_missing"] = m["fonts_missing"]
                result["overflowing"] = [e["id"] or e["role"] for e in m["elements"] if e["overflow"] and e["is_text"]]
        finally:
            browser.close()
    size = dest.stat().st_size
    result["bytes"] = size
    result["kb"] = round(size / 1024, 1)
    if max_kb and size > max_kb * 1024:
        result["warnings"].append(f"{result['kb']} KB is over the {max_kb:g} KB cap"
                                  + ("; try --format jpeg" if fmt == "png" else "; simplify the design or "
                                     "reduce photo detail"))
    return result


def cmd_render(a) -> None:
    out(render_file(Path(a.html), Path(a.out) if a.out else None, a.format, a.scale, a.dpi, a.quality, a.max_kb,
                    a.measure, a.thumb, a.canvas, a.bleed, a.wait_ms))


def cmd_measure(a) -> None:
    from playwright.sync_api import sync_playwright

    html_path = Path(a.html)
    if not html_path.is_file():
        raise Fail(f"no such file: {html_path}")
    geo = canvas_for(html_path, a.canvas, a.bleed)
    with sync_playwright() as p:
        browser, page = _open(p, html_path, geo, 1, a.wait_ms)
        try:
            m = _measure(page, geo)
        finally:
            browser.close()
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")
        out({"ok": True, "out": a.out, "fonts_missing": m["fonts_missing"], "elements": len(m["elements"])})
    out({"ok": True, **m})


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(s):
        s.add_argument("html")
        s.add_argument("--canvas", help="override the canvas meta, e.g. 1080x1350 or 210x297mm")
        s.add_argument("--bleed", help="override the bleed meta, e.g. 3mm or 0.125in")
        s.add_argument("--wait-ms", type=int, default=0, help="extra settle time after fonts load")

    s = sub.add_parser("render", help="render HTML to PNG, JPEG or PDF")
    common(s)
    s.add_argument("--out")
    s.add_argument("--format", choices=["png", "jpeg", "pdf"], default="png")
    s.add_argument("--scale", type=float, help="device pixel ratio for PNG/JPEG")
    s.add_argument("--dpi", type=float, help="print raster resolution for mm canvases (default 300)")
    s.add_argument("--quality", type=int, default=90)
    s.add_argument("--max-kb", type=float, help="file-size cap; JPEG quality steps down to fit")
    s.add_argument("--measure", action="store_true", help="also write <out>.measure.json")
    s.add_argument("--thumb", type=float, help="also write a <out>.thumb.png at this fraction, e.g. 0.25")
    s.set_defaults(fn=cmd_render)

    s = sub.add_parser("measure", help="measure data-role elements: boxes, type sizes, fonts, overflow, contrast")
    common(s)
    s.add_argument("--out")
    s.set_defaults(fn=cmd_measure)

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
