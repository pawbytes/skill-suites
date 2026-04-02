---
name: code-patterns
description: SvelteKit + sql.js patterns for LLM code generation. Svelte 5 runes, form actions, server routes.
---

# Dashboard Code Patterns

Reference patterns for generating SvelteKit + sql.js dashboards. Adapt to match actual brand data.

## Project Configuration

### package.json

```json
{
  "name": "{brand-slug}-dashboard",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite dev",
    "build": "vite build",
    "preview": "vite preview",
    "start": "node build"
  },
  "devDependencies": {
    "@sveltejs/adapter-node": "^5",
    "@sveltejs/kit": "^2",
    "@sveltejs/vite-plugin-svelte": "^5",
    "@tailwindcss/vite": "^4",
    "svelte": "^5",
    "tailwindcss": "^4",
    "typescript": "^5",
    "vite": "^6"
  },
  "dependencies": {
    "sql.js": "^1",
    "marked": "^15"
  }
}
```

### svelte.config.js

```js
import adapter from '@sveltejs/adapter-node';

export default {
  kit: {
    adapter: adapter({
      out: 'build',
      precompress: false
    })
  }
};
```

### vite.config.ts

```ts
import { sveltekit } from '@sveltejs/kit/vite';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    tailwindcss(),
    sveltekit()
  ]
});
```

**Note:** No `ssr.external` needed — sql.js is pure JavaScript, no native modules.

### postcss.config.js

```js
// Empty file — prevents parent project's PostCSS/Tailwind config from being inherited.
// Required when the dashboard lives inside a monorepo or project that uses Tailwind v3.
export default {};
```

**This file is critical in monorepo contexts.** Without it, a parent project's PostCSS config causes `@layer base` errors with Tailwind v4.

### src/app.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  %sveltekit.head%
</head>
<body data-sveltekit-preload-data="hover">
  <div style="display: contents">%sveltekit.body%</div>
</body>
</html>
```

### src/app.css

```css
@import 'tailwindcss';

@theme {
  --font-sans: 'Plus Jakarta Sans', system-ui, sans-serif;

  --color-neutral-50: oklch(97% 0.01 250);
  --color-neutral-100: oklch(94% 0.01 250);
  --color-neutral-200: oklch(88% 0.01 250);
  --color-neutral-300: oklch(78% 0.015 250);
  --color-neutral-400: oklch(62% 0.015 250);
  --color-neutral-500: oklch(50% 0.015 250);
  --color-neutral-600: oklch(40% 0.015 250);
  --color-neutral-700: oklch(32% 0.02 250);
  --color-neutral-800: oklch(24% 0.02 250);
  --color-neutral-900: oklch(16% 0.02 250);

  --color-primary: oklch(55% 0.15 250);
  --color-primary-light: oklch(92% 0.04 250);
  --color-primary-dark: oklch(40% 0.12 250);

  --color-success: oklch(55% 0.14 145);
  --color-success-light: oklch(92% 0.05 145);
  --color-warning: oklch(70% 0.14 80);
  --color-warning-light: oklch(92% 0.06 80);
  --color-error: oklch(55% 0.18 25);
  --color-error-light: oklch(92% 0.05 25);
}

body {
  font-variant-numeric: tabular-nums;
}
```

**Note:** Use `@import 'tailwindcss'` with `@theme {}` directive — NOT `@layer theme`. Do not use Vite aliases for tailwindcss — let `@tailwindcss/vite` handle resolution.

---

## Database Layer — sql.js

### Module Structure (Single File)

All database logic lives in one file: `src/lib/server/db.ts`. No separate `schema.ts` — schema creation and seed data are part of the db module.

**Exports from `$lib/server/db`:**
- `initDb()` — Initialize database, create tables, seed data
- `getDb()` — Get the database instance
- `run(sql, params?)` — Execute INSERT/UPDATE/DELETE
- `get(sql, params?)` — Get single row
- `all(sql, params?)` — Get all rows
- `exec(sql)` — Execute raw SQL
- `saveDb()` — Persist to disk

**Never export `initSchema` from a separate file.** This was a source of import confusion.

### src/lib/server/db.ts

```ts
import sqlJsPkg from 'sql.js';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DB_DIR = path.resolve(__dirname, '../../../../data');
const DB_PATH = path.join(DB_DIR, 'dashboard.db');

// Handle sql.js default export quirk
const initSqlJs = (sqlJsPkg as { default: typeof sqlJsPkg }).default || sqlJsPkg;

let db: InstanceType<Awaited<ReturnType<typeof initSqlJs>>['Database']>;
let SQL: Awaited<ReturnType<typeof initSqlJs>>;

export async function initDb() {
  if (db) return db;

  SQL = await initSqlJs();
  fs.mkdirSync(DB_DIR, { recursive: true });

  if (fs.existsSync(DB_PATH)) {
    const buffer = fs.readFileSync(DB_PATH);
    db = new SQL.Database(buffer);
  } else {
    db = new SQL.Database();
  }

  // Enable foreign keys
  db.run('PRAGMA foreign_keys = ON');

  // Create tables + seed data
  initSchema();
  saveDb();

  return db;
}

function initSchema() {
  // --- Create tables (adapt to actual brand data) ---

  db.run(`
    CREATE TABLE IF NOT EXISTS campaigns (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      type TEXT DEFAULT 'other',
      status TEXT DEFAULT 'planning',
      start_date TEXT,
      end_date TEXT,
      budget REAL,
      channels TEXT,
      notes TEXT,
      created_at TEXT DEFAULT (datetime('now')),
      updated_at TEXT DEFAULT (datetime('now'))
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS content (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      type TEXT DEFAULT 'blog',
      status TEXT DEFAULT 'draft',
      platform TEXT,
      publish_date TEXT,
      campaign_id INTEGER,
      notes TEXT,
      created_at TEXT DEFAULT (datetime('now')),
      updated_at TEXT DEFAULT (datetime('now')),
      FOREIGN KEY (campaign_id) REFERENCES campaigns(id) ON DELETE SET NULL
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS sostac_progress (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      phase TEXT NOT NULL UNIQUE,
      phase_name TEXT NOT NULL,
      description TEXT,
      complete INTEGER DEFAULT 0,
      notes TEXT,
      updated_at TEXT DEFAULT (datetime('now'))
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS analytics_metrics (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      metric_name TEXT NOT NULL,
      value TEXT,
      period TEXT,
      date_recorded TEXT DEFAULT (date('now')),
      notes TEXT
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS channels (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      content_count INTEGER DEFAULT 0,
      notes TEXT,
      updated_at TEXT DEFAULT (datetime('now'))
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS documents (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      slug TEXT NOT NULL UNIQUE,
      title TEXT NOT NULL,
      category TEXT DEFAULT 'root',
      source_path TEXT NOT NULL,
      content TEXT NOT NULL,
      created_at TEXT DEFAULT (datetime('now'))
    )
  `);

  // --- Seed SOSTAC phases if empty ---
  const result = db.exec('SELECT COUNT(*) as c FROM sostac_progress');
  const count = result.length > 0 ? result[0].values[0][0] as number : 0;

  if (count === 0) {
    const phases = [
      ['situation', 'Situation Analysis', 'Where are we now?'],
      ['objectives', 'Objectives', 'Where do we want to go?'],
      ['strategy', 'Strategy', 'How do we get there?'],
      ['tactics', 'Tactics', 'What tools and activities?'],
      ['action', 'Action', 'Who does what, when?'],
      ['control', 'Control', 'How do we measure success?'],
    ];
    for (const [phase, name, desc] of phases) {
      db.run(
        'INSERT INTO sostac_progress (phase, phase_name, description, complete) VALUES (?, ?, ?, 0)',
        [phase, name, desc]
      );
    }
  }

  // --- Seed additional data from brand discovery here ---

  // --- Seed documents from discovered .md files ---
  // During generation, the LLM reads all .md files from the brand workspace
  // and inserts them here. Each file becomes a row in the documents table.
  // Example:
  //
  // const docs = [
  //   { slug: 'brand-context', title: 'Brand Context', category: 'root', source_path: 'brand-context.md', content: `...raw markdown...` },
  //   { slug: 'sostac-situation', title: 'Situation Analysis', category: 'sostac', source_path: 'sostac/situation.md', content: `...raw markdown...` },
  //   { slug: 'campaigns-launch-plan', title: 'Launch Plan', category: 'campaigns', source_path: 'campaigns/launch/plan.md', content: `...raw markdown...` },
  // ];
  //
  // const docCount = db.exec('SELECT COUNT(*) as c FROM documents');
  // const existingDocs = docCount.length > 0 ? docCount[0].values[0][0] as number : 0;
  // if (existingDocs === 0) {
  //   for (const doc of docs) {
  //     db.run(
  //       'INSERT INTO documents (slug, title, category, source_path, content) VALUES (?, ?, ?, ?, ?)',
  //       [doc.slug, doc.title, doc.category, doc.source_path, doc.content]
  //     );
  //   }
  // }
}

export function getDb() {
  if (!db) throw new Error('Database not initialized. Call initDb() first.');
  return db;
}

export function run(sql: string, params: unknown[] = []) {
  db.run(sql, params);
  saveDb();
}

export function get(sql: string, params: unknown[] = []): Record<string, unknown> | undefined {
  const stmt = db.prepare(sql);
  if (params.length) stmt.bind(params);
  if (stmt.step()) {
    const columns = stmt.getColumnNames();
    const values = stmt.get();
    stmt.free();
    const row: Record<string, unknown> = {};
    columns.forEach((col, i) => { row[col] = values[i]; });
    return row;
  }
  stmt.free();
  return undefined;
}

export function all(sql: string, params: unknown[] = []): Record<string, unknown>[] {
  const results: Record<string, unknown>[] = [];
  const stmt = db.prepare(sql);
  if (params.length) stmt.bind(params);
  while (stmt.step()) {
    const columns = stmt.getColumnNames();
    const values = stmt.get();
    const row: Record<string, unknown> = {};
    columns.forEach((col, i) => { row[col] = values[i]; });
    results.push(row);
  }
  stmt.free();
  return results;
}

export function exec(sql: string) {
  db.exec(sql);
  saveDb();
}

export function saveDb() {
  if (!db) return;
  const data = db.export();
  const buffer = Buffer.from(data);
  fs.writeFileSync(DB_PATH, buffer);
}
```

### Key Differences from better-sqlite3

| Aspect | better-sqlite3 | sql.js |
|--------|---------------|--------|
| **Installation** | Needs C++ compiler | Pure JS, works everywhere |
| **Initialization** | Synchronous | Async (`await initSqlJs()`) |
| **Persistence** | Automatic (file-backed) | Manual — call `saveDb()` after writes |
| **Query results** | Returns objects directly | Returns arrays, need manual mapping |
| **Import** | `import Database from 'better-sqlite3'` | `import sqlJsPkg from 'sql.js'` with default export handling |
| **Vite config** | Needs `ssr.external: ['better-sqlite3']` | No special config needed |

### Using db in routes

Import `initDb` in `+layout.server.ts` to ensure database is ready:

```ts
// src/routes/+layout.server.ts
import { initDb, all } from '$lib/server/db';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async () => {
  await initDb();

  // ... load nav data
};
```

All other `+page.server.ts` files can import helpers directly — db is already initialized by layout:

```ts
// src/routes/campaigns/+page.server.ts
import { all, run, get } from '$lib/server/db';
```

**Do NOT import `initDb` or `initSchema` in page server files** — only in the root layout.

---

## Route Patterns

### Layout (Dashboard Shell)

```ts
// src/routes/+layout.server.ts
import { initDb, all, get } from '$lib/server/db';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async () => {
  await initDb();

  const campaignCount = get('SELECT COUNT(*) as c FROM campaigns') as { c: number } | undefined;
  const contentCount = get('SELECT COUNT(*) as c FROM content') as { c: number } | undefined;
  const sostac = get('SELECT COUNT(*) as c FROM sostac_progress WHERE complete = 1') as { c: number } | undefined;
  const docCount = get('SELECT COUNT(*) as c FROM documents') as { c: number } | undefined;

  return {
    brandName: '{brand_name}',
    nav: [
      { href: '/', label: 'Overview', count: null },
      { href: '/campaigns', label: 'Campaigns', count: campaignCount?.c ?? 0 },
      { href: '/content', label: 'Content', count: contentCount?.c ?? 0 },
      { href: '/strategy', label: 'Strategy', count: `${sostac?.c ?? 0}/6` },
      { href: '/channels', label: 'Channels', count: null },
      { href: '/metrics', label: 'Metrics', count: null },
      { href: '/documents', label: 'Documents', count: docCount?.c ?? 0 },
    ],
  };
};
```

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import '../app.css';
  import Sidebar from '$lib/components/Sidebar.svelte';

  let { data, children } = $props();
</script>

<div class="flex min-h-screen bg-neutral-50">
  <Sidebar brandName={data.brandName} nav={data.nav} />
  <main class="flex-1 ml-60 p-8">
    {@render children()}
  </main>
</div>
```

### CRUD Route Pattern (Campaigns Example)

```ts
// src/routes/campaigns/+page.server.ts
import { all, run, get } from '$lib/server/db';
import { fail } from '@sveltejs/kit';
import type { PageServerLoad, Actions } from './$types';

export const load: PageServerLoad = async ({ url }) => {
  const status = url.searchParams.get('status');
  const search = url.searchParams.get('q');

  let query = 'SELECT * FROM campaigns WHERE 1=1';
  const params: unknown[] = [];

  if (status) {
    query += ' AND status = ?';
    params.push(status);
  }
  if (search) {
    query += ' AND name LIKE ?';
    params.push(`%${search}%`);
  }

  query += ' ORDER BY updated_at DESC';

  const campaigns = all(query, params);
  return { campaigns };
};

export const actions: Actions = {
  create: async ({ request }) => {
    const data = await request.formData();
    const name = data.get('name') as string;
    if (!name?.trim()) return fail(400, { error: 'Name is required' });

    run(`
      INSERT INTO campaigns (name, type, status, start_date, end_date, budget, channels, notes)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `, [
      name.trim(),
      data.get('type') || 'other',
      data.get('status') || 'planning',
      data.get('start_date') || null,
      data.get('end_date') || null,
      data.get('budget') ? Number(data.get('budget')) : null,
      data.get('channels') || null,
      data.get('notes') || null,
    ]);

    return { success: true };
  },

  update: async ({ request }) => {
    const data = await request.formData();
    const id = data.get('id');
    const name = data.get('name') as string;
    if (!name?.trim()) return fail(400, { error: 'Name is required' });

    run(`
      UPDATE campaigns SET name=?, type=?, status=?, start_date=?, end_date=?,
      budget=?, channels=?, notes=?, updated_at=datetime('now')
      WHERE id=?
    `, [
      name.trim(),
      data.get('type'),
      data.get('status'),
      data.get('start_date') || null,
      data.get('end_date') || null,
      data.get('budget') ? Number(data.get('budget')) : null,
      data.get('channels') || null,
      data.get('notes') || null,
      id,
    ]);

    return { success: true };
  },

  delete: async ({ request }) => {
    const data = await request.formData();
    const id = data.get('id');
    run('DELETE FROM campaigns WHERE id = ?', [id]);
    return { success: true };
  },
};
```

### Svelte Page with CRUD (Campaigns Example)

```svelte
<!-- src/routes/campaigns/+page.svelte -->
<script lang="ts">
  import { enhance } from '$app/forms';
  import Modal from '$lib/components/Modal.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  import EmptyState from '$lib/components/EmptyState.svelte';

  let { data } = $props();
  let showModal = $state(false);
  let editing = $state<Record<string, unknown> | null>(null);

  function openEdit(campaign: Record<string, unknown>) {
    editing = { ...campaign };
    showModal = true;
  }

  function openAdd() {
    editing = null;
    showModal = true;
  }

  function closeModal() {
    showModal = false;
    editing = null;
  }
</script>

<div class="space-y-6">
  <div class="flex items-center justify-between">
    <h1 class="text-xl font-semibold text-neutral-900">Campaigns</h1>
    <button onclick={openAdd}
            class="bg-primary text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-primary-dark transition-colors">
      Add campaign
    </button>
  </div>

  <!-- Filters -->
  <form method="GET" class="flex gap-3">
    <select name="status" class="border border-neutral-200 rounded-lg px-3 py-2 text-sm bg-white">
      <option value="">All status</option>
      <option value="planning">Planning</option>
      <option value="active">Active</option>
      <option value="paused">Paused</option>
      <option value="completed">Completed</option>
    </select>
    <input name="q" type="search" placeholder="Search campaigns..."
           class="border border-neutral-200 rounded-lg px-3 py-2 text-sm flex-1" />
    <button type="submit" class="border border-neutral-200 rounded-lg px-4 py-2 text-sm hover:bg-neutral-100">
      Filter
    </button>
  </form>

  {#if data.campaigns.length === 0}
    <EmptyState
      title="No campaigns yet"
      description="Track campaign progress, deadlines, and channel distribution."
      action="Add your first campaign"
      onAction={openAdd}
    />
  {:else}
    <div class="bg-white rounded-lg border border-neutral-200 overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b border-neutral-200">
            <th class="text-left px-4 py-3 font-medium text-neutral-500">Name</th>
            <th class="text-left px-4 py-3 font-medium text-neutral-500">Type</th>
            <th class="text-left px-4 py-3 font-medium text-neutral-500">Status</th>
            <th class="text-left px-4 py-3 font-medium text-neutral-500">Dates</th>
            <th class="text-right px-4 py-3 font-medium text-neutral-500">Actions</th>
          </tr>
        </thead>
        <tbody>
          {#each data.campaigns as campaign}
            <tr class="border-b border-neutral-100 last:border-0">
              <td class="px-4 py-3 font-medium text-neutral-900">{campaign.name}</td>
              <td class="px-4 py-3 text-neutral-600 capitalize">{campaign.type}</td>
              <td class="px-4 py-3">
                <StatusBadge status={campaign.status} />
              </td>
              <td class="px-4 py-3 text-neutral-500">
                {campaign.start_date || '—'} — {campaign.end_date || '—'}
              </td>
              <td class="px-4 py-3 text-right">
                <button onclick={() => openEdit(campaign)}
                        class="text-primary hover:text-primary-dark text-sm mr-3">Edit</button>
                <form method="POST" action="?/delete" use:enhance class="inline">
                  <input type="hidden" name="id" value={campaign.id} />
                  <button type="submit"
                          class="text-error hover:text-red-700 text-sm"
                          onclick={(e) => { if (!confirm('Delete this campaign?')) e.preventDefault(); }}>
                    Delete
                  </button>
                </form>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  {/if}
</div>

{#if showModal}
  <Modal onclose={closeModal} title={editing ? 'Edit campaign' : 'Add campaign'}>
    <form method="POST" action={editing ? '?/update' : '?/create'} use:enhance={() => {
      return async ({ update }) => {
        await update();
        closeModal();
      };
    }}>
      {#if editing}
        <input type="hidden" name="id" value={editing.id} />
      {/if}

      <div class="space-y-4">
        <div>
          <label for="name" class="block text-sm font-medium text-neutral-700 mb-1">Name</label>
          <input id="name" name="name" type="text" required value={editing?.name ?? ''}
                 class="w-full border border-neutral-200 rounded-lg px-3 py-2 text-sm" />
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label for="type" class="block text-sm font-medium text-neutral-700 mb-1">Type</label>
            <select id="type" name="type" class="w-full border border-neutral-200 rounded-lg px-3 py-2 text-sm">
              <option value="launch" selected={editing?.type === 'launch'}>Launch</option>
              <option value="email" selected={editing?.type === 'email'}>Email</option>
              <option value="paid-ads" selected={editing?.type === 'paid-ads'}>Paid Ads</option>
              <option value="content" selected={editing?.type === 'content'}>Content</option>
              <option value="social" selected={editing?.type === 'social'}>Social</option>
              <option value="other" selected={!editing || editing?.type === 'other'}>Other</option>
            </select>
          </div>
          <div>
            <label for="status" class="block text-sm font-medium text-neutral-700 mb-1">Status</label>
            <select id="status" name="status" class="w-full border border-neutral-200 rounded-lg px-3 py-2 text-sm">
              <option value="planning" selected={!editing || editing?.status === 'planning'}>Planning</option>
              <option value="active" selected={editing?.status === 'active'}>Active</option>
              <option value="paused" selected={editing?.status === 'paused'}>Paused</option>
              <option value="completed" selected={editing?.status === 'completed'}>Completed</option>
            </select>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label for="start_date" class="block text-sm font-medium text-neutral-700 mb-1">Start date</label>
            <input id="start_date" name="start_date" type="date" value={editing?.start_date ?? ''}
                   class="w-full border border-neutral-200 rounded-lg px-3 py-2 text-sm" />
          </div>
          <div>
            <label for="end_date" class="block text-sm font-medium text-neutral-700 mb-1">End date</label>
            <input id="end_date" name="end_date" type="date" value={editing?.end_date ?? ''}
                   class="w-full border border-neutral-200 rounded-lg px-3 py-2 text-sm" />
          </div>
        </div>
        <div>
          <label for="notes" class="block text-sm font-medium text-neutral-700 mb-1">Notes</label>
          <textarea id="notes" name="notes" rows="3"
                    class="w-full border border-neutral-200 rounded-lg px-3 py-2 text-sm">{editing?.notes ?? ''}</textarea>
        </div>
      </div>

      <div class="mt-6 flex justify-end gap-3">
        <button type="button" onclick={closeModal}
                class="border border-neutral-200 rounded-lg px-4 py-2 text-sm hover:bg-neutral-100">
          Cancel
        </button>
        <button type="submit"
                class="bg-primary text-white rounded-lg px-4 py-2 text-sm font-medium hover:bg-primary-dark transition-colors">
          {editing ? 'Save changes' : 'Add campaign'}
        </button>
      </div>
    </form>
  </Modal>
{/if}
```

---

## Shared Components

### Sidebar.svelte

```svelte
<script lang="ts">
  import { page } from '$app/state';

  let { brandName, nav }: {
    brandName: string;
    nav: Array<{ href: string; label: string; count: string | number | null }>
  } = $props();
</script>

<aside class="w-60 bg-white border-r border-neutral-200 fixed inset-y-0 left-0 flex flex-col">
  <div class="p-6 border-b border-neutral-200">
    <h1 class="font-semibold text-neutral-900">{brandName}</h1>
    <p class="text-xs text-neutral-400 mt-1">Marketing Dashboard</p>
  </div>

  <nav class="flex-1 p-3 space-y-0.5">
    {#each nav as item}
      <a href={item.href}
         class="flex items-center justify-between px-3 py-2.5 rounded-lg text-sm transition-colors
                {page.url.pathname === item.href ? 'bg-primary-light text-primary-dark font-medium' : 'text-neutral-600 hover:bg-neutral-100'}">
        <span>{item.label}</span>
        {#if item.count !== null}
          <span class="text-xs text-neutral-400">{item.count}</span>
        {/if}
      </a>
    {/each}
  </nav>

  <div class="p-4 border-t border-neutral-200 space-y-2">
    <a href="/api/export"
       class="block text-center text-xs text-neutral-500 hover:text-neutral-700 py-1.5 border border-neutral-200 rounded-lg">
      Export JSON
    </a>
  </div>
</aside>
```

### Modal.svelte

```svelte
<script lang="ts">
  import type { Snippet } from 'svelte';

  let { title, onclose, children }: { title: string; onclose: () => void; children: Snippet } = $props();
</script>

<div class="fixed inset-0 z-50 flex items-center justify-center">
  <button class="absolute inset-0 bg-neutral-900/30" onclick={onclose} aria-label="Close"></button>
  <div class="relative bg-white rounded-xl shadow-lg w-full max-w-lg mx-4 p-6">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-lg font-semibold text-neutral-900">{title}</h2>
      <button onclick={onclose} class="text-neutral-400 hover:text-neutral-600 text-xl leading-none">&times;</button>
    </div>
    {@render children()}
  </div>
</div>
```

### StatusBadge.svelte

```svelte
<script lang="ts">
  let { status }: { status: string } = $props();

  const styles: Record<string, string> = {
    active: 'bg-success-light text-green-800',
    published: 'bg-success-light text-green-800',
    completed: 'bg-success-light text-green-800',
    planning: 'bg-warning-light text-yellow-800',
    review: 'bg-warning-light text-yellow-800',
    pending: 'bg-warning-light text-yellow-800',
    draft: 'bg-neutral-100 text-neutral-600',
    paused: 'bg-neutral-100 text-neutral-600',
    inactive: 'bg-neutral-100 text-neutral-600',
    failed: 'bg-error-light text-red-800',
    blocked: 'bg-error-light text-red-800',
    cancelled: 'bg-error-light text-red-800',
  };
</script>

<span class="inline-flex px-2 py-0.5 rounded text-xs font-medium capitalize {styles[status] ?? 'bg-neutral-100 text-neutral-600'}">
  {status}
</span>
```

### EmptyState.svelte

```svelte
<script lang="ts">
  let { title, description, action, onAction }: {
    title: string;
    description: string;
    action: string;
    onAction: () => void;
  } = $props();
</script>

<div class="bg-white rounded-lg border border-neutral-200 p-12 text-center">
  <h3 class="text-sm font-medium text-neutral-900 mb-1">{title}</h3>
  <p class="text-sm text-neutral-500 mb-4">{description}</p>
  <button onclick={onAction}
          class="bg-primary text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-primary-dark transition-colors">
    {action}
  </button>
</div>
```

---

## Markdown Rendering

### src/lib/utils/markdown.ts

Server-side utility that converts raw markdown to HTML using `marked`.

```ts
import { marked } from 'marked';

// Configure marked for clean output
marked.setOptions({
  gfm: true,
  breaks: true,
});

export function renderMarkdown(content: string): string {
  return marked.parse(content) as string;
}
```

**Note:** `marked` is used server-side only — called in `+page.server.ts`, never in Svelte components directly.

### MarkdownContent.svelte

```svelte
<script lang="ts">
  let { html }: { html: string } = $props();
</script>

<article class="markdown-content">
  {@html html}
</article>

<style>
  .markdown-content :global(h1) {
    font-size: 1.75rem;
    font-weight: 600;
    color: var(--color-neutral-900);
    margin-top: 2rem;
    margin-bottom: 0.75rem;
    line-height: 1.2;
  }
  .markdown-content :global(h2) {
    font-size: 1.375rem;
    font-weight: 600;
    color: var(--color-neutral-900);
    margin-top: 1.75rem;
    margin-bottom: 0.5rem;
    line-height: 1.25;
  }
  .markdown-content :global(h3) {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--color-neutral-800);
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
  }
  .markdown-content :global(p) {
    margin-bottom: 1rem;
    line-height: 1.7;
    color: var(--color-neutral-700);
  }
  .markdown-content :global(ul),
  .markdown-content :global(ol) {
    margin-bottom: 1rem;
    padding-left: 1.5rem;
    color: var(--color-neutral-700);
  }
  .markdown-content :global(li) {
    margin-bottom: 0.25rem;
    line-height: 1.6;
  }
  .markdown-content :global(ul) {
    list-style-type: disc;
  }
  .markdown-content :global(ol) {
    list-style-type: decimal;
  }
  .markdown-content :global(code) {
    background: var(--color-neutral-100);
    padding: 0.15rem 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.875em;
  }
  .markdown-content :global(pre) {
    background: var(--color-neutral-900);
    color: var(--color-neutral-100);
    padding: 1rem 1.25rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    margin-bottom: 1rem;
    font-size: 0.875rem;
    line-height: 1.5;
  }
  .markdown-content :global(pre code) {
    background: none;
    padding: 0;
    border-radius: 0;
    color: inherit;
    font-size: inherit;
  }
  .markdown-content :global(blockquote) {
    border-left: 3px solid var(--color-primary);
    padding-left: 1rem;
    margin-bottom: 1rem;
    color: var(--color-neutral-600);
    font-style: italic;
  }
  .markdown-content :global(table) {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
    font-size: 0.875rem;
  }
  .markdown-content :global(th) {
    text-align: left;
    padding: 0.5rem 0.75rem;
    border-bottom: 2px solid var(--color-neutral-200);
    font-weight: 600;
    color: var(--color-neutral-700);
  }
  .markdown-content :global(td) {
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid var(--color-neutral-100);
    color: var(--color-neutral-600);
  }
  .markdown-content :global(a) {
    color: var(--color-primary);
    text-decoration: underline;
    text-underline-offset: 2px;
  }
  .markdown-content :global(a:hover) {
    color: var(--color-primary-dark);
  }
  .markdown-content :global(hr) {
    border: none;
    border-top: 1px solid var(--color-neutral-200);
    margin: 2rem 0;
  }
  .markdown-content :global(strong) {
    font-weight: 600;
    color: var(--color-neutral-900);
  }
  .markdown-content :global(img) {
    max-width: 100%;
    border-radius: 0.5rem;
    margin: 1rem 0;
  }
</style>
```

---

## Documents Route Patterns

### Documents Index — src/routes/documents/+page.server.ts

```ts
import { all } from '$lib/server/db';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  const documents = all('SELECT id, slug, title, category, source_path FROM documents ORDER BY category, title');

  // Group by category
  const grouped: Record<string, Array<{ slug: string; title: string; source_path: string }>> = {};
  for (const doc of documents) {
    const cat = (doc.category as string) || 'root';
    if (!grouped[cat]) grouped[cat] = [];
    grouped[cat].push({
      slug: doc.slug as string,
      title: doc.title as string,
      source_path: doc.source_path as string,
    });
  }

  return { grouped, total: documents.length };
};
```

### Documents Index — src/routes/documents/+page.svelte

```svelte
<script lang="ts">
  import EmptyState from '$lib/components/EmptyState.svelte';

  let { data } = $props();

  const categoryLabels: Record<string, string> = {
    root: 'Brand',
    sostac: 'SOSTAC Strategy',
    campaigns: 'Campaigns',
    content: 'Content',
    channels: 'Channels',
    operations: 'Operations',
  };

  const categories = Object.entries(data.grouped);
</script>

<div class="space-y-8">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-xl font-semibold text-neutral-900">Documents</h1>
      <p class="text-sm text-neutral-500 mt-1">{data.total} files from brand workspace</p>
    </div>
  </div>

  {#if categories.length === 0}
    <EmptyState
      title="No documents found"
      description="Documents are indexed from your brand workspace during dashboard generation."
      action="Regenerate dashboard"
      onAction={() => {}}
    />
  {:else}
    {#each categories as [category, docs]}
      <section>
        <h2 class="text-sm font-medium text-neutral-500 uppercase tracking-wide mb-3">
          {categoryLabels[category] ?? category}
        </h2>
        <div class="bg-white rounded-lg border border-neutral-200 divide-y divide-neutral-100">
          {#each docs as doc}
            <a href="/documents/{doc.slug}"
               class="flex items-center justify-between px-4 py-3 hover:bg-neutral-50 transition-colors">
              <div>
                <span class="text-sm font-medium text-neutral-900">{doc.title}</span>
                <span class="text-xs text-neutral-400 ml-2">{doc.source_path}</span>
              </div>
              <span class="text-neutral-300 text-sm">&rarr;</span>
            </a>
          {/each}
        </div>
      </section>
    {/each}
  {/if}
</div>
```

### Document Detail — src/routes/documents/[slug]/+page.server.ts

```ts
import { get } from '$lib/server/db';
import { error } from '@sveltejs/kit';
import { renderMarkdown } from '$lib/utils/markdown';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const doc = get('SELECT * FROM documents WHERE slug = ?', [params.slug]);
  if (!doc) throw error(404, 'Document not found');

  const html = renderMarkdown(doc.content as string);

  return {
    title: doc.title as string,
    category: doc.category as string,
    source_path: doc.source_path as string,
    html,
  };
};
```

### Document Detail — src/routes/documents/[slug]/+page.svelte

```svelte
<script lang="ts">
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';

  let { data } = $props();

  const categoryLabels: Record<string, string> = {
    root: 'Brand',
    sostac: 'SOSTAC Strategy',
    campaigns: 'Campaigns',
    content: 'Content',
    channels: 'Channels',
    operations: 'Operations',
  };
</script>

<div class="space-y-6">
  <div>
    <a href="/documents" class="text-sm text-primary hover:text-primary-dark">&larr; All documents</a>
  </div>

  <div>
    <div class="flex items-center gap-2 mb-1">
      <span class="text-xs text-neutral-400 uppercase tracking-wide">
        {categoryLabels[data.category] ?? data.category}
      </span>
      <span class="text-xs text-neutral-300">/</span>
      <span class="text-xs text-neutral-400">{data.source_path}</span>
    </div>
    <h1 class="text-xl font-semibold text-neutral-900">{data.title}</h1>
  </div>

  <div class="bg-white rounded-lg border border-neutral-200 p-8 max-w-3xl">
    <MarkdownContent html={data.html} />
  </div>
</div>
```

---

## Export/Import API

### src/routes/api/export/+server.ts

```ts
import { json } from '@sveltejs/kit';
import { all } from '$lib/server/db';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import type { RequestHandler } from './$types';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const EXPORT_DIR = path.resolve(__dirname, '../../../../../data/export');

export const GET: RequestHandler = async () => {
  const tables = ['campaigns', 'content', 'sostac_progress', 'analytics_metrics', 'channels', 'documents'];
  const exported: Record<string, number> = {};

  fs.mkdirSync(EXPORT_DIR, { recursive: true });

  for (const table of tables) {
    const rows = all(`SELECT * FROM ${table}`);
    fs.writeFileSync(
      path.join(EXPORT_DIR, `${table}.json`),
      JSON.stringify(rows, null, 2)
    );
    exported[table] = rows.length;
  }

  return json({ exported, path: 'data/export/' });
};
```

### src/routes/api/import/+server.ts

```ts
import { json } from '@sveltejs/kit';
import { run, exec, saveDb } from '$lib/server/db';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import type { RequestHandler } from './$types';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const IMPORT_DIR = path.resolve(__dirname, '../../../../../data/export');

export const POST: RequestHandler = async () => {
  if (!fs.existsSync(IMPORT_DIR)) {
    return json({ error: 'No export directory found' }, { status: 404 });
  }

  const imported: Record<string, number> = {};
  const files = fs.readdirSync(IMPORT_DIR).filter(f => f.endsWith('.json'));

  for (const file of files) {
    const table = path.basename(file, '.json');
    const data = JSON.parse(fs.readFileSync(path.join(IMPORT_DIR, file), 'utf-8'));

    if (!Array.isArray(data) || data.length === 0) continue;

    exec(`DELETE FROM ${table}`);

    const columns = Object.keys(data[0]);
    const placeholders = columns.map(() => '?').join(', ');

    for (const row of data) {
      run(
        `INSERT INTO ${table} (${columns.join(', ')}) VALUES (${placeholders})`,
        columns.map(c => row[c])
      );
    }

    imported[table] = data.length;
  }

  saveDb();
  return json({ imported });
};
```

---

## Key SvelteKit Behaviors

### Reactivity After Form Actions

After a form action completes, SvelteKit automatically re-runs the page's `load` function. The UI updates without any manual `fetch()` or `invalidate()`.

### Server-Side Filtering

Use URL search params for filters. GET forms submit to the same page with params. The `load` function reads `url.searchParams` and queries accordingly.

### Progressive Enhancement

`use:enhance` on forms makes them submit via fetch (no page reload) while preserving the form's ability to work without JavaScript.

### $lib/server/ Boundary

SvelteKit enforces that `$lib/server/` files cannot be imported from client code. All database code must live in `+page.server.ts`, `+layout.server.ts`, or `+server.ts` files.

### sql.js Persistence

Unlike better-sqlite3, sql.js operates in memory. The `saveDb()` function writes the database to disk. It is called automatically by `run()` and `exec()` helpers. Always use those helpers rather than calling `db.run()` directly.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| **Changes not reflected in browser** | Stop dev server, delete `.svelte-kit` folder, restart `npm run dev` |
| **`@layer base` or PostCSS errors** | Ensure empty `postcss.config.js` exists in dashboard root |
| **Port already in use** | Use `npm run dev -- --port 5180` |
| **Database not persisting** | Check that `saveDb()` is called after writes (use `run()`/`exec()` helpers) |
| **Import errors** | All DB imports come from `$lib/server/db` — never import `initSchema` separately |

---

## Generation Checklist

Before finishing generation, verify:

- [ ] `postcss.config.js` exists (empty, prevents parent config inheritance)
- [ ] `vite.config.ts` has NO `ssr.external` (not needed for sql.js)
- [ ] `@sveltejs/vite-plugin-svelte` is `^5` (compatible with Vite 6)
- [ ] All DB code is in single `$lib/server/db.ts` (no separate schema.ts)
- [ ] Only `+layout.server.ts` imports `initDb` — page routes import `all`/`run`/`get`
- [ ] Schema creation and seed data live inside `db.ts`
- [ ] Every CRUD route has `create`, `update`, `delete` form actions
- [ ] `use:enhance` on all POST forms
- [ ] `saveDb()` is called in `run()` and `exec()` helpers
- [ ] Filters use GET forms with URL search params
- [ ] Empty states have title, description, and action button
- [ ] Status badges use semantic colors (not gradients)
- [ ] Documents table seeded with all discovered `.md` files from brand workspace
- [ ] `marked` is in `dependencies` (not devDependencies) in package.json
- [ ] Markdown rendered server-side in `+page.server.ts`, never in Svelte components
- [ ] Document slugs are unique, derived from file path (e.g., `sostac-situation`, `campaigns-launch-plan`)
- [ ] `.gitignore` includes `data/dashboard.db`, `node_modules`, `.svelte-kit`
- [ ] Design follows `design-guide.md` anti-patterns checklist