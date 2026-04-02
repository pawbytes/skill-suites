# Gap Identification

Find under-served opportunities in the market by systematically analyzing what's missing, broken, or underserved.

## Purpose

Identify opportunities where market needs are not being fully met by existing solutions. Produces an opportunity-gap report.

## Core Question

**Where is the market underserved, and how do we know?**

## Gap Types

### 1. Feature Gaps

**What to look for:** Features users expect but don't find

| Source | How to Identify |
|--------|-----------------|
| Feature requests | Product Hunt comments, competitor roadmaps |
| User reviews | "I wish it had...", "Missing..." |
| Support forums | What users ask about repeatedly |
| Competitor comparisons | Features present in some but not all |

**Analysis approach:**
1. List features across all competitors
2. Identify which features are: universal, common, rare, missing
3. Rare/missing features that users request = opportunity gaps

### 2. Audience Gaps

**What to look for:** Segments not being served or underserved

| Gap Type | How to Identify |
|----------|-----------------|
| Demographic gaps | Who's NOT in testimonials and case studies |
| Firmographic gaps | Company sizes, industries not mentioned |
| Use case gaps | Problems mentioned but no clear solution |
| Expertise gaps | Beginner vs. advanced user needs |

**Research approach:**
1. Analyze competitor positioning: Who do they target?
2. Analyze competitor testimonials: Who do they actually serve?
3. Identify segments missing from both
4. Validate: Do these segments exist and have the problem?

### 3. Positioning Gaps

**What to look for:** Angles and messaging not claimed

| Gap Type | Examples |
|----------|----------|
| Price positioning | No budget option, no premium option |
| Speed positioning | "Fast" not claimed by anyone |
| Simplicity positioning | All solutions are complex |
| Outcome positioning | Specific result not promised |
| Audience positioning | Specific segment not targeted |

**Analysis approach:**
1. Map competitor positioning statements on a grid
2. Identify empty spaces
3. Validate: Is the empty space viable?

### 4. Experience Gaps

**What to look for:** UX problems, friction points, unmet expectations

| Source | What to Capture |
|--------|-----------------|
| Negative reviews | Common complaints |
| Cancellations | Why people leave (if visible) |
| Support tickets | Recurring issues |
| Onboarding friction | Setup complexity |
| Integration gaps | Missing connections |

### 5. Value Gaps

**What to look for:** Price-to-value mismatches

| Gap Type | How to Identify |
|----------|-----------------|
| Overpriced segments | Complaints about price for specific use cases |
| Underpriced segments | High value, low price (opportunity for premium) |
| Bundling gaps | Features that should/shouldn't be bundled |
| Add-on gaps | Missing integrations, services, extras |

## Research Process

### Step 1: Competitor Feature Audit

Create a feature presence matrix:

```markdown
| Feature | Comp A | Comp B | Comp C | Comp D | Gap Score |
|---------|--------|--------|--------|--------|-----------|
| Feature 1 | Yes | Yes | Yes | Yes | 0 (saturated) |
| Feature 2 | Yes | Yes | No | No | 2 (gap) |
| Feature 3 | No | No | No | No | 4 (complete gap) |
```

**Gap Score:** Number of competitors WITHOUT the feature (higher = bigger gap)

### Step 2: User Pain Point Analysis

Aggregate complaints across sources:

```markdown
| Pain Point | Mentions | Sources | Severity | Validated |
|------------|----------|---------|----------|-----------|
| {Pain 1} | 47 | Reddit, G2 | High | Yes |
| {Pain 2} | 23 | Twitter, Reviews | Medium | Yes |
```

**Severity assessment:**
- High: Blocks task completion, causes churn
- Medium: Frustrating, workaround exists
- Low: Annoying, doesn't block usage

### Step 3: Audience Segmentation Analysis

Map who competitors serve:

```markdown
| Segment | Comp A | Comp B | Comp C | Served? |
|---------|--------|--------|--------|---------|
| Enterprise | Yes | Yes | Yes | Saturated |
| Mid-market | Yes | Yes | No | Moderate |
| Solo/Small | No | No | No | **Gap** |
| {Industry} | Yes | No | No | Moderate |
```

### Step 4: Positioning Map

Create a 2x2 positioning map:

```
                    Complex/Simple
                    ↑
          Comp A    |    Comp B
                   |
    Enterprise ----+---- SMB
                   |
          Comp C   |    [GAP]
                   |
                    ↓
                  Full-featured/Minimal
```

Identify empty quadrants and validate opportunity.

### Step 5: Prioritize Gaps

Score gaps by opportunity:

| Gap | Market Size | Competition | Fit | Effort | Score |
|-----|-------------|-------------|-----|--------|-------|
| Gap 1 | Large | Low | High | Medium | **8** |
| Gap 2 | Medium | Medium | High | Low | **7** |

**Scoring:**
- Market size: 1-3 (small/large)
- Competition: 1-3 (saturated/empty)
- Fit: 1-3 (low/high alignment with strengths)
- Effort: 3-1 (high/low effort — inverted)

## Output Format

### Opportunity-Gap Report

```markdown
# Opportunity Gap Analysis: {Product Category}

## Executive Summary
[1-2 sentences: Top 2-3 gaps identified with opportunity assessment]

## Gap Summary Table

| Gap | Type | Opportunity Score | Confidence |
|-----|------|-------------------|------------|
| {Gap 1} | Feature | 8/12 | HIGH |
| {Gap 2} | Audience | 7/12 | MED |
| {Gap 3} | Positioning | 6/12 | MED |

## Detailed Gap Analysis

### Gap 1: {Gap Name}

**Type:** {Feature/Audience/Positioning/Experience/Value}

**Description:** {What is missing or underserved}

**Evidence:**
- {Evidence point 1} `[Source]`
- {Evidence point 2} `[Source]`

**Market opportunity:**
- **Segment size:** {assessment} `[CONFIDENCE]`
- **Willingness to pay:** {assessment}
- **Competition:** {who addresses this, if anyone}

**Implementation considerations:**
- **Effort:** {low/medium/high}
- **Differentiation potential:** {assessment}
- **Risks:** {potential issues}

**Recommendation:** {specific action}

---

### Gap 2: {Gap Name}
[Same structure]

## Feature Gap Matrix

| Feature | Comp A | Comp B | Comp C | Gap Score |
|---------|--------|--------|--------|-----------|
| {Feature} | Yes | No | No | 2 |
| {Feature} | No | No | No | 3 |

## Audience Gap Analysis

| Segment | Served By | Gap Opportunity |
|---------|-----------|-----------------|
| {Segment 1} | {competitors} | {assessment} |
| {Segment 2} | None | **Clear gap** |

## Positioning Map

```
[ASCII visualization of positioning gaps]
```

## Prioritized Recommendations

### High Priority
1. **{Gap 1}** — {why this is priority 1}

### Medium Priority
2. **{Gap 2}** — {why this is priority 2}

### Lower Priority
3. **{Gap 3}** — {why deprioritized}

## Uncertainty Log

| Unknown | Impact | How to Validate |
|---------|--------|-----------------|
| {Unknown 1} | {impact} | {method} |

## Sources
- [Source 1](url) — accessed {date}
```

## Confidence Standards

| Gap Type | High Confidence | Medium Confidence |
|----------|-----------------|-------------------|
| Feature gap | Visible in product, mentioned in reviews | Inferred from absence |
| Audience gap | Segment mentioned in research | Inferred from omission |
| Positioning gap | Clear positioning statements | Inferred from messaging |
| Experience gap | Multiple complaint sources | Single source |

## Completion Criteria

Research is complete when:
- [ ] All 5 gap types examined
- [ ] At least 3 significant gaps identified
- [ ] Each gap has supporting evidence
- [ ] Gaps prioritized with reasoning
- [ ] Confidence levels assigned
- [ ] Uncertainty logged

## Common Pitfalls

- **Inventing gaps** — Gap must be supported by evidence, not assumption
- **Over-prioritizing easy gaps** — Small effort doesn't mean valuable
- **Ignoring competitor response** — If gap is real, competitors may fill it
- **Confusing niche with gap** — Small segment != underserved segment
- **Missing the "why"** — Gap exists for a reason; understand why

## Handoff

When gap analysis is complete:
1. Update `curated/market-intelligence.md` with gaps section
2. Save full analysis to `products/{slug}/research/opportunity-gaps.md`
3. Log activity in daily file
4. Recommend next step: research synthesis or strategist engagement