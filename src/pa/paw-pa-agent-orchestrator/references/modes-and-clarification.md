# Modes & Thin-Brief Clarification

Two execution modes control how the pipeline handles gaps, pauses, and seller involvement. Mode is chosen **per run**, not permanently — `default_mode` in config is only the session default.

## Guided mode

**Behavior:** Pause for seller input at thin-brief gaps and at check-in gates after research, pricing, and draft.

**Thin brief handling:**

1. After intake completes, read `brief.md` and any completeness report / `assumptions[]`.
2. For **critical gaps** (client name, project scope, proposal type), ask clarifying questions before invoking research.
3. Present missing fields plainly: "Budget isn't in the brief — what's the client's range or your target quote?"
4. After answers, either update `brief.md` via re-invoking `paw-pa-intake` or note corrections for the seller to confirm.
5. Do **not** proceed to research until critical gaps are resolved or the seller explicitly says "proceed with what we have."

**Critical fields** (from intake completeness rules):

- `clientName` — who is this for?
- `projectDescription` — what work is being proposed?
- `proposalType` — pitch, RFP, or scoping?
- `budget` — strongly recommended before pricing (ask if missing)
- `timeline` — strongly recommended before pricing (ask if missing)

**Check-in gates** — see `references/check-in-gates.md`. After research, pricing, and draft, present the artifact and wait for approval before the next phase.

**When to recommend:** First-time users, high-stakes deals, unfamiliar clients, RFP responses, or when the seller says "walk me through it."

## Autonomous mode

**Behavior:** No pauses. Workflows run back-to-back. Intake records reasonable `assumptions[]` for missing fields instead of asking questions.

**Thin brief handling:**

1. Let `paw-pa-intake` flag gaps and write `assumptions[]` in `brief.md`.
2. Before starting, tell the seller what autonomous mode means: "I'll run straight through. Missing budget and timeline will be assumed and flagged at the top of the final proposal."
3. Do not stop mid-pipeline for clarification.
4. After generation completes, summarize all assumptions in one callout for the seller to review.

**Assumption visibility contract:** Generation surfaces `assumptions[]` as a callout at the top of `final-proposal.*`. Your closing summary should list them again with the run folder path.

**When to recommend:** Batch runs, repeat clients with strong history, voice memos the seller will audit later, or when the seller says "just run it" / "fast mode."

## Mode selection

At run start:

```
**Pipeline mode for this run?**
- **Guided** — I'll ask on thin briefs and pause after research, pricing, and draft for your review. (default: {default_mode})
- **Autonomous** — Brief in, proposal out. Assumptions flagged, no check-ins.
```

Accept inline overrides: "autonomous", "guided", "fast mode", "walk me through."

Persist mode choice only for the current run (in conversation context) — do not write to config unless the seller asks to change `default_mode` (then route to `paw-pa-setup` or note the config key).

## Clarification vs assumption — decision table

| Gap | Guided | Autonomous |
|-----|--------|------------|
| Missing client name | Ask before research | Assume from context; flag |
| Missing budget | Ask before pricing | Assume mid-market placeholder; flag prominently |
| Missing timeline | Ask before pricing | Assume "TBD with client"; flag |
| Ambiguous proposal type | Ask at intake | Use `default_proposal_type`; flag if inferred |
| Vague scope | Ask 1–2 sharpening questions | Synthesize best-effort scope; flag assumptions |

## Never silent weakness

Both modes honor the non-negotiable: a thin brief must never silently become a weak proposal. Guided mode asks; autonomous mode flags. If the seller refuses to answer in guided mode, document their choice and proceed with flagged assumptions — same visibility as autonomous.
