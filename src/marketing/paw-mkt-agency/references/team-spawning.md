# Team Spawning & Implementation

This reference covers assembling specialist teams from a completed SOSTAC plan, managing campaigns, output routing, and legacy directory detection.

---

## Spawning Implementation Teams

When the SOSTAC plan is complete and the user wants to implement, assemble a team of specialists.

### Step 1 — Read the Tactics Phase

Read `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/04-tactics.md` to identify which marketing channels and tactics the plan calls for. This file is the source of truth for what specialists are needed.

### Step 2 — Map Tactics to Specialists

| Tactic/Channel Category | Specialist Role | Skill to Use |
|---|---|---|
| SEO, organic search, technical SEO, content optimization | SEO Specialist | `paw-mkt-seo` |
| PPC, paid search, display ads, paid social ads, retargeting | Paid Media Manager | `paw-mkt-paid-ads` |
| Social media management, community posting, organic social | Social Media Manager | `paw-mkt-social` |
| Blog posts, whitepapers, case studies, content calendar | Content Strategist | `paw-mkt-content` |
| Email campaigns, newsletters, drip sequences, automation | Email Marketing Specialist | `paw-mkt-email` |
| Guerrilla marketing, stunts, unconventional tactics, viral | Growth Hacker | `paw-mkt-guerrilla` |
| Video content, YouTube, TikTok production, webinars | Video Strategist | `paw-mkt-video` |
| Influencer partnerships, creator collaborations, UGC | Influencer Manager | `paw-mkt-influencer` |
| Press releases, media outreach, thought leadership | PR Specialist | `paw-mkt-pr` |
| Community building, forums, Discord, user groups | Community Manager | `paw-mkt-community` |
| Referral programs, affiliate marketing, partnerships | Referral/Affiliate Manager | `paw-mkt-referral` |
| Analytics, reporting, A/B testing, attribution | Analytics Analyst | `paw-mkt-analytics` |
| Landing page CRO, signup optimization, onboarding activation, forms, popups, paywalls | CRO Specialist | `paw-mkt-cro` |
| Churn reduction, cancel flows, dunning sequences, win-back campaigns, health scoring | Retention Specialist | `paw-mkt-retention` |
| Product launch, go-to-market, Product Hunt, launch content, announcement cadence | Launch Strategist | `paw-mkt-launch` |
| Pricing strategy, tier packaging, value metric, pricing page, willingness-to-pay | Pricing Strategist | `paw-mkt-pricing` |
| Behavioral science, cognitive biases, persuasion frameworks, copy psychology | Psychology Strategist | `paw-mkt-psychology` |
| Sales decks, one-pagers, objection handling, demo scripts, ROI calculators, champion kits | Sales Enablement Specialist | `paw-mkt-sales` |

### Step 3 — Confirm the Team with the User

Before spawning, present the proposed team:

```
Based on your SOSTAC plan, here is the recommended team:

  Team Lead: Agency Coordinator (me)

  Specialists:
  - SEO Specialist — organic search optimization, technical SEO audit
  - Content Strategist — blog content calendar, thought leadership pieces
  - Email Marketing Specialist — welcome sequence, nurture campaigns
  - Social Media Manager — LinkedIn and Twitter organic strategy

  Not needed for this plan:
  - Paid Media (plan focuses on organic growth first)
  - Video Strategist (deferred to Phase 2)

Shall I assemble this team and begin implementation? You can add or remove specialists.
```

### Step 4 — Spawn the Team

Use the TeamCreate tool to create the implementation team:

- **Team name**: `{brand-slug}-marketing`
- **Description**: "Marketing implementation team for {Brand Name}"

Then create tasks based on the SOSTAC Action phase (`05-action.md`), which should contain the implementation timeline and task breakdown. Assign tasks to the appropriate specialists.

### Step 5 — Coordinate Implementation

As the team lead:
1. Create tasks from the Action plan's timeline and milestones.
2. Assign each task to the appropriate specialist agent.
3. Ensure specialists have access to:
   - `brand-context.md` (brand voice, audience, USP)
   - The relevant SOSTAC phase files (especially Tactics and Action)
   - The `campaigns/`, `channels/`, and `operations/` directories for output
4. Monitor progress and report back to the user.
5. Each specialist should write their outputs to the appropriate brand subdirectory.

---

## Specialist Output Locations

Specialists use dual-mode routing. When working within a named campaign, deliverables go under the campaign directory. When working standalone (evergreen or independent), deliverables go to the top-level `channels/` or `operations/` directory.

**Channel Specialists (content-producing)**:

| Specialist | Campaign Mode | Standalone Mode |
|---|---|---|
| SEO Specialist | `campaigns/{type}-{slug}/channels/seo/content/` | `channels/seo/content/` |
| Paid Media Manager | `campaigns/{type}-{slug}/channels/paid-ads/content/` | `channels/paid-ads/content/` |
| Social Media Manager | `campaigns/{type}-{slug}/channels/social/content/` | `channels/social/content/` |
| Content Strategist | `campaigns/{type}-{slug}/channels/blog/content/` | `channels/blog/content/` and `channels/content/content/` |
| Email Marketing Specialist | `campaigns/{type}-{slug}/channels/email/content/` | `channels/email/content/` |
| Video Strategist | `campaigns/{type}-{slug}/channels/video/content/` | `channels/video/content/` |
| Influencer Manager | `campaigns/{type}-{slug}/channels/influencer/content/` | `channels/influencer/content/` |
| PR Specialist | `campaigns/{type}-{slug}/channels/pr/content/` | `channels/pr/content/` |

**Operational Specialists (non-channel disciplines)**:

| Specialist | Campaign Mode | Standalone Mode |
|---|---|---|
| Growth Hacker | `campaigns/{type}-{slug}/guerrilla/` | `operations/guerrilla/` |
| CRO Specialist | `campaigns/{type}-{slug}/cro/` | `operations/cro/` |
| Retention Specialist | `campaigns/{type}-{slug}/retention/` | `operations/retention/` |
| Launch Strategist | `campaigns/{type}-{slug}/launch/` | `operations/launch/` (rare — launch is typically a campaign type) |
| Pricing Strategist | `campaigns/{type}-{slug}/pricing/` | `operations/pricing/` |
| Community Manager | `campaigns/{type}-{slug}/community/` | `operations/community/` |
| Referral/Affiliate Manager | `campaigns/{type}-{slug}/referral/` | `operations/referral/` |
| Sales Enablement Specialist | `campaigns/{type}-{slug}/sales/` | `operations/sales/` |
| Analytics Analyst | `campaigns/{type}-{slug}/performance/` | `analytics/` |
| Psychology Strategist | *(cross-cutting — annotates other specialists' deliverables)* | *(cross-cutting)* |

---

## Campaign Creation

When the user wants to create a new campaign:

1. **Select campaign type**: `launch`, `evergreen`, `seasonal`, `promotion`, `awareness`, `growth`, `retention`, `event`
2. **Name the campaign**: derive a slug (e.g., "Spring Product Release" → `spring-product-release`)
3. **Create the campaign directory**: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`
4. **Write strategy.md** with this template:

```markdown
# Campaign: {Campaign Name}

## Meta
- **Type**: {campaign type}
- **Brand**: {brand name}
- **Created**: {YYYY-MM-DD}
- **Status**: Planning

## Objective
{What this campaign aims to achieve — tied to SOSTAC objectives}

## Target Audience
{Specific segment(s) this campaign targets}

## Channels
{Which channels will this campaign use — determines which channel subdirs to create}

## Key Messages
{Core messages across all channels}

## Timeline
| Phase | Dates | Activities |
|---|---|---|

## Budget
{Budget allocation across channels}

## Success Metrics
| Metric | Target | Measurement |
|---|---|---|
```

5. **Scaffold channel directories** based on the channels listed in strategy.md
6. **Spawn specialists** for each channel

---

## Legacy Directory Detection

If a brand workspace uses the old flat structure (`content/{type}/` or `campaigns/{channel}/`):

1. **Detect**: Check for `content/social/`, `content/email/`, `content/blog/`, `content/video/`, `content/seo/`, `campaigns/paid-ads/`, `campaigns/pr/`, `campaigns/influencer/`, etc.
2. **Inform**: "This brand uses the legacy directory structure. The new structure organizes content by Campaign → Channel → Content for campaign work, and channels/ for standalone work."
3. **Offer migration**: "Would you like me to migrate to the new structure? I'll move existing files to their new locations."
4. **If declined**: Continue using the old paths. Specialists have a legacy fallback mode.
