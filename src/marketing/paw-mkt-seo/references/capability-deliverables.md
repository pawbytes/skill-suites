# Deliverables & Action Plans Capability

## Overview
Produce structured SEO deliverables: audits, keyword reports, action plans, schema markup, and programmatic SEO framework packs. All outputs saved to resolved path with implementation guidance.

## When to Use
- SEO audit delivery
- Monthly action planning
- Schema markup implementation
- Programmatic SEO framework
- Content brief delivery

## Capability Workflow

### 6.1 SEO Audit

Produce `seo-audit-{YYYY-MM-DD}.md` with:

**Sections**:
- Audit Summary
- Technical SEO checks table (CWV, sitemap, robots.txt, schema, mobile, HTTPS, canonicals, internal linking, crawl errors, page speed)
  - Each with Status, Priority (P1/P2/P3), Notes
- Content SEO checks (titles, metas, H1s, content depth, keyword targeting, internal links, alt text)
- Off-Page checks (backlink health, referring domains, toxic links)
- Local SEO checks if applicable (GBP, NAP, reviews)
- AI Search Readiness checks (FAQ schema, direct answers, structured data)
- Priority Action Items (ordered critical to low)

### 6.2 Keyword Research Report

Save as `keyword-research-{topic}-{YYYY-MM-DD}.md` with:
- Seed keywords table (keyword, volume, difficulty, intent)
- Keyword clusters (primary keyword, supporting keywords, recommended content, target URL per cluster)
- Prioritization matrix (Quick Wins, Strategic Targets, Long-Tail Opportunities)
- Content calendar recommendations

### 6.3 Monthly SEO Action Plan

Save as `seo-action-plan-{YYYY-MM}.md` with:
- Month's focus (aligned to SOSTAC objectives)
- Task tables for: Technical SEO, Content, Link Building, Local SEO, AI Search Optimization
  - Each with: task, priority, deadline, owner, status
- KPIs to track (metric, current, target, tool)
- Last month's results review

### 6.4 Schema Markup Code

Save as `schema/{type}-{YYYY-MM-DD}.json` with:
- Ready-to-implement JSON-LD
- Implementation notes: where to place, how to test, how to verify in GSC

### 6.5 Programmatic SEO Framework Pack

Save pSEO deliverables under `programmatic-seo/` when planning scaled SEO page systems.

**Framework Lookup**: Read `./references/frameworks-index.csv` by `seo_domain` = "Programmatic SEO" and load relevant files.

Produce as needed:
- `pseo-opportunity-map-{YYYY-MM-DD}.md` -- page families, search patterns, business value, source data, uniqueness levers, major risks
- `pseo-template-spec-{page-type}-{YYYY-MM-DD}.md` -- URL pattern, target intent, required fields, content blocks, schema, internal linking rules, indexation policy
- `pseo-launch-checklist-{YYYY-MM-DD}.md` -- sampling plan, QA gates, sitemap/canonical rules, analytics setup, rollback triggers
- `pseo-monitoring-plan-{YYYY-MM-DD}.md` -- KPIs by template family, prune thresholds, refresh cadence, ownership

## File Organization

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/content/
  seo-audit-{YYYY-MM-DD}.md
  keyword-research-{topic}-{YYYY-MM-DD}.md
  seo-action-plan-{YYYY-MM}.md
  content-briefs/
    brief-{slug}.md
  schema/
    {type}-{YYYY-MM-DD}.json

# Standalone mode (default for evergreen work):
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/content/
  seo-audit-{YYYY-MM-DD}.md
  keyword-research-{topic}-{YYYY-MM-DD}.md
  seo-action-plan-{YYYY-MM}.md
  content-briefs/
    brief-{slug}.md
  schema/
    {type}-{YYYY-MM-DD}.json
  programmatic-seo/
    pseo-opportunity-map-{YYYY-MM-DD}.md
    pseo-template-spec-{page-type}-{YYYY-MM-DD}.md
    pseo-launch-checklist-{YYYY-MM-DD}.md
    pseo-monitoring-plan-{YYYY-MM-DD}.md
  link-building/
    backlink-analysis-{YYYY-MM-DD}.md
    outreach-tracker.md
  local-seo/
    gbp-optimization.md
    citation-tracker.md
```

## Output Contract

All SEO deliverables include:
- **SEO type**: technical, content, local, pSEO, or GEO
- **Findings/recommendations**: specific, prioritized actions (P1/P2/P3)
- **Keywords**: target terms with volume and difficulty when available
- **Implementation notes**: what to change and where
- **Expected impact**: which metrics should improve
- **File saved to**: path where deliverable was written