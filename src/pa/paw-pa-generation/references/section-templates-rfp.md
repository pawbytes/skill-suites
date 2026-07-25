# Section Templates — RFP Response

Type: `rfp` — formal tender/RFP response. Tone: precise, compliance-oriented, evidence-backed. Evaluators score against requirements — every requirement gets a traceable answer.

## Section order

1. Assumptions callout (autonomous only)
2. **Cover / submission summary** — RFP reference, client, date, contact
3. **Executive summary** — compliance statement + win theme (3–5 bullets)
4. **Understanding of requirements** — structured recap of RFP scope
5. **Compliance matrix** — Requirement | Response | Reference (section/page)
6. **Technical approach** — methodology mapped to each requirement category
7. **Project plan & timeline** — phases, milestones, dependencies, client inputs needed
8. **Team & qualifications** — bios, roles, relevant certifications
9. **Case studies & references** — local matches + cited web benchmarks; formatted for evaluator scanning
10. **Pricing** — line-item table preferred; milestone billing; no hidden costs statement
11. **Risk register** — full matrix (5+ risks)
12. **Quality assurance & governance** — how work is reviewed and accepted
13. **Terms & conditions** — verbatim from `terms.md` (RFP/large-deal variant if present)
14. **Appendices** — optional: detailed resumes, additional case studies, visuals

## Tone notes

- Formal but not stiff — clarity beats jargon.
- Every claim in proof sections must trace to dossier evidence.
- Compliance matrix is non-negotiable for RFP — evaluators use it to score.
- Pricing: transparent line items; note what's excluded vs included.
- Objection weaving: address "incumbent advantage" and "price sensitivity" in executive summary and pricing rationale.

## Compliance matrix format

```markdown
## Compliance matrix

| # | Requirement (from RFP) | Compliant | Response summary | Reference |
|---|------------------------|-----------|------------------|-----------|
| 1 | {req from brief} | Yes / Partial / N/A | {how we meet it} | § Technical Approach |
| 2 | … | … | … | … |
```

Populate from `brief.md` `requirements[]`. Mark Partial with mitigation plan.

## Template skeleton

```markdown
# Response to RFP — {RFP title/reference}

**Submitted to:** {client name}
**Date:** {date}
**Contact:** {seller contact from bios}

> **Assumptions** *(autonomous mode only)*
> - {assumption}

## Executive summary

**Win theme:** {one sentence — why we're the right fit}

- {Key differentiator 1}
- {Key differentiator 2}
- {Compliance highlight}
- {Pricing summary — total, model}
- {Timeline summary}

## Understanding of requirements
{Structured recap — group by category from brief.}

## Compliance matrix
{Full matrix table — see format above.}

## Technical approach

### {Category 1 — e.g., Discovery}
{Methodology, tools, deliverables — maps to requirements 1–N.}

### {Category 2 — e.g., Implementation}
…

## Project plan & timeline

| Phase | Start | End | Deliverables | Client dependencies |
|-------|-------|-----|--------------|---------------------|
| … | … | … | … | … |

## Team & qualifications

| Role | Name | Relevant experience |
|------|------|---------------------|
| … | … | … |

{Bios from boilerplate — expanded.}

## Case studies & references

### {Case study 1 — local}
| Field | Detail |
|-------|--------|
| Client | … |
| Scope | … |
| Outcome | … |
| Reference | … |

### Industry context
{Web benchmarks from dossier — cited.}

## Pricing

| Line item | Qty | Rate | Total |
|-----------|-----|------|-------|
| … | … | … | … |

**Total investment:** {total}
**Payment terms:** {from terms.md or pricing.json}
**Exclusions:** {explicit list}

## Risk register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| … | … | … | … | … |

## Quality assurance
{Review gates, acceptance criteria, change control.}

## Terms & conditions
{Verbatim from brand/boilerplate/terms.md}

## Appendices
- A: Detailed team resumes
- B: Additional case studies
- C: {Visuals from visuals/ folder if any}
```

## Short variation (`draft-v1-short.md`)

Executive summary + compliance matrix summary (top requirements only) + pricing total + contact. For evaluator pre-read.

## Long variation (`draft-v1-long.md`)

Full compliance matrix (every requirement), expanded technical approach per category, complete case studies, full pricing with calibration notes, appendices with resumes and diagrams.
