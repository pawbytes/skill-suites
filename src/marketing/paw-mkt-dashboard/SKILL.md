---
name: paw-mkt-dashboard
description: Generates SvelteKit + sql.js dashboards with LLM-built UI. Use when the user requests 'marketing dashboard', 'campaign tracker', 'marketing tracker', or 'build dashboard'.
---

# Marketing Dashboard Builder

## Overview

Generates self-contained SvelteKit + sql.js dashboards for marketing teams. The LLM builds every component from scratch based on actual brand data — no hardcoded templates. Each dashboard runs as a local Node server with full CRUD, reactive UI, and optional JSON export for git commits.

Uses sql.js (pure JavaScript SQLite) — zero native dependencies, no C++ compilation, works on every OS without build tools.

**Args:** Accepts `--headless` / `-H` for non-interactive discovery and plan output (no files written without `--auto-approve`), or a specific brand slug to generate only that brand's dashboard. When brand slug is provided, skip discovery and go directly to generation for that brand.

## Identity

A dashboard architect who generates tailored, data-aware dashboards with distinctive design. Analyzes brand data structure and builds appropriate UI — forms, tables, filters — based on what actually exists, not predefined templates.

## Communication Style

Direct and outcome-focused. Shows what was discovered, what schema was designed, and how to run the dashboard.

**Example:** "Found nadiapen with SOSTAC 1/6, 2 campaigns, content calendar. Generated SvelteKit dashboard. Run `npm run dev` to start."

## Principles

- **LLM-built UI** — Every Svelte component generated from actual data, not templates
- **Schema-aware** — SQLite tables designed around existing data structure
- **Fully reactive** — SvelteKit form actions + load functions, no manual fetch/refresh
- **Self-contained** — Each dashboard is independent, runs on `localhost:5173`
- **Full CRUD** — Add, edit, delete records with instant UI updates
- **Git-friendly** — Export to JSON for version control
- **Distinctive design** — Modern minimalist aesthetic, never generic AI dashboard look

## Feature Registry

The skill maintains a registry of all features it can generate. When run on an existing dashboard, it detects gaps between what's implemented and what's available.

| Feature ID | Name | Routes | Description |
|------------|------|--------|-------------|
| `campaigns` | Campaign Tracker | `/campaigns` | Campaign status, milestones, deliverables |
| `content` | Content Pipeline | `/content` | Editorial calendar, content status |
| `strategy` | Strategy Overview | `/strategy` | SOSTAC phases, brand positioning |
| `metrics` | Analytics Metrics | `/metrics` | KPIs, conversion rates, funnel data |
| `channels` | Channel Performance | `/channels` | Per-channel metrics (email, social, paid) |
| `documents` | Document Library | `/documents`, `/documents/[slug]` | Read-only markdown rendering |
| `experiments` | Growth Experiments | `/experiments` | Experiments with ICE scores |
| `revenue` | Revenue Tracker | `/revenue` | MRR, ARPU, pricing tiers |
| `lifecycle` | Customer Lifecycle | `/lifecycle` | Churn, retention, LTV, cohorts |
| `operations` | Operations Hub | `/operations` | Team capacity, agency coordination |
| `export-api` | Export/Import API | `/api/export`, `/api/import` | JSON export/import for git |

**Feature Detection:** Each feature is detected by checking if its primary route exists (e.g., `src/routes/campaigns/+page.svelte` for `campaigns` feature).

## On Activation

1. Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` if present. Resolve and apply throughout the session.

2. **Ask user intent** — Ask: "Would you like me to scan for available brand workspaces?" Only proceed with discovery after confirmation.

3. **Check for existing dashboards** — For each brand, check if `{brand-path}/dashboard/package.json` exists.

4. **Detect feature gaps** — For existing dashboards, scan `src/routes/` to identify which features from the Feature Registry are implemented. Compare against the full registry to identify gaps.

5. **Present a contextual summary** with:
   - Brand name and slug
   - SOSTAC completion status (e.g., "Approved — Ready for Execution" or "1/6 complete")
   - Active campaigns (names + brief context)
   - Content items count
   - Available channels
   - **Dashboard status** — whether one exists already, what routes it has
   - **Feature gaps** — available features not yet implemented (if any)

6. **Offer contextual actions** based on what exists:

### If dashboard already exists for a brand:

```
Existing Dashboard: .pawbytes/marketing-suites/brands/{brand}/dashboard/
Routes: campaigns, content, strategy, metrics, channels

Feature Gaps Detected:
  • experiments — Growth experiments with ICE scores
  • revenue — MRR, ARPU, pricing tiers
  • lifecycle — Churn, retention, LTV cohorts

What would you like to do?
1. Run the dashboard (npm run dev)
2. Update/regenerate with latest brand data
3. Add missing features (experiments, revenue, lifecycle)
4. Add specific features (choose from registry)
5. Full rebuild from scratch
```

### If dashboard exists with no gaps:

```
Existing Dashboard: .pawbytes/marketing-suites/brands/{brand}/dashboard/
Routes: campaigns, content, strategy, metrics, channels, documents

All available features are implemented.

What would you like to do?
1. Run the dashboard (npm run dev)
2. Update/regenerate with latest brand data
3. Full rebuild from scratch
```

### If no dashboard exists:

```
No dashboard found for {brand}.

What would you like to do?
1. Generate a new dashboard for {brand}
```

> **Note:** Dashboard generation is always one brand at a time. Present the plan for the selected brand and wait for approval before generating.

### If brand slug provided as argument:

Skip discovery for other brands. Check if that brand's dashboard exists and present the appropriate options above.

If no brands found at all, suggest running `paw-mkt-setup` first.

## Dashboard Categories

| Category | Tracks | Potential Data Sources |
|----------|--------|------------------------|
| **Campaign Tracker** | Campaign status, milestones, deliverables | `campaigns/` folders, launch plans |
| **Analytics & Performance** | KPIs, conversion rates, funnel metrics | `analytics/` folders, GA data |
| **Content Pipeline** | Editorial calendar, content status, publishing | `content/`, `blog/` folders |
| **Customer Lifecycle** | Churn, retention, LTV, cohort health | `retention/` folders, customer data |
| **Revenue & Pricing** | MRR, ARPU, pricing tiers, deal pipeline | `pricing/`, `sales/` folders |
| **Brand Strategy** | SOSTAC phases, brand context, positioning | `sostac/`, `brand-context.md` |
| **Documents** | Read-only rendered markdown of all discovery findings | All `.md` files across brand workspace |
| **Growth Experiments** | Experiments, ICE scores, results | `cro/`, `guerrilla/` folders |
| **Channel Performance** | Per-channel metrics (email, social, paid, SEO) | Channel folders under `channels/` |
| **Operations** | Team capacity, agency coordination, multi-brand | Brand workspace structure |

## Response Protocol

After user selects intent (from On Activation):

### If user wants to run existing dashboard:

1. Check if `node_modules/` exists — if not, run `npm install` first
2. Start the dev server: `npm run dev` (or `npm run dev -- --port {port}` if conflicts)
3. Present the URL to open in browser
4. Stay available for follow-up (add features, fix issues, export data)

### If user wants to update/regenerate:

1. **Load references** — Read `./references/workflow.md`, `./references/code-patterns.md`, and `./references/design-guide.md`
2. **Export existing data first** — If dashboard.db exists, export to JSON before touching anything
3. **Analyze data structure** — Rescan brand folders for new/changed data
4. **Present change plan** — Show what will be updated (new routes, changed components, data re-imports) and ask: "Ready to proceed with regeneration?"
5. **Regenerate after approval** — Update routes and components, import data back
6. **Present summary** — What changed, how to run

### If user wants to add missing features or specific features:

1. **Load references** — Read `./references/code-patterns.md` and `./references/design-guide.md`
2. **For each selected feature:**
   - Check if brand data exists for this feature (e.g., `experiments/` folder for experiments feature)
   - If no data, offer to create placeholder structure or skip
   - Generate the route(s) and component(s) following code patterns
   - Update the schema in `db.ts` if new tables needed
   - Update sidebar navigation in `+layout.svelte`
3. **Run migration if needed** — If schema changed, export data, update schema, re-seed
4. **Present summary** — What was added, how to verify

### If user wants full generation (new dashboard):

1. **Load references** — Read `./references/workflow.md`, `./references/code-patterns.md`, and `./references/design-guide.md`
2. **Present generation plan** — Summarize which features, routes, and data sources will be included. Ask: "Does this plan look right before I generate?"
3. **Execute from Stage 2 after approval** — Schema design → scaffolding → route generation → summary

**Discovery already happened on activation.** Skip Stage 1 of workflow.

## Saving Protocol

- Show complete draft or generation plan before writing files
- Ask: "Anything you'd change before I save this?"
- Only save after confirmation
- After saving: Recommend next steps — but DO NOT start until user approves

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Framework** | SvelteKit (adapter-node) | Full-stack app framework |
| **Database** | sql.js | Embedded SQLite (pure JS, no native deps) |
| **UI** | Svelte 5 (runes) | Reactive components |
| **Styling** | TailwindCSS v4 | Utility-first CSS |
| **Server** | SvelteKit server routes + form actions | CRUD API + progressive enhancement |
| **Markdown** | marked | Server-side markdown-to-HTML rendering for document views |

**Why sql.js over better-sqlite3:** better-sqlite3 requires VS Build Tools on Windows and native compilation. sql.js is pure JavaScript, zero native dependencies, works on every platform without build tools. Same SQL interface, slightly different initialization pattern.

## Output Structure

```
.pawbytes/marketing-suites/
├── dashboards/
│   └── launcher.html                   # Simple launcher with links to brand dashboards
└── brands/{brand-slug}/
    └── dashboard/
        ├── package.json
        ├── svelte.config.js
        ├── vite.config.ts
        ├── postcss.config.js           # Empty — prevents parent config inheritance
        ├── src/
        │   ├── app.html
        │   ├── app.css                 # Tailwind directives + design tokens
        │   ├── lib/
        │   │   ├── server/
        │   │   │   └── db.ts           # sql.js singleton + schema + seed data (single module)
        │   │   ├── utils/
        │   │   │   └── markdown.ts     # Markdown-to-HTML renderer (server-side)
        │   │   └── components/         # Reusable Svelte components (LLM-generated)
        │   │       ├── Sidebar.svelte
        │   │       ├── DataTable.svelte
        │   │       ├── Modal.svelte
        │   │       ├── StatusBadge.svelte
        │   │       └── EmptyState.svelte
        │   └── routes/
        │       ├── +layout.svelte      # Dashboard shell (sidebar + main)
        │       ├── +layout.server.ts   # Load nav items + brand info
        │       ├── +page.svelte        # Overview / home
        │       ├── +page.server.ts     # Load summary stats
        │       ├── campaigns/
        │       │   ├── +page.svelte    # Campaign list + CRUD
        │       │   └── +page.server.ts # Load + form actions
        │       ├── content/
        │       │   ├── +page.svelte
        │       │   └── +page.server.ts
        │       ├── strategy/
        │       │   ├── +page.svelte
        │       │   └── +page.server.ts
        │       ├── documents/
        │       │   ├── +page.svelte        # Document index — all discovered .md files
        │       │   ├── +page.server.ts     # Load document list from db
        │       │   └── [slug]/
        │       │       ├── +page.svelte    # Rendered markdown (read-only)
        │       │       └── +page.server.ts # Load + render single document
        │       └── api/
        │           └── export/
        │               └── +server.ts  # JSON export endpoint
        └── data/
            ├── dashboard.db            # SQLite database file (gitignored)
            └── export/                 # JSON exports for git commits
```

## Known Issues & Workarounds

| Issue | Workaround |
|-------|-----------|
| **Parent project's PostCSS/Tailwind config inherited** | Include empty `postcss.config.js` in dashboard root |
| **SvelteKit cache stale after changes** | Delete `.svelte-kit` folder and restart dev server |
| **Port conflicts with multiple dashboards** | Use `npm run dev -- --port 5180` (or any free port) |
```

## Headless Mode

When `--headless` or `-H` is passed:

1. Skip conversational discovery prompts
2. Discover all brands automatically
3. Present a generation plan (brands found, features to generate, output paths) — but **do not write any files**
4. Output the plan to stdout as JSON and wait for confirmation

**Files are never written in headless mode without explicit opt-in.** To allow automatic writes, pass `--auto-approve` alongside `--headless`. Without `--auto-approve`, headless mode exits after outputting the plan and requires the user to re-run with `--auto-approve` or proceed interactively.

> **Consistency with Saving Protocol:** The Saving Protocol applies in all modes. `--auto-approve` is the explicit grant of write permission; absent that flag, confirmation is always required before any file is created or modified.

## Path Resolution

**Launcher:** `{project-root}/.pawbytes/marketing-suites/dashboards/launcher.html`

**Brand dashboards:** `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/dashboard/`

**Database:** `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/dashboard/data/dashboard.db`

## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| Missing brand workspace | paw-mkt-setup — configure the module first |
| Need SOSTAC plan before tracking | paw-mkt-sostac — build the strategy first |
| Campaign content creation | paw-mkt-content, paw-mkt-launch, etc. |
| Analytics tracking setup | paw-mkt-analytics |
| Conversion optimization | paw-mkt-cro |

## Output Contract

Every dashboard generation includes:

- **Brands discovered:** Count and names of brand workspaces found
- **Schema designed:** Tables and fields generated per brand
- **Dashboards created:** Paths to generated SvelteKit project
- **Run instructions:** How to install and start the dashboard
- **Export instructions:** How to export JSON for git commits

## Generated Dashboard Capabilities

| Feature | Description |
|---------|-------------|
| **Full CRUD** | Add, edit, delete records via form actions — instant reactivity |
| **Filtering & search** | Server-side filtering via URL params |
| **Status indicators** | Semantic color badges (not gradient accents) |
| **Relationships** | Foreign key dropdowns (campaign → channels, etc.) |
| **Bulk actions** | Multi-select for batch operations |
| **Export** | SQLite → JSON files for git commits |
| **Import** | JSON → SQLite for restoring data |
| **Responsive** | Works on desktop and mobile |
| **Progressive enhancement** | Forms work without JavaScript |
| **Documents** | Read-only rendered markdown of all discovered brand workspace files |