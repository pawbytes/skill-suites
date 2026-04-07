# Pawbytes Skill Suites

> 59 AI agent skills for Claude Code — agentic marketing automation, AI creative agency workflows, product development, webinar creation, and developer productivity tools.

## Install

```bash
npx skills add pawbytes/skill-suites
```

The interactive installer lets you pick individual modules or install everything at once.

***

## Modules

### `Marketing Suites` — 23 skills

A full AI marketing team inside Claude Code. One agency agent routes every request to the right specialist automatically — no need to know which skill to call.

| Skill                     | What it does                                                               |
| ------------------------- | -------------------------------------------------------------------------- |
| `paw-mkt-agency`          | Master router — coordinates all 22 specialists from a single prompt        |
| `paw-mkt-sostac`          | Full 6-phase SOSTAC marketing strategy with research-first analysis        |
| `paw-mkt-product-context` | Product positioning, ICP, messaging framework, competitive differentiation |
| `paw-mkt-content`         | Blog posts, whitepapers, case studies, editorial calendars                 |
| `paw-mkt-seo`             | Technical SEO audits, keyword research, pSEO, GEO, link building           |
| `paw-mkt-email`           | Email sequences, newsletters, drip campaigns, lifecycle automation         |
| `paw-mkt-social`          | Organic social strategy, content calendars, hashtag and UGC programs       |
| `paw-mkt-paid-ads`        | Google Ads, Meta Ads, PPC strategy, retargeting, ad creative               |
| `paw-mkt-video`           | YouTube/TikTok/Reels strategy, scripts, SEO, thumbnails                    |
| `paw-mkt-pr`              | Press releases, journalist outreach, crisis comms, reputation management   |
| `paw-mkt-influencer`      | Influencer and creator partnerships, UGC programs, affiliate programs      |
| `paw-mkt-cro`             | Landing pages, signup flows, A/B tests, forms, exit popups, onboarding     |
| `paw-mkt-referral`        | Referral programs, affiliate structures, word-of-mouth campaigns           |
| `paw-mkt-retention`       | Churn prevention, cancel flows, dunning, win-back, health scoring          |
| `paw-mkt-pricing`         | Pricing tiers, freemium models, willingness-to-pay, value metrics          |
| `paw-mkt-launch`          | Product launch plans, GTM strategy, Product Hunt, early access             |
| `paw-mkt-sales`           | Sales decks, pitch decks, demo scripts, objection handling, battle cards   |
| `paw-mkt-community`       | Discord/Slack communities, champions programs, community-led growth        |
| `paw-mkt-analytics`       | GA4, GTM, UTM setup, attribution, measurement infrastructure               |
| `paw-mkt-guerrilla`       | Growth hacks, viral campaigns, low-budget unconventional tactics           |
| `paw-mkt-psychology`      | Behavioral science, cognitive biases, Cialdini persuasion frameworks       |
| `paw-mkt-dashboard`       | SvelteKit + sql.js marketing dashboards with LLM-generated UI              |
| `paw-mkt-setup`           | One-time module setup and configuration                                    |

***

### `Creative Agency Suites` — 15 skills

A full AI creative agency with persistent agent personas and deterministic production workflows. Brief Aria the Creative Director — she coordinates the Designer, Strategist, and Video Producer automatically.

**Agents** (persistent personas with memory across sessions):

| Agent                             | Role                                                                 |
| --------------------------------- | -------------------------------------------------------------------- |
| `paw-cra-agent-creative-director` | Aria — orchestrator, entry point for all creative requests           |
| `paw-cra-agent-designer`          | Visual production — social posts, carousels, brand assets, templates |
| `paw-cra-agent-strategist`        | Research, content strategy, scripts, copy, competitor analysis       |
| `paw-cra-agent-video-producer`    | Short-form, long-form, episodic video, subtitles, voiceover          |

**Workflows** (deterministic production pipelines):

| Workflow                         | What it produces                                                 |
| -------------------------------- | ---------------------------------------------------------------- |
| `paw-cra-campaign-orchestration` | Full campaign — dispatches Designer + Video Producer in parallel |
| `paw-cra-content-research`       | Competitor analysis, trend research, content opportunity bundles |
| `paw-cra-design-social`          | Platform-ready social posts and carousels                        |
| `paw-cra-design-brand`           | Logos, icons, flyers, banners, brand identity assets             |
| `paw-cra-design-batch`           | Bulk asset generation from a content calendar or campaign brief  |
| `paw-cra-video-shortform`        | TikTok, Reels, and YouTube Shorts vertical video                 |
| `paw-cra-video-longform`         | YouTube and web long-form (1–10 min), episodic series            |
| `paw-cra-video-clips`            | Clip extraction and repurposing for multi-platform distribution  |
| `paw-cra-multi-platform-export`  | Resize and encode master assets for every platform spec          |
| `paw-cra-quality-control`        | Cross-asset QC with severity-rated report for full campaigns     |
| `paw-cra-setup`                  | One-time module setup and configuration                          |

***

### `Prodig Suites` — 14 skills

End-to-end product development orchestrator. Transform concepts into production-ready deliverables with research, strategy, and execution phases.

| Skill                            | What it does                                                         |
| -------------------------------- | -------------------------------------------------------------------- |
| `paw-ps-orchestrator`            | Master coordinator — routes requests to appropriate agents/workflows |
| `paw-ps-strategist`              | Product strategist — roadmap, positioning, competitive analysis      |
| `paw-ps-discovery`               | Creative discovery — ideation, market gaps, opportunity mapping      |
| `paw-ps-research`                | Rigorous market research — surveys, interviews, data analysis        |
| `paw-ps-audience`                | Customer insight specialist — personas, segmentation, JTBD           |
| `paw-ps-research-to-brief`       | Convert discovery and research into actionable briefs                |
| `paw-ps-concept-to-product-plan` | Transform accepted concepts into product plans                       |
| `paw-ps-knowledge-executor`      | Build knowledge base content and documentation                       |
| `paw-ps-service-executor`        | Execute service-based product deliverables                           |
| `paw-ps-software-executor`       | Product execution for software and technical deliverables            |
| `paw-ps-template-executor`       | Build template-based assets and frameworks                           |
| `paw-ps-product-package-assembler` | Bundle product artifacts into deliverable packages                  |
| `paw-ps-publish-ready-check`     | Evaluate whether products meet publish-ready criteria                |
| `paw-ps-setup`                   | One-time module setup and configuration                              |

***

### `Webinar Creator Suites` — 4 skills

AI-powered webinar production from research to final deliverable.

| Skill                      | What it does                                                    |
| -------------------------- | --------------------------------------------------------------- |
| `paw-wbc-agent-discovery`  | Research-obsessed strategist — topic research, audience analysis|
| `paw-wbc-agent-producer`   | Structured producer — slides, scripts, recording coordination   |
| `paw-wbc-webinar-creation` | Guided end-to-end webinar creation workflow                     |
| `paw-wbc-setup`            | One-time module setup and configuration                         |

***

### `Utility` — 3 skills

| Skill                    | What it does                                                         |
| ------------------------ | -------------------------------------------------------------------- |
| `paw-tools-presentation` | Generate McKinsey-style HTML slide decks from marketing strategies   |
| `paw-tools-release`      | Automate releases — version bump, changelog, git tag, GitHub release |
| `paw-tools-setup`        | One-time module setup and configuration                              |

***

## Repository Structure

```
skill-suites/
├── src/
│   ├── marketing/           # paw-mkt-* skills (23)
│   │   ├── paw-mkt-agency/
│   │   ├── paw-mkt-content/
│   │   ├── paw-mkt-seo/
│   │   └── ... (20 more)
│   │
│   ├── creative/            # paw-cra-* skills (15)
│   │   ├── paw-cra-agent-creative-director/
│   │   ├── paw-cra-agent-designer/
│   │   └── ... (13 more)
│   │
│   ├── prodig/              # paw-ps-* skills (14)
│   │   ├── paw-ps-orchestrator/
│   │   ├── paw-ps-strategist/
│   │   └── ... (12 more)
│   │
│   ├── webinar/             # paw-wbc-* skills (4)
│   │   ├── paw-wbc-agent-discovery/
│   │   ├── paw-wbc-agent-producer/
│   │   └── ... (2 more)
│   │
│   └── tools/               # paw-tools-* skills (3)
│       ├── paw-tools-presentation/
│       ├── paw-tools-release/
│       └── paw-tools-setup/
│
└── .claude-plugin/
    └── marketplace.json     # unified installer manifest
```

Each skill folder contains:
```
paw-{suite}-{skill-name}/
├── SKILL.md      # Main skill definition and prompts
├── assets/       # Supporting assets (templates, examples)
└── scripts/      # Optional automation scripts
```

***

## Manual Installation Guide

If you're cloning this repository directly (e.g., for use with Claude Code, OpenClaw, or other AI environments), follow these steps:

### Step 1: Clone the Repository

```bash
git clone https://github.com/pawbytes/skill-suites.git
cd skill-suites
```

### Step 2: Copy Skills to Your AI's Skills Folder

Each suite is located under `src/{suite-name}/`. Copy the skill folders to your AI's skills directory:

**For Claude Code:**
```bash
# Copy individual skills (example: marketing setup)
cp -r src/marketing/paw-mkt-setup ~/.claude/skills/

# Copy all skills from a suite
cp -r src/marketing/paw-mkt-* ~/.claude/skills/

# Copy all skills from all suites
cp -r src/marketing/paw-mkt-* ~/.claude/skills/
cp -r src/creative/paw-cra-* ~/.claude/skills/
cp -r src/prodig/paw-ps-* ~/.claude/skills/
cp -r src/webinar/paw-wbc-* ~/.claude/skills/
cp -r src/tools/paw-tools-* ~/.claude/skills/
```

**For OpenClaw or similar environments:**
```bash
# Adjust the destination path to your environment's skills folder
cp -r src/marketing/paw-mkt-* /path/to/your/skills/folder/
```

### Step 3: Run the Setup Skill

After copying skills, run the appropriate setup skill to initialize each suite:

| Suite      | Setup Skill            | What it does                                    |
| ---------- | ---------------------- | ----------------------------------------------- |
| Marketing  | `/paw-mkt-setup`       | Initialize marketing workflows and configuration |
| Creative   | `/paw-cra-setup`       | Set up creative agency agents and workflows      |
| Prodig     | `/paw-ps-setup`        | Initialize product development environment       |
| Webinar    | `/paw-wbc-setup`       | Set up webinar creation workflows                |
| Tools      | `/paw-tools-setup`     | Initialize utility tools                         |

**Example:**
```
/paw-mkt-setup
```

This will:
1. Create necessary configuration files
2. Set up agent personas and memory (for Creative suite)
3. Initialize workflow templates
4. Configure any required integrations

### Quick Reference: Suite Prefixes

| Prefix       | Suite              | Skills Count |
| ------------ | ------------------ | ------------ |
| `paw-mkt-`   | Marketing          | 23           |
| `paw-cra-`   | Creative Agency    | 15           |
| `paw-ps-`    | Prodig             | 14           |
| `paw-wbc-`   | Webinar Creator    | 4            |
| `paw-tools-` | Utility Tools      | 3            |

***

## License

MIT License — use freely for personal and commercial projects.