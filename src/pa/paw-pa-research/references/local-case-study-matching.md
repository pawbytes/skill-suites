# Local Case-Study Matching

Always loaded. Matches the seller's indexed portfolio to the current brief — the "we've done this" proof layer. Runs regardless of web-research mode.

## Inputs

- `{run-folder}/brief.md` — client, industry signals, requirements, deliverables, proposal type
- `{memory-root}/library/case-studies-index.json` — array of indexed case studies

If the index is empty or missing, tell the seller to run `paw-pa-library` or drop docs in `{memory-root}/library/inbox/`. Proceed with zero local matches; do not invent portfolio entries.

## Matching dimensions

Score each index entry against the brief on these axes (0–1 each, weighted):

| Dimension | Weight | Match signals |
| --------- | ------ | ------------- |
| Industry / vertical | 0.20 | Same or adjacent industry in brief vs entry |
| Service type | 0.25 | Overlap with `serviceType` and brief scope |
| Deliverables | 0.25 | Shared deliverables between `deliverables[]` and brief requirements |
| Outcome relevance | 0.15 | Outcome addresses the client's stated goal |
| Tags / keywords | 0.15 | Tag overlap with brief terms, tech, constraints |

**Relevance score** = weighted sum, rounded to two decimals (0.00–1.00). Include only entries scoring **≥ 0.35** unless fewer than three qualify — then include top 3 with explicit "weak match" note in highlights.

## Output shape (per match)

Add to findings JSON `localCaseStudyMatches[]`:

```json
{
  "id": "cs-001",
  "client": "Prior Client Co",
  "relevanceScore": 0.87,
  "matchReasons": ["Same industry: manufacturing", "Deliverable overlap: ERP integration"],
  "sourceDocPath": "library/inbox/prior-proposal.pdf",
  "highlights": "One sentence: outcome + why it matters for THIS client"
}
```

## Ranking rules

1. Sort by `relevanceScore` descending.
2. Cap at **5 matches** — quality over quantity.
3. Never paraphrase outcomes not present in the index entry; read `outcome` and `testimonial` verbatim or closely.
4. Every match must cite `sourceDocPath` from the index — traceability is mandatory.

## When index is sparse

If fewer than 2 entries score ≥ 0.35:

- State in findings `caveats`: "Thin local library — N indexed case studies; recommend paw-pa-library ingest."
- Still return whatever matches exist; pricing and generation will lean more on web evidence.

## Record as you match

Append matches to `{run-folder}/.research-findings-{date}.json` immediately after scoring — do not hold matches only in conversation memory.
