"""End to end through the scripts: copy deck, layout, greybox, scaffold, render, QC, export.

Needs Playwright Chromium for the render tests; Google Fonts are not used (system fonts),
so the tests run offline.
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import SHARED, SUITE, load, needs_browser

production = load(SHARED / "production.py", "design_prod_p")
specs = load(SHARED / "specs.py", "specs")
frames = load(SHARED / "frames.py", "design_frames")
qc = load(SHARED / "qc.py", "design_qc")
render = load(SHARED / "render.py", "render")
hooks = load(SUITE / "paw-design-concept" / "scripts" / "hooks.py", "hooks")
copydeck = load(SUITE / "paw-design-concept" / "scripts" / "copydeck.py", "design_copydeck")
export = load(SUITE / "paw-design-deliver" / "scripts" / "export.py", "design_export")

COPY = {"proposition": "Timing beats flour.", "goal": "engagement",
        "hook": {"id": "mistake-warning", "text": "7 mistakes killing your sourdough"},
        "visual_hook": {"id": "scale-contrast"},
        "pieces": [{"id": "p01", "role": "single", "headline": "7 mistakes killing your sourdough",
                    "subhead": "Most are about time, not flour.", "cta": "Get the fix list"}]}


def test_hook_lint_flags_the_research_faults():
    res = hooks.lint("TIPS FOR BETTER BREAD AND MUCH MUCH MORE THAN THAT TODAY?", "carousel-cover")
    assert not res["ok"] and any("all caps" in w for w in res["warns"])
    assert any("question" in w for w in res["warns"]) and any("filler" in w for w in res["warns"])
    assert hooks.lint("7 pricing mistakes killing your margin", "carousel-cover")["ok"]


def test_copydeck_mandatory_lines():
    deck = {**COPY, "mandatory": ["Get the fix list", "Terms apply"]}
    fails, _, _ = copydeck.validate(deck, "social-post", 1)
    assert fails == ["mandatory copy missing verbatim: 'Terms apply'"]


def test_copydeck_budgets_and_hook_ids():
    fails, warns, _ = copydeck.validate(COPY, "social-post", 1)
    assert fails == [] and warns == []
    bad = json.loads(json.dumps(COPY))
    bad["hook"]["id"] = "nope"
    bad["pieces"][0]["body"] = " ".join(["word"] * 70)
    fails, _, _ = copydeck.validate(bad, "social-post", 1)
    assert any("not a headline hook" in f for f in fails) and any("fails above" in f for f in fails)


def _frame(placement, elements, fid=None):
    return {"id": fid or f"p01--{placement}", "piece": "p01", "placement": placement, "elements": elements}


def test_layout_validate_catches_safe_zone_and_missing_copy():
    data = specs.load()
    layout = {"frames": [_frame("instagram-story", [
        {"id": "headline", "role": "headline", "box": [0.06, 0.02, 0.8, 0.1], "copy": "p01.headline"},
        {"id": "cta", "role": "cta", "box": [0.06, 0.5, 0.5, 0.05], "copy": "p01.missing"}])]}
    problems, _ = frames.validate(layout, COPY, None, data)
    assert any("crosses the instagram-story safe zone" in p for p in problems)
    assert any("p01.missing" in p for p in problems)
    problems, _ = frames.coverage(layout, {"placements": ["instagram-story", "iab-300x250"]}, COPY, data)
    assert problems == ["no frame for piece p01 at iab-300x250"]


def _project(tmp_path, profile="social-post", placements="instagram-feed-portrait"):
    subprocess.run([sys.executable, str(SHARED / "production.py"), "init", "--root", str(tmp_path), "--slug", "t",
                    "--title", "T", "--profile", profile, "--placements", placements], check=True,
                   capture_output=True)
    p = tmp_path / "t"
    (p / "concept" / "copy.json").write_text(json.dumps(COPY), encoding="utf-8")
    for st in production.STAGES[:-1]:
        for cmd in (["start"], ["submit", "--artifact", "x"], ["approve"]):
            subprocess.run([sys.executable, str(SHARED / "production.py"), cmd[0], "--project", str(p), st, *cmd[1:]],
                           check=True, capture_output=True)
    return p


def _design(path: Path, canvas: str, body: str, bleed: str | None = None, css: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    meta = f'<meta name="canvas" content="{canvas}">' + (f'<meta name="bleed" content="{bleed}">' if bleed else "")
    path.write_text(f"<!doctype html><html><head><meta charset='utf-8'>{meta}<style>html,body{{margin:0;"
                    f"overflow:hidden}} body{{position:relative;font-family:Arial}} .e{{position:absolute}}"
                    f"{css}</style></head><body>{body}</body></html>", encoding="utf-8")


@needs_browser
def test_greybox_render_flags_overflow(tmp_path):
    data = specs.load()
    layout = {"frames": [_frame("instagram-feed-portrait", [
        {"id": "headline", "role": "headline", "box": [0.08, 0.1, 0.3, 0.05], "copy": "p01.headline"}])]}
    fr = layout["frames"][0]
    _, entry = specs.resolve("instagram-feed-portrait", data)
    html = tmp_path / "g.html"
    html.write_text(frames.greybox_html(fr, entry, data, COPY, None), encoding="utf-8")
    render.render_file(html, tmp_path / "g.png", measure=True)
    m = json.loads((tmp_path / "g.measure.json").read_text(encoding="utf-8"))
    fails, _ = qc.check_design(m, "instagram-feed-portrait", entry, data)
    assert any("overflows" in f for f in fails)


@needs_browser
def test_contrast_is_measured_against_the_pixels_behind(tmp_path):
    data = specs.load()
    _, entry = specs.resolve("instagram-feed-portrait", data)
    _design(tmp_path / "d.html", "1080x1350",
            "<div class=e data-role=headline data-id=h style='left:100px;top:100px;width:800px;font-size:90px;"
            "color:#ffffff'>Low contrast</div>", css="body{background:#d9d9d9}")
    render.render_file(tmp_path / "d.html", tmp_path / "d.png", measure=True)
    m = json.loads((tmp_path / "d.measure.json").read_text(encoding="utf-8"))
    fails, _ = qc.check_design(m, "instagram-feed-portrait", entry, data)
    assert any("contrast" in f for f in fails)


@needs_browser
def test_export_display_ad_border_and_weight(tmp_path):
    p = _project(tmp_path, "ad-set", "iab-300x250")
    layout = {"frames": [_frame("iab-300x250", [
        {"id": "headline", "role": "headline", "box": [0.06, 0.1, 0.88, 0.3], "copy": "p01.headline"}])]}
    (p / "layout" / "layout.json").write_text(json.dumps(layout), encoding="utf-8")
    html = p / "compose" / "p01--iab-300x250" / "design.html"
    body = ("<div class=e data-role=headline data-id=headline style='left:18px;top:25px;width:264px;"
            "font-size:24px;font-weight:700'>7 mistakes killing your sourdough</div>")
    _design(html, "300x250", body, css="body{background:#fff;width:300px;height:250px}")
    with pytest.raises(SystemExit) as ex:
        export.cmd_run(type("A", (), {"project": str(p), "frame": None, "no_proof": True})())
    assert ex.value.code == 1
    report = json.loads((p / "deliver" / "qc.json").read_text(encoding="utf-8"))
    assert any("border" in f for f in report["results"][0]["fails"])
    _design(html, "300x250", body, css="body{background:#fff;width:300px;height:250px;"
            "box-shadow:inset 0 0 0 1px #6b6b6b}")
    with pytest.raises(SystemExit) as ex:
        export.cmd_run(type("A", (), {"project": str(p), "frame": None, "no_proof": True})())
    assert ex.value.code == 0
    out = p / "deliver" / "iab-300x250" / "p01--iab-300x250.png"
    assert out.is_file() and out.stat().st_size <= 150 * 1024


@needs_browser
def test_export_print_pdf_with_bleed_and_proof(tmp_path):
    p = _project(tmp_path, "flyer", "print-a5")
    layout = {"frames": [_frame("print-a5", [
        {"id": "headline", "role": "headline", "box": [0.1, 0.1, 0.8, 0.2], "copy": "p01.headline"}])]}
    (p / "layout" / "layout.json").write_text(json.dumps(layout), encoding="utf-8")
    _design(p / "compose" / "p01--print-a5" / "design.html", "148x210mm",
            "<div class=e data-role=headline data-id=headline style='left:20mm;top:25mm;width:110mm;"
            "font-size:28pt;font-weight:700'>Night Market</div>", bleed="3mm",
            css="html,body{width:154mm;height:216mm} body{background:#0b3d2e;color:#fff}")
    with pytest.raises(SystemExit) as ex:
        export.cmd_run(type("A", (), {"project": str(p), "frame": None, "no_proof": False})())
    assert ex.value.code == 0
    pdf = p / "deliver" / "print-a5" / "p01--print-a5.pdf"
    w, h = qc.pdf_page_mm(pdf)
    assert abs(w - 154) < 0.6 and abs(h - 216) < 0.6
    assert (p / "deliver" / "print-a5" / "p01--print-a5.proof.png").is_file()


@needs_browser
def test_linkedin_document_pages_merge(tmp_path):
    p = _project(tmp_path, "carousel", "linkedin-document-post")
    frs = []
    for i in (1, 2):
        fid = f"s0{i}--linkedin-document-post"
        frs.append(_frame("linkedin-document-post", [
            {"id": "headline", "role": "headline", "box": [0.1, 0.1, 0.8, 0.2], "copy": "p01.headline"}], fid))
        _design(p / "compose" / fid / "design.html", "1080x1350",
                f"<div class=e data-role=headline data-id=headline style='left:120px;top:140px;width:800px;"
                f"font-size:90px;font-weight:700'>Slide {i}</div>", css="html,body{width:1080px;height:1350px}")
    (p / "layout" / "layout.json").write_text(json.dumps({"frames": frs}), encoding="utf-8")
    with pytest.raises(SystemExit) as ex:
        export.cmd_run(type("A", (), {"project": str(p), "frame": None, "no_proof": True})())
    assert ex.value.code == 0
    from pypdf import PdfReader

    doc = p / "deliver" / "linkedin-document-post" / "t-document.pdf"
    assert len(PdfReader(doc).pages) == 2
    with pytest.raises(SystemExit) as ex:  # re-exporting one frame keeps the rest of the package
        export.cmd_run(type("A", (), {"project": str(p), "frame": "s02--linkedin-document-post", "no_proof": True})())
    assert ex.value.code == 0 and len(PdfReader(doc).pages) == 2
    report = json.loads((p / "deliver" / "manifest.json").read_text(encoding="utf-8"))
    assert [m["frame"] for m in report["frames"]] == ["s01--linkedin-document-post", "s02--linkedin-document-post"]
