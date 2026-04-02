---
name: workflow
description: Staged workflow for SvelteKit + sql.js dashboard generation with LLM-built UI.
---

# Dashboard Builder Workflow

Workflow for generating and managing SvelteKit dashboards with LLM-built UI.

**Note:** Stage 1 (Discovery) happens on skill activation. Route to the appropriate stage based on user intent.

## Stage 1: Discovery (On Activation)

**Purpose:** Find all brand workspaces, check for existing dashboards, detect feature gaps, and present contextual options.

**When:** This runs automatically when the skill is invoked, before user interaction.

**Actions:**

1. Scan `{project-root}/.pawbytes/marketing-suites/brands/` for brand directories
2. For each brand directory, check for:
   - `sostac/README.md` — SOSTAC phase completion
   - `sostac/*.md` — Individual phase documents
   - `brand-context.md` — Brand positioning
   - `campaigns/` — Campaign folders and their contents
   - `channels/` — Channel-specific content
   - `content/` — Content calendar, email sequences, SEO research
   - `operations/` — Operational data (analytics, cro, retention, etc.)
   - `experiments/` — Growth experiments data
   - `revenue/` — Revenue and pricing data
   - `lifecycle/` — Customer lifecycle data
3. **Collect all markdown documents** — Recursively find all `.md` files across the brand workspace. For each file, record:
   - Relative path from brand root (used as slug)
   - Parent folder name (used as category: sostac, campaigns, content, channels, operations, root)
   - File title (first `# heading` in the file, or filename if no heading)
   - Full raw markdown content
   These get stored in a `documents` table during schema creation (Stage 2) and rendered read-only in the `/documents` route.
4. **Check for existing dashboards** — For each brand, check if `{brand-path}/dashboard/package.json` exists. If so, scan what routes exist (look for `src/routes/*/+page.svelte`).
5. **Detect feature gaps** — Compare existing routes against the Feature Registry:
   - `campaigns` → check `src/routes/campaigns/+page.svelte`
   - `content` → check `src/routes/content/+page.svelte`
   - `strategy` → check `src/routes/strategy/+page.svelte`
   - `metrics` → check `src/routes/metrics/+page.svelte`
   - `channels` → check `src/routes/channels/+page.svelte`
   - `documents` → check `src/routes/documents/+page.svelte`
   - `experiments` → check `src/routes/experiments/+page.svelte`
   - `revenue` → check `src/routes/revenue/+page.svelte`
   - `lifecycle` → check `src/routes/lifecycle/+page.svelte`
   - `operations` → check `src/routes/operations/+page.svelte`
   - `export-api` → check `src/routes/api/export/+server.ts`
6. Build discovery summary: brands found, data available, documents found, dashboard status, feature gaps
7. Present contextual options to user (see SKILL.md On Activation)

**Routing after user selects intent:**

| User Intent | Route To |
|-------------|----------|
| Run existing dashboard | **Stage 1a: Run** |
| Update/regenerate dashboard | **Stage 2** (export first, then regenerate) |
| Add missing/specific features | **Stage 4b: Feature Addition** |
| Generate new dashboard | **Stage 2** (full flow) |
| Full rebuild from scratch | **Stage 2** (delete existing first) |

---

## Stage 1a: Run Existing Dashboard

**Purpose:** Start an existing dashboard server for the user.

**Actions:**

1. Navigate to `{brand-path}/dashboard/`
2. Check if `node_modules/` exists — if not, run `npm install`
3. Start the dev server: `npm run dev` (or `npm run dev -- --port {port}` if port 5173 is busy)
4. Present the URL: `http://localhost:{port}`
5. Stay available for follow-up requests

**This is the fast path.** No generation, no schema design — just start the server.

**Progression:** Session continues. User may request changes, exports, or new features.

---

## Stage 2: Schema Design

**Purpose:** Design SQLite schema based on actual data structure.

**Actions:**

1. For each brand, deeply analyze discovered data:
   - Read campaign files to understand fields (name, type, status, dates, channels)
   - Read content files to understand structure (title, type, publish date, platform)
   - Read SOSTAC files to understand phase completion criteria
   - Identify relationships between data (campaign → channels, content → campaign)
2. Design SQLite tables:
   - `campaigns` — with fields matching actual campaign data
   - `content` — with types, status, dates, platform
   - `sostac_progress` — phase completion tracking with notes
   - `analytics_metrics` — KPI storage with date tracking
   - `channels` — channel performance data
   - `experiments` — growth experiments with ICE scores
   - `documents` — all discovered `.md` files with slug, category, title, and raw markdown content (read-only reference)
   - Additional tables as needed based on data
3. Plan seed data from discovered files — including inserting all collected markdown documents into the `documents` table

**Output:** Schema design (internal, used for code generation).

**Progression:** Proceed to Stage 3 when schema is designed.

---

## Stage 3: Project Scaffolding

**Purpose:** Generate the SvelteKit project structure.

**Actions:**

### 3a. Create Project Root

Generate `package.json` with dependencies:
- `@sveltejs/kit`, `@sveltejs/adapter-node` (^5), `svelte` (^5)
- `sql.js` (^1) — pure JS SQLite, no native deps
- `tailwindcss` (^4), `@tailwindcss/vite` (^4)
- `@sveltejs/vite-plugin-svelte` (^5) — must be ^5 for Vite 6 compatibility
- `typescript`, `vite` (^6)

### 3b. Generate Configuration Files

- `svelte.config.js` — adapter-node
- `vite.config.ts` — SvelteKit + Tailwind plugins (no `ssr.external` needed for sql.js)
- `postcss.config.js` — **Empty file** to prevent parent project's config inheritance
- `src/app.html` — base HTML shell with Google Fonts link
- `src/app.css` — `@import 'tailwindcss'` with `@theme {}` directive for design tokens

**Monorepo note:** The empty `postcss.config.js` is critical. Without it, parent project's PostCSS/Tailwind v3 config causes `@layer base` errors with Tailwind v4.

### 3c. Generate Database Layer

Single file: `src/lib/server/db.ts` — contains everything:
- sql.js initialization (async, with default export handling)
- Schema creation (CREATE TABLE IF NOT EXISTS)
- Seed data insertion
- Query helpers: `initDb()`, `getDb()`, `run()`, `get()`, `all()`, `exec()`, `saveDb()`

**No separate `schema.ts`.** Schema and seed data live in `db.ts` to prevent import confusion.

**Key constraint:** All database code lives in `$lib/server/` — SvelteKit enforces this boundary at build time.

**Progression:** Proceed to Stage 4 when project structure exists.

---

## Stage 4: Route & Component Generation

**Purpose:** Generate all SvelteKit routes and Svelte components.

**This is the core LLM generation stage.** Every component and route is built from scratch based on the schema and design guide. Read `./references/code-patterns.md` for SvelteKit patterns and `./references/design-guide.md` for aesthetic direction.

**Actions:**

### 4a. Generate Layout

- `+layout.server.ts` — Import `initDb` (only here, nowhere else), load brand name, nav items, summary stats
- `+layout.svelte` — Dashboard shell with sidebar navigation, responsive

### 4b. Generate Overview Page

- `+page.server.ts` — Load aggregate stats across all categories (import `all`/`get` from `$lib/server/db`)
- `+page.svelte` — Overview with varied card sizes, key metrics, quick actions

### 4c. Generate Category Routes

For each category with data (campaigns, content, strategy, metrics, channels, etc.):

- `+page.server.ts` — Import `all`/`run`/`get` from `$lib/server/db` + load function + form actions (create, update, delete)
- `+page.svelte` — List view with table, filters, add/edit modal, status badges

**Import rules:**
- `+layout.server.ts` → imports `initDb`, `all`, `get` from `$lib/server/db`
- `+page.server.ts` → imports `all`, `run`, `get` from `$lib/server/db` (NOT `initDb`, NOT from `schema`)
- `+server.ts` → imports `all`, `run`, `exec`, `saveDb` from `$lib/server/db`

Form actions pattern:
```
export const actions = {
  create: async ({ request }) => { ... },
  update: async ({ request }) => { ... },
  delete: async ({ request }) => { ... },
}
```

After each form action, SvelteKit automatically re-runs the load function — the UI updates reactively without manual fetch/refresh.

### 4d. Generate Documents Route

A read-only route that renders all discovered markdown files as formatted HTML.

**Index page** (`/documents`):
- `+page.server.ts` — Load all documents from `documents` table, grouped by category
- `+page.svelte` — Document index with category sections and links to individual docs

**Detail page** (`/documents/[slug]`):
- `+page.server.ts` — Load single document by slug, render markdown to HTML server-side using `marked`
- `+page.svelte` — Rendered HTML with prose-friendly typography (generous line height, heading hierarchy, code blocks, lists)

The markdown renderer (`$lib/utils/markdown.ts`) uses `marked` for server-side conversion. Rendered content uses a `MarkdownContent.svelte` component with Tailwind prose-like styling.

**No CRUD on documents.** They are seeded from discovery and regenerated on update. Users read them, not edit them.

### 4e. Generate Shared Components

In `src/lib/components/`:
- `Sidebar.svelte` — Navigation with active state
- `Modal.svelte` — Add/edit dialog
- `StatusBadge.svelte` — Semantic color badges
- `EmptyState.svelte` — Meaningful empty states with actions
- `MarkdownContent.svelte` — Prose-formatted markdown display (used by documents route)
- Additional components as needed

### 4f. Generate Export/Import API

- `src/routes/api/export/+server.ts` — GET dumps all tables to JSON, writes to `data/export/`
- `src/routes/api/import/+server.ts` — POST reads JSON from `data/export/`, upserts into SQLite

### 4g. Generate .gitignore

```
node_modules/
.svelte-kit/
data/dashboard.db
build/
```

**Progression:** Proceed to Stage 5 when all routes and components are generated.

---

## Stage 4b: Feature Addition

**Purpose:** Add one or more features to an existing dashboard without full regeneration.

**When:** User selects "Add missing features" or "Add specific features" from the options.

**Prerequisites:** Existing dashboard with `package.json` and `src/lib/server/db.ts`.

**Actions:**

### 4b-1. Analyze Request

1. Parse the list of features to add (from Feature Registry)
2. For each feature, verify it doesn't already exist (check route presence)
3. Skip any that already exist, inform user

### 4b-2. Check Data Availability

For each feature, check if corresponding data exists in the brand workspace:

| Feature | Data Location | If Missing |
|---------|---------------|------------|
| `experiments` | `experiments/` folder | Offer to create template structure |
| `revenue` | `revenue/` folder | Offer to create template structure |
| `lifecycle` | `lifecycle/` folder | Offer to create template structure |
| `operations` | `operations/` folder | Use existing if any |
| `metrics` | `operations/analytics/` | Use existing if any |

If user declines template creation, skip that feature.

### 4b-3. Update Schema

1. Read existing `src/lib/server/db.ts`
2. Add new tables for selected features:
   - `experiments` → `experiments` table (id, name, hypothesis, ice_score, status, results)
   - `revenue` → `revenue` table (id, metric_type, value, date, notes)
   - `lifecycle` → `lifecycle_metrics` table (id, cohort, churn_rate, retention_rate, ltv)
   - `operations` → `operations` table (id, item_type, status, assignee, due_date)
3. Add seed data from discovered files or create placeholder records
4. Ensure backward compatibility — don't modify existing tables

### 4b-4. Generate Routes

For each feature, generate:
- `src/routes/{feature}/+page.server.ts` — Load + form actions
- `src/routes/{feature}/+page.svelte` — List view with table/filters

Follow the same patterns as Stage 4c.

### 4b-5. Update Navigation

1. Read `src/routes/+layout.svelte`
2. Add new nav items to sidebar for each new feature
3. Maintain existing nav order, append new items

### 4b-6. Run Migration (if needed)

If schema was updated:
1. Export existing data via the export endpoint
2. Restart the dev server to pick up schema changes
3. Data persists in `dashboard.db` — no re-seed needed for existing tables

### 4b-7. Present Summary

```
## Features Added

**Brand:** {brand}

Added:
  • experiments — Growth experiments with ICE scores
  • revenue — MRR, ARPU, pricing tracker

Schema updated: 2 new tables
Routes added: /experiments, /revenue

To verify:
  npm run dev
  Open http://localhost:5173
```

**Progression:** Session continues. User may run dashboard, add more features, or export data.

---

## Stage 5: Summary & Instructions

**Purpose:** Present what was built and how to use it.

**Actions:**

1. Summarize:
   - Brands discovered
   - Schema designed (tables, fields)
   - Routes generated
   - Data seeded from existing files
2. Provide run instructions:
   ```
   cd .pawbytes/marketing-suites/brands/{brand-slug}/dashboard
   npm install
   npm run dev
   # Open http://localhost:5173
   ```
3. For multiple dashboards, use different ports:
   ```
   npm run dev -- --port 5180
   ```
4. Explain export/import for git commits:
   - Visit `/api/export` or click Export button → writes JSON to `data/export/`
   - Commit JSON files to git (`.db` file is gitignored)
   - After clone, visit `/api/import` or click Import → loads JSON into SQLite
5. Generate launcher page if multiple brands

**Output Contract:**

```
## Dashboard Generation Complete

**Brand:** nadiapen
**Schema:** 5 tables (campaigns, content, sostac_progress, channels, analytics_metrics)

**Routes generated:**
- / — Overview with summary stats
- /campaigns — Campaign tracker (3 seeded)
- /content — Content pipeline (14 items from calendar)
- /strategy — SOSTAC progress (1/6 phases complete)
- /channels — Channel performance
- /metrics — Analytics metrics
- /documents — Read-only markdown documents (12 files indexed)
- /documents/{slug} — Individual document view
- /api/export — JSON export
- /api/import — JSON import

**To run:**
cd .pawbytes/marketing-suites/brands/nadiapen/dashboard
npm install
npm run dev

Open http://localhost:5173
```

---

## Recovery Logic

If the workflow is interrupted or resumed:

1. Check for existing dashboard files in `{brand-path}/dashboard/`
2. If `package.json` exists:
   - Check if `data/dashboard.db` exists (has been run)
   - Check if `data/export/*.json` exists (has been exported)
3. Ask user which approach:
   - **Preserve data** — Keep SQLite, regenerate UI only (re-run Stage 4)
   - **Full regeneration** — Delete and recreate everything
   - **Cancel** — Keep existing dashboard unchanged

---

## Data Migration

When regenerating a dashboard that already has data:

1. **Export first** — Read existing SQLite data via export endpoint
2. **Generate new schema** — If data structure changed
3. **Import data** — Map old schema to new schema
4. **Or preserve** — Keep existing `dashboard.db`, only regenerate routes/components

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| **Changes not reflected** | Stop server → delete `.svelte-kit` folder → restart `npm run dev` |
| **`@layer base` PostCSS errors** | Ensure empty `postcss.config.js` exists in dashboard root |
| **Port in use** | Use `npm run dev -- --port 5180` |
| **Database not persisting** | Ensure `saveDb()` is called after writes (use `run()`/`exec()` helpers) |
| **Import errors on page routes** | Only `+layout.server.ts` imports `initDb`. Pages import `all`/`run`/`get` directly. |