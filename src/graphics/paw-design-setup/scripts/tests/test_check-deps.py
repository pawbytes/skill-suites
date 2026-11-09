"""check-deps.py: fixes never carry secrets; quick mode skips the browser probe."""
import importlib.util
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_deps", SCRIPTS / "check-deps.py")
cd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cd)


def test_env_fix_has_placeholder_only(monkeypatch):
    monkeypatch.setenv("FAL_KEY", "secret-value")
    for fam in ("windows", "macos", "linux"):
        text = cd.env_fix("FAL_KEY", fam, "https://fal.ai")
        assert "<your-key>" in text and "secret-value" not in text


def test_quick_report_shape(monkeypatch):
    monkeypatch.delenv("FAL_KEY", raising=False)
    args = type("A", (), {"project_root": ".", "image_provider": "codex-cli", "codex_path": None, "quick": True})()
    rep = cd.check(args)
    assert rep["checks"]["chromium"]["skipped"] and "codex" in rep["checks"]
    assert rep["checks"]["fal_key"]["required"] is False
    assert "fal_key" in rep["summary"]["missing_optional"]
