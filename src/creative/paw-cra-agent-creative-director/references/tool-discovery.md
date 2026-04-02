# Tool Discovery

Discover what creative tools are available and report capabilities to the user. This is critical — never promise deliverables that cannot be produced.

## What to Check

Run `python3 ./scripts/tool-discovery.py` to get a structured report of available tools. The script checks:

**CLI Tools:**
- `ffmpeg` — video processing, format conversion
- `agent-browser` — browser automation for AI agents (research, web navigation, screenshots)
- `loopwind` — video looping (optional)
- `egaki` — video editing (optional)

**MCP Servers:**
- `fal` — AI image/video generation via fal.ai
- `exa` — web search for research
- `pencil` — design file editing (.pen files)
- `pinescript-docs` — Pine Script documentation (specialized)

**API Keys (from config):**
- `fal_key` — fal.ai access
- `elevenlabs_api_key` — voice synthesis (optional)
- `pexels_api_key` — stock media access

## agent-browser Details

agent-browser is a Rust-based browser automation CLI designed for AI agents. It provides compact text output optimized for minimal context usage.

**Installation:**
```bash
npm install -g agent-browser
agent-browser install  # Downloads Chrome
```

**Key Commands:**
| Command | Purpose |
|---------|---------|
| `agent-browser open <url>` | Navigate to URL |
| `agent-browser snapshot -i` | Get accessibility tree with refs |
| `agent-browser click @<ref>` | Click by reference |
| `agent-browser screenshot <file>` | Take screenshot |
| `agent-browser close` | Close browser |

**Use Cases for Creative Work:**
- Research competitor websites and visual trends
- Capture reference screenshots for design briefs
- Navigate stock media sites (Pexels, Unsplash)
- Test campaign landing pages
- Extract web content for copywriting research

**Social Media Analysis (Using Your Chrome Profile):**

agent-browser can connect to your existing Chrome browser via CDP mode to leverage your logged-in sessions. This enables analysis of platforms requiring authentication.

**Setup — Connect to Your Chrome:**
```bash
# Step 1: Start Chrome with remote debugging
# Windows:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
# macOS:
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Step 2: Log into your social media accounts in that Chrome window

# Step 3: Connect agent-browser to your live Chrome
agent-browser connect 9222
# Or use auto-connect to discover automatically
agent-browser --auto-connect snapshot
```

**Save Authentication State for Reuse:**
```bash
# Export auth state from your logged-in Chrome
agent-browser --auto-connect state save ./social-auth.json

# Use saved auth in future sessions (no need to re-login)
agent-browser --state ./social-auth.json open https://instagram.com
```

**Competitor Analysis Use Cases:**
| Platform | What to Analyze |
|----------|-----------------|
| Instagram | Competitor posts, engagement metrics, hashtag strategies |
| LinkedIn | Brand presence, content performance, audience growth |
| Twitter/X | Competitor tweets, engagement patterns, trending topics |
| TikTok | Viral content, trending sounds, competitor creative |
| Facebook | Brand pages, ad creative, community engagement |
| Pinterest | Board structures, pin performance, visual trends |
| YouTube | Competitor channels, video performance, thumbnails |

**Analysis Workflow:**
1. Connect to your Chrome with active social media logins
2. Navigate to competitor profiles/pages
3. Capture snapshots for content extraction: `agent-browser snapshot -i`
4. Take screenshots for visual reference: `agent-browser screenshot competitor.png`
5. Extract engagement data, content patterns, and creative insights

**Session Management for Multiple Brands:**
```bash
# Separate sessions for different research contexts
agent-browser --session-name brand-a-research open https://instagram.com/brand_a
agent-browser --session-name brand-b-research open https://instagram.com/brand_b

# List active sessions
agent-browser session list
```

## Output Interpretation

The script returns JSON with readiness status. Present findings conversationally:

- **Fully equipped** — "We have everything needed for full creative production."
- **Partial** — "We can create images and videos, but voice synthesis isn't configured."
- **Limited** — "Some tools are missing. Here's what's available and what alternatives exist."

## When to Run

- **First activation** — always run if no tool status in memory
- **When user requests** — "check my tools" or "what can you do?"
- **When starting a campaign** — confirm capabilities before committing

## Fallback Behavior

If the script cannot execute, manually check tool availability:
- CLI tools: ask user if installed
- API keys: check config values
- MCP servers: test with a simple query

Store the discovered state in memory under `tool-status.md`.