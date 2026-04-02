# Shared Skill Patterns

These patterns are referenced by all marketing specialist skills. Read them as part of your operating instructions.

## Starting Context Router

Choose the starting mode before doing the work. Brand workspace context is preferred, but do not block progress if the user provides a real codebase or live URL.

### Context A — Blank Page / Strategy Work
Use when the user needs strategy, planning, or a fresh roadmap. Read brand and SOSTAC context first when available, then align recommendations to audience, objections, and business goals.

### Context B — Existing Local Codebase / Implementation Work
Use when the user wants changes made or specified in an existing repository, site, product, or app. Before proposing changes, deeply research the codebase: inspect the stack, architecture, relevant files, dependencies, and existing patterns. Match existing conventions before changing anything.

### Context C — Live Website URL Audit
Use when the user provides a public URL for review. Audit the live experience first. If brand files are missing, use the live page and visible structure as the working source of truth.

## Pre-Flight: Read Strategic Context

Before any specialist work, read these files in order when available:

1. `./.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md` — brand identity, audience, USP
2. `./.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md` — deep positioning, customer language, objections
3. `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/03-strategy.md` — target segments, positioning
4. `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/04-tactics.md` — channel plan, priorities

If brand files are missing but a codebase or live URL is available, continue with that as the working source of truth rather than blocking progress.

## agent-browser Setup

Before running browser-based research, check if `agent-browser` is available (`agent-browser --version`). If the command is not found, install it:

```bash
npm install -g agent-browser && npx playwright install chromium
```

If installation fails, use `WebFetch` and `WebSearch` tools as alternatives for all research tasks.

## Reference Lookup Protocol

All skills use this pattern to avoid loading all framework files into context:

1. Read `./references/frameworks-index.csv` — lightweight index (10–40 rows)
2. Match the user's situation to the `best_for` column
3. Read ONLY the matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files

General references (shared-patterns.md, best-practices.md) are read directly — not indexed.
