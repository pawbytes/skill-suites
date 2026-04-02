#!/usr/bin/env python3
"""Unit tests for cleanup-legacy.py"""
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

# Load the module with hyphen in filename
script_path = Path(__file__).parent.parent / "cleanup-legacy.py"
spec = importlib.util.spec_from_file_location("cleanup_legacy", script_path)
cl = importlib.util.module_from_spec(spec)
sys.modules["cleanup_legacy"] = cl
spec.loader.exec_module(cl)


class TestFindSkillDirs:
    """Tests for find_skill_dirs function."""

    def test_nonexistent_directory(self):
        """Should return empty list for nonexistent directory."""
        result = cl.find_skill_dirs("/nonexistent/path")
        assert result == []

    def test_empty_directory(self):
        """Should return empty list for directory with no skills."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = cl.find_skill_dirs(tmpdir)
            assert result == []

    def test_finds_skill_directory(self):
        """Should find directories containing SKILL.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            skill_dir = Path(tmpdir) / "my-skill"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text("---\nname: test\n---\n")

            result = cl.find_skill_dirs(tmpdir)
            assert "my-skill" in result

    def test_finds_nested_skills(self):
        """Should find skills in nested directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            nested = Path(tmpdir) / "module" / "nested-skill"
            nested.mkdir(parents=True)
            (nested / "SKILL.md").write_text("---\nname: test\n---\n")

            result = cl.find_skill_dirs(tmpdir)
            assert "nested-skill" in result


class TestCountFiles:
    """Tests for count_files function."""

    def test_empty_directory(self):
        """Should return 0 for empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = cl.count_files(Path(tmpdir))
            assert result == 0

    def test_counts_files(self):
        """Should count files correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "file1.txt").write_text("a")
            (Path(tmpdir) / "file2.txt").write_text("b")

            result = cl.count_files(Path(tmpdir))
            assert result == 2

    def test_counts_nested_files(self):
        """Should count files in nested directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            subdir = Path(tmpdir) / "sub"
            subdir.mkdir()
            (subdir / "file.txt").write_text("a")

            result = cl.count_files(Path(tmpdir))
            assert result == 1


class TestCleanupDirectories:
    """Tests for cleanup_directories function."""

    def test_removes_directory(self):
        """Should remove specified directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "to-remove"
            target.mkdir()
            (target / "file.txt").write_text("content")

            removed, not_found, files = cl.cleanup_directories(
                tmpdir, ["to-remove"], verbose=False
            )

            assert "to-remove" in removed
            assert not target.exists()

    def test_handles_missing_directory(self):
        """Should report missing directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            removed, not_found, files = cl.cleanup_directories(
                tmpdir, ["nonexistent"], verbose=False
            )

            assert "nonexistent" in not_found


class TestParseArgs:
    """Tests for parse_args function."""

    def test_required_args(self):
        """Should require bmad-dir and module-code."""
        sys.argv = [
            "cleanup-legacy.py",
            "--bmad-dir", "/path/to/_bmad",
            "--module-code", "bmb",
        ]
        args = cl.parse_args()
        assert args.bmad_dir == "/path/to/_bmad"
        assert args.module_code == "bmb"


def run_tests():
    """Run all tests and report results."""
    test_classes = [
        TestFindSkillDirs,
        TestCountFiles,
        TestCleanupDirectories,
        TestParseArgs,
    ]

    passed = 0
    failed = 0

    for test_class in test_classes:
        instance = test_class()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                try:
                    getattr(instance, method_name)()
                    passed += 1
                    print(f"PASS: {test_class.__name__}.{method_name}")
                except AssertionError as e:
                    failed += 1
                    print(f"FAIL: {test_class.__name__}.{method_name}")
                    print(f"  {e}")

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)