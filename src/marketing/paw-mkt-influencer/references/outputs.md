# Outputs and Deliverables

> Capability prompt for paw-mkt-influencer skill. Load when user needs to create deliverables or understand file structure.

---

## File Organization

### Campaign Mode
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/influencer/content/
  campaign-plan-{name}-{YYYY-MM-DD}.md
  outreach-templates-{YYYY-MM-DD}.md
  creator-brief-{campaign}-{YYYY-MM-DD}.md
  contract-outline-{YYYY-MM-DD}.md
  performance/
    campaign-report-{name}-{YYYY-MM-DD}.md
```

### Standalone Mode
```
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/influencer/content/
  campaign-plan-{name}-{YYYY-MM-DD}.md
  outreach-templates-{YYYY-MM-DD}.md
  creator-brief-{campaign}-{YYYY-MM-DD}.md
  contract-outline-{YYYY-MM-DD}.md
  ambassador-program-{YYYY-MM-DD}.md
  affiliate-program-{YYYY-MM-DD}.md
  ugc-program-{YYYY-MM-DD}.md
  influencer-shortlist-{YYYY-MM-DD}.md
  performance/
    campaign-report-{name}-{YYYY-MM-DD}.md
    monthly-report-{YYYY-MM}.md
```

---

## Deliverable Specifications

### Campaign Plan

Filename: `campaign-plan-{name}-{YYYY-MM-DD}.md`

Sections:
- Campaign Objective (SOSTAC alignment, KPI, target)
- Target Audience
- Influencer Strategy (tier mix, platforms, campaign type, creator count)
- Influencer Shortlist table (Creator, Platform, Followers, Eng Rate, Niche, Fit Score, Est Cost)
- Campaign Timeline table
- Budget breakdown (creator fees, gifting, shipping, tools, paid amplification, total)
- Creative Brief Summary
- Compensation Model
- Tracking and Attribution (codes, links, surveys)
- Success Metrics table
- Legal and Compliance

### Outreach Templates

Filename: `outreach-templates-{YYYY-MM-DD}.md`

Sections:
- DM Template (Cold)
- Email Template (Cold)
- Follow-Up Sequence (3 touchpoints)
- Negotiation Response Templates
- Onboarding Welcome Message

For detailed templates, read `./references/frameworks/cold-dms.md` and `./references/frameworks/follow-up-sequence.md`.

### Creator Brief

Filename: `creator-brief-{campaign}-{YYYY-MM-DD}.md`

Use template from `./references/campaign-management.md` or `./references/frameworks/creative-brief.md`.

### Contract Outline

Filename: `contract-outline-{YYYY-MM-DD}.md`

Sections:
- Parties
- Scope of Work (deliverables, platforms, timeline)
- Compensation (amount, schedule, method)
- Content Approval Process
- Usage Rights (scope, duration, paid media)
- Exclusivity
- Disclosure Requirements
- Content Ownership
- Termination
- Confidentiality
- Performance Benchmarks

Note: outline only -- consult legal for binding agreements.

For detailed template, read `./references/frameworks/contract-outline.md`.

### Ambassador Program

Filename: `ambassador-program-{YYYY-MM-DD}.md`

Sections:
- Program Objective
- Tier Structure (levels, requirements, benefits)
- Selection Criteria
- Application and Onboarding Process
- Content Requirements
- Compensation and Perks by Tier
- Tracking
- Communication Cadence
- Rules and Guidelines
- Renewal Criteria

For detailed tier structure, read `./references/frameworks/ambassador-tiers.md`.

### Performance Report

Filename: `performance/campaign-report-{name}-{YYYY-MM-DD}.md`

Sections:
- Campaign Summary
- Performance Overview table
- Creator-Level Performance table
- Top-Performing Content analysis
- Underperforming Content analysis
- ROI Analysis
- Key Learnings
- Recommendations

For detailed template, read `./references/frameworks/campaign-reporting.md`.

---

## Outcome

Deliver specified document(s) saved to resolved path with appropriate filename convention.