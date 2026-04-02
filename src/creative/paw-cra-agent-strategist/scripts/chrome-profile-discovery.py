#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Chrome Profile Discovery - Finds Chrome profiles available for agent-browser.

Agent-browser uses Chrome user profiles to maintain authenticated sessions.
This script discovers existing Chrome profiles and helps identify which one
to use for research.

Usage:
    python3 chrome-profile-discovery.py
    python3 chrome-profile-discovery.py --list
    python3 chrome-profile-discovery.py --create strategist
"""

import argparse
import json
import os
import platform
import sys
from pathlib import Path


def get_chrome_user_data_dir() -> Path:
    """Get the Chrome user data directory for the current platform."""
    system = platform.system()
    home = Path.home()

    if system == "Windows":
        return Path(os.environ.get("LOCALAPPDATA", home / "AppData" / "Local")) / "Google" / "Chrome" / "User Data"
    elif system == "Darwin":  # macOS
        return home / "Library" / "Application Support" / "Google" / "Chrome"
    else:  # Linux
        return home / ".config" / "google-chrome"


def get_edge_user_data_dir() -> Path:
    """Get the Edge user data directory for the current platform."""
    system = platform.system()
    home = Path.home()

    if system == "Windows":
        return Path(os.environ.get("LOCALAPPDATA", home / "AppData" / "Local")) / "Microsoft" / "Edge" / "User Data"
    elif system == "Darwin":
        return home / "Library" / "Application Support" / "Microsoft Edge"
    else:
        return home / ".config" / "microsoft-edge"


def discover_profiles(browser_dir: Path) -> list[dict]:
    """Discover browser profiles from a user data directory."""
    profiles = []

    if not browser_dir.exists():
        return profiles

    # Check Local State for profile info
    local_state_path = browser_dir / "Local State"
    profile_info = {}

    if local_state_path.exists():
        try:
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
                profile_info = local_state.get("profile", {}).get("info_cache", {})
        except (json.JSONDecodeError, KeyError):
            pass

    # Find profile directories
    for item in browser_dir.iterdir():
        if item.is_dir() and (item.name.startswith("Profile") or item.name == "Default"):
            name = profile_info.get(item.name, {}).get("name", item.name)
            profiles.append({
                "folder": item.name,
                "name": name,
                "path": str(item),
                "has_cookies": (item / "Cookies").exists(),
                "has_login_data": (item / "Login Data").exists(),
            })

    return profiles


def format_output(profiles: list[dict], browser_name: str) -> str:
    """Format profiles as markdown table."""
    if not profiles:
        return f"No {browser_name} profiles found."

    lines = [
        f"## {browser_name} Profiles",
        "",
        "| Profile Name | Folder | Auth Data | Path |",
        "|--------------|--------|-----------|------|",
    ]

    for p in profiles:
        auth_status = "✓" if p["has_cookies"] or p["has_login_data"] else "—"
        lines.append(f"| {p['name']} | {p['folder']} | {auth_status} | `{p['path']}` |")

    return "\n".join(lines)


def suggest_agent_browser_usage(profiles: list[dict], browser_name: str) -> str:
    """Suggest how to use discovered profiles with agent-browser."""
    if not profiles:
        return ""

    lines = [
        "",
        f"### Using with agent-browser",
        "",
        "```bash",
        f"# Use a specific {browser_name} profile",
    ]

    # Suggest the first profile with auth data, or Default
    suggested = None
    for p in profiles:
        if p["has_cookies"] or p["has_login_data"]:
            suggested = p
            break

    if not suggested:
        suggested = profiles[0]

    # On Windows, we need to use the profile directory path
    if platform.system() == "Windows":
        lines.append(f'agent-browser --profile "{suggested["path"]}" open https://linkedin.com')
    else:
        lines.append(f'agent-browser --profile "{suggested["path"]}" open https://linkedin.com')

    lines.extend([
        "",
        "# Or create a dedicated strategist profile",
        'agent-browser --profile "~/.strategist-profile" open https://linkedin.com/login',
        "# After logging in, the profile stays authenticated",
        "```",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Discover Chrome/Edge profiles for agent-browser"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all discovered profiles"
    )
    parser.add_argument(
        "--browser", "-b",
        choices=["chrome", "edge", "all"],
        default="all",
        help="Which browser to scan (default: all)"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON"
    )
    parser.add_argument(
        "--create",
        metavar="NAME",
        help="Suggest command to create a new profile"
    )
    args = parser.parse_args()

    all_profiles = {}

    if args.browser in ("chrome", "all"):
        chrome_dir = get_chrome_user_data_dir()
        all_profiles["chrome"] = discover_profiles(chrome_dir)

    if args.browser in ("edge", "all"):
        edge_dir = get_edge_user_data_dir()
        all_profiles["edge"] = discover_profiles(edge_dir)

    if args.json:
        print(json.dumps(all_profiles, indent=2))
        return 0

    # Markdown output
    print("# Browser Profile Discovery")
    print("")
    print(f"Platform: {platform.system()}")
    print("")

    for browser, profiles in all_profiles.items():
        print(format_output(profiles, browser.title()))
        print(suggest_agent_browser_usage(profiles, browser.title()))
        print("")

    if args.create:
        profile_name = args.create
        print("## Creating a New Profile")
        print("")
        print("```bash")
        print(f'# Create a dedicated profile for {profile_name}')
        print(f'agent-browser --profile "~/.{profile_name}-profile" open https://linkedin.com/login')
        print("# Log in with your credentials")
        print("# The profile will stay authenticated for future sessions")
        print("```")
        print("")
        print("**Note:** On Windows, you may need to use a full path like:")
        print(f'agent-browser --profile "%USERPROFILE%\\.{profile_name}-profile" open https://linkedin.com/login')

    return 0


if __name__ == "__main__":
    sys.exit(main())