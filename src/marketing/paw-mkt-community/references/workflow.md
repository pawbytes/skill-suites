# Community Workflow: Community Flywheel Lifecycle

This reference defines the standard workflow, diagnostic questions, phase gates, and measurement methodology for all community building and management work.

---

## Core Principle: A Community With Zero Content on Launch Day Feels Dead

The most common community failure is launching to an empty space and expecting members to create the energy. They will not. Communities require seeded content, founding members, and intentional culture design BEFORE opening to the public.

**Phase 3 (Founding Members) MUST be completed before Phase 4 (Launch Execution).** Launching without founding members and seeded content creates a ghost town that is nearly impossible to recover. First impressions are permanent -- a member who joins an empty community rarely returns.

---

## Phase 1: Strategy & Purpose

### Purpose
Define the community's reason for existing, its business goal, target audience, and how success will be measured. A community without a clear purpose becomes a support forum by default.

### Entry Conditions
- User has requested community-related work
- Brand context loaded (or acknowledged as unavailable)
- SOSTAC plan consulted if available

### Key Activities

#### 1.1 Define Community Type

Every community serves a dominant function. Mixing too many functions dilutes focus.

| Community Type | Primary Function | Business Value | Example |
|---|---|---|---|
| Product community | User help, feature requests, best practices | Reduces support costs, increases retention | Figma Community, Notion |
| Learning community | Courses, workshops, skill building | Drives product adoption, premium upsell | Maven, Reforge |
| Networking community | Peer connections, introductions, events | Membership revenue, referral pipeline | YC alumni, Pavilion |
| Practice community | Shared craft, methodology, tools | Thought leadership, recruitment pipeline | dbt community, DevRel |
| Brand community | Fan engagement, exclusivity, early access | Advocacy, word-of-mouth, launch amplification | Glossier Into The Gloss |

#### 1.2 Clarify Business Goal

A community must serve the business. Altruistic communities without business alignment lose funding and die.

| Business Goal | How Community Delivers | Key Metric |
|---|---|---|
| Reduce support costs | Peer-to-peer answers deflect tickets | Support ticket deflection rate (target: 20-40%) |
| Increase retention | Social bonds create switching costs | NRR lift (target: 5-15 point improvement) |
| Drive acquisition | Member referrals and content amplification | Community-attributed signups (target: 10-20% of new users) |
| Enable upsell | Power users discover advanced use cases | Expansion revenue from community members vs non-members |
| Build moat | Network effects make product more valuable | Member-generated content volume, DAU/MAU ratio |

#### 1.3 Define Target Audience

Be specific -- "our customers" is not a target audience. Define:

- **Who**: Job title, company size, experience level
- **Why they would join**: What value do they get that they cannot get elsewhere?
- **Where they already gather**: What platforms and communities do they currently use?
- **Engagement capacity**: How much time can they realistically invest? (Executives: 15 min/week. Practitioners: 1-2 hours/week.)

#### 1.4 Set Success Metrics

Define metrics BEFORE launch so there is a clear measurement baseline.

| Metric | 30-Day Target | 90-Day Target | 6-Month Target |
|---|---|---|---|
| Total members | 50-100 (founding) | 200-500 | 1,000+ |
| Weekly active members (WAM) | 30-40% of total | 25-35% of total | 20-30% of total |
| Posts per week | 15-25 (mostly seeded) | 40-80 (50%+ organic) | 100+ (80%+ organic) |
| Member-to-member replies | 20%+ of threads | 40%+ of threads | 60%+ of threads |
| Time to first response | Under 4 hours | Under 2 hours | Under 1 hour |

### Deliverables
- Community strategy document: type, business goal, audience, success metrics
- Community positioning statement: "This is the community for [audience] who want to [outcome] through [mechanism]"

### Exit Conditions
- Community type and business goal clearly defined
- Target audience specified with detail (not generic)
- Success metrics set with 30/90/180-day targets
- Positioning statement written and reviewed

---

## Phase 2: Platform Selection

### Purpose
Choose the right platform based on audience behavior, community type, and operational requirements. Platform choice is a 1-3 year commitment -- switching platforms loses 30-60% of members.

### Entry Conditions
- Phase 1 complete: strategy and audience defined

### Key Activities

#### 2.1 Platform Comparison Matrix

| Factor | Discord | Slack | Circle | Skool | Forum (Discourse) |
|---|---|---|---|---|---|
| Best for | Gaming, creator, developer communities | B2B, professional, small teams | Course-based, premium communities | Course + community bundle | Open-source, large-scale |
| Audience fit | Under-35, tech-savvy, async + real-time | Business professionals, already on Slack | Paid memberships, learning cohorts | Info-product creators, coaches | Developer, open-source, enterprise |
| Real-time chat | Excellent | Excellent | Limited | Limited | No |
| Async discussion | Moderate (threads lack depth) | Poor (messages disappear in free tier) | Good (threaded posts) | Good (classroom model) | Excellent |
| Content persistence | Permanent (free) | 90-day limit (free), permanent (paid) | Permanent | Permanent | Permanent |
| Price (community side) | Free | Free tier limited; Pro $7.25/user/mo | From $49/mo | From $99/mo | Free self-hosted; $50/mo hosted |
| Events | Voice channels, Stage | Huddles (limited) | Events built-in | Limited | Plugin-based |
| Monetization | Paywalled roles | No native | Built-in paywalls | Built-in payments | Plugin-based |
| SEO value | None (walled garden) | None (walled garden) | Optional (public posts) | Limited | Excellent (public by default) |
| Moderation tools | Good (bots, AutoMod) | Basic | Moderate | Basic | Excellent |

#### 2.2 Platform Decision Framework

Answer these questions to narrow the choice:

1. **Where does your audience already spend time?** (If they live in Slack, do not force them to Discord.)
2. **Real-time or async?** (B2B professionals need async. Gaming/creator audiences expect real-time.)
3. **Free or paid community?** (Paid requires Circle, Skool, or gated Discord/Slack.)
4. **SEO value needed?** (Public forums win. Walled gardens contribute zero SEO.)
5. **Budget for tooling?** (Discord is free. Circle starts at $49/mo. Slack Pro is per-seat.)
6. **Technical audience?** (Developers often prefer Discourse or Discord. Non-technical audiences may prefer Circle or Skool.)

#### 2.3 Hybrid Architecture

Many successful communities use platform combinations:

| Primary | Secondary | Use Case |
|---|---|---|
| Discord | Forum (Discourse) | Real-time chat + persistent knowledge base |
| Circle | Slack | Async content + quick team communication |
| Discourse | Discord | SEO-indexed knowledge + real-time events |

### Deliverables
- Platform recommendation with justification
- Platform comparison scorecard specific to this audience
- Migration plan if switching from an existing platform
- Tooling and integration requirements (bots, automation, analytics)

### Exit Conditions
- Platform selected with documented rationale
- Budget approved for platform costs
- Technical setup requirements identified

---

## Phase 3: Founding Members

### Purpose
Recruit the first 10-50 members who will set the culture, seed content, and create the energy that makes the community feel alive on launch day. This is the most important phase -- skip it and the community dies.

### Entry Conditions
- Phase 2 complete: platform selected and configured
- Platform basic setup complete (channels/spaces created, welcome message written)

### Key Activities

#### 3.1 Founding Member Recruitment

Target: 10-50 founding members before public launch. Quality over quantity.

| Source | Approach | Expected Conversion |
|---|---|---|
| Existing power users | Personal email invitation from founder/CEO | 30-50% acceptance |
| Beta/early access customers | "Join our private community" positioning | 20-30% |
| Newsletter subscribers (engaged) | Exclusive invitation to most engaged segment | 10-15% |
| Social media followers (active commenters) | DM invitation to people who regularly engage | 15-25% |
| Industry contacts / network | Personal outreach to respected practitioners | 20-40% |

Founding member outreach template elements:
- Personal (not mass email -- use their name and reference specific interactions)
- Exclusive ("You are one of 30 people we are inviting")
- Clear ask ("We need you to post once this week and respond to 2-3 threads")
- Benefit ("Shape the community direction, direct access to our team")

#### 3.2 Seed Initial Content

Before ANY public member joins, the community must have:

| Content Type | Minimum Quantity | Purpose |
|---|---|---|
| Welcome/introduction thread | 1 | Model the format for member intros |
| Discussion posts (questions + opinions) | 10-15 | Create activity that new members can join |
| Resource/value post | 3-5 | Demonstrate the community delivers value |
| Founding member introductions | 5-10 | Social proof that real people are here |
| Pinned guidelines/rules | 1 | Set expectations from day one |
| First event or AMA announcement | 1 | Give members something to anticipate |

#### 3.3 Establish Culture

Culture is set by the first 20 interactions, not by a rules document. Design it:

- **Tone**: Define the communication style (professional, casual, emoji-heavy, structured)
- **Norms**: Model behavior by posting as the founding team (ask questions, share insights, celebrate members)
- **Rituals**: Establish 2-3 recurring engagement patterns (weekly thread, monthly spotlight, "show your work" Fridays)
- **Response time**: The founding team must respond to every post within 2-4 hours during the first 30 days

### Deliverables
- Founding member recruitment plan with target list and outreach templates
- Seed content calendar (15-20 pieces pre-written)
- Culture brief: tone, norms, modeled behaviors
- Founding member welcome kit (onboarding message, expectations, perks)

### Exit Conditions
- Minimum 10 founding members active in the platform
- Minimum 15 content pieces posted (mix of team + founding member)
- Culture norms demonstrated through real interactions (not just documented)
- This phase MUST be complete before Phase 4 begins

---

## Phase 4: Launch Execution

### Purpose
Execute a coordinated launch that drives initial member signups while maintaining the community energy established by founding members.

### Entry Conditions
- Phase 3 complete: founding members active, content seeded, culture established (GATE ENFORCED)
- Launch assets prepared (landing page, email, social posts)

### Key Activities

#### 4.1 Pre-Launch Content (7-14 days before)

| Day | Channel | Content |
|---|---|---|
| Day -14 | Email list | Teaser: "Something new is coming for [audience]" |
| Day -10 | Social media | Behind-the-scenes content from founding members |
| Day -7 | Email list | Announcement with waitlist/early access signup |
| Day -5 | Social media | Founding member testimonials about early experience |
| Day -3 | Email + social | "Doors open in 3 days" with clear value proposition |
| Day -1 | Email + social | "Tomorrow" reminder with specific launch time |

#### 4.2 Launch Day Execution

| Time | Action | Owner |
|---|---|---|
| Launch hour | Send launch email to full list | Marketing |
| Launch hour | Publish social media posts (all platforms simultaneously) | Social |
| Launch + 1h | Post welcome thread in community | Community lead |
| Launch + 2h | Founding members post welcome messages (pre-coordinated) | Founding members |
| Launch + 4h | First value-add content post (resource, tip, or insight) | Community lead |
| Launch + 8h | Evening engagement prompt (timezone coverage) | Community lead |

#### 4.3 First 48-Hour Activation Plan

The first 48 hours determine whether a new member stays or ghosts. Every new member must:

1. **Complete onboarding** (introduce themselves, set up profile) -- within first 30 minutes
2. **Experience value** (find a useful thread, get a response) -- within first 2 hours
3. **Take an action** (reply to a thread, react to a post, join an event RSVP) -- within first 24 hours
4. **Return on day 2** (triggered by notification of a reply to their intro or a @mention) -- within 48 hours

Target: 60%+ of day-1 joiners should be active on day 2.

#### 4.4 Launch Metrics Dashboard

Track hourly for the first 48 hours, then daily for the first 2 weeks:

| Metric | First 24h Target | First 7d Target |
|---|---|---|
| New member signups | 50-200 (depends on list size) | 100-500 |
| Introduction posts | 30%+ of new members | 40%+ cumulative |
| Threads with replies | 80%+ of threads get a reply | 90%+ |
| Average time to first reply | Under 2 hours | Under 1 hour |
| Return rate (day 2) | 50%+ | N/A |
| Return rate (day 7) | N/A | 35%+ |

### Deliverables
- Launch timeline with hour-by-hour execution plan
- Pre-launch content calendar (email + social)
- New member onboarding flow specification
- Launch metrics dashboard setup
- First 48-hour activation playbook

### Exit Conditions
- Launch executed per timeline
- Day-7 return rate measured and documented
- Post-launch retro completed: what worked, what to adjust

---

## Phase 5: Engagement Design

### Purpose
Build sustainable engagement programs that keep members active without requiring constant team effort. The goal is member-to-member engagement, not team-to-member broadcasting.

### Entry Conditions
- Phase 4 complete: community launched with initial members
- At least 2 weeks of post-launch activity data available

### Key Activities

#### 5.1 Engagement Programs

| Program Type | Cadence | Description | Effort |
|---|---|---|---|
| Weekly discussion thread | Weekly | Themed prompt ("What are you working on?" / "Wins this week") | Low |
| Expert AMA | Monthly | Invite internal or external expert for live Q&A | Medium |
| Member spotlight | Bi-weekly | Feature one member's story, project, or achievement | Low |
| Challenge/build week | Monthly or quarterly | Members work on a shared challenge with accountability | High |
| Resource drops | Weekly | Curated resources, templates, tools shared by team or members | Low |
| Feedback rounds | Monthly | Members give feedback on product, features, or community itself | Medium |

#### 5.2 Content Cadence

Establish a repeatable weekly rhythm:

| Day | Content Type | Owner |
|---|---|---|
| Monday | Weekly kickoff thread + week's agenda | Community lead |
| Tuesday | Resource or tutorial share | Team or member volunteer |
| Wednesday | Discussion prompt or hot take | Community lead |
| Thursday | Member spotlight or case study | Community lead |
| Friday | "Show your work" or wins celebration | Members (prompted) |

#### 5.3 Recognition Systems

Recognition drives repeat participation. Build tiered recognition:

| Level | Criteria | Recognition |
|---|---|---|
| Active member | 5+ posts/month, 30-day streak | Badge/role, shoutout in weekly digest |
| Contributor | Helps others consistently, creates resources | Special role, featured in spotlight |
| Champion | Top 1% engagement, recruits new members | Champion badge, direct access to team, early feature access |
| Moderator | Trusted member who enforces norms | Mod role, community leadership title, possible compensation |

#### 5.4 Engagement Decay Prevention

Watch for these signals and intervene:

| Signal | Timeline | Intervention |
|---|---|---|
| Weekly active members dropping | 2+ weeks decline | Re-engage with high-value content or event |
| Founding members going quiet | 30 days inactive | Personal outreach, ask for feedback |
| Reply rate declining | 2+ weeks decline | Seed more discussion-worthy prompts, tag active members |
| New member intros declining | Week over week drop | Improve onboarding flow, launch recruitment push |

### Deliverables
- Engagement program portfolio (programs, cadence, owners)
- Weekly content calendar template
- Recognition system design with tiers and criteria
- Engagement health monitoring checklist

### Exit Conditions
- At least 3 recurring engagement programs launched
- Content cadence running for 2+ weeks
- Recognition system active
- Engagement metrics tracking in place

---

## Phase 6: Moderation Framework

### Purpose
Establish rules, enforcement tiers, and moderator processes that keep the community safe and welcoming as it scales. Moderation at 50 members is different from moderation at 5,000.

### Entry Conditions
- Community is active with regular member posting
- At least 1 incident or edge case has occurred that needs a policy response

### Key Activities

#### 6.1 Community Rules

Write rules that are specific, enforceable, and short. Target: 5-8 rules maximum.

Standard rule categories:
1. **Respect**: No personal attacks, harassment, or discrimination
2. **Relevance**: Stay on topic for the community's purpose
3. **Self-promotion**: Limits on promotional content (e.g., max 1 self-promo post/week in designated channel)
4. **Privacy**: No sharing others' private information
5. **No spam**: No repetitive posts, unsolicited DMs, or automated content
6. **Constructive conflict**: Disagree with ideas, not people
7. **Safety**: No illegal content, threats, or doxxing

#### 6.2 Enforcement Tiers

| Tier | Violation | Action | Who Decides |
|---|---|---|---|
| 1 - Gentle redirect | Off-topic post, accidental rule break | DM with friendly reminder | Any moderator |
| 2 - Warning | Repeated minor violations, mild self-promo abuse | Public or DM warning with rule citation | Any moderator |
| 3 - Temporary mute | Heated argument, continued violations after warning | 24-72 hour mute + DM explanation | Senior moderator |
| 4 - Temporary ban | Serious violation (harassment, sustained toxicity) | 7-30 day ban + documented reason | Community lead |
| 5 - Permanent ban | Severe violation (threats, doxxing, hate speech) | Permanent removal + account report | Community lead + escalation |

#### 6.3 Moderator Recruitment

| Moderator Ratio | Community Size | Notes |
|---|---|---|
| 1 moderator per 50-100 members | Under 500 | Founding team can cover this |
| 1 moderator per 100-200 members | 500-2,000 | Recruit from champion members |
| 1 moderator per 200-500 members | 2,000+ | Formalize moderator program with guidelines |

Moderator selection criteria:
- Active member for 60+ days
- Consistently helpful and constructive
- Demonstrated good judgment in conflicts
- Available for 3-5 hours/week minimum

#### 6.4 Escalation Protocol

| Situation | Escalate To | SLA |
|---|---|---|
| Member-to-member conflict | Moderator DM mediation | 4 hours |
| Harassment report | Senior moderator / community lead | 2 hours |
| Legal threat or doxxing | Community lead + legal | Immediate |
| Brand/PR risk (public complaint going viral) | Community lead + marketing lead | 1 hour |
| Moderator misconduct | Community lead | 24 hours |

### Deliverables
- Community rules document (public-facing)
- Moderator handbook (enforcement tiers, escalation, tools)
- Moderator recruitment criteria and onboarding plan
- Incident response playbook

### Exit Conditions
- Rules published and visible to all members
- At least 1 moderator recruited (beyond founding team) for communities over 100 members
- Enforcement tiers documented and moderators trained

---

## Phase 7: Growth (Community-Led Growth)

### Purpose
Scale the community through member-driven growth tactics that leverage existing members as acquisition channels. Paid advertising to a community rarely works -- members recruit members.

### Entry Conditions
- Community has 100+ active members
- Engagement metrics are stable or growing
- Founding member phase complete (culture is established)

### Key Activities

#### 7.1 Member Referral Mechanisms

| Mechanism | Description | Expected Impact |
|---|---|---|
| Invite-only exclusivity | Members can invite 2-3 friends, creating scarcity | 15-30% of new members via referral |
| Referral rewards | Refer X members -> unlock badge, role, or perk | 10-20% growth acceleration |
| "Bring a friend" events | Specific events where members can bring a guest | Event attendance +30-50% |
| Collaborative content | Members co-create content that gets shared externally | 5-15% organic traffic increase |

#### 7.2 Content Amplification

Community-generated content is the highest-leverage growth channel:

| Content Type | Amplification Channel | Owner |
|---|---|---|
| Best community discussions | Social media reposts (with permission) | Community team |
| Member success stories | Blog posts, case studies, social proof | Marketing team |
| Community event recordings | YouTube, podcast feed, blog | Community team |
| Member-written guides | SEO-optimized blog posts | Content team |
| Community data/insights | PR, thought leadership, social | Marketing team |

#### 7.3 Community-Led Growth (CLG) Metrics

| Metric | Definition | Benchmark |
|---|---|---|
| Community-attributed signups | Users who join product after community exposure | 10-20% of total signups |
| Member referral rate | % of members who have invited at least 1 person | 5-15% |
| Content amplification reach | External impressions from community-sourced content | 2-5x community size |
| Community-to-paid conversion | Free community members who become paying customers | 5-15% |
| Viral coefficient | Average invites per member that convert | > 0.3 (healthy), > 0.7 (strong) |

#### 7.4 Partnership and Cross-Pollination

| Tactic | Description | Effort |
|---|---|---|
| Community swaps | Partner with complementary community for joint events | Medium |
| Guest expert exchanges | Their expert does AMA in your community, and vice versa | Low |
| Co-created content | Joint guides, research, or events with partner brand | High |
| Platform cross-posting | Share best content to Reddit, LinkedIn groups, Hacker News | Low |

### Deliverables
- Community-led growth strategy with prioritized tactics
- Member referral program design
- Content amplification playbook
- CLG metrics dashboard specification
- Partnership outreach list and proposal templates

### Exit Conditions
- At least 2 growth tactics active
- Community-attributed signups being tracked
- Member referral mechanism live
- Growth metrics reporting established

---

## Phase 8: Metrics & Health

### Purpose
Measure community health, engagement quality, and business impact with a systematic framework. Vanity metrics (total members) are easy to track but worthless for decision-making.

### Entry Conditions
- Community has been active for 30+ days
- Basic analytics in place (platform native or third-party)

### Key Activities

#### 8.1 Community Health Score

Composite score from weighted engagement signals:

| Signal | Weight | Healthy | Moderate | Unhealthy |
|---|---|---|---|---|
| WAM / Total members | 25% | 25%+ | 15-24% | Under 15% |
| Posts per active member/week | 20% | 2+ | 1-2 | Under 1 |
| Member-to-member reply ratio | 20% | 60%+ threads | 30-59% | Under 30% |
| New member 7-day retention | 15% | 40%+ | 25-39% | Under 25% |
| Time to first response | 10% | Under 1 hour | 1-4 hours | Over 4 hours |
| Moderator intervention rate | 10% | Under 2% of posts | 2-5% | Over 5% |

Overall score: 0-100. Healthy (70-100), Moderate (40-69), Unhealthy (0-39).

#### 8.2 Engagement Metrics

| Metric | Definition | Frequency |
|---|---|---|
| DAU / MAU ratio | Daily active / monthly active members | Weekly |
| Posts per week | Total posts (excluding bot/automated) | Weekly |
| Replies per post | Average replies on discussion threads | Weekly |
| Lurker ratio | Members with 0 posts in 30 days / total members | Monthly |
| Content creation ratio | Members who posted / total members | Monthly |
| Event attendance rate | Attendees / total members | Per event |

Benchmark: Healthy communities have a DAU/MAU ratio of 15-25%. Above 30% is exceptional. Below 10% indicates engagement problems.

#### 8.3 Business Impact Metrics

| Metric | How to Measure | Target |
|---|---|---|
| Support deflection | Tickets answered in community vs support queue | 20-40% deflection |
| Retention lift | Retention rate of community members vs non-members | 10-25% higher retention |
| NPS difference | NPS of community members vs non-members | 15-30 points higher |
| Referral attribution | New signups attributed to community members | 10-20% of signups |
| Revenue influence | Revenue from community members vs non-members | 1.5-3x higher LTV |

#### 8.4 Reporting Cadence

| Report | Frequency | Audience | Key Contents |
|---|---|---|---|
| Community pulse | Weekly | Community team | WAM, posts, new members, flags |
| Community health report | Monthly | Marketing leadership | Health score, engagement trends, business impact |
| Community ROI review | Quarterly | Executive team | Business metrics, cost per member, revenue attribution |
| Annual community strategy | Yearly | Leadership + community | Full review, strategy refresh, budget planning |

### Deliverables
- Community health score model with weights and thresholds
- Metrics dashboard specification
- Monthly report template
- Quarterly ROI review template
- Annual strategy review framework

### Exit Conditions
- Health score model implemented
- Reporting cadence active
- Business impact metrics being tracked (even if early data is limited)

---

## Diagnostic Questions

Ask these before producing any community recommendation. Building a community strategy without this context leads to generic advice.

1. **Goal clarity**: What is the primary business goal for this community? (Retention, acquisition, support deflection, upsell, moat?)
2. **Audience definition**: Who exactly are the target members? (Role, seniority, industry, company size?)
3. **Existing communities**: Where does this audience currently gather online? Are there competing communities?
4. **Current state**: Do you have an existing community? If yes, what platform, how many members, what is the engagement level?
5. **Resources**: Who will manage the community day-to-day? What is the time commitment budget? (Community management is 10-20 hours/week minimum.)
6. **Budget**: What is the budget for platform, tools, events, and content creation?
7. **Content engine**: Do you have existing content (blog, newsletter, courses) that can seed the community?
8. **Timeline expectations**: When do you need the community to show results? (Realistic: 6-12 months to meaningful business impact.)
9. **Platform preferences**: Does your team or audience have strong platform preferences or constraints?
10. **Monetization intent**: Will this be a free, paid, or freemium community?

If the user cannot answer questions 1-2, recommend completing community strategy (Phase 1) before making any platform or execution decisions.

---

## Escalation Routes

| Signal Detected | Escalate To | Reason |
|---|---|---|
| Social media content for community promotion | paw-mkt-social | Social amplification is a distinct skill |
| Influencer partnerships for community seeding | paw-mkt-influencer | Influencer outreach requires specialized approach |
| Email sequences for community onboarding | paw-mkt-email | Email automation needs email specialist |
| Content creation for community resources | paw-mkt-content | Long-form content creation at scale |
| Paid advertising for community growth | paw-mkt-paid-ads | Paid community growth requires ad expertise |
| PR for community launch announcements | paw-mkt-pr | Media relations for launch coverage |
| Community pricing / paid membership tiers | paw-mkt-pricing | Pricing strategy for paid communities |
| Retention mechanics within community | paw-mkt-retention | Churn prevention at the product level |
| No brand or product context established | paw-mkt-product-context | Foundation must exist before community |

---

## Ethics: Community Management Responsibilities

Communities create real human connections and power dynamics. The ethical obligations are significant.

### Ethical Community Practices

- **Privacy by default**: Do not share member data, DM content, or participation patterns externally without consent.
- **Transparent moderation**: Rules are public. Enforcement actions are consistent. Members can appeal.
- **No manufactured engagement**: Fake accounts, bot-generated discussions, and paid shills destroy trust when discovered.
- **Inclusive access**: Ensure community is accessible to members with disabilities (alt text, screen reader compatibility, captioned events).
- **Data ownership**: Members own their content. If the community closes, provide export or notice period.
- **No dark patterns for growth**: Do not auto-enroll users, send unsolicited invites from member contact lists, or create misleading "you were mentioned" notifications.

### Dark Patterns to Refuse

| Pattern | Description | Why It Harms |
|---|---|---|
| Auto-enrollment | Adding customers to community without consent | Violates trust, inflates vanity metrics |
| Contact list harvesting | Using member connections to spam invites | Destroys member trust, potential legal liability |
| Fake engagement | Bot accounts or paid engagement to simulate activity | Discovered quickly, destroys credibility permanently |
| Notification spam | Excessive notifications to drive return visits | Causes notification fatigue, drives members to leave |
| Bait-and-switch | Free community that requires payment for basic features | Trust destruction, negative word-of-mouth |

Before implementing any community growth tactic, ask: **Would members feel proud to be part of this community if they knew how it operated?** If not, redesign the approach.

---

## Path Resolution

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/community/`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/community/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All community work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Community Strategy | `community-strategy-{YYYY-MM-DD}.md` | Type, business goal, audience, positioning, success metrics |
| Platform Selection | `platform-selection-{YYYY-MM-DD}.md` | Comparison scorecard, recommendation, rationale, migration plan |
| Launch Plan | `community-launch-plan-{YYYY-MM-DD}.md` | Founding member plan, seed content calendar, launch timeline, 48-hour playbook |
| Engagement Design | `engagement-design-{YYYY-MM-DD}.md` | Programs, content cadence, recognition system, decay prevention |
| Moderation Guide | `moderation-guide-{YYYY-MM-DD}.md` | Rules, enforcement tiers, escalation protocol, moderator handbook |
| Growth Strategy | `community-growth-{YYYY-MM-DD}.md` | CLG tactics, referral program, content amplification, partnerships |
| Health Dashboard | `community-health-{YYYY-MM-DD}.md` | Health score model, metrics, reporting cadence, templates |
| Community Roadmap | `community-roadmap-{YYYY-MM-DD}.md` | Phased plan across all 8 phases, timeline, milestones, owners |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/community/
  community-strategy-{YYYY-MM-DD}.md
  platform-selection-{YYYY-MM-DD}.md
  community-launch-plan-{YYYY-MM-DD}.md
  engagement-design-{YYYY-MM-DD}.md
  moderation-guide-{YYYY-MM-DD}.md
  community-growth-{YYYY-MM-DD}.md
  community-health-{YYYY-MM-DD}.md
  community-roadmap-{YYYY-MM-DD}.md

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/community/
  (same structure as above)
```

---

## Response Protocol

When the user requests community work:

1. **Load context**: Read brand context and SOSTAC plan when available. Check for existing community deliverables.
2. **Ask diagnostic questions** if the user has not already provided this information.
3. **Determine current phase**: Is this a new community (start Phase 1) or existing (identify current phase)?
4. **Route to capability**: Based on the current phase, load the appropriate reference file:
   - Strategy -> `./references/community-strategy.md`
   - Platform selection -> `./references/platform-selection.md`
   - Launch -> `./references/community-launch.md`
   - Engagement -> `./references/engagement-design.md`
   - Moderation -> `./references/moderation.md`
   - Growth -> `./references/community-led-growth.md`
   - Metrics -> `./references/metrics-measurement.md`
5. **Enforce phase gates**: Phase 3 must complete before Phase 4 launch. Do not skip founding members.
6. **Deliver structured output**: Strategy and specifications following the deliverables format.
7. **Save deliverables** to the resolved path.
8. **Recommend next steps**: What phase to execute next, what to prepare, when to measure.
