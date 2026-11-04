#!/usr/bin/env python3
"""Unit tests for merge-help-csv.py"""
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

# Load the module with hyphen in filename
script_path = Path(__file__).parent.parent / "merge-help-csv.py"
spec = importlib.util.spec_from_file_location("merge_help_csv", script_path)
mhc = importlib.util.module_from_spec(spec)
sys.modules["merge_help_csv"] = mhc
spec.loader.exec_module(mhc)


class TestHeader:
    """Tests for CSV header."""

    def test_header_has_required_fields(self):
        """Should have all required fields."""
        assert "module" in mhc.HEADER
        assert "skill" in mhc.HEADER
        assert "display-name" in mhc.HEADER
        assert "description" in mhc.HEADER

    def test_header_length(self):
        """Should have expected number of fields."""
        assert len(mhc.HEADER) == 13


class TestExtractModuleCodes:
    """Tests for extract_module_codes function."""

    def test_empty_rows(self):
        """Should return empty set for empty rows."""
        result = mhc.extract_module_codes([])
        assert result == set()

    def test_extracts_codes(self):
        """Should extract module codes from rows."""
        rows = [
            ["mkt", "skill1", "Skill 1"],
            ["mkt", "skill2", "Skill 2"],
            ["seo", "skill3", "Skill 3"],
        ]
        result = mhc.extract_module_codes(rows)
        assert "mkt" in result
        assert "seo" in result

    def test_strips_whitespace(self):
        """Should strip whitespace from codes."""
        rows = [["  mkt  ", "skill1", "Skill 1"]]
        result = mhc.extract_module_codes(rows)
        assert "mkt" in result


class TestFilterRows:
    """Tests for filter_rows function."""

    def test_filters_by_module_code(self):
        """Should remove rows matching module code."""
        rows = [
            ["mkt", "skill1", "Skill 1"],
            ["seo", "skill2", "Skill 2"],
            ["mkt", "skill3", "Skill 3"],
        ]
        result = mhc.filter_rows(rows, "mkt")
        assert len(result) == 1
        assert result[0][0] == "seo"

    def test_handles_empty_rows(self):
        """Should handle empty rows."""
        rows = [[], ["mkt", "skill1"]]
        result = mhc.filter_rows(rows, "mkt")
        assert len(result) == 1  # empty row preserved


class TestReadCsvRows:
    """Tests for read_csv_rows function."""

    def test_nonexistent_file(self):
        """Should return empty for nonexistent file."""
        header, rows = mhc.read_csv_rows("/nonexistent/file.csv")
        assert header == []
        assert rows == []

    def test_reads_csv(self):
        """Should read CSV file correctly."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, newline="") as f:
            f.write("module,skill,name\n")
            f.write("mkt,skill1,Skill 1\n")
            f.flush()

            header, rows = mhc.read_csv_rows(f.name)

        assert header == ["module", "skill", "name"]
        assert len(rows) == 1
        assert rows[0][0] == "mkt"


class TestWriteCsv:
    """Tests for write_csv function."""

    def test_creates_file(self):
        """Should create CSV file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "output.csv"
            mhc.write_csv(str(path), ["a", "b"], [["1", "2"]], verbose=False)

            assert path.exists()
            content = path.read_text()
            assert "a,b" in content
            assert "1,2" in content

    def test_creates_parent_dirs(self):
        """Should create parent directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "subdir" / "output.csv"
            mhc.write_csv(str(path), ["a"], [["1"]], verbose=False)

            assert path.exists()


class TestCleanupLegacyCsvs:
    """Tests for cleanup_legacy_csvs function."""

    def test_deletes_legacy_files(self):
        """Should delete legacy CSV files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create legacy files
            module_dir = Path(tmpdir) / "mkt"
            core_dir = Path(tmpdir) / "core"
            module_dir.mkdir()
            core_dir.mkdir()

            (module_dir / "module-help.csv").write_text("module,skill\n")
            (core_dir / "module-help.csv").write_text("module,skill\n")

            deleted = mhc.cleanup_legacy_csvs(tmpdir, "mkt", verbose=False)

            assert len(deleted) == 2
            assert not (module_dir / "module-help.csv").exists()
            assert not (core_dir / "module-help.csv").exists()


class TestParseArgs:
    """Tests for parse_args function."""

    def test_required_args(self):
        """Should require target and source."""
        sys.argv = [
            "merge-help-csv.py",
            "--target", "/path/to/target.csv",
            "--source", "/path/to/source.csv",
        ]
        args = mhc.parse_args()
        assert args.target == "/path/to/target.csv"
        assert args.source == "/path/to/source.csv"


def run_tests():
    """Run all tests and report results."""
    test_classes = [
        TestHeader,
        TestExtractModuleCodes,
        TestFilterRows,
        TestReadCsvRows,
        TestWriteCsv,
        TestCleanupLegacyCsvs,
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