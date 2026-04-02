#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest>=7.0"]
# ///
"""Unit tests for research-synthesizer.py"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).parent.parent / "research-synthesizer.py"


def test_help_flag():
    """Test that --help works and shows usage."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Research Synthesizer" in result.stdout or "research-synthesizer" in result.stdout.lower()


def test_basic_synthesis():
    """Test basic synthesis from JSON input."""
    test_input = [
        {
            "title": "Test Source",
            "url": "https://example.com",
            "content": "This is test content for synthesis."
        }
    ]

    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--title", "Test Report"],
        input=json.dumps(test_input),
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "# Test Report" in result.stdout
    assert "Test Source" in result.stdout
    assert "https://example.com" in result.stdout


def test_sources_analyzed_count():
    """Test that source count is correct."""
    test_input = [
        {"title": "Source 1", "url": "https://example.com/1", "content": "Content 1"},
        {"title": "Source 2", "url": "https://example.com/2", "content": "Content 2"},
        {"title": "Source 3", "url": "https://example.com/3", "content": "Content 3"}
    ]

    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        input=json.dumps(test_input),
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Sources analyzed: 3" in result.stdout


def test_handles_wrapped_results():
    """Test handling of results wrapped in a 'results' key."""
    test_input = {
        "results": [
            {"title": "Wrapped Source", "url": "https://example.com", "content": "Wrapped content"}
        ]
    }

    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        input=json.dumps(test_input),
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Wrapped Source" in result.stdout


def test_invalid_json_returns_error():
    """Test that invalid JSON returns error code 2."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        input="not valid json",
        capture_output=True,
        text=True
    )

    assert result.returncode == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])