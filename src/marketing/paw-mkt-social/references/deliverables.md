# Deliverables

> Social content calendars, platform strategy documents, content briefs, caption templates, hashtag sets, and UGC campaign briefs.
> Load this reference when creating or formatting social media deliverables.

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/social/content/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/social/content/`

**Legacy fallback** -- old directory structure detected:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/content/social/`
  -> Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## 1. Social Content Calendar

Save as `social-calendar-{YYYY-MM}.md`:

```markdown
# Social Content Calendar -- {Brand Name} -- {Month Year}

## Monthly Theme: {theme}
## Platform Focus: {primary platforms}
## Key Dates: {holidays, launches, events}

## Weekly Breakdown

### Week 1: {sub-theme}
| Day | Platform | Format | Pillar | Topic/Caption | Hashtags | Asset Needed |
|---|---|---|---|---|---|---|

### Week 2-4: {repeat}

## Content Production Checklist
## Repurposing Plan
```

---

## 2. Platform Strategy Document

Save as `platform-strategy-{platform}-{YYYY-MM-DD}.md`:

```markdown
# {Platform} Strategy -- {Brand Name}

## Objective (from SOSTAC)
## Target Audience on This Platform
## Content Pillars and Mix
## Posting Frequency and Schedule
## Content Formats
## Hashtag Sets
## Growth Tactics
## Engagement Plan

## KPIs and Targets
| Metric | Current | Target (30d) | Target (90d) |

## Competitor Benchmarks
```

---

## 3. Content Brief

Save as `content-brief-{slug}-{YYYY-MM-DD}.md`:

```markdown
# Content Brief: {Title}

## Platform(s)
## Format
## Content Pillar
## Objective
## Hook
## Key Message
## Caption Draft
## CTA
## Hashtags
## Visual Direction
## References / Inspiration
```

---

## 4. Caption Templates

Save as `caption-templates-{platform}.md`.

Sections: Educational, Entertaining, Promotional, Community/Engagement -- 3-5 fill-in-the-blank templates with hooks and CTAs per section.

---

## 5. Hashtag Sets

Save as `hashtag-sets.md`.

Sections: Branded, Set A/B/C by topic, Trending (update weekly), Rotation Schedule.

---

## 6. UGC Campaign Brief

Save as `ugc-campaign-{name}-{YYYY-MM-DD}.md`.

Sections: Objective, Branded Hashtag, Participation Mechanic, Incentive Structure, Content Guidelines, Curation Process, Legal (permissions/rights), Promotion Plan, Success Metrics.

---

## 7. Competitor Analysis

Save as `competitor-analysis-{YYYY-MM-DD}.md`.

Document per competitor:
- Platforms and handles
- Posting frequency
- Content themes and formats
- Engagement rates
- Top-performing content patterns
- Gaps you can own

---

## 8. Performance Report

Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/social/content/performance/monthly-report-{YYYY-MM}.md`.

Include:
- Summary metrics (reach, engagement, followers)
- Top 5 and bottom 5 posts
- Platform-by-platform breakdown
- Trend analysis
- Recommendations for next month

---

## File Organization Summary

```
## Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/social/content/
  social-calendar-{YYYY-MM}.md
  platform-strategy-{platform}-{YYYY-MM-DD}.md
  content-brief-{slug}-{YYYY-MM-DD}.md
  caption-templates-{platform}.md
  hashtag-sets.md
  ugc-campaign-{name}-{YYYY-MM-DD}.md

## Standalone mode (default for evergreen work):
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/social/content/
  social-calendar-{YYYY-MM}.md
  platform-strategy-{platform}-{YYYY-MM-DD}.md
  content-brief-{slug}-{YYYY-MM-DD}.md
  caption-templates-{platform}.md
  hashtag-sets.md
  ugc-campaign-{name}-{YYYY-MM-DD}.md
  competitor-analysis-{YYYY-MM-DD}.md
  performance/
    monthly-report-{YYYY-MM}.md
```

---

## Output Contract

Social media deliverables include:
- **Platform**: which platform(s) the content targets
- **Content type**: post, story, thread, carousel, etc.
- **Copy**: ready-to-publish text with hashtags and CTAs
- **Visual direction**: image/video guidance or specifications
- **Posting schedule**: recommended day/time with reasoning
- **File saved to**: path where the deliverable was written