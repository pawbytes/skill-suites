#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Template Renderer for Aria Creative Suite

Renders structured files from templates, reducing LLM token usage for
repetitive formatting operations like brief files, brand profiles,
campaign status files, and daily log entries.
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional


def render_brief(
    name: str,
    deliverables: list[dict],
    objective: str,
    audience: str,
    brand: str,
    timeline: dict,
    constraints: Optional[dict] = None,
    references: Optional[list[str]] = None,
    notes: Optional[str] = None,
) -> str:
    """Render a brief file from structured data."""
    lines = [f"# {name}", "", "## Deliverables"]

    for d in deliverables:
        format_str = d.get("format", "")
        quantity = d.get("quantity", 1)
        specs = d.get("specs", "")
        lines.append(f"- {format_str}: {quantity} × {specs}")

    lines.extend([
        "",
        "## Objective",
        objective,
        "",
        "## Audience",
        audience,
        "",
        "## Brand",
        brand,
        "",
        "## Timeline",
    ])

    if timeline.get("received"):
        lines.append(f"- Brief received: {timeline['received']}")
    if timeline.get("draft"):
        lines.append(f"- Draft due: {timeline['draft']}")
    if timeline.get("final"):
        lines.append(f"- Final due: {timeline['final']}")

    if constraints:
        lines.extend(["", "## Constraints"])
        if constraints.get("must"):
            lines.append(f"- Must: {constraints['must']}")
        if constraints.get("must_not"):
            lines.append(f"- Must not: {constraints['must_not']}")

    if references:
        lines.extend(["", "## References"])
        for ref in references:
            lines.append(f"- {ref}")

    if notes:
        lines.extend(["", "## Notes", notes])

    return "\n".join(lines) + "\n"


def render_brand_profile(
    name: str,
    colors: Optional[list[dict]] = None,
    typography: Optional[dict] = None,
    logo: Optional[str] = None,
    voice_style: Optional[str] = None,
    voice_do: Optional[list[str]] = None,
    voice_dont: Optional[list[str]] = None,
    differentiator: Optional[str] = None,
    key_messages: Optional[list[str]] = None,
    target_audience: Optional[str] = None,
    assets_location: Optional[str] = None,
    assets_available: Optional[list[str]] = None,
) -> str:
    """Render a brand profile from structured data."""
    lines = [f"# {name}", "", "## Visual Identity"]

    if colors:
        color_strs = []
        for c in colors:
            if isinstance(c, dict):
                color_strs.append(f"{c.get('name', '')}: {c.get('hex', '')}")
            else:
                color_strs.append(str(c))
        lines.append(f"- Colors: {', '.join(color_strs)}")

    if typography:
        fonts = typography.get("fonts", [])
        if fonts:
            lines.append(f"- Typography: {', '.join(fonts)}")

    if logo:
        lines.append(f"- Logo: {logo}")

    lines.extend(["", "## Voice & Tone"])
    if voice_style:
        lines.append(f"- Style: {voice_style}")
    if voice_do:
        lines.append(f"- Do: {', '.join(voice_do)}")
    if voice_dont:
        lines.append(f"- Don't: {', '.join(voice_dont)}")

    lines.extend(["", "## Positioning"])
    if differentiator:
        lines.append(f"- Differentiator: {differentiator}")
    if key_messages:
        lines.append(f"- Key messages: {'; '.join(key_messages)}")
    if target_audience:
        lines.append(f"- Audience: {target_audience}")

    lines.extend(["", "## Assets"])
    if assets_location:
        lines.append(f"- Location: {assets_location}")
    if assets_available:
        lines.append(f"- Available: {', '.join(assets_available)}")

    return "\n".join(lines) + "\n"


def render_campaign_status(
    name: str,
    status: str = "in_progress",
    brief_path: Optional[str] = None,
    plan_path: Optional[str] = None,
    deliverables: Optional[list[dict]] = None,
    notes: Optional[str] = None,
) -> str:
    """Render a campaign status file."""
    lines = [
        f"# {name} - Campaign Status",
        "",
        f"**Status:** {status}",
        "",
    ]

    if brief_path:
        lines.append(f"- Brief: [{brief_path}]({brief_path})")
    if plan_path:
        lines.append(f"- Plan: [{plan_path}]({plan_path})")

    if deliverables:
        lines.extend(["", "## Deliverables", ""])
        for d in deliverables:
            name_d = d.get("name", "")
            status_d = d.get("status", "pending")
            assignee = d.get("assignee", "")
            lines.append(f"- [ ] {name_d} ({status_d}) - {assignee}")

    if notes:
        lines.extend(["", "## Notes", notes])

    return "\n".join(lines) + "\n"


def render_daily_log_entry(
    time: str,
    action: str,
    summary: str,
    decisions: Optional[list[str]] = None,
    next_steps: Optional[list[str]] = None,
) -> str:
    """Render a daily log entry."""
    lines = [
        f"## {time} — {action}",
        summary,
    ]

    if decisions:
        lines.append("")
        lines.append("**Decisions:**")
        for d in decisions:
            lines.append(f"- {d}")

    if next_steps:
        lines.append("")
        lines.append("**Next Steps:**")
        for s in next_steps:
            lines.append(f"- {s}")

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Render template files for Aria Creative Suite"
    )
    parser.add_argument(
        "template_type",
        choices=["brief", "brand", "campaign", "daily-entry"],
        help="Type of template to render"
    )
    parser.add_argument(
        "-n", "--name",
        required=True,
        help="Name for the file/entry"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "-d", "--data",
        help="JSON file with template data"
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to existing file instead of overwriting"
    )

    args = parser.parse_args()

    # Load data from file or stdin
    if args.data:
        data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    else:
        # Read from stdin if available, else use empty dict
        if not sys.stdin.isatty():
            data = json.load(sys.stdin)
        else:
            data = {}

    # Render based on template type
    if args.template_type == "brief":
        content = render_brief(
            name=args.name,
            deliverables=data.get("deliverables", []),
            objective=data.get("objective", ""),
            audience=data.get("audience", ""),
            brand=data.get("brand", ""),
            timeline=data.get("timeline", {}),
            constraints=data.get("constraints"),
            references=data.get("references"),
            notes=data.get("notes"),
        )
    elif args.template_type == "brand":
        content = render_brand_profile(
            name=args.name,
            colors=data.get("colors"),
            typography=data.get("typography"),
            logo=data.get("logo"),
            voice_style=data.get("voice_style"),
            voice_do=data.get("voice_do"),
            voice_dont=data.get("voice_dont"),
            differentiator=data.get("differentiator"),
            key_messages=data.get("key_messages"),
            target_audience=data.get("target_audience"),
            assets_location=data.get("assets_location"),
            assets_available=data.get("assets_available"),
        )
    elif args.template_type == "campaign":
        content = render_campaign_status(
            name=args.name,
            status=data.get("status", "in_progress"),
            brief_path=data.get("brief_path"),
            plan_path=data.get("plan_path"),
            deliverables=data.get("deliverables"),
            notes=data.get("notes"),
        )
    elif args.template_type == "daily-entry":
        content = render_daily_log_entry(
            time=data.get("time", datetime.now().strftime("%H:%M")),
            action=data.get("action", args.name),
            summary=data.get("summary", ""),
            decisions=data.get("decisions"),
            next_steps=data.get("next_steps"),
        )

    # Output
    if args.output:
        output_path = Path(args.output)
        if args.append and output_path.exists():
            existing = output_path.read_text(encoding="utf-8")
            # Find insertion point (before the last --- or at end)
            if existing.rstrip().endswith("---"):
                content = existing.rstrip()[:-3] + "\n" + content + "\n---\n"
            else:
                content = existing + "\n" + content
            output_path.write_text(content, encoding="utf-8")
        else:
            output_path.write_text(content, encoding="utf-8")

        result = {
            "status": "success",
            "template_type": args.template_type,
            "output_file": str(output_path),
            "lines": len(content.splitlines()),
        }
        print(json.dumps(result, indent=2))
    else:
        print(content)

    return 0


if __name__ == "__main__":
    sys.exit(main())