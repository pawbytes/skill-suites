# Pawbytes Skill Suites

> 41 AI agent skills for Claude Code — agentic marketing automation, AI creative agency workflows, and developer productivity tools.

## Install

```bash
npx skills add pawbytes/pawbytes-skill-suites
```

The interactive installer lets you pick individual modules or install everything at once.

---

## Modules

### `paw-agentic-marketing` — 23 skills

A full AI marketing team inside Claude Code. One agency agent routes every request to the right specialist automatically — no need to know which skill to call.

| Skill | What it does |
|---|---|
| `paw-mkt-agency` | Master router — coordinates all 22 specialists from a single prompt |
| `paw-mkt-sostac` | Full 6-phase SOSTAC marketing strategy with research-first analysis |
| `paw-mkt-product-context` | Product positioning, ICP, messaging framework, competitive differentiation |
| `paw-mkt-content` | Blog posts, whitepapers, case studies, editorial calendars |
| `paw-mkt-seo` | Technical SEO audits, keyword research, pSEO, GEO, link building |
| `paw-mkt-email` | Email sequences, newsletters, drip campaigns, lifecycle automation |
| `paw-mkt-social` | Organic social strategy, content calendars, hashtag and UGC programs |
| `paw-mkt-paid-ads` | Google Ads, Meta Ads, PPC strategy, retargeting, ad creative |
| `paw-mkt-video` | YouTube/TikTok/Reels strategy, scripts, SEO, thumbnails |
| `paw-mkt-pr` | Press releases, journalist outreach, crisis comms, reputation management |
| `paw-mkt-influencer` | Influencer and creator partnerships, UGC programs, affiliate programs |
| `paw-mkt-cro` | Landing pages, signup flows, A/B tests, forms, exit popups, onboarding |
| `paw-mkt-referral` | Referral programs, affiliate structures, word-of-mouth campaigns |
| `paw-mkt-retention` | Churn prevention, cancel flows, dunning, win-back, health scoring |
| `paw-mkt-pricing` | Pricing tiers, freemium models, willingness-to-pay, value metrics |
| `paw-mkt-launch` | Product launch plans, GTM strategy, Product Hunt, early access |
| `paw-mkt-sales` | Sales decks, pitch decks, demo scripts, objection handling, battle cards |
| `paw-mkt-community` | Discord/Slack communities, champions programs, community-led growth |
| `paw-mkt-analytics` | GA4, GTM, UTM setup, attribution, measurement infrastructure |
| `paw-mkt-guerrilla` | Growth hacks, viral campaigns, low-budget unconventional tactics |
| `paw-mkt-psychology` | Behavioral science, cognitive biases, Cialdini persuasion frameworks |
| `paw-mkt-dashboard` | SvelteKit + sql.js marketing dashboards with LLM-generated UI |
| `paw-mkt-setup` | One-time module setup and configuration |

---

### `paw-creative-agency` — 15 skills

A full AI creative agency with persistent agent personas and deterministic production workflows. Brief Aria the Creative Director — she coordinates the Designer, Strategist, and Video Producer automatically.

**Agents** (persistent personas with memory across sessions):

| Agent | Role |
|---|---|
| `paw-cra-agent-creative-director` | Aria — orchestrator, entry point for all creative requests |
| `paw-cra-agent-designer` | Visual production — social posts, carousels, brand assets, templates |
| `paw-cra-agent-strategist` | Research, content strategy, scripts, copy, competitor analysis |
| `paw-cra-agent-video-producer` | Short-form, long-form, episodic video, subtitles, voiceover |

**Workflows** (deterministic production pipelines):

| Workflow | What it produces |
|---|---|
| `paw-cra-campaign-orchestration` | Full campaign — dispatches Designer + Video Producer in parallel |
| `paw-cra-content-research` | Competitor analysis, trend research, content opportunity bundles |
| `paw-cra-design-social` | Platform-ready social posts and carousels |
| `paw-cra-design-brand` | Logos, icons, flyers, banners, brand identity assets |
| `paw-cra-design-batch` | Bulk asset generation from a content calendar or campaign brief |
| `paw-cra-video-shortform` | TikTok, Reels, and YouTube Shorts vertical video |
| `paw-cra-video-longform` | YouTube and web long-form (1–10 min), episodic series |
| `paw-cra-video-clips` | Clip extraction and repurposing for multi-platform distribution |
| `paw-cra-multi-platform-export` | Resize and encode master assets for every platform spec |
| `paw-cra-quality-control` | Cross-asset QC with severity-rated report for full campaigns |
| `paw-cra-setup` | One-time module setup and configuration |

---

### `paw-tools` — 3 skills

| Skill | What it does |
|---|---|
| `paw-tools-presentation` | Generate McKinsey-style HTML slide decks from marketing strategies |
| `paw-tools-release` | Automate releases — version bump, changelog, git tag, GitHub release |
| `paw-tools-setup` | One-time module setup and configuration |

---

## Repository Structure

```
pawbytes-skill-suites/
├── src/
│   ├── marketing/          # paw-mkt-* skills (23)
│   ├── creative/           # paw-cra-* skills (15)
│   └── tools/              # paw-tools-* skills (3)
├── _bmad/
│   ├── bmb/                # BMad builder tools
│   └── core/               # BMad core skills
└── .claude-plugin/
    └── marketplace.json    # unified installer manifest
```

## Development

Skills are built using the [BMad Module Builder](https://github.com/bmad-build/bmad-module-builder). The builder is preconfigured in `_bmad/bmb/config.yaml` to output new skills to `src/{module}/`.

```bash
# Build a new skill
/bmad-module-builder --target-dir src/marketing/

# Run the release workflow
/paw-tools-release
```
