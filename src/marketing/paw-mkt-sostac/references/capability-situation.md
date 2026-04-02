# Capability: Situation Analysis

**Outcome:** Deliver a comprehensive "Where are we now?" assessment with evidence-based findings and strategic implications.

**Output:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/01-situation.md`

**Phase Question:** "Where are we now?"

## Frameworks Applied

Load from `./references/frameworks-index.csv` (filter: `sostac_phase=Situation`):
- SWOT + TOWS
- PESTLE
- Porter's Five Forces
- TAM/SAM/SOM
- Jobs-to-be-Done
- 5S Digital Baseline

## Research Work

Using auto-discovery data + user context:

### 1. Draft the SWOT from Evidence
- Strengths from reviews and product quality
- Weaknesses from customer complaints and gaps
- Opportunities from market trends and competitor weaknesses
- Threats from competitive moves and market shifts

**Use actual evidence, not generic statements.**

### 2. Generate TOWS Strategic Options
Cross strengths with opportunities, strengths with threats, etc. Present 2-3 concrete strategic directions with reasoning.

### 3. Run the PESTLE Scan
Research regulatory changes, economic trends, technology shifts, social trends. Present only factors affecting the business in the next 18 months.

### 4. Assess Porter's Five Forces
Rate each force from competitive research. Highlight the 1-2 forces that matter most.

### 5. Estimate TAM/SAM/SOM
Use available data to build bottom-up estimate. Present as a range.

### 6. Build the JTBD Profile
Extract from customer reviews, Reddit, Quora. Present functional, emotional, and social jobs in customer's own language.

### 7. Score the 5S Digital Baseline
Estimate current performance across Sell, Serve, Speak, Save, Sizzle.

## Presentation Format

Share complete Situation Analysis draft with:
- Executive summary of 5-8 most important findings
- Each framework section with analysis and evidence
- "Strategic Implications" section connecting findings to plan priorities
- Highlighted areas needing user confirmation

## Validation Questions (Targeted Only)

Ask only what research cannot determine:
- Internal metrics (actual conversion rates, revenue breakdown, team size)
- Strategic intent (upcoming product changes, fundraising, expansion)
- Corrections to estimates ("I estimated X — is that close?")

## Output Template

```markdown
## Executive Summary
(5-8 bullets: most important findings that shape the entire plan)

## Business Overview
(Product/Service, Revenue Model, Stage, Team, Budget)

## Digital Performance Baseline (5S Model)
| S | Metric | Current Value | Target |

## SWOT Analysis
### Strengths / Weaknesses / Opportunities / Threats
(Each with specific evidence, not assertions)

## TOWS Strategic Options
(SO, ST, WO, WT combinations — 2-3 named strategic directions)

## PESTLE Scan
| Factor | Observation | Implication | Urgency |

## Porter's Five Forces Summary
| Force | Rating (H/M/L) | Key Drivers | Strategic Response |

## Market Sizing (TAM/SAM/SOM)
| Level | Conservative | Base | Optimistic | Method |

## Customer JTBD Profile
(Functional job, emotional job, social job — in customer language)

## Competitor Landscape
| Competitor | Positioning | Strengths | Weaknesses | Key Channels | Vulnerability |

## Technology Stack

## Key Insights and Strategic Implications
(5-8 bullets that directly shape Objectives and Strategy phases)
```

## Success Criteria

- Every SWOT entry has specific evidence
- TOWS produces actionable strategic options
- PESTLE focuses on relevant near-term factors
- Porter highlights the forces that actually matter
- JTBD uses customer language from research
- Strategic implications connect to actionable next steps