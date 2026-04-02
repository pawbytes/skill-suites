#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Content Calendar Generator - Creates structured content calendar from strategy data.

Generates a markdown content calendar with posting schedule, themes, and
asset requirements from a campaign brief or strategy input.

Usage:
    python3 content-calendar-generator.py -i brief.json -o calendar.md
    python3 content-calendar-generator.py --weeks 4 --platforms "Instagram,TikTok,LinkedIn"
"""

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate content calendar from strategy data"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        help="Input JSON file with campaign/strategy data"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output markdown file (default: stdout)"
    )
    parser.add_argument(
        "--weeks",
        type=int,
        default=4,
        help="Number of weeks to generate (default: 4)"
    )
    parser.add_argument(
        "--start-date",
        help="Start date (YYYY-MM-DD, default: today)"
    )
    parser.add_argument(
        "--platforms",
        help="Comma-separated list of platforms"
    )
    parser.add_argument(
        "--pillars",
        help="Comma-separated list of content pillars"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output to stderr"
    )
    return parser.parse_args()


PLATFORM_SCHEDULES = {
    "Instagram": {"days": ["Tuesday", "Wednesday", "Friday"], "times": ["11:00", "14:00", "19:00"]},
    "TikTok": {"days": ["Tuesday", "Wednesday", "Thursday"], "times": ["07:00", "10:00", "19:00"]},
    "LinkedIn": {"days": ["Tuesday", "Wednesday", "Thursday"], "times": ["08:00", "12:00"]},
    "Twitter": {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": ["08:00", "12:00", "17:00"]},
    "YouTube": {"days": ["Thursday", "Friday", "Saturday"], "times": ["14:00", "17:00"]},
}

CONTENT_TYPES = {
    "Instagram": ["carousel", "reel", "static", "story"],
    "TikTok": ["video", "story"],
    "LinkedIn": ["text", "carousel", "video"],
    "Twitter": ["text", "thread", "image"],
    "YouTube": ["long-form", "shorts"],
}


def load_strategy(input_path: Path | None) -> dict:
    """Load strategy data from file or return defaults."""
    if input_path and input_path.exists():
        with open(input_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "name": "Content Campaign",
        "platforms": ["Instagram", "TikTok", "LinkedIn"],
        "pillars": ["Educational", "Behind-the-Scenes", "User Stories"],
        "frequency": {"Instagram": 3, "TikTok": 3, "LinkedIn": 2}
    }


def generate_week(
    start_date: datetime,
    week_num: int,
    platforms: list[str],
    pillars: list[str],
    frequency: dict
) -> list[dict]:
    """Generate a week's worth of content entries."""
    entries = []
    pillar_index = 0

    for day_offset in range(7):
        current_date = start_date + timedelta(days=day_offset)
        day_name = current_date.strftime("%A")

        for platform in platforms:
            schedule = PLATFORM_SCHEDULES.get(platform, {})
            if day_name not in schedule.get("days", []):
                continue

            pillar = pillars[pillar_index % len(pillars)]
            pillar_index += 1

            content_types = CONTENT_TYPES.get(platform, ["post"])
            content_type = content_types[pillar_index % len(content_types)]

            entries.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "day": day_name,
                "platform": platform,
                "type": content_type,
                "pillar": pillar,
                "topic": f"[{pillar} content topic]",
                "cta": "[Call to action]",
                "asset": f"{content_type} asset needed"
            })

    return entries


def format_calendar(
    entries: list[dict],
    campaign_name: str,
    platforms: list[str],
    pillars: list[str],
    weeks: int,
    start_date: datetime
) -> str:
    """Format calendar as markdown."""
    lines = [
        f"# Content Calendar: {campaign_name}",
        "",
        "## Overview",
        f"- **Duration:** {start_date.strftime('%Y-%m-%d')} to {(start_date + timedelta(weeks=weeks)).strftime('%Y-%m-%d')}",
        f"- **Platforms:** {', '.join(platforms)}",
        f"- **Content Pillars:** {', '.join(pillars)}",
        "",
        "## Content Pillars",
        ""
    ]

    for i, pillar in enumerate(pillars, 1):
        lines.append(f"{i}. **{pillar}**: [Description]")

    lines.extend(["", "## Weekly Schedule", ""])

    # Group entries by week
    current_week = 1
    week_start = start_date

    for i, entry in enumerate(entries):
        if i > 0 and i % 7 == 0:
            current_week += 1
            week_start = start_date + timedelta(weeks=current_week - 1)

        if i % 7 == 0:
            lines.append(f"### Week {current_week}: {pillars[(current_week - 1) % len(pillars)]}")
            lines.append("")
            lines.append("| Date | Day | Platform | Type | Pillar | Topic | CTA | Asset |")
            lines.append("|------|-----|----------|------|--------|-------|-----|-------|")

        lines.append(
            f"| {entry['date']} | {entry['day']} | {entry['platform']} | "
            f"{entry['type']} | {entry['pillar']} | {entry['topic']} | "
            f"{entry['cta']} | {entry['asset']} |"
        )

    # Asset summary
    lines.extend(["", "## Asset Requirements Summary", ""])
    lines.append("| Asset Type | Quantity | Suggested Due Date |")
    lines.append("|------------|----------|-------------------|")

    asset_counts = {}
    for entry in entries:
        asset_type = entry["type"]
        asset_counts[asset_type] = asset_counts.get(asset_type, 0) + 1

    for asset_type, count in sorted(asset_counts.items()):
        due_date = start_date + timedelta(days=3)
        lines.append(f"| {asset_type} | {count} | {due_date.strftime('%Y-%m-%d')} |")

    return "\n".join(lines)


def main():
    args = parse_args()

    try:
        if args.verbose:
            print(f"Generating {args.weeks} week calendar", file=sys.stderr)

        strategy = load_strategy(args.input)

        platforms = args.platforms.split(",") if args.platforms else strategy.get("platforms", ["Instagram"])
        pillars = args.pillars.split(",") if args.pillars else strategy.get("pillars", ["Content"])
        frequency = strategy.get("frequency", {})

        start_date = datetime.now()
        if args.start_date:
            start_date = datetime.strptime(args.start_date, "%Y-%m-%d")

        all_entries = []
        for week in range(args.weeks):
            week_start = start_date + timedelta(weeks=week)
            week_entries = generate_week(week_start, week + 1, platforms, pillars, frequency)
            all_entries.extend(week_entries)

        calendar = format_calendar(
            all_entries,
            strategy.get("name", "Content Campaign"),
            platforms,
            pillars,
            args.weeks,
            start_date
        )

        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(calendar)
            if args.verbose:
                print(f"Wrote calendar to {args.output}", file=sys.stderr)
        else:
            print(calendar)

        sys.exit(0)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input - {e}", file=sys.stderr)
        sys.exit(2)
    except ValueError as e:
        print(f"Error: Invalid value - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()