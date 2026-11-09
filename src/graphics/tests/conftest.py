"""Shared helpers for the PawBytes Graphics Suite tests: load canonical scripts as modules."""
import importlib.util
import sys
from pathlib import Path

import pytest

SUITE = Path(__file__).resolve().parent.parent
SHARED = SUITE / "_shared" / "scripts"


def load(path: Path, name: str):
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def chromium_ok() -> bool:
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            p.chromium.launch().close()
        return True
    except Exception:  # noqa: BLE001
        return False


needs_browser = pytest.mark.skipif(not chromium_ok(), reason="Playwright Chromium not installed")
