# Competitor Analysis

Systematic analysis of the competitive landscape to understand market positioning, strengths, weaknesses, and opportunities.

## Purpose

Understand the market landscape to inform positioning, differentiation, and gap strategy. Produces a competitor matrix or HTML report.

## Input Requirements

Gather from conversation or product context:
- Product category or market segment
- Known competitors (if any)
- Geographic scope
- Specific aspects to analyze (pricing, features, positioning, audience)

## Research Process

### Step 1: Competitor Identification

**If competitors provided:** Validate and expand the list

**If no competitors known:** Discover through:
- Exa search: `"{product category}" competitors alternatives`
- Review sites: G2, Capterra, Product Hunt
- Industry directories and rankings
- Search: `"top {category}" tools software`

**Target count:** 5-10 direct competitors, 2-3 indirect

### Step 2: Data Collection Framework

For each competitor, gather:

| Category | Data Points | Sources |
|----------|-------------|---------|
| Positioning | Value prop, target audience, brand messaging | Homepage, about page |
| Pricing | Tiers, price points, free trial, discounts | Pricing page |
| Features | Core features, differentiators, gaps | Product page, feature comparison |
| Audience | Who they target, testimonials, case studies | Customer stories, reviews |
| Strengths | What they do well, positive reviews | G2/Capterra, testimonials |
| Weaknesses | Complaints, gaps, negative reviews | Reviews, forums, social |
| Market presence | Traffic, funding, company size | SimilarWeb, Crunchbase, LinkedIn |

### Step 3: Analysis Framework

Apply competitive analysis frameworks:

**SWOT Analysis (per competitor):**
```markdown
## {Competitor Name}
### Strengths
- {What they do well}

### Weaknesses
- {Where they struggle}

### Opportunities (for us)
- {Gaps we could fill}

### Threats (to us)
- {Their advantages we'd compete with}
```

**Competitive Positioning Matrix:**
- X-axis: Price (low to high)
- Y-axis: Feature completeness (basic to advanced)
- Plot each competitor and identify clusters

**Feature Comparison Table:**

| Feature | Us | Comp A | Comp B | Comp C |
|---------|-----|--------|--------|--------|
| Feature 1 | ? | Yes | Yes | No |
| Feature 2 | ? | Yes | No | Yes |

### Step 4: Synthesize Findings

Organize into:
1. **Market overview** — Size, growth, trends
2. **Competitive landscape** — Key players and positioning
3. **Common patterns** — What everyone does
4. **Differentiation opportunities** — Where no one plays
5. **Threat assessment** — What to watch

## Output Format

### Competitor Matrix (Markdown)

```markdown
# Competitor Analysis: {Product Category}

## Executive Summary
[2-3 sentences on market landscape and key insight]

## Market Overview
- **Market size:** {size} `[CONFIDENCE]`
- **Growth trend:** {trend}
- **Key players:** {count} significant competitors

## Competitor Profiles

### {Competitor 1}
| Aspect | Details |
|--------|---------|
| Positioning | {one-line value prop} |
| Target audience | {who they serve} |
| Pricing | {price range} |
| Key features | {top 3-5 features} |
| Strengths | {what they do well} |
| Weaknesses | {gaps or complaints} |

### {Competitor 2}
[Same structure]

## Feature Comparison Matrix

| Feature | {Comp A} | {Comp B} | {Comp C} | {Comp D} |
|---------|----------|----------|----------|----------|
| {Feature 1} | Yes | Yes | No | Yes |
| {Feature 2} | Yes | No | Yes | No |

## Market Gaps Identified

1. **{Gap 1}** — {description} `[OPPORTUNITY]`
2. **{Gap 2}** — {description} `[OPPORTUNITY]`

## Positioning Recommendations

Based on competitive analysis:
- **Differentiation angle:** {recommendation}
- **Avoid:** {saturated positioning}
- **Opportunity:** {underserved segment}

## Sources
- [Source 1](url) — accessed {date}
- [Source 2](url) — accessed {date}

## Confidence Assessment

| Finding | Confidence | Reasoning |
|---------|------------|-----------|
| Pricing data | HIGH | Verified on pricing pages |
| Feature comparison | MED | Based on public info, may be outdated |
| Market gaps | LOW | Inferred from absence, needs validation |
```

### HTML Report (Optional)

For presentations, generate an HTML competitor matrix with:
- Visual positioning chart
- Feature comparison grid
- Expandable competitor cards

## Confidence Standards

| Data Type | Minimum Sources | Confidence |
|-----------|-----------------|------------|
| Pricing | 1 (official page) | HIGH |
| Features | 1-2 (official + reviews) | MED-HIGH |
| Market size | 2+ independent | MED |
| User sentiment | 20+ reviews | MED |
| Company info | 1 (official) | HIGH |

## Completion Criteria

Research is complete when:
- [ ] At least 5 competitors analyzed with full profiles
- [ ] Feature comparison matrix complete
- [ ] Market gaps identified with opportunity assessment
- [ ] All sources cited with access dates
- [ ] Confidence levels assigned to all key findings

## Quality Standards

- Cite all sources with URLs and access dates
- Distinguish between verified facts and inferences
- Note data currency (when information was gathered)
- Flag any information that couldn't be verified
- Include both positive and negative findings

## Common Pitfalls

- **Over-researching** — Know when to stop; 80% confidence is often enough
- **Confirmation bias** — Look for disconfirming evidence
- **Outdated data** — Check dates on sources; note if >6 months old
- **Feature bloat** — Focus on features that matter to target audience
- **Ignoring indirect competitors** — Sometimes the biggest threat isn't direct

## Handoff

When competitor analysis is complete:
1. Update `curated/market-intelligence.md` with summary
2. Save detailed matrix to `products/{slug}/research/competitor-matrix.md`
3. Log activity in daily file
4. Recommend next step: gap identification or demand signal analysis