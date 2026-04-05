# Launch Deliverables and File Structure

All launch deliverables are presented for review before saving. Save to the resolved path only after user confirmation.

## Path Resolution

**Campaign mode** — working within a named campaign:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/launch/
```
Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** — evergreen or independent work:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/launch/
```

If unsure, ask: "Is this part of a specific campaign, or standalone work?"

## Deliverables List

| Deliverable | Filename | Contents |
|---|---|---|
| Launch Strategy | `launch-strategy-{YYYY-MM-DD}.md` | Launch type, ORB plan, phase timeline, channel owners, success metrics, budget |
| Launch Brief | `launch-brief-{YYYY-MM-DD}.md` | One-page summary: what, who, when, key messages, channel plan, launch day schedule |
| Launch Blog Post | `content/launch-post-{YYYY-MM-DD}.md` | Full blog post draft, SEO title, meta description, tags |
| Email Announcement | `channels/email/content/email-announcement-{YYYY-MM-DD}.md` | Subject line variants, preheader, full body copy, CTA |
| Social Posts | `channels/social/content/social-posts-{YYYY-MM-DD}.md` | Per-platform drafts: X thread, LinkedIn post, Instagram captions, Reddit/community posts |
| Press Release | `channels/pr/content/press-release-{YYYY-MM-DD}.md` | Full press release, distribution plan |
| Product Hunt Brief | `content/product-hunt-brief-{YYYY-MM-DD}.md` | Tagline variants, description, first comment draft, gallery spec, supporter outreach template |
| Supporter Outreach | `channels/email/content/supporter-email-{YYYY-MM-DD}.md` | Pre-launch supporter briefing email + launch day ask email |
| Launch Day Schedule | `launch-day-schedule-{YYYY-MM-DD}.md` | Minute-by-minute timeline with owners and channel links |
| Launch Performance Report | `performance/launch-report-{YYYY-MM}.md` | Results vs targets, learnings, recommendations for next launch |

## File Organization

### Campaign Mode

```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/launch-{campaign-slug}/launch/
  launch-strategy-{YYYY-MM-DD}.md
  launch-brief-{YYYY-MM-DD}.md
  launch-day-schedule-{YYYY-MM-DD}.md
  assets/
    press-kit/
      screenshots/
      logos/
  performance/
    launch-report-{YYYY-MM}.md

# Channel-specific content lives in the campaign's channel dirs:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/launch-{campaign-slug}/channels/
  email/content/email-announcement-{YYYY-MM-DD}.md
  social/content/social-posts-{YYYY-MM-DD}.md
  content/content/launch-post-{YYYY-MM-DD}.md
  pr/content/press-release-{YYYY-MM-DD}.md
```

### Standalone Mode

```
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/launch/
  (same structure, content/ subdir for non-campaign work)
```

## Evergreen Launch Assets

Maintain these so each launch activates faster:

- **Press kit**: updated product screenshots, founder headshots, company boilerplate, recent coverage logos. Store at `{resolved-path}/assets/press-kit/`.
- **Launch email templates**: maintain 3-5 subject line formulas and body templates that can be adapted per launch.
- **Social proof library**: rotating bank of testimonials, case study quotes, and metrics. Update monthly.
- **Supporter list**: maintain a rolling list of launch supporters (Product Hunt voters, beta users who responded) for future launches.