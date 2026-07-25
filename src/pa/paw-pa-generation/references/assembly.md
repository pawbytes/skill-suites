# Proposal Assembly

The primary generation path. Outcome: a branded, type-adaptive proposal draft with short/long variations, ready for export. You have `brief.md`, `pricing.json`, research dossier, brand files, and scope templates in context from activation.

## Pre-flight

Before writing a word, confirm:

1. **`proposalType`** from brief — `pitch` | `rfp` | `scoping`. Load the matching section template reference.
2. **Language** — `default_language` from config, or brief override. All output in that language.
3. **Autonomous assumptions** — if `assumptions[]` in brief is non-empty, plan the callout block at the very top of every output variant.
4. **Missing dossier** — if `research-dossier.html` is absent, note in `generation-summary.json` and lean on brief + scope templates; do not invent case studies.
5. **T&Cs variant** — scan `brand/boilerplate/terms.md` for a section matching proposal type and deal size (from `pricing.json` total). If none matches, use the closest variant and flag for seller review — never draft new legal text.

## Synthesis pass (internal, before drafting)

Read and cross-reference:

| Source | Extract |
|--------|---------|
| `brief.md` | Client name, problem, requirements, constraints, timeline, budget signals, decision maker |
| `research-dossier.html` | Client intel, tech stack, ranked local case-study matches, web benchmarks, competitive context |
| `pricing.json` | Mode, line items/tiers, total, calibration notes, sanity check, discount modeling |
| `scope-templates.md` | Reusable clauses matching service type / deliverables |
| `brand/boilerplate/` | About-us, bios, T&Cs (verbatim) |
| `brand/identity.md` | Voice, tone, colors (for export styling) |

Build an internal outline:

- **Hook** — client's problem in their words (from brief + research intel)
- **Proof points** — 2–4 case studies (local first, web second) with specific outcomes
- **Approach** — how you'll solve it, mapped to requirements
- **Scope** — deliverables pulled from templates + brief requirements
- **Pricing** — formatted per type and `pricing.json` mode
- **Timeline & milestones** — from brief, realistic against scope
- **Risk register** — especially for RFP/scoping; lighter for pitch
- **Team / about** — from boilerplate bios + about-us
- **T&Cs** — verbatim from terms.md
- **Objection threads** — 3–5 anticipated objections with pre-emptive copy woven into relevant sections (not a separate FAQ dump unless RFP type)

## Type-adaptive assembly

One flow; `proposalType` selects which sections expand and which tone to use. Load the type-specific template for section order and emphasis:

| Type | Template | Tone | Pricing style | Risk register |
|------|----------|------|---------------|---------------|
| `pitch` | `section-templates-pitch.md` | Persuasive, outcome-led | Tiered preferred; value anchor | Brief (top 3 risks) |
| `rfp` | `section-templates-rfp.md` | Formal, compliance-oriented | Line-item tables; milestone billing | Full matrix + compliance |
| `scoping` | `section-templates-scoping.md` | Collaborative, precise | Line-items + milestones | Full matrix; assumptions explicit |

### Shared section bones (all types)

Every proposal includes these, reordered per type template:

1. **Assumptions callout** (autonomous mode only, when `assumptions[]` present)
2. **Executive summary / hook** — problem → outcome promise
3. **Understanding & context** — proves you read the brief and researched the client
4. **Proposed approach** — methodology mapped to requirements
5. **Scope & deliverables** — from templates + brief; acceptance criteria where scoping/RFP
6. **Evidence / case studies** — local matches first, web benchmarks second; cite sources
7. **Pricing & investment** — per `pricing.json`; include sanity-check narrative if strong
8. **Timeline** — phases/milestones aligned to scope
9. **Risk register** — table: Risk | Likelihood | Impact | Mitigation
10. **Team & credentials** — bios + about-us boilerplate
11. **Terms & conditions** — verbatim from `terms.md`
12. **Next steps / CTA** — clear, low-friction action

## Case study integration

From the research dossier:

- **Local matches** — lead with these. Format: Client (or anonymized) | Challenge | What we did | Outcome | Relevance to this brief.
- **Web evidence** — industry benchmarks, external examples. Always cite the source URL or dossier reference. Frame as "industry context" not "we did this."
- **Never invent** — if matches are thin, say so honestly and lean on approach + team credentials. Do not fabricate logos, metrics, or testimonials.

Pull reusable phrasing from `scope-templates.md` when deliverables overlap — adapt, don't paste blindly.

## Pricing presentation

Match `pricing.json.mode`:

| Mode | Pitch | RFP | Scoping |
|------|-------|-----|---------|
| `tiered` | Good/Better/Best cards; recommend middle tier | Table with tier comparison + line-item backup | Optional tiers as packages |
| `line-item` | Summarized total with expandable detail | Full line-item table with quantities/rates | Full breakdown with hours/roles |
| `value-based` | Outcome-value anchor before price | ROI framing + price | Value milestones tied to outcomes |

Include `calibrationNotes` and `sanityCheck` insights as a brief "investment rationale" paragraph — not raw JSON dump.

If `discountModeling` exists, note the recommended scenario in pricing narrative (not all scenarios — pick the strategic one).

## Objection pre-brief (woven, not bolted)

Identify 3–5 likely objections from brief + research signals:

| Signal | Likely objection | Weave into |
|--------|------------------|------------|
| Budget below scope | "Too expensive" | Pricing rationale + phased option |
| Aggressive timeline | "Can you hit the date?" | Timeline section + risk mitigations |
| No prior relationship | "Why you?" | Case studies + team credentials |
| Complex requirements | "Can you handle X?" | Approach + relevant proof |
| Incumbent vendor | "We already have someone" | Differentiators from competitive context |

Integrate answers into the relevant sections — a pitch weaves into approach and proof; an RFP addresses in compliance matrix rows; scoping doc addresses in assumptions and risk register.

## Risk register

Standard table for all types (expanded for RFP/scoping):

```markdown
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {risk from scope/research} | Low/Med/High | Low/Med/High | {specific mitigation} |
```

Seed risks from: brief constraints, tech stack complexity, timeline pressure, dependency on client inputs, third-party integrations, regulatory/compliance (RFP). Pitch type: top 3 only.

## Variations

Produce three markdown files from the same synthesis:

### `draft-v1.md` (standard)
Full proposal at the type template's default depth. This is the canonical draft.

### `draft-v1-short.md` (executive)
~1 page / 400–600 words. Hook, outcome promise, top proof point, pricing summary (recommended tier/total), CTA. Assumptions callout if autonomous. No T&Cs body — reference "full terms attached" or include abbreviated terms pointer.

### `draft-v1-long.md` (detailed)
Expanded proof (all case studies), full scope with acceptance criteria, complete risk register, expanded timeline with dependencies, full pricing detail including calibration notes. For RFP: full compliance matrix. For scoping: workshop/ discovery phases detailed.

## Bounded visuals (optional)

If visuals add value, load `references/visuals-bounds.md`. Save to `{run-folder}/visuals/` and reference in draft with relative paths. Skip if user declined or CRA handoff is preferred.

## Revision passes

When revising (user feedback or orchestrator check-in):

1. Read the prior `draft-v{N}.md` and feedback notes.
2. Increment version: `draft-v{N+1}.md` (+ short/long variants).
3. Do not delete prior versions.
4. Re-export `final-proposal.*` from the latest standard draft.

## Finalize

1. Write `draft-v1.md`, `draft-v1-short.md`, `draft-v1-long.md` to `{run-folder}/`.
2. Build `brand-snapshot.json` from `brand/identity.md` for the export script.
3. Run export per `references/export-and-styling.md` → `final-proposal.{html,md,pdf,docx}`.
4. Write `generation-summary.json`:

```json
{
  "run": "{slug}-{date}",
  "proposalType": "pitch|rfp|scoping",
  "language": "English",
  "draftVersion": 1,
  "sections": ["executive-summary", "approach", "..."],
  "exports": {"html": "...", "pdf": null},
  "warnings": ["research-dossier missing", "pandoc not found"],
  "assumptionsSurfaced": true,
  "visuals": ["visuals/hero.png"],
  "craHandoff": null
}
```

5. Append `[generation]` to daily log. Offer to curate new scope clauses to `scope-templates.md`.
