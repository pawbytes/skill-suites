# Competitor Research

Analyze competitor content, positioning, and market gaps using proven frameworks.

**Key Methodologies:** SWOT Analysis, Porter's Five Forces, Strategic Group Analysis, Perceptual Mapping, Competitive Profile Matrix. Load `./methodologies.md` for detailed framework templates.

## Input

Gather from conversation or brand context:
- Brand name and industry
- Known competitors (if any)
- Research scope (broad scan vs. specific competitors)
- Focus areas (content types, platforms, messaging)

## Research Process

### Step 1: Select Framework

Before diving in, choose the right tool:

| Situation | Framework |
|-----------|-----------|
| Fast competitive overview | SWOT Analysis |
| Entering a new market | Porter's Five Forces |
| Too many competitors | Strategic Group Analysis |
| Repositioning brand | Perceptual Mapping |
| Quantitative comparison | Competitive Profile Matrix |

### Step 2: Gather Competitor Data

**Identify competitors** (if not provided):
- Search "{industry} brands similar to {brand}"
- Use Exa `web_search_exa` for discovery
- Check industry directories and rankings

**Analyze using appropriate tools:**

| Content Type | Tool |
|--------------|------|
| Public websites, articles, press | Exa `crawling_exa` |
| Social profiles (LinkedIn, Instagram, TikTok) | Agent-browser with auth |
| Gated/membership content | Agent-browser with auth |

See `./browser-tools.md` for authentication setup.

### Step 3: Apply Framework & Synthesize

Use the selected framework from `./methodologies.md` to structure analysis. Focus on:
- Positioning (how competitors differentiate)
- Content gaps (what's missing in the market)
- Opportunity areas (where to compete)

## Output

Create `{brand-name}/research/competitor-analysis.md`:

```markdown
# Competitor Analysis: {Brand}
## Executive Summary
## Competitor Profiles
### {Competitor 1}
- Positioning
- Content strategy
- Strengths
- Weaknesses

### {Competitor 2}
...

## Market Gaps
- Gap 1: {description}
- Gap 2: {description}

## Recommendations
- Opportunity 1: {specific action}
- Opportunity 2: {specific action}

## Sources
- [Source 1](url)
- [Source 2](url)
```

## Completion Criteria

Research is complete when:
- [ ] At least 3 competitors analyzed with full profiles
- [ ] Market gaps identified with specific opportunity descriptions
- [ ] All sources cited with URLs
- [ ] Actionable recommendations tied to brand strengths

## Quality Standard

- Cite all sources with URLs
- Focus on actionable insights, not just observations
- Highlight gaps that align with brand strengths
- Recommend specific content opportunities