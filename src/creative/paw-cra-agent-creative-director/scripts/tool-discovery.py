#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Tool Discovery Script for Aria Creative Suite
Checks availability of CLI tools, MCP servers, and API keys.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone


def check_cli_tool(name: str) -> dict:
    """Check if a CLI tool is available on PATH."""
    path = shutil.which(name)
    if path:
        return {"name": name, "status": "available", "path": path}
    return {"name": name, "status": "unavailable", "path": None}


def check_cli_tool_version(name: str, version_flag: str = "--version") -> dict:
    """Check CLI tool and extract version if available."""
    result = check_cli_tool(name)
    if result["status"] == "available":
        try:
            proc = subprocess.run(
                [name, version_flag],
                capture_output=True,
                text=True,
                timeout=5
            )
            if proc.returncode == 0:
                # Parse version from output
                output = proc.stdout.strip() or proc.stderr.strip()
                first_line = output.split("\n")[0]
                # Try to extract version number
                import re
                match = re.search(r'(\d+\.\d+\.\d+|\d+\.\d+)', first_line)
                if match:
                    result["version"] = match.group(1)
                else:
                    result["version"] = "installed"
        except Exception:
            result["version"] = "installed"
    return result


def check_ffmpeg() -> dict:
    """Check ffmpeg and get version if available."""
    result = check_cli_tool("ffmpeg")
    if result["status"] == "available":
        try:
            proc = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if proc.returncode == 0:
                first_line = proc.stdout.split("\n")[0]
                result["version"] = first_line.split()[2] if len(first_line.split()) > 2 else "unknown"
        except Exception:
            result["version"] = "unknown"
    return result


def check_agent_browser() -> dict:
    """Check agent-browser CLI and get version if available."""
    result = check_cli_tool("agent-browser")
    if result["status"] == "available":
        result["purpose"] = "Browser automation for AI agents"
        result["install_command"] = "npm install -g agent-browser"
        try:
            # Check if Chrome is installed for agent-browser
            proc = subprocess.run(
                ["agent-browser", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if proc.returncode == 0:
                output = proc.stdout.strip() or proc.stderr.strip()
                import re
                match = re.search(r'(\d+\.\d+\.\d+|\d+\.\d+)', output)
                if match:
                    result["version"] = match.group(1)
                else:
                    result["version"] = "installed"
        except Exception:
            result["version"] = "installed"
    else:
        result["purpose"] = "Browser automation for AI agents"
        result["install_command"] = "npm install -g agent-browser"
    return result


def load_config() -> dict:
    """Load configuration from config files."""
    config = {}
    config_paths = [
        Path(".pawbytes/config/config.yaml"),
        Path(".pawbytes/config/config.user.yaml"),
    ]

    # Also check project root
    cwd = Path.cwd()
    config_paths = [
        cwd / ".pawbytes/config/config.yaml",
        cwd / ".pawbytes/config/config.user.yaml",
    ]

    for config_path in config_paths:
        if config_path.exists():
            try:
                import re
                content = config_path.read_text(encoding="utf-8")
                # Simple YAML key extraction for flat config
                for line in content.split("\n"):
                    match = re.match(r'^(\w+):\s*"?([^"\n]+)"?', line.strip())
                    if match:
                        key, value = match.groups()
                        config[key] = value.strip('"')
            except Exception:
                pass

    return config


def check_api_keys(config: dict) -> list:
    """Check for API key availability."""
    keys = [
        ("fal_key", "fal.ai"),
        ("elevenlabs_api_key", "ElevenLabs"),
        ("pexels_api_key", "Pexels"),
    ]

    results = []
    for key_name, display_name in keys:
        value = config.get(key_name, "")
        # Check if key exists and is not empty/placeholder
        if value and not value.startswith("your_") and len(value) > 10:
            results.append({
                "name": display_name,
                "key": key_name,
                "status": "available"
            })
        else:
            results.append({
                "name": display_name,
                "key": key_name,
                "status": "unavailable"
            })

    return results


def check_mcp_servers() -> list:
    """Check MCP server availability based on known server names."""
    # MCP servers are typically discovered through the client
    # We report them as "unknown" and let the LLM verify
    servers = [
        ("fal", "fal.ai MCP server"),
        ("exa", "Exa web search"),
        ("pencil", "Pencil design editor"),
        ("context7", "Context7 documentation"),
    ]

    results = []
    for server_id, display_name in servers:
        results.append({
            "name": display_name,
            "server_id": server_id,
            "status": "unknown",  # Requires LLM to verify
            "note": "Verify via MCP tool availability"
        })

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Discover available creative tools for Aria Creative Suite"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Include additional details"
    )

    args = parser.parse_args()

    # Run checks
    cli_tools = [
        check_ffmpeg(),
        check_agent_browser(),
        check_cli_tool("loopwind"),
        check_cli_tool("egaki"),
    ]

    config = load_config()
    api_keys = check_api_keys(config)
    mcp_servers = check_mcp_servers()

    # Build result
    result = {
        "script": "tool-discovery",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cli_tools": cli_tools,
        "api_keys": api_keys,
        "mcp_servers": mcp_servers,
        "summary": {
            "cli_available": sum(1 for t in cli_tools if t["status"] == "available"),
            "cli_total": len(cli_tools),
            "api_available": sum(1 for k in api_keys if k["status"] == "available"),
            "api_total": len(api_keys),
        }
    }

    if args.verbose:
        result["config_loaded"] = {k: "***" if "key" in k.lower() or "api" in k.lower() else v
                                   for k, v in config.items()}

    # Output
    output = json.dumps(result, indent=2)
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())