# Save Memory Protocol

## Purpose

Define how the Software Executor writes to shared memory to maintain continuity across sessions and enable other agents to build on its work.

## Memory Structure

```
.pawbytes/prodig-suites/memory/paw-ps-sidecar/
├── index.md                      # Orientation file
├── daily/
│   └── YYYY-MM-DD.md            # Session logs
├── curated/
│   ├── product-context.md        # Current active product
│   ├── market-intelligence.md    # Research synthesis
│   ├── audience-intelligence.md  # Customer understanding
│   ├── product-decisions.md      # Decision log
│   ├── output-standards.md       # Quality bar
│   └── product-types/
│       └── software-products.md  # Software product guidance
└── artifacts/
    └── {product-slug}/           # Product artifacts
        ├── feature-spec.md
        ├── user-flows.md
        ├── mvp-definition.md
        ├── prd-lite.md
        ├── technical-context.md
        └── execution-checklist.md
```

## Write Triggers

Always update memory after:

1. **Creating artifacts** — Write to artifacts/{product-slug}/
2. **Refining product-type guidance** — Update curated/product-types/software-products.md
3. **Completing a session** — Append to daily log
4. **Discovering reusable patterns** — Update product-type guidance

## Write Operations

### Artifacts

Write artifact files to the product workspace:

```markdown
# [Artifact Type]: [Product Name]

**Created**: [YYYY-MM-DD HH:MM]
**By**: Software Executor
**Inputs**: [List of input files used]

---

[Artifact content]
```

### Daily Log

Append session activity:

```markdown
## [HH:MM] Software Executor

**Task**: [Capability type - feature definition, user flows, MVP, PRD-lite]
**For**: [Product name]
**Inputs**: [What context was loaded]
**Outputs**: [Artifacts created]
**Decisions**: [Any notable decisions made]
**Next**: [Recommended next steps]
```

### Product-Type Guidance

When refining software product patterns:

```markdown
# Software Products Guidance

## Overview
[Updated description of software product patterns]

## Feature Definition Patterns
[Patterns discovered/refined]

## MVP Scoping Patterns
[Patterns discovered/refined]

## Common Technical Decisions
[Patterns discovered/refined]

## Updated: [YYYY-MM-DD]
```

## Read Access (What We Read)

- `curated/product-context.md` — Product context
- `curated/audience-intelligence.md` — Audience insights
- `curated/market-intelligence.md` — Market intelligence
- `curated/output-standards.md` — Quality standards
- `curated/product-types/software-products.md` — Product-type guidance
- `daily/YYYY-MM-DD.md` — Recent activity

## Write Access (What We Write)

- `artifacts/{product-slug}/*.md` — Product artifacts
- `daily/YYYY-MM-DD.md` — Session logs
- `curated/product-types/software-products.md` — Refined guidance

## Deny Zones

- Other product workspaces (not in scope)
- `curated/product-context.md` (read-only for executors)
- `curated/audience-intelligence.md` (read-only for executors)
- `curated/market-intelligence.md` (read-only for executors)

## Example Daily Log Entry

```markdown
## 14:30 Software Executor

**Task**: Feature Definition + User Flows
**For**: Task Automation Platform
**Inputs**: product-context.md, audience-intelligence.md, feature-spec.md (partial)
**Outputs**:
  - artifacts/task-automation-platform/feature-spec.md (completed)
  - artifacts/task-automation-platform/user-flows.md (created)
**Decisions**:
  - Excluded webhooks from MVP (deferred to v1.1)
  - Added email trigger as P1 (was P2)
**Next**: MVP scoping when features approved
```

## Coordination with Other Agents

The Software Executor outputs feed into:

| Artifact | Used By | Purpose |
|----------|---------|---------|
| feature-spec.md | paw-ps-agent-product-builder | Progress tracking |
| mvp-definition.md | paw-ps-strategist | Pricing/packaging |
| prd-lite.md | Development team | Build handoff |
| technical-context.md | paw-ps-architect | Architecture refinement |