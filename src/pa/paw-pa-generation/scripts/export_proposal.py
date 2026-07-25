#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Export a proposal markdown draft to branded HTML and optional PDF/DOCX via pandoc.

Plumbing only: the LLM assembles proposal content and brand-snapshot.json.
This script wraps the markdown in branded HTML and delegates binary formats to
pandoc when available. Degrades gracefully when pandoc is missing.

Brand JSON shape:
{
  "companyName": "Acme Consulting",
  "logoPath": "/path/to/logo.png",       # optional
  "colors": {
    "primary": "#1a365d",
    "secondary": "#2b6cb0",
    "accent": "#ed8936",
    "text": "#1a202c",
    "background": "#ffffff"
  },
  "fonts": {
    "heading": "Georgia, serif",
    "body": "system-ui, sans-serif"
  }
}

Usage:
  python export_proposal.py --input draft.md --brand-json brand.json \\
    --out-dir ./proposals/acme-2026-07-03 --formats html,md,pdf,docx

Outputs JSON to stdout:
  {"ok": true, "exports": {...}, "pandoc_available": true, "warnings": []}
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path


def esc(value) -> str:
    return html.escape(str(value if value is not None else ""))


def pandoc_available() -> bool:
    return shutil.which("pandoc") is not None


def load_brand(path: Path | None) -> dict:
    if path is None or not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def md_to_html_body(md: str) -> str:
    """Minimal markdown-to-HTML for headings, paragraphs, tables, lists, blockquotes."""
    # Intentionally simple — pandoc handles rich export; this covers HTML preview.
    lines = md.splitlines()
    out: list[str] = []
    in_table = False
    table_header_done = False
    in_ul = False
    in_ol = False
    in_blockquote = False
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Blockquote
        if stripped.startswith("> "):
            if not in_blockquote:
                out.append('<blockquote class="callout">')
                in_blockquote = True
            out.append(f"<p>{esc(stripped[2:])}</p>")
            i += 1
            if i >= len(lines) or not lines[i].strip().startswith("> "):
                out.append("</blockquote>")
                in_blockquote = False
            continue

        # Table
        if "|" in stripped and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= {"-", ":", " "} for c in cells):
                i += 1
                continue  # separator row
            if not in_table:
                out.append("<table><thead><tr>")
                in_table = True
                table_header_done = False
            if not table_header_done:
                for c in cells:
                    out.append(f"<th>{esc(c)}</th>")
                out.append("</tr></thead><tbody>")
                table_header_done = True
            else:
                out.append("<tr>")
                for c in cells:
                    out.append(f"<td>{esc(c)}</td>")
                out.append("</tr>")
            i += 1
            if i >= len(lines) or "|" not in lines[i]:
                out.append("</tbody></table>")
                in_table = False
            continue

        if in_table:
            out.append("</tbody></table>")
            in_table = False

        # Headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{esc(m.group(2))}</h{level}>")
            i += 1
            continue

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            out.append("<hr>")
            i += 1
            continue

        # Unordered list
        if re.match(r"^[-*+]\s+", stripped):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            if in_ol:
                out.append("</ol>")
                in_ol = False
            item = re.sub(r"^[-*+]\s+", "", stripped)
            out.append(f"<li>{esc(item)}</li>")
            i += 1
            if i >= len(lines) or not re.match(r"^[-*+]\s+", lines[i].strip()):
                out.append("</ul>")
                in_ul = False
            continue

        # Ordered list
        if re.match(r"^\d+\.\s+", stripped):
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            if in_ul:
                out.append("</ul>")
                in_ul = False
            item = re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"<li>{esc(item)}</li>")
            i += 1
            if i >= len(lines) or not re.match(r"^\d+\.\s+", lines[i].strip()):
                out.append("</ol>")
                in_ol = False
            continue

        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

        # Images
        img = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
        if img:
            alt, src = img.group(1), img.group(2)
            out.append(f'<img src="{esc(src)}" alt="{esc(alt)}" class="proposal-img">')
            i += 1
            continue

        # Empty line
        if not stripped:
            i += 1
            continue

        # Paragraph
        out.append(f"<p>{esc(stripped)}</p>")
        i += 1

    if in_table:
        out.append("</tbody></table>")
    if in_ul:
        out.append("</ul>")
    if in_ol:
        out.append("</ol>")
    if in_blockquote:
        out.append("</blockquote>")

    return "\n".join(out)


def build_css(brand: dict) -> str:
    colors = brand.get("colors") or {}
    fonts = brand.get("fonts") or {}
    primary = colors.get("primary", "#1a365d")
    secondary = colors.get("secondary", "#2b6cb0")
    accent = colors.get("accent", "#ed8936")
    text = colors.get("text", "#1a202c")
    background = colors.get("background", "#ffffff")
    heading_font = fonts.get("heading", "Georgia, serif")
    body_font = fonts.get("body", "system-ui, -apple-system, sans-serif")

    return f"""
:root {{
  --primary: {primary};
  --secondary: {secondary};
  --accent: {accent};
  --text: {text};
  --background: {background};
}}
* {{ box-sizing: border-box; }}
body {{
  font-family: {body_font};
  color: var(--text);
  background: var(--background);
  margin: 0;
  line-height: 1.6;
}}
.header {{
  background: var(--primary);
  color: #fff;
  padding: 1.5rem 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}}
.header img {{ max-height: 48px; }}
.header h1 {{
  font-family: {heading_font};
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}}
.content {{
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1.5rem 4rem;
}}
h1, h2, h3, h4 {{ font-family: {heading_font}; color: var(--primary); }}
h1 {{ font-size: 1.75rem; border-bottom: 2px solid var(--accent); padding-bottom: 0.5rem; }}
h2 {{ font-size: 1.35rem; margin-top: 2rem; }}
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.95rem;
}}
th, td {{
  border: 1px solid #e2e8f0;
  padding: 0.5rem 0.75rem;
  text-align: left;
}}
th {{ background: color-mix(in srgb, var(--secondary) 15%, white); }}
tr:nth-child(even) td {{ background: #f7fafc; }}
blockquote.callout {{
  border-left: 4px solid var(--accent);
  background: color-mix(in srgb, var(--accent) 8%, white);
  margin: 1rem 0;
  padding: 0.75rem 1rem;
}}
blockquote.callout p {{ margin: 0.25rem 0; }}
.proposal-img {{ max-width: 100%; height: auto; margin: 1rem 0; border-radius: 4px; }}
hr {{ border: none; border-top: 1px solid #e2e8f0; margin: 2rem 0; }}
@media print {{
  .header {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .content {{ max-width: 100%; }}
  h2 {{ page-break-before: auto; }}
}}
"""


def render_html(md: str, brand: dict, title: str = "Proposal") -> str:
    company = esc(brand.get("companyName", ""))
    logo_path = brand.get("logoPath", "")
    logo_html = ""
    if logo_path and Path(logo_path).is_file():
        logo_html = f'<img src="{esc(logo_path)}" alt="{company} logo">'
    elif logo_path:
        logo_html = f'<img src="{esc(logo_path)}" alt="{company} logo">'

    header_title = company or title
    body = md_to_html_body(md)
    css = build_css(brand)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>{css}</style>
</head>
<body>
<header class="header">
  {logo_html}
  <h1>{header_title}</h1>
</header>
<main class="content">
{body}
</main>
</body>
</html>"""


def run_pandoc(input_path: Path, output_path: Path, to_format: str) -> tuple[bool, str]:
    cmd = ["pandoc", str(input_path), "-o", str(output_path)]
    if to_format == "pdf":
        cmd.extend(["--pdf-engine=pdflatex"])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            return False, (result.stderr or result.stdout or "pandoc failed").strip()
        return True, ""
    except FileNotFoundError:
        return False, "pandoc not found"
    except subprocess.TimeoutExpired:
        return False, "pandoc timed out"
    except OSError as e:
        return False, str(e)


def export_proposal(
    input_path: Path,
    brand_json: Path | None,
    out_dir: Path,
    formats: list[str],
    basename: str = "final-proposal",
) -> dict:
    warnings: list[str] = []
    exports: dict[str, str | None] = {"html": None, "md": None, "pdf": None, "docx": None}

    if not input_path.is_file():
        return {"ok": False, "error": f"input not found: {input_path}", "exports": exports, "warnings": warnings}

    out_dir.mkdir(parents=True, exist_ok=True)
    md_text = input_path.read_text(encoding="utf-8")
    brand = load_brand(brand_json)

    title_match = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else "Proposal"

    if "html" in formats:
        html_path = out_dir / f"{basename}.html"
        html_path.write_text(render_html(md_text, brand, title), encoding="utf-8")
        exports["html"] = str(html_path.resolve())

    if "md" in formats:
        md_path = out_dir / f"{basename}.md"
        header = f"<!-- exported by paw-pa-generation | {title} -->\n\n"
        md_path.write_text(header + md_text, encoding="utf-8")
        exports["md"] = str(md_path.resolve())

    has_pandoc = pandoc_available()
    for fmt in ("pdf", "docx"):
        if fmt not in formats:
            continue
        if not has_pandoc:
            warnings.append(f"{fmt}: pandoc not found on PATH — skipped")
            exports[fmt] = None
            continue
        out_path = out_dir / f"{basename}.{fmt}"
        # Use the markdown source for pandoc
        src = out_dir / f"{basename}.md" if exports.get("md") else input_path
        if not src.is_file():
            src = input_path
        ok, err = run_pandoc(src, out_path, fmt)
        if ok:
            exports[fmt] = str(out_path.resolve())
        else:
            warnings.append(f"{fmt}: {err}")
            exports[fmt] = None

    return {
        "ok": True,
        "exports": exports,
        "pandoc_available": has_pandoc,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Export proposal markdown to branded formats")
    parser.add_argument("--input", required=True, help="Path to draft markdown")
    parser.add_argument("--brand-json", default=None, help="Brand snapshot JSON")
    parser.add_argument("--out-dir", required=True, help="Output directory")
    parser.add_argument(
        "--formats",
        default="html,md,pdf,docx",
        help="Comma-separated: html, md, pdf, docx",
    )
    parser.add_argument("--basename", default="final-proposal", help="Output file basename")
    parser.add_argument("--no-open", action="store_true", help="Do not open HTML in browser")
    args = parser.parse_args()

    formats = [f.strip().lower() for f in args.formats.split(",") if f.strip()]
    brand_path = Path(args.brand_json) if args.brand_json else None

    result = export_proposal(
        input_path=Path(args.input),
        brand_json=brand_path,
        out_dir=Path(args.out_dir),
        formats=formats,
        basename=args.basename,
    )

    print(json.dumps(result, indent=2))

    if result.get("ok") and not args.no_open and result.get("exports", {}).get("html"):
        try:
            webbrowser.open(Path(result["exports"]["html"]).as_uri())
            result["opened"] = True
        except OSError:
            pass

    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
