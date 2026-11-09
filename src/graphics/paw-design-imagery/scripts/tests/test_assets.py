"""assets.py: imports leave originals untouched; check catches upscaling."""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

SCRIPTS = Path(__file__).resolve().parents[1]


def run(*args):
    p = subprocess.run([sys.executable, str(SCRIPTS / "assets.py"), *args], capture_output=True, text=True,
                       encoding="utf-8")
    return p.returncode, json.loads(p.stdout or p.stderr)


def _project(tmp_path):
    subprocess.run([sys.executable, str(SCRIPTS / "production.py"), "init", "--root", str(tmp_path), "--slug", "p",
                    "--title", "P", "--profile", "social-post"], check=True, capture_output=True)
    p = tmp_path / "p"
    layout = {"frames": [{"id": "p01--instagram-feed-portrait", "piece": "p01", "placement": "instagram-feed-portrait",
                          "elements": [{"id": "hero", "role": "image", "box": [0, 0, 1, 1], "asset": "hero"}]}]}
    (p / "layout" / "layout.json").write_text(json.dumps(layout), encoding="utf-8")
    return p


def test_import_copies_and_check_flags_small_image(tmp_path):
    p = _project(tmp_path)
    src = tmp_path / "photo.png"
    Image.new("RGB", (400, 500), "#888").save(src)
    before = src.read_bytes()
    code, res = run("import", "--project", str(p), "--file", str(src), "--name", "hero", "--kind", "photo")
    assert code == 0 and res["path"] == "imagery/source/photo.png" and src.read_bytes() == before
    code, res = run("check", "--project", str(p))
    assert code == 1 and "upscaled" in res["problems"][0]


def test_check_passes_with_big_enough_pick(tmp_path):
    p = _project(tmp_path)
    (p / "imagery" / "hero").mkdir(parents=True)
    Image.new("RGB", (1200, 1500), "#888").save(p / "imagery" / "hero" / "take-01.png")
    assert run("pick", "--project", str(p), "--name", "hero", "--path", "imagery/hero/take-01.png",
               "--kind", "hero", "--source", "fal")[0] == 0
    code, res = run("check", "--project", str(p))
    assert code == 0 and res["slots"][0]["need_px"] == [1080, 1350]
