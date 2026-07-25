# Progress Tracking

When the seller asks where they are, what's in flight, or what's next, read memory first and give position plus one clear next step — don't dump file contents.

## Read order

1. `{memory-root}/index.md` — brand summary, library stats, recent proposals, open threads.
2. Scan `{memory-root}/proposals/*/` — folders with artifacts but no `final-proposal.*` = in progress.
3. For the active run (user-named or most recent in-progress), check:

| File | Stage complete |
|------|----------------|
| `brief.md` | Intake |
| `research-dossier.html` | Research |
| `pricing.json` | Pricing |
| `draft-v1.md` | Generation (draft) |
| `final-proposal.*` | Generation (export) |
| `outcome.md` | Learning loop closed |

4. `library/case-studies-index.json` — entry count (empty → recommend library).
5. `clients/{slug}/history.md` — if seller named a client.

## Present as position + next step

```
# Proposal Pipeline — Status

**Where you are:** {one line — e.g. "Acme run in progress — research done, pricing not started."}

**Library:** {N} case studies indexed | last re-index {date or "never"}
**In-progress runs:** {list slug-date + stage, or "none"}
**Recent completed:** {last 1–2 with outcome if known}

**Highest-value next step:** {single actionable item}
```

## Arc-based next steps

| State | Next step |
|-------|-----------|
| No workspace / missing `index.md` | Run `paw-pa-setup` |
| Empty case-study index | Drop docs in `library/inbox/` → `paw-pa-library` |
| No active run, seller has a brief | Start pipeline — create run folder → `paw-pa-intake` |
| `brief.md` only | Clarify gaps (guided) or `paw-pa-research` |
| Dossier, no pricing | `paw-pa-pricing` (or check-in first in guided mode) |
| Pricing, no draft | `paw-pa-generation` |
| Final proposal, no outcome | Send reminder + offer outcome intake |
| Outcome recorded | Suggest next brief or library refresh if index stale |

## In-progress run resume offer

If multiple in-progress runs exist, list them and ask which to resume:

```
**Open runs:**
1. `acme-corp-2026-07-03` — brief + dossier (ready for pricing)
2. `beta-inc-2026-07-01` — brief only (needs research)

Which run should we continue?
```

## Mode reminder

If a run was started in guided mode, note which check-in gate applies next. If autonomous, state that the next specialist can run without pausing.
