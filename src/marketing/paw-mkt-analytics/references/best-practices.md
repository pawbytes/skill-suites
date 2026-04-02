# Marketing Analytics Best Practices & Industry Standards (2025-2026)

**Purpose:** Reference for GA4, attribution, dashboards, UTM standards, experimentation, and analytics frameworks. Consult by section as needed.

---

## 1. GA4 Mastery

### Event Model Best Practices
- GA4 is event-based (not session-based like UA). Everything is an event.
- **Automatically collected**: page_view, session_start, first_visit, scroll, click, file_download
- **Recommended events**: login, sign_up, purchase, add_to_cart, begin_checkout, search, share, view_item
- **Custom events**: Use snake_case naming. Max 500 distinct event names. Group with event parameters.

### Event Naming Convention
```
{action}_{object}_{qualifier}
Examples: click_cta_header, submit_form_contact, view_pricing_page, start_free_trial
```
- Always lowercase, snake_case
- Be specific: "click_signup_button" not just "click"
- Consistent across the team (document in a naming guide)

### Key Events (Conversions)
- Mark 5-10 events as key events (formerly "conversions")
- Must include: primary business goal (purchase, lead_form_submit, trial_start)
- Should include: micro-conversions (email_signup, pricing_page_view, demo_request)
- Set conversion counting: "once per session" for leads, "every event" for purchases

### Data Retention
- Default: 2 months. Change to 14 months immediately.
- For longer history: export to BigQuery (free 10GB/month storage)

### Consent Mode v2 (Required EU/EEA)
- Sends pings to Google even without consent, enabling modeled conversions
- Two modes: Basic (no data until consent) and Advanced (cookieless pings)
- Integrates with CMP (Cookiebot, OneTrust, etc.)

---

## 2. Attribution Models

| Model | How It Works | Best For | Limitation |
|-------|-------------|----------|-----------|
| Last-click | 100% to final touchpoint | Simple ecommerce | Ignores awareness |
| First-click | 100% to first touchpoint | Brand awareness | Ignores conversion |
| Linear | Equal across all touches | Balanced view | Oversimplifies |
| Time-decay | More to recent touches | Long sales cycles | Undervalues TOFU |
| Position-based | 40% first, 40% last, 20% middle | B2B journeys | Arbitrary weights |
| Data-driven (GA4 default) | ML-modeled allocation | 600+ conversions/month | Needs data volume |
| Incrementality | Holdout test for true lift | Most accurate | Expensive, slow |
| MMM (Marketing Mix Modeling) | Statistical model of channel impact | Enterprise budget allocation | Complex, lagging |

### Practical Attribution Strategy
1. **Primary**: GA4 data-driven attribution for day-to-day optimization
2. **Validation**: Blended ROAS (total ad spend / total revenue) as sanity check
3. **Strategic**: Quarterly incrementality tests on top 2-3 channels
4. **Supplementary**: Post-purchase survey ("How did you hear about us?")

---

## 3. Dashboard Design

### KPI Hierarchy
```
North Star Metric
├── Primary KPIs (3-5 max, reviewed weekly)
│   ├── New customers / revenue
│   ├── CAC / ROAS
│   └── Retention rate
├── Channel KPIs (per channel, reviewed weekly)
│   ├── Traffic, conversion rate, CPA per channel
│   └── Pipeline generated per channel (B2B)
└── Diagnostic Metrics (investigated when KPIs move)
    ├── Bounce rate, session duration, pages/session
    ├── Ad CTR, quality score, impression share
    └── Email open rate, click rate, deliverability
```

### Dashboard Layout Principles
- **Executive dashboard**: 1 page, 5-8 metrics, trend lines, vs target
- **Channel dashboards**: Per-channel detail, actionable breakdowns
- **Real-time**: Only for launches, events, or anomaly detection
- **Update frequency**: Automated daily refresh. Manual commentary weekly.

### Common Dashboard Mistakes
- Too many metrics (>15 on one view)
- No context (numbers without targets, trends, or comparisons)
- Vanity metrics prominently placed (impressions, followers)
- No action triggers (what do we do when X drops?)
- Manual data entry (should be automated via API/connectors)

---

## 4. UTM Parameter Standards

### Naming Convention
Always: lowercase, hyphens between words, no spaces, no special characters.

### Standard Values

**utm_source** (where traffic comes from):
| Value | Use For |
|-------|---------|
| google | Google Ads, Google organic |
| facebook | Meta Ads (Facebook placements) |
| instagram | Meta Ads (Instagram placements) |
| linkedin | LinkedIn Ads or organic |
| tiktok | TikTok Ads |
| twitter | X/Twitter |
| email | Email campaigns |
| newsletter | Newsletter specifically |
| partner-{name} | Partner referrals |
| direct | Direct traffic campaigns |

**utm_medium** (how traffic arrives):
| Value | Use For |
|-------|---------|
| cpc | Paid search (cost per click) |
| cpm | Paid display (cost per thousand) |
| social | Organic social posts |
| paid-social | Paid social ads |
| email | Email campaigns |
| referral | Partner/affiliate referrals |
| organic | Organic search (typically auto-tagged) |
| affiliate | Affiliate programs |
| influencer | Influencer campaigns |
| display | Display advertising |
| video | Video advertising |

**utm_campaign** format:
```
{yyyy-mm}_{type}_{description}
Examples:
2025-03_launch_spring-sale
2025-04_nurture_onboarding-series
2025-03_retargeting_cart-abandoners
```

**utm_content** (ad/creative variant):
```
{format}_{variant}
Examples: video_testimonial-a, carousel_product-features, static_social-proof
```

**utm_term** (keyword or audience):
```
Used for: paid search keywords, audience segments
Examples: crm-software, enterprise-saas, retargeting-30day
```

### Platform-Specific Notes
- **Google Ads**: Use auto-tagging (gclid) AND manual UTMs. Auto-tagging feeds GA4 natively.
- **Meta Ads**: Set UTM parameters in ad URL settings. Use dynamic parameters: {{campaign.name}}, {{adset.name}}, {{ad.name}}
- **Email**: Most ESPs support dynamic UTM insertion per campaign/subscriber

---

## 5. Experimentation Framework

### A/B Test Process
1. **Hypothesis**: "Changing [X] will [improve Y] because [reason]"
2. **Metric**: Define primary metric and guardrail metrics
3. **Sample size**: Calculate required sample (use calculator). Minimum 1,000 per variant for landing pages.
4. **Duration**: Minimum 1-2 business weeks. Account for day-of-week patterns.
5. **Run**: No peeking. Let test reach significance.
6. **Analyze**: 95% statistical significance standard. Check for segment-level effects.
7. **Document**: Record hypothesis, result, learning, next test.

### What to Test (Priority Order)
1. **Headlines and value propositions** (highest impact)
2. **CTAs** (text, color, placement, size)
3. **Social proof** (testimonials, logos, numbers)
4. **Page layout** (hero section, above-the-fold content)
5. **Pricing presentation** (anchoring, framing, decoy)
6. **Form fields** (fewer = higher conversion, usually)
7. **Images/video** (human faces, product shots, UGC)

### ICE Scoring for Test Prioritization
- **Impact** (1-10): How much will this move the KPI?
- **Confidence** (1-10): How sure are we, based on data/research?
- **Ease** (1-10): How easy/fast to implement?
- Score = (I + C + E) / 3. Run highest scores first.

---

## 6. Key Frameworks

### AARRR (Pirate Metrics)

| Stage | Metric | Calculation | Healthy Benchmark |
|-------|--------|-------------|-------------------|
| Acquisition | CAC | Total marketing spend / new customers | Varies by vertical |
| Activation | Activation rate | Users who complete key action / signups | 20-40% (SaaS) |
| Retention | Retention rate | Users active month N / users from month 0 | 40-60% month 1, 25-35% month 6 |
| Referral | K-factor | Invites per user × conversion per invite | >1 = viral, 0.1-0.5 typical |
| Revenue | LTV | Avg revenue per user × avg lifespan | LTV:CAC ≥ 3:1 |

### LTV:CAC Analysis

| Ratio | Meaning | Action |
|-------|---------|--------|
| < 1:1 | Losing money per customer | Fix unit economics urgently |
| 1:1 - 2:1 | Barely sustainable | Optimize CAC or increase LTV |
| 3:1 | Healthy target | Maintain and optimize |
| 5:1+ | Under-investing in growth | Spend more on acquisition |
| 10:1+ | Significantly under-investing | Scale aggressively |

**LTV Calculation**: ARPU × Gross Margin % × (1 / Monthly Churn Rate)
Example: $50/mo × 80% × (1 / 5%) = $800 LTV

### Marketing Efficiency Ratio (MER)
```
MER = Total Revenue / Total Marketing Spend
```
- Blended metric across all channels. Not channel-specific.
- Healthy: 3-5x for DTC ecommerce, 5-10x for SaaS
- Track weekly as a sanity check against platform-reported ROAS.

---

## 7. Privacy-First Analytics

### Cookieless Alternatives
| Tool | Type | Privacy Level | Cost |
|------|------|--------------|------|
| GA4 | Full analytics | Medium (consent required in EU) | Free |
| Plausible | Privacy-focused | High (no cookies, GDPR compliant) | $9-99/mo |
| Fathom | Privacy-focused | High (no cookies) | $14-44/mo |
| PostHog | Product analytics | High (self-hosted option) | Free-$450+/mo |
| Matomo | Full analytics | High (self-hosted, GDPR compliant) | Free-$229+/mo |

### Server-Side Tracking
- Moves tracking logic from browser to server
- Bypasses ad blockers and ITP (Safari)
- More accurate data, better compliance
- Implementation: GTM Server-Side, Segment, Rudderstack
- All major ad platforms now support server-side event APIs

---

## 8. Reporting Templates

### Monthly Marketing Report Structure
1. **Executive Summary** (3-5 bullet points: wins, issues, next steps)
2. **KPI Dashboard** (North Star, primary KPIs vs targets, MoM and YoY trends)
3. **Channel Performance** (per-channel: spend, leads/revenue, CPA/ROAS, key changes)
4. **Experiments & Tests** (what was tested, results, learnings, next tests)
5. **Content Performance** (top content, traffic trends, conversion from content)
6. **Budget** (spend vs plan, forecast for next month)
7. **Priorities Next Month** (top 3-5 initiatives)

### Quarterly Strategy Review
1. SOSTAC re-check: Has the situation changed? Are objectives on track?
2. Channel portfolio review: What's working, what's not, reallocation recommendations
3. Competitive movement: Any major competitor changes?
4. Experiment roadmap: Next quarter's test priorities
5. Budget recommendation: Any reallocation needed?
