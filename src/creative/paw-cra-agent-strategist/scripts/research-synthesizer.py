#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Research Synthesizer - Consolidates search results into structured insights.

Takes JSON input from stdin containing search results and produces a structured
markdown summary with key insights, themes, and citations.

Usage:
    cat search_results.json | python3 research-synthesizer.py
    python3 research-synthesizer.py -i search_results.json -o report.md
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synthesize research results into structured markdown"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        help="Input JSON file (default: stdin)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output markdown file (default: stdout)"
    )
    parser.add_argument(
        "--title",
        default="Research Synthesis",
        help="Title for the report"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output to stderr"
    )
    return parser.parse_args()


def load_input(input_path: Path | None) -> list[dict]:
    """Load search results from file or stdin."""
    if input_path:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    # Handle various input formats
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "results" in data:
        return data["results"]
    return [data]


def extract_insights(results: list[dict]) -> dict:
    """Extract key insights from search results."""
    insights = {
        "total_sources": len(results),
        "themes": {},
        "key_findings": [],
        "sources": []
    }

    for result in results:
        # Extract source info
        source = {
            "title": result.get("title", "Untitled"),
            "url": result.get("url", ""),
            "snippet": result.get("snippet", result.get("content", ""))[:500]
        }
        insights["sources"].append(source)

        # Extract key content
        content = result.get("content", result.get("snippet", ""))
        if content:
            insights["key_findings"].append({
                "source": source["title"],
                "finding": content[:300] + "..." if len(content) > 300 else content
            })

    return insights


def format_markdown(insights: dict, title: str) -> str:
    """Format insights as markdown report."""
    lines = [
        f"# {title}",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Sources analyzed:** {insights['total_sources']}",
        "",
        "## Key Findings",
        ""
    ]

    for i, finding in enumerate(insights["key_findings"], 1):
        lines.append(f"### {i}. {finding['source']}")
        lines.append("")
        lines.append(finding['finding'])
        lines.append("")

    lines.extend([
        "## Sources",
        ""
    ])

    for source in insights["sources"]:
        lines.append(f"- [{source['title']}]({source['url']})")

    return "\n".join(lines)


def main():
    args = parse_args()

    try:
        if args.verbose:
            print(f"Loading input from {args.input or 'stdin'}", file=sys.stderr)

        results = load_input(args.input)
        insights = extract_insights(results)
        markdown = format_markdown(insights, args.title)

        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(markdown)
            if args.verbose:
                print(f"Wrote report to {args.output}", file=sys.stderr)
        else:
            print(markdown)

        sys.exit(0)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input - {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()