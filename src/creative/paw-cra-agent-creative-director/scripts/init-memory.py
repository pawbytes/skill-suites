#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Memory Initialization Script for Aria Creative Suite
Creates the suite tree at paw-suites/creative/ (or --suite-root): _memory/ with
index.md, daily/ and knowledge/, plus brands/.
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone


SUITE_ROOT = Path("paw-suites") / "creative"


def create_memory_structure(root_path: Path, suite_root: Path | None = None) -> dict:
    """Create the suite folder structure under the project root (or an explicit suite root)."""
    base = suite_root if suite_root else root_path / SUITE_ROOT
    memory = base / "_memory"

    folders = [
        base,
        memory,
        memory / "daily",
        memory / "knowledge",
        base / "brands",
    ]

    created = []
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        created.append(str(folder))

    return {
        "base": str(base),
        "memory": str(memory),
        "folders": created
    }


def create_index(memory: Path) -> bool:
    """Create the initial index.md file in the memory folder."""
    index_path = memory / "index.md"

    if index_path.exists():
        return False

    today = datetime.now().strftime("%Y-%m-%d")

    content = f"""# Creative Suites Index

## Tool Status
- fal: unknown
- elevenlabs: unknown
- pexels: unknown
- ffmpeg: unknown

## Active Brand
_none_

## Active Campaigns
_none_

## Recent Activity
- {today}: Memory initialized

## Notes
Run tool discovery to update tool status. Onboard a brand to set active brand.
"""

    index_path.write_text(content, encoding="utf-8")
    return True


def create_daily_log(memory: Path) -> bool:
    """Create today's daily log file in the memory folder."""
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = memory / "daily" / f"{today}.md"

    if log_path.exists():
        return False

    content = f"""# {today}

## Session Log

### Initialized
Memory structure created by Aria.

---
"""

    log_path.write_text(content, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Initialize Aria Creative Suite memory structure"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Project root path (default: current directory)"
    )
    parser.add_argument(
        "--suite-root",
        help="Suite folder when config cra.output_directory sets one (default: <path>/paw-suites/creative)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output JSON file path (default: stdout)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Include additional details"
    )

    args = parser.parse_args()

    root_path = Path(args.path).resolve()

    # Create structure
    suite_root = Path(args.suite_root).resolve() if args.suite_root else None
    result = create_memory_structure(root_path, suite_root)

    memory = Path(result["memory"])
    index_created = create_index(memory)
    log_created = create_daily_log(memory)

    # Build output
    output = {
        "script": "init-memory",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "success",
        "project_root": str(root_path),
        "suite_root": result["base"],
        "memory_base": result["memory"],
        "folders_created": len(result["folders"]),
        "files": {
            "index.md": "created" if index_created else "exists",
            "daily_log": "created" if log_created else "exists"
        }
    }

    if args.verbose:
        output["structure"] = result["folders"]

    json_output = json.dumps(output, indent=2)

    if args.output:
        Path(args.output).write_text(json_output, encoding="utf-8")
    else:
        print(json_output)

    return 0


if __name__ == "__main__":
    sys.exit(main())