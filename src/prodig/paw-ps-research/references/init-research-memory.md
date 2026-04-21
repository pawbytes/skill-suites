# Initialize Research Memory

## Purpose

First-run setup for research memory when `market-intelligence.md` doesn't exist yet.

## When to Run

Execute this process when:
- First activation of the Research Agent
- `market-intelligence.md` doesn't exist in the curated directory
- Research memory needs to be reset or reinitialized

## Initialization Steps

### 1. Verify Directory Structure

Ensure the sidecar directory structure exists:

```text
.pawbytes/prodig-suites/memory/paw-ps-sidecar/
├── index.md
├── daily/
└── curated/
```

If missing, run the full sidecar initialization first (see `paw-ps-agent-product-builder/references/init-sidecar.md`).

### 2. Create market-intelligence.md

Create the file at `curated/market-intelligence.md`:

```markdown
# Market Intelligence

**Last Updated:** {YYYY-MM-DD}
**Status:** Initialized (no research yet)

## Purpose

This file holds synthesized market research that informs product decisions. Research is stored with confidence levels and clearly separated evidence from assumptions.

## Research Areas

### Competitor Landscape
*No competitor research yet.*

### Demand Signals
*No demand signal research yet.*

### Market Gaps & Opportunities
*No gap analysis yet.*

### Market Sizing
*No market sizing research yet.*

## Confidence Framework

| Level | Criteria | Label |
|-------|----------|-------|
| High | Multiple independent sources, consistent data | `[HIGH]` |
| Medium | Limited sources, some variance in data | `[MED]` |
| Low | Single source, inferred, or proxy data | `[LOW]` |
| Assumption | No direct evidence, logical inference | `[ASSUMED]` |

## Recent Findings

*No findings recorded yet. Run competitor analysis, demand signal analysis, or gap identification to populate this section.*

## Sources Log

| Date | Research Type | Sources | Confidence |
|------|---------------|---------|------------|
| - | - | - | - |

## How to Add Research

1. Run research capability (competitor analysis, demand signals, etc.)
2. Findings are synthesized with confidence levels
3. This file is updated with new sections
4. Daily log records the research activity

## Getting Started

Tell the Research Agent:
- "Research competitors in [market]"
- "Analyze demand signals for [product idea]"
- "Identify gaps in [market space]"
- "What's the competitive landscape for [topic]?"
```

### 3. Update Sidecar Index

Update `curated-files-status` in `index.md`:

```markdown
## Curated Files Status

| File | Status | Description |
|------|--------|-------------|
| product-context.md | [status] | [description] |
| market-intelligence.md | Created | Market research synthesis |
| audience-intelligence.md | [status] | [description] |
```

### 4. Log Initialization

Append to the daily log at `daily/{YYYY-MM-DD}.md`:

```markdown
## [Research] HH:MM - Memory Initialized
- **Action:** Created market-intelligence.md
- **Reason:** First activation or missing file
- **Next:** Ready for research requests
```

## Verification

After initialization, verify:

- [ ] `curated/market-intelligence.md` exists and has content
- [ ] Sidecar index has been updated
- [ ] Daily log has been updated
- [ ] File is ready to receive research findings

## Post-Initialization

After setup, the Research Agent can:

1. Load the newly created `market-intelligence.md`
2. Accept research requests
3. Begin populating research findings with confidence levels

```markdown
Research memory initialized. Ready to gather market intelligence.

What would you like me to research?
- Competitor analysis
- Demand signal analysis
- Gap identification
- Market sizing
```