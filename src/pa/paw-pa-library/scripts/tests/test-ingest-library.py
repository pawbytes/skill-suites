#!/usr/bin/env python3
"""Unit tests for ingest-library.py"""
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

script_path = Path(__file__).parent.parent / "ingest-library.py"
spec = importlib.util.spec_from_file_location("ingest_library", script_path)
il = importlib.util.module_from_spec(spec)
sys.modules["ingest_library"] = il
spec.loader.exec_module(il)


class TestClassifyDocument:
    def test_case_study_by_filename(self):
        path = Path("acme-case-study.md")
        doc_type = il.classify_document(path, "Some content")
        assert doc_type == il.DOC_CASE_STUDY

    def test_pricing_by_filename(self):
        path = Path("client-proposal-2026.md")
        doc_type = il.classify_document(path, "Total: $1000")
        assert doc_type == il.DOC_PRICING

    def test_terms_by_filename(self):
        path = Path("standard-terms.md")
        doc_type = il.classify_document(path, "Liability clause")
        assert doc_type == il.DOC_BOILERPLATE_TERMS


class TestExtractFields:
    def test_extract_client(self):
        content = "Client: Acme Corp\nIndustry: Retail"
        assert il.extract_field([r"^client\s*:\s*(.+)$"], content) == "Acme Corp"

    def test_extract_deliverables(self):
        content = "## Deliverables\n- Item one\n- Item two\n## Other"
        items = il.extract_deliverables(content)
        assert items == ["Item one", "Item two"]

    def test_extract_line_items(self):
        content = "- Discovery — $5,000\n- Build — $20,000"
        items = il.extract_line_items(content)
        assert len(items) == 2
        assert items[0]["amount"] == 5000.0

    def test_extract_total(self):
        content = "Some text\nTotal: $25,000\n"
        assert il.extract_total(content) == 25000.0


class TestUpsert:
    def test_upsert_by_source_replaces(self):
        entries = [{"sourceDocPath": "a.md", "client": "Old"}]
        new = {"sourceDocPath": "a.md", "client": "New"}
        result = il.upsert_by_source(entries, new)
        assert len(result) == 1
        assert result[0]["client"] == "New"

    def test_upsert_case_study_by_id(self):
        entries = [{"id": "x", "client": "Old"}]
        new = {"id": "x", "client": "New"}
        result = il.upsert_case_study_by_id(entries, new)
        assert result[0]["client"] == "New"


class TestProcessInbox:
    def test_ingests_case_study(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            inbox = root / "library" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "retail-case-study.md").write_text(
                "Client: Retail Co\nIndustry: Retail\nOutcome: Won\n",
                encoding="utf-8",
            )
            summary = il.process_inbox(root, inbox, force=False, verbose=False)
            assert summary["processed"] == 1
            case_index = json.loads(
                (root / "library" / "case-studies-index.json").read_text()
            )
            assert len(case_index) == 1
            assert case_index[0]["client"] == "Retail Co"

    def test_skips_unchanged_on_second_run(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            inbox = root / "library" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "retail-case-study.md").write_text(
                "Client: Retail Co\n", encoding="utf-8"
            )
            il.process_inbox(root, inbox, force=False, verbose=False)
            summary = il.process_inbox(root, inbox, force=False, verbose=False)
            assert summary["skipped"] == 1
            assert summary["processed"] == 0

    def test_ingests_pricing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            inbox = root / "library" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "acme-quote.md").write_text(
                "Client: Acme\n- Discovery — $5,000\nTotal: $5,000\nWon: yes\n",
                encoding="utf-8",
            )
            summary = il.process_inbox(root, inbox, force=False, verbose=False)
            assert summary["processed"] == 1
            pricing = json.loads(
                (root / "library" / "pricing-history.json").read_text()
            )
            assert len(pricing) == 1
            assert pricing[0]["total"] == 5000.0
            assert pricing[0]["won"] is True


class TestValidate:
    def test_detects_orphan(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            library = root / "library"
            library.mkdir(parents=True)
            (library / "inbox").mkdir()
            (library / "case-studies-index.json").write_text(
                json.dumps(
                    [{"id": "x", "sourceDocPath": "missing.md", "client": "X"}]
                ),
                encoding="utf-8",
            )
            (library / "pricing-history.json").write_text("[]", encoding="utf-8")
            manifest = {"version": 1, "files": {}}
            report = il.validate_indexes(root, manifest, verbose=False)
            assert report["issueCount"] >= 1
            assert any(i["type"] == "orphaned_case_study" for i in report["issues"])


def run_tests():
    test_classes = [
        TestClassifyDocument,
        TestExtractFields,
        TestUpsert,
        TestProcessInbox,
        TestValidate,
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
