#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Copy the canonical shared files into every skill that bundles them.

Edit src/graphics/_shared/<scripts|assets>/<file>, then run `uv run src/graphics/_shared/sync.py`.
Skills are installed one by one from the marketplace, so each carries its own copy;
src/graphics/tests/test_shared_copies.py fails when a copy drifts.

Output: JSON with the copies that drifted and the ones written. `--check` writes
nothing and exits 1 on drift.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

SHARED = Path(__file__).resolve().parent
SUITE = SHARED.parent

STAGE_SKILLS = ["paw-design-agent-director", "paw-design-concept", "paw-design-style", "paw-design-layout",
                "paw-design-imagery", "paw-design-compose", "paw-design-deliver"]
IMAGE_SKILLS = ["paw-design-style", "paw-design-imagery"]
SPEC_SKILLS = ["paw-design-agent-director", "paw-design-layout", "paw-design-imagery", "paw-design-compose", "paw-design-deliver"]
RENDER_SKILLS = ["paw-design-style", "paw-design-layout", "paw-design-compose", "paw-design-deliver"]
QC_SKILLS = ["paw-design-layout", "paw-design-compose", "paw-design-deliver"]

COPIES = {
    "scripts/production.py": STAGE_SKILLS,
    "scripts/fal.py": IMAGE_SKILLS,
    "scripts/codex_image.py": IMAGE_SKILLS,
    "scripts/specs.py": sorted(set(SPEC_SKILLS + QC_SKILLS)),
    "assets/platform-specs.json": sorted(set(SPEC_SKILLS + QC_SKILLS)),
    "scripts/render.py": RENDER_SKILLS,
    "scripts/qc.py": QC_SKILLS,
    "scripts/frames.py": ["paw-design-layout", "paw-design-imagery", "paw-design-compose", "paw-design-deliver"],
}


def plan() -> list[tuple[Path, Path]]:
    pairs = []
    for rel, skills in COPIES.items():
        for skill in skills:
            if (SUITE / skill).is_dir():
                pairs.append((SHARED / rel, SUITE / skill / rel))
    return pairs


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true", help="report drift without writing; exit 1 on drift")
    a = p.parse_args(argv)
    drift, written = [], []
    for src, dest in plan():
        if dest.is_file() and dest.read_bytes() == src.read_bytes():
            continue
        drift.append(str(dest.relative_to(SUITE)))
        if not a.check:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
            written.append(str(dest.relative_to(SUITE)))
    print(json.dumps({"ok": not (a.check and drift), "drift": drift, "written": written}, indent=2))
    sys.exit(1 if a.check and drift else 0)


if __name__ == "__main__":
    main()
