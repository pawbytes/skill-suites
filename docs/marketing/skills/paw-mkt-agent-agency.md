# paw-mkt-agent-agency

## Overview

The coordinator skill. Start here when you want help choosing the right workflow or specialist. Routes to planning or execution based on what brand context and strategy already exist.

## When to use it

Use `/paw-mkt-agent-agency` when:
- you are starting marketing work for a brand
- you are not sure which specialist to use
- you want the suite to check brand context and SOSTAC status first
- you want coordinated implementation after planning
- you provided a URL or codebase and want the suite to orient itself

## Inputs to prepare

- brand name, slug, website URL, or codebase path
- business goal
- timeline and constraints
- any existing strategy or campaign context

## What the interaction looks like

The skill can start from three contexts:

| Starting point | What it does first |
|---|---|
| Live URL or profile | Audits the live presence |
| Local repo or codebase | Inspects the repo and uses it as context |
| Brand workspace | Reads `brand-context.md` and checks SOSTAC status |

After context is established:
1. Checks SOSTAC plan status
2. Routes to planning (`paw-mkt-sostac`) or execution
3. If strategy is complete, can spawn a specialist implementation team

## Deliverables

- routing decision
- recommended workflow
- specialist handoff guidance
- implementation team recommendation when strategy is complete

## Output locations

This skill mainly routes work into:
- `.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/`
- `.pawbytes/marketing-suites/brands/{brand-slug}/content/`
- `.pawbytes/marketing-suites/brands/{brand-slug}/analytics/`

## Reference files

The agency skill uses extracted reference files to stay lean:

- `references/frameworks/` — 10 frameworks indexed via `frameworks-index.csv`
- `references/team-spawning.md` — how to assemble and coordinate multi-specialist teams
- `references/progress-tracking.md` — how to track campaign and project status
- `references/directory-structure.md` — canonical brand workspace layout
- `references/martech-landscape.md` — tool selection guidance

## Related skills

- `paw-mkt-sostac`
- `paw-mkt-product-context`
- All specialist skills

## Sample prompts

```text
/paw-mkt-agent-agency
Help me figure out what marketing work we should do next.
```

```text
/paw-mkt-agent-agency
Work on Northstar AI. We have some brand context already, but I need to know whether to do SOSTAC planning first or go straight into execution.
```

```text
/paw-mkt-agent-agency
Our SOSTAC plan is complete. Assemble the right specialist workflow for implementation.
```

```text
/paw-mkt-agent-agency
Here's our product URL: example.com — audit it and tell me where our marketing is weakest.
```
