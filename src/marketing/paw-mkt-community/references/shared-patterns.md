# Shared Skill Patterns

These patterns are referenced by all marketing specialist skills. Read them as part of your operating instructions.

## Starting Context Router

Choose the starting mode before doing the work. Brand workspace context is preferred, but do not block progress if the user provides a real codebase or live URL.

### Context A — Blank Page / Strategy Work
Use when the user needs strategy, planning, or a fresh roadmap. Read brand and SOSTAC context first when available, then align recommendations to audience, objections, and business goals.

### Context B — Existing Local Codebase / Implementation Work
Use when the user wants changes made or specified in an existing repository, site, product, or app. Before proposing changes, deeply research the codebase: inspect the stack, architecture, relevant files, dependencies, and existing patterns. Match existing conventions before changing anything.

### Context C — Live Website URL Audit
Use when the user provides a public URL for review. Audit the live experience first. If brand files are missing, use the live page and visible structure as the working source of truth.

## Pre-Flight: Read Strategic Context

Before any specialist work, read these files in order when available:

1. `./.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md` — brand identity, audience, USP
2. `./.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md` — deep positioning, customer language, objections
3. `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/03-strategy.md` — target segments, positioning
4. `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/04-tactics.md` — channel plan, priorities

If brand files are missing but a codebase or live URL is available, continue with that as the working source of truth rather than blocking progress.

## Pre-Flight: Tool Discovery

Before starting work that requires external tools, run the tool discovery script to check availability:

```bash
# Run tool discovery
./skills/paw-mkt-setup/assets/scripts/tool-discovery.sh --verbose

# On Windows
.\skills\paw-mkt-setup\assets\scripts\tool-discovery.bat --verbose
```

### Required Tools Check

| Tool | Check Command | Purpose |
|------|---------------|---------|
| `node` | `node --version` | JavaScript runtime |
| `npm/npx` | `npm --version` | Package management |
| `agent-browser` | `agent-browser --version` | Browser automation |
| `python3` | `python3 --version` | Configuration scripts |
| `git` | `git --version` | Version control |

### Fallback Behavior

- If `agent-browser` is unavailable, use `WebFetch` and `WebSearch` MCP tools for research tasks
- MCP tools have limitations: no authenticated sessions, limited JS rendering support
- For best results, install agent-browser before research-heavy tasks

## agent-browser Setup

Before running browser-based research, check if `agent-browser` is available (`agent-browser --version`). If the command is not found, install it:

```bash
# Install the agent-browser skill (recommended)
npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser

# Or install the CLI directly
npm install -g agent-browser && npx playwright install chromium
```

If installation fails, use `WebFetch` and `WebSearch` tools as alternatives for all research tasks.

## Authenticated Browser Sessions

For gated content (LinkedIn, Twitter/X, Facebook, competitor dashboards, etc.), use persistent browser profiles to maintain authentication.

### Discover Chrome Profiles

```bash
# List available Chrome profiles
./skills/paw-mkt-setup/assets/scripts/chrome-profiles.sh --paths

# On Windows
.\skills\paw-mkt-setup\assets\scripts\chrome-profiles.bat --paths
```

### Using Profiles with agent-browser

```bash
# Method 1: Direct profile path
agent-browser --profile ~/.myapp-profile open https://linkedin.com

# Method 2: Environment variable (persists across commands)
export AGENT_BROWSER_PROFILE=~/.myapp-profile
agent-browser open https://linkedin.com

# Method 3: Import auth from existing Chrome session
# First, start Chrome with remote debugging:
# macOS: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
# Windows: "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

# Then save the auth state:
agent-browser --auto-connect state save ./my-auth.json

# Use saved auth in future sessions:
agent-browser --state ./my-auth.json open https://linkedin.com
```

### Authenticated Research Patterns

#### LinkedIn Research (Requires Login)
```bash
# First run: login manually
agent-browser --profile ~/.linkedin-profile open https://linkedin.com/login
# ... complete login flow manually ...

# All future runs: already authenticated
agent-browser --profile ~/.linkedin-profile open "https://www.linkedin.com/search/results/people/?keywords=marketing"
agent-browser get text body
```

#### Facebook Ads Library (Partial Auth)
```bash
# Public access available, but logged-in sees more
agent-browser open "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q={brand-name}"
agent-browser wait --load networkidle
agent-browser get text body
```

#### Twitter/X Research (Requires Login)
```bash
# Use profile for authenticated access
agent-browser --profile ~/.twitter-profile open "https://twitter.com/search?q={brand-name}"
agent-browser wait --load networkidle
agent-browser get text body
```

#### Competitor Dashboards (App Login Required)
```bash
# Login once, reuse session
agent-browser --profile ~/.competitor-research open https://app.competitor.com/login
# ... complete login ...

# Later: access dashboard
agent-browser --profile ~/.competitor-research open https://app.competitor.com/dashboard
agent-browser screenshot ./research/competitor-dashboard.png
agent-browser get text body
```

### Security Notes

- Auth state files contain sensitive session tokens in plaintext
- Add auth files to `.gitignore`
- Use dedicated profiles for automation, not personal profiles
- Consider using separate browser profiles per client/project

## Common agent-browser Commands

### Session Management
```bash
# Named session (shared context across commands)
agent-browser --session research open https://example.com
agent-browser --session research wait --load networkidle
agent-browser --session research get text body
agent-browser --session research close

# Anonymous session (ephemeral)
agent-browser open https://example.com
agent-browser close
```

### Navigation & Interaction
```bash
# Open URL
agent-browser open https://example.com

# Wait for page load
agent-browser wait --load networkidle
agent-browser wait 2000  # Wait 2 seconds

# Take screenshot
agent-browser screenshot ./output/page.png
agent-browser screenshot --full ./output/fullpage.png

# Get page content
agent-browser get text body
agent-browser get html body

# Interactive elements
agent-browser snapshot -i  # Get interactive elements with refs
agent-browser click @e1    # Click element by ref
agent-browser fill @e2 "search term"  # Fill input
```

### Research Workflow
```bash
# Standard research session
agent-browser --session research open "https://example.com/pricing"
agent-browser wait --load networkidle
agent-browser screenshot ./screenshots/pricing-page.png
agent-browser get text body
agent-browser --session research close
```

## Fallback: WebFetch/WebSearch

When `agent-browser` is unavailable, use MCP tools:

```
# Use WebSearch for discovery
WebSearch: "competitor pricing comparison [industry]"

# Use WebFetch for specific pages
WebFetch: https://example.com/pricing
Prompt: Extract pricing tiers, features, and pricing model details
```

### Limitations of MCP Tools
- No JavaScript rendering (SPA content may be missing)
- No authenticated sessions (gated content inaccessible)
- No interactive elements (forms, buttons)
- Limited to publicly accessible pages