#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest>=7.0"]
# ///
"""Unit tests for content-calendar-generator.py"""

import subprocess
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).parent.parent / "content-calendar-generator.py"


def test_help_flag():
    """Test that --help works and shows usage."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Content Calendar Generator" in result.stdout or "content-calendar" in result.stdout.lower()


def test_default_calendar():
    """Test default calendar generation."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--weeks", "1"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "# Content Calendar" in result.stdout
    assert "## Overview" in result.stdout
    assert "## Weekly Schedule" in result.stdout


def test_custom_platforms():
    """Test calendar with custom platforms."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--platforms", "Instagram,TikTok", "--weeks", "1"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Instagram" in result.stdout
    assert "TikTok" in result.stdout


def test_custom_pillars():
    """Test calendar with custom content pillars."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--pillars", "Education,Inspiration", "--weeks", "1"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Education" in result.stdout
    assert "Inspiration" in result.stdout


def test_asset_summary():
    """Test that asset requirements summary is generated."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--weeks", "1"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "## Asset Requirements Summary" in result.stdout


def test_custom_start_date():
    """Test calendar with custom start date."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--start-date", "2026-01-01", "--weeks", "1"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "2026-01-01" in result.stdout


def test_invalid_date_format():
    """Test that invalid date format returns error."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--start-date", "not-a-date"],
        capture_output=True,
        text=True
    )

    # Should return error code
    assert result.returncode != 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])