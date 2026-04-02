#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["tomli>=2.0.0;python_version<'3.11'"]
# ///
"""
Detect and parse version files in a project.

Scans for common version file patterns and outputs their current versions.
Supports package.json, Cargo.toml, pyproject.toml, VERSION, __version__.py, setup.py.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# For Python < 3.11, use tomli; for 3.11+, use tomllib
try:
    import tomllib
except ImportError:
    import tomli as tomllib


@dataclass
class VersionFile:
    path: Path
    file_type: str
    current_version: str
    field_path: str  # How to update the version (e.g., "version", "project.version")


VERSION_PATTERNS = {
    "package.json": {
        "pattern": r'"version"\s*:\s*"([^"]+)"',
        "field": "version",
    },
    "Cargo.toml": {
        "pattern": r'^version\s*=\s*"([^"]+)"',
        "field": "version",
    },
    "pyproject.toml": {
        "pattern": r'version\s*=\s*"([^"]+)"',
        "field": "version",
    },
    "VERSION": {
        "pattern": r'^(\d+\.\d+\.\d+[-\w]*)$',
        "field": "content",
    },
    "__version__.py": {
        "pattern": r'__version__\s*=\s*["\']([^"\']+)["\']',
        "field": "__version__",
    },
    "setup.py": {
        "pattern": r'version\s*=\s*["\']([^"\']+)["\']',
        "field": "version",
    },
    "setup.cfg": {
        "pattern": r'^version\s*=\s*(.+)$',
        "field": "version",
    },
}


def detect_version_files(project_root: Path) -> list[VersionFile]:
    """Scan project root for version files."""
    found = []

    for filename, config in VERSION_PATTERNS.items():
        # Check multiple possible locations
        candidates = [
            project_root / filename,
            project_root / "src" / filename,
        ]

        # For Python packages, also check package directory
        if filename in ("__version__.py", "setup.py"):
            # Find any __version__.py in src/ or package directories
            for py_file in project_root.rglob(filename):
                candidates.append(py_file)

        for candidate in candidates:
            if candidate.exists() and candidate.is_file():
                version = extract_version(candidate, config["pattern"])
                if version:
                    found.append(VersionFile(
                        path=candidate,
                        file_type=filename,
                        current_version=version,
                        field_path=config["field"],
                    ))

    return found


def extract_version(file_path: Path, pattern: str) -> Optional[str]:
    """Extract version string from file."""
    content = file_path.read_text(encoding="utf-8")

    # For VERSION file, the entire content IS the version
    if file_path.name == "VERSION":
        content = content.strip()
        # Simple semver pattern check
        if re.match(r'^\d+\.\d+\.\d+[-\w.]*$', content):
            return content
        return None

    # For pyproject.toml, try structured parsing first
    if file_path.name == "pyproject.toml":
        try:
            data = tomllib.loads(content)
            # Check project.version (PEP 621)
            if "project" in data and "version" in data["project"]:
                return data["project"]["version"]
            # Check poetry.tool.version
            if "tool" in data and "poetry" in data["tool"] and "version" in data["tool"]["poetry"]:
                return data["tool"]["poetry"]["version"]
        except Exception:
            pass  # Fall back to regex

    # For package.json, use JSON parsing
    if file_path.name == "package.json":
        try:
            data = json.loads(content)
            if "version" in data:
                return data["version"]
        except json.JSONDecodeError:
            pass  # Fall back to regex

    # Regex fallback
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        return match.group(1)

    return None


def output_json(files: list[VersionFile], project_root: Path) -> dict:
    """Format output as JSON."""
    return {
        "script": "detect_version_files",
        "version": "1.0.0",
        "project_root": str(project_root),
        "files": [
            {
                "path": str(f.path),
                "relative_path": str(f.path.relative_to(project_root)),
                "type": f.file_type,
                "current_version": f.current_version,
                "field": f.field_path,
            }
            for f in files
        ],
        "count": len(files),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Detect version files in a project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s .
  %(prog)s /path/to/project --json
        """,
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to project root",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON (default: human-readable)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show verbose output",
    )

    args = parser.parse_args()
    project_root = args.path.resolve()

    if not project_root.is_dir():
        print(f"Error: {project_root} is not a directory", file=sys.stderr)
        sys.exit(2)

    files = detect_version_files(project_root)

    if args.json:
        print(json.dumps(output_json(files, project_root), indent=2))
    else:
        if not files:
            print("No version files detected")
            sys.exit(0)

        print(f"Found {len(files)} version file(s):")
        for f in files:
            print(f"  {f.path.relative_to(project_root)}: {f.current_version} ({f.file_type})")


if __name__ == "__main__":
    main()