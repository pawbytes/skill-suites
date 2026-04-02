# Memory Management

## Purpose

Define how Prodig Suites uses shared memory to maintain context across sessions and agents.

## Memory Architecture

Prodig Suites uses a **single shared module sidecar** because all agents benefit from shared visibility into the evolving product, market, customer, and output standards.

```
.pawbytes/prodig-suites/memory/paw-ps-sidecar/
├── index.md                      # Orientation - READ FIRST
├── daily/
│   └── YYYY-MM-DD.md            # Append-only session logs
└── curated/
    ├── product-context.md        # Current active product(s)
    ├── market-intelligence.md    # Research synthesis
    ├── audience-intelligence.md  # Customer understanding
    ├── product-decisions.md      # Decision log
    ├── output-standards.md       # Quality bar and formats
    └── product-types/
        ├── knowledge-products.md
        ├── template-products.md
        ├── software-products.md
        └── service-products.md
```

## Memory Contract

| File | Purpose | Read By | Written By | Key Contents |
|------|---------|---------|------------|--------------|
| `index.md` | Orientation and recent activity | All agents | Orchestrator | Active products, recent updates, next actions |
| `daily/*.md` | Session log | All agents as needed | All agents | Timestamps, actions, findings, handoffs |
| `curated/product-context.md` | Active product definition | All agents | Orchestrator, Strategist | Product type, stage, goals, constraints |
| `curated/market-intelligence.md` | Market research synthesis | Orchestrator, Strategist | Research agent | Competitors, gaps, demand signals |
| `curated/audience-intelligence.md` | Customer insights | Orchestrator, Strategist, Executors | Audience agent | Personas, pains, desired outcomes |
| `curated/product-decisions.md` | Decision log | Orchestrator, Strategist | Orchestrator, Strategist | Choices, rationale, rejected options |
| `curated/output-standards.md` | Quality criteria | Executors, QC workflow | Orchestrator, Strategist | Production-ready definition, formats |
| `curated/product-types/*.md` | Product-family guidance | Relevant executor | Executors, Strategist | Best practices per product type |

## Reading Protocol

### On Activation

Every agent reads in this order:

1. **index.md** — Always read first for orientation
2. **Relevant curated files** — Based on agent's purpose:
   - Research agent → product-context.md, market-intelligence.md
   - Audience agent → product-context.md, market-intelligence.md (if exists)
   - Strategist → all curated files
   - Executors → product-context.md, audience-intelligence.md, output-standards.md, relevant product-type file

### Progressive Loading

Never bulk-read all files. Load based on need:

```markdown
## Agent Activation Sequence

1. READ index.md (always)
2. READ product-context.md (if working on active product)
3. READ relevant curated files based on task
4. SKIP files not relevant to current task
```

## Writing Protocol

### Daily Log

All agents append to daily log:

```markdown
## YYYY-MM-DD

### HH:MM - {agent-name}

**Action:** {what was done}

**Context:** {relevant context}

**Outputs:** {what was produced}

**Next:** {recommended next step}
```

**Rules:**
- Append-only, never modify past entries
- Include timestamp and agent name
- Keep entries concise but complete
- Note any handoffs or routing decisions

### Curated Files

Curated files are updated when:
- Significant new information is discovered
- Decisions are made that affect future work
- Stage transitions occur
- Quality standards evolve

**Update format:**
```markdown
<!-- When updating, add note at top -->
**Updated:** YYYY-MM-DD by {agent-name}
**Change:** {brief description of update}

{Updated content...}
```

### Never Overwrite

Curated files accumulate context:
- Append new findings, don't replace
- Note when information is superseded
- Keep decision history visible

## Memory File Templates

### index.md

```markdown
# Prodig Suites Memory Index

**Last Updated:** YYYY-MM-DD

## Active Products

| Product | Type | Stage | Last Active |
|---------|------|-------|-------------|
| {name} | {type} | {stage} | {date} |

## Recent Activity

### YYYY-MM-DD
- {agent} completed {action} for {product}
- {agent} discovered {finding}
- Stage transition: {old} → {new} for {product}

## Curated Files Status

| File | Last Updated | Status |
|------|--------------|--------|
| product-context.md | YYYY-MM-DD | Active |
| market-intelligence.md | YYYY-MM-DD | Research complete |
| audience-intelligence.md | - | Pending |
| product-decisions.md | YYYY-MM-DD | 3 decisions logged |
| output-standards.md | - | Not yet defined |

## Next Actions

- {Product 1}: {recommended next step}
- {Product 2}: {recommended next step}
```

### product-context.md

```markdown
# Product Context

**Product:** {name}
**Slug:** {slug}
**Type:** {knowledge|template|software|service}
**Status:** {discovery|research|audience|strategy|execution|packaging|readiness}
**Created:** YYYY-MM-DD
**Updated:** YYYY-MM-DD

## Concept

{Product description}

## Goals

- Goal 1
- Goal 2

## Constraints

- Constraint 1
- Constraint 2

## Target Audience

{From audience-intelligence.md or placeholder}

## Stage Progress

| Stage | Status | Key Outputs |
|-------|--------|-------------|
| Discovery | complete | {outputs} |
| Research | complete | {outputs} |
| Audience | in_progress | - |
| Strategy | pending | - |
| Execution | pending | - |
| Packaging | pending | - |
| Readiness | pending | - |
```

### product-decisions.md

```markdown
# Product Decisions

Decision log for {product-name}. Records key choices, rationale, and rejected alternatives.

---

## Decision: {Decision Title}

**Date:** YYYY-MM-DD
**Made by:** {agent or user}

### Context
{Why this decision was needed}

### Options Considered
1. **{Option A}** — {description}
2. **{Option B}** — {description}
3. **{Option C}** — {description}

### Decision
**Chosen:** {Option X}

### Rationale
{Why this option was selected}

### Trade-offs
- Gain: {what we get}
- Loss: {what we give up}

### Rejected Options
- {Option Y}: {reason for rejection}

---
```

## Cross-Agent Memory Patterns

### Handoff via Memory

When one agent hands off to another:

1. Source agent writes findings to relevant curated file
2. Source agent logs the handoff in daily file
3. Target agent reads curated file + daily log on activation

### Avoiding Redundancy

Before doing work:
1. Check if relevant curated file exists
2. Check daily log for recent related activity
3. Don't re-ask questions already answered in memory

### Memory Hygiene

Periodic cleanup (can be triggered by orchestrator):
- Archive old daily logs (keep last 30 days visible)
- Consolidate daily findings into curated files
- Update index.md with current state
- Remove stale products to archive

## Memory Recovery

If memory becomes inconsistent:

1. **Rebuild from artifacts** — Check product workspaces for ground truth
2. **Rebuild from daily logs** — Reconstruct recent history
3. **Ask user** — Clarify current state if needed
4. **Reinitialize** — Last resort: start fresh with current session