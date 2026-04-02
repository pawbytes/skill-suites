# Brand Workspace Structure

Brand workspaces are persistent directories containing all context, plans, and artifacts for a specific brand. They enable skills to maintain continuity across sessions and share information.

## Purpose

Brand workspaces serve as:

- **Single source of truth** — All brand information lives in one place
- **Context persistence** — Skills can resume work without re-onboarding
- **Cross-skill coordination** — Different specialists work from the same foundation
- **Progress tracking** — Status files show what's complete and what's pending

## Directory Structure

### Marketing Brand Workspace

```
.pawbytes/marketing-suites/brands/{brand-slug}/
├── brand-context.md              # Brand identity and positioning
├── product-marketing-context.md  # Product-specific context
├── status.md                     # Progress tracking
│
├── sostac/                       # SOSTAC marketing plan
│   ├── README.md                 # Phase completion tracker
│   ├── 00-auto-discovery.md      # Research findings
│   ├── 01-situation.md           # Situation analysis
│   ├── 02-objectives.md          # Objectives and KPIs
│   ├── 03-strategy.md            # Strategy and segmentation
│   ├── 04-tactics.md             # Tactical plan
│   ├── 05-action.md              # Implementation timeline
│   ├── 06-control.md             # Measurement framework
│   └── plan-summary.md           # Executive summary
│
├── campaigns/                    # Campaign coordination
│   └── {type}-{campaign-slug}/
│       ├── README.md             # Campaign overview
│       ├── brief.md              # Campaign brief
│       ├── coordination.md       # Team assignments
│       └── results.md            # Campaign results
│
└── channels/                     # Channel-specific plans
    ├── seo.md
    ├── social.md
    ├── email.md
    └── paid.md
```

### Creative Brand Workspace

```
.pawbytes/creative-suites/brands/{brand-slug}/
├── brand-context.md              # Brand identity and visual guidelines
├── campaigns/                    # Campaign deliverables
│   └── {campaign-slug}/
│       ├── brief.md
│       ├── assets/
│       │   ├── images/
│       │   └── videos/
│       └── status.md
│
├── carousels/                    # Social carousels
│   └── {carousel-slug}/
│       ├── slides/
│       └── export/
│
├── videos/                       # Video productions
│   ├── shortform/
│   │   └── {video-slug}/
│   │       ├── script.md
│   │       ├── assets/
│   │       └── final.mp4
│   └── longform/
│       └── {video-slug}/
│
└── exports/                      # Multi-platform exports
    └── {export-slug}/
        ├── instagram/
        ├── tiktok/
        └── youtube/
```

## Core Files

### brand-context.md

Foundation document containing brand identity:

```markdown
# {Brand Name} - Brand Context

## Brand Identity
- **Name**: {Brand Name}
- **Tagline**: {Tagline}
- **Industry**: {Industry}
- **Founded**: {Year}

## Positioning
- **Target Audience**: {Description}
- **Value Proposition**: {Statement}
- **Key Differentiators**: 
  - {Differentiator 1}
  - {Differentiator 2}

## Brand Voice
- **Tone**: {Tone description}
- **Language Style**: {Style notes}
- **Avoid**: {What to avoid}

## Visual Identity
- **Primary Color**: #{Hex}
- **Secondary Colors**: #{Hex}, #{Hex}
- **Fonts**: {Font names}
- **Logo**: {Path to logo file}

## Key Messages
1. {Message 1}
2. {Message 2}
3. {Message 3}

## Competitors
- {Competitor 1}: {Brief note}
- {Competitor 2}: {Brief note}
```

### status.md

Progress tracking document:

```markdown
# {Brand Name} - Status

## SOSTAC Progress
| Phase | Status | Last Updated |
|-------|--------|--------------|
| Situation | Complete | 2024-01-15 |
| Objectives | Complete | 2024-01-16 |
| Strategy | In Progress | 2024-01-17 |
| Tactics | Not Started | - |
| Action | Not Started | - |
| Control | Not Started | - |

## Active Campaigns
- **launch-q1-2024**: Planning phase
- **social-awareness**: Execution

## Recent Activity
- 2024-01-17: Started Strategy phase
- 2024-01-16: Completed Objectives
- 2024-01-15: Completed Situation analysis

## Next Steps
1. Complete Strategy segmentation
2. Validate targeting with user
3. Begin Tactics planning
```

### sostac/README.md

Phase completion tracker:

```markdown
# SOSTAC Progress Tracker

## Completion Status

**Overall Progress**: 2/6 phases complete (33%)

| Phase | File | Status | Completed |
|-------|------|--------|-----------|
| Situation | 01-situation.md | Complete | 2024-01-15 |
| Objectives | 02-objectives.md | Complete | 2024-01-16 |
| Strategy | 03-strategy.md | In Progress | - |
| Tactics | 04-tactics.md | Not Started | - |
| Action | 05-action.md | Not Started | - |
| Control | 06-control.md | Not Started | - |

## Current Phase: Strategy

**Started**: 2024-01-17
**Focus**: Segmentation and positioning

## Notes
- Situation analysis revealed strong B2B opportunity
- Objectives set for 50% lead growth in Q2
```

## Workspace Lifecycle

### Creation

Brand workspaces are created during onboarding:

1. User provides brand name
2. System generates slug: `{brand-name}` -> `brand-name`
3. Directory created: `.pawbytes/{module}/brands/{brand-slug}/`
4. `brand-context.md` initialized
5. `status.md` created with empty state

### Updates

Workspaces are updated when:

- User provides new brand information
- SOSTAC phases complete
- Campaigns are created or updated
- Progress status changes

### Reading Before Acting

Skills must read existing files before generating content:

```markdown
## Principles
- **Read Before Acting**: Never generate content without first reading the brand's existing files. Brand context, SOSTAC plan, and campaigns are ground truth.
```

## Cross-Module Sharing

When skills from different modules work on the same brand:

1. **Read from both workspaces** — Marketing context informs creative work
2. **Write to module-specific workspace** — Each module maintains its own outputs
3. **Reference, don't duplicate** — Link to shared context rather than copying

Example: Creative agents read marketing brand context for consistency:

```
.pawbytes/marketing-suites/brands/acme-corp/brand-context.md
     ↓ (read by)
.pawbytes/creative-suites/brands/acme-corp/ (creative outputs follow brand guidelines)
```

## Best Practices

1. **Always check for existing workspace** before creating a new one
2. **Read all relevant files** before making recommendations
3. **Update status.md** when completing work
4. **Use consistent slugs** across all references
5. **Maintain README files** for quick status checks