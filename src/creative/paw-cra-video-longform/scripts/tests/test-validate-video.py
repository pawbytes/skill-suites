#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""Tests for validate-video.py"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).parent.parent / "validate-video.py"


def run_script(*args: str) -> tuple[int, dict | None, str]:
    """Run validate-video.py and return (exit_code, parsed_json, stderr)."""
    cmd = [sys.executable, str(SCRIPT_PATH)] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    try:
        parsed = json.loads(result.stdout) if result.stdout.strip() else None
    except json.JSONDecodeError:
        parsed = None
    return result.returncode, parsed, result.stderr


def test_help():
    """--help should exit 0 and show usage."""
    code, _, stderr = run_script("--help")
    # argparse prints help to stdout, exits 0
    assert code == 0, f"Expected exit 0 for --help, got {code}"
    print("  PASS: --help exits 0")


def test_missing_file():
    """Non-existent file should produce critical finding and exit 1."""
    code, data, _ = run_script("/nonexistent/video.mp4")
    assert code == 1, f"Expected exit 1 for missing file, got {code}"
    assert data is not None, "Expected JSON output"
    assert data["status"] == "fail"
    assert data["summary"]["critical"] >= 1
    assert data["script"] == "validate-video"
    assert data["version"] == "1.0.0"
    print("  PASS: Missing file returns critical failure")


def test_json_structure():
    """Output should have all required fields."""
    _, data, _ = run_script("/nonexistent/video.mp4")
    assert data is not None
    required_keys = {"script", "version", "video_path", "timestamp", "status", "findings", "summary"}
    missing = required_keys - set(data.keys())
    assert not missing, f"Missing keys in output: {missing}"
    summary_keys = {"total", "critical", "high", "medium", "low"}
    missing_summary = summary_keys - set(data["summary"].keys())
    assert not missing_summary, f"Missing summary keys: {missing_summary}"
    print("  PASS: JSON structure is complete")


def main():
    print("Running validate-video.py tests...")
    tests = [test_help, test_missing_file, test_json_structure]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  FAIL: {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {test.__name__}: {e}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
