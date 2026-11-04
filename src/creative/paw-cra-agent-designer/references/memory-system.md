# Memory System for Designer

**Shared agency tree:** `{suite-root}/` (memory in `_memory/`, deliverables under `brands/`)

## Core Principle

The Designer shares memory with all agents in the Aria Creative Suite. This ensures brand consistency across all creative outputs—when the Strategist defines brand voice, the Designer knows exactly what it is.

## Shared Memory Structure

```
{suite-root}/
├── _memory/
│   ├── index.md                # Agency roster, active campaigns, status
│   ├── knowledge/              # Researched specs and guides
│   └── daily/{YYYY-MM-DD}.md   # Activity log
├── templates/                  # Reusable design templates
└── brands/
    └── {brand-name}/
        ├── README.md           # Brand dashboard (Status:, Next:, links)
        ├── guidelines.md       # Colors, fonts, logo, visual identity
        ├── research/           # Strategist research reports
        ├── brand-assets/       # logo/, icons/, banners/, avatars/
        ├── campaigns/
        │   └── {YYYY-MM-campaign}/
        │       ├── brief.md    # Approved creative brief
        │       ├── scripts/    # Approved copy/scripts
        │       └── designs/    # social/, carousels/, flyers/, resized/, batch-{date}/
        └── designs/            # Non-campaign work: social/, carousels/, flyers/, resized/, wip/
```

## What to Read

| File | When to Read | Contains |
|------|-------------|----------|
| `_memory/index.md` | Every activation | Active brand, current campaigns |
| `brands/{brand}/guidelines.md` | Before every design task | Colors, typography, logo rules |
| `brands/{brand}/campaigns/{campaign}/brief.md` | When working on campaign | Requirements, deliverables |
| `brands/{brand}/campaigns/{campaign}/scripts/` | When creating visuals | Approved copy, storyboards |

## What to Write

| File | When to Write | Contains |
|------|--------------|----------|
| `brands/{brand}/designs/` (or the campaign's `designs/`) | After every design | Generated visual assets |
| `_memory/daily/{date}.md` | After every task | Activity log entry |
| `brands/{brand}/guidelines.md` | When brand is created/updated | Brand identity elements |

## Read Access

- `{suite-root}/_memory/index.md`
- `{suite-root}/brands/{brand}/guidelines.md`
- `{suite-root}/brands/{brand}/campaigns/{campaign}/brief.md`
- `{suite-root}/brands/{brand}/campaigns/{campaign}/scripts/`
- `{suite-root}/brands/{brand}/research/`

## Write Access

- `{suite-root}/brands/{brand}/designs/` and `{suite-root}/brands/{brand}/brand-assets/`
- `{suite-root}/brands/{brand}/campaigns/{campaign}/designs/`
- `{suite-root}/_memory/daily/{date}.md`
- `{suite-root}/brands/{brand}/guidelines.md` (when creating/updating brand)

## Deny Zones

- `{suite-root}/brands/{other-brand}/` — Other brands not in scope
- Any files outside `{suite-root}/` without explicit permission

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