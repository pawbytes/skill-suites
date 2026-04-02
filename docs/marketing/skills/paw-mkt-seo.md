# `marketing-seo`

## Overview

Covers technical SEO, content SEO, programmatic SEO (pSEO), local SEO, link building, and AI search optimization (GEO / Google AI Overviews).

## When to use it

Use `/paw-mkt-seo` when you need:
- a technical or content SEO audit
- keyword research
- content briefs for search
- programmatic SEO strategy and templates
- schema markup
- local SEO recommendations
- GEO or AI Overview readiness work
- link building strategy or digital PR for backlinks

## Inputs to prepare

- active brand
- site or page scope
- target topics or keywords
- competitors
- any existing analytics or ranking data

## Output path resolution

The skill routes output based on whether work is part of a campaign or standalone:

| Mode | When to use | Output path |
|---|---|---|
| Campaign | Work tied to a specific launch or push | `brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/` |
| Standalone | Evergreen or independent work | `brands/{brand-slug}/channels/seo/` |
| Legacy fallback | Old workspace structure detected | `brands/{brand-slug}/content/seo/` |

If unsure which mode applies, the skill will ask.

## Deliverables

- SEO audits (technical and content)
- keyword research docs
- monthly action plans
- content briefs
- schema files
- programmatic SEO data contracts, page archetypes, and template specs
- AI Overview / GEO optimization recommendations

## Framework files

22 individual framework files, indexed in `frameworks-index.csv`:

- Technical audit, core web vitals, site architecture
- Schema markup, sitemap, robots.txt
- Internal linking, JavaScript SEO
- International SEO
- Programmatic SEO (pSEO): opportunity mapping, page archetypes, template spec, data contract, indexation, internal linking, launch strategy, monitoring, anti-cannibalization, refresh/pruning
- AI Overview optimization
- Algorithm update guidance

## Related skills

- `marketing-content` — content creation from SEO briefs
- `marketing-analytics` — search performance tracking
- `marketing-cro` — landing page optimization for search traffic
- `marketing-pr` — digital PR for link building

## Sample prompts

```text
/paw-mkt-seo
Run a technical and content SEO audit.
```

```text
/paw-mkt-seo
For Northstar AI, build keyword research around recruiting automation, interview notes, and candidate scorecards.
```

```text
/paw-mkt-seo
Use our SOSTAC plan and product marketing context to create three high-intent SEO briefs.
```

```text
/paw-mkt-seo
Design a programmatic SEO strategy for our location-based landing pages.
```
