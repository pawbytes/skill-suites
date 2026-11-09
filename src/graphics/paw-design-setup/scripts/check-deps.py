#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check the machine dependencies of PawBytes Graphics Suite and print one JSON report.

Checks: uv; Playwright with its Chromium build (probed with `uv run --with playwright`, which
may download Playwright into the uv cache the first time; skip with --quick); FAL_KEY
(presence only, the value is never read into the report); the Codex CLI when
--image-provider codex-cli (searched like `codex_image.py find`: --codex-path, $CODEX_PATH,
PATH, %LOCALAPPDATA%/OpenAI/Codex/bin/*/codex.exe); whether fonts.googleapis.com answers,
because tokens.css loads Google Fonts at render time; and Ghostscript, optional, for
converting print PDFs to CMYK.

Each check reports `ok`, what was found, `required`, `needed_for`, and `fix`: the exact
command for this OS, or null when ok. The report never blocks setup; the caller decides.

Output: JSON on stdout, exit 0 whenever the check ran. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

PROBE = ("from playwright.sync_api import sync_playwright\n"
         "with sync_playwright() as p:\n"
         "    b = p.chromium.launch(); print(b.version); b.close()\n")


def os_family(platform: str) -> str:
    if platform.startswith("win"):
        return "windows"
    return "macos" if platform == "darwin" else "linux"


def env_fix(name: str, family: str, where: str) -> str:
    """How to set an environment variable on this OS, with a placeholder, never a value."""
    if family == "windows":
        return (f'PowerShell, this session: $env:{name} = "<your-key>"; persist for new terminals: '
                f'setx {name} "<your-key>" (then restart the terminal and the agent). Get a key at {where}')
    profile = "~/.zshrc" if family == "macos" else "~/.bashrc (or ~/.zshrc)"
    return f'Add export {name}="<your-key>" to {profile}, then open a new terminal. Get a key at {where}'


FIXES = {
    "uv": {"windows": 'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"',
           "macos": "curl -LsSf https://astral.sh/uv/install.sh | sh  (or brew install uv)",
           "linux": "curl -LsSf https://astral.sh/uv/install.sh | sh"},
    "chromium": {k: "uv run --with playwright python -m playwright install chromium"
                 for k in ("windows", "macos", "linux")},
    "ghostscript": {"windows": "winget install ArtifexSoftware.GhostScript",
                    "macos": "brew install ghostscript", "linux": "sudo apt install ghostscript"},
    "codex": {k: "npm install -g @openai/codex  (or install the Codex app), then sign in with `codex login`"
              for k in ("windows", "macos", "linux")},
}


def run(cmd: list[str], timeout: int = 60) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or p.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)


def find_codex(explicit: str | None) -> str | None:
    cands = [explicit, os.environ.get("CODEX_PATH"), shutil.which("codex")]
    local = os.environ.get("LOCALAPPDATA")
    if local:
        cands += sorted(glob.glob(os.path.join(local, "OpenAI", "Codex", "bin", "*", "codex.exe")),
                        key=os.path.getmtime, reverse=True)
    return next((c for c in cands if c and Path(c).is_file()), None)


def check(a) -> dict:
    fam = os_family(sys.platform)
    checks: dict[str, dict] = {}
    uv = shutil.which("uv")
    checks["uv"] = {"ok": bool(uv), "found": uv, "required": True,
                    "needed_for": "every script in the suite (`uv run`)", "fix": None if uv else FIXES["uv"][fam]}
    if a.quick or not uv:
        checks["chromium"] = {"ok": False, "skipped": True, "required": True, "found": None,
                              "needed_for": "rendering every wireframe, design and export",
                              "fix": FIXES["chromium"][fam]}
    else:
        code, text = run([uv, "run", "--quiet", "--with", "playwright", "python", "-c", PROBE], timeout=600)
        ok = code == 0
        checks["chromium"] = {"ok": ok, "found": text.splitlines()[-1] if ok and text else None, "required": True,
                              "needed_for": "rendering every wireframe, design and export",
                              "fix": None if ok else FIXES["chromium"][fam]}
    has_key = bool(os.environ.get("FAL_KEY"))
    checks["fal_key"] = {"ok": has_key, "found": "set" if has_key else None,
                         "required": a.image_provider == "fal",
                         "needed_for": "generated images, background removal and upscaling on fal.ai",
                         "fix": None if has_key else env_fix("FAL_KEY", fam, "https://fal.ai/dashboard/keys")}
    if a.image_provider == "codex-cli":
        found = find_codex(a.codex_path)
        checks["codex"] = {"ok": bool(found), "found": found, "required": True,
                           "needed_for": "images through the Codex CLI (design.image_provider: codex-cli)",
                           "fix": None if found else FIXES["codex"][fam]}
    try:
        with urllib.request.urlopen("https://fonts.googleapis.com/css2?family=Inter", timeout=8) as r:
            fonts_ok = r.status == 200
    except Exception:  # noqa: BLE001
        fonts_ok = False
    checks["google_fonts"] = {"ok": fonts_ok, "found": "reachable" if fonts_ok else None, "required": False,
                              "needed_for": "catalog type pairings load from fonts.googleapis.com at render time",
                              "fix": None if fonts_ok else "Check the network or proxy; offline, lock local brand "
                              "fonts (styles.py lock --font-source local --font-file ...)"}
    gs = shutil.which("gswin64c") or shutil.which("gs")
    checks["ghostscript"] = {"ok": bool(gs), "found": gs, "required": False,
                             "needed_for": "optional CMYK PDF/X conversion of print files (many printers convert)",
                             "fix": None if gs else FIXES["ghostscript"][fam]}
    summary = {"ok": [], "missing_required": [], "missing_optional": [], "skipped": []}
    for name, c in checks.items():
        key = "skipped" if c.get("skipped") else "ok" if c["ok"] else \
            "missing_required" if c["required"] else "missing_optional"
        summary[key].append(name)
    return {"ok": True, "os": fam, "project_root": a.project_root, "image_provider": a.image_provider,
            "checks": checks, "summary": summary}


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--project-root", default=".")
    p.add_argument("--image-provider", choices=["fal", "codex-cli"], default="fal")
    p.add_argument("--codex-path")
    p.add_argument("--quick", action="store_true", help="skip the Playwright/Chromium probe")
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        print(json.dumps(check(a), indent=2, ensure_ascii=False))
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
