# Brief Schema (`brief.md`)

Every intake run writes `{run-folder}/brief.md`. Downstream skills parse the YAML frontmatter; humans read the markdown body.

## File format

```markdown
---
# === Required contract fields (memory plan) ===
clientName: "Acme Corp"
clientContext: "Series B fintech; 120 employees; prior vendor churn on mobile app"
proposalType: pitch          # pitch | rfp | scoping
proposalTypeConfidence: high # high | medium | low
proposalTypeDetectionNotes: "Sales call transcript; buyer asked for 'a proposal to win the redesign'"

projectDescription: |
  Multi-paragraph narrative of the work, problem, and desired outcome.
budget: "$80k–$120k fixed"    # string — preserve client's phrasing; null if unknown
timeline: "Kickoff April; MVP in 12 weeks"
requirements:
  - "Native iOS + Android from shared codebase"
  - "SOC 2–aligned auth flow"
constraints:
  - "Must integrate with existing Stripe billing"
  - "No offshore team per procurement"
decisionMaker: "Jordan Lee, VP Product"
sourceInputRef: "text:inline"  # path, URL, or text:inline | text:file:{path}
language: "English"

# === Intake metadata ===
intakeDate: "2026-07-03"
intakeMode: guided             # guided | autonomous
inputType: text                # text | audio | video | url

# === Completeness (always populated) ===
completenessReport:
  score: 0.85                  # 0.0–1.0
  readyForPipeline: true
  gaps:
    - field: budget
      severity: medium
      message: "Budget range not stated; needed for pricing calibration"
      resolved: false

# === Autonomous mode only — explicit assumptions for gaps ===
assumptions: []
# Example entry:
# - field: budget
#   assumedValue: "$100k fixed (mid-market mobile rebuild)"
#   rationale: "No figure in transcript; inferred from scope size and 'enterprise' mention"

# === Optional enrichment (extract when present) ===
industry: "Fintech"
companySize: "120 employees"
competitorsMentioned: []
deliverables: []
milestones: []
successCriteria: []
complianceRequirements: []     # emphasize for rfp
stakeholders: []
urgency: ""
---
# Brief: {clientName}

## Problem & context
{Expanded narrative for humans — not a transcript dump.}

## Scope summary
{Bulleted scope in plain language.}

## Open questions
{Items still unclear after intake — mirrors unresolved gaps in guided mode.}
```

## Field reference

| Field | Type | Required for pipeline | Notes |
|-------|------|----------------------|-------|
| `clientName` | string | **yes** | Company or contact name; slug source for run folder |
| `clientContext` | string | recommended | Industry, size, relationship, prior work |
| `proposalType` | enum | **yes** | `pitch` \| `rfp` \| `scoping` |
| `projectDescription` | string | **yes** | Core problem + desired outcome |
| `budget` | string \| null | recommended | Exact phrasing from source; gap if missing for pricing |
| `timeline` | string \| null | recommended | Dates, duration, or deadlines |
| `requirements` | string[] | **yes** (≥1) | Testable needs from the client |
| `constraints` | string[] | optional | Technical, legal, procurement limits |
| `decisionMaker` | string \| null | recommended | Who signs / owns the decision |
| `sourceInputRef` | string | **yes** | Traceability to original input |
| `assumptions` | object[] | autonomous gaps | `{field, assumedValue, rationale}` |
| `completenessReport` | object | **yes** | Always include `score`, `gaps`, `readyForPipeline` |

### Optional enrichment

Extract when the source mentions them: `industry`, `companySize`, `deliverables`, `milestones`, `successCriteria`, `complianceRequirements` (critical for `rfp`), `stakeholders`, `urgency`, `competitorsMentioned`.

## Proposal type detection

| Type | Signals | Extraction priority |
|------|---------|---------------------|
| **pitch** | "proposal to win", pre-sale, capabilities deck, "send us a quote", discovery call | Problem, outcome, differentiation, budget range |
| **rfp** | RFP, tender, compliance matrix, evaluation criteria, submission deadline, mandatory requirements | `requirements[]`, `complianceRequirements[]`, deadlines, format constraints |
| **scoping** | SOW, statement of work, post-award, "we've signed", milestones, deliverables list | `deliverables[]`, `milestones[]`, acceptance criteria, timeline |

**Confidence rules:**

- **high** — explicit type stated OR ≥3 strong signals for one type
- **medium** — mixed signals but one type dominates
- **low** — vague "need a document" with no type signals → use `default_proposal_type`, note in `proposalTypeDetectionNotes`

Interactive: confirm when `low`. Headless: apply `default_proposal_type`.

## Extraction guidelines

1. **Quote sparingly** — use client phrasing in `requirements[]`; paraphrase in `projectDescription`.
2. **One requirement per bullet** — split compound sentences.
3. **Budget** — capture ranges, caps, "TBD", currency; never convert to a number unless explicitly stated.
4. **Timeline** — include hard deadlines (RFP) and soft targets (pitch).
5. **Do not copy** the full transcript into `projectDescription` — synthesize 2–4 paragraphs max.

## `sourceInputRef` values

| Pattern | When |
|---------|------|
| `text:inline` | Pasted in chat |
| `text:file:{absolute-or-project-path}` | Read from file |
| `audio:{path}` | Local audio transcribed |
| `video:{path}` | Local video transcribed |
| `url:{https://...}` | Remote media URL |

## Validation before write

- `clientName` non-empty
- `proposalType` valid enum
- `requirements` has at least one item (or a gap + assumption)
- `completenessReport` present with computed `score`
- YAML parses cleanly (quote strings with colons)
