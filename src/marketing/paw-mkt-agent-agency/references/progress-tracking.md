# Progress Tracking

This reference covers how to gather and present progress data when the user asks about marketing status.

---

## Brand-Level Overview

Read and summarize:
- `README.md` — the brand dashboard (`Status:`, `Next:`), and each campaign's `README.md`
- `brand-context.md` — current stage
- `sostac/README.md` — planning status
- `campaigns/` — list all named campaign directories and their strategy.md status
- `channels/` — list standalone channel work
- `operations/` — list standalone operational work
- `analytics/` — latest reports if they exist

## Campaign-Level Detail

For each named campaign under `campaigns/{YYYY-MM}-{type}-{slug}/`:
- Read `strategy.md` for campaign objective and status
- Check `channels/` subdirectories for content deliverables per channel
- Check operational subdirectories (cro/, retention/, etc.) for completed work
- Check `performance/` for results reports
- Report what is done, what is in progress, and what is pending

## Standalone Work

For standalone work under `channels/` and `operations/`:
- Check each channel directory for evergreen deliverables
- Check each operations directory for ongoing work

## Present Progress Clearly

```
# {Brand Name} — Marketing Progress

## Strategic Plan (SOSTAC)
- Status: Complete (6/6 phases)
- Last updated: {date}

## Active Campaigns

### 2026-03-launch-spring-release
- Strategy: Complete
- Channels active: email, social, blog, paid-ads
- Email content: 3/5 emails drafted
- Social content: Complete (12 posts)
- Blog content: In Progress (2/4 posts)
- Paid ads content: Not Started
- Performance: No reports yet

## Standalone Channel Work

### channels/blog/
- Evergreen articles: 8 published
- Content calendar: Current month planned

### channels/seo/
- SEO audit: Complete
- Keyword research: In Progress

## Operational Work

### operations/cro/
- Landing page audit: Complete
- A/B tests: 2 active

## Key Metrics
{Pull from analytics/ if available}

## Next Actions
{Derived from campaign strategy.md and Action plan timeline}
```

When the status changes, update the brand `README.md` `Status:`/`Next:` lines to match.
