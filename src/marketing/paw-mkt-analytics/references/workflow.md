# Analytics Workflow

This reference defines the standard Measurement Framework Pipeline, diagnostic questions, data source requirements, tool recommendations, deliverable templates, and ethical guidelines that govern all analytics work.

---

## Measurement Framework Pipeline

Work through each phase sequentially. Do not skip phases — a dashboard built without a KPI hierarchy is a dashboard that displays noise instead of signal.

### Phase 1: Business Objectives Alignment

**Purpose:** Map business goals to measurable marketing outcomes. Every metric in the system must trace back to a business objective or it does not belong.

**Entry conditions:**
- Brand context is loaded (SOSTAC plan, product positioning, or brand brief)
- Stakeholder access confirmed (who will consume analytics outputs)
- Existing analytics state is known (tools in place, current tracking, known gaps)

**Diagnostic questions:**
1. What are the top 3 business objectives for the next 90 days? (Revenue growth, user acquisition, retention, market expansion, etc.)
2. Who are the primary stakeholders for analytics output? (CEO/founder, marketing lead, product team, investors)
3. What decisions will this data inform? (Budget allocation, channel prioritization, feature investment, hiring)
4. Is there an existing measurement framework, or are we starting from scratch?
5. What is the current analytics maturity level? (No tracking, basic GA, full stack with attribution)

**Key activities:**
- Document business objectives in measurable terms ("Increase MRR from $50K to $75K in Q3" not "grow revenue")
- Map each objective to the marketing levers that influence it (acquisition channels, conversion points, retention loops)
- Identify the decision-makers for each objective and their data literacy level
- Audit existing analytics infrastructure — what is tracked, what is missing, what is broken

**Deliverables:**
- Business Objectives Map: objectives -> marketing levers -> required measurement capabilities
- Analytics Maturity Assessment: current state, gaps, recommended investment

**Exit conditions:**
- All business objectives are documented with measurable targets
- Stakeholder map is complete with data consumption preferences
- Current analytics state is assessed — proceed to KPI Hierarchy

---

### Phase 2: KPI Hierarchy

**Purpose:** Define primary KPIs, secondary metrics, and leading/lagging indicators that form a coherent measurement system. The hierarchy prevents metric sprawl — every number on a dashboard must have a defined relationship to a business objective.

**Entry conditions:**
- Phase 1 complete — business objectives are documented and measurable
- Marketing channel mix is known (organic, paid, email, social, referral, etc.)

**Key activities:**
- Define the North Star Metric — the single metric that best captures the value the product delivers to customers
- Build the KPI tree: North Star -> Primary KPIs (3-5 max) -> Secondary Metrics (per channel/function) -> Leading Indicators

**KPI Hierarchy Structure:**

| Level | Definition | Example | Cadence |
|---|---|---|---|
| North Star | Single metric capturing core value delivery | Weekly Active Users, Monthly Revenue | Weekly review |
| Primary KPIs | 3-5 metrics directly tied to business objectives | MRR, CAC, Trial-to-Paid CVR, NRR | Weekly review |
| Secondary Metrics | Channel/function-level performance indicators | Organic traffic, Email open rate, ROAS by channel | Weekly review |
| Leading Indicators | Early signals that predict primary KPI movement | Demo requests, Trial activations, Feature adoption | Daily monitoring |
| Lagging Indicators | Outcome confirmations (slower to move) | LTV, Churn rate, NPS | Monthly/quarterly |

**Metric selection criteria:**
- **Actionable**: Can a team take a specific action based on this metric moving?
- **Accessible**: Can it be measured with available tools and data sources?
- **Auditable**: Can the calculation be reproduced and verified?
- **Aligned**: Does it connect to a business objective in the hierarchy?

**Deliverables:**
- KPI Hierarchy Document: visual tree + table with all metrics, owners, cadence, and targets
- Metric Ownership Matrix: who owns each metric, who reviews, who acts on changes

**Exit conditions:**
- North Star Metric is defined and agreed upon
- Primary KPIs are limited to 3-5 with explicit targets
- Every secondary metric maps to a primary KPI
- No orphan metrics — everything connects to the hierarchy

---

### Phase 3: Metric Definitions

**Purpose:** Eliminate ambiguity. Every metric must have one precise definition, one calculation method, and one source of truth. "Conversion rate" means nothing until you define the numerator, denominator, time window, and inclusion/exclusion criteria.

**Entry conditions:**
- Phase 2 complete — KPI hierarchy is defined
- Data sources are identified (even if not yet connected)

**Key activities:**
- Write a Metric Definition Card for every metric in the hierarchy

**Metric Definition Card Template:**

| Field | Description |
|---|---|
| **Metric Name** | Human-readable name (e.g., "Trial-to-Paid Conversion Rate") |
| **Business Question** | What question does this metric answer? ("What percentage of trial users become paying customers?") |
| **Formula** | Exact calculation (e.g., `(Paid conversions in period) / (Trial starts in same cohort) * 100`) |
| **Numerator Definition** | Precise definition with inclusion/exclusion criteria |
| **Denominator Definition** | Precise definition with inclusion/exclusion criteria |
| **Data Source** | Primary source (e.g., Stripe for revenue, GA4 for traffic, product DB for activations) |
| **Granularity** | Time granularity (daily, weekly, monthly) and segment dimensions (channel, geography, plan) |
| **Target** | Current baseline and target value with timeframe |
| **Action Threshold** | At what point does this metric trigger action? (e.g., "<2% triggers investigation, <1% triggers escalation") |
| **Owner** | Person or team accountable for this metric |
| **Known Limitations** | What this metric does NOT capture; edge cases; sampling caveats |

**Common definition pitfalls:**
- "Active users" without defining what "active" means (logged in? performed key action? opened email?)
- "Conversion rate" without specifying the conversion event and the denominator (visitors, sessions, unique users?)
- "Revenue" without specifying gross vs. net, one-time vs. recurring, refund treatment
- "Traffic" without distinguishing sessions vs. users vs. pageviews
- "CAC" without specifying which costs are included (ad spend only? salaries? tooling?)

**Deliverables:**
- Metric Definition Library: complete set of Metric Definition Cards
- Data Dictionary: all event names, properties, and expected values

**Exit conditions:**
- Every metric in the KPI hierarchy has a completed Metric Definition Card
- No two metrics share an ambiguous name (e.g., "conversion rate" is always qualified)
- Data sources are identified for every metric, even if not yet connected

---

### Phase 4: Tracking Implementation

**Purpose:** Translate metric definitions into working data collection. This phase bridges the gap between "what we want to measure" and "what the technology actually captures."

**Entry conditions:**
- Phase 3 complete — metric definitions are locked
- Technology stack is known (website platform, app framework, CRM, payment processor)
- Developer/engineering access or handoff path confirmed

**Key activities:**

#### Tag Management Setup
- **Recommended stack**: Google Tag Manager (GTM) for web; server-side GTM for privacy-sensitive implementations
- **Container architecture**: one GTM container per domain; separate containers for staging and production
- **Naming convention**: `Category - Action - Label` format (e.g., `CTA - Click - Hero Signup Button`)

#### Event Schema Design

| Event Category | Example Events | Required Properties |
|---|---|---|
| Pageview | `page_view` | `page_title`, `page_location`, `page_referrer`, `content_group` |
| Engagement | `scroll_depth`, `video_play`, `file_download` | `engagement_type`, `content_id`, `duration` |
| Conversion | `sign_up`, `purchase`, `demo_request` | `conversion_type`, `value`, `currency`, `method` |
| E-commerce | `add_to_cart`, `begin_checkout`, `purchase` | `items[]`, `value`, `currency`, `transaction_id` |
| Custom | `feature_used`, `plan_selected`, `onboarding_step` | Context-specific; define per event |

#### GA4 Configuration Checklist
- [ ] GA4 property created with correct data stream(s)
- [ ] Enhanced measurement enabled (scroll, outbound clicks, site search, video, file downloads)
- [ ] Custom events defined and documented
- [ ] Custom dimensions and metrics configured
- [ ] Conversion events marked
- [ ] Google Signals enabled (if privacy policy allows)
- [ ] Data retention set to 14 months
- [ ] Cross-domain tracking configured (if multiple domains)
- [ ] Internal traffic filter active
- [ ] BigQuery export linked (if applicable)

#### UTM Convention Standard

| Parameter | Format | Example |
|---|---|---|
| `utm_source` | Platform name, lowercase | `google`, `meta`, `linkedin`, `newsletter` |
| `utm_medium` | Traffic type | `cpc`, `email`, `social`, `referral`, `organic` |
| `utm_campaign` | Campaign identifier | `q3-2024-brand-awareness`, `black-friday-sale` |
| `utm_term` | Keyword or audience segment | `marketing-automation`, `cmo-audience` |
| `utm_content` | Creative variant identifier | `headline-a`, `video-v2`, `cta-green` |

**UTM rules:**
- All lowercase, hyphens instead of spaces, no special characters
- Document the naming convention in a shared UTM builder spreadsheet
- Never use UTM parameters on internal links (it destroys session attribution)
- Audit UTM consistency monthly — inconsistent tagging is worse than no tagging

#### Server-Side Tracking (when needed)
- Required for: accurate conversion tracking with ad blockers, HIPAA/sensitive data, high-value conversion events
- Implementation options: server-side GTM, Segment, RudderStack, custom API endpoints
- Trade-off: higher accuracy, higher implementation cost, requires server infrastructure

**Deliverables:**
- Tracking Implementation Spec: event schema, GTM configuration, custom dimensions, conversion events
- UTM Convention Document: naming rules, builder template, audit schedule
- QA Validation Checklist: expected events per page/flow with test procedures

**Exit conditions:**
- All events fire correctly in staging/preview mode
- Data appears in GA4 DebugView or equivalent
- UTM parameters are documented and builder is shared with the team
- QA sign-off on tracking accuracy

---

### Phase 5: Dashboard Design

**Purpose:** Build audience-specific dashboards that answer the viewer's question — not showcase available data. A dashboard no one checks is a dashboard that failed.

**Entry conditions:**
- Phase 4 complete — tracking is live and validated
- Stakeholder map from Phase 1 defines who sees what
- At least 1-2 weeks of data is flowing (for non-empty dashboards)

**Key activities:**

#### Dashboard Audience Matrix

| Audience | Questions They Ask | Update Cadence | Metrics Focus | Recommended Tool |
|---|---|---|---|---|
| Executive / Founder | "Are we growing? Are we efficient?" | Weekly | North Star, MRR, CAC, LTV, burn rate | Looker Studio, Notion embed, or slide deck |
| Marketing Lead | "Which channels perform? Where do we invest?" | Weekly | Channel ROAS, CVR by source, pipeline velocity | Looker Studio, HubSpot dashboards |
| Channel Owner | "Is my campaign working? What do I optimize?" | Daily | Campaign-level metrics, creative performance, CPA | Platform-native dashboards + Looker Studio |
| Product Team | "Are users engaging? Where do they drop?" | Weekly | Activation rate, feature adoption, retention cohorts | Amplitude, Mixpanel, PostHog |
| Sales Team | "Which leads are qualified? Where do they come from?" | Daily | MQL volume, lead source, pipeline by source | CRM dashboards (HubSpot, Salesforce) |

#### Dashboard Design Principles
1. **One question per section.** Each dashboard section answers one specific question. Label the section with the question, not the metric name. ("Are we acquiring users efficiently?" not "CAC Overview")
2. **Comparison is mandatory.** Never show a number without context. Compare to: prior period, target, benchmark, or trend. A standalone number is meaningless.
3. **5-second rule.** The most important insight should be visible within 5 seconds of opening the dashboard. If the viewer has to scroll or click to find the answer, redesign.
4. **Hierarchy matches KPI hierarchy.** Top of dashboard = North Star and primary KPIs. Below = secondary metrics. Drill-down = leading indicators and segment detail.
5. **No vanity metrics.** If a metric cannot trigger a decision or action, remove it from the dashboard.

#### Visualization Selection Guide

| Data Type | Best Visualization | Avoid |
|---|---|---|
| Trend over time | Line chart | Pie chart |
| Part of whole | Stacked bar, treemap | 3D pie chart |
| Comparison across categories | Horizontal bar chart | Vertical bar with too many categories |
| Single KPI with target | Scorecard with delta and sparkline | Gauge charts (low information density) |
| Funnel progression | Funnel chart or horizontal bar | Tables for funnels |
| Geographic distribution | Choropleth map | Tables with country names |
| Correlation | Scatter plot | Side-by-side line charts |

**Deliverables:**
- Dashboard Specification: wireframe layout per audience, metrics per section, visualization type, data source, filter dimensions
- Dashboard Build: implemented in Looker Studio, Amplitude, or agreed tool
- Dashboard User Guide: how to read each section, where to find drill-downs, when to escalate

**Exit conditions:**
- Each stakeholder group has a dashboard they actively use
- Dashboards are reviewed in at least one team meeting and confirmed useful
- No orphan dashboards — every dashboard has a named owner and review cadence

---

### Phase 6: Reporting & Insights

**Purpose:** Transform data into decisions. Dashboards show current state; reporting explains why it matters and what to do about it. This phase establishes cadence, templates, anomaly detection, and action triggers.

**Entry conditions:**
- Phase 5 complete — dashboards are live and in use
- At least 30 days of data for meaningful trend analysis
- Stakeholder feedback loop is established

**Key activities:**

#### Reporting Cadence

| Report Type | Cadence | Audience | Format | Key Contents |
|---|---|---|---|---|
| Pulse Check | Daily | Marketing team (Slack/email) | Automated alert | Key metric movements, anomalies, campaign status |
| Weekly Performance | Weekly | Marketing lead, channel owners | Written summary + dashboard link | Channel performance, WoW trends, action items |
| Monthly Business Review | Monthly | Executive team | Slide deck (5-10 slides max) | North Star progress, channel ROI, budget vs. actual, next month priorities |
| Quarterly Strategic Review | Quarterly | Leadership + stakeholders | Document + presentation | Goal progress, attribution insights, experiment results, strategic recommendations |
| Campaign Post-Mortem | Per campaign | Campaign team + marketing lead | Structured report | Objectives vs. results, learnings, recommendations for next campaign |

#### Insight Generation Framework

Every insight must follow this structure — raw data observations are not insights:

1. **Observation**: What happened? ("Organic traffic dropped 18% WoW")
2. **Diagnosis**: Why did it happen? ("Google algorithm update on March 15 impacted 3 high-traffic pages")
3. **Impact**: What does this mean for the business? ("Estimated loss of 240 trial signups this month at current CVR")
4. **Recommendation**: What should we do? ("Audit impacted pages against new E-E-A-T guidelines; prioritize content refresh for top 3 pages")
5. **Owner & Timeline**: Who acts, by when? ("SEO lead, action plan by Friday, implementation within 2 weeks")

#### Anomaly Detection & Action Triggers

Define thresholds that trigger automatic investigation or escalation:

| Metric | Warning Threshold | Critical Threshold | Action |
|---|---|---|---|
| Daily traffic | -15% vs. 7-day avg | -30% vs. 7-day avg | Investigate source; check for tracking issues |
| Conversion rate | -10% vs. 30-day avg | -20% vs. 30-day avg | Investigate funnel; check for UX changes |
| CAC | +15% vs. target | +30% vs. target | Review channel spend; check for audience saturation |
| ROAS | -10% vs. target | Below 1.0 | Pause underperforming campaigns; escalate to paid ads |
| Email deliverability | <95% delivery rate | <90% delivery rate | Investigate sender reputation; check for blacklisting |
| Bounce rate (key pages) | +10% vs. baseline | +25% vs. baseline | Check page load time; review recent changes |

#### Attribution Modeling

Attribution is directional, not absolute. Use multiple models to triangulate:

| Model | Best For | Limitation |
|---|---|---|
| Last-click | Understanding closing channels | Ignores awareness and consideration |
| First-click | Understanding discovery channels | Ignores nurture and closing |
| Linear | Fair distribution across touchpoints | Treats all touches equally regardless of impact |
| Time-decay | Weighting recent interactions | Still arbitrary weighting |
| Data-driven (GA4) | Best available algorithmic attribution | Requires significant conversion volume (300+/month) |
| Marketing Mix Modeling (MMM) | Channel-level budget allocation | Expensive; requires 2+ years of data |
| Incrementality testing | True causal impact measurement | Requires holdout groups; complex to execute |

**Recommendation**: Use data-driven attribution as the default in GA4. Supplement with first-click reporting for awareness channel evaluation. Run incrementality tests for high-spend channels ($10K+/month).

**Deliverables:**
- Reporting Calendar: cadence, owner, audience, template for each report type
- Report Templates: structured templates for each report type
- Anomaly Alert Configuration: thresholds, notification channels, escalation paths
- Attribution Model Documentation: chosen model(s), rationale, known limitations

**Exit conditions:**
- Reporting cadence is active and reports are being delivered on schedule
- At least one anomaly alert has been configured and tested
- Attribution model is documented with known limitations acknowledged
- Stakeholders confirm reports are actionable (not just informational)

---

## Tool Recommendations

### Analytics Platforms

| Tool | Best For | Price Range | Setup Complexity |
|---|---|---|---|
| **Google Analytics 4** | Web analytics, standard reporting | Free / 360 ($150K+/yr) | Medium |
| **Mixpanel** | Product analytics, event-based tracking | Free tier / $25+/mo | Medium |
| **Amplitude** | Product analytics, behavioral cohorts | Free tier / $49+/mo | Medium |
| **PostHog** | Open-source product analytics, session replay | Free self-hosted / cloud plans | Medium-High |
| **Heap** | Auto-capture everything, retroactive analysis | $$$$ (enterprise) | Low (auto-capture) |

### Tag Management

| Tool | Best For | Price |
|---|---|---|
| **Google Tag Manager** | Standard web tag management | Free |
| **Server-side GTM** | Privacy-compliant, high-accuracy tracking | Cloud hosting costs (~$50-200/mo) |
| **Segment** | Customer data platform, multi-destination routing | $120+/mo |
| **RudderStack** | Open-source CDP alternative | Free self-hosted / cloud plans |

### Dashboard & Visualization

| Tool | Best For | Price |
|---|---|---|
| **Looker Studio** | GA4 integration, shareable dashboards | Free |
| **Metabase** | Open-source BI, SQL-based | Free self-hosted / $85+/mo cloud |
| **Tableau** | Enterprise BI, complex visualization | $70+/user/mo |
| **Supermetrics** | Multi-source data pulling into Sheets/Looker | $39+/mo per connector |

### Testing & Experimentation

| Tool | Best For | Price |
|---|---|---|
| **Google Optimize** (sunset) | Migrate to alternatives below | N/A |
| **VWO** | A/B testing, heatmaps | $99+/mo |
| **Optimizely** | Enterprise experimentation | $$$$ |
| **PostHog** | Feature flags + experimentation | Free tier available |
| **Statsig** | Feature flags + experimentation at scale | Free tier / usage-based |

---

## Escalation Routes

Analytics work frequently surfaces problems that require other skills to resolve:

| Finding | Escalate To | Context to Pass |
|---|---|---|
| Conversion rate drop on key pages | **paw-mkt-cro** | Affected pages, traffic source, drop magnitude, funnel stage |
| Organic traffic decline | **paw-mkt-seo** | Affected pages, keyword rankings lost, algorithm update timeline |
| Email engagement declining | **paw-mkt-email** | Deliverability metrics, open/click trends, list health data |
| Paid channel ROAS below threshold | **paw-mkt-paid-ads** | Channel, campaign, audience, creative performance data |
| Social engagement dropping | **paw-mkt-social** | Platform, content type performance, audience growth/decline |
| Content performance declining | **paw-mkt-content** | Top/bottom performers, traffic trends, engagement metrics |
| Churn rate increasing | **paw-mkt-retention** | Cohort data, churn reasons if available, segment breakdown |
| Attribution shows channel mix shift | **paw-mkt-agency** | Full attribution report, budget allocation recommendations |
| Pricing page drop-off increasing | **paw-mkt-pricing** | Funnel data, pricing page analytics, competitor pricing context |

**Escalation protocol**: When escalating, always provide: (1) the specific metric and its movement, (2) the time range, (3) any diagnosis you have performed, (4) the data supporting the observation. Do not escalate raw numbers without context.

---

## Ethics: Data Privacy & Responsible Measurement

Analytics relies on collecting user behavior data. This comes with obligations — legal, ethical, and strategic.

### Privacy-First Measurement Principles

- **Consent before collection**: No tracking fires before the user has given informed consent (where legally required under GDPR, CCPA, ePrivacy Directive)
- **Minimum necessary data**: Collect only what is needed to answer defined business questions. Do not collect "just in case" data
- **Anonymization by default**: Use aggregated and anonymized data wherever possible. PII should only flow through systems that require it (CRM, payment) — never into analytics platforms without explicit consent and purpose
- **Retention limits**: Set data retention periods. GA4 default is 2 months for user-level data; extend to 14 months only if needed. Delete data you no longer use
- **Transparency**: Users should be able to understand what is collected and why. Privacy policies must be accurate and current

### Consent Management Implementation

| Requirement | Implementation |
|---|---|
| Cookie consent banner | Implement via CMP (Cookiebot, OneTrust, Osano, or custom) |
| Consent mode (Google) | Enable Google Consent Mode v2 for GA4 and Google Ads |
| Consent categories | Essential (always), Analytics (opt-in for EU), Marketing (opt-in for EU) |
| Consent logging | Store consent records with timestamp, version, and choices |
| Opt-out mechanism | Provide clear opt-out in privacy settings, not buried in footer links |

### Dark Patterns to Avoid in Analytics

| Pattern | Description | Why It Harms |
|---|---|---|
| Pre-checked consent | Analytics/marketing cookies checked by default | Illegal under GDPR; erodes trust |
| Consent wall | Blocking content entirely without consent | Violates ePrivacy guidance in most EU jurisdictions |
| Deceptive consent UI | "Accept All" prominent, "Manage" hidden/tiny | Regulatory risk; user resentment |
| Fingerprinting | Tracking without cookies via browser fingerprinting | Explicitly prohibited under GDPR as a tracking mechanism |
| Shadow tracking | Firing analytics tags before consent is granted | Direct GDPR/ePrivacy violation |
| PII in analytics | Sending email addresses, names, or IPs to GA4 | GA4 TOS violation; privacy regulation violation |

### The Business Case for Privacy-First Analytics

Privacy-compliant measurement is not a constraint — it is a competitive advantage:
- **Data quality improves**: consented users provide higher-quality signals than coerced consent
- **Regulatory risk drops**: GDPR fines can reach 4% of global revenue; CCPA fines up to $7,500 per intentional violation
- **User trust increases**: transparent data practices build brand credibility
- **Future-proofing**: cookie deprecation, browser restrictions, and new regulations all favor first-party, consent-based data strategies

Before implementing any tracking, ask: **If users fully understood what data is being collected and how it is used, would they still consent?** If the answer is uncertain, reconsider.

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** — working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/analytics/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** — evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/analytics/`

**Legacy fallback** — old directory structure detected:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/analytics/`
  -> Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All analytics work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Measurement Framework | `measurement-framework-{YYYY-MM-DD}.md` | Business objectives map, KPI hierarchy, metric definitions, data sources |
| Tracking Implementation Spec | `tracking-spec-{YYYY-MM-DD}.md` | Event schema, GTM configuration, custom dimensions, conversion events, QA checklist |
| UTM Convention Guide | `utm-conventions-{YYYY-MM-DD}.md` | Naming rules, parameter standards, builder template link, audit schedule |
| Dashboard Specification | `dashboard-spec-{audience}-{YYYY-MM-DD}.md` | Wireframe, metrics per section, visualization types, data sources, filters |
| Report Template | `report-template-{type}-{YYYY-MM-DD}.md` | Structure, metrics, insight format, distribution list |
| Attribution Analysis | `attribution-analysis-{YYYY-MM-DD}.md` | Model comparison, channel performance, budget recommendations |
| Analytics Audit | `analytics-audit-{YYYY-MM-DD}.md` | Current state, gaps, tracking accuracy, recommendations |
| Campaign Post-Mortem | `campaign-postmortem-{campaign-slug}-{YYYY-MM-DD}.md` | Objectives vs. results, channel breakdown, insights, next-campaign recommendations |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/analytics/
  measurement-framework-{YYYY-MM-DD}.md
  tracking-spec-{YYYY-MM-DD}.md
  utm-conventions-{YYYY-MM-DD}.md
  dashboard-spec-{audience}-{YYYY-MM-DD}.md
  report-template-{type}-{YYYY-MM-DD}.md
  attribution-analysis-{YYYY-MM-DD}.md

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/analytics/
  (same structure as above)
```

---

## Response Protocol

When the user requests analytics work:

1. **Route the starting context** (see `./references/shared-patterns.md` for Starting Context Router). Decide whether this is measurement framework, tracking implementation, dashboard design, or reporting work.
2. **Read the strongest available context** (Pre-Flight): brand and SOSTAC first when available; otherwise assess the existing analytics state.
3. **Identify the analytics domain.** Read the appropriate reference file before producing recommendations:
   - Measurement framework -> `./references/measurement-framework.md`
   - Tracking setup -> `./references/tracking-setup.md`
   - Dashboard design -> `./references/dashboard-design.md`
   - Reporting -> `./references/reporting.md`
   - Attribution -> `./references/attribution.md`
   - A/B testing -> `./references/ab-testing.md`
   - Funnel analysis -> `./references/funnel-analysis.md`
   - Marketing ROI -> `./references/marketing-roi.md`
   - Privacy/compliance -> `./references/privacy-compliance.md`
   - UTM standards -> `./references/utm-standards.md`
4. **Ask the diagnostic questions** from Phase 1 if the user has not already provided this context. Do not produce tracking specs without knowing business objectives.
5. **Work through the pipeline phases** in order. If the user requests a specific phase (e.g., "set up tracking"), verify that prerequisite phases are addressed or explicitly skipped.
6. **Deliver structured output.** Follow the deliverable templates. Every metric recommendation must include: name, formula, data source, target, and action threshold.
7. **Save deliverables** to the resolved path (see Path Resolution).
8. **Recommend next steps**: What to implement immediately, what requires engineering support, when to review initial data.

### When to escalate

- Conversion optimization needed based on funnel findings -- route to **paw-mkt-cro** skill with funnel data and drop-off analysis.
- Paid media performance questions surfacing from attribution -- route to **paw-mkt-paid-ads** skill with channel performance data.
- Email metrics declining -- route to **paw-mkt-email** skill with deliverability and engagement data.
- SEO traffic patterns require investigation -- route to **paw-mkt-seo** skill with organic traffic trends and page-level data.
- Brand positioning questions surface during measurement framework design -- route to **paw-mkt-product-context** or brand context update.
- Content performance analysis reveals strategic gaps -- route to **paw-mkt-content** skill with content analytics.
