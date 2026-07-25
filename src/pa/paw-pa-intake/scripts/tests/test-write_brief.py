#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Unit tests for write_brief.py — stdlib unittest, no external deps."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

_spec = importlib.util.spec_from_file_location(
    "write_brief", Path(__file__).resolve().parent.parent / "write_brief.py"
)
wb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wb)


SAMPLE_BRIEF = {
    "clientName": "Acme Corp",
    "clientContext": "B2B manufacturer",
    "proposalType": "pitch",
    "proposalTypeConfidence": "high",
    "projectDescription": "Shopify Plus rebuild with ERP integration for mid-market B2B catalog and pricing rules.",
    "budget": "$50k-$80k",
    "timeline": "Q3 2026",
    "requirements": ["Theme rebuild", "ERP sync"],
    "constraints": ["Shopify Plus only"],
    "decisionMaker": "Jane Doe, VP Ops",
    "sourceInputRef": "audio:intake/call.m4a",
    "assumptions": [],
    "intakeMode": "headless",
    "inputType": "audio",
}


class TestIsEmpty(unittest.TestCase):
    def test_tbd_values(self):
        self.assertTrue(wb.is_empty("TBD"))
        self.assertTrue(wb.is_empty("not stated"))

    def test_real_value(self):
        self.assertFalse(wb.is_empty("$50k"))


class TestComputeCompleteness(unittest.TestCase):
    def test_complete_brief(self):
        result = wb.compute_completeness(SAMPLE_BRIEF)
        self.assertGreaterEqual(result["score"], 0.85)
        self.assertTrue(result["readyForPipeline"])
        self.assertTrue(result["readyForResearch"])
        self.assertEqual(result["blockers"], [])

    def test_missing_budget_flags_gap(self):
        data = {**SAMPLE_BRIEF, "budget": "TBD"}
        result = wb.compute_completeness(data)
        budget_gaps = [g for g in result["gaps"] if g["field"] == "budget"]
        self.assertEqual(len(budget_gaps), 1)
        self.assertEqual(budget_gaps[0]["severity"], "high")

    def test_autonomous_assumption_covers_budget(self):
        data = {
            **SAMPLE_BRIEF,
            "budget": "",
            "intakeMode": "autonomous",
            "assumptions": [{"field": "budget", "assumedValue": "$65k", "rationale": "mid-market rebuild"}],
        }
        result = wb.compute_completeness(data)
        self.assertTrue(result["readyForPipeline"])

    def test_critical_gap_no_client(self):
        data = {**SAMPLE_BRIEF, "clientName": ""}
        result = wb.compute_completeness(data)
        self.assertFalse(result["readyForPipeline"])
        self.assertIn("clientName", result["blockers"])
        self.assertFalse(result["readyForResearch"])


class TestRenderBriefMd(unittest.TestCase):
    def test_renders_frontmatter_arrays(self):
        completeness = wb.compute_completeness(SAMPLE_BRIEF)
        md = wb.render_brief_md(SAMPLE_BRIEF, completeness)
        self.assertIn("clientName: Acme Corp", md)
        self.assertIn("requirements:", md)
        self.assertIn("- Theme rebuild", md)
        self.assertIn("completenessReport:", md)
        self.assertIn("readyForPipeline:", md)
        self.assertIn("## Problem & context", md)


class TestMainIntegration(unittest.TestCase):
    def test_write_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            brief_json = Path(tmp) / "brief.json"
            brief_json.write_text(json.dumps(SAMPLE_BRIEF), encoding="utf-8")
            out_md = Path(tmp) / "brief.md"
            summary = Path(tmp) / ".intake-summary.json"

            with patch.object(
                __import__("sys"),
                "argv",
                [
                    "write_brief.py",
                    "--brief",
                    str(brief_json),
                    "--out",
                    str(out_md),
                    "--summary-out",
                    str(summary),
                ],
            ):
                with self.assertRaises(SystemExit) as ctx:
                    wb.main()
                self.assertEqual(ctx.exception.code, 0)

            self.assertTrue(out_md.exists())
            self.assertTrue(summary.exists())
            content = out_md.read_text(encoding="utf-8")
            self.assertIn("Acme Corp", content)
            summary_data = json.loads(summary.read_text(encoding="utf-8"))
            self.assertIn("completeness", summary_data)


if __name__ == "__main__":
    unittest.main()
