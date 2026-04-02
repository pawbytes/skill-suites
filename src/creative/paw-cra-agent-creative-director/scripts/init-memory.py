#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Memory Initialization Script for Aria Creative Suite
Creates the shared memory structure at .pawbytes/creative-suites/
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone


def create_memory_structure(root_path: Path) -> dict:
    """Create the memory folder structure."""
    base = root_path / ".pawbytes" / "creative-suites"

    folders = [
        base,
        base / "brands",
        base / "campaigns",
        base / "briefs",
        base / "daily",
    ]

    created = []
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        created.append(str(folder))

    return {
        "base": str(base),
        "folders": created
    }


def create_index(base: Path) -> bool:
    """Create the initial index.md file."""
    index_path = base / "index.md"

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


def create_daily_log(base: Path) -> bool:
    """Create today's daily log file."""
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = base / "daily" / f"{today}.md"

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
    result = create_memory_structure(root_path)

    base = Path(result["base"])
    index_created = create_index(base)
    log_created = create_daily_log(base)

    # Build output
    output = {
        "script": "init-memory",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "success",
        "project_root": str(root_path),
        "memory_base": result["base"],
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