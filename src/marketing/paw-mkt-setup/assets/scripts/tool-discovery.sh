#!/bin/bash
# =============================================================================
# Tool Discovery Script for Agentic Marketing Suite
# =============================================================================
# This script checks all CLI tools, MCP servers, and third-party API
# accessibility required by the marketing suite skills.
#
# Usage:
#   ./tool-discovery.sh [--json] [--check-apis] [--verbose]
#
# Options:
#   --json       Output results in JSON format
#   --check-apis Also check third-party API connectivity (slower)
#   --verbose    Show detailed output for each check
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse arguments
OUTPUT_JSON=false
CHECK_APIS=false
VERBOSE=false

for arg in "$@"; do
    case $arg in
        --json) OUTPUT_JSON=true ;;
        --check-apis) CHECK_APIS=true ;;
        --verbose) VERBOSE=true ;;
    esac
done

# Results arrays
declare -A CLI_TOOLS
declare -A MCP_TOOLS
declare -A APIS

# =============================================================================
# CLI Tool Checks
# =============================================================================

check_cli_tool() {
    local tool_name="$1"
    local check_command="$2"
    local install_hint="$3"

    if eval "$check_command" &>/dev/null; then
        CLI_TOOLS["$tool_name"]="available"
        if [ "$VERBOSE" = true ]; then
            echo -e "${GREEN}✓${NC} $tool_name: available"
        fi
    else
        CLI_TOOLS["$tool_name"]="missing"
        if [ "$VERBOSE" = true ]; then
            echo -e "${RED}✗${NC} $tool_name: missing"
            echo -e "  Install: $install_hint"
        fi
    fi
}

check_agent_browser() {
    local tool_name="agent-browser"
    local install_hint="npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser OR npm install -g agent-browser && npx playwright install chromium"

    if command -v agent-browser &>/dev/null; then
        # Check if playwright browser is installed
        if agent-browser --version &>/dev/null; then
            CLI_TOOLS["$tool_name"]="available"
            if [ "$VERBOSE" = true ]; then
                local version=$(agent-browser --version 2>/dev/null || echo "unknown")
                echo -e "${GREEN}✓${NC} $tool_name: available (v$version)"
            fi
        else
            CLI_TOOLS["$tool_name"]="partial"
            if [ "$VERBOSE" = true ]; then
                echo -e "${YELLOW}⚠${NC} $tool_name: installed but browser not ready"
                echo -e "  Fix: npx playwright install chromium"
            fi
        fi
    else
        CLI_TOOLS["$tool_name"]="missing"
        if [ "$VERBOSE" = true ]; then
            echo -e "${RED}✗${NC} $tool_name: missing"
            echo -e "  Install: $install_hint"
        fi
    fi
}

# =============================================================================
# MCP Tool Checks
# =============================================================================

check_mcp_tool() {
    local tool_name="$1"
    local description="$2"
    # MCP tools are checked by their availability in the Claude environment
    # This is a placeholder - actual MCP availability is determined by the host
    MCP_TOOLS["$tool_name"]="check_in_claude_session"
}

# =============================================================================
# API Checks
# =============================================================================

check_api() {
    local api_name="$1"
    local endpoint="$2"

    if [ "$CHECK_APIS" = true ]; then
        if curl -s --max-time 5 "$endpoint" &>/dev/null; then
            APIS["$api_name"]="reachable"
            if [ "$VERBOSE" = true ]; then
                echo -e "${GREEN}✓${NC} $api_name: reachable"
            fi
        else
            APIS["$api_name"]="unreachable"
            if [ "$VERBOSE" = true ]; then
                echo -e "${YELLOW}⚠${NC} $api_name: unreachable (may require auth or VPN)"
            fi
        fi
    else
        APIS["$api_name"]="skipped"
    fi
}

# =============================================================================
# Chrome Profile Discovery
# =============================================================================

discover_chrome_profiles() {
    local profiles_dir=""
    local os=$(uname -s)

    case "$os" in
        Darwin*)
            profiles_dir="$HOME/Library/Application Support/Google/Chrome"
            ;;
        MINGW*|MSYS*|CYGWIN*)
            profiles_dir="$LOCALAPPDATA/Google/Chrome/User Data"
            if [ ! -d "$profiles_dir" ]; then
                profiles_dir="$APPDATA/Google/Chrome/User Data"
            fi
            ;;
        Linux*)
            profiles_dir="$HOME/.config/google-chrome"
            ;;
    esac

    if [ -d "$profiles_dir" ]; then
        echo "$profiles_dir"
        return 0
    else
        return 1
    fi
}

# =============================================================================
# Main Execution
# =============================================================================

run_checks() {
    if [ "$VERBOSE" = true ] && [ "$OUTPUT_JSON" = false ]; then
        echo -e "\n${BLUE}═══════════════════════════════════════════════════════════${NC}"
        echo -e "${BLUE}  Agentic Marketing Suite - Tool Discovery${NC}"
        echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

        echo -e "${YELLOW}CLI Tools:${NC}"
    fi

    # Check CLI tools
    check_cli_tool "node" "node --version" "https://nodejs.org/"
    check_cli_tool "npm" "npm --version" "https://nodejs.org/"
    check_cli_tool "npx" "npx --version" "https://nodejs.org/"
    check_cli_tool "python3" "python3 --version" "https://www.python.org/"
    check_cli_tool "git" "git --version" "https://git-scm.com/"
    check_agent_browser

    if [ "$VERBOSE" = true ] && [ "$OUTPUT_JSON" = false ]; then
        echo -e "\n${YELLOW}MCP Tools (check availability in Claude session):${NC}"
    fi

    # MCP Tools - these are available within Claude environment
    check_mcp_tool "WebFetch" "Fetch web content"
    check_mcp_tool "WebSearch" "Web search capability"

    if [ "$CHECK_APIS" = true ]; then
        if [ "$VERBOSE" = true ] && [ "$OUTPUT_JSON" = false ]; then
            echo -e "\n${YELLOW}API Connectivity:${NC}"
        fi

        # Marketing-relevant APIs
        check_api "Google" "https://www.google.com"
        check_api "Facebook Ads Library" "https://www.facebook.com/ads/library"
        check_api "Google Ads Transparency" "https://adstransparency.google.com"
    fi
}

print_summary() {
    if [ "$OUTPUT_JSON" = true ]; then
        echo "{"
        echo '  "cli_tools": {'
        local first=true
        for tool in "${!CLI_TOOLS[@]}"; do
            if [ "$first" = true ]; then
                first=false
            else
                echo ","
            fi
            echo -n "    \"$tool\": \"${CLI_TOOLS[$tool]}\""
        done
        echo ""
        echo "  },"
        echo '  "mcp_tools": {'
        first=true
        for tool in "${!MCP_TOOLS[@]}"; do
            if [ "$first" = true ]; then
                first=false
            else
                echo ","
            fi
            echo -n "    \"$tool\": \"${MCP_TOOLS[$tool]}\""
        done
        echo ""
        echo "  },"
        echo '  "apis": {'
        first=true
        for api in "${!APIS[@]}"; do
            if [ "$first" = true ]; then
                first=false
            else
                echo ","
            fi
            echo -n "    \"$api\": \"${APIS[$api]}\""
        done
        echo ""
        echo "  },"

        # Chrome profiles
        local chrome_dir=$(discover_chrome_profiles 2>/dev/null || echo "")
        echo "  \"chrome_profiles_dir\": \"$chrome_dir\","
        echo "  \"chrome_available\": $([ -n "$chrome_dir" ] && echo "true" || echo "false")"
        echo "}"
    else
        echo -e "\n${BLUE}═══════════════════════════════════════════════════════════${NC}"
        echo -e "${BLUE}  Summary${NC}"
        echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

        # Count statuses
        local available=0
        local missing=0
        local partial=0

        for tool in "${!CLI_TOOLS[@]}"; do
            case "${CLI_TOOLS[$tool]}" in
                available) ((available++)) ;;
                missing) ((missing++)) ;;
                partial) ((partial++)) ;;
            esac
        done

        echo -e "CLI Tools: ${GREEN}$available available${NC}, ${YELLOW}$partial partial${NC}, ${RED}$missing missing${NC}"

        # Chrome profile info
        local chrome_dir=$(discover_chrome_profiles 2>/dev/null || echo "")
        if [ -n "$chrome_dir" ]; then
            echo -e "\n${GREEN}Chrome Profiles Directory:${NC}"
            echo -e "  $chrome_dir"
            echo -e "\n${BLUE}Tip:${NC} Use --profile flag with agent-browser for authenticated sessions"
            echo -e "  Example: agent-browser --profile ~/.myapp-profile open https://linkedin.com"
        else
            echo -e "\n${YELLOW}Chrome profiles directory not found${NC}"
        fi

        # Recommendations
        if [ "${CLI_TOOLS[agent-browser]}" = "missing" ]; then
            echo -e "\n${YELLOW}⚠ Recommended Action:${NC}"
            echo -e "  Install agent-browser for live website research capabilities:"
            echo -e "  ${BLUE}npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser${NC}"
        elif [ "${CLI_TOOLS[agent-browser]}" = "partial" ]; then
            echo -e "\n${YELLOW}⚠ Action Required:${NC}"
            echo -e "  Complete agent-browser setup by installing Chromium:"
            echo -e "  ${BLUE}npx playwright install chromium${NC}"
        fi
    fi
}

# Run the checks
run_checks
print_summary