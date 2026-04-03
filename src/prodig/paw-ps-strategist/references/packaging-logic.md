# Packaging Logic

Recommend how the product should be structured and sold — turning product decisions into go-to-market decisions.

## Purpose

Define how to package, price, and position the product for market success. Packaging bridges product decisions with commercial viability.

## Required Inputs

| Input | Source | Purpose |
|-------|--------|---------|
| Product Brief | `curated/product-decisions.md` | Value proposition |
| Scope Map | `curated/product-decisions.md` | Feature set |
| Market Intelligence | `curated/market-intelligence.md` | Competitive pricing, market expectations |
| Audience Intelligence | `curated/audience-intelligence.md` | Willingness to pay, segment value |

## Packaging Framework

### 1. Value Metrics Analysis

Determine what users pay for:

**Value Metric Types:**

| Type | Definition | Examples |
|------|------------|----------|
| Usage-based | Pay for consumption | API calls, storage, seats |
| Feature-based | Pay for capability | Tiered features, modules |
| Outcome-based | Pay for results | Revenue share, savings |
| Flat-rate | Pay for access | Subscription, one-time |

**Selection Criteria:**
- What aligns with how users derive value?
- What is measurable and predictable?
- What matches market expectations?
- What supports growth?

### 2. Tier Structure Design

Define the package structure:

**Common Tier Models:**

| Model | Best For | Structure |
|-------|----------|-----------|
| Good/Better/Best | Most products | 3 tiers with clear upgrade path |
| Freemium | Growth products | Free tier + paid upgrade |
| Usage tiers | Usage-based products | Tiered by usage volume |
| Module-based | Complex products | Base + add-on modules |

**Tier Differentiation:**

For each tier, define:
- **Target segment:** Who is this tier for?
- **Value delivered:** What outcome does it enable?
- **Feature set:** What's included vs not?
- **Price point:** What's the target price range?
- **Upgrade trigger:** What drives users to higher tiers?

### 3. Pricing Strategy

Set pricing direction:

**Pricing Approaches:**

| Approach | When to Use |
|----------|-------------|
| Cost-plus | When costs are well-known and margins are standard |
| Competitive | When market has established price points |
| Value-based | When value is clear and differentiated |
| Penetration | When growth is prioritized over margin |
| Skimming | When differentiation is strong and early market |

**Pricing Factors:**

| Factor | Consideration |
|--------|---------------|
| Competitive landscape | What are alternatives priced at? |
| Value delivered | What is the worth of the outcome? |
| User segment | What can the target segment afford? |
| Business model | What margin does the business need? |
| Growth goals | Is the priority revenue or adoption? |

### 4. Positioning Clarity

Define how to position in the market:

**Positioning Framework:**

| Element | Definition |
|---------|------------|
| Category | What category do we compete in? |
| Alternative | What do people use instead? |
| Differentiation | What makes us different? |
| Proof | How do we prove our claims? |
| Audience | Who is our primary buyer? |

## Output: Packaging Recommendation

Produce a structured packaging document:

```markdown
# Packaging Recommendation: {Product Name}

## Executive Summary
One paragraph on recommended packaging approach.

## Value Metric
**Primary metric:** {metric}
**Rationale:** {why this metric aligns with value}

## Tier Structure

### Tier 1: {Name}
**Target:** {segment}
**Price:** {range}
**Value:** {outcome delivered}

| Includes | Excludes |
|----------|----------|
| {feature} | {feature} |

**Upgrade triggers:** {what drives upgrade}

### Tier 2: {Name}
**Target:** {segment}
**Price:** {range}
**Value:** {outcome delivered}

| Includes | Excludes |
|----------|----------|
| {feature} | {feature} |

**Upgrade triggers:** {what drives upgrade}

### Tier 3: {Name} (if applicable)
{same structure}

## Pricing Strategy
**Approach:** {approach name}
**Rationale:** {why this approach}

### Price Points
| Tier | Price | Competitive Context |
|------|-------|---------------------|
| {tier} | {price} | {vs competition} |

## Positioning Statement
**For** {target segment}
**Who** {need/problem}
**We are** {category}
**That** {differentiation}
**Unlike** {alternatives}
**We** {proof}

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {risk} | H/M/L | H/M/L | {mitigation} |

## Open Questions
1. {question to validate}
2. {question to validate}

## Recommendations
1. {immediate recommendation}
2. {follow-up recommendation}
```

## Process

1. Load product brief, scope map, and intelligence
2. Analyze value metrics
3. Design tier structure
4. Determine pricing strategy
5. Define positioning
6. Assess commercial risks
7. Produce packaging recommendation
8. Write to `curated/product-decisions.md`
9. Update `curated/product-context.md`
10. Log activity in daily file

## Quality Check

Before finalizing, verify:

- [ ] Value metric aligns with how users derive value
- [ ] Tiers have clear differentiation and upgrade paths
- [ ] Pricing is grounded in market and value context
- [ ] Positioning is specific and differentiated
- [ ] Commercial risks are identified and mitigated
- [ ] Recommendations are actionable