#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""
Unit tests for tool-discovery.py
"""

import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import module with hyphen in name
import importlib.util
spec = importlib.util.spec_from_file_location("tool_discovery", Path(__file__).parent.parent / "tool-discovery.py")
tool_discovery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool_discovery)

check_cli_tool = tool_discovery.check_cli_tool
check_cli_tool_version = tool_discovery.check_cli_tool_version
check_ffmpeg = tool_discovery.check_ffmpeg
check_agent_browser = tool_discovery.check_agent_browser
check_api_keys = tool_discovery.check_api_keys
load_config = tool_discovery.load_config


class TestCheckCliTool:
    """Tests for check_cli_tool function."""

    def test_returns_available_for_existing_tool(self):
        """Should return available for tools on PATH."""
        # Python should always be available
        result = check_cli_tool("python")

        assert result["name"] == "python"
        assert result["status"] == "available"
        assert result["path"] is not None

    def test_returns_unavailable_for_nonexistent_tool(self):
        """Should return unavailable for tools not on PATH."""
        result = check_cli_tool("this-tool-definitely-does-not-exist-xyz123")

        assert result["name"] == "this-tool-definitely-does-not-exist-xyz123"
        assert result["status"] == "unavailable"
        assert result["path"] is None


class TestCheckCliToolVersion:
    """Tests for check_cli_tool_version function."""

    def test_extracts_version(self):
        """Should extract version from tool output."""
        result = check_cli_tool_version("python", "--version")

        assert result["status"] == "available"
        assert "version" in result
        # Python version should be something like 3.x.x
        assert "." in result.get("version", "")


class TestCheckFfmpeg:
    """Tests for check_ffmpeg function."""

    def test_returns_unavailable_when_not_installed(self):
        """Should return unavailable if ffmpeg not on PATH."""
        with patch("shutil.which", return_value=None):
            result = check_ffmpeg()

        assert result["status"] == "unavailable"


class TestCheckAgentBrowser:
    """Tests for check_agent_browser function."""

    def test_includes_install_command(self):
        """Should include install command in result."""
        with patch("shutil.which", return_value=None):
            result = check_agent_browser()

        assert "install_command" in result
        assert "npm install" in result["install_command"]

    def test_includes_purpose(self):
        """Should include purpose description."""
        result = check_agent_browser()

        assert "purpose" in result
        assert "browser" in result["purpose"].lower()


class TestLoadConfig:
    """Tests for load_config function."""

    def test_loads_yaml_config(self, tmp_path: Path):
        """Should load config from YAML file."""
        config_dir = tmp_path / "_bmad"
        config_dir.mkdir()

        config_file = config_dir / "config.user.yaml"
        config_file.write_text("""
fal_key: "test-key-12345"
pexels_api_key: "test-pexels-key"
""", encoding="utf-8")

        # Change to temp directory to test config loading
        import os
        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            config = load_config()
            assert config.get("fal_key") == "test-key-12345"
        finally:
            os.chdir(original_cwd)

    def test_returns_empty_dict_when_no_config(self, tmp_path: Path):
        """Should return empty dict when config doesn't exist."""
        import os
        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            config = load_config()
            assert isinstance(config, dict)
        finally:
            os.chdir(original_cwd)


class TestCheckApiKeys:
    """Tests for check_api_keys function."""

    def test_detects_available_key(self):
        """Should detect valid API key."""
        config = {
            "fal_key": "a-valid-key-with-sufficient-length",
            "elevenlabs_api_key": "",
            "pexels_api_key": "another-valid-key-here"
        }

        results = check_api_keys(config)

        fal_result = next(r for r in results if r["key"] == "fal_key")
        assert fal_result["status"] == "available"

        pexels_result = next(r for r in results if r["key"] == "pexels_api_key")
        assert pexels_result["status"] == "available"

    def test_detects_unavailable_key(self):
        """Should detect missing or placeholder keys."""
        config = {
            "fal_key": "your_api_key_here",  # Placeholder
            "elevenlabs_api_key": "",  # Empty
            "pexels_api_key": "short"  # Too short
        }

        results = check_api_keys(config)

        for result in results:
            assert result["status"] == "unavailable"

    def test_returns_all_expected_keys(self):
        """Should return all expected API keys."""
        results = check_api_keys({})

        key_names = {r["key"] for r in results}
        assert "fal_key" in key_names
        assert "elevenlabs_api_key" in key_names
        assert "pexels_api_key" in key_names


class TestCLI:
    """Tests for CLI interface."""

    def test_output_to_stdout(self, tmp_path: Path):
        """Should output JSON to stdout by default."""
        import subprocess
        import os

        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = subprocess.run(
                [sys.executable, str(Path(__file__).parent.parent / "tool-discovery.py")],
                capture_output=True,
                text=True,
                timeout=30
            )

            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert "cli_tools" in output
            assert "api_keys" in output
        finally:
            os.chdir(original_cwd)

    def test_output_to_file(self, tmp_path: Path):
        """Should write JSON to file when -o specified."""
        import subprocess
        import os

        output_file = tmp_path / "output.json"

        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = subprocess.run(
                [sys.executable, str(Path(__file__).parent.parent / "tool-discovery.py"),
                 "-o", str(output_file)],
                capture_output=True,
                text=True,
                timeout=30
            )

            assert result.returncode == 0
            assert output_file.exists()

            data = json.loads(output_file.read_text(encoding="utf-8"))
            assert "script" in data
            assert data["script"] == "tool-discovery"
        finally:
            os.chdir(original_cwd)

    def test_verbose_flag(self, tmp_path: Path):
        """Should include additional details with --verbose."""
        import subprocess
        import os

        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = subprocess.run(
                [sys.executable, str(Path(__file__).parent.parent / "tool-discovery.py"), "--verbose"],
                capture_output=True,
                text=True,
                timeout=30
            )

            output = json.loads(result.stdout)
            assert "config_loaded" in output
        finally:
            os.chdir(original_cwd)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])