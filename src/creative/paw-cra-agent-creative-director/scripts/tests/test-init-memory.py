#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""
Unit tests for init-memory.py
"""

import json
import sys
import tempfile
from pathlib import Path

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import module with hyphen in name
import importlib.util
spec = importlib.util.spec_from_file_location("init_memory", Path(__file__).parent.parent / "init-memory.py")
init_memory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(init_memory)

create_memory_structure = init_memory.create_memory_structure
create_index = init_memory.create_index
create_daily_log = init_memory.create_daily_log


class TestCreateMemoryStructure:
    """Tests for create_memory_structure function."""

    def test_creates_all_folders(self, tmp_path: Path):
        """Should create all required folders."""
        result = create_memory_structure(tmp_path)

        assert result["base"] == str(tmp_path / ".pawbytes" / "creative-suites")
        assert len(result["folders"]) == 5

        # Verify all folders exist
        base = Path(result["base"])
        assert (base).exists()
        assert (base / "brands").exists()
        assert (base / "campaigns").exists()
        assert (base / "briefs").exists()
        assert (base / "daily").exists()

    def test_idempotent_creation(self, tmp_path: Path):
        """Should not fail if folders already exist."""
        result1 = create_memory_structure(tmp_path)
        # Second call should succeed and return same base
        result2 = create_memory_structure(tmp_path)
        assert result1["base"] == result2["base"]

    def test_creates_nested_structure(self, tmp_path: Path):
        """Should create .pawbytes/creative-suites nested path."""
        result = create_memory_structure(tmp_path)

        base = Path(result["base"])
        assert ".pawbytes" in str(base)
        assert "creative-suites" in str(base)


class TestCreateIndex:
    """Tests for create_index function."""

    def test_creates_index_file(self, tmp_path: Path):
        """Should create index.md file."""
        result = create_index(tmp_path)

        assert result is True
        assert (tmp_path / "index.md").exists()

    def test_index_contains_required_sections(self, tmp_path: Path):
        """Index should have all required sections."""
        create_index(tmp_path)

        content = (tmp_path / "index.md").read_text(encoding="utf-8")

        assert "## Tool Status" in content
        assert "## Active Brand" in content
        assert "## Active Campaigns" in content
        assert "## Recent Activity" in content

    def test_index_not_overwritten(self, tmp_path: Path):
        """Should not overwrite existing index."""
        create_index(tmp_path)

        # Modify the index
        index_path = tmp_path / "index.md"
        original_content = index_path.read_text(encoding="utf-8")
        modified_content = original_content + "\n## Custom Section"
        index_path.write_text(modified_content, encoding="utf-8")

        # Second call should not overwrite
        result = create_index(tmp_path)
        assert result is False

        # Content should still have our modification
        current_content = index_path.read_text(encoding="utf-8")
        assert "## Custom Section" in current_content


class TestCreateDailyLog:
    """Tests for create_daily_log function."""

    def test_creates_daily_log(self, tmp_path: Path):
        """Should create daily log file."""
        # First create the structure
        result = create_memory_structure(tmp_path)
        base = Path(result["base"])

        log_result = create_daily_log(base)

        assert log_result is True

        # Find the log file
        daily_dir = base / "daily"
        log_files = list(daily_dir.glob("*.md"))
        assert len(log_files) == 1

    def test_log_has_correct_format(self, tmp_path: Path):
        """Daily log should have expected format."""
        result = create_memory_structure(tmp_path)
        base = Path(result["base"])
        create_daily_log(base)

        daily_dir = base / "daily"
        log_file = list(daily_dir.glob("*.md"))[0]
        content = log_file.read_text(encoding="utf-8")

        assert "# " in content  # Has title
        assert "## Session Log" in content

    def test_log_not_overwritten(self, tmp_path: Path):
        """Should not overwrite existing daily log."""
        result = create_memory_structure(tmp_path)
        base = Path(result["base"])
        create_daily_log(base)

        # Modify the log
        daily_dir = base / "daily"
        log_file = list(daily_dir.glob("*.md"))[0]
        original = log_file.read_text(encoding="utf-8")
        log_file.write_text(original + "\nTest entry", encoding="utf-8")

        # Second call should return False
        log_result = create_daily_log(base)
        assert log_result is False


class TestCLI:
    """Tests for CLI interface."""

    def test_output_to_stdout(self, tmp_path: Path, capsys):
        """Should output JSON to stdout by default."""
        import subprocess
        result = subprocess.run(
            [sys.executable, str(Path(__file__).parent.parent / "init-memory.py"), str(tmp_path)],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = json.loads(result.stdout)
        assert output["status"] == "success"

    def test_output_to_file(self, tmp_path: Path):
        """Should write JSON to file when -o specified."""
        import subprocess
        output_file = tmp_path / "output.json"

        result = subprocess.run(
            [sys.executable, str(Path(__file__).parent.parent / "init-memory.py"),
             str(tmp_path / "project"), "-o", str(output_file)],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        assert output_file.exists()

        data = json.loads(output_file.read_text(encoding="utf-8"))
        assert data["status"] == "success"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])