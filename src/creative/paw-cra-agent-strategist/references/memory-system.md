# Memory System

The Strategist reads and writes to the **shared agency memory** at `{project-root}/.pawbytes/creative-suites/`.

## Memory Structure

```
.pawbytes/creative-suites/
├── index.md                    # Agency roster, active campaigns, status
├── daily/
│   └── YYYY-MM-DD.md           # Activity log (append-only)
└── brands/
    └── {brand-name}/
        ├── guidelines.md       # Brand identity
        ├── research/
        │   ├── competitor-analysis.md
        │   ├── content-opportunities.md
        │   └── trend-analysis.md
        └── campaigns/
            └── {campaign-name}/
                ├── brief.md
                ├── scripts/
                ├── copy/
                └── content-calendar.md
```

## What to Read on Activation

1. `{project-root}/.pawbytes/creative-suites/index.md` — agency context
2. If `active_brand` in index: load `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md`
3. If `active_campaign` in index: load the campaign brief

## What to Write

| Output | Path |
|--------|------|
| Competitor analysis | `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/research/competitor-analysis.md` |
| Content opportunities | `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/research/content-opportunities.md` |
| Trend analysis | `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/research/trend-analysis.md` |
| Scripts | `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/scripts/{script-name}.md` |
| Copy drafts | `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/copy/{platform}-{type}.md` |
| Content calendar | `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/content-calendar.md` |

## Activity Logging

Append to `{project-root}/.pawbytes/creative-suites/daily/YYYY-MM-DD.md`:

```markdown
## [Strategist] HH:MM - {Activity}
- {What was done}
- {Key outputs or findings}
```

## Handoff Context

When the Strategist completes work that feeds into production:

1. Update the campaign brief with a "Strategy Complete" section
2. Note which assets are ready for Designer/Video Producer
3. Update `index.md` if the campaign status changed