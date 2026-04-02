# Email Automation Pipeline Workflow

This reference defines the standard workflow, diagnostic questions, benchmark data, deliverables, and ethical guidelines for all email marketing work.

---

## Diagnostic Questions

Ask these before producing any email recommendation. Recommendations without this data are guesses.

1. **Goal**: What is the business objective of this email program? (Lead nurture, onboarding activation, revenue, retention, re-engagement, newsletter growth?)
2. **Audience**: Who is the recipient? What customer journey stage are they in? What do they already know about the product?
3. **Current state**: What emails are currently being sent? What ESP is in use? What is the current list size and segmentation?
4. **Performance baseline**: What are current open rates, click rates, unsubscribe rates, and conversion rates? How are these measured?
5. **Trigger events**: What user actions or time-based events should initiate email sequences? What data is available for personalization?
6. **Technical constraints**: What ESP or marketing automation platform is in use? What integrations exist (CRM, product analytics, billing)?
7. **Compliance**: What jurisdictions do subscribers reside in? (CAN-SPAM, GDPR, CASL, CCPA applicability?) Is there an existing unsubscribe and preference center?

If the user cannot answer questions 3-4, recommend an email audit and baseline measurement period before building new sequences. Automation without measurement is activity without learning.

---

## Phase 1: Goal & Journey Mapping

### Purpose
Define the specific business objective the email program serves, map the customer journey stage it targets, and identify the trigger events that initiate email communication.

### Entry Conditions
- Brand context and SOSTAC plan available (or brand intake completed)
- Business objective identified (even if broad)
- Target audience defined at minimum persona level

### Key Activities
1. **Define the email objective** with a measurable outcome:
   - Lead nurture: Move MQL to SQL (target: X% conversion within Y days)
   - Onboarding: Drive activation metric (target: X% reach activation within Y days)
   - Revenue: Generate $X from sequence (target: $X revenue per subscriber)
   - Retention: Reduce churn by X% (target: X% improvement in retention rate)
   - Re-engagement: Recover X% of inactive subscribers (target: X% re-activation)

2. **Map the customer journey stage** this email program addresses:

   | Journey Stage | Email Role | Typical Sequences |
   |---|---|---|
   | Awareness | Educate and build trust | Welcome, newsletter |
   | Consideration | Differentiate and prove value | Nurture, case study drip |
   | Decision | Reduce risk and drive action | Trial, demo follow-up, pricing |
   | Onboarding | Activate and retain | Welcome, setup, quick-win |
   | Retention | Deepen engagement | Usage tips, feature announcements |
   | Expansion | Upsell and cross-sell | Upgrade, add-on, annual plan |
   | Win-back | Re-engage lapsed users | Re-engagement, sunset |

3. **Identify trigger events** that initiate the sequence:
   - User actions: signup, trial start, feature use, purchase, inactivity
   - Time-based: X days after signup, X days before trial expiry, anniversary
   - Behavioral: visited pricing page, downloaded resource, opened but did not click
   - External: seasonal, product launch, industry event

### Deliverables
- Email program brief: objective, journey stage, trigger events, success metrics
- Journey map showing where email fits relative to other touchpoints

### Exit Conditions
- Clear, measurable objective documented
- Journey stage and trigger events defined
- Success metrics agreed with stakeholder

---

## Phase 2: Sequence Architecture

### Purpose
Design the email flow structure including number of emails, timing, conditional branches, and the logic that moves subscribers through the sequence.

### Entry Conditions
- Phase 1 complete: objective, journey stage, and triggers defined
- ESP capabilities known (branching, conditional content, wait steps)

### Key Activities
1. **Design the sequence flow** — map every email, delay, and branch:
   - Number of emails in the sequence
   - Delay between each email (hours or days)
   - Conditional branches based on subscriber behavior (opened, clicked, converted, did not engage)
   - Exit conditions (converted, unsubscribed, moved to another sequence)

2. **Apply sequence timing benchmarks**:

   | Sequence Type | Emails | Duration | Typical Cadence |
   |---|---|---|---|
   | Welcome | 3-5 | 7-14 days | Day 0, 1, 3, 7, 14 |
   | Onboarding | 5-8 | 14-30 days | Day 0, 1, 3, 5, 7, 10, 14, 21 |
   | Nurture | 5-7 | 21-45 days | Every 3-5 days |
   | Win-back | 3-4 | 14-21 days | Day 0, 5, 10, 14 |
   | Abandoned cart | 3 | 3-5 days | 1 hour, 24 hours, 72 hours |
   | Post-purchase | 3-5 | 30-60 days | Day 1, 3, 7, 14, 30 |
   | Re-engagement | 3-4 | 14-30 days | Day 0, 7, 14, 21 |

3. **Define branch logic**:
   - If opened but did not click -> send follow-up with different CTA
   - If clicked but did not convert -> send social proof email
   - If no opens after 2 emails -> move to re-engagement or sunset
   - If converted -> exit sequence, enter post-conversion flow

4. **Map sequence interconnections** — how sequences hand off to each other:
   - Welcome -> Onboarding (on trial start)
   - Onboarding -> Nurture (on activation) or Win-back (on inactivity)
   - Win-back -> Sunset (on no re-engagement)

### Deliverables
- Sequence flow diagram (text-based or visual)
- Email-by-email outline: number, delay, purpose, branch logic
- Entry/exit conditions for each sequence

### Exit Conditions
- Complete sequence architecture documented
- Branch logic defined for all decision points
- Timing validated against benchmarks

---

## Phase 3: Copy & Creative

### Purpose
Write the subject lines, preview text, body copy, and CTAs for each email in the sequence. Every word earns its place.

### Entry Conditions
- Phase 2 complete: sequence architecture finalized
- Brand voice and tone guidelines available
- Key messages, proof points, and objection-handling content available

### Key Activities
1. **Write subject lines** (the single highest-leverage element):
   - Keep under 50 characters for mobile visibility (35-45 ideal)
   - Front-load the value or curiosity element
   - Write 3-5 variants per email for A/B testing
   - Avoid spam trigger words: "free," "guarantee," "act now," all caps, excessive punctuation
   - Personalization tokens in subject lines lift open rates 10-22% on average

2. **Write preview text** (the second subject line):
   - 40-90 characters visible in most clients
   - Complement the subject line -- do not repeat it
   - If left blank, email clients pull the first line of body copy (often ugly)

3. **Write body copy** per email:
   - One email = one goal = one CTA
   - Open with the reader's situation, not the brand's news
   - Use short paragraphs (1-3 sentences), bullet points, and whitespace
   - Write at a 6th-8th grade reading level for broad audiences
   - Include a P.S. line -- it is the second most-read element after the subject line

4. **Design CTAs**:
   - One primary CTA per email (button or prominent link)
   - CTA copy describes the outcome: "Start My Free Trial" not "Click Here"
   - Place CTA after the value proposition is established, not before
   - For long emails: repeat the CTA at top and bottom

5. **Apply the email copy formula per sequence type**:

   | Sequence Type | Email 1 | Email 2 | Email 3 | Email 4+ |
   |---|---|---|---|---|
   | Welcome | Deliver + set expectations | Brand story / origin | Quick win / tutorial | Social proof |
   | Onboarding | Key action prompt | Second activation step | Social proof + tip | Feature discovery |
   | Nurture | Pain point + empathy | Insight / education | Case study / proof | Soft offer |
   | Win-back | "We miss you" + value | Incentive / offer | Final chance + urgency | Sunset warning |

### Deliverables
- Complete copy for each email: subject line (3-5 variants), preview text, body, CTA
- Copy brief noting tone, personalization tokens, and dynamic content blocks

### Exit Conditions
- All emails in the sequence have complete copy
- Subject line variants ready for A/B testing
- Copy reviewed against brand voice guidelines
- **Human review gate**: No AI-generated email copy goes to production without human review and approval

---

## Phase 4: Technical Setup

### Purpose
Configure automation triggers, segmentation rules, merge tags, and send conditions in the ESP. This is where strategy becomes executable.

### Entry Conditions
- Phase 3 complete: copy and creative approved
- ESP access available
- Data sources for triggers and personalization identified

### Key Activities
1. **Configure automation triggers**:
   - Event-based: API event from product (signup, purchase, feature use)
   - Form-based: form submission on landing page or in-app
   - Segment-based: enters or exits a segment (e.g., "inactive 30 days")
   - Date-based: X days after a specific date field (trial start, purchase date)

2. **Build segmentation rules**:
   - Behavioral: actions taken in product or on website
   - Demographic: role, company size, industry
   - Engagement: email engagement level (active, at-risk, inactive)
   - Lifecycle: trial, active, churned, expansion candidate

3. **Set merge tags and dynamic content**:
   - First name, company name, plan type
   - Usage-based variables (features used, login count, progress)
   - Conditional content blocks (show different content by segment)
   - Fallback values for empty fields ("there" as fallback for empty first name)

4. **Define send conditions and suppression rules**:
   - Send window: respect timezone (send at 10am recipient local time)
   - Frequency cap: maximum emails per subscriber per week (2-3 for most B2B; 3-5 for B2C)
   - Suppression: do not send to unsubscribed, bounced, or recently contacted (24-48 hour cooldown)
   - Conflict resolution: if subscriber qualifies for multiple sequences, which takes priority?

5. **Recommended ESP capabilities by use case**:

   | Use Case | Recommended Tools |
   |---|---|
   | SaaS lifecycle | Customer.io, Intercom, Braze |
   | Ecommerce | Klaviyo, Omnisend, Drip |
   | Newsletter | ConvertKit, Beehiiv, Substack |
   | SMB / general | Mailchimp, ActiveCampaign, MailerLite |
   | Enterprise | HubSpot, Marketo, Salesforce Marketing Cloud |
   | Cold outreach | Instantly, Smartlead, Apollo |

### Deliverables
- Automation configuration document: triggers, segments, merge tags, send conditions
- Suppression and frequency cap rules

### Exit Conditions
- All automation triggers configured and tested
- Segmentation rules verified against subscriber data
- Merge tags tested with sample data (including edge cases with empty fields)

---

## Phase 5: Deliverability Check

### Purpose
Ensure emails reach the inbox. Deliverability is the foundation — the best copy in the world is worthless in the spam folder.

### Entry Conditions
- Phase 4 complete: technical setup configured
- Sending domain and ESP confirmed

### Key Activities
1. **Authentication setup** (non-negotiable prerequisites):
   - **SPF**: Sender Policy Framework record in DNS authorizing the ESP to send on behalf of your domain
   - **DKIM**: DomainKeys Identified Mail signing with 2048-bit key minimum
   - **DMARC**: Start with `p=none` for monitoring, progress to `p=quarantine`, then `p=reject` over 30-90 days
   - **Custom return-path / bounce domain**: Aligns envelope sender with header sender
   - **BIMI**: Brand Indicators for Message Identification (optional, adds logo in inbox)

2. **List hygiene**:
   - Remove hard bounces immediately (automatic in most ESPs)
   - Soft bounce threshold: remove after 3-5 consecutive soft bounces
   - Sunset policy: move subscribers with no opens for 90-120 days to re-engagement sequence, then suppress if no response
   - Never purchase email lists -- purchased lists destroy sender reputation and violate most ESPs' terms of service
   - Double opt-in for non-transactional lists (required in GDPR jurisdictions, best practice everywhere)

3. **Sender reputation monitoring**:
   - Check domain reputation: Google Postmaster Tools (free, essential)
   - Check IP reputation: Sender Score (Return Path), Talos Intelligence
   - Monitor blacklists: MXToolbox blacklist check
   - Track complaint rate: target under 0.1% (Google threshold is 0.3% before penalties)
   - Track bounce rate: target under 2% per send

4. **Deliverability benchmarks**:

   | Metric | Good | Warning | Critical |
   |---|---|---|---|
   | Inbox placement rate | >95% | 85-95% | <85% |
   | Bounce rate (per send) | <2% | 2-5% | >5% |
   | Complaint rate | <0.1% | 0.1-0.3% | >0.3% |
   | Unsubscribe rate | <0.5% | 0.5-1% | >1% |

5. **Warm-up protocol for new domains or IPs**:
   - Week 1: 50-100 emails/day to most engaged subscribers
   - Week 2: 200-500/day
   - Week 3: 1,000-2,000/day
   - Week 4+: Gradually increase to full volume
   - Monitor reputation after each increase; pause if complaint rate exceeds 0.1%

### Deliverables
- Deliverability audit report: authentication status, list health, reputation scores
- Warm-up schedule (if new domain or IP)
- Ongoing monitoring checklist

### Exit Conditions
- SPF, DKIM, and DMARC all passing authentication checks
- List hygiene audit complete: bounces removed, sunset policy active
- Sender reputation clean: no blacklist listings, complaint rate under 0.1%

---

## Phase 6: QA & Launch

### Purpose
Test every email before it reaches a real subscriber. Catch rendering issues, broken links, personalization errors, and logic failures before launch.

### Entry Conditions
- Phase 5 complete: deliverability verified
- All emails built in ESP with copy, merge tags, and automation logic

### Key Activities
1. **Test sends** — send to internal test list covering:
   - Gmail (personal and Workspace), Outlook (desktop and web), Apple Mail (iOS and macOS), Yahoo
   - Dark mode rendering
   - Mobile (iOS Mail, Gmail app, Outlook app)
   - Multiple screen sizes

2. **Link verification**:
   - Click every link in every email
   - Verify UTM parameters are appended correctly
   - Verify tracking redirects resolve to final destination
   - Check unsubscribe link works and preference center loads
   - Test CTA buttons on mobile (minimum 44x44px tap target)

3. **Personalization testing**:
   - Test with populated merge tags
   - Test with empty merge tags (verify fallback values render correctly)
   - Test conditional content blocks with different segment criteria

4. **Automation logic testing**:
   - Walk through the entire sequence as a test subscriber
   - Verify delays fire correctly
   - Verify branch conditions route to correct emails
   - Verify exit conditions remove subscribers from the sequence
   - Verify suppression rules prevent duplicate or conflicting sends

5. **Pre-launch checklist**:

   | Check | Status |
   |---|---|
   | Subject lines finalized (A/B variants set) | |
   | Preview text populated (not pulling body copy) | |
   | From name and reply-to address correct | |
   | Unsubscribe link present and functional | |
   | Physical mailing address included (CAN-SPAM) | |
   | All links working and UTM-tagged | |
   | Merge tags tested with data and without | |
   | Rendered correctly in top 5 email clients | |
   | Dark mode tested | |
   | Mobile rendering verified | |
   | Automation triggers firing correctly | |
   | Suppression and frequency caps active | |
   | Human approval sign-off received | |

### Deliverables
- QA test report: rendering screenshots, link check results, logic test results
- Launch sign-off document

### Exit Conditions
- All checklist items passing
- Human sign-off received from stakeholder
- Sequence activated in ESP

---

## Phase 7: Performance & Iteration

### Purpose
Monitor email performance against benchmarks, identify optimization opportunities, and establish a continuous testing cadence.

### Entry Conditions
- Phase 6 complete: sequence launched and live
- Analytics tracking confirmed (opens, clicks, conversions, revenue)

### Key Activities
1. **Monitor core metrics** against benchmarks:

   | Metric | Welcome | Onboarding | Nurture | Newsletter | Win-back |
   |---|---|---|---|---|---|
   | Open rate | 50-60% | 40-50% | 25-35% | 20-30% | 15-25% |
   | Click rate | 8-15% | 5-10% | 3-5% | 2-4% | 2-4% |
   | Click-to-open rate | 15-25% | 12-20% | 10-15% | 8-12% | 10-15% |
   | Conversion rate | 5-10% | 3-8% | 1-3% | 0.5-2% | 2-5% |
   | Unsubscribe rate | <0.5% | <0.3% | <0.5% | <0.3% | <1% |

   Note: Open rate tracking is less reliable since Apple MPP (Mail Privacy Protection). Use click rate and conversion rate as primary performance indicators.

2. **Establish A/B testing cadence**:
   - Test one element at a time: subject line, send time, CTA, content length, sender name
   - Minimum sample: 1,000 recipients per variant for subject line tests
   - Run each test for minimum 1 full send cycle before declaring a winner
   - Document every test: hypothesis, variants, sample size, results, confidence level

3. **Testing priority order** (highest to lowest expected impact):
   1. Subject line (directly controls open rate)
   2. Send time and day (affects open and click rate)
   3. CTA copy and placement (affects click and conversion rate)
   4. Email length and format (affects engagement)
   5. Personalization depth (affects relevance)
   6. From name (affects open rate)
   7. Preview text (affects open rate on mobile)

4. **Performance review cadence**:
   - **Weekly**: Open rate, click rate, unsubscribe rate, deliverability metrics
   - **Monthly**: Conversion rate, revenue per email, list growth rate, segment performance
   - **Quarterly**: Full sequence performance review, sunset inactive segments, update benchmarks

5. **Iteration triggers** — act when these thresholds are breached:
   - Open rate drops >10% from baseline -> investigate subject lines, deliverability, send time
   - Click rate drops >15% from baseline -> review CTA copy, content relevance, design
   - Unsubscribe rate exceeds 1% -> review frequency, content, and targeting
   - Conversion rate drops >20% from baseline -> review landing page, offer, audience fit

### Deliverables
- Performance dashboard (weekly, monthly, quarterly reports)
- A/B test log with results and learnings
- Optimization roadmap with prioritized improvements

### Exit Conditions
- Performance monitoring active and reporting automated
- First A/B test designed and scheduled
- Iteration playbook documented for ongoing optimization

---

## Email Benchmarks by Type

Reference benchmarks for planning and performance evaluation. Actual benchmarks vary significantly by industry, audience, and list quality.

### B2B SaaS Benchmarks

| Email Type | Open Rate | Click Rate | Conversion Rate | Revenue/Email |
|---|---|---|---|---|
| Welcome (single) | 50-65% | 10-15% | 5-10% | -- |
| Welcome (sequence avg) | 40-55% | 8-12% | 3-8% | -- |
| Onboarding | 35-50% | 5-10% | 3-8% | -- |
| Nurture / Drip | 25-35% | 3-5% | 1-3% | -- |
| Newsletter | 20-30% | 2-4% | 0.5-2% | $0.10-0.50 |
| Product announcement | 30-40% | 4-7% | 2-5% | -- |
| Win-back | 15-25% | 2-4% | 2-5% | -- |
| Abandoned cart | 40-50% | 8-12% | 5-10% | $3-8 per email |
| Post-purchase | 35-45% | 5-8% | -- | $0.50-2.00 |
| Cold outreach | 30-50% | 3-8% | 1-3% | -- |

### B2C / Ecommerce Benchmarks

| Email Type | Open Rate | Click Rate | Conversion Rate | Revenue/Email |
|---|---|---|---|---|
| Welcome (single) | 45-60% | 8-12% | 3-8% | $0.50-2.00 |
| Welcome (sequence avg) | 35-50% | 6-10% | 2-6% | $0.30-1.50 |
| Abandoned cart | 40-50% | 8-15% | 5-12% | $5-15 per email |
| Post-purchase | 35-45% | 5-8% | 2-5% | $1-5 |
| Win-back | 12-20% | 2-4% | 1-3% | $0.50-3.00 |
| Newsletter | 18-25% | 2-4% | 0.5-2% | $0.05-0.30 |
| Promotional | 15-25% | 2-5% | 1-4% | $0.10-1.00 |
| Birthday / anniversary | 40-50% | 6-10% | 3-7% | $2-8 |

### Newsletter-Specific Benchmarks

| Metric | Excellent | Good | Needs Work |
|---|---|---|---|
| Open rate (engaged segment) | >40% | 25-40% | <25% |
| Click rate | >4% | 2-4% | <2% |
| List growth rate (monthly) | >5% | 2-5% | <2% |
| Unsubscribe rate (per send) | <0.1% | 0.1-0.3% | >0.3% |
| Forward / share rate | >0.5% | 0.1-0.5% | <0.1% |
| Paid subscriber conversion (if applicable) | >3% | 1-3% | <1% |

---

## Ethics: Email Marketing Compliance and Trust

Email marketing relies on permission and trust. Breaking either destroys long-term performance.

### Legal Compliance (Non-Negotiable)

| Regulation | Jurisdiction | Key Requirements |
|---|---|---|
| CAN-SPAM | United States | Physical address, unsubscribe link, honor opt-outs within 10 business days, accurate headers |
| GDPR | EU/EEA/UK | Explicit consent (pre-checked boxes do not count), right to erasure, data processing records, DPO for large-scale processing |
| CASL | Canada | Express consent with record, identification of sender, unsubscribe mechanism |
| CCPA/CPRA | California | Right to know, right to delete, right to opt out of sale of personal information |

### Ethical Email Practices

- **Permission-based only**: Never add someone to a marketing list without their explicit opt-in. Purchased lists are never acceptable.
- **Honest subject lines**: The subject line must accurately represent the email content. Deceptive subjects (fake RE:, misleading urgency) are CAN-SPAM violations and trust destroyers.
- **Easy unsubscribe**: One-click unsubscribe (required by Gmail and Yahoo as of 2024). No login-to-unsubscribe, no multi-step processes.
- **Frequency respect**: Honor subscriber preferences. If someone opts into weekly, do not send daily.
- **Data minimalism**: Collect only the data you need for personalization and segmentation. More data is more liability.
- **Transparent tracking**: Disclose tracking in privacy policy. Consider whether tracking respects subscriber expectations.

### Dark Patterns to Avoid

| Pattern | Description | Why It Harms |
|---|---|---|
| Pre-checked consent | Consent boxes checked by default | GDPR violation; erodes trust |
| Hidden unsubscribe | Making unsubscribe difficult to find | CAN-SPAM/GDPR violation; increases complaints |
| Confirm-shaming | "No thanks, I hate saving money" | Creates resentment, not loyalty |
| Bait-and-switch | Promise one thing in subject, deliver another | Destroys open rates long-term; FTC risk |
| Purchased lists | Buying email lists and importing | Destroys sender reputation; legal liability |
| Engagement farming | "Reply YES to stay subscribed" without context | Manipulative; damages relationship |

Before implementing any email tactic, ask: **If the subscriber fully understood what was happening, would they still feel respected?** If not, do not do it.

---

## Escalation Routes

| Signal | Route To | Reason |
|---|---|---|
| Landing page conversion rate low | paw-mkt-cro | CRO specialist for page optimization |
| Content quality or editorial calendar needs | paw-mkt-content | Content specialist for blog, case studies |
| Email driving paid traffic (ad retargeting lists) | paw-mkt-paid-ads | Paid media for audience sync |
| SEO implications of email-driven content | paw-mkt-seo | SEO for content optimization |
| Social proof or community content for emails | paw-mkt-social | Social media for UGC and social proof |
| Influencer mentions or co-marketing emails | paw-mkt-influencer | Influencer partnerships |
| Email analytics infrastructure needs | paw-mkt-analytics | Analytics for tracking and attribution |
| Churn patterns surfacing in email data | paw-mkt-retention | Retention specialist for churn prevention |
| PR-related announcements via email | paw-mkt-pr | PR for press release alignment |

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/email/content/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/email/content/`

**Legacy fallback** -- old directory structure detected:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/content/email/`
  -> Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All email work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Email Program Brief | `email-brief-{sequence-type}-{YYYY-MM-DD}.md` | Objective, journey stage, trigger events, success metrics, sequence architecture |
| Sequence Copy | `sequence-{type}-{YYYY-MM-DD}.md` | Email-by-email copy: subject lines (A/B variants), preview text, body, CTAs |
| Automation Config | `automation-config-{sequence-type}-{YYYY-MM-DD}.md` | Triggers, segments, merge tags, send conditions, suppression rules |
| Deliverability Audit | `deliverability-audit-{YYYY-MM-DD}.md` | Authentication status, list health, reputation scores, warm-up schedule |
| QA Report | `qa-report-{sequence-type}-{YYYY-MM-DD}.md` | Rendering tests, link checks, logic verification, launch sign-off |
| Performance Report | `performance-{sequence-type}-{YYYY-MM-DD}.md` | Metrics vs benchmarks, A/B test results, optimization roadmap |

---

## Response Protocol

When the user requests email marketing work:

1. **Route the starting context** (see `./references/shared-patterns.md` for Starting Context Router). Decide whether this is strategy, implementation, or audit work.
2. **Read the strongest available context** (Pre-Flight): brand and SOSTAC first when available; otherwise use existing ESP data or email history.
3. **Ask the diagnostic questions** if the user has not already provided this information. Do not produce recommendations without knowing the email objective and current performance.
4. **Identify the workflow phase**. Determine where in the pipeline the work begins:
   - New program: start at Phase 1
   - Existing program needing copy: start at Phase 3
   - Technical issues: start at Phase 5
   - Performance problems: start at Phase 7
5. **Execute the relevant phases** sequentially, producing deliverables at each phase.
6. **Apply benchmark tables** to set expectations and evaluate performance.
7. **Save deliverables** to the resolved path (see Path Resolution).
8. **Recommend next steps**: what to launch, what to test, when to review results.

### When to escalate

- Landing page or signup flow conversion issues -> route to paw-mkt-cro
- Content strategy for email-driven blog or resources -> route to paw-mkt-content
- Paid media integration for retargeting lists -> route to paw-mkt-paid-ads
- Analytics infrastructure for email attribution -> route to paw-mkt-analytics
- Churn signals surfacing in email engagement data -> route to paw-mkt-retention
