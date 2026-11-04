"""The creative layout map: legacy .pawbytes/creative-suites paths land in the paw-suites/creative scheme."""
import importlib.util
import json
from pathlib import Path

import pytest

SKILL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("paw_paths", SKILL / "scripts" / "paw-paths.py")
pp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pp)
LAYOUT = json.loads((SKILL / "assets" / "layout.json").read_text(encoding="utf-8"))

FORWARD = {
    "index.md": "_memory/index.md",
    "daily/2026-03-31.md": "_memory/daily/2026-03-31.md",
    "knowledge/index.md": "_memory/knowledge/index.md",
    "campaigns/summer/assets/images/hero.png": "brands/unassigned/campaigns/summer/designs/hero.png",
    "campaigns/summer/brief.md": "brands/unassigned/campaigns/summer/brief.md",
    "output/clips/s1/tiktok/a.mp4": "brands/unassigned/videos/clips/s1/tiktok/a.mp4",
    "brands/acme/assets/brand-identity/logo/l.png": "brands/acme/brand-assets/logo/l.png",
    "brands/acme/assets/intro.mp4": "brands/acme/brand-assets/intro.mp4",
    "brands/acme/assets/wip/v1.png": "brands/acme/designs/wip/v1.png",
    "brands/acme/assets/social/2026-03-30/p.png": "brands/acme/designs/social/2026-03-30/p.png",
    "brands/acme/assets/spring/social/p.png": "brands/acme/campaigns/spring/designs/social/p.png",
    "brands/acme/campaigns/spring/assets/batch-1/m.json": "brands/acme/campaigns/spring/designs/batch-1/m.json",
    "brands/acme/videos/t.mp4": "brands/acme/videos/short-form/t.mp4",
    "brands/acme/videos/clips/s1/c.json": "brands/acme/videos/clips/s1/c.json",
    "brands/acme/videos/.work/1/a.mp4": "brands/acme/videos/.work/1/a.mp4",
    "brands/acme/videos/spring/short-form/a.mp4": "brands/acme/campaigns/spring/videos/short-form/a.mp4",
    "brands/acme/videos/spring/series/how-to/e1.mp4": "brands/acme/campaigns/spring/videos/series/how-to/e1.mp4",
    "brands/acme/videos/brand-story/scene-plan.json": "brands/acme/videos/long-form/brand-story/scene-plan.json",
    "brands/acme/exports/spring/ig/a.jpg": "brands/acme/campaigns/spring/exports/ig/a.jpg",
    "brands/acme/exports/loose.jpg": "brands/acme/exports/loose.jpg",
    "brands/acme/guidelines.md": "brands/acme/guidelines.md",
}


@pytest.fixture
def lay(tmp_path):
    return pp.Layout(json.loads(json.dumps(LAYOUT)), tmp_path)


@pytest.mark.parametrize("old,new", FORWARD.items())
def test_forward(lay, tmp_path, old, new):
    assert lay.forward(old)[0] == tmp_path / "paw-suites/creative" / new


def test_secrets_stay_hidden(lay, tmp_path):
    assert lay.forward(".auth/session.json")[0] == tmp_path / ".pawbytes/creative/.auth/session.json"
    assert lay.forward(".profiles/strategist/x")[0] == tmp_path / ".pawbytes/creative/.profiles/strategist/x"


@pytest.mark.parametrize("new,old", [
    ("brands/acme/videos/short-form/n.mp4", "brands/acme/videos/n.mp4"),
    ("brands/acme/campaigns/spring/designs/social/n.png", "brands/acme/assets/spring/social/n.png"),
    ("brands/acme/campaigns/spring/designs/batch-2/n.png", "brands/acme/campaigns/spring/assets/batch-2/n.png"),
    ("brands/acme/campaigns/spring/videos/short-form/n.mp4", "brands/acme/videos/spring/short-form/n.mp4"),
    ("_memory/daily/2026-11-05.md", "daily/2026-11-05.md"),
])
def test_legacy_write_goes_to_canonical_old_path(lay, tmp_path, new, old):
    (tmp_path / ".pawbytes/creative-suites/index.md").parent.mkdir(parents=True)
    (tmp_path / ".pawbytes/creative-suites/index.md").write_text("x", encoding="utf-8")
    assert Path(pp.locate(lay, new, write=True)["path"]) == tmp_path / ".pawbytes/creative-suites" / old


def test_config_default_rewritten():
    keys = {k["key"]: k for k in LAYOUT["config_keys"]}
    assert keys["output_directory"]["new"] == "{project-root}/paw-suites/creative"
