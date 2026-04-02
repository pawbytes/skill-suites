# Getting Started

If you're new to the suite, use this order:

1. **Install the skills**
2. **Start with `/paw-mkt-agency`** for most work
3. **Create or select a brand**
4. **Build strategy with `/paw-mkt-sostac`** if you do not already have one
5. **Create `/paw-mkt-product-context`** so specialist output uses real positioning and customer language
6. **Run specialist skills** for execution

## Install

```bash
npx skills add pawbytes/agentic-marketing-suites
```

Install globally:

```bash
npx skills add pawbytes/agentic-marketing-suites --global
```

Install one skill only:

```bash
npx skills add pawbytes/agentic-marketing-suites --skill marketing-sostac
npx skills add pawbytes/agentic-marketing-suites --skill marketing-seo
```

## First commands to know

```text
/paw-mkt-agency
/paw-mkt-sostac
/paw-mkt-product-context
/paw-mkt-content
/paw-mkt-seo
/paw-mkt-email
/paw-mkt-social
/paw-mkt-paid-ads
```

## Recommended starting paths

### Path 1: New brand, no strategy yet
- Start with `/paw-mkt-agency`
- Let it create or select a brand workspace
- Run `/paw-mkt-sostac`
- Create `/paw-mkt-product-context`
- Move into specialist execution

### Path 2: You already know the task
- Start with `/paw-mkt-agency` or invoke the specialist directly
- Load the right brand
- If no SOSTAC plan exists, the suite may recommend planning first
- Continue with the direct deliverable you need now

### Path 3: Existing brand, plan already complete
- Load the brand
- Review `brands/{brand-slug}/sostac/`
- Refresh `/paw-mkt-product-context` if needed
- Run the relevant specialist skill

## What to prepare before you start

The suite works best when you can provide:
- Brand name and website
- Product or service description
- Target audience
- Current stage: pre-launch, early-stage, established, or scaling
- Known competitors
- Goals, constraints, and timeline
- Existing assets or previous marketing work

## Core brand files

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

## What to read next

- [Docs home](README.md)
- [New brand onboarding](workflows/new-brand-onboarding.md)
- [SOSTAC planning](workflows/sostac-planning.md)
- [Implementation after SOSTAC](workflows/implementation-after-sostac.md)
- [Quick task without a full plan](workflows/quick-task-without-full-plan.md)
