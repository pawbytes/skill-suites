#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Unit tests for render_dashboard.py — stdlib unittest, no external deps."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "render_dashboard", Path(__file__).resolve().parent.parent / "render_dashboard.py"
)
rd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rd)


class TestBar(unittest.TestCase):
    def test_normal_scale(self):
        self.assertEqual(rd.bar(9), 90.0)
        self.assertEqual(rd.bar(0), 0.0)
        self.assertEqual(rd.bar(10), 100.0)

    def test_clamps_out_of_range(self):
        self.assertEqual(rd.bar(15), 100.0)
        self.assertEqual(rd.bar(-3), 0.0)

    def test_invert_low_value_is_wide(self):
        # competition 3 -> open lane 70%
        self.assertEqual(rd.bar(3, invert=True), 70.0)
        self.assertEqual(rd.bar(9, invert=True), 10.0)

    def test_non_numeric_is_zero(self):
        self.assertEqual(rd.bar(None), 0.0)
        self.assertEqual(rd.bar("x"), 0.0)


class TestScoreClass(unittest.TestCase):
    def test_thresholds(self):
        self.assertEqual(rd.score_class(90), "good")
        self.assertEqual(rd.score_class(66), "good")
        self.assertEqual(rd.score_class(50), "mid")
        self.assertEqual(rd.score_class(33), "mid")
        self.assertEqual(rd.score_class(10), "weak")


class TestEsc(unittest.TestCase):
    def test_escapes_html(self):
        self.assertEqual(rd.esc("<b>&"), "&lt;b&gt;&amp;")

    def test_none_is_empty(self):
        self.assertEqual(rd.esc(None), "")


class TestRender(unittest.TestCase):
    def setUp(self):
        self.data = {
            "freelancer": "Alex <Rivera>",
            "generated": "2026-06-23",
            "mode": "local-browser",
            "recommendation": "Go Shopify speed.",
            "niches": [
                {"name": "Shopify speed", "rank": 1, "fit": 9, "demand": 8,
                 "competition": 3, "rate_range": "$60-$95/hr",
                 "evidence": "40 jobs scanned.", "sample_jobs": ["Fix slow store"]},
                {"name": "General web dev", "rank": 2, "fit": 7, "demand": 9,
                 "competition": 9, "rate_range": "$25/hr", "evidence": "Crowded."},
            ],
            "rate_notes": "Cluster $50-90.",
            "caveats": "Read-only live scan.",
        }

    def test_contains_key_content(self):
        h = rd.render(self.data)
        self.assertIn("Shopify speed", h)
        self.assertIn("Recommended lane", h)  # rank 1 badge
        self.assertIn("$60-$95/hr", h)
        self.assertIn("Live market scan", h)  # mode label
        self.assertIn("Read-only live scan", h)
        self.assertIn("width:90%", h)  # fit 9
        self.assertIn("width:70%", h)  # competition 3 inverted

    def test_escapes_freelancer_name(self):
        h = rd.render(self.data)
        self.assertIn("Alex &lt;Rivera&gt;", h)
        self.assertNotIn("Alex <Rivera>", h)

    def test_manual_mode_label(self):
        self.data["mode"] = "manual"
        h = rd.render(self.data)
        self.assertIn("Pasted-listing analysis", h)

    def test_empty_niches(self):
        h = rd.render({"freelancer": "X", "niches": []})
        self.assertIn("No niches in findings.", h)

    def test_full_pipeline_writes_and_no_open(self):
        with tempfile.TemporaryDirectory() as d:
            fp = Path(d) / "findings.json"
            fp.write_text(json.dumps(self.data), encoding="utf-8")
            out = Path(d) / "sub" / "dash.html"
            import sys
            argv = sys.argv
            sys.argv = ["render_dashboard.py", "--findings", str(fp),
                        "--out", str(out), "--no-open"]
            try:
                code = rd.main()
            finally:
                sys.argv = argv
            self.assertEqual(code, 0)
            self.assertTrue(out.exists())
            self.assertIn("Shopify speed", out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
