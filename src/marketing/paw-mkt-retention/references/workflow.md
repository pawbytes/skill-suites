# Retention Workflow: Churn Diagnostic Framework

This reference defines the standard workflow, diagnostic questions, phase gates, and measurement methodology for all retention and churn prevention work.

---

## Core Principle: Diagnose Before Prescribing

The most common retention mistake is jumping to intervention design (cancel flows, save offers, win-back emails) without understanding WHY customers are churning. A save offer cannot fix a product that fails to deliver value. A dunning sequence cannot fix voluntary churn.

**Phase 1 MUST be completed before Phase 3.** Skip diagnosis and you will build interventions that address the wrong problem, waste resources on low-recovery segments, and create dark-pattern cancel flows that delay churn without preventing it.

---

## Phase 1: Churn Diagnosis

### Purpose
Classify the churn problem, identify root causes, and assess data availability before designing any intervention.

### Entry Conditions
- User has requested retention or churn-related work
- Brand context loaded (or acknowledged as unavailable)
- SOSTAC plan consulted if available

### Key Activities

#### 1.1 Classify Churn Type
Every churn event falls into one of two categories. The intervention for each is fundamentally different.

| Churn Type | Definition | Typical Share of Total Churn | Recovery Rate |
|---|---|---|---|
| Involuntary | Payment failure, expired card, bank decline | 20-40% of SaaS churn | 30-70% recoverable |
| Voluntary | Customer actively cancels | 60-80% of SaaS churn | 5-15% recoverable via save offers |

If the user does not know their split, assume 30% involuntary / 70% voluntary as a starting point and flag this assumption.

#### 1.2 Identify Root Causes
For voluntary churn, classify the dominant cancel reason:

| Cancel Reason Category | Signal | Typical Frequency |
|---|---|---|
| Price/value mismatch | "Too expensive" or downgrade attempts | 25-35% |
| Product-market fit gap | "Missing feature X" or low usage | 20-30% |
| Competitor switch | "Found a better alternative" | 10-20% |
| No longer needed | Business closed, project ended, seasonal | 10-15% |
| Poor experience | Support issues, bugs, UX friction | 5-15% |
| Never activated | Signed up but never used the product | 5-10% |

For involuntary churn, classify the payment failure type:

| Failure Type | Cause | Recovery Approach |
|---|---|---|
| Hard decline | Insufficient funds, closed account | Dunning sequence with payment update prompts |
| Soft decline | Expired card, processing error | Card updater + retry schedule |
| Fraud flag | Bank flagged as suspicious | Customer notification to authorize |

#### 1.3 Assess Data Availability

| Data Source | What It Tells You | Priority |
|---|---|---|
| Exit survey data | Self-reported cancel reasons | Critical |
| Usage/engagement metrics | Product adoption depth | Critical |
| Payment failure logs | Involuntary churn volume and type | Critical |
| Cohort retention curves | When customers churn (month 1, 3, 6, 12) | High |
| Support ticket themes | Frustration signals before cancel | High |
| NPS or CSAT scores | Satisfaction trajectory | Medium |
| Feature adoption tracking | Which features correlate with retention | Medium |

If the user lacks exit survey data, recommend implementing one immediately -- it is the single highest-ROI data collection for retention work.

### Deliverables
- Churn diagnosis report: churn type split, root cause classification, data gaps identified
- Data collection plan for any missing critical data sources

### Exit Conditions
- Churn type (voluntary vs involuntary) classified with data or documented assumptions
- Top 3 cancel reasons identified or hypothesized
- Data gaps documented with collection plan

---

## Phase 2: Prioritization

### Purpose
Sequence interventions by expected recovery rate and business impact, starting with the highest-probability wins.

### Entry Conditions
- Phase 1 complete: churn type classified, root causes identified

### Key Activities

#### 2.1 Apply the Retention Priority Stack

Work through this stack top to bottom. Each level has a higher recovery rate than the one below it.

| Priority | Intervention | Expected Recovery Rate | Effort |
|---|---|---|---|
| P0 | Payment failure recovery (dunning) | 30-70% | Low-medium |
| P1 | Card expiration pre-dunning | 40-60% prevented | Low |
| P2 | Cancel flow with save offers (price-sensitive segment) | 10-20% | Medium |
| P3 | Cancel flow with pause/downgrade options | 8-15% | Medium |
| P4 | Proactive health score interventions | 5-15% reduction in at-risk churn | High |
| P5 | Win-back campaigns (30-90 day churned) | 2-8% | Low-medium |
| P6 | Win-back campaigns (90+ day churned) | 0.5-3% | Low |

#### 2.2 Segment by Recovery Economics

Not all churned revenue is worth recovering equally:

- **High-LTV customers**: Justify more aggressive recovery investment (personal outreach, custom offers)
- **Low-LTV / free-to-paid converts**: Automated recovery only -- manual intervention does not pay back
- **Trial-only churners**: These are activation failures, not retention problems -- escalate to CRO/onboarding

#### 2.3 Calculate Recovery Opportunity

```
Monthly recoverable revenue = (involuntary churn MRR x recovery rate) + (voluntary churn MRR x save rate)
```

Benchmark save rates:
- Dunning sequences: 30-50% of failed payments recovered (industry average)
- Cancel flow save offers: 10-15% of cancel attempts saved (best-in-class: 20-25%)
- Win-back campaigns: 3-5% reactivation rate within 90 days

### Deliverables
- Prioritized intervention roadmap with expected recovery rates
- Revenue recovery opportunity estimate (monthly and annual)
- Segment-level prioritization matrix

### Exit Conditions
- Intervention priority sequence agreed with user
- Top 2-3 interventions selected for Phase 3

---

## Phase 3: Intervention Design

### Purpose
Design specific retention mechanisms matched to the diagnosed churn causes and prioritized segments.

### Entry Conditions
- Phase 1 complete (diagnosis done -- this gate is enforced)
- Phase 2 complete (priorities set)
- Churn root causes are mapped to specific intervention types

### Key Activities

#### 3.1 Cancel Flow Design

Load `./references/cancel-flow-design.md` for detailed patterns. Key elements:

- **Exit survey**: 4-6 cancel reason options, presented BEFORE any save offer
- **Dynamic offer routing**: Match the save offer to the stated cancel reason
  - "Too expensive" -> discount or downgrade offer
  - "Missing feature" -> feature roadmap preview or workaround
  - "Not using it" -> pause option (30-90 days)
  - "Switching to competitor" -> competitive comparison + offer
  - "Business closed / no longer needed" -> graceful exit with data export
- **Confirmation page**: Include reactivation path and data retention notice

Cancel flow ethical requirements:
- Cancel must be completable in 3 clicks or fewer
- No phone-call-required cancellation
- Save offers are presented once -- no loops or dark patterns
- "Just cancel" option is always visible and clearly labeled

#### 3.2 Dunning Sequence Design

Load `./references/payment-recovery.md` for detailed patterns. Standard sequence:

| Day | Action | Channel |
|---|---|---|
| Day 0 | First retry attempt (automatic) | System |
| Day 1 | Payment failed notification | Email |
| Day 3 | Second retry + update payment method CTA | Email |
| Day 5 | Third retry | System |
| Day 7 | Urgent: service interruption warning | Email + in-app |
| Day 10 | Final retry | System |
| Day 12 | Last chance: account will be paused | Email |
| Day 14 | Account paused (not deleted) | Email |
| Day 30 | Win-back attempt with easy reactivation | Email |

Pre-dunning (proactive): Send card expiration reminder 30, 14, and 7 days before expiry.

#### 3.3 Health Scoring System

Design a customer health score using weighted signals:

| Signal | Weight | Healthy | At-Risk | Critical |
|---|---|---|---|---|
| Login frequency (last 30d) | 25% | 8+ sessions | 2-7 sessions | 0-1 sessions |
| Core feature usage | 25% | Uses 3+ core features | Uses 1-2 features | No core feature use |
| Support tickets (last 60d) | 15% | 0-1 tickets | 2-3 tickets | 4+ tickets |
| NPS/CSAT score | 15% | 9-10 (promoter) | 7-8 (passive) | 0-6 (detractor) |
| Billing issues (last 90d) | 10% | None | 1 failed payment | 2+ failed payments |
| Contract/renewal proximity | 10% | 6+ months | 1-6 months | Under 30 days |

Composite score: 0-100. Thresholds: Healthy (70-100), At-Risk (40-69), Critical (0-39).

#### 3.4 Save Offer Matrix

| Cancel Reason | Primary Offer | Secondary Offer | Do NOT Offer |
|---|---|---|---|
| Too expensive | 20-30% discount for 3 months | Downgrade to lower tier | Free extension (devalues) |
| Missing feature | Feature roadmap + timeline | Workaround documentation | Discount (wrong problem) |
| Not using it | 30-90 day pause | Onboarding session | Discount (wrong problem) |
| Competitor switch | Competitive comparison + match | Migration assistance from competitor | Desperate discounting |
| Business closed | Graceful exit + data export | Account freeze option | Any retention offer |

### Deliverables
- Cancel flow decision tree with offer routing logic
- Dunning sequence specification (timing, channels, copy briefs)
- Health scoring model with signal weights and thresholds
- Save offer matrix matched to cancel reasons

### Exit Conditions
- All selected interventions have complete specifications
- Offer routing logic documented
- Ethical review passed (no dark patterns)

---

## Phase 4: Sequence Building

### Purpose
Build the actual email sequences, in-app messages, and support triggers that execute the intervention designs from Phase 3.

### Entry Conditions
- Phase 3 complete: intervention designs approved
- Email infrastructure confirmed (ESP, transactional email provider)
- In-app messaging capability assessed

### Key Activities

#### 4.1 Email Sequence Production

For each intervention, build the complete email sequence:

**Dunning sequence** (load `./references/frameworks/dunning-email-sequence.md`):
- 4-6 emails over 14 days
- Each email: subject line, preview text, body copy, CTA
- Escalating urgency: informational -> warning -> final notice
- Payment update deep link in every email

**Win-back sequence** (load `./references/frameworks/win-back-email-sequence.md`):
- 3-5 emails over 60-90 days post-churn
- Sequence: "We miss you" -> product update -> special offer -> final attempt
- Include reactivation link with pre-filled account recovery

**Proactive retention outreach** (load `./references/frameworks/proactive-retention-emails.md`):
- Triggered by health score dropping below threshold
- Sequence: check-in -> value reminder -> support offer -> escalation to account manager

#### 4.2 In-App Messaging

- Payment failure banner: persistent, non-dismissible until resolved
- Health score-triggered tooltips: guide at-risk users to underused features
- Cancel flow UI: survey -> dynamic offer -> confirmation -> exit survey

#### 4.3 Support Triggers

Define escalation rules for the support team:

| Trigger | Action | SLA |
|---|---|---|
| Health score drops to Critical | Assign to retention specialist | 24 hours |
| High-LTV customer initiates cancel | Route to account manager | 2 hours |
| 3+ support tickets in 7 days | Proactive outreach from support lead | Same day |
| Failed payment after 3 retries | Phone call from billing support | 48 hours |

#### 4.4 Subject Line Selection

Load `./references/frameworks/subject-line-reference.md` for tested subject lines by sequence type. Key benchmarks:

- Dunning email open rates: target 50-65% (transactional urgency)
- Win-back email open rates: target 20-30%
- Proactive retention open rates: target 35-45%

### Deliverables
- Complete email sequences (copy-ready) for each intervention
- In-app messaging specifications
- Support team escalation playbook
- Subject line variants for A/B testing

### Exit Conditions
- All sequences reviewed for brand voice consistency
- Ethical review passed (no manipulative urgency, honest deadlines)
- Technical implementation requirements documented

---

## Phase 5: Measurement & Iteration

### Purpose
Track retention intervention performance, run cohort analysis, and iterate on underperforming sequences.

### Entry Conditions
- Phase 4 sequences deployed or ready for deployment
- Analytics tracking confirmed for retention events

### Key Activities

#### 5.1 Core Retention Metrics

| Metric | Definition | Benchmark (SaaS) | Measurement Frequency |
|---|---|---|---|
| Gross churn rate | Lost MRR / Starting MRR | 3-7% monthly | Monthly |
| Net churn rate | (Lost MRR - Expansion MRR) / Starting MRR | < 0% (net negative = growth) | Monthly |
| Logo churn rate | Lost customers / Starting customers | 3-5% monthly (SMB), 0.5-1% (enterprise) | Monthly |
| Involuntary churn rate | Failed payment churn / Total churn | < 30% of total churn | Monthly |
| Dunning recovery rate | Recovered payments / Total failed payments | 30-50% | Weekly |
| Cancel flow save rate | Saved cancellations / Total cancel attempts | 10-15% (good), 20%+ (excellent) | Weekly |
| Win-back reactivation rate | Reactivated / Total churned (90-day window) | 3-5% | Monthly |
| Customer health score distribution | % Healthy / At-Risk / Critical | 60%+ Healthy | Weekly |

#### 5.2 Cohort Analysis

Run monthly cohort retention curves:
- Track retention by signup month through months 1, 3, 6, 12
- Compare cohorts before and after intervention deployment
- Segment by acquisition channel, plan type, and company size
- Target: each new cohort's 90-day retention should exceed the previous cohort's

#### 5.3 A/B Testing

Load `./references/frameworks/cancel-flow-ab-testing.md` for detailed methodology.

Priority test sequence for retention:
1. Save offer type (discount vs pause vs downgrade) -- largest expected impact
2. Dunning email cadence (aggressive vs gentle timing)
3. Cancel flow survey placement (before vs after offer)
4. Win-back email timing (30-day vs 60-day first touch)
5. Subject lines within each sequence
6. Health score thresholds for intervention triggers

Minimum sample sizes for retention tests:
- Cancel flow save rate: 500+ cancel attempts per variant
- Dunning recovery: 200+ failed payments per variant
- Win-back campaigns: 1,000+ recipients per variant

#### 5.4 Iteration Cadence

| Review | Frequency | Focus |
|---|---|---|
| Dunning performance | Weekly | Recovery rate, retry success, email engagement |
| Cancel flow metrics | Bi-weekly | Save rate by reason, offer acceptance rate |
| Cohort retention curves | Monthly | Month-over-month trend, segment breakdowns |
| Health score calibration | Quarterly | Re-weight signals based on actual churn correlation |
| Full retention audit | Quarterly | All metrics, competitive benchmarking, strategy refresh |

### Deliverables
- Retention dashboard specification (metrics, dimensions, refresh cadence)
- A/B test roadmap for retention interventions
- Monthly retention report template
- Quarterly retention strategy review template

### Exit Conditions
- All core metrics have tracking in place
- First A/B test launched or scheduled
- Reporting cadence established

---

## Diagnostic Questions

Ask these before producing any retention recommendation. Recommendations without this data are assumptions, not strategies.

1. **Churn rate**: What is your current monthly churn rate (logo and revenue)? How is it measured?
2. **Churn type split**: What percentage of churn is involuntary (payment failures) vs voluntary (active cancellation)?
3. **Cancel reasons**: Do you have exit survey data? What are the top 3 stated cancel reasons?
4. **Churn timing**: When do most customers churn -- month 1, month 3, after annual renewal? Do you have cohort data?
5. **Current interventions**: What retention mechanisms are already in place? (Cancel flow, dunning, save offers, health scoring?)
6. **Billing infrastructure**: What payment processor and subscription management platform are you using? (Stripe, Chargebee, Recurly, etc.)
7. **Customer segments**: What is your customer breakdown by plan tier and contract type (monthly vs annual)?
8. **Product engagement data**: Do you track feature usage and login frequency? What tool? (Mixpanel, Amplitude, Heap, etc.)
9. **Revenue context**: What is your ARPU? What is your customer acquisition cost? (Needed to calculate recovery ROI.)
10. **Team capacity**: Who handles retention today? Is there a dedicated retention team or is it shared with support?

If the user cannot answer questions 1-3, recommend implementing exit surveys and churn tracking before designing interventions. Retention without measurement is guessing.

---

## Escalation Routes

| Signal Detected | Escalate To | Reason |
|---|---|---|
| Pricing/positioning mismatch as top cancel reason | paw-mkt-pricing | Retention cannot fix a pricing problem |
| Low activation as churn driver | paw-mkt-cro (onboarding) | This is an onboarding failure, not a retention failure |
| Email deliverability issues with dunning/win-back | paw-mkt-email | Sequences that do not reach inbox cannot recover revenue |
| Competitor switching as dominant reason | paw-mkt-product-context | Positioning and differentiation work needed |
| Content/education gap driving churn | paw-mkt-content | Customer success content strategy needed |
| Traffic source quality affecting retention | paw-mkt-paid-ads | Acquiring wrong-fit customers |
| Need for community-driven retention | paw-mkt-community | Community as retention lever |

---

## Ethics: Retention Without Manipulation

Retention work directly affects whether customers can leave a product. The ethical line must be clear and non-negotiable.

### Ethical Retention Practices

- **Cancel must be completable in 3 clicks or fewer.** No phone-call-required cancellation, no hidden cancel buttons, no redirect loops.
- **Save offers are presented once.** If the customer declines, proceed to cancellation immediately. No second pop-up, no guilt trip, no countdown timer.
- **Dunning communications are factual.** "Your payment failed" is appropriate. "Your account will be PERMANENTLY DELETED" when you retain data for 90 days is dishonest.
- **Data retention is transparent.** Tell customers exactly how long you keep their data and how to reactivate.
- **Pause options are genuine.** If you offer a pause, the account actually pauses -- no stealth billing during pause.

### Dark Patterns to Refuse

| Pattern | Description | Why It Harms |
|---|---|---|
| Cancel maze | Hiding cancellation behind multiple screens, phone calls, or chat-only | Delays churn but creates brand enemies; regulatory risk (FTC Click-to-Cancel rule) |
| Guilt-trip copy | "Are you sure? Your team will lose access to everything" with no alternative | Creates resentment, negative reviews, social media backlash |
| Infinite save loop | Presenting offer after offer, never allowing clean exit | Hostile UX that violates customer autonomy |
| Stealth billing | Continuing to charge after "pause" or unclear trial-to-paid conversion | Chargebacks, legal liability, trust destruction |
| Data hostage | Making data export difficult to discourage cancellation | Short-term retention, long-term brand damage |

Before implementing any retention mechanism, ask: **If the customer understood exactly how this works, would they feel respected?** If the answer is no, redesign it.

---

## Path Resolution

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/retention/`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/retention/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All retention work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Churn Diagnosis Report | `churn-diagnosis-{YYYY-MM-DD}.md` | Churn type split, root cause analysis, data gaps, priority recommendations |
| Cancel Flow Specification | `cancel-flow-spec-{YYYY-MM-DD}.md` | Decision tree, survey design, offer routing logic, UI wireframe notes |
| Dunning Sequence | `dunning-sequence-{YYYY-MM-DD}.md` | Email sequence (timing, copy, CTAs), retry schedule, pre-dunning plan |
| Win-Back Campaign | `win-back-campaign-{YYYY-MM-DD}.md` | Email sequence, reactivation offers, segmentation, timing |
| Health Score Model | `health-score-model-{YYYY-MM-DD}.md` | Signals, weights, thresholds, intervention triggers |
| Retention Dashboard Spec | `retention-dashboard-{YYYY-MM-DD}.md` | Metrics, dimensions, targets, refresh cadence |
| Retention Roadmap | `retention-roadmap-{YYYY-MM-DD}.md` | Prioritized intervention backlog, timeline, expected recovery impact |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/retention/
  churn-diagnosis-{YYYY-MM-DD}.md
  cancel-flow-spec-{YYYY-MM-DD}.md
  dunning-sequence-{YYYY-MM-DD}.md
  win-back-campaign-{YYYY-MM-DD}.md
  health-score-model-{YYYY-MM-DD}.md
  retention-dashboard-{YYYY-MM-DD}.md
  retention-roadmap-{YYYY-MM-DD}.md

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/retention/
  (same structure as above)
```

---

## Response Protocol

When the user requests retention or churn prevention work:

1. **Load context**: Read brand context and SOSTAC plan when available. Check for existing retention deliverables.
2. **Run Phase 1 Diagnosis**: Ask diagnostic questions. Classify churn type. Identify root causes. Do NOT skip to intervention design.
3. **Prioritize** (Phase 2): Apply the retention priority stack. Calculate recovery opportunity.
4. **Route to capability**: Based on diagnosed problem, load the appropriate reference file:
   - Cancel flow -> `./references/cancel-flow-design.md`
   - Dunning/payment recovery -> `./references/payment-recovery.md`
   - Proactive retention -> `./references/proactive-retention.md`
   - Win-back -> `./references/win-back-campaigns.md`
   - Benchmarking -> `./references/benchmarks.md`
5. **Design interventions** (Phase 3): Build specifications matched to diagnosed causes.
6. **Build sequences** (Phase 4): Produce copy-ready email sequences and messaging specs.
7. **Define measurement** (Phase 5): Specify metrics, A/B tests, and iteration plan.
8. **Save deliverables** to the resolved path.
9. **Recommend next steps**: What to implement first, what to test, when to review.
