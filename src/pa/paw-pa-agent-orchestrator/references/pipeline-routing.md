# Pipeline Routing

The orchestrator coordinates; the specialists produce. When the seller is ready for a pipeline phase, hand off with full context rather than doing the work yourself. Each specialist reads shared memory on activation, so the handoff is mostly confirming prerequisites, naming the run folder, and telling the seller what they'll get and where it lands.

## The specialists

| Phase | Specialist | What it produces | Reads from workspace |
|-------|-----------|------------------|----------------------|
| Brief intake | `paw-pa-intake` | Structured `brief.md` + optional `transcript.md` | Config (`assemblyai_api_key`, `default_proposal_type`), `index.md` |
| Research | `paw-pa-research` | HTML research dossier (auto-opens) + optional `.md` | `brief.md`, `case-studies-index.json`, `clients/{slug}/history.md` |
| Pricing | `paw-pa-pricing` | `pricing.json` + pricing-history append | `brief.md`, research dossier, `pricing-history.json` |
| Generation | `paw-pa-generation` | `draft-v1.md`, variations, `final-proposal.{html,pdf,docx,md}` | `brief.md`, dossier, `pricing.json`, `brand/` |
| Library (independent) | `paw-pa-library` | Updated indexes, boilerplate, scope templates | `library/inbox/`, existing indexes |

## Pipeline order

The default arc is linear:

```
intake → research → pricing → generation
```

**Ideal prerequisites:**

- **Research** requires `brief.md`. Recommend a populated `case-studies-index.json` before first research run.
- **Pricing** requires `brief.md`. Research dossier strongly recommended for calibrated benchmarks.
- **Generation** requires `brief.md` and `pricing.json`. Research dossier recommended for proof sections.

Power users may skip or re-run phases on existing artifacts — e.g. re-price without re-research, regenerate draft without re-pricing.

## How to hand off

1. **Confirm the run folder** — `{memory-root}/proposals/{slug}-{date}/`. Create it at run start if new.
2. **State the mode** — guided (you'll check in after this phase) or autonomous (runs through).
3. **Name the specialist** — tell the seller which skill to invoke and what path to pass.
4. **Set expectations** — what artifact appears, where it saves, what you'll do after (check-in or next handoff).

Example handoff:

> "Run folder is `proposals/acme-corp-2026-07-03/`. Invoke **`paw-pa-intake`** with your voice memo — it'll transcribe (AssemblyAI) and write `brief.md`. When intake finishes, I'll review completeness before we send it to research."

The seller invokes the specialist directly. Shared memory carries context — you don't need to restate the brief in chat.

## After a specialist runs

When the seller returns from a specialist:

1. Read what landed in `{run-folder}/`.
2. In **guided** mode, run the appropriate check-in gate (`references/check-in-gates.md`).
3. Update `index.md` if the run status changed.
4. Append `[orchestrator]` to today's `daily/` log.
5. Route to the next specialist or close the run.

## Resume logic

Scan `{run-folder}/` for artifacts to determine stage:

| Artifacts present | Next step |
|-------------------|-----------|
| (empty folder) | Intake |
| `brief.md` only | Research (or clarification if gaps in guided mode) |
| `brief.md` + dossier | Pricing |
| `brief.md` + `pricing.json` | Generation |
| `draft-v*.md` / `final-proposal.*` | Offer outcome intake or revision |

## Orchestrator creates; specialists write phase artifacts

- **You create** the run folder at pipeline start.
- **Intake writes** `brief.md` (and `transcript.md` when applicable).
- **Research writes** `research-dossier.html`.
- **Pricing writes** `pricing.json`.
- **Generation writes** drafts and exports.
- **You write** `outcome.md` and curate `index.md` / `clients/` after seller feedback.

Never write research content, pricing numbers, or proposal copy into those files yourself — only coordinate the specialists that own them.
