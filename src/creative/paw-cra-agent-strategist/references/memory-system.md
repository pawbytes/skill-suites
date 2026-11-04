# Memory System

The Strategist reads and writes the **shared agency tree** at `{suite-root}/` (memory in `_memory/`).

## Memory Structure

```
{suite-root}/
├── _memory/
│   ├── index.md                # Agency roster, active campaigns, status
│   └── daily/YYYY-MM-DD.md     # Activity log (append-only)
└── brands/
    └── {brand-name}/
        ├── README.md           # Brand dashboard (Status:, Next:, links)
        ├── guidelines.md       # Brand identity
        ├── research/
        │   ├── competitor-analysis.md
        │   ├── content-opportunities.md
        │   ├── trend-analysis.md
        │   └── screenshots/
        └── campaigns/
            └── {YYYY-MM-campaign}/
                ├── brief.md
                ├── scripts/
                ├── copy/
                └── content-calendar.md
```

## What to Read on Activation

1. `{suite-root}/_memory/index.md` — agency context
2. If `active_brand` in index: load `{suite-root}/brands/{brand-name}/guidelines.md`
3. If `active_campaign` in index: load the campaign brief

## What to Write

| Output | Path |
|--------|------|
| Competitor analysis | `{suite-root}/brands/{brand-name}/research/competitor-analysis.md` |
| Content opportunities | `{suite-root}/brands/{brand-name}/research/content-opportunities.md` |
| Trend analysis | `{suite-root}/brands/{brand-name}/research/trend-analysis.md` |
| Scripts | `{suite-root}/brands/{brand-name}/campaigns/{campaign}/scripts/{script-name}.md` |
| Copy drafts | `{suite-root}/brands/{brand-name}/campaigns/{campaign}/copy/{platform}-{type}.md` |
| Content calendar | `{suite-root}/brands/{brand-name}/campaigns/{campaign}/content-calendar.md` |

## Activity Logging

Append to `{suite-root}/_memory/daily/YYYY-MM-DD.md`:

```markdown
## [Strategist] HH:MM - {Activity}
- {What was done}
- {Key outputs or findings}
```

## Handoff Context

When the Strategist completes work that feeds into production:

1. Update the campaign brief with a "Strategy Complete" section
2. Note which assets are ready for Designer/Video Producer
3. Update `{suite-root}/_memory/index.md` if the campaign status changed