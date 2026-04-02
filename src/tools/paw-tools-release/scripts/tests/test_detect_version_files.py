"""Tests for detect_version_files.py"""

import json
import pytest
from pathlib import Path
import sys

# Add parent directory to path for import
sys.path.insert(0, str(Path(__file__).parent.parent))
from detect_version_files import detect_version_files, extract_version, VERSION_PATTERNS


@pytest.fixture
def temp_project(tmp_path):
    """Create a temporary project structure for testing."""
    return tmp_path


def test_detect_package_json(temp_project):
    """Test detection of package.json version."""
    package_json = temp_project / "package.json"
    package_json.write_text(json.dumps({
        "name": "test-package",
        "version": "1.2.3"
    }))

    files = detect_version_files(temp_project)
    assert len(files) == 1
    assert files[0].file_type == "package.json"
    assert files[0].current_version == "1.2.3"


def test_detect_cargo_toml(temp_project):
    """Test detection of Cargo.toml version."""
    cargo_toml = temp_project / "Cargo.toml"
    cargo_toml.write_text('[package]\nname = "test"\nversion = "0.1.0"\n')

    files = detect_version_files(temp_project)
    assert len(files) == 1
    assert files[0].file_type == "Cargo.toml"
    assert files[0].current_version == "0.1.0"


def test_detect_pyproject_toml(temp_project):
    """Test detection of pyproject.toml version."""
    pyproject = temp_project / "pyproject.toml"
    pyproject.write_text('[project]\nname = "test"\nversion = "2.0.0"\n')

    files = detect_version_files(temp_project)
    assert len(files) == 1
    assert files[0].file_type == "pyproject.toml"
    assert files[0].current_version == "2.0.0"


def test_detect_version_file(temp_project):
    """Test detection of VERSION file."""
    version_file = temp_project / "VERSION"
    version_file.write_text("1.0.0-beta.1\n")

    files = detect_version_files(temp_project)
    assert len(files) == 1
    assert files[0].file_type == "VERSION"
    assert files[0].current_version == "1.0.0-beta.1"


def test_detect_multiple_files(temp_project):
    """Test detection of multiple version files."""
    # Create multiple version files
    (temp_project / "package.json").write_text(json.dumps({"version": "1.0.0"}))
    (temp_project / "VERSION").write_text("1.0.0\n")

    files = detect_version_files(temp_project)
    assert len(files) == 2


def test_no_version_files(temp_project):
    """Test handling when no version files exist."""
    files = detect_version_files(temp_project)
    assert len(files) == 0


def test_extract_version_invalid_json(temp_project):
    """Test handling of malformed JSON."""
    package_json = temp_project / "package.json"
    package_json.write_text('{"version": "1.0.0"')  # Missing closing brace

    # Should fall back to regex extraction
    version = extract_version(package_json, VERSION_PATTERNS["package.json"]["pattern"])
    assert version == "1.0.0"


def test_version_file_with_prerelease(temp_project):
    """Test VERSION file with pre-release suffix."""
    version_file = temp_project / "VERSION"
    version_file.write_text("2.1.0-rc.2\n")

    files = detect_version_files(temp_project)
    assert files[0].current_version == "2.1.0-rc.2"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])