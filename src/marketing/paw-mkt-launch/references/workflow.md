# Launch Campaign Workflow

This reference defines the standard workflow, tier classification decision tree, phase gates, ORB channel activation checklists, escalation routes, and ethical guidelines for all product launch work.

---

## Workflow Overview

The launch workflow moves through six phases (Phase 0 through Phase 5). Phase 0 establishes prerequisites and classifies the launch tier. Phases 1-5 follow the Five-Phase Timeline with explicit gates between each phase. The tier classification determines the depth and breadth of each subsequent phase.

```
Phase 0: Prerequisites & Tier Classification
    |
    +-- SOSTAC exists? --NO--> Escalate to paw-mkt-sostac --> Return
    |
    +-- YES
    |
    +-- Tier Classification Decision Tree
    |       |           |           |
    |    Tier 1      Tier 2      Tier 3
    |   (Full)     (Scaled)   (Changelog)
    |       |           |           |
Phase 1: Strategy & Planning (T-8 weeks / T-4 weeks / N/A)
    |
    +-- GATE: Launch brief approved, channel plan complete, team assigned
    |
Phase 2: Asset Creation (T-6 weeks / T-3 weeks / T-1 week)
    |
    +-- GATE: All launch assets complete and reviewed
    |
Phase 3: Pre-Launch (T-2 weeks / T-1 week / N/A)
    |
    +-- GATE: Early access seeded, launch day plan confirmed
    |
Phase 4: Launch Day (T-0)
    |
    +-- GATE: All channels activated, real-time monitoring active
    |
Phase 5: Post-Launch (T+1 to T+4 weeks / T+1 to T+2 weeks / T+1 week)
```

---

## Diagnostic Questions

Ask these before producing any launch plan. A launch without this context is a press release with no strategy.

1. **Launch subject**: What specifically is being launched? New product, major feature, minor feature, partnership, or patch?
2. **SOSTAC availability**: Does a SOSTAC plan exist for this brand? If not, this is the first prerequisite.
3. **Launch tier**: Is this a Tier 1 (full treatment), Tier 2 (scaled), or Tier 3 (changelog)? See the Tier Classification Decision Tree below.
4. **Target date**: What is the target launch date? Is it fixed (event-driven) or flexible?
5. **Owned channels**: What does the brand currently own? Email list size, social accounts and follower counts, community size, blog traffic.
6. **Product Hunt**: Is Product Hunt part of the plan? Does the brand have a support network that can upvote?
7. **Press and media**: Is there a PR budget? Existing journalist relationships? Previous media coverage?
8. **Partners and influencers**: Are there partners, influencers, or early users who can be activated for launch?
9. **Success metrics**: What does success look like? Signups, revenue, press mentions, Product Hunt ranking, other?
10. **Team**: Who is available for launch execution? Marketing, engineering, design, founder?

If no SOSTAC plan exists, escalate to paw-mkt-sostac before proceeding. A launch without strategic context is a tactical exercise disconnected from business goals.

---

## Phase 0: Prerequisites & Tier Classification

**Purpose**: Verify strategic prerequisites are met, assess the launch type, and determine the tier that drives all subsequent planning.

### Entry Conditions
- User has requested launch planning or execution
- Product or feature to be launched is identified

### SOSTAC Prerequisite Check

The SOSTAC plan is the entry condition for all launch work. Check for:
- `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/` directory exists
- At minimum, Situation Analysis and Objectives phases are complete
- Strategy phase provides positioning and audience intelligence

**If SOSTAC does not exist**: Stop. Escalate to paw-mkt-sostac. A Tier 1 launch without strategic context wastes resources and misses the audience. Tier 2 and Tier 3 launches can proceed with minimal context (brand brief or user-provided positioning), but note the risk.

### Tier Classification Decision Tree

```
Is this the first public release of an entirely new product?
  YES --> Tier 1 (Full Treatment)
  NO  --> Continue

Does this launch expand the product's value proposition significantly?
(New pricing tier, new platform, new core capability, new market segment)
  YES --> Tier 1 (Full Treatment)
  NO  --> Continue

Is this a partnership launch requiring cross-brand coordination?
  YES --> Tier 1 (Full Treatment)
  NO  --> Continue

Is this a meaningful feature that improves existing workflows?
(New integration, new template library, significant UI improvement)
  YES --> Tier 2 (Scaled Treatment)
  NO  --> Continue

Is this a bug fix, performance improvement, or minor polish?
  YES --> Tier 3 (Changelog Only)
  NO  --> Tier 2 (default for anything that does not clearly fit above)
```

### Tier Summary

| Dimension | Tier 1 (Full) | Tier 2 (Scaled) | Tier 3 (Changelog) |
|-----------|---------------|------------------|---------------------|
| Timeline | T-8 weeks | T-4 weeks | T-1 week |
| ORB activation | Full: all owned, rented, and borrowed channels | Partial: blog + email + social | Minimal: changelog + tweet |
| Product Hunt | Yes (if applicable) | No | No |
| Press outreach | Yes | No | No |
| Influencer seeding | Yes (5-15 creators) | Optional (1-3 creators) | No |
| Content suite | Full: blog, email, social, PH, press | Blog + email + 3-5 social posts | Changelog entry + 1 social post |
| Landing page | Dedicated launch page | Feature announcement page or blog | None (in-app notification) |
| Team required | Marketing + engineering + design + founder | Marketing + engineering | Engineering only |
| Post-launch duration | 4 weeks | 2 weeks | 1 week |

### Key Activities
- Verify SOSTAC prerequisite
- Classify launch type (new product, major feature, minor feature, patch, partnership, category entry)
- Determine tier using the decision tree
- Confirm target launch date and flexibility
- Inventory owned channels: email list size, social followers, community members, blog traffic
- Identify available team members and assign initial roles

### Deliverables
- Tier classification document with rationale
- Launch type assessment
- Channel inventory summary
- Preliminary timeline based on tier

### Exit Conditions
- SOSTAC plan exists or is in progress (Tier 1 requirement) or user provides equivalent context (Tier 2-3)
- Tier is classified and agreed upon
- Target date is confirmed
- Channel inventory is documented

---

## Phase 1: Strategy & Planning

**Purpose**: Build the launch brief, define the channel strategy, and assemble the team. Timeline: T-8 weeks for Tier 1, T-4 weeks for Tier 2. Tier 3 skips this phase.

### Entry Conditions
- Tier classification is complete (Phase 0 exit)
- SOSTAC context is loaded
- Target date is confirmed

### Key Activities — Tier 1
- Write the launch brief:
  - Product/feature description and value proposition
  - Target audience (primary and secondary personas)
  - Key messages (3 core messages, adapted per channel)
  - Success metrics with specific targets (signups, revenue, press mentions, PH ranking)
  - Budget allocation across channels
  - Risk assessment and contingency plan
- Design the ORB channel strategy:
  - **Owned**: Email sequences, blog content, in-product announcements, landing page, community posts
  - **Rented**: Paid social, paid search, retargeting, sponsored content
  - **Borrowed**: Press outreach, influencer seeding, Product Hunt, guest posts, podcast appearances, community posts in third-party communities
- Build the ORB channel plan with owners:
  - Assign owner per channel
  - Define content requirements per channel
  - Set timeline milestones per channel
  - Establish the "attention funnel": borrowed/rented -> owned (every tactic must have a path to email opt-in or product signup)
- Assemble the team:
  - Marketing lead: owns the launch brief and coordinates execution
  - Engineering: ensures product stability, launch day monitoring, feature flags
  - Design: launch assets, landing page, Product Hunt gallery
  - Founder/CEO: press interviews, community engagement, Product Hunt first comment
- Begin press and influencer outreach planning:
  - Build journalist target list (10-20 relevant journalists)
  - Identify 5-15 micro-influencers or content creators in the category
  - Draft embargo pitch and influencer outreach templates

### Key Activities — Tier 2
- Write abbreviated launch brief (product description, key messages, success metrics)
- Plan blog + email + social content
- Assign owner for each content piece
- No press outreach, no Product Hunt, no influencer seeding (unless opportunistic)

### Deliverables
- Launch brief document
- ORB channel plan with owners and timeline
- Press and influencer target lists (Tier 1 only)
- Team roster with roles and responsibilities

### Exit Conditions
- Launch brief is approved by stakeholders
- ORB channel plan is complete with owners assigned
- All team members are briefed and committed
- Press and influencer lists are built (Tier 1)

---

## Phase 2: Asset Creation

**Purpose**: Produce all launch content — blog posts, email sequences, social posts, ad creative, landing pages, and Product Hunt assets. Timeline: T-6 weeks for Tier 1, T-3 weeks for Tier 2, T-1 week for Tier 3.

### Entry Conditions
- Launch brief is approved (Phase 1 exit)
- ORB channel plan defines all required assets
- Design and content resources are available

### ORB Asset Checklist — Tier 1

#### Owned Channel Assets
- [ ] Launch blog post (1,500-3,000 words: problem, solution, features, social proof, CTA)
- [ ] Email announcement to full list (subject line, preview text, body, CTA)
- [ ] Email sequence for waitlist (3-email warm-up: teaser, early access, launch day)
- [ ] Email sequence for early access users (onboarding, activation, feedback request)
- [ ] In-product announcement (banner, modal, or notification)
- [ ] Dedicated landing page with launch messaging and social proof
- [ ] Changelog entry with technical details
- [ ] Community post (Discord, Slack, forum — if applicable)

#### Rented Channel Assets
- [ ] Social media launch posts (platform-specific: LinkedIn, Twitter/X, Instagram, TikTok)
  - Minimum: 5-8 posts per platform across launch week
  - Mix: announcement, feature highlight, social proof, behind-the-scenes, CTA
- [ ] Paid ad creative (if budget allocated): 3-5 variants per platform
- [ ] Retargeting creative for launch page visitors who did not convert

#### Borrowed Channel Assets
- [ ] Product Hunt gallery: 5-8 screenshots, 1 demo GIF, 260-character tagline, first comment draft
- [ ] Press kit: press release, founder bio, product screenshots, logo files, key metrics
- [ ] Influencer briefing kit: product access, key messages, asset library, share suggestions
- [ ] Guest post drafts for partner or industry blogs (if applicable)
- [ ] Podcast talking points (if appearances are scheduled)

### ORB Asset Checklist — Tier 2
- [ ] Launch blog post (800-1,500 words)
- [ ] Email announcement to full list
- [ ] 3-5 social media posts
- [ ] In-product announcement
- [ ] Changelog entry

### ORB Asset Checklist — Tier 3
- [ ] Changelog entry
- [ ] 1 social media post (Twitter/X or LinkedIn)
- [ ] In-app notification (if applicable)

### Key Activities
- Produce all assets on the ORB checklist for the appropriate tier
- Review all content for message consistency across channels
- Stage landing page and test conversion flow
- Prepare Product Hunt submission (Tier 1): gallery, tagline, first comment, maker profile
- Schedule all social posts in advance
- Set up email sequences in the automation platform
- Create launch day run sheet with exact timing for each channel activation

### Deliverables
- Complete set of launch assets per the tier-appropriate ORB checklist
- Launch day run sheet with timing and owners
- Product Hunt submission (Tier 1, staged and ready)
- All content staged and scheduled

### Exit Conditions
- Every item on the tier-appropriate ORB checklist is complete and reviewed
- Landing page is live (or staged) and conversion flow is tested
- All email sequences are built and tested
- Social posts are scheduled
- Launch day run sheet is distributed to the team

---

## Phase 3: Pre-Launch

**Purpose**: Seed early access, build anticipation, activate influencers, and confirm launch day coordination. Timeline: T-2 weeks for Tier 1, T-1 week for Tier 2. Tier 3 skips this phase.

### Entry Conditions
- All launch assets are complete (Phase 2 exit)
- Product is stable and ready for external users
- Influencer and press outreach lists are ready (Tier 1)

### Key Activities — Tier 1
- Seed early access:
  - Invite 50-200 trusted external users (power users, waitlist top, community members)
  - Personal invitations, not mass blast: "You are getting early access because..."
  - Collect testimonials and social proof from early access users
  - Monitor activation: are they completing the core workflow?
- Build anticipation:
  - Begin teaser campaign on social channels ("something is coming" without full reveal)
  - Post in relevant communities with genuine context (Reddit, Slack groups, Discord, Indie Hackers)
  - Share behind-the-scenes content: building process, design decisions, team stories
- Activate influencers:
  - Provide early access to 5-15 micro-influencers with briefing kit
  - Coordinate embargo timing: content goes live on launch day
  - Confirm each influencer's planned content format and channel
- Confirm press:
  - Send final embargo pitch to journalists
  - Confirm embargo lift time aligns with launch day timing
  - Provide press kit with all required assets
- Final coordination:
  - Confirm launch day roles with every team member
  - Test all technical systems: signup flow, payment, email triggers, in-app announcements
  - Stage Product Hunt submission for launch day
  - Send launch supporter briefing: exact time, links, and simple ask ("Upvote and comment at 9am PT")

### Key Activities — Tier 2
- Send early access to top 20-50 users (optional)
- Begin social teaser content (2-3 posts)
- Final QA pass on product and launch assets

### Deliverables
- Early access results: activation rate, testimonials collected, issues identified
- Social proof compilation (quotes, metrics, screenshots)
- Launch supporter briefing email
- Final launch day run sheet (updated with any changes)

### Exit Conditions
- At least 60-70% of early access users complete the core workflow (Tier 1)
- At least 3-5 usable testimonials collected (Tier 1)
- No blocking product issues outstanding
- All launch day coordination confirmed
- Product Hunt submission is staged and ready (Tier 1)
- Launch supporter email is sent (Tier 1)

---

## Phase 4: Launch Day

**Purpose**: Execute coordinated activation across all channels with real-time monitoring and rapid response. Timeline: T-0.

### Entry Conditions
- Pre-launch activities are complete (Phase 3 exit)
- All assets are staged and scheduled
- Team is briefed and available for the full launch day
- Product is stable (no P0/P1 bugs outstanding)

### Launch Day Run Sheet — Tier 1

| Time (Adjust to Target TZ) | Action | Owner | Channel |
|-----------------------------|--------|-------|---------|
| T-1 hour | Final product QA check | Engineering | Product |
| T-0 | Product Hunt submission goes live | Founder/Marketing | Borrowed |
| T-0 | Blog post published | Marketing | Owned |
| T+5 min | Email announcement sent to full list | Marketing | Owned |
| T+10 min | Social posts go live (all platforms) | Marketing | Owned/Rented |
| T+15 min | In-product announcement activated | Engineering | Owned |
| T+15 min | Community posts published | Marketing | Owned/Borrowed |
| T+30 min | Launch supporter reminder sent | Marketing | Borrowed |
| T+1 hour | Press embargo lifts | PR/Marketing | Borrowed |
| T+1 hour | Influencer content goes live | Influencers | Borrowed |
| T+2 hours | First social engagement round (reply to comments, retweet supporters) | Marketing | Owned/Borrowed |
| T+4 hours | Product Hunt engagement: respond to every comment | Founder | Borrowed |
| T+6 hours | Mid-day social boost post | Marketing | Owned |
| T+8 hours | Email to non-openers (subject line variant) | Marketing | Owned |
| T+12 hours | End-of-day social recap | Marketing | Owned |

### Launch Day Run Sheet — Tier 2

| Time | Action | Owner |
|------|--------|-------|
| T-0 | Blog post published | Marketing |
| T+5 min | Email announcement sent | Marketing |
| T+10 min | Social posts go live | Marketing |
| T+15 min | In-product announcement | Engineering |
| T+4 hours | Social engagement round | Marketing |

### Launch Day Run Sheet — Tier 3

| Time | Action | Owner |
|------|--------|-------|
| T-0 | Changelog published | Engineering |
| T+5 min | Social post (1) | Marketing/Engineering |
| T+15 min | In-app notification (if applicable) | Engineering |

### Real-Time Monitoring — Tier 1
- Monitor Product Hunt ranking and comments (respond within 15 minutes)
- Track signup/conversion rates vs targets (hourly)
- Monitor social mentions and sentiment (respond to all mentions)
- Watch for technical issues: site uptime, signup flow errors, payment processing
- Track press coverage as it appears
- Escalation protocol: if site goes down or signup is broken, pause paid promotion and send holding message

### Deliverables
- Launch day execution log (timestamps, actions taken, results)
- Real-time metrics snapshot (hourly for Tier 1)
- Product Hunt final ranking and comment summary (Tier 1)
- Social engagement summary

### Exit Conditions
- All channels have been activated per the run sheet
- No unresolved technical issues
- Initial metrics are captured (first 24 hours)
- All Product Hunt comments are responded to (Tier 1)

---

## Phase 5: Post-Launch

**Purpose**: Review performance, optimize based on data, and build momentum campaigns. Timeline: T+1 to T+4 weeks for Tier 1, T+1 to T+2 weeks for Tier 2, T+1 week for Tier 3.

### Entry Conditions
- Launch day is complete (Phase 4 exit)
- Initial 24-48 hour metrics are available
- Team is available for post-launch activities

### Key Activities — Week 1 (All Tiers)
- Compile launch results:
  - Signups/conversions vs targets
  - Traffic by source (owned, rented, borrowed)
  - Email performance: open rates, click rates, conversion rates
  - Social performance: impressions, engagement, click-throughs
  - Product Hunt results: ranking, upvotes, comments, traffic (Tier 1)
  - Press coverage: articles published, reach, sentiment (Tier 1)
- Identify what worked and what did not:
  - Which channels drove the most signups?
  - Which content performed best?
  - Where did the funnel leak?
  - What was the cost per acquisition by channel?
- Quick optimizations:
  - Retarget launch page visitors who did not convert
  - Send follow-up email to non-converters with social proof from launch day
  - Amplify top-performing social content
  - Fix any friction points identified in the signup or activation flow

### Key Activities — Weeks 2-4 (Tier 1 and Tier 2)
- Momentum campaigns:
  - Customer story series: publish case studies from early adopters
  - Feature deep-dive content: blog posts or videos highlighting specific capabilities
  - Community engagement: AMA, office hours, or feedback sessions
  - Partner co-marketing: joint content with launch partners
- Ongoing press and influencer follow-up (Tier 1):
  - Send follow-up pitches with launch results and traction data
  - Coordinate second-wave influencer content
  - Pursue podcast appearances with launch story
- Activation optimization:
  - Analyze where new signups drop off in the activation flow
  - Build targeted onboarding sequences for launch cohort
  - A/B test activation emails and in-product prompts
- Build the repeatable announcement cadence:
  - Document the launch playbook: what worked, what to repeat, what to skip
  - Set up the ongoing announcement cadence for future Tier 2 and Tier 3 launches
  - Schedule the next announcement (feature update, milestone, case study)

### Post-Launch Performance Benchmarks

| Metric | Tier 1 Target | Tier 2 Target | Tier 3 Target |
|--------|---------------|---------------|---------------|
| Launch day signups | 500-5,000+ (varies by market) | 100-500 | N/A |
| Product Hunt ranking | Top 5 of the day | N/A | N/A |
| Email open rate (launch) | > 35% | > 30% | N/A |
| Email click rate (launch) | > 8% | > 5% | N/A |
| Social engagement rate | > 5% | > 3% | N/A |
| Landing page conversion | > 15% (warm traffic) | > 10% | N/A |
| Press articles | 3-10+ | N/A | N/A |
| Activation rate (7-day) | > 40% of signups | > 35% | N/A |
| Referral from launch cohort | > 10% refer within 30 days | > 5% | N/A |

### Deliverables
- Post-launch performance report with metrics vs targets
- Channel performance breakdown (owned, rented, borrowed)
- Optimization recommendations for ongoing campaigns
- Launch playbook documentation (what to repeat for future launches)
- Announcement cadence plan for next 90 days

### Exit Conditions
- Performance report is complete and distributed to stakeholders
- Optimization actions are identified and assigned
- Launch playbook is documented for future use
- Next announcement is scheduled
- Launch cohort is transitioned to standard onboarding and retention flows

---

## ORB Channel Activation Matrix

This matrix shows which channels activate at each phase, by tier.

### Owned Channels

| Channel | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|---------|---------|---------|---------|---------|---------|
| Email list | Plan sequences | Build sequences | Warm-up/teaser | Launch blast | Follow-up/nurture |
| Blog | Plan content | Write post | Stage | Publish | Deep-dive series |
| Landing page | Plan | Build/test | Stage | Live | Optimize |
| In-product | Plan placement | Build announcement | Test | Activate | Iterate |
| Community (owned) | Brief members | Prepare content | Tease | Announce | Engage |

### Rented Channels

| Channel | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|---------|---------|---------|---------|---------|---------|
| Paid social | Plan budget | Create ads | -- | Launch campaigns | Optimize/retarget |
| Paid search | Plan keywords | Create ads | -- | Launch campaigns | Optimize |
| Retargeting | Plan audiences | Create creative | -- | Activate | Expand |

### Borrowed Channels

| Channel | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|---------|---------|---------|---------|---------|---------|
| Product Hunt | Plan strategy | Build gallery | Stage submission | Submit/engage | Follow up |
| Press/media | Build list | Write press kit | Pitch under embargo | Embargo lifts | Follow-up pitches |
| Influencers | Identify targets | Brief/provide access | Seed content | Content goes live | Second wave |
| Communities (3P) | Identify targets | Prepare posts | Tease where appropriate | Post | Engage/follow up |
| Podcasts | Identify shows | Pitch/schedule | Record | Air | Promote episodes |

---

## Escalation Routes

| Situation | Route To | Why |
|-----------|----------|-----|
| No SOSTAC plan exists | paw-mkt-sostac | Strategic foundation required before Tier 1 launch |
| Press release and journalist outreach | paw-mkt-pr | Media relations and press distribution expertise |
| Post-launch email sequences | paw-mkt-email | Drip campaigns, automation, and deliverability |
| Paid retargeting and ad campaigns | paw-mkt-paid-ads | Ad creative, targeting, and budget optimization |
| Influencer seeding and management | paw-mkt-influencer | Creator relationships and campaign coordination |
| Community building post-launch | paw-mkt-community | Community platform strategy and engagement |
| SEO optimization of launch content | paw-mkt-seo | Technical SEO and content optimization |
| Video production for launch | paw-mkt-video | Video scripting, production, and optimization |
| Analytics and attribution setup | paw-mkt-analytics | Tracking infrastructure and measurement framework |
| Landing page conversion optimization | paw-mkt-cro | Page optimization and A/B testing |
| Product positioning refinement | paw-mkt-product-context | Positioning, differentiation, and persona updates |
| Referral program for launch cohort | paw-mkt-referral | Referral program design and activation |
| Pricing strategy for launch | paw-mkt-pricing | Pricing model, tier packaging, and launch pricing |

---

## Ethics: Honest Launch Marketing

Launches create concentrated attention. That attention carries responsibility. Overpromising during a launch creates a wave of disappointed customers who churn, leave negative reviews, and warn others.

### Ethical Launch Practices

- **Honest product state**: Do not launch with known critical bugs. If the product is beta-quality, label it beta.
- **Accurate claims**: Every metric, testimonial, and capability claim in launch materials must be verifiable.
- **Genuine social proof**: Launch day testimonials come from real early access users, not fabricated quotes.
- **Transparent limitations**: If the product has known limitations, acknowledge them. "Coming soon" is honest; pretending it exists is not.
- **Product Hunt integrity**: Do not buy upvotes, use vote rings, or coordinate inauthentic voting. Violation risks permanent ban and brand damage.
- **Press honesty**: Press materials include accurate metrics and do not exaggerate traction, funding, or user counts.
- **Launch pricing clarity**: If launch pricing is temporary, state the duration and future price clearly.

### The Day-After Test

Before publishing any launch claim, ask: **If a journalist fact-checked this claim tomorrow, would it hold up?** If the answer is no, revise or remove it.

---

## Path Resolution

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/launch/`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/launch/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All launch work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|-------------|----------|--------------|
| Tier Classification | `tier-classification-{YYYY-MM-DD}.md` | Launch type, tier decision rationale, channel inventory |
| Launch Brief | `launch-brief-{YYYY-MM-DD}.md` | Product description, key messages, success metrics, budget, timeline |
| ORB Channel Plan | `orb-channel-plan-{YYYY-MM-DD}.md` | Channel-by-channel plan with owners, content requirements, timeline |
| Launch Content Suite | `content/` directory | Blog post, email sequences, social posts, Product Hunt assets, press kit |
| Launch Day Run Sheet | `launch-day-runsheet-{YYYY-MM-DD}.md` | Minute-by-minute execution plan with owners |
| Post-Launch Report | `post-launch-report-{YYYY-MM-DD}.md` | Metrics vs targets, channel performance, optimization recommendations |
| Launch Playbook | `launch-playbook-{YYYY-MM-DD}.md` | Documented lessons, repeatable process, announcement cadence plan |

---

## Response Protocol

When the user requests launch planning or execution:

1. **Check SOSTAC prerequisite** -- if no SOSTAC plan exists, escalate to paw-mkt-sostac before proceeding with Tier 1 launches
2. **Route starting context** (blank-page, codebase, or live URL) -- see `./references/shared-patterns.md`
3. **Read strategic context** -- SOSTAC plan, brand positioning, and audience intelligence
4. **Classify the launch tier** using the Tier Classification Decision Tree
5. **Assess current phase** -- has planning started? Are assets in progress? Is launch day imminent?
6. **Deliver phase-appropriate output** -- brief, channel plan, content drafts, run sheet, or post-launch analysis depending on where the user is in the timeline
7. **Apply the tier-appropriate ORB checklist** -- do not over-invest in Tier 3 work or under-invest in Tier 1
8. **Save deliverables** to the resolved path
9. **Recommend next phase** -- what to do next, gate criteria to advance, who needs to act
