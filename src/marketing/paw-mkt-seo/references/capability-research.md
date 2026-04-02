# Research Mode (Live Competitive Intelligence) Capability

## Overview
Gather live SEO data using browser automation for SERP analysis, competitor intelligence, and technical audits. Use when current positions, competitor rankings, or live metrics are needed.

## When to Use
- Current SERP position checking
- Competitor ranking analysis
- Core Web Vitals testing
- Schema validation
- Rich results eligibility
- Index status verification
- Keyword research expansion

## Prerequisites

**Setup**: See `./references/shared-patterns.md` for `agent-browser` installation instructions.

If `agent-browser` is unavailable, use `WebFetch` and `WebSearch` tools as alternatives.

## Capability Workflow

### 1. Google SERP Analysis

```bash
# Check current rankings for target keywords
agent-browser --session seo-research open "https://www.google.com/search?q={target-keyword}" && agent-browser wait --load networkidle
agent-browser get text body
# Look for: brand's position, featured snippets owned, PAA questions, competitors visible

# Check AI Overview presence
agent-browser screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/seo/serp-{keyword}.png
```

### 2. Competitor Organic Intelligence (SimilarWeb free)

```bash
agent-browser --session seo-research open "https://www.similarweb.com/website/{competitor-domain}/#overview" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
# Extract: monthly visits, organic search %, top organic keywords (if visible)
```

### 3. PageSpeed Insights / Core Web Vitals

```bash
agent-browser --session seo-research open "https://pagespeed.web.dev/report?url=https://{domain}" && agent-browser wait --load networkidle && agent-browser wait 8000
agent-browser get text body
# Extract: LCP, INP, CLS scores, opportunities list
```

### 4. Schema Markup Check

```bash
agent-browser --session seo-research open "https://validator.schema.org/#url=https://{domain}" && agent-browser wait --load networkidle && agent-browser wait 5000
agent-browser get text body
# Extract: detected schema types, errors, warnings
```

### 5. Rich Results Test

```bash
agent-browser --session seo-research open "https://search.google.com/test/rich-results?url=https://{page-url}" && agent-browser wait --load networkidle && agent-browser wait 5000
agent-browser get text body
# Extract: rich result eligibility, detected structured data
```

### 6. Google Index Check

```bash
agent-browser --session seo-research open "https://www.google.com/search?q=site:{domain}" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: approximate indexed page count
```

### 7. Keyword Difficulty Research (Answer The Public)

```bash
agent-browser --session seo-research open "https://answerthepublic.com/" && agent-browser wait --load networkidle
agent-browser snapshot -i
# Find search box, type keyword
agent-browser fill @e{n} "{keyword}"
agent-browser press Enter && agent-browser wait --load networkidle && agent-browser wait 5000
agent-browser get text body
# Extract: questions, prepositions, comparisons around keyword
```

### Close Session

Always close the research session when done:

```bash
agent-browser --session seo-research close
```

## Output

- Live SERP analysis data
- Competitor intelligence reports
- Technical audit data from live testing
- Screenshots for documentation