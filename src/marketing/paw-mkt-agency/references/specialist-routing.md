# Specialist Routing

This reference covers mapping campaign tactics to specialist skills, the context brief format, and where specialist output goes.

---

## Tactic-to-Specialist Map

| Tactic / Channel | Specialist | Skill |
|---|---|---|
| SEO, organic search, technical SEO | SEO Specialist | `paw-mkt-seo` |
| PPC, paid search, display ads, retargeting | Paid Media Manager | `paw-mkt-paid-ads` |
| Social media management, organic social | Social Media Manager | `paw-mkt-social` |
| Blog posts, whitepapers, case studies, editorial | Content Strategist | `paw-mkt-content` |
| Email campaigns, newsletters, drip sequences | Email Marketing Specialist | `paw-mkt-email` |
| Guerrilla marketing, unconventional tactics, viral | Growth Hacker | `paw-mkt-guerrilla` |
| Video content, YouTube, TikTok, webinars | Video Strategist | `paw-mkt-video` |
| Influencer partnerships, creator collabs, UGC | Influencer Manager | `paw-mkt-influencer` |
| Press releases, media outreach, thought leadership | PR Specialist | `paw-mkt-pr` |
| Community building, forums, Discord, user groups | Community Manager | `paw-mkt-community` |
| Referral programs, affiliate marketing | Referral Manager | `paw-mkt-referral` |
| Analytics, reporting, A/B testing, attribution | Analytics Analyst | `paw-mkt-analytics` |
| Landing pages, signup flows, conversion optimization | CRO Specialist | `paw-mkt-cro` |
| Churn reduction, win-back, retention flows | Retention Specialist | `paw-mkt-retention` |
| Product launch, go-to-market | Launch Strategist | `paw-mkt-launch` |
| Pricing strategy, tier packaging | Pricing Strategist | `paw-mkt-pricing` |
| Behavioral science, persuasion, copy psychology | Psychology Strategist | `paw-mkt-psychology` |
| Sales decks, objection handling, demo scripts | Sales Enablement | `paw-mkt-sales` |

## Context Brief Format

Each brief is a markdown file the user takes to the specialist skill. Write it to the specialist's output directory within the brand workspace.

```markdown
# Specialist Brief: {Specialist Role}

## Brand
- **Name**: {brand name}
- **Brand context**: `{path to brand-context.md}`

## Campaign
- **Campaign**: {campaign name} (or "Standalone")
- **Strategy**: `{path to strategy.md}` (if campaign)

## Objective
{What this specialist should achieve — tied to campaign objectives}

## Audience
{Relevant audience segments for this channel/discipline}

## Voice & Tone
{Brand voice guidance and any campaign-specific tone notes}

## Key Messages
{Core messages this specialist should carry through their work}

## Constraints
{Budget, timeline, compliance, or other constraints}

## Deliverables
{Specific outputs expected from this specialist}

## Context Files
{List of SOSTAC phases, brand assets, or other files the specialist should read}
```

## Specialist Output Locations

All paths relative to the brand workspace (`.pawbytes/marketing-suites/brands/{slug}/`).

**Campaign mode** — deliverables go under the campaign directory:

| Type | Path |
|---|---|
| Channel content | `campaigns/{type}-{slug}/channels/{channel}/content/` |
| Operational work | `campaigns/{type}-{slug}/{discipline}/` |
| Performance | `campaigns/{type}-{slug}/performance/` |

**Standalone mode** — deliverables go to top-level directories:

| Type | Path |
|---|---|
| Channel content | `channels/{channel}/content/` |
| Operational work | `operations/{discipline}/` |
| Analytics | `analytics/` |

### Channel-to-Directory Mapping

| Specialist Skill | Channel Dir |
|---|---|
| `paw-mkt-seo` | `seo` |
| `paw-mkt-paid-ads` | `paid-ads` |
| `paw-mkt-social` | `social` |
| `paw-mkt-content` | `blog` and `content` |
| `paw-mkt-email` | `email` |
| `paw-mkt-video` | `video` |
| `paw-mkt-influencer` | `influencer` |
| `paw-mkt-pr` | `pr` |

### Operational-to-Directory Mapping

| Specialist Skill | Operations Dir |
|---|---|
| `paw-mkt-guerrilla` | `guerrilla` |
| `paw-mkt-cro` | `cro` |
| `paw-mkt-retention` | `retention` |
| `paw-mkt-launch` | `launch` |
| `paw-mkt-pricing` | `pricing` |
| `paw-mkt-community` | `community` |
| `paw-mkt-referral` | `referral` |
| `paw-mkt-sales` | `sales` |
| `paw-mkt-analytics` | → `analytics/` (brand-level) |
| `paw-mkt-psychology` | → `psychology/` (campaign or standalone) — cross-cutting advisory; receives requests from other specialists (CRO, pricing, email, content, retention, sales, social, paid-ads), returns behavioral recommendations to the originating skill. See `paw-mkt-psychology` SKILL.md § Escalation Routes for full inbound/outbound details |
