# Marketing Analytics Frameworks & Methodologies

> Comprehensive reference for analytics setup, measurement frameworks, attribution models, testing methodology, and data-driven marketing decision-making.

---

## Table of Contents

1. [GA4 Setup Checklist & Event Taxonomy](#ga4-setup-checklist--event-taxonomy)
2. [UTM Parameter Standards](#utm-parameter-standards)
3. [Marketing Attribution Models](#marketing-attribution-models)
4. [Dashboard Design Frameworks](#dashboard-design-frameworks)
5. [A/B Test Design Framework](#ab-test-design-framework)
6. [Cohort Analysis Methodology](#cohort-analysis-methodology)
7. [Customer LTV Calculation Methods](#customer-ltv-calculation-methods)
8. [Funnel Analysis Framework](#funnel-analysis-framework)
9. [Marketing Mix Modeling (MMM)](#marketing-mix-modeling-mmm)
10. [Data Quality & Governance](#data-quality--governance)

---

## GA4 Setup Checklist & Event Taxonomy

### Initial GA4 Configuration Checklist

#### Account & Property Setup
- [ ] Create GA4 property (separate from Universal Analytics if migrating)
- [ ] Set correct timezone and currency
- [ ] Link Google Ads account
- [ ] Link Google Search Console
- [ ] Link BigQuery (for raw data export)
- [ ] Set up data streams (web, iOS, Android as applicable)
- [ ] Configure data retention settings (14 months recommended)
- [ ] Enable Google Signals for cross-device tracking
- [ ] Set up user ID tracking for logged-in users
- [ ] Configure IP anonymization (verify GDPR compliance)

#### Consent & Privacy
- [ ] Implement cookie consent banner (TCF 2.0 or equivalent)
- [ ] Configure consent mode v2 (basic or advanced)
- [ ] Set up server-side tagging (recommended for first-party data)
- [ ] Enable consent-aware measurement
- [ ] Define data retention policies
- [ ] Document data processing agreements

#### Enhanced Measurement (Auto-tracked)
- [ ] Page views (enabled by default)
- [ ] Scrolls (90% threshold)
- [ ] Outbound clicks
- [ ] Site search
- [ ] Video engagement (YouTube embeds)
- [ ] File downloads
- [ ] Form interactions

#### Custom Event Taxonomy

##### Engagement Events
| Event Name              | Parameters                          | Trigger                    |
|-------------------------|-------------------------------------|----------------------------|
| `page_view`             | page_title, page_location           | Every page load            |
| `scroll_depth`          | percent_scrolled (25, 50, 75, 100)  | Scroll thresholds          |
| `click_cta`             | cta_text, cta_location, cta_destination | CTA button clicks     |
| `video_play`            | video_title, video_duration         | Video play initiated       |
| `video_complete`        | video_title, video_duration         | Video watched to end       |
| `content_share`         | content_type, share_platform        | Share button clicks        |
| `search`                | search_term                         | Site search used           |

##### Conversion Events
| Event Name              | Parameters                          | Trigger                    |
|-------------------------|-------------------------------------|----------------------------|
| `generate_lead`         | lead_type, form_name, value         | Form submission            |
| `sign_up`               | method, plan_type                   | Account creation           |
| `begin_trial`           | trial_type, plan_name               | Free trial started         |
| `purchase`              | transaction_id, value, currency, items | Purchase completed     |
| `subscribe`             | plan_name, value, billing_cycle     | Subscription started       |
| `upgrade`               | from_plan, to_plan, value           | Plan upgrade               |
| `add_to_cart`           | items, value                        | Item added to cart         |
| `begin_checkout`        | items, value, coupon                | Checkout initiated         |

##### Product Events (SaaS-specific)
| Event Name              | Parameters                          | Trigger                    |
|-------------------------|-------------------------------------|----------------------------|
| `feature_used`          | feature_name, feature_category      | Key feature interaction    |
| `onboarding_step`       | step_number, step_name              | Onboarding progress        |
| `onboarding_complete`   | time_to_complete                    | Onboarding finished        |
| `invite_sent`           | invite_method                       | Team invite sent           |
| `integration_connected` | integration_name                    | Third-party integration    |
| `export_data`           | export_type, export_format          | Data exported              |

##### E-commerce Events (GA4 recommended)
| Event Name              | Parameters                          | Trigger                    |
|-------------------------|-------------------------------------|----------------------------|
| `view_item`             | items (id, name, category, price)   | Product page viewed        |
| `view_item_list`        | items, item_list_name               | Category/list viewed       |
| `select_item`           | items, item_list_name               | Product clicked in list    |
| `add_to_wishlist`       | items, value                        | Added to wishlist          |
| `view_cart`             | items, value                        | Cart page viewed           |
| `remove_from_cart`      | items, value                        | Item removed from cart     |
| `add_shipping_info`     | shipping_tier, value                | Shipping step completed    |
| `add_payment_info`      | payment_type, value                 | Payment step completed     |

### GA4 Key Dimensions & Metrics to Configure
- **Custom dimensions**: user_type, subscription_plan, company_size, industry
- **Custom metrics**: feature_usage_count, session_score
- **Audiences**: Trial users, paying customers, churned users, power users, dormant users
- **Conversions**: Mark key events as conversions (max 30 custom conversions)

---

## UTM Parameter Standards

See dedicated file: `./references/utm-standards.md` for comprehensive UTM naming conventions.

### Quick Reference
| Parameter      | Purpose                    | Example                    |
|----------------|----------------------------|----------------------------|
| `utm_source`   | Where traffic comes from   | google, facebook, newsletter |
| `utm_medium`   | Marketing channel type     | cpc, social, email         |
| `utm_campaign` | Specific campaign name     | spring-sale-2026           |
| `utm_term`     | Paid keyword (optional)    | marketing+automation       |
| `utm_content`  | Ad/content variation       | hero-cta-v2, blue-banner   |

---

## Marketing Attribution Models

### Model Comparison

#### Last-Click Attribution
- **How it works**: 100% credit to the last touchpoint before conversion
- **Pros**: Simple, easy to implement, actionable
- **Cons**: Ignores awareness and consideration touchpoints; over-credits bottom-funnel
- **Best for**: Direct response campaigns, short sales cycles
- **GA4 default**: Yes (reporting default)

#### First-Click Attribution
- **How it works**: 100% credit to the first touchpoint in the journey
- **Pros**: Highlights discovery and awareness channels
- **Cons**: Ignores nurture and conversion touchpoints
- **Best for**: Understanding top-of-funnel performance, brand awareness evaluation
- **GA4 default**: No (available in comparisons)

#### Linear Attribution
- **How it works**: Equal credit distributed across all touchpoints
- **Pros**: Acknowledges every touchpoint; balanced view
- **Cons**: Doesn't distinguish high-impact from low-impact touchpoints
- **Best for**: Long sales cycles with multiple meaningful touchpoints
- **GA4 default**: No (available in comparisons)

#### Time-Decay Attribution
- **How it works**: More credit to touchpoints closer to conversion; exponential decay
- **Pros**: Rewards recent engagement, reflects recency bias
- **Cons**: May undervalue initial awareness touchpoints
- **Best for**: B2B with long sales cycles, consideration-heavy purchases
- **GA4 default**: No (available in comparisons)

#### Position-Based (U-shaped) Attribution
- **How it works**: 40% first touch, 40% last touch, 20% distributed across middle
- **Pros**: Credits both discovery and conversion; acknowledges middle
- **Cons**: Arbitrary weighting; middle touches may be undervalued
- **Best for**: Balanced marketing programs with both awareness and conversion focus

#### Data-Driven Attribution (DDA)
- **How it works**: Machine learning analyzes all paths, assigns credit based on actual impact
- **Pros**: Most accurate; learns from your data; no arbitrary rules
- **Cons**: Requires significant data volume; black-box model; GA4 implementation varies
- **Best for**: Mature marketing programs with sufficient conversion volume
- **GA4 default**: Yes (default for Ads reports; requires sufficient data)
- **Minimum data**: ~300 conversions/month recommended for reliable DDA

#### Marketing Mix Modeling (MMM)
- **How it works**: Statistical analysis of aggregate marketing spend vs. business outcomes
- **Pros**: Privacy-friendly (no user-level data); includes offline channels; accounts for external factors
- **Cons**: Requires 2-3 years of data; expensive to implement; slow to update
- **Best for**: Enterprise brands with large multi-channel budgets; post-cookie planning
- **Tools**: Meta Robyn (open source), Google Meridian, Recast, Paramark

### Attribution Model Selection Guide
| Scenario                              | Recommended Model           |
|---------------------------------------|----------------------------|
| Limited data, simple funnel           | Last-click                 |
| Evaluating brand awareness            | First-click                |
| Long B2B sales cycle                  | Time-decay or Position-based |
| Mature program, high volume           | Data-driven                |
| Multi-channel, large budget           | MMM + DDA hybrid           |
| Privacy-first, cookieless future      | MMM + incrementality testing |

### Incrementality Testing
- **Purpose**: Measure true causal impact of a marketing channel
- **Method**: Geographic lift tests, holdout groups, PSA tests
- **When to use**: Validating attribution model outputs; evaluating channels with unclear ROAS
- **Tools**: Meta Conversion Lift, Google Geo-Lift, in-house holdout testing

---

## Dashboard Design Frameworks

### Executive Dashboard
- **Audience**: C-suite, board members
- **Update frequency**: Weekly or monthly
- **Key metrics**:
  - Revenue and MRR/ARR trend
  - Customer acquisition cost (CAC) and LTV:CAC ratio
  - Pipeline value and velocity
  - Channel-level ROAS/ROI summary
  - Key conversion rates (visitor > lead > customer)
  - Top-line growth rate vs. target
- **Design principles**: High-level KPIs only, trend lines, RAG status (red/amber/green), comparison to targets

### Channel Dashboard
- **Audience**: Marketing managers, channel owners
- **Update frequency**: Daily or weekly
- **Key metrics per channel**:
  - Spend, impressions, clicks, conversions
  - CPA, ROAS, CTR, conversion rate
  - Quality metrics (bounce rate, time on site, pages per session)
  - Funnel progression (MQL > SQL > Opportunity > Customer)
  - Budget pacing (actual vs. planned)
- **Design principles**: Channel comparison view, time-series trends, budget pacing gauges

### Campaign Dashboard
- **Audience**: Campaign managers, specialists
- **Update frequency**: Daily
- **Key metrics**:
  - Campaign-level performance (spend, conversions, CPA)
  - Ad set/ad group performance breakdown
  - Creative performance comparison
  - Audience segment performance
  - Landing page conversion rates
  - A/B test results
- **Design principles**: Drill-down capability, comparative tables, real-time data where possible

### Content Dashboard
- **Audience**: Content team, SEO team
- **Update frequency**: Weekly or monthly
- **Key metrics**:
  - Organic traffic by page/post
  - Keyword rankings and movements
  - Content engagement (time on page, scroll depth, shares)
  - Content-driven conversions
  - Content velocity (published vs. target)
  - Top-performing content by traffic, engagement, conversions
- **Design principles**: Content-level detail, ranking trend charts, content gap identification

### Dashboard Design Best Practices
1. **One question per section**: Each dashboard section answers one business question
2. **Progressive disclosure**: Overview first, then drill-down capability
3. **Context always**: Show comparisons (vs. target, vs. prior period, vs. benchmark)
4. **Limit metrics**: 5-8 KPIs per dashboard; more is noise
5. **Consistent time periods**: Same date range across all metrics
6. **Clear definitions**: Document what each metric means and how it is calculated
7. **Actionable**: Every metric should suggest an action when it changes

---

## A/B Test Design Framework

### Step 1: Hypothesis Formation
**Template**: "If we [change], then [metric] will [improve/increase/decrease] by [expected amount] because [rationale]."

**Example**: "If we change the CTA button from 'Learn More' to 'Start Free Trial', then the signup rate will increase by 15% because it sets a clearer expectation of the next step."

### Step 2: Test Parameters

#### Minimum Sample Size Calculation
| Baseline Rate | MDE (5%)  | MDE (10%) | MDE (20%) |
|---------------|-----------|-----------|-----------|
| 1%            | 62,000    | 15,700    | 4,000     |
| 2%            | 30,500    | 7,700     | 2,000     |
| 5%            | 11,800    | 3,000     | 780       |
| 10%           | 5,600     | 1,400     | 380       |
| 20%           | 2,500     | 640       | 170       |

*Per variation, at 80% power and 95% significance level.*
*MDE = Minimum Detectable Effect (relative change you want to detect).*

#### Test Duration Guidelines
- **Minimum**: 7 days (capture day-of-week effects)
- **Recommended**: 14-28 days
- **Maximum**: 42 days (avoid novelty effect decay)
- **Traffic calculation**: Required sample / daily traffic = minimum days
- **Always run full weeks**: End on the same day you started

### Step 3: Test Execution Checklist
- [ ] Define primary metric (one metric, one hypothesis)
- [ ] Define secondary metrics (guardrail metrics)
- [ ] Calculate required sample size
- [ ] Estimate test duration based on traffic
- [ ] Implement tracking for all metrics
- [ ] QA both variations across devices and browsers
- [ ] Verify random traffic allocation
- [ ] Set up monitoring for technical issues
- [ ] Document the test in a test log
- [ ] Do NOT peek at results before the test is complete

### Step 4: Analysis & Decision
- **Statistical significance**: p < 0.05 (95% confidence)
- **Practical significance**: Is the effect size meaningful for the business?
- **Segment analysis**: Check if the effect holds across key segments
- **Revenue impact**: Calculate expected annual revenue impact of the change
- **Decision framework**:
  - **Clear winner (significant + practical)**: Implement winner
  - **Significant but small effect**: Consider cost of implementation vs. benefit
  - **Not significant**: Keep control; test a bolder variation
  - **Negative result**: Valuable learning; document and move on

### Common A/B Testing Mistakes
1. Stopping tests early when results look good ("peeking")
2. Testing too many variations with insufficient traffic
3. Not accounting for seasonality or external events
4. Testing trivial changes (button color) instead of meaningful ones (value proposition)
5. Running overlapping tests that interact with each other
6. Ignoring secondary metrics and guardrails
7. No documentation of test learnings

---

## Cohort Analysis Methodology

### What Is Cohort Analysis?
Grouping users by a shared characteristic (usually acquisition date) and tracking their behavior over time. Essential for understanding retention, LTV, and product-market fit.

### Cohort Types

#### Acquisition Cohorts
- **Grouped by**: Sign-up date (week or month)
- **Track**: Retention rate, activation rate, revenue per user
- **Use case**: Are we acquiring better or worse users over time?

#### Behavioral Cohorts
- **Grouped by**: Action taken (e.g., completed onboarding, used feature X)
- **Track**: Retention, upgrade rate, LTV
- **Use case**: Which behaviors correlate with retention?

#### Channel Cohorts
- **Grouped by**: Acquisition channel (organic, paid, referral)
- **Track**: Retention, LTV, payback period
- **Use case**: Which channels bring the highest-quality users?

### Cohort Retention Table Template
| Cohort    | Month 0 | Month 1 | Month 2 | Month 3 | Month 6 | Month 12 |
|-----------|---------|---------|---------|---------|---------|----------|
| Jan 2026  | 100%    | 65%     | 52%     | 45%     | 35%     | -        |
| Feb 2026  | 100%    | 68%     | 55%     | 48%     | -       | -        |
| Mar 2026  | 100%    | 70%     | 58%     | -       | -       | -        |

### Reading Cohort Data
- **Horizontal**: How a single cohort retains over time (retention curve)
- **Vertical**: How retention at a given period changes across cohorts (improvement trend)
- **Diagonal**: What is happening right now across all active cohorts
- **Healthy sign**: Retention flattens (finds a floor) rather than continually declining
- **Product-market fit signal**: Month-over-month retention improvement in newer cohorts

---

## Customer LTV Calculation Methods

### Method 1: Historical LTV (Simple)
```
LTV = Average Revenue per User (ARPU) x Average Customer Lifespan
```
- **Example**: $50/month x 24 months = $1,200
- **Pros**: Simple, easy to calculate
- **Cons**: Backward-looking, ignores churn trends

### Method 2: Predictive LTV (Retention-based)
```
LTV = ARPU x Gross Margin / Monthly Churn Rate
```
- **Example**: $50 x 0.80 / 0.05 = $800
- **Pros**: Forward-looking, accounts for churn
- **Cons**: Assumes constant churn rate (rarely true)

### Method 3: Cohort-based LTV
- Calculate cumulative revenue per cohort over time
- Plot revenue curves, extrapolate to steady state
- **Pros**: Most accurate, accounts for cohort differences
- **Cons**: Requires historical cohort data, complex

### Method 4: DCF LTV (Discounted Cash Flow)
```
LTV = Sum of [ (ARPU x Gross Margin x Retention Rate^n) / (1 + Discount Rate)^n ]
for n = 0 to infinity
```
- **Pros**: Accounts for time value of money, most financially rigorous
- **Cons**: Requires discount rate assumption, complex to implement

### LTV:CAC Ratio Benchmarks
| Ratio    | Interpretation                                       |
|----------|------------------------------------------------------|
| < 1:1    | Losing money on every customer                       |
| 1:1-2:1  | Barely break-even; improve retention or reduce CAC   |
| 3:1      | Healthy SaaS benchmark; standard target              |
| 5:1+     | Excellent, but may be under-investing in growth      |

### CAC Payback Period Benchmarks
| Payback     | Rating    | Notes                                     |
|-------------|-----------|-------------------------------------------|
| < 6 months  | Excellent | Aggressive growth is viable                |
| 6-12 months | Good      | Standard for most SaaS                     |
| 12-18 months| Okay      | Monitor closely; look for improvements     |
| 18+ months  | Concerning| Cash flow risk; reduce CAC or improve ARPU |

---

## Funnel Analysis Framework

### The Three-Step Funnel Methodology

#### Step 1: Identify
Map every stage of your customer journey and define what constitutes progression.

**Standard Marketing Funnel Stages**:
1. **Awareness**: Impression, ad view, content view
2. **Interest**: Website visit, content engagement (scroll, time on page)
3. **Consideration**: Multiple visits, email signup, content download, pricing page view
4. **Intent**: Trial signup, demo request, add to cart
5. **Evaluation**: Trial usage, demo completion, proposal review
6. **Purchase**: Subscription, purchase, contract signed

**SaaS-Specific Funnel**:
1. Website visitor
2. Signup / trial start
3. Activation (reaches "aha moment")
4. Conversion (free to paid)
5. Expansion (upgrade, add seats)
6. Advocacy (referral, review)

#### Step 2: Measure
For each stage transition, calculate:
- **Conversion rate**: Users progressing / Users at previous stage
- **Drop-off rate**: 1 - conversion rate
- **Time to convert**: Average time between stages
- **Volume**: Absolute numbers at each stage

**Benchmark Conversion Rates (SaaS)**:
| Stage Transition          | Benchmark Range |
|---------------------------|-----------------|
| Visit > Signup            | 2-5%            |
| Signup > Activation       | 20-40%          |
| Activation > Paid         | 15-30%          |
| Trial > Paid              | 10-25%          |
| Free > Paid (freemium)    | 2-5%            |
| Monthly > Annual          | 20-40%          |

#### Step 3: Optimize
- **Find the biggest leak**: Calculate absolute lost users at each stage
- **Prioritize by impact**: Biggest leak x easiest fix = highest priority
- **Test hypotheses**: Run A/B tests on the highest-impact stage
- **Track improvement**: Monitor cohort-over-cohort improvement at the optimized stage
- **Iterate**: Move to the next biggest leak once current stage is improved

### Funnel Visualization Best Practices
- Show both percentages and absolute numbers
- Highlight the biggest drop-off stage
- Compare funnel performance across time periods
- Segment funnels by channel, persona, or cohort
- Include time-between-stages where relevant

---

## Marketing Mix Modeling (MMM)

### When to Use MMM
- Annual marketing budget exceeds $500K
- Running 5+ channels simultaneously
- Need to account for offline channels (TV, radio, OOH)
- Cookie deprecation concerns affecting digital attribution
- Need to quantify external factors (seasonality, economy, competitor actions)

### MMM Process
1. **Data collection**: 2-3 years of weekly data (spend by channel, revenue, external factors)
2. **Variable selection**: Marketing spend, price, promotions, seasonality, macroeconomics
3. **Model building**: Regression analysis with adstock (decay) and saturation (diminishing returns)
4. **Validation**: Out-of-sample testing, comparison to known results
5. **Optimization**: Budget allocation simulation to maximize ROI
6. **Refresh**: Update model quarterly or semi-annually

### Open Source MMM Tools
- **Meta Robyn**: R-based, automated hyperparameter tuning, well-documented
- **Google Meridian**: Python-based, Bayesian approach, newer but powerful
- **PyMC Marketing**: Python, flexible Bayesian modeling framework
- **Lightweight MMM (Google)**: Python, good for smaller datasets

---

## Data Quality & Governance

### Data Quality Checklist
- [ ] Tracking code fires on all pages/screens
- [ ] No duplicate events (check for double-firing)
- [ ] UTM parameters are consistent and following naming convention
- [ ] Cross-domain tracking configured correctly
- [ ] Bot/spam traffic filtered
- [ ] Internal traffic excluded
- [ ] Currency and timezone consistent
- [ ] Consent mode functioning correctly
- [ ] Regular data audits (monthly recommended)

### Reporting Hygiene Rules
1. **Define metrics once**: Create a shared glossary everyone uses
2. **Single source of truth**: One dashboard per KPI, not multiple conflicting reports
3. **Document methodology**: Every report explains how metrics are calculated
4. **Version control**: Track changes to tracking implementation
5. **Anomaly alerts**: Set up automated alerts for unexpected metric changes
6. **Regular audits**: Monthly check that tracking is functioning correctly

---

*This framework should be adapted to your specific tech stack, business model, and data maturity. Start with the basics (GA4 setup, UTM standards, basic funnel) and progressively add complexity (attribution modeling, cohort analysis, MMM) as your data infrastructure matures.*
