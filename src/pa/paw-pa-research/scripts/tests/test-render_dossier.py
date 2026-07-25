#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Unit tests for render_dossier.py — stdlib unittest, no external deps."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "render_dossier", Path(__file__).resolve().parent.parent / "render_dossier.py"
)
rd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rd)


class TestScorePct(unittest.TestCase):
    def test_fraction_to_percent(self):
        self.assertEqual(rd.score_pct(0.92), 92.0)

    def test_already_percent(self):
        self.assertEqual(rd.score_pct(85), 85.0)

    def test_invalid_is_zero(self):
        self.assertEqual(rd.score_pct(None), 0.0)
        self.assertEqual(rd.score_pct("x"), 0.0)


class TestScoreClass(unittest.TestCase):
    def test_thresholds(self):
        self.assertEqual(rd.score_class(80), "high")
        self.assertEqual(rd.score_class(75), "high")
        self.assertEqual(rd.score_class(60), "mid")
        self.assertEqual(rd.score_class(40), "low")


class TestEsc(unittest.TestCase):
    def test_escapes_html(self):
        self.assertEqual(rd.esc("<script>"), "&lt;script&gt;")


class TestRender(unittest.TestCase):
    def setUp(self):
        self.data = {
            "clientName": "Acme <Corp>",
            "proposalSlug": "acme-2026-07-03",
            "generated": "2026-07-03",
            "mode": "local-browser",
            "briefSummary": "Shopify rebuild for B2B.",
            "recommendation": "Lead with checkout case study.",
            "clientIntel": {
                "summary": "Mid-market manufacturer.",
                "signals": [{"label": "Industry", "detail": "Manufacturing", "source": "acme.com/about"}],
            },
            "techStack": {
                "summary": "Legacy stack migrating to modern web.",
                "technologies": [{"name": "Shopify Plus", "evidence": "Careers page", "source": "acme.com/jobs"}],
            },
            "localCaseStudyMatches": [
                {
                    "id": "cs-1",
                    "client": "Beta Inc",
                    "relevanceScore": 0.88,
                    "matchReasons": ["B2B e-commerce"],
                    "sourceDocPath": "library/inbox/beta-case.pdf",
                    "highlights": "40% conversion lift.",
                }
            ],
            "webEvidence": {
                "summary": "Industry moving to composable commerce.",
                "examples": [{"title": "Gartner report", "url": "https://example.com", "keyTakeaway": "Headless adoption up.", "relevance": "Supports approach"}],
            },
            "pricingBenchmarks": {
                "summary": "Shopify Plus projects cluster mid-five figures.",
                "observations": [{"workType": "Shopify rebuild", "range": "$40k-$80k", "source": "Clutch listings", "notes": "US agencies"}],
            },
            "competitiveContext": {
                "summary": "Client may compare to full-service agencies.",
                "alternatives": [{"name": "Big Agency", "differentiator": "Brand breadth vs specialist speed", "source": "RFP context"}],
            },
            "caveats": "Live scan of 6 sources; 3 local matches.",
        }

    def test_contains_sections(self):
        h = rd.render(self.data)
        self.assertIn("Research Dossier", h)
        self.assertIn("Acme &lt;Corp&gt;", h)
        self.assertIn("Top match", h)
        self.assertIn("88%", h)
        self.assertIn("browser-harness", h)
        self.assertIn("Gartner report", h)
        self.assertIn("$40k-$80k", h)

    def test_local_only_mode(self):
        self.data["mode"] = "local-only"
        h = rd.render(self.data)
        self.assertIn("Local library only", h)

    def test_empty_matches(self):
        self.data["localCaseStudyMatches"] = []
        h = rd.render(self.data)
        self.assertIn("No local case studies matched", h)

    def test_pipeline_writes_file(self):
        with tempfile.TemporaryDirectory() as d:
            fp = Path(d) / "findings.json"
            fp.write_text(json.dumps(self.data), encoding="utf-8")
            out = Path(d) / "research-dossier.html"
            import sys
            argv = sys.argv
            sys.argv = ["render_dossier.py", "--findings", str(fp), "--out", str(out), "--no-open"]
            try:
                code = rd.main()
            finally:
                sys.argv = argv
            self.assertEqual(code, 0)
            self.assertTrue(out.exists())
            self.assertIn("Beta Inc", out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
