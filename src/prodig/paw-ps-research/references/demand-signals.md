# Demand Signal Analysis

Assess whether the market is alive, growing, and accessible. Identify signals that validate (or invalidate) market demand for a product concept.

## Purpose

Determine if there's genuine demand for a product idea before investing in development. Produces a demand signal summary with confidence levels.

## Core Question

**Is the market alive, and how do we know?**

## Input Requirements

Gather from conversation or product context:
- Product concept or category
- Target audience hypothesis
- Geographic scope
- Time frame (when would this launch?)

## Signal Categories

### 1. Search Demand

**What it tells us:** Active interest and problem-seeking behavior

| Metric | Tool | What to Look For |
|--------|------|------------------|
| Search volume | Google Trends, Keyword tools | Volume, trend direction |
| Related queries | Google Trends | What else they search |
| Search intent | Manual analysis | Informational vs. commercial |
| Seasonality | Google Trends (12mo view) | Peaks and troughs |

**Interpretation:**
- High volume + growing = strong signal
- High volume + declining = market may be maturing
- Low volume + growing = emerging opportunity
- Low volume + flat = weak or niche market

### 2. Social Signals

**What it tells us:** Conversations, sentiment, unmet needs

| Source | What to Analyze |
|--------|-----------------|
| Reddit | Subreddit activity, common questions, complaints |
| Twitter/X | Hashtag volume, sentiment, influencer mentions |
| LinkedIn | Professional discussions, job postings |
| YouTube | Video count, views, comments |
| TikTok | Trending topics, engagement |

**Research commands:**
```
Exa search: "site:reddit.com {problem}" OR "{product category}"
Exa search: "{product category}" complaints problems issues
```

**What to capture:**
- Volume of discussion (how many people talking)
- Sentiment (positive/negative/neutral)
- Common pain points (what problems are mentioned repeatedly)
- Solutions mentioned (what are they using now)

### 3. Marketplace Activity

**What it tells us:** Commercial viability and pricing benchmarks

| Platform | What to Check |
|----------|---------------|
| Product Hunt | Launches, upvotes, comments in category |
| App stores | Number of apps, ratings, reviews |
| Amazon | Products, reviews, bestsellers |
| Gumroad/Etsy | Digital products, sales estimates |
| SaaS directories | G2, Capterra listings and reviews |

**Key metrics:**
- Number of products in category (saturation)
- Review counts (activity level)
- Rating distributions (satisfaction)
- Pricing ranges (willingness to pay)

### 4. Competitor Traction

**What it tells us:** Market validation from existing players

| Signal | Source | Interpretation |
|--------|--------|----------------|
| Funding raised | Crunchbase, TechCrunch | Investor confidence |
| Headcount growth | LinkedIn | Company health |
| Traffic trends | SimilarWeb | Market interest |
| Customer growth | Case studies | Real adoption |

### 5. Intent Signals

**What it tells us:** Purchase readiness and decision criteria

| Signal | Source |
|--------|--------|
| "Alternative to X" searches | Google, G2 comparisons |
| Pricing page traffic | SimilarWeb (if available) |
| Review velocity | G2, Capterra review dates |
| Job postings | LinkedIn (hiring = growth) |

## Research Process

### Step 1: Define Search Terms

Generate search variations:
```
Core terms: "{product category}", "{problem}", "{solution type}"
Modifier terms: "best", "how to", "alternative", "vs", "review", "comparison"
Audience terms: "{audience} {product}", "{job title} {problem}"
```

### Step 2: Gather Signals

Run searches in order of signal strength:

1. **Search demand** (Google Trends, keyword data)
2. **Social signals** (Reddit, Twitter, YouTube)
3. **Marketplace activity** (Product Hunt, app stores)
4. **Competitor traction** (funding, traffic, growth)
5. **Intent signals** (comparison searches, reviews)

### Step 3: Score Signals

Rate each signal category:

| Category | Score (1-5) | Evidence |
|----------|-------------|----------|
| Search demand | | |
| Social signals | | |
| Marketplace activity | | |
| Competitor traction | | |
| Intent signals | | |

**Scoring guide:**
- 5 = Strong positive signal (high volume, growing, positive sentiment)
- 3 = Mixed signal (moderate activity, unclear trend)
- 1 = Weak or negative signal (low volume, declining, negative sentiment)

### Step 4: Synthesize Demand Assessment

Calculate overall demand signal:

**Strong Demand:** 4+ average, multiple strong signals
**Moderate Demand:** 3-3.9 average, mixed signals
**Weak Demand:** <3 average, few positive signals

## Output Format

### Demand Signal Summary

```markdown
# Demand Signal Analysis: {Product Concept}

## Executive Summary
[1-2 sentences: Is demand strong/moderate/weak? Key signal.]

## Demand Scorecard

| Signal Category | Score | Key Evidence |
|-----------------|-------|--------------|
| Search demand | X/5 | {evidence summary} |
| Social signals | X/5 | {evidence summary} |
| Marketplace activity | X/5 | {evidence summary} |
| Competitor traction | X/5 | {evidence summary} |
| Intent signals | X/5 | {evidence summary} |
| **Overall** | **X/5** | |

## Detailed Findings

### Search Demand
- **Volume:** {volume assessment} `[CONFIDENCE]`
- **Trend:** {direction} over {timeframe}
- **Top queries:** {list}
- **Intent:** {informational/commercial/transactional}

### Social Signals
- **Discussion volume:** {assessment}
- **Common themes:** {themes}
- **Pain points mentioned:**
  1. {pain point 1}
  2. {pain point 2}
- **Sentiment:** {overall sentiment}

### Marketplace Activity
- **Products found:** {count}
- **Average rating:** {rating}
- **Price range:** {range}
- **Saturation level:** {low/medium/high}

### Competitor Traction
- **Funded competitors:** {count}
- **Average traffic estimate:** {range}
- **Growth trend:** {assessment}

### Intent Signals
- **"Alternative to" searches:** {assessment}
- **Review velocity:** {assessment}
- **Purchase intent indicators:** {list}

## Demand Verdict

**Overall assessment:** {Strong/Moderate/Weak} demand

**Supporting evidence:**
- {Evidence point 1}
- {Evidence point 2}

**Contradicting evidence:**
- {Counter-evidence 1}

**Confidence:** {HIGH/MED/LOW}

## Recommendations

- **If strong:** Proceed with confidence; focus on differentiation
- **If moderate:** Validate with audience research; test positioning
- **If weak:** Reconsider concept or pivot to adjacent opportunity

## Sources
- [Source 1](url) — accessed {date}
- [Source 2](url) — accessed {date}

## Uncertainty Log

| What We Don't Know | Why It Matters | How to Learn |
|--------------------|----------------|--------------|
| {unknown 1} | {impact} | {method} |
```

## Confidence Standards

| Signal Type | Strong Evidence | Weak Evidence |
|-------------|-----------------|---------------|
| Search volume | 2+ tools agreeing | Single tool estimate |
| Social sentiment | 50+ data points | <20 data points |
| Market size | Multiple reports | Single report or proxy |
| Competitor traction | Verified data | Estimated data |

## Completion Criteria

Research is complete when:
- [ ] All 5 signal categories scored
- [ ] At least 3 sources per category (where possible)
- [ ] Confidence levels assigned
- [ ] Overall demand verdict rendered
- [ ] Uncertainty log populated
- [ ] Recommendations tied to findings

## Common Pitfalls

- **Cherry-picking signals** — Report all signals, not just positive ones
- **Ignoring negative signals** — Declining trends are valuable data
- **Over-weighting single signals** — Look for convergence across categories
- **Confusing interest with demand** — Searches != purchases
- **Ignoring timing** — Seasonality can skew interpretation

## Handoff

When demand analysis is complete:
1. Update `curated/market-intelligence.md` with demand section
2. Save full analysis to `products/{slug}/research/demand-signals.md`
3. Log activity in daily file
4. Recommend next step: gap identification or audience validation