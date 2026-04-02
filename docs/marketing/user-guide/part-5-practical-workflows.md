# Part 5: Practical Workflows (Step-by-Step)

This part provides detailed, practical workflows you can follow step-by-step. Each chapter includes sample prompts, expected outputs, and specific file paths where work gets saved.

---

## Chapter 13: Starting a New Brand

### 13.1 What Happens When You Start Fresh

When you begin marketing work for a brand that does not yet have a workspace in the system, the paw-mkt-agency skill orchestrates the setup:

1. **Workspace creation**: A new directory is created under `.pawbytes/marketing-suites/brands/{brand-slug}/`
2. **Context capture**: The `brand-context.md` file captures essential identity information
3. **Planning scaffold**: The `sostac/README.md` creates a phase tracker for strategy work
4. **Routing**: After setup, you typically route into `/paw-mkt-sostac` for planning

The system never asks you to manually create directories or files. All setup happens through skill orchestration.

### 13.2 The Recommended Sequence

Follow this sequence for new brands:

#### Step 1: Brand Context Creation

Start with the paw-mkt-agency skill:

```
/paw-mkt-agency
I want to set up marketing for a new brand called [Brand Name]. We [brief description of what you sell]. Our target audience is [who you're marketing to]. We're at [pre-launch | early-stage | established | scaling] stage.
```

**What gets created:**

```
.pawbytes/marketing-suites/brands/{brand-slug}/
├── brand-context.md
└── sostac/
    └── README.md
```

**Sample output (brand-context.md):**

```markdown
# Flowstack

## Overview
- **Name**: Flowstack
- **Slug**: flowstack
- **Website**: TBD
- **Stage**: early-stage
- **Created**: 2026-03-31

## What We Do
Flowstack is a workflow automation platform for operations teams at mid-market companies. We replace manual spreadsheet tracking with automated pipelines that sync data across tools and send proactive alerts.

## Target Audience
Operations managers and directors at companies with 50-500 employees who manage cross-tool workflows (Salesforce, Jira, Slack, spreadsheets).

## Unique Selling Proposition
The only workflow automation platform built for operations teams, not developers. Setup in under 30 minutes with no code.

## Current Marketing Status
Starting fresh. Previous efforts: one blog post, LinkedIn posts by founder.

## Competitors
To be researched in Situation Analysis.

## Notes
Founder has strong network in operations community. Budget: $5K/month initial.
```

#### Step 2: SOSTAC Planning

After brand setup, continue to SOSTAC:

```
/paw-mkt-sostac
Let's build a complete marketing plan for Flowstack.
```

**What gets created (over multiple sessions):**

```
.pawbytes/marketing-suites/brands/flowstack/sostac/
├── README.md                (phase tracker, updated as you progress)
├── 00-auto-discovery.md     (competitive research, audience insights)
├── 01-situation.md          (5S audit, TOWS analysis)
├── 02-objectives.md         (SMART objectives, OKRs)
├── 03-strategy.md           (segmentation, positioning, targeting)
├── 04-tactics.md            (channel plan, content strategy)
├── 05-action.md             (implementation timeline, budgets)
├── 06-control.md            (metrics, measurement framework)
└── plan-summary.md          (executive summary after all phases)
```

**Key behavior during SOSTAC:**

- The skill reads existing brand files before each phase
- It resumes from the first incomplete phase if you return mid-plan
- It drafts each phase for your confirmation before saving
- Earlier phases shape later phases (cross-phase consistency)
- Questions come in batches, not overwhelming single prompts

#### Step 3: Product Marketing Context

After SOSTAC Strategy (Phase 3) is complete, create deep positioning:

```
/product-marketing-context
Now that we have our strategy, let's build detailed positioning with customer language and objection handling.
```

**What gets created:**

```
.pawbytes/marketing-suites/brands/flowstack/paw-mkt-product-context.md
```

This file contains:
- Positioning statement
- Customer language (exact phrases from research)
- Objection handling framework
- Feature-benefit ladder
- Competitor positioning map

#### Step 4: Channel Activation

With strategy and positioning complete, activate channels:

```
/paw-mkt-content
Based on our SOSTAC tactics, build a content plan for the first quarter.
```

Or:

```
/paw-mkt-email
Create a welcome sequence and nurture framework aligned to our SOSTAC objectives.
```

Or:

```
/paw-mkt-seo
Run a technical SEO audit and content keyword strategy for flowstack.com.
```

**File locations for channel work:**

| Channel | Path |
|---------|------|
| Content | `.pawbytes/marketing-suites/brands/flowstack/content/` |
| SEO | `.pawbytes/marketing-suites/brands/flowstack/channels/seo/` |
| Email | `.pawbytes/marketing-suites/brands/flowstack/channels/email/` |
| Social | `.pawbytes/marketing-suites/brands/flowstack/channels/social/` |
| Analytics | `.pawbytes/marketing-suites/brands/flowstack/channels/analytics/` |

### 13.3 Complete Example: New SaaS Brand

**Scenario**: You are launching Flowstack, a workflow automation platform for operations teams.

**Day 1: Setup**

```
/paw-mkt-agency
Set up a brand workspace for Flowstack. We're a workflow automation platform for operations teams at mid-market companies (50-500 employees). Our buyers are operations managers who struggle with cross-tool coordination (Salesforce, Jira, Slack, spreadsheets). We're at early-stage: we have 15 beta customers and are preparing for our first serious marketing investment. Budget is $5K/month. Website is flowstack.com.
```

**Expected response:**

> I've created the Flowstack workspace. Here's what I captured:
>
> - Brand: Flowstack
> - Slug: flowstack
> - Stage: early-stage
> - Website: flowstack.com
> - Product: Workflow automation for ops teams
> - Audience: Ops managers at 50-500 person companies
>
> Files created:
> - `.pawbytes/marketing-suites/brands/flowstack/brand-context.md`
> - `.pawbytes/marketing-suites/brands/flowstack/sostac/README.md`
>
> Should I proceed into SOSTAC planning to build your full marketing strategy?

**Day 1-3: SOSTAC Auto-Discovery and Situation**

```
/paw-mkt-sostac
Let's build the full plan. Start with auto-discovery and situation analysis.
```

**Expected output (00-auto-discovery.md):**

```markdown
# Auto-Discovery: Flowstack

## Competitive Landscape

| Competitor | Positioning | Strength | Weakness |
|------------|-------------|----------|----------|
| Zapier | For everyone, any integration | Massive library, brand awareness | Too technical for ops teams, no workflow visibility |
| Workato | Enterprise automation | Enterprise features, IT-approved | Expensive, requires implementation consultant |
| Tray.io | Technical automation | Flexible, powerful | Developer-centric, complex setup |
| Make (Integromat) | Visual automation | Visual builder | Still requires technical thinking |

**Gap identified**: No platform specifically positions for operations managers. All competitors target developers or IT.

## Audience Language (from Reddit, LinkedIn, community scraping)

**Pain phrases**:
- "My ops team lives in spreadsheets"
- "We have no visibility when things break"
- "I'm the only one who knows how the workflow actually works"
- "Manual tracking is eating 20% of my team's time"

**Hope phrases**:
- "I need something my team can actually use"
- "I want alerts before problems cascade"
- "I need a view of the whole process, not just one integration"

## Market Data

- Mid-market operations teams: ~120K in US
- Average ops team size: 3-5 people
- Typical tools managed: 8-12
- Budget authority: Ops managers typically control $20-50K tool budget
```

**Day 4-6: Objectives and Strategy**

Continue the SOSTAC workflow. The skill asks targeted questions based on Situation findings:

> Based on the competitive gap (no ops-focused positioning) and your early-stage status, I recommend these objectives:
>
> 1. Acquire 50 paying customers in Q2 (from 15 beta)
> 2. Build ops manager awareness: 5K website visitors/month by end of Q2
> 3. Establish ops positioning: 3 case studies from ops leaders published
>
> Does this align with your expectations? Adjust if needed.

After your confirmation, the skill saves `02-objectives.md` and moves to Strategy:

> For Strategy, I recommend segmenting by ops team maturity:
>
> - Segment A: Growing ops teams (company just hired first ops manager) - highest pain, lowest budget authority
> - Segment B: Established ops teams (3+ ops staff, multiple workflows) - highest budget, most urgent
>
> Primary target: Segment B. They have budget authority and urgent cross-tool chaos.
>
> Positioning: "The workflow platform built for operations teams. Setup in 30 minutes. No code required."

### 13.4 Common Mistakes to Avoid

| Mistake | Why It Hurts | Correction |
|---------|--------------|------------|
| Skipping SOSTAC | Tactics become disconnected, specialists work without shared strategy | Always run SOSTAC for new brands before channel activation |
| Starting with paid ads | You burn budget before positioning is validated | Establish positioning and content foundation first |
| Incomplete brand-context | Specialists lack grounding, outputs feel generic | Fill brand-context thoroughly; it feeds every subsequent skill |
| Jumping mid-SOSTAC | Later phases lose connection to earlier insights | Let SOSTAC run sequentially; resume from incomplete phases |
| Multiple brand selection confusion | When you have multiple brands, work may go to wrong workspace | Always confirm brand selection when multiple exist in portfolio |

---

## Chapter 14: Launching a Product

### 14.1 Pre-Launch Phase (T-8 weeks)

The paw-mkt-launch skill coordinates a five-phase timeline for Tier 1 launches. Here is the breakdown:

#### Phase 1: Internal Launch (T-8 to T-6 weeks)

**Goal**: Validate core experience before external eyes see the product.

**Who**: Team, advisors, investors, close professional network (10-30 people).

**Actions**:
- Deploy to staging or limited-access environment
- Invite internal testers with structured feedback instructions
- Fix P0/P1 bugs (crashes, data loss, broken core flows)
- Validate onboarding achieves "aha moment" within 5 minutes
- Finalize messaging: positioning statement, tagline, hero copy

**Command:**

```
/paw-mkt-launch
We're launching Flowstack in 8 weeks. We're at internal testing stage. Help me plan Phase 1.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/campaigns/launch-flowstack-q2/launch/phase-1-internal.md
```

**Gate to advance**: Core experience stable. Messaging locked. Launch date confirmed.

#### Phase 2: Alpha Launch (T-6 to T-4 weeks)

**Goal**: Controlled external validation with real users.

**Who**: 50-200 trusted external users (waitlist power users, loyal customers, community members matching ICP).

**Actions**:
- Send personal invitations (email or DM, not blast)
- Set expectations: "Early access in return for honest feedback"
- Provide structured feedback form
- Monitor activation: who completes core workflow? Where do they drop off?
- Collect testimonials (quotes, case study candidates, video)

**Command:**

```
/paw-mkt-launch
Continue Phase 2 alpha launch. We have 80 waitlist signups. Help me structure the invitation and feedback process.
```

**Gate to advance**: 60-70% of alpha users complete core workflow successfully. 3-5 usable testimonials collected.

#### Phase 3: Beta Launch (T-4 to T-2 weeks)

**Goal**: Expand validation, build buzz, generate social proof at scale.

**Who**: 200-1,000 users (open waitlist intake, community promotion).

**Actions**:
- Open public waitlist or beta application page
- Begin teaser campaign: "something is coming" on social channels
- Post in relevant communities (Reddit, Slack, Discord, Indie Hackers)
- Activate influencer seeding: early access to 5-15 micro-influencers
- Ramp social content: 3-5x per week with teases, problem-centric content
- Begin drafting all launch day content

**Command:**

```
/paw-mkt-launch
We're at T-4 weeks. Help me build the beta teaser campaign and Product Hunt preparation.
```

**Output files:**

```
.pawbytes/marketing-suites/brands/flowstack/campaigns/launch-flowstack-q2/launch/
├── phase-3-beta.md
├── ph-gallery-prep.md
├── launch-content-drafts/
│   ├── blog-post-draft.md
│   ├── email-announcement-draft.md
│   └── social-posts-draft.md
```

**Gate to advance**: 10-30 testimonials ready. All launch content drafted. Product Hunt hunter confirmed.

### 14.2 Launch Week Execution

#### Phase 4: Early Access Launch (T-2 weeks to T-1 day)

**Goal**: Open to wider public while coordinating launch day.

**Actions**:
- Open early access publicly with landing page featuring beta social proof
- Promote waitlist aggressively
- Send early access reminder emails
- Finalize Product Hunt gallery (5-8 screenshots, demo GIF, tagline, first comment)
- Confirm launch supporters list (beta users, community, friends)
- Brief team on launch day roles
- Schedule all social posts
- Final QA pass

#### Phase 5: Full Launch (Launch Day)

**Goal**: Maximum coordinated push across all channels.

**Minute-by-minute schedule:**

| Time (PT) | Action |
|-----------|--------|
| 12:01 AM | Submit to Product Hunt |
| 12:05 AM | Post maker's first comment |
| 8:00 AM | Send supporter email with PH link |
| 9:00 AM | Post in communities (Reddit, Indie Hackers, Slack/Discord) |
| 9:00-6:00 PM | Respond to every PH comment within 30 minutes |
| Throughout | Post milestone celebrations, live Q&A, behind-the-scenes |

**Command:**

```
/paw-mkt-launch
It's launch day. Walk me through the minute-by-minute execution plan and help me respond to Product Hunt comments.
```

### 14.3 Post-Launch Follow-through

After launch day, the skill helps with:

1. **Thank supporters**: Email everyone who voted or commented
2. **Collect case studies**: Follow up with users who shared positive feedback
3. **Analyze results**: Traffic, signups, conversion rate from launch
4. **Plan next announcement**: Build ongoing cadence (not just one launch)

**Command:**

```
/paw-mkt-launch
Launch day is done. Help me build the post-launch follow-up plan and analyze results.
```

**Output files:**

```
.pawbytes/marketing-suites/brands/flowstack/campaigns/launch-flowstack-q2/launch/
├── post-launch-plan.md
├── launch-results-analysis.md
└── announcement-cadence.md
```

### 14.4 Skills That Activate and When

| Phase | Skills That May Activate |
|-------|--------------------------|
| Phase 1 (Internal) | None (internal focus) |
| Phase 2 (Alpha) | paw-mkt-email (alpha invitation sequences) |
| Phase 3 (Beta) | paw-mkt-social (teaser content), paw-mkt-email (beta sequences), paw-mkt-pr (embargo pitches) |
| Phase 4 (Early Access) | marketing-content (landing page), paw-mkt-email (waitlist emails) |
| Phase 5 (Launch Day) | paw-mkt-social (live posting), paw-mkt-pr (press release), paw-mkt-analytics (real-time tracking) |
| Post-launch | paw-mkt-email (thank you sequences), marketing-retention (activation focus), paw-mkt-analytics (results analysis) |

### 14.5 Complete Example: Product Launch Timeline

**Day-by-day breakdown for Flowstack launch:**

| Day | Phase | Action | File Output |
|-----|-------|--------|-------------|
| T-56 | Phase 1 | Internal testing invites sent | `phase-1-internal.md` |
| T-50 | Phase 1 | Feedback sessions completed | Feedback notes in phase file |
| T-45 | Phase 1 | Messaging finalized | `messaging-final.md` |
| T-42 | Phase 2 | Alpha invitations drafted | `alpha-invitation-email.md` |
| T-40 | Phase 2 | Alpha invites sent (50 people) | Email in ESP |
| T-35 | Phase 2 | Feedback form live | `alpha-feedback-form.md` |
| T-30 | Phase 2 | Testimonials collected (3 usable) | `testimonials-raw.md` |
| T-28 | Phase 3 | Waitlist page live | Landing page on site |
| T-25 | Phase 3 | Teaser social campaign begins | `teaser-content-plan.md` |
| T-22 | Phase 3 | Community posts drafted | `community-post-drafts.md` |
| T-20 | Phase 3 | Influencer seeding begins | `influencer-brief.md` |
| T-15 | Phase 3 | Product Hunt hunter confirmed | PH hunter DM confirmation |
| T-14 | Phase 3 | Launch content drafted | `launch-content-drafts/` |
| T-10 | Phase 4 | Early access opens | Landing page update |
| T-7 | Phase 4 | Supporter email drafted | `supporter-email-draft.md` |
| T-5 | Phase 4 | PH gallery finalized | `ph-gallery-final.md` |
| T-3 | Phase 4 | All social posts scheduled | Social scheduler loaded |
| T-1 | Phase 4 | Final QA pass | QA checklist complete |
| T-0 | Phase 5 | LAUNCH DAY | Live execution |
| T+1 | Post-launch | Thank supporters | `thank-you-email.md` |
| T+3 | Post-launch | Results analysis | `launch-results-analysis.md` |
| T+7 | Post-launch | Case study outreach | `case-study-outreach.md` |

---

## Chapter 15: Improving Conversions

### 15.1 The CRO Diagnostic Process

The marketing-cro skill follows a structured diagnostic before producing recommendations. You should expect these questions:

| Question | Why It Matters |
|----------|----------------|
| What is the current conversion rate? | Baseline for measuring improvement |
| What is the goal conversion rate? | Target defines scope of work |
| How is it being measured? | Ensures valid measurement methodology |
| What are primary traffic sources? | Cold vs warm traffic needs different treatment |
| Where do users drop off? | Funnel analytics identify problem location |
| What has already been tested? | Avoid re-testing known losers |
| What platform is the page built on? | Determines implementation constraints |

**If you cannot answer questions 1-3, the skill recommends installing analytics before running tests.**

### 15.2 From Audit to Implementation

#### Step 1: Request the Audit

```
/paw-mkt-cro
Audit our signup landing page at flowstack.com/signup. Current conversion rate is 3.2%. Traffic is primarily from paid LinkedIn ads (cold traffic). We're using HubSpot for the landing page.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/operations/cro/audit-signup-landing-2026-03-31.md
```

#### Step 2: Review the Priority Framework Assessment

The CRO skill applies a universal priority framework. It always works from highest to lowest priority:

1. **Value Proposition Clarity** (most common failure)
2. **Headline Effectiveness**
3. **CTA Placement and Copy**
4. **Visual Hierarchy**
5. **Trust Signals**
6. **Objection Handling**
7. **Friction Points**

**Sample audit output:**

```markdown
# Landing Page Audit: flowstack.com/signup

## Current State
- Conversion rate: 3.2%
- Goal: 5%+
- Traffic: Cold (paid LinkedIn)
- Platform: HubSpot

## Priority Framework Assessment

### P1: Value Proposition Clarity -- FAILING
The headline reads: "Workflow Automation Platform"
This is a category label, not a value proposition. A first-time visitor cannot answer "Is this for me?" in 5 seconds.

**Recommendation**: Rewrite to outcome-led headline targeting ops managers specifically.

### P2: Headline Effectiveness -- FAILING
Current: "Workflow Automation Platform"
- Does not lead with outcome
- No specific number or timeframe
- Reads like company tagline, not customer language

**Recommendation**: "Cut manual tracking from 4 hours to 20 minutes" -- specific, outcome-led, addresses skeptic.

### P3: CTA Placement -- PASSING
Primary CTA above fold. Copy: "Get Started"
This is weak. "Get Started" describes user action, not what happens next.

**Recommendation**: "Start Free Trial" -- describes outcome.

### P4: Visual Hierarchy -- PARTIAL
Headline and CTA visible. But bullets are buried below form.
Scanners miss the key benefits.

**Recommendation**: Move 3 key benefit bullets above form.

### P5: Trust Signals -- MISSING
No customer logos, no testimonials, no review ratings.
Cold traffic needs trust signals to convert.

**Recommendation**: Add 2-3 customer logos + 1 testimonial quote.

### P6: Objection Handling -- MISSING
No FAQ, no risk reduction language.
Cold traffic has price, effort, and relevance objections.

**Recommendation**: Add "Setup in 30 minutes. No code required." near CTA.

### P7: Friction Points -- PARTIAL
Form has 5 fields: name, email, company, role, phone.
Phone field is optional but creates perceived friction.

**Recommendation**: Remove phone field from initial signup.

## Quick Wins (same-day, no developer)
- Rewrite headline: "Cut manual tracking from 4 hours to 20 minutes"
- Rewrite CTA: "Start Free Trial"
- Add trust line: "Setup in 30 minutes. No code required."
- Remove phone field

## High-Impact Changes (1-5 day effort)
- Add customer logos section above form
- Add testimonial quote with photo and company
- Move benefit bullets above form
- Add FAQ section addressing top 3 objections

## Test Hypotheses
1. If we change headline to outcome-led, signup rate will improve 15-25% because cold traffic immediately understands value.
2. If we add trust signals (logos + testimonial), signup rate will improve 10-15% because cold traffic needs credibility before committing.
```

#### Step 3: Implement Quick Wins

Quick wins require no developer. Implement immediately:

```
/paw-mkt-cro
Help me write the specific copy for the Quick Wins so I can update the HubSpot page now.
```

#### Step 4: Plan High-Impact Changes

```
/paw-mkt-cro
Create implementation briefs for the High-Impact Changes. I have a designer available next week.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/operations/cro/implementation-briefs-2026-03-31.md
```

### 15.3 Testing and Measurement

#### When to A/B Test vs Just Ship

| Situation | Action |
|-----------|--------|
| Current version clearly broken (missing CTA, illegible mobile) | Just ship the fix |
| Change is hypothesis with uncertain outcome | Run A/B test |
| Page has sufficient traffic (500+ conversions/month) | A/B test viable |
| Low traffic (<500 conversions/month) | Ship best variant, measure before/after over 60 days |

#### Minimum Sample Size

| Current CVR | Min detectable lift | Visitors per variant |
|-------------|---------------------|----------------------|
| 1% | 20% relative | ~47,000 |
| 3% | 15% relative | ~12,000 |
| 5% | 10% relative | ~15,000 |
| 10% | 10% relative | ~7,500 |

#### Test Priority Order

1. Value proposition / headline (largest potential swing)
2. CTA copy and placement
3. Form length (removing fields)
4. Social proof type and placement
5. Pricing page structure
6. Page layout
7. Button color (smallest impact -- test last)

#### Creating a Test Brief

```
/paw-mkt-cro
Create an A/B test brief for the headline change. We have 8K visitors/month and current CVR is 3.2%.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/operations/cro/test-brief-headline-2026-03-31.md
```

**Sample test brief:**

```markdown
# A/B Test Brief: Headline

## Hypothesis
If we change the headline from "Workflow Automation Platform" to "Cut manual tracking from 4 hours to 20 minutes," signup rate will improve 15-25% because cold traffic immediately understands the specific value.

## Variants

| Variant | Headline Copy |
|---------|---------------|
| Control | "Workflow Automation Platform" |
| A | "Cut manual tracking from 4 hours to 20 minutes" |
| B | "The workflow platform built for operations teams" |

## Primary Metric
Signup conversion rate (visitor to trial signup)

## Secondary Metrics
- Time on page (guardrail: should not decrease)
- Form start rate (leading indicator)

## Sample Size
Current: 8K visitors/month, 3.2% CVR = ~256 conversions/month
Min detectable lift: 15% relative
Required: ~12,000 visitors per variant
Duration: 4-5 months at current traffic

Recommendation: Traffic is borderline for A/B test. Consider shipping variant A and measuring before/after for 60 days instead.

## Success Criteria
Variant A wins if signup rate improves >= 15% relative lift with 95% confidence.
```

### 15.4 Complete Example: Landing Page Optimization

**Scenario**: Flowstack signup page at 3.2% conversion, goal of 5%.

**Week 1: Audit**

```
/paw-mkt-cro
Audit flowstack.com/signup. Current CVR 3.2%. Traffic from LinkedIn ads (cold). Platform is HubSpot.
```

Audit reveals:
- P1 (Value Prop): FAILING
- P2 (Headline): FAILING
- P3 (CTA): PARTIAL
- P5 (Trust): MISSING
- P6 (Objections): MISSING

**Week 2: Quick Wins**

Implement headline and CTA rewrite in HubSpot:

| Element | Before | After |
|---------|--------|-------|
| Headline | Workflow Automation Platform | Cut manual tracking from 4 hours to 20 minutes |
| CTA | Get Started | Start Free Trial |
| Trust line | (none) | Setup in 30 minutes. No code required. |

**Week 3-4: High-Impact Implementation**

Designer creates:
- Customer logo section (3 logos from beta users)
- Testimonial quote with photo
- FAQ section addressing setup time, pricing, integration support

**Week 5: Measure Results**

After 30 days with Quick Wins only:

| Metric | Before | After | Change |
|---------|--------|-------|--------|
| CVR | 3.2% | 3.8% | +18.7% |

After 30 days with High-Impact changes:

| Metric | Before Quick Wins | After All Changes | Total Change |
|---------|-------------------|-------------------|--------------|
| CVR | 3.2% | 4.9% | +53% |

Goal of 5% nearly achieved. Additional iteration on form fields pushes to 5.3%.

---

## Chapter 16: Building an Email Program

### 16.1 Strategy First Approach

Before writing any email, the paw-mkt-email skill requires strategy alignment.

**Start by defining email's role:**

```
/paw-mkt-email
Based on our SOSTAC objectives (acquisition focus), define email's role in our marketing mix and recommend which sequences to prioritize.
```

**Sample output:**

```markdown
# Email Strategy: Flowstack

## Channel Role
Primary acquisition channel. Email captures leads from content and paid channels, then nurtures toward trial signup.

## SOSTAC Alignment
Objective: Acquire 50 paying customers Q2
Email priority: Welcome + Nurture sequences for lead capture

## Recommended Sequences (Priority Order)
1. Welcome Sequence (3-7 emails, 0-14 days) -- for lead magnet downloads
2. Nurture Sequence (weekly/biweekly) -- ongoing value delivery
3. Sales Sequence (3-7 emails, 7-14 days) -- triggered by high-intent behavior
4. Post-Trial Sequence -- for trial signups who don't convert

## Not Recommended Yet
- Re-engagement (no dormant subscribers yet)
- Winback (no lapsed customers yet)
```

### 16.2 Sequence Design Process

#### Step 1: Define Sequence Type

```
/paw-mkt-email
I want to create a welcome sequence for Flowstack. We're offering a "Workflow Audit Template" as lead magnet. Our goal is trial signup.
```

#### Step 2: Review Sequence Framework

The skill loads from `./references/frameworks-index.csv` and reads the matched welcome sequence framework.

**Sample welcome framework (5-email):**

| Email | Day | Purpose | Content |
|-------|-----|---------|---------|
| 1 | 0 | Deliver lead magnet + set expectations | Template + "what to expect" |
| 2 | 3 | Brand story + credibility | Why we built this, founder story |
| 3 | 7 | Quick win + social proof | How to use template + customer example |
| 4 | 10 | Soft offer | Trial invitation with specific value |
| 5 | 14 | Conversion CTA | Direct trial signup push + urgency |

#### Step 3: Write Emails

```
/paw-mkt-email
Write the 5-email welcome sequence for Flowstack. Use the positioning from paw-mkt-product-context.md.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/email/content/welcome-sequence.md
```

### 16.3 Integration with Content

Email sequences integrate with content strategy:

- Welcome sequence delivers lead magnet (created by marketing-content)
- Nurture sequence repurposes blog content (created by marketing-content)
- Sales sequence links to case studies (created by marketing-content)

**Command:**

```
/paw-mkt-email
Create a nurture sequence that repurposes our Q1 blog content. We have 4 published posts: "The Ops Manager's Guide to Workflow Automation", "5 Signs Your Team Needs Process Visibility", "How to Build Cross-Tool Alert Systems", "Spreadsheet vs Automation: Cost Comparison".
```

**Output:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/email/content/nurture-sequence-q1.md
```

### 16.4 Complete Example: Welcome + Nurture Series

**Scenario**: Flowstack needs email sequences for lead capture.

**Email 1: Lead Magnet Delivery (Day 0)**

```
Subject: Your Workflow Audit Template is ready

Hi [Name],

Thanks for grabbing the Workflow Audit Template.

Here's your download link:
[Link]

What's inside:
- Audit checklist for your top 5 workflows
- Risk scoring framework
- Quick-fix prioritization matrix

Over the next 2 weeks, I'll send you:
- How real ops teams use this template
- A behind-the-scenes look at how we built Flowstack
- Specific ways to cut your manual tracking time

If you want to jump ahead and see how Flowstack automates the workflows you're auditing, start a free trial here: [Link]

-- Sarah, Founder at Flowstack
```

**Email 2: Brand Story (Day 3)**

```
Subject: Why I built Flowstack after 6 years in ops

Hi [Name],

I spent 6 years running operations at a 200-person company.

The hardest part wasn't the work itself. It was the invisible work.

I had 12 tools to manage. Salesforce for sales. Jira for engineering. Slack for communication. Spreadsheets for everything that didn't fit elsewhere.

And I was the only person who knew how they all connected.

When something broke, I'd get 10 Slack messages asking "why didn't the alert trigger?" -- and I'd have to manually trace through 5 tools to find the answer.

That's why I built Flowstack.

Not for developers. Not for IT. For ops teams who need visibility without becoming technical experts.

Setup takes 30 minutes. No code. You see your whole workflow, not just one integration.

If this sounds familiar, try Flowstack free: [Link]

-- Sarah
```

**Email 3: Quick Win + Social Proof (Day 7)**

```
Subject: How Taylor cut 4 hours of manual tracking

Hi [Name],

Taylor runs ops at a 150-person recruiting firm.

Before Flowstack, she spent 4 hours every Monday manually updating 3 spreadsheets with data from Salesforce and Jira.

Now: 20 minutes.

Here's how she used the Workflow Audit Template you downloaded:

1. Listed her top 3 recurring manual tasks
2. Scored each by time spent + error risk
3. Prioritized the weekly data sync as highest impact

Then she set up Flowstack to:
- Pull candidate status from Salesforce
- Pull interview notes from Jira
- Sync both to her team's tracker automatically

The result: Her team now gets Monday updates at 8am without Taylor touching anything.

Want to see how this would work for your workflows? Start a trial: [Link]

-- Sarah
```

**Email 4: Soft Offer (Day 10)**

```
Subject: Your workflow audit (what to do next)

Hi [Name],

By now you've probably audited a few workflows.

Here's what most ops teams find:

- 2-3 workflows that should be automated (high time, high error risk)
- 1-2 workflows that need better visibility (alerts, dashboards)
- 1 workflow that's actually fine manually (low effort, low risk)

For the first category: Flowstack automates in under 30 minutes.

For the second: Flowstack gives you visibility without needing to change how your tools work.

For the third: Keep doing what you're doing.

If your audit identified at least 2 automatable workflows, Flowstack will likely save 10+ hours per week for your team.

Start a free trial to test it: [Link]

-- Sarah
```

**Email 5: Conversion CTA (Day 14)**

```
Subject: Last email in this series (and an offer)

Hi [Name],

This is the last email in the welcome series.

But it's not the last time we'll talk. I send a monthly ops workflow tip to subscribers who stay on the list.

Before I switch to monthly: one offer.

If you haven't tried Flowstack yet, here's a reason to do it this week:

I'm offering a 30-minute setup call for anyone who starts a trial before Friday.

We'll set up your first workflow together. No technical knowledge needed. You'll see automation working before the call ends.

Book your trial + setup call here: [Link]

After Friday, setup calls go back to paid customers only.

-- Sarah
```

**File saved to:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/email/content/welcome-sequence-5-email.md
```

---

## Chapter 17: SEO Optimization

### 17.1 Technical Foundation First

The marketing-seo skill always starts with technical SEO. Content optimization without technical foundation is wasted effort.

**Start the audit:**

```
/paw-mkt-seo
Run a technical SEO audit on flowstack.com. We're a new site with 15 pages. Priority is establishing crawlability and indexation foundation.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/seo/audit-technical-2026-03-31.md
```

**Sample technical audit output:**

```markdown
# Technical SEO Audit: flowstack.com

## Site Overview
- Pages indexed: 15
- Domain age: 6 months
- Platform: Next.js on Vercel

## P1 Issues (Critical)

### 1. Missing XML Sitemap
No sitemap.xml found. Google cannot efficiently discover all pages.

**Fix**: Generate sitemap.xml with all 15 pages. Submit via Google Search Console.

### 2. Robots.txt Blocks CSS/JS
Current robots.txt disallows /assets/ which contains CSS and JS files.
Google cannot render pages properly.

**Fix**: Update robots.txt to allow /assets/.

### 3. No Canonical Tags
Pages lack self-referencing canonicals. Risk of duplicate content issues.

**Fix**: Add canonical tag to every page pointing to its own URL.

## P2 Issues (Important)

### 4. Slow LCP on Homepage
LCP: 4.2s (target: 2.5s)
Hero image is 2.8MB unoptimized.

**Fix**: Compress hero image to WebP, preload in HTML.

### 5. Missing Meta Descriptions
8 of 15 pages have no meta description.
CTR in SERP will be reduced.

**Fix**: Write unique meta descriptions (150-160 characters) for all pages.

### 6. No Schema Markup
Zero structured data. Missing opportunity for rich snippets.

**Fix**: Implement Organization schema on homepage, SoftwareApplication schema on product page.

## P3 Issues (Enhancement)

### 7. H1 Tag Inconsistent
Some pages have multiple H1s. Some have H1s that are logos (image).

**Fix**: One H1 per page. H1 should be the page's main topic.

### 8. Internal Linking Weak
Homepage links to only 3 other pages. Deep pages have 0 internal links.

**Fix**: Add contextual internal links from blog posts to product page.

## Action Plan

| Issue | Priority | Effort | Impact |
|-------|----------|--------|--------|
| XML sitemap | P1 | 30 min | High |
| Robots.txt fix | P1 | 10 min | High |
| Canonical tags | P1 | 1 hour | Medium |
| LCP optimization | P2 | 2 hours | High |
| Meta descriptions | P2 | 2 hours | Medium |
| Schema markup | P2 | 3 hours | Medium |

Recommended order: P1 items this week. P2 items next week.
```

### 17.2 Content SEO Workflow

After technical foundation, move to content SEO:

#### Step 1: Keyword Research

```
/paw-mkt-seo
Based on our SOSTAC positioning (workflow automation for ops teams), research target keywords. Focus on terms ops managers would search.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/seo/keyword-strategy-2026-03-31.md
```

**Sample keyword output:**

```markdown
# Keyword Strategy: Flowstack

## Primary Target Keywords

| Keyword | Volume | Difficulty | Intent | Priority |
|---------|--------|------------|--------|----------|
| workflow automation | 12K | 68 | Informational | P2 |
| operations automation | 1.8K | 35 | Informational | P1 |
| cross-tool workflow | 320 | 15 | Informational | P1 |
| workflow visibility | 480 | 22 | Informational | P1 |
| manual workflow tracking | 180 | 8 | Problem | P1 |

## Secondary Keywords (Long-tail)

| Keyword | Volume | Intent | Content Type |
|---------|--------|--------|--------------|
| how to automate workflow without coding | 240 | How-to | Guide |
| best workflow tools for operations teams | 540 | Comparison | Listicle |
| workflow automation for mid-market companies | 90 | Research | Case study |
| reduce manual tracking time | 120 | Problem | Guide |

## Content Plan

| Target Keyword | Content Title | Type | Priority |
|----------------|---------------|------|----------|
| operations automation | The Ops Manager's Guide to Workflow Automation | Guide | P1 |
| workflow visibility | 5 Signs Your Team Needs Workflow Visibility | Listicle | P1 |
| cross-tool workflow | How to Build Cross-Tool Workflow Visibility | How-to | P1 |
| workflow automation | Workflow Automation: Complete Guide for 2026 | Pillar | P2 |
```

#### Step 2: Content Optimization

```
/paw-mkt-seo
Optimize our existing blog post "The Ops Manager's Guide to Workflow Automation" for target keyword "operations automation".
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/seo/content/ops-guide-optimization.md
```

**Sample optimization recommendations:**

```markdown
# Content Optimization: Ops Manager's Guide

## Current State
- Title: "The Ops Manager's Guide to Workflow Automation"
- Target keyword: "operations automation"
- Current position: Not indexed

## Optimization Actions

### Title
Current: "The Ops Manager's Guide to Workflow Automation"
Optimized: "Operations Automation: The Complete Guide for Ops Managers"

Reason: Primary keyword in first 60 characters.

### H1
Current: "Workflow Automation for Operations Teams"
Optimized: "Operations Automation Guide: From Manual to Automated"

Reason: Keyword present, benefit clear.

### Meta Description
Current: (missing)
Optimized: "Learn operations automation from setup to scale. Cut manual tracking time, build workflow visibility, and automate cross-tool processes without code."

Reason: Keyword present, benefit-led, 155 characters.

### First Paragraph
Add keyword in first 100 words:
"Operations automation transforms how mid-market ops teams manage cross-tool workflows. This guide shows you how to cut manual tracking from hours to minutes."

### Subheadings
Add H2 with keyword:
H2: "What is Operations Automation?"
H2: "5 Operations Automation Use Cases"
H2: "Operations Automation Tools Comparison"

### Internal Links
Add links to:
- Product page (from "operations automation tools" section)
- "5 Signs Your Team Needs Workflow Visibility" post

### Schema
Add Article schema with headline, author, datePublished.
```

### 17.3 Measuring Results

#### SEO Metrics to Track

| Metric | Tool | Frequency |
|--------|------|-----------|
| Indexed pages | Google Search Console | Weekly |
| Organic impressions | GSC | Weekly |
| Organic clicks | GSC | Weekly |
| Keyword positions | GSC + Ahrefs | Weekly |
| Organic traffic | GA4 | Monthly |
| Backlinks | Ahrefs | Monthly |

#### Monthly SEO Report

```
/paw-mkt-seo
Generate an SEO progress report for March. Compare to February baseline.
```

**Output file:**

```
.pawbytes/marketing-suites/brands/flowstack/channels/seo/monthly-report-2026-03.md
```

### 17.4 Complete Example: Technical + Content SEO Project

**Week 1: Technical Foundation**

```
/paw-mkt-seo
Run technical audit on flowstack.com. Prioritize crawlability and indexation.
```

Audit reveals P1 issues: missing sitemap, robots.txt blocking assets, no canonicals.

**Implementation (same week):**
- Generate and submit sitemap.xml
- Fix robots.txt
- Add canonical tags to all pages

**Week 2: Technical P2 + Keyword Research**

```
/paw-mkt-seo
Fix P2 technical issues (LCP, meta descriptions, schema). Then research keywords for ops automation positioning.
```

**Implementation:**
- Compress hero image (LCP from 4.2s to 2.1s)
- Write meta descriptions for all 15 pages
- Add Organization and SoftwareApplication schema

**Keyword research identifies:**
- "operations automation" (1.8K volume, 35 difficulty) - P1 target
- "workflow visibility" (480 volume, 22 difficulty) - P1 target
- "cross-tool workflow" (320 volume, 15 difficulty) - P1 target

**Week 3-4: Content Optimization**

```
/paw-mkt-seo
Optimize existing blog content for target keywords. Create one new pillar page for "operations automation".
```

**Optimized:**
- "Ops Manager's Guide" for "operations automation"
- "5 Signs Your Team Needs Visibility" for "workflow visibility"

**Created:**
- New pillar: "Operations Automation: Complete Guide for 2026"

**Week 5-8: Indexation and Measurement**

After 8 weeks:

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Indexed pages | 8 | 18 | +10 |
| Organic impressions | 120 | 1,840 | +1,533% |
| Organic clicks | 5 | 48 | +860% |
| Avg position (top 10 keywords) | Not tracked | 24.5 | New baseline |

**Keywords in top 50:**
- "operations automation": Position 28
- "workflow visibility": Position 18
- "cross-tool workflow": Position 12

---

## Summary

| Workflow | Starting Command | Key Output Path |
|----------|------------------|-----------------|
| New Brand | `/paw-mkt-agency` | `brands/{slug}/brand-context.md` |
| SOSTAC Planning | `/paw-mkt-sostac` | `brands/{slug}/sostac/*.md` |
| Product Launch | `/paw-mkt-launch` | `brands/{slug}/campaigns/launch-{name}/` |
| CRO Audit | `/paw-mkt-cro` | `brands/{slug}/operations/cro/audit-*.md` |
| Email Sequence | `/paw-mkt-email` | `brands/{slug}/channels/email/content/` |
| SEO Audit | `/paw-mkt-seo` | `brands/{slug}/channels/seo/audit-*.md` |

All workflows follow the same pattern:
1. Read brand and SOSTAC context first (Pre-Flight)
2. Research before recommending
3. Draft for confirmation before saving
4. Save to resolved path
5. Recommend next steps