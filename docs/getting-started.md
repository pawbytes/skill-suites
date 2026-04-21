# Getting Started

Welcome to Pawbytes Skill Suites. This guide helps you install the right module and get started quickly.

## Which Module Should I Use?

| I need to... | Use this module | Start with |
|--------------|-----------------|------------|
| Plan marketing strategy | Marketing | `/paw-mkt-agent-agency` |
| Create content, SEO, ads, email | Marketing | `/paw-mkt-agent-agency` or specialist skill |
| Design social posts, carousels, logos | Creative | `/paw-cra-agent-creative-director` |
| Produce videos (Reels, TikTok, YouTube) | Creative | `/paw-cra-agent-video-producer` |
| Build a presentation from strategy | Tools | `/paw-tools-presentation` |
| Automate software releases | Tools | `/paw-tools-release` |

---

## Install

### Install All Modules

```bash
npx skills add pawbytes/skill-suites
```

### Install Globally

```bash
npx skills add pawbytes/skill-suites --global
```

### Install Specific Skills

```bash
# Marketing skills
npx skills add pawbytes/skill-suites --skill paw-mkt-agent-agency
npx skills add pawbytes/skill-suites --skill paw-mkt-sostac
npx skills add pawbytes/skill-suites --skill paw-mkt-seo

# Creative skills
npx skills add pawbytes/skill-suites --skill paw-cra-agent-creative-director
npx skills add pawbytes/skill-suites --skill paw-cra-agent-designer

# Tools skills
npx skills add pawbytes/skill-suites --skill paw-tools-presentation
npx skills add pawbytes/skill-suites --skill paw-tools-release
```

---

## Marketing Suite (paw-mkt-*)

### First Commands

```text
/paw-mkt-agent-agency          # Central coordinator, routes to specialists
/paw-mkt-sostac          # SOSTAC marketing planning
/paw-mkt-product-context # Product marketing context
/paw-mkt-content         # Content strategy
/paw-mkt-seo             # SEO optimization
/paw-mkt-email           # Email marketing
/paw-mkt-social          # Social media
/paw-mkt-paid-ads        # Paid advertising
```

### Starting Paths

**Path 1: New brand, no strategy yet**
1. Start with `/paw-mkt-agent-agency`
2. Let it create or select a brand workspace
3. Run `/paw-mkt-sostac`
4. Create `/paw-mkt-product-context`
5. Move into specialist execution

**Path 2: You already know the task**
1. Start with `/paw-mkt-agent-agency` or invoke the specialist directly
2. Load the right brand
3. If no SOSTAC plan exists, the suite may recommend planning first
4. Continue with the direct deliverable you need now

**Path 3: Existing brand, plan already complete**
1. Load the brand
2. Review `brands/{brand-slug}/sostac/`
3. Refresh `/paw-mkt-product-context` if needed
4. Run the relevant specialist skill

### What to Prepare

The Marketing suite works best when you can provide:
- Brand name and website
- Product or service description
- Target audience
- Current stage: pre-launch, early-stage, established, or scaling
- Known competitors
- Goals, constraints, and timeline
- Existing assets or previous marketing work

### Core Brand Files

Most work lives under:

```text
brands/{brand-slug}/
├── brand-context.md
├── product-marketing-context.md
├── sostac/
├── campaigns/
├── content/
├── analytics/
└── assets/
```

**Learn more:** [Marketing Module Documentation](./marketing/README.md)

---

## Creative Suite (paw-cra-*)

### First Commands

```text
/paw-cra-agent-creative-director  # Aria - orchestrates all creative work
/paw-cra-agent-designer           # Visual production specialist
/paw-cra-agent-video-producer     # Video production specialist
/paw-cra-agent-strategist         # Research and content strategy (on-demand)
```

### Starting Paths

**Path 1: First creative asset for a brand**
1. Start with `/paw-cra-agent-creative-director` (Aria)
2. Say: "I need a [social post / logo / video] for [brand]"
3. Aria will ask about your brand or load existing context
4. Aria routes to Designer or Video Producer
5. Receive your asset

**Path 2: You need multiple assets**
1. Start with `/paw-cra-agent-creative-director`
2. Describe your campaign: "I need a launch campaign for [product]"
3. Aria creates a plan with recommended assets
4. Approve the plan
5. Aria orchestrates production across Designer and Video Producer

**Path 3: Direct production (you know exactly what you want)**
1. Go straight to Designer: `/paw-cra-agent-designer`
2. Or Video Producer: `/paw-cra-agent-video-producer`
3. Describe your asset
4. Receive your deliverable

### What to Prepare

The Creative suite works best when you have:
- Brand name
- What you want to create (social post, logo, video, etc.)
- Platform (Instagram, TikTok, YouTube, etc.)
- Any brand materials (logo, colors, reference images) -- optional

**Learn more:** [Creative Module Documentation](./creative/README.md)

---

## Tools Suite (paw-tools-*)

### First Commands

```text
/paw-tools-presentation  # Create McKinsey-style HTML presentations
/paw-tools-release       # Automate software releases
```

### When to Use Each Tool

**Presentation Builder** (`/paw-tools-presentation`)
- You have a marketing plan and need to present it
- You need to share strategy with stakeholders
- You want a professional deck without design work

**Release Automation** (`/paw-tools-release`)
- You're ready to release a new version
- You want consistent release processes
- You use conventional commits

### Prerequisites

**Presentation Builder:**
- A marketing plan or strategy document (SOSTAC output works great)

**Release Automation:**
- Git repository
- GitHub CLI installed and authenticated
- Conventional commit messages (feat:, fix:, breaking:)

**Learn more:** [Tools Module Documentation](./tools/README.md)

---

## What to Read Next

- [Docs home](README.md)
- [Marketing Module](./marketing/README.md)
- [New brand onboarding](./marketing/workflows/new-brand-onboarding.md)
- [SOSTAC planning](./marketing/workflows/sostac-planning.md)