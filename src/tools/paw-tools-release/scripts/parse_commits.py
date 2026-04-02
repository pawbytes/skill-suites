#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Parse conventional commits and group them for changelog generation.

Analyzes git commit messages following the Conventional Commits specification
and outputs grouped results suitable for changelog generation.
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class CommitType(Enum):
    BREAKING = "breaking"
    FEAT = "feat"
    FIX = "fix"
    DOCS = "docs"
    STYLE = "style"
    REFACTOR = "refactor"
    PERF = "perf"
    TEST = "test"
    BUILD = "build"
    CI = "ci"
    CHORE = "chore"
    REVERT = "revert"
    OTHER = "other"


@dataclass
class Commit:
    hash: str
    type: CommitType
    scope: Optional[str]
    breaking: bool
    description: str
    original: str
    pr_number: Optional[str] = None


# Mapping from conventional commit prefixes to categories
CATEGORY_MAPPING = {
    CommitType.BREAKING: "Breaking Changes",
    CommitType.FEAT: "Features",
    CommitType.FIX: "Bug Fixes",
    CommitType.DOCS: "Documentation",
    CommitType.PERF: "Performance",
    CommitType.REFACTOR: "Refactoring",
    CommitType.TEST: "Tests",
    CommitType.BUILD: "Build",
    CommitType.CI: "CI",
    CommitType.CHORE: "Chores",
    CommitType.REVERT: "Reverts",
    CommitType.STYLE: "Style",
    CommitType.OTHER: "Other Changes",
}

# Order for changelog output
CATEGORY_ORDER = [
    CommitType.BREAKING,
    CommitType.FEAT,
    CommitType.FIX,
    CommitType.PERF,
    CommitType.REFACTOR,
    CommitType.DOCS,
    CommitType.TEST,
    CommitType.BUILD,
    CommitType.CI,
    CommitType.CHORE,
    CommitType.REVERT,
    CommitType.STYLE,
    CommitType.OTHER,
]


def parse_commit_message(message: str) -> Commit:
    """Parse a single commit message into structured data."""
    # Conventional commit pattern: type(scope)!: description
    # Examples:
    #   feat: add new feature
    #   feat(api): add new endpoint
    #   feat!: breaking change
    #   feat(api)!: breaking change with scope
    #   breaking: remove deprecated API

    pattern = r'^(?P<type>\w+)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<description>.+)$'
    match = re.match(pattern, message.strip())

    if match:
        type_str = match.group("type").lower()
        scope = match.group("scope")
        breaking = match.group("breaking") == "!"
        description = match.group("description").strip()

        # Handle explicit 'breaking' type or breaking marker
        if type_str == "breaking":
            commit_type = CommitType.BREAKING
            breaking = True
        elif breaking:
            commit_type = CommitType.BREAKING
        else:
            try:
                commit_type = CommitType(type_str)
            except ValueError:
                commit_type = CommitType.OTHER
    else:
        # Non-conventional commit
        commit_type = CommitType.OTHER
        scope = None
        breaking = False
        description = message.strip()

    # Extract PR number from description
    pr_match = re.search(r'\(#(\d+)\)$', description)
    pr_number = pr_match.group(1) if pr_match else None

    return Commit(
        hash="",
        type=commit_type,
        scope=scope,
        breaking=breaking,
        description=description,
        original=message,
        pr_number=pr_number,
    )


def get_commits_from_git(commit_range: Optional[str] = None) -> list[tuple[str, str]]:
    """Get commits from git log."""
    cmd = ["git", "log", "--pretty=format:%h %s", "--no-merges"]
    if commit_range:
        cmd.insert(3, commit_range)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running git: {e}", file=sys.stderr)
        sys.exit(2)

    commits = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        parts = line.split(" ", 1)
        if len(parts) == 2:
            commits.append((parts[0], parts[1]))

    return commits


def parse_commits(commits: list[tuple[str, str]]) -> list[Commit]:
    """Parse list of (hash, message) tuples into Commit objects."""
    parsed = []
    for commit_hash, message in commits:
        commit = parse_commit_message(message)
        commit.hash = commit_hash
        parsed.append(commit)
    return parsed


def group_commits(commits: list[Commit]) -> dict[CommitType, list[Commit]]:
    """Group commits by type."""
    grouped = defaultdict(list)
    for commit in commits:
        grouped[commit.type].append(commit)
    return dict(grouped)


def determine_version_bump(commits: list[Commit]) -> str:
    """Determine version bump level based on commits."""
    has_breaking = any(c.breaking or c.type == CommitType.BREAKING for c in commits)
    has_feat = any(c.type == CommitType.FEAT for c in commits)

    if has_breaking:
        return "major"
    elif has_feat:
        return "minor"
    else:
        return "patch"


def format_changelog(grouped: dict[CommitType, list[Commit]], verbose: bool = False) -> str:
    """Format commits as changelog markdown."""
    lines = []

    for commit_type in CATEGORY_ORDER:
        commits = grouped.get(commit_type)
        if not commits:
            continue

        category = CATEGORY_MAPPING[commit_type]
        lines.append(f"### {category}")

        for commit in commits:
            if commit.scope:
                line = f"- **{commit.scope}:** {commit.description}"
            else:
                line = f"- {commit.description}"

            if commit.pr_number:
                line += f" (#{commit.pr_number})"
            elif verbose:
                line += f" ({commit.hash})"

            lines.append(line)

        lines.append("")  # Empty line between sections

    return "\n".join(lines).strip()


def main():
    parser = argparse.ArgumentParser(
        description="Parse conventional commits for changelog generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s HEAD~10
  %(prog)s v1.0.0..HEAD
  %(prog)s --format changelog v1.0.0..HEAD
        """,
    )
    parser.add_argument(
        "commit_range",
        nargs="?",
        help="Git commit range (e.g., v1.0.0..HEAD, HEAD~10)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "changelog", "bump"],
        default="json",
        help="Output format: json (default), changelog (markdown), bump (version level)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Include commit hashes in output",
    )

    args = parser.parse_args()

    raw_commits = get_commits_from_git(args.commit_range)
    commits = parse_commits(raw_commits)

    if not commits:
        print("No commits found", file=sys.stderr)
        sys.exit(0)

    if args.format == "bump":
        print(determine_version_bump(commits))
    elif args.format == "changelog":
        grouped = group_commits(commits)
        print(format_changelog(grouped, args.verbose))
    else:  # json
        grouped = group_commits(commits)
        output = {
            "script": "parse_commits",
            "version": "1.0.0",
            "commit_count": len(commits),
            "version_bump": determine_version_bump(commits),
            "groups": {
                CATEGORY_MAPPING[ct]: [
                    {
                        "hash": c.hash,
                        "scope": c.scope,
                        "description": c.description,
                        "breaking": c.breaking,
                        "pr_number": c.pr_number,
                    }
                    for c in commits_list
                ]
                for ct, commits_list in grouped.items()
            },
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()