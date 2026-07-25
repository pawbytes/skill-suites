#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Unit tests for export_proposal.py — stdlib unittest, no external deps."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "export_proposal",
    Path(__file__).resolve().parent.parent / "export_proposal.py",
)
ep = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ep)


class TestEsc(unittest.TestCase):
    def test_escapes_html(self):
        self.assertEqual(ep.esc("<b>&"), "&lt;b&gt;&amp;")

    def test_none_is_empty(self):
        self.assertEqual(ep.esc(None), "")


class TestMdToHtmlBody(unittest.TestCase):
    def test_heading(self):
        h = ep.md_to_html_body("# Title\n\nParagraph.")
        self.assertIn("<h1>Title</h1>", h)
        self.assertIn("<p>Paragraph.</p>", h)

    def test_table(self):
        md = "| A | B |\n|---|---|\n| 1 | 2 |"
        h = ep.md_to_html_body(md)
        self.assertIn("<table>", h)
        self.assertIn("<th>A</th>", h)
        self.assertIn("<td>1</td>", h)

    def test_blockquote(self):
        h = ep.md_to_html_body("> Assumption one")
        self.assertIn('blockquote class="callout"', h)
        self.assertIn("Assumption one", h)

    def test_list(self):
        h = ep.md_to_html_body("- item one\n- item two")
        self.assertIn("<ul>", h)
        self.assertIn("<li>item one</li>", h)


class TestBuildCss(unittest.TestCase):
    def test_uses_brand_colors(self):
        brand = {"colors": {"primary": "#ff0000", "secondary": "#00ff00"}}
        css = ep.build_css(brand)
        self.assertIn("#ff0000", css)
        self.assertIn("#00ff00", css)


class TestRenderHtml(unittest.TestCase):
    def test_full_document(self):
        brand = {"companyName": "Test Co", "colors": {}, "fonts": {}}
        doc = ep.render_html("# Hello\n\nWorld.", brand, "Hello")
        self.assertIn("<!DOCTYPE html>", doc)
        self.assertIn("Test Co", doc)
        self.assertIn("<h1>Hello</h1>", doc)

    def test_escapes_company_name(self):
        brand = {"companyName": "<Evil>", "colors": {}, "fonts": {}}
        doc = ep.render_html("text", brand)
        self.assertIn("&lt;Evil&gt;", doc)
        self.assertNotIn("<Evil>", doc)


class TestExportProposal(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.draft = self.root / "draft-v1.md"
        self.draft.write_text("# Proposal Title\n\n## Section\n\nContent here.\n", encoding="utf-8")
        self.brand = self.root / "brand.json"
        self.brand.write_text(
            json.dumps({
                "companyName": "Acme",
                "colors": {"primary": "#111", "secondary": "#222", "accent": "#333",
                           "text": "#000", "background": "#fff"},
                "fonts": {"heading": "serif", "body": "sans-serif"},
            }),
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_exports_html_and_md(self):
        out = self.root / "out"
        result = ep.export_proposal(
            self.draft, self.brand, out, formats=["html", "md"]
        )
        self.assertTrue(result["ok"])
        self.assertIsNotNone(result["exports"]["html"])
        self.assertIsNotNone(result["exports"]["md"])
        self.assertTrue(Path(result["exports"]["html"]).is_file())
        html_content = Path(result["exports"]["html"]).read_text(encoding="utf-8")
        self.assertIn("Acme", html_content)
        self.assertIn("Proposal Title", html_content)

    def test_missing_input(self):
        result = ep.export_proposal(
            self.root / "nope.md", self.brand, self.root / "out", formats=["html"]
        )
        self.assertFalse(result["ok"])

    def test_pdf_skipped_without_pandoc(self):
        # pandoc may or may not be installed; if missing, should warn not crash
        out = self.root / "out"
        result = ep.export_proposal(
            self.draft, self.brand, out, formats=["html", "pdf"]
        )
        self.assertTrue(result["ok"])
        if not result["pandoc_available"]:
            self.assertIsNone(result["exports"]["pdf"])
            self.assertTrue(any("pandoc" in w for w in result["warnings"]))


class TestPandocAvailable(unittest.TestCase):
    def test_returns_bool(self):
        self.assertIsInstance(ep.pandoc_available(), bool)


if __name__ == "__main__":
    unittest.main()
