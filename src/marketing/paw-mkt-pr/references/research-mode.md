# Research Mode: Media & PR Intelligence

> Use agent-browser for browser-based research on coverage, journalist queries, and backlink opportunities before pitching.

## Prerequisites

Check `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md` for PR data already collected.

**Setup**: See `./references/shared-patterns.md` for agent-browser installation instructions.

## Research Commands

### Google News - Brand Coverage

```bash
agent-browser --session pr-research open "https://news.google.com/search?q={brand-name}&hl=en" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: recent coverage, media outlets, story angles, sentiment
```

### Google News - Competitor Coverage

```bash
agent-browser --session pr-research open "https://news.google.com/search?q={competitor-name}&hl=en" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: competitor coverage, outlets covering them, angles
```

### HARO/Connectively - Active Journalist Queries

```bash
agent-browser --session pr-research open "https://www.connectively.us/sources" && agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser get text body
# Extract: active queries in relevant categories
```

### Journalist LinkedIn Search

```bash
agent-browser --session pr-research open "https://www.linkedin.com/search/results/people/?keywords={topic}+journalist&origin=GLOBAL_SEARCH_HEADER" && agent-browser wait --load networkidle
agent-browser get text body
```

### Backlink Opportunity - Competitor Analysis

```bash
agent-browser --session pr-research open "https://ahrefs.com/backlink-checker?target={competitor-domain}&mode=domain" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
# Extract: top referring domains visible in free report
```

### Close Session

```bash
agent-browser --session pr-research close
```

## Research Outputs

Document findings in the campaign or brand workspace:

- **Coverage audit**: Recent media mentions, outlets, sentiment, share of voice
- **Competitor PR analysis**: Where competitors are getting coverage, their angles
- **Journalist pipeline**: Relevant journalists with beats, recent articles, contact info
- **Backlink landscape**: Domains linking to competitors, potential link opportunities
- **Query opportunities**: Active HARO/source requests matching brand expertise

## Integration with Other Skills

- Share backlink data with paw-mkt-seo for link building coordination
- Share competitor coverage insights with paw-mkt-content for content gaps
- Share journalist pipeline with paw-mkt-social for engagement strategy