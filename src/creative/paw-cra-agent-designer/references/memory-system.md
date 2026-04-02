# Memory System for Designer

**Memory location:** `.pawbytes/creative-suites/` (Shared Agency Memory)

## Core Principle

The Designer shares memory with all agents in the Aria Creative Suite. This ensures brand consistency across all creative outputs—when the Strategist defines brand voice, the Designer knows exactly what it is.

## Shared Memory Structure

```
.pawbytes/creative-suites/
├── index.md                    # Agency roster, active campaigns, status
├── brands/
│   └── {brand-name}/
│       ├── guidelines.md       # Colors, fonts, logo, visual identity
│       ├── research/           # Strategist research reports
│       ├── campaigns/
│       │   └── {campaign}/
│       │       ├── brief.md    # Approved creative brief
│       │       ├── scripts/    # Approved copy/scripts
│       │       └── assets/     # Generated assets
│       └── assets/
│           ├── social/
│           ├── carousels/
│           ├── flyers/
│           └── brand-identity/
└── daily/
    └── {YYYY-MM-DD}.md         # Activity log
```

## What to Read

| File | When to Read | Contains |
|------|-------------|----------|
| `index.md` | Every activation | Active brand, current campaigns |
| `brands/{brand}/guidelines.md` | Before every design task | Colors, typography, logo rules |
| `brands/{brand}/campaigns/{campaign}/brief.md` | When working on campaign | Requirements, deliverables |
| `brands/{brand}/campaigns/{campaign}/scripts/` | When creating visuals | Approved copy, storyboards |

## What to Write

| File | When to Write | Contains |
|------|--------------|----------|
| `brands/{brand}/assets/` | After every design | Generated visual assets |
| `daily/{date}.md` | After every task | Activity log entry |
| `brands/{brand}/guidelines.md` | When brand is created/updated | Brand identity elements |

## Read Access

- `.pawbytes/creative-suites/index.md`
- `.pawbytes/creative-suites/brands/{brand}/guidelines.md`
- `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/brief.md`
- `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/`
- `.pawbytes/creative-suites/brands/{brand}/research/`

## Write Access

- `.pawbytes/creative-suites/brands/{brand}/assets/`
- `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/assets/`
- `.pawbytes/creative-suites/daily/{date}.md`
- `.pawbytes/creative-suites/brands/{brand}/guidelines.md` (when creating/updating brand)

## Deny Zones

- `.pawbytes/creative-suites/brands/{other-brand}/` — Other brands not in scope
- Any files outside `.pawbytes/creative-suites/` without explicit permission

## Save Triggers

Always update memory after:

1. **Creating visual assets** — Log location, type, campaign
2. **Brand guideline changes** — Update guidelines.md immediately
3. **Design decisions confirmed** — Note in daily log
4. **User preference discovered** — Update brand notes if brand-specific

## Activity Log Format

```markdown
## {HH:MM} [Designer]
**Task:** {capability type}
**For:** {brand}/{campaign}
**Output:** {file paths}
**Notes:** {any relevant notes}
```

## Brand Guidelines Template

When creating new brand guidelines:

```markdown
# {Brand Name} Brand Guidelines

## Colors
| Role | Name | HEX |
|------|------|-----|
| Primary | {name} | #XXXXXX |
| Secondary | {name} | #XXXXXX |
| Accent | {name} | #XXXXXX |
| Background | {name} | #XXXXXX |
| Text | {name} | #XXXXXX |

## Typography
- Headlines: {Font Family} {Weight}
- Body: {Font Family} {Weight}
- Accent: {Font Family} {Weight}

## Logo
- Path: {path to logo files}
- Clear space: {measurement}
- Minimum size: {measurement}

## Visual Style
- Photography: {description}
- Illustration: {description}
- Overall aesthetic: {description}

## Design Notes
- {any additional notes}
```