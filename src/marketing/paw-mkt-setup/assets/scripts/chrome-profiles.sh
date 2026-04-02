#!/bin/bash
# =============================================================================
# Chrome Profile Discovery Script for Agent-Browser
# =============================================================================
# Lists available Chrome profiles that can be used with agent-browser for
# authenticated sessions (gated content like LinkedIn, Twitter/X, Facebook, etc.)
#
# Usage:
#   ./chrome-profiles.sh [--json] [--paths]
#
# Options:
#   --json    Output results in JSON format
#   --paths   Show full profile paths suitable for --profile flag
#
# Agent-Browser Usage:
#   agent-browser --profile <profile-path> open <url>
#
# Environment Variable:
#   AGENT_BROWSER_PROFILE=<path>  # Set default profile
# =============================================================================

set -e

OUTPUT_JSON=false
SHOW_PATHS=false

for arg in "$@"; do
    case $arg in
        --json) OUTPUT_JSON=true ;;
        --paths) SHOW_PATHS=true ;;
    esac
done

# Detect OS and Chrome profiles location
detect_chrome_base() {
    local os=$(uname -s)
    local base_dir=""

    case "$os" in
        Darwin*)
            # macOS
            base_dir="$HOME/Library/Application Support/Google/Chrome"
            ;;
        MINGW*|MSYS*|CYGWIN*|Windows_NT)
            # Windows - try both LOCALAPPDATA and APPDATA
            if [ -d "$LOCALAPPDATA/Google/Chrome/User Data" ]; then
                base_dir="$LOCALAPPDATA/Google/Chrome/User Data"
            elif [ -d "$APPDATA/Google/Chrome/User Data" ]; then
                base_dir="$APPDATA/Google/Chrome/User Data"
            elif [ -d "/c/Users/$USER/AppData/Local/Google/Chrome/User Data" ]; then
                base_dir="/c/Users/$USER/AppData/Local/Google/Chrome/User Data"
            fi
            ;;
        Linux*)
            base_dir="$HOME/.config/google-chrome"
            ;;
    esac

    echo "$base_dir"
}

# Parse Local State to get profile names
parse_profiles() {
    local base_dir="$1"
    local local_state="$base_dir/Local State"

    if [ ! -f "$local_state" ]; then
        return 1
    fi

    # Try to parse with Python (more reliable)
    if command -v python3 &>/dev/null; then
        python3 -c "
import json
import sys

try:
    with open('$local_state', 'r', encoding='utf-8') as f:
        data = json.load(f)

    profiles = data.get('profile', {}).get('info_cache', {})

    # Default profile
    if 'Default' in profiles:
        default_name = profiles['Default'].get('name', 'Default')
        print(f'Default|Default|{default_name}')

    # Other profiles
    for profile_id, info in profiles.items():
        if profile_id != 'Default':
            name = info.get('name', profile_id)
            print(f'{profile_id}|{profile_id}|{name}')
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
    sys.exit(1)
" 2>/dev/null
        return $?
    fi

    # Fallback: just list directories
    for dir in "$base_dir"/Default "$base_dir"/Profile*; do
        if [ -d "$dir" ]; then
            local profile_name=$(basename "$dir")
            echo "${profile_name}|${profile_name}|${profile_name}"
        fi
    done
}

# List available profiles
list_profiles() {
    local base_dir=$(detect_chrome_base)

    if [ -z "$base_dir" ] || [ ! -d "$base_dir" ]; then
        if [ "$OUTPUT_JSON" = true ]; then
            echo '{"error": "Chrome profiles directory not found", "profiles": []}'
        else
            echo "Error: Chrome profiles directory not found"
            echo "Checked: $base_dir"
        fi
        return 1
    fi

    local profiles=()
    while IFS='|' read -r profile_id profile_dir display_name; do
        profiles+=("$profile_id|$profile_dir|$display_name")
    done < <(parse_profiles "$base_dir")

    if [ ${#profiles[@]} -eq 0 ]; then
        if [ "$OUTPUT_JSON" = true ]; then
            echo '{"error": "No profiles found", "profiles": []}'
        else
            echo "No Chrome profiles found in: $base_dir"
        fi
        return 1
    fi

    if [ "$OUTPUT_JSON" = true ]; then
        echo "{"
        echo "  \"base_dir\": \"$base_dir\","
        echo "  \"profiles\": ["
        local first=true
        for profile in "${profiles[@]}"; do
            IFS='|' read -r id dir name <<< "$profile"
            local profile_path="$base_dir/$dir"

            if [ "$first" = true ]; then
                first=false
            else
                echo ","
            fi
            echo -n "    {\"id\": \"$id\", \"name\": \"$name\", \"path\": \"$profile_path\"}"
        done
        echo ""
        echo "  ],"
        echo "  \"usage\": {"
        echo "    \"agent_browser\": \"agent-browser --profile <path> open <url>\","
        echo "    \"env_var\": \"export AGENT_BROWSER_PROFILE=<path>\""
        echo "  }"
        echo "}"
    else
        echo "Chrome Profiles Directory: $base_dir"
        echo ""
        echo "Available Profiles:"
        echo "─────────────────────────────────────────────────────────────"

        for profile in "${profiles[@]}"; do
            IFS='|' read -r id dir name <<< "$profile"
            local profile_path="$base_dir/$dir"

            if [ "$SHOW_PATHS" = true ]; then
                echo "  [$id] $name"
                echo "       Path: $profile_path"
                echo ""
            else
                echo "  [$id] $name"
            fi
        done

        echo ""
        echo "Usage with agent-browser:"
        echo "─────────────────────────────────────────────────────────────"
        echo ""
        echo "  # Use a specific profile for authenticated sessions:"
        echo "  agent-browser --profile \"\$HOME/.chrome-profiles/myprofile\" open https://linkedin.com"
        echo ""
        echo "  # Or set environment variable:"
        echo "  export AGENT_BROWSER_PROFILE=\"\$HOME/.chrome-profiles/myprofile\""
        echo "  agent-browser open https://linkedin.com"
        echo ""
        echo "  # For gated content (social media, etc.):"
        echo "  agent-browser --profile <path> open https://twitter.com"
        echo "  agent-browser --profile <path> open https://facebook.com"
        echo ""
        if [ "$SHOW_PATHS" != true ]; then
            echo "Tip: Use --paths flag to see full profile paths"
        fi
    fi
}

# Main
list_profiles