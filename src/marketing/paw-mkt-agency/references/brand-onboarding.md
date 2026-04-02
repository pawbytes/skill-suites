# Brand Onboarding

## Purpose
Create a new brand workspace with required structure and initial context files.

## Required Information

Gather from user:
- **Brand name** (derive slug: lowercase, hyphens, no special characters)
- **What the brand sells** (product/service, one-liner)
- **Target audience** (who they're marketing to)
- **Current stage** (pre-launch, early stage, established, scaling)

## Optional Information

Ask but don't block:
- Website URL
- Existing social media profiles
- Current marketing efforts
- Budget range
- Key competitors
- Unique selling proposition

## Directory Structure

> See `./directory-structure.md` for full layout. Create top-level directories during onboarding.

```
./.pawbytes/marketing-suites/brands/{brand-slug}/
├── brand-context.md
├── sostac/
│   └── README.md
├── campaigns/
├── channels/
└── operations/
```

## brand-context.md Template

```markdown
# {Brand Name}

## Overview
- **Name**: {Brand Name}
- **Slug**: {brand-slug}
- **Website**: {url or "TBD"}
- **Stage**: {pre-launch | early-stage | established | scaling}
- **Created**: {YYYY-MM-DD}

## What We Do
{One paragraph describing the product/service}

## Target Audience
{Description of primary audience segments}

## Unique Selling Proposition
{What makes this brand different}

## Current Marketing Status
{Summary of existing efforts, or "Starting fresh"}

## Competitors
{List of known competitors, or "To be researched in Situation Analysis"}

## Notes
{Any additional context from the user}
```

## sostac/README.md Template

Create the SOSTAC status tracker:

```markdown
# SOSTAC Plan — {Brand Name}

## Status

| Phase | File | Status |
|---|---|---|
| Situation Analysis | `01-situation.md` | Not Started |
| Objectives | `02-objectives.md` | Not Started |
| Strategy | `03-strategy.md` | Not Started |
| Tactics | `04-tactics.md` | Not Started |
| Action | `05-action.md` | Not Started |
| Control | `06-control.md` | Not Started |

## Last Updated
{YYYY-MM-DD}
```

## After Onboarding

Immediately proceed to SOSTAC planning workflow.