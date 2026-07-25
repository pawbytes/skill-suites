# Proposal Type Detection

`proposalType` selects downstream section emphasis, tone, and pricing presentation. Intake must set it explicitly — detect from content, confirm with seller when uncertain, or default from config with assumption flagged.

## Valid values

| Value | When to use |
| ----- | ----------- |
| `pitch` | Pre-sale — win new work; problem → approach → proof → pricing → CTA |
| `rfp` | Formal tender/RFP response; compliance matrix, structured Q&A, risk register emphasis |
| `scoping` | Post-yes project plan; milestones, deliverables, assumptions, timeline detail |

## Detection signals

Score each type from source text/transcript. Highest score wins unless seller overrides.

### pitch signals (+)

- "proposal", "quote", "estimate", "pitch", "win the work", "send a proposal"
- Pre-contract language: "interested in working with", "looking for a partner"
- Budget exploration without formal RFP structure
- Sales-call or discovery-call tone

### rfp signals (+)

- "RFP", "RFQ", "tender", "bid", "submission deadline", "compliance", "mandatory requirements"
- Numbered requirements, evaluation criteria, submission format instructions
- "respond to section", "attachment B", "scoring matrix"
- Formal procurement language

### scoping signals (+)

- "SOW", "statement of work", "project plan", "scope document", "already approved", "kickoff"
- Post-award: "we've decided to move forward", "need a scoping doc"
- Milestone/phases already agreed; needs detail not persuasion
- Internal stakeholder alignment doc

## Decision flow

```
1. Seller explicitly stated type? → use it (no assumption)
2. Run signal scoring on source text
3. Clear winner (≥2 more signals than runner-up)? → set type, note confidence in intake summary
4. Tie or weak signal? → use default_proposal_type from config
5. Always: if inferred (steps 3–4), add assumptions[] entry
```

## Confidence levels

Record in `.intake-summary.json` (optional `typeDetection` block):

| Confidence | Meaning |
| ---------- | ------- |
| `explicit` | Seller stated type |
| `high` | Strong signal match (≥3 unique signals for winner) |
| `medium` | Winner by 1–2 signals |
| `low` | Default applied — source ambiguous |

## Guided confirmation

When confidence is `medium` or `low`, ask once:

> "This reads like a **{detected}** proposal ({reason}). Confirm, or say pitch / rfp / scoping."

Do not block on answer — if user ignores, proceed with detected type and note in assumptions.

## Headless behavior

Use signal scoring + `default_proposal_type` fallback. Always include in assumptions when not explicit:

```markdown
- proposalType set to rfp (inferred from "submission deadline" and numbered requirements)
```

## Examples

| Source excerpt | Detected type | Reason |
| -------------- | ------------- | ------ |
| "Can you send us a proposal for the Shopify rebuild by Friday?" | `pitch` | Pre-sale quote request |
| "Please respond to Attachment A requirements by March 15. Late submissions rejected." | `rfp` | Formal tender language |
| "We've signed the MSA — need a detailed SOW for Phase 1 kickoff next week." | `scoping` | Post-award scope doc |
| "They want something written up about the project." | `pitch` (default) | Ambiguous → config default + assumption |

## Downstream impact (inform seller when confirming)

| Type | Research emphasis | Pricing style | Generation template |
| ---- | ----------------- | ------------- | ------------------- |
| `pitch` | Proof + differentiation | Tiered packages common | `section-templates-pitch.md` |
| `rfp` | Compliance + benchmarks | Line-item / milestone | `section-templates-rfp.md` |
| `scoping` | Prior work + tech detail | Milestone line-items | `section-templates-scoping.md` |

Type is stored in frontmatter — generation reads `proposalType` directly; no re-detection downstream.
