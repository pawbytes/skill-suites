"""export.py plan: the right format per placement class."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("export", SCRIPTS / "export.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)
DATA = ex.specs.load()


def _plan(tmp_path, placement, canvas=None):
    fr = {"id": f"p01--{placement}", "placement": placement}
    if canvas:
        html = tmp_path / "compose" / fr["id"] / "design.html"
        html.parent.mkdir(parents=True)
        html.write_text(f'<meta name="canvas" content="{canvas}">', encoding="utf-8")
    return ex.plan_frame(tmp_path, fr, DATA)


def test_print_gets_pdf_and_proof(tmp_path):
    outs = _plan(tmp_path, "print-a3")["outputs"]
    assert [o["format"] for o in outs] == ["pdf", "png"] and outs[1]["proof"]


def test_document_placement_gets_pdf_pages(tmp_path):
    outs = _plan(tmp_path, "linkedin-document-post")["outputs"]
    assert len(outs) == 1 and outs[0]["format"] == "pdf" and outs[0]["document"]


def test_thumbnail_png_scaled_up_with_jpeg_fallback(tmp_path):
    o = _plan(tmp_path, "youtube-thumbnail", "1280x720")["outputs"][0]
    assert o["format"] == "png" and o["scale"] == 3.0 and o["fallback_jpeg"]


def test_aspect_mismatch_is_an_error(tmp_path):
    assert "re-layout" in _plan(tmp_path, "iab-728x90", "300x250")["error"]
