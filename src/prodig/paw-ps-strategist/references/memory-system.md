# Memory System

The Product Strategist reads and writes to the **shared sidecar memory** at `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/`.

## Memory Structure

```
.pawbytes/prodig-suites/memory/paw-ps-sidecar/
├── index.md                    # Sidecar index, status, active context
├── curated/
│   ├── product-context.md      # Current product context
│   ├── product-decisions.md    # Product decisions (output)
│   ├── market-intelligence.md  # Market research (input)
│   └── audience-intelligence.md # Audience insights (input)
├── daily/
│   └── YYYY-MM-DD.md           # Activity log (append-only)
└── archive/
    └── {archived-items}/       # Historical decisions
```

## What to Read on Activation

1. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md` — sidecar context and status
2. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-context.md` — current product context
3. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/market-intelligence.md` — market data (if exists)
4. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/audience-intelligence.md` — audience data (if exists)

## Input Sources

The Strategist consumes intelligence from research agents:

| File | Producer | Content |
|------|----------|---------|
| `market-intelligence.md` | paw-ps-discovery | Market size, competition, trends |
| `audience-intelligence.md` | paw-ps-audience | User needs, segments, pain points |
| `product-context.md` | Any agent | Constraints, existing decisions |

## Output Files

| Output | Path | Purpose |
|--------|------|---------|
| Product decisions | `curated/product-decisions.md` | All product strategy decisions |
| Product context updates | `curated/product-context.md` | Updated context for other agents |
| Daily activity | `daily/YYYY-MM-DD.md` | Activity log |

## Product Decisions Structure

`curated/product-decisions.md` contains:

```markdown
# Product Decisions

## Status
- Current Phase: {phase}
- Last Updated: {date}
- Decision Count: {number}

## Product Brief
{Product shaping output}

## Scope Map
{Scope design output}

## Packaging Recommendation
{Packaging logic output}

## Execution Handoff
{Execution handoff output}

## Decision Log
| Date | Decision | Rationale | Owner |
|------|----------|-----------|-------|
| {date} | {decision} | {why} | Strategist |
```

## Activity Logging

Append to `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md`:

```markdown
## [Strategist] HH:MM - {Activity Type}
- **Input:** {what intelligence was consumed}
- **Decision:** {what was decided}
- **Output:** {what was produced}
- **Files:** {paths written}
```

## Memory Discipline

### Reading Rules
- Always read input files before making decisions
- Check `product-context.md` for existing constraints
- Verify intelligence freshness (date check)

### Writing Rules
- Append to `product-decisions.md`, don't overwrite
- Update `product-context.md` with new constraints
- Always log activity in daily file
- Never modify other agents' curated outputs

### Coordination
- Check `index.md` for active sessions from other agents
- Update `index.md` with current activity status
- Signal completion for dependent agents

## Handoff Context

When the Strategist completes decisions that feed into execution:

1. Update `product-context.md` with status change
2. Note which decisions are ready for execution
3. Update `index.md` if orchestration needed
4. Signal to Orchestrator if execution ready