# Check-In Gates

Check-in gates apply in **guided mode only**. After each major workflow completes, present the artifact, summarize what matters, and wait for seller approval before invoking the next specialist.

Autonomous mode skips all gates — workflows run sequentially without pauses.

## Gate 1 — After research

**Trigger:** `paw-pa-research` completed; `{run-folder}/research-dossier.html` exists.

**Present:**
- Path to the dossier (offer to open it — research auto-opens HTML on completion).
- Top 2–3 local case-study matches and whether web benchmarks were found.
- Any caveats ("thin web evidence for this niche — local matches only").
- Returning-client notes if `clients/{slug}/history.md` informed the dossier.

**Ask:**
```
Research dossier is ready at `{run-folder}/research-dossier.html`.

**Highlights:** {2–3 bullets}

Ready to move to pricing, or do you want to re-run research / add context first?
```

**Outcomes:**
- **Approve** → Route to `paw-pa-pricing`.
- **Revise** → Seller provides notes; re-invoke `paw-pa-research` with context.
- **Skip pricing calibration** → Rare; still route to pricing but note reduced benchmark quality.

## Gate 2 — After pricing

**Trigger:** `paw-pa-pricing` completed; `{run-folder}/pricing.json` exists.

**Present:**
- Pricing mode (line-item, tiered, value-based).
- Total or tier summary (numbers only — you read them from the file, you didn't calculate them).
- Sanity check headline from `pricing.json` if present (too cheap / too expensive signals).
- Calibration note if history informed rates.

**Ask:**
```
Pricing breakdown is at `{run-folder}/pricing.json`.

**Summary:** {mode} — {tier or total summary}
**Sanity check:** {one line from pricing.json or "no flags"}

Approve to generate the proposal, or adjust pricing first?
```

**Outcomes:**
- **Approve** → Route to `paw-pa-generation`.
- **Revise** → Re-invoke `paw-pa-pricing` (optionally with mode override).
- **Change tiers** → Note seller preference; hand back to pricing specialist.

## Gate 3 — After draft

**Trigger:** `paw-pa-generation` completed; `{run-folder}/draft-v1.md` and/or `final-proposal.*` exist.

**Present:**
- Draft and export paths.
- Proposal type and client name.
- Assumptions callout reminder if autonomous or thin brief.
- Export formats available (note if pandoc missing → HTML/MD only).

**Ask:**
```
Draft ready at `{run-folder}/draft-v1.md`.
Final export: `{run-folder}/final-proposal.{ext}`

Review the draft. Want a revision (v2), a short/long variation, or is this ready to send?
```

**Outcomes:**
- **Approve / send** → Remind seller to record outcome when they hear back (`references/outcome-and-client-history.md`).
- **Revise** → Re-invoke `paw-pa-generation` with revision notes (increments draft version).
- **Re-price then regenerate** → Route to pricing first, then generation.

## Skipping gates

If the seller says "skip check-ins", "run it through", or "autonomous for this run", switch to autonomous behavior for the remainder of the run — no further gates until completion summary.

## Gate discipline

- **Don't summarize the full artifact** — point to the file and highlight 2–4 bullets. The seller reads the real output.
- **Don't rewrite pricing or research** in chat — the JSON and HTML are source of truth.
- **Don't invoke the next workflow** until approval or explicit skip.
- **Log gate decisions** — append `[orchestrator] check-in: {gate} approved|revised|skipped` to `daily/YYYY-MM-DD.md`.
