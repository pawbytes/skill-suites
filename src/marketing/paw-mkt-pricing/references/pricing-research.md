# Pricing Research: Methods, Scripts, and Templates

**Purpose:** Full methodology, scripts, and templates for pricing research and price change communications. Read the relevant section when running a specific research method or drafting price increase emails.

---

## 1. Van Westendorp Price Sensitivity Meter (PSM)

### 1.1 What It Is

The Van Westendorp PSM is a survey-based pricing research methodology developed by Dutch economist Peter van Westendorp in 1976. It uses four questions to identify an acceptable price range and an optimal price point from the perspective of potential buyers. It does not require respondents to choose between options -- it asks them to draw their own price boundaries.

**Output**: Two key data points:
- **Acceptable Price Range** (APR): the range within which the price is defensible
- **Optimal Price Point** (OPP): the single price with the highest acceptance

**When to use**:
- Validating a new price point before launch
- Choosing between two or three candidate prices
- Understanding what price level is causing drop-off in conversion
- After adding significant new value and before raising prices

**When not to use**:
- Fewer than 80-100 respondents (results are not reliable)
- When you need to understand feature trade-offs (use conjoint analysis instead)
- When respondents have no familiarity with the product or category (stated WTP is not meaningful without context)

**Minimum sample size**: 100 responses for consumer; 50 for B2B (harder to recruit).

---

### 1.2 The Four Survey Questions

Administer these questions in order. Do not change the wording -- the questions are calibrated to produce distinct distributions.

Before asking the questions, provide a brief product description (2-4 sentences) so respondents understand what they are pricing. For existing products, show the current feature set.

---

**Question 1 -- Too Cheap**

> "At what [monthly / annual] price would you consider [Product Name] to be SO CHEAP that you would question the quality or wonder what was wrong with it?"

Response format: Open text entry (dollar amount) or slider ($X -- $X range).

---

**Question 2 -- Bargain (Acceptable/Cheap)**

> "At what [monthly / annual] price would you consider [Product Name] to be a BARGAIN -- a great buy for the money?"

Response format: Open text entry or slider.

---

**Question 3 -- Getting Expensive (Acceptable/Expensive)**

> "At what [monthly / annual] price would [Product Name] start to feel EXPENSIVE, though you might still consider purchasing it?"

Response format: Open text entry or slider.

---

**Question 4 -- Too Expensive**

> "At what [monthly / annual] price would [Product Name] be so EXPENSIVE that you would not consider purchasing it, regardless of quality?"

Response format: Open text entry or slider.

---

**Optional follow-up** (add context to the analysis):

> "What is your current [monthly] budget for tools like [Product Name]?"

> "Which of the following best describes your role?" [title/segment options]

> "How familiar are you with [Product Name]?" [Never heard of it / Heard of it / Trialed it / Current user]

---

### 1.3 How to Administer the Survey

**Platform options**:
- Typeform or Google Forms (free; manual analysis in spreadsheet)
- SurveyMonkey (has PSM analysis templates in paid plans)
- Qualtrics (built-in PSM module; enterprise)
- Wynter (specialized for B2B messaging and pricing research panels)

**Where to recruit respondents** (in order of quality):
1. Your existing customer base (segment by tier and tenure for comparison)
2. Trial users who did not convert (highest value for conversion analysis)
3. Your email list / newsletter subscribers
4. LinkedIn outreach to target persona (offer $25-$50 gift card incentive)
5. Prolific or User Interviews panel (fastest recruitment; costs $10-$30 per response)

**Survey context note**: Tell respondents you are gathering feedback on pricing, not that you are planning to raise prices. Framing matters. Use: "We are researching how to structure pricing for [Product Name] and would value your perspective."

---

### 1.4 Cleaning the Data

Before analysis, remove responses where:
- Any price is $0 (respondents did not take the question seriously)
- Prices are not monotonically ordered (Too Cheap < Bargain < Getting Expensive < Too Expensive). A small violation (e.g., Bargain slightly higher than Getting Expensive) is acceptable -- exclude only obvious outliers where the order is completely reversed.
- Prices are extreme outliers (more than 3 standard deviations from the mean for that question)

---

### 1.5 Analysis: Plotting the Four Curves

Create a chart with price on the X-axis and cumulative percentage of respondents on the Y-axis. Plot four lines:

| Curve | Data | Direction |
|---|---|---|
| Too Cheap | % of respondents who said "Too Cheap" at or below each price | Descending (as price rises, fewer say it is too cheap) |
| Bargain (Acceptable/Cheap) | % who said "Bargain" at or below each price | Descending |
| Getting Expensive (Acceptable/Expensive) | % who said "Getting Expensive" at or above each price | Ascending (as price rises, more say it is getting expensive) |
| Too Expensive | % who said "Too Expensive" at or above each price | Ascending |

**Key intersections**:

- **Point of Marginal Cheapness (PMC)**: Intersection of "Too Cheap" (descending) and "Too Expensive" (ascending). This is the lower bound of the Acceptable Price Range. Pricing below PMC triggers quality concerns.
- **Point of Marginal Expensiveness (PME)**: Intersection of "Bargain/Cheap" (descending) and "Getting Expensive" (ascending). This is the upper bound of the Acceptable Price Range. Pricing above PME triggers resistance.
- **Acceptable Price Range (APR)**: The range between PMC and PME. Prices within this range face the least resistance.
- **Optimal Price Point (OPP)**: Intersection of "Too Cheap" (descending) and "Bargain" (descending). The price with maximum acceptance -- the largest share of respondents find it neither too cheap nor a bargain (just right).

**Spreadsheet method** (no software required):
1. List every price point mentioned across all responses in a single column, sorted ascending.
2. For each price point, count how many respondents answered at-or-below (for descending curves) or at-or-above (for ascending curves).
3. Divide by total responses to get percentages.
4. Plot in Excel or Google Sheets as a line chart.
5. Find intersections visually or by interpolation.

**Tools for automated PSM analysis**:
- Peter van Westendorp PSM Calculator (free online tools available)
- R package `pricesensitivitymeter`
- Python: manual implementation in pandas with matplotlib

---

### 1.6 Interpreting Results

| Scenario | Interpretation | Action |
|---|---|---|
| Current price is below OPP | Underpricing -- room to raise | Raise price toward OPP; test on new customers first |
| Current price is above PME | Overpricing -- resistance zone | Lower price or add significant perceived value |
| Current price is within APR | Pricing is defensible | Optimize for value communication rather than price changes |
| APR is very narrow | High price sensitivity in this segment | Explore a lower-tier entry point; or target a less price-sensitive segment |
| OPP is lower than your cost floor | Product economics are broken | Reconsider value metric, cost structure, or target segment |

---

## 2. Willingness-to-Pay Customer Interview Script

### 2.1 Setup

**Who to interview**:
- 3-5 current customers on the highest tier (understand max WTP)
- 3-5 current customers on the lowest tier (understand price sensitivity)
- 3-5 churned customers (understand price breaking points)
- 3-5 prospects who did not convert after a trial (understand conversion blockers)

**Interview length**: 30-45 minutes.

**Format**: Video call. Record with permission ("I would like to record this to avoid taking notes -- is that okay?").

**Incentive**: $50-$100 Amazon gift card or equivalent. Never skip the incentive for customer interviews -- it signals that you value their time.

**Moderator note**: Do not lead with price questions. Build rapport and understand context first. The price questions (Q6-Q10) land differently when you understand how the person uses the product and what they compare it to.

---

### 2.2 Interview Script

**Introduction (2 min)**

> "Thank you for making time today. We are doing research to make sure our pricing reflects the value we actually deliver -- not just what our cost structure looks like. There are no right or wrong answers. I will ask you to think out loud as much as possible. Everything you share is confidential and will only be used in aggregate with other responses."

---

**Q1 -- Role and context**

> "To start -- can you tell me a bit about your role and what your team is trying to accomplish?"

*Listen for: company size, team size, their personal authority over the budget decision.*

---

**Q2 -- How they use the product**

> "Walk me through how you typically use [Product Name] in a given week."

*Listen for: which features get used, how deeply, how often, which features they skip.*

---

**Q3 -- Value delivered**

> "What would you say is the most valuable thing [Product Name] does for you or your team?"

*Listen for: the outcome in their language -- time saved, revenue generated, mistakes avoided, headcount avoided.*

---

**Q4 -- Quantifying value**

> "If you had to estimate the dollar value of what [Product Name] saves or generates for you in a month -- what would you guess? Even a rough ballpark is helpful."

*Listen for: ratio of value to current price. If value >> price, there is room to raise. If value ≈ price, they are at their ceiling.*

---

**Q5 -- Alternatives**

> "If [Product Name] did not exist, what would you do instead? How would you solve this problem?"

*Listen for: the next best alternative and its cost. This is your floor.*

---

**Q6 -- Current price reaction**

> "When you first saw our pricing, what was your reaction? Did it feel about right, expensive, or surprisingly affordable?"

*Listen for: unprompted price calibration. If "surprisingly affordable" -- you are underpriced.*

---

**Q7 -- Ceiling (open-ended)**

> "At what point -- what monthly price -- would you start to seriously reconsider whether [Product Name] is worth it?"

*Listen for: their personal ceiling. Note this exactly.*

---

**Q8 -- Floor (quality signal)**

> "Is there a price so low that you would question whether the product could actually be as good as it is?"

*Listen for: quality floor perception. Useful for freemium and low-tier design.*

---

**Q9 -- Competitive comparison**

> "Are there other tools or services you pay for that solve a similar problem? What do you pay for those?"

*Listen for: competitive price anchors in their mind.*

---

**Q10 -- Upgrade or churn trigger**

> "What would need to change -- in the product, in your situation, or in the pricing -- for you to [upgrade to a higher tier / consider canceling]?"

*Listen for: feature gates that drive upgrades, pricing thresholds that trigger churn.*

---

**Closing (2 min)**

> "That is really helpful. One last thing -- is there anything about pricing or value that you think we should know that I did not ask about?"

> "Thank you so much. We really appreciate you taking the time."

---

### 2.3 Synthesizing Interview Findings

After 10-15 interviews, create a synthesis document at `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/pricing/research/interview-synthesis-{YYYY-MM-DD}.md` (or `campaigns/{type}-{slug}/pricing/research/` if campaign-tied) with:

- **Ceiling range**: The range of monthly prices at which customers said they would reconsider
- **Value statements in customer language**: Direct quotes about what they would lose without the product
- **Next best alternative and its cost**: Average cost of the next best alternative -- this is your floor
- **Value-to-price ratio estimates**: Average estimated dollar value vs current price paid
- **Churn triggers**: Specific conditions that would cause customers to cancel
- **Upgrade triggers**: Specific features or conditions that would cause customers to pay more

---

## 3. Price Increase Email Templates

### 3.1 Usage Instructions

Choose a template based on the nature of the increase:
- **Template A**: Modest increase (under 20%) tied to new value delivered. Warm, confident tone.
- **Template B**: Significant restructuring. More explanation, grandfather offer, longer lead time.
- **Template C**: Legacy/grandfather notice. For customers kept at old price who are now transitioning.

Customize all placeholders in `[brackets]` before sending. These templates are starting points -- adapt to match your brand voice from `./.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md`.

Send from: a named person (CEO, founder, or Head of Product) -- not a generic marketing address. Personalize with the customer's first name and current plan.

---

### Template A: Modest Increase with New Value

**Subject**: A note about your [Brand Name] subscription

---

Hi [First Name],

I wanted to reach out personally to let you know about an upcoming change to your subscription.

Starting [DATE -- 60+ days from send], your [Plan Name] plan will move from **[$X/month]** to **[$Y/month]**.

This is the first time we have updated pricing in [X years/months], and it reflects the significant work we have shipped to the product since you joined. Since [rough timeframe], we have added:

- [New feature or capability 1]
- [New feature or capability 2]
- [New feature or capability 3]

We have also expanded our support team to [new support detail -- faster response times, extended hours, etc.].

**Your price stays the same until [DATE].** No action is needed -- your card will continue to be charged at the current rate until then.

If you would like to lock in 12 months at the current price, you can do that here: **[LINK]**. This option is available until [DATE -- 30 days before change].

If you have any questions, reply to this email and I will respond personally.

Thank you for being a [Brand Name] customer. We do not take that lightly.

[Signature -- CEO/Founder name, title]

---

P.S. If you are on annual billing, your renewal will be at the new rate when your current term ends. You will receive a reminder 30 days before renewal.

---

### Template B: Significant Restructuring

**Subject**: Changes to [Brand Name] pricing -- what this means for you

---

Hi [First Name],

We need to share some important news about your [Brand Name] subscription, and we wanted to give you as much time as possible to plan.

**What is changing**: On [DATE -- 90 days from send], we are updating our pricing structure. We are consolidating our plans from [old number] to [new number] tiers, and adjusting price points to better reflect the value the product delivers.

**What this means for you**: Your current [Plan Name] plan maps closest to our new [New Plan Name] plan, which will be **[$Y/month]**.

Here is what you are gaining with this change:
- [Specific feature or limit that improves for this customer's tier]
- [Specific feature or limit that improves]
- [Better support / new capability]

**We are grandfathering you at your current rate for [X months].** Until [DATE], you will continue to be billed at your current price of [$X/month]. After that date, your subscription will move to the new rate.

To lock in an additional 12 months at your current price before the transition, visit your billing page here: **[LINK]**.

We know pricing changes are disruptive, and we have tried to give you as much runway as possible. If this change significantly affects your situation, please reply to this email -- we will do our best to find a solution that works.

[Signature]

---

**FAQ -- you can link to a full FAQ page**:

**Q: Why are you changing pricing?**
A: [Honest, brief explanation -- infrastructure costs, R&D investment, market alignment, etc.]

**Q: Will my features change?**
A: [Clear answer specific to the recipient's tier.]

**Q: Can I downgrade to avoid the increase?**
A: Yes -- you can adjust your plan at any time from your account settings at [LINK].

**Q: I pay annually -- when does this affect me?**
A: Your annual subscription will renew at the new rate at the end of your current term. You will receive a reminder 30 days before.

---

### Template C: Legacy Grandfather Transition Notice

**Subject**: Your grandfathered [Brand Name] rate is changing

---

Hi [First Name],

When we updated our pricing in [YEAR], we grandfathered your account at your original rate of [$X/month] as a thank-you for being an early customer.

We have kept that commitment for [X months/years]. However, the gap between your rate and our current pricing has grown significantly, and we need to bring all accounts onto a consistent structure.

**Starting [DATE -- 60 days from send]**, your subscription will move to our current [Plan Name] rate of **[$Y/month]**.

Here is what has been added to [Brand Name] since you originally joined at that rate:

- [Major feature added]
- [Major feature added]
- [Major feature added -- list the most significant value additions since their original price]

We deeply appreciate that you have been with us since [approximate year or "the beginning"]. If you would like to discuss this change, or if the new rate creates a genuine hardship for your situation, please reply to this email. We will do what we can.

Thank you for being part of [Brand Name] for so long.

[Signature]

---

## 4. Competitive Pricing Analysis Template

### 4.1 Purpose

Use this template to structure the competitive pricing intelligence gathered during Research Mode. Save the completed template to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/pricing/research/competitive-pricing-analysis-{YYYY-MM-DD}.md` (or `campaigns/{type}-{slug}/pricing/research/` if campaign-tied).

---

### 4.2 Template

```markdown
# Competitive Pricing Analysis: [Brand Name]
Date: {YYYY-MM-DD}
Analyst: [Name or "AI-assisted"]
Sources: Pricing pages scraped via agent-browser, G2 reviews, Wayback Machine

---

## 1. Competitor Overview

| Competitor | Website | Primary Segment | Pricing Model | Value Metric |
|---|---|---|---|---|
| [Name] | [URL] | SMB / Mid / Enterprise | Tiered / Usage / Flat | Per seat / Per contact / etc. |
| [Name] | | | | |
| [Name] | | | | |

---

## 2. Tier-by-Tier Comparison

### 2.1 Entry Tier

| Brand | Tier Name | Monthly Price | Annual Price | Annual Discount | Key Limits | Key Inclusions |
|---|---|---|---|---|---|---|
| [Our Brand] | | | | | | |
| Competitor A | | | | | | |
| Competitor B | | | | | | |
| Competitor C | | | | | | |

### 2.2 Mid Tier (Most Popular)

| Brand | Tier Name | Monthly Price | Annual Price | Annual Discount | Key Limits | Key Inclusions |
|---|---|---|---|---|---|---|
| [Our Brand] | | | | | | |
| Competitor A | | | | | | |
| Competitor B | | | | | | |
| Competitor C | | | | | | |

### 2.3 Top Tier / Enterprise

| Brand | Tier Name | Monthly Price | Annual Price | Custom Pricing? | Key Inclusions | Enterprise Features |
|---|---|---|---|---|---|---|
| [Our Brand] | | | | | | |
| Competitor A | | | | | | |
| Competitor B | | | | | | |
| Competitor C | | | | | | |

---

## 3. Pricing Page Observations

For each competitor, note:

### Competitor A: [Name]

- **Page URL**:
- **Default toggle**: Monthly / Annual
- **Recommended tier**: [Which tier is badged as "Most Popular"]
- **Free trial or freemium**: [Yes/No, details]
- **Credit card required**: [Yes/No]
- **Pricing page conversion elements**: [Trust signals, FAQ, guarantees observed]
- **Value messaging on pricing page**: [Key headlines and subheadlines]
- **Notable features gated at each tier**:
- **What they do well**:
- **What they do poorly**:

### Competitor B: [Name]
[Repeat structure]

### Competitor C: [Name]
[Repeat structure]

---

## 4. Price Positioning Map

Plot all competitors on a 2x2:
- X-axis: Entry price (low to high)
- Y-axis: Feature depth / capabilities (basic to advanced)

```
High Features
      |
      |  [Competitor B]         [Our Brand target?]
      |
      |
      |       [Our Brand now]   [Competitor A]
      |
Low Features
      +------------------------------------------
      Low Price              High Price
```

Narrative: [Where does our brand sit now? Where should it sit? What gap exists?]

---

## 5. Pricing Gaps and Opportunities

**Underserved price points**: [e.g., "No competitor has a strong offering at $49/mo for 3 users -- white space"]

**Overpriced areas**: [e.g., "Competitor A charges $199/mo for features we include at $99/mo -- opportunity to highlight"]

**Feature differentiation**: [Features we have that no competitor prices into -- potential for premium tier justification]

**Value metric opportunity**: [e.g., "All competitors charge per seat; if our product delivers more value per user session, usage-based pricing could differentiate"]

---

## 6. Recommended Price Positioning

Based on competitive analysis:

- **Recommended entry tier price**: $[X]/mo
- **Recommended mid tier price**: $[X]/mo
- **Recommended top tier price**: $[X]/mo or "Contact us"
- **Recommended annual discount**: [X]%
- **Recommended value metric**: [per seat / usage-based / flat]
- **Rationale**: [2-4 sentences connecting the recommendation to the competitive landscape and brand positioning]

---

## 7. Data Confidence

| Data Point | Confidence | Source | Last Verified |
|---|---|---|---|
| Competitor A pricing | High / Medium / Low | Pricing page scraped [date] | {date} |
| Competitor B pricing | | | |
| Customer WTP data | | [Survey / Interviews / None] | |
| Win/loss pricing data | | [CRM / Sales team / None] | |

**Gaps to fill before finalizing pricing**: [List any data that is missing or uncertain]
```

---

## 5. Quick Reference: Pricing Research Method Selection

| Situation | Recommended Method | Time Required | Cost |
|---|---|---|---|
| Need price validation before launch | Van Westendorp PSM | 2-3 weeks (survey + analysis) | $500-$2,000 (incentives + panel) |
| High churn, need to understand why | WTP interviews with churned customers | 2-3 weeks (recruiting + calls) | $500-$1,500 (incentives) |
| Deciding on tier packaging | Conjoint analysis | 4-6 weeks | $2,000-$10,000+ |
| Need competitive price benchmarks | Competitive analysis (Research Mode) | 1-2 days | Free (agent-browser) |
| Enough traffic to test | A/B price test (in-product) | 4-8 weeks for significance | Development time only |
| Quick gut-check, limited budget | WTP interviews (5-7 customers) | 1 week | $250-$700 (incentives) |

---

## 6. Freemium vs Free Trial: Detailed Decision Framework

### 6.1 Decision Matrix

| Factor | Points to Freemium | Points to Free Trial |
|---|---|---|
| Acquisition cost | High CAC -- freemium spreads word organically | Lower CAC -- paid or content acquisition |
| Product virality | Built-in network effects or viral sharing | No natural virality |
| Activation complexity | Simple -- users reach value in minutes | Complex -- requires setup or configuration |
| Value clarity | Value is immediate and obvious | Value becomes clear after sustained use |
| Support cost | Low -- product is self-serve | Higher -- free users may demand support |
| Business model | Volume play, monetize through expansion | Conversion play, quality > quantity |
| Competitor behavior | Competitors have freemium -- table stakes | Competitors use free trials |

### 6.2 Freemium Design Rules

If choosing freemium:
- The free tier must deliver genuine value (not a crippled demo). Users who get value stay; users who do not, churn.
- Gate on the value metric: free users get 100 contacts, 3 projects, 500 API calls -- not 10 days.
- Make the upgrade path visible within the product: trigger upgrade prompts at the limit, not before.
- Track free-to-paid conversion rate. Healthy range: 2-5% for consumer, 5-15% for SMB SaaS.
- Design for viral loops: free users share, invite, embed, or publish -- which drives new signups.

### 6.3 Free Trial Design Rules

If choosing free trial:
- **Length**: 7, 14, or 30 days. Match trial length to time-to-value. If users reach the "aha moment" in 3 days, a 30-day trial delays conversion.
- **Credit card required vs not**: CC required reduces trial starts by ~50% but improves paid conversion by 2-3x. Net result depends on conversion rate and traffic volume. Test both.
- **Trial experience**: Full product access during trial (or access to the "Professional" tier). Crippled trials create negative impressions.
- **Trial email sequence**: Day 0 (welcome), Day 3 (tips to get value fast), Day 7 (key feature highlight), Day 10 (conversion push), Day 13 (urgency / final reminder). See paw-mkt-email skill for sequence design.
- **Expiry behavior**: Trial end should show a clear upgrade screen, not lock users out with no explanation. Show what they accomplished during the trial and what they would lose.

### 6.4 Hybrid Approaches

- **Freemium + time-limited trial of paid features**: Start on free tier, activate a 14-day trial of Pro features automatically, then revert to free. This shows the value of paid before the user decides.
- **Freemium with usage-based monetization**: Free up to a usage limit; pay-as-you-go beyond that. No forced upgrade; just pay for what you use. Works well for developer tools.
