# Content SEO Capability

## Overview
Research keywords, map search intent, create content briefs, and build topic clusters. Delivers keyword research reports, content briefs, and gap analysis grounded in SERP patterns.

## When to Use
- Keyword research for new content
- Content brief creation
- Content gap analysis
- Topic cluster planning
- Content refresh strategy
- E-E-A-T optimization

## Reference Files
- `./references/best-practices.md` -- extended content SEO practices
- `./references/frameworks/ai-overview-optimization.md` -- GEO content patterns

## Capability Workflow

### 2.1 Keyword Research Methodology

**Step 1 -- Seed Keywords**: Extract from brand context, product descriptions, competitor analysis, customer language. List 10-30 seed terms.

**Step 2 -- Expansion**: For each seed, expand using:
- Autocomplete suggestions (Google, YouTube, Amazon, Bing)
- "People Also Ask"
- Related searches
- Competitor keyword gaps
- Topical variations (synonyms, long-tail, modifiers)

**Step 3 -- Clustering**: Group by topic and intent.
- One primary keyword per page/cluster
- 5-15 supporting keywords per cluster
- Map clusters to existing or planned pages

**Step 4 -- Prioritization**: Score each cluster on search volume, keyword difficulty, business relevance, search intent match, conversion potential.

Present as prioritized matrix:
- Quick Wins (low difficulty + high relevance)
- Strategic Targets (high volume + high difficulty)
- Long-Tail Opportunities (low volume + low difficulty + high conversion)

### 2.2 Search Intent Mapping

Classify every target keyword by intent:

| Intent | Signal Words | Content Format | Conversion Stage |
|---|---|---|---|
| Informational | how to, what is, guide, tips | Blog, guide, video | Awareness |
| Navigational | brand name, product name, login | Homepage, product page | Consideration |
| Commercial | best, review, comparison, vs, top | Comparison, review | Consideration |
| Transactional | buy, price, discount, order | Product page, pricing | Decision |

Match content format to intent. Check the SERP to confirm what format ranks.

### 2.3 Content Briefs

Every SEO content brief includes:
- Target keyword
- Supporting keywords (5-15)
- Search intent
- Target word count (from SERP analysis)
- Target URL
- SERP analysis (top 5 results, content gaps, featured snippet opportunity, PAA questions)
- Recommended H1/H2/H3 structure
- Must-include elements (data points, internal links, external links, media)
- E-E-A-T signals (author bio, first-person experience, citations, updated date)
- On-page optimization (title tag 60 chars, meta description 155 chars, URL slug, image alt text)

Save briefs to `content-briefs/brief-{slug}.md` within resolved path.

### 2.4 Content Gap Analysis

Compare brand's keyword coverage against top 3-5 competitors:
- Topics competitors rank for that brand does not
- Topics where brand ranks page 2-3 (striking distance)
- Topics no competitor covers well (blue ocean)

Present as prioritized content calendar with estimated effort and impact.

### 2.5 Topic Clusters and Pillar Pages

- **Pillar Page**: Comprehensive guide on broad topic (2000-5000 words). Targets head keyword. Links to every cluster page.
- **Cluster Pages**: Focused articles on subtopics (800-2000 words). Target long-tail keywords. Link back to pillar and to each other.
- **Internal Linking Map**: Every cluster links to pillar. Pillar links to all clusters. Related clusters cross-link.

One pillar per core business topic. Build topical authority through depth and interconnection.

### 2.6 Content Refresh Strategy

Audit existing content quarterly:
- Pages losing traffic (3-month rolling average)
- Pages ranking 4-20 (striking distance)
- Pages with outdated information
- Thin content on competitive topics

For each refresh: update stats, add sections, improve structure, refresh meta tags, update internal links, add schema, re-submit to GSC.

### 2.7 E-E-A-T Optimization

- **Experience**: First-hand accounts, case studies, original data, screenshots
- **Expertise**: Author bios with credentials, bylines, author pages, expert quotes
- **Authoritativeness**: Backlinks from authority sites, brand mentions, industry awards
- **Trustworthiness**: HTTPS, contact info, privacy policy, editorial policy, cited sources

For YMYL topics (health, finance, legal), E-E-A-T requirements are higher. Flag and recommend stronger trust signals.

## Output

- `keyword-research-{topic}-{YYYY-MM-DD}.md` -- seed keywords, clusters, prioritization matrix
- `content-briefs/brief-{slug}.md` -- SEO content briefs
- Content calendar recommendations