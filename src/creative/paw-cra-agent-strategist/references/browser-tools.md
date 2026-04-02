# Browser Research Tools

Agent-browser CLI for authenticated web research, social media analysis, and gated content access.

## Why Agent-Browser

Unlike standard web scraping, agent-browser can use your existing Chrome profile — meaning you stay logged in to all your accounts. This enables:

- **Social media research** while logged in (Instagram, TikTok, LinkedIn, Twitter)
- **Competitor analysis** behind login gates
- **Platform-specific data** that requires authentication
- **Gated content access** (membership sites, subscription services)

## Installation

```bash
# Install via npm
npm install -g agent-browser

# Or via Homebrew
brew install agent-browser

# Initialize Chrome environment
agent-browser install
```

## Profile Discovery

**Before using agent-browser, discover available Chrome profiles:**

```bash
# Run the profile discovery script
python3 ./scripts/chrome-profile-discovery.py

# Or list as JSON for programmatic use
python3 ./scripts/chrome-profile-discovery.py --json
```

This will show all existing Chrome/Edge profiles with authentication data. Use one of these profiles, or create a new dedicated profile.

## Authentication Methods

### Method 1: Use Existing Chrome Profile (Recommended)

Use a profile you're already logged into:

```bash
# Discover your profiles first
python3 ./scripts/chrome-profile-discovery.py --list

# Use a discovered profile (example path from discovery output)
agent-browser --profile "/Users/you/Library/Application Support/Google/Chrome/Profile 1" open https://linkedin.com/feed
```

### Method 2: Create Dedicated Profile

Create a new profile specifically for Strategist research:

```bash
# First run: create profile and login manually
agent-browser --profile ~/.strategist-profile open https://linkedin.com/login

# All future runs: already authenticated
agent-browser --profile ~/.strategist-profile open https://linkedin.com/feed
```

### Method 3: Saved Session State

Export and reuse an authenticated session:

```bash
# 1. Start Chrome with remote debugging
# macOS:
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222

# Windows:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

# 2. Save the authenticated state to agency memory
agent-browser --auto-connect state save "{project-root}/.pawbytes/creative-suites/.auth/session.json"

# 3. Use in research sessions
agent-browser --state "{project-root}/.pawbytes/creative-suites/.auth/session.json" open https://instagram.com
```

## Command Reference

### Navigation

| Command | Description |
|---------|-------------|
| `agent-browser open <url>` | Navigate to URL (aliases: goto, navigate) |
| `agent-browser back` | Go to previous page |
| `agent-browser forward` | Go to next page |
| `agent-browser reload` | Reload current page |
| `agent-browser close` | Close browser |

### Element Selection

| Command | Description |
|---------|-------------|
| `agent-browser snapshot` | Get accessibility tree with element refs |
| `agent-browser snapshot -i` | Get interactive elements only (buttons, inputs, links) |
| `agent-browser snapshot -s "#selector"` | Scope to CSS selector |
| `agent-browser snapshot -d 3` | Limit depth to 3 levels |

**Output format:**
```
[1] @e1 button "Submit"
[2] @e2 link "Learn More"
[3] @e3 textbox "Email"
```

### Interaction

| Command | Description |
|---------|-------------|
| `agent-browser click @e1` | Click element by ref |
| `agent-browser click @e1 --new-tab` | Click and open in new tab |
| `agent-browser fill @e3 "text"` | Type text into input |
| `agent-browser select @e1 "Option"` | Select dropdown option |
| `agent-browser press Enter` | Press keyboard key |
| `agent-browser press Control+a` | Press key combination |
| `agent-browser hover @e1` | Hover over element |
| `agent-browser scroll down 500` | Scroll 500 pixels down |
| `agent-browser scroll up 300` | Scroll 300 pixels up |
| `agent-browser upload @e1 file.pdf` | Upload file |

### Content Extraction

| Command | Description |
|---------|-------------|
| `agent-browser get text @e1` | Get text content of element |
| `agent-browser get text body` | Get all page text |
| `agent-browser get title` | Get page title |
| `agent-browser get url` | Get current URL |
| `agent-browser screenshot` | Capture viewport to temp file |
| `agent-browser screenshot page.png` | Save screenshot to path |
| `agent-browser screenshot --full page.png` | Full page screenshot |
| `agent-browser screenshot --annotate page.png` | Screenshot with element labels |
| `agent-browser pdf output.pdf` | Save page as PDF |

### Tabs

| Command | Description |
|---------|-------------|
| `agent-browser tab` | List all open tabs |
| `agent-browser tab new` | Open new tab |
| `agent-browser tab new https://url.com` | Open new tab with URL |
| `agent-browser tab 2` | Switch to tab index 2 |
| `agent-browser tab close` | Close current tab |
| `agent-browser tab close 2` | Close tab at index 2 |

### Wait & Sync

| Command | Description |
|---------|-------------|
| `agent-browser wait @e1` | Wait for element to appear |
| `agent-browser wait 2000` | Wait 2 seconds |
| `agent-browser wait --load networkidle` | Wait for network idle |

## Research Workflows

### Social Media Analysis (Logged In)

```bash
# Use your Chrome profile
agent-browser --profile ~/.strategist-profile open https://instagram.com/explore

# Wait for content to load
agent-browser wait --load networkidle

# Get interactive elements
agent-browser snapshot -i

# Capture for analysis
agent-browser screenshot --full ./research/instagram-explore.png

# Extract text content
agent-browser get text body > ./research/instagram-content.txt
```

### Competitor Profile Analysis

```bash
# Navigate to competitor's LinkedIn
agent-browser --profile ~/.strategist-profile open https://linkedin.com/company/competitor

# Scroll to load more content
for i in {1..5}; do
    agent-browser scroll down 800
    agent-browser wait 1000
done

# Capture full page
agent-browser screenshot --full ./research/competitor-linkedin-full.png

# Extract posts
agent-browser snapshot -s ".org-update-card"
```

### Trend Analysis on TikTok

```bash
# Open TikTok (logged in via profile)
agent-browser --profile ~/.strategist-profile open https://tiktok.com/foryou

# Wait for videos to load
agent-browser wait --load networkidle

# Snapshot the feed structure
agent-browser snapshot -i

# Scroll and capture multiple views
for i in {1..10}; do
    agent-browser scroll down 600
    agent-browser wait 500
    agent-browser screenshot "./research/tiktok-view-$i.png"
done
```

### Form Research (e.g., Lead Gen Pages)

```bash
agent-browser open https://competitor.com/demo-request

# Get form structure
agent-browser snapshot -i

# Capture form
agent-browser screenshot --annotate ./research/competitor-form.png

# Note the form fields
# [1] @e1 textbox "Name"
# [2] @e2 textbox "Email"
# [3] @e3 textbox "Company"
# [4] @e4 select "Industry"
# [5] @e5 button "Submit"
```

### Content Extraction from Gated Sites

```bash
# Use logged-in session
agent-browser --state "{project-root}/.pawbytes/creative-suites/.auth/session.json" open https://membership-site.com/premium-content

# Wait for content
agent-browser wait --load networkidle

# Extract the article
agent-browser get text article > ./research/premium-article.txt

# Save as PDF for reference
agent-browser pdf ./research/premium-article.pdf
```

## Output Integration

All captured content should be saved to the shared agency memory:

```bash
# Screenshots → research folder
agent-browser screenshot --full "{project-root}/.pawbytes/creative-suites/brands/{brand}/research/screenshots/"

# Text content → analysis files
agent-browser get text body > "{project-root}/.pawbytes/creative-suites/brands/{brand}/research/content-extract.txt"

# PDFs → reports folder
agent-browser pdf "{project-root}/.pawbytes/creative-suites/brands/{brand}/research/page-capture.pdf"
```

## Security Notes

- Auth state files contain session tokens in plaintext
- Store auth files in `.pawbytes/creative-suites/.auth/` (gitignored)
- Never commit auth files to version control
- Use environment variable for profile path: `AGENT_BROWSER_PROFILE`
- Chrome profiles contain sensitive data — use dedicated profiles when possible

## Fallback

If agent-browser is unavailable, fall back to:
- Exa `web_search_exa` and `crawling_exa` for public content
- Web Search tool for general research
- Request user to provide screenshots manually for gated content