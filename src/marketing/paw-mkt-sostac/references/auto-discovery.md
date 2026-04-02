# Auto-Discovery Reference — Pre-SOSTAC Brand & Competitor Intelligence

## Overview

**Purpose:** Gather all publicly available intelligence about a brand and its competitors BEFORE the SOSTAC interview begins.

This phase reduces the burden on the user — they should not need to explain what is already discoverable through open web research. By completing auto-discovery first, the SOSTAC interview can focus on internal knowledge, strategic intent, and context that only the client can provide.

**Output saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md`

**Session convention:** All browser automation in this phase uses a named session:
```bash
agent-browser --session sostac-discovery-{brand-slug} open {url}
```

> **Setup:** Before running research, check if `agent-browser` is available (`agent-browser --version`). If the command is not found, install it: `npm install -g agent-browser && npx playwright install chromium`. If installation fails, use `WebFetch` and `WebSearch` tools as alternatives for all research tasks in this document.

---

## Section 1: Brand's Own Digital Presence

### 1.1 Homepage Analysis

```bash
agent-browser --session sostac-discovery-{brand-slug} open https://{brand-url} && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/screenshots/homepage.png
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Hero headline and sub-headline
- Primary value proposition statement
- Call-to-action button text (primary and secondary)
- Main navigation structure and menu labels
- Trust signals (customer logos, testimonials, awards, certifications, media mentions)
- Whether a pricing page link is present in navigation
- Footer signals (company size, locations, year founded)

---

### 1.2 Technology Stack Detection

```bash
agent-browser --session sostac-discovery-{brand-slug} open https://www.builtwith.com/{brand-domain} && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- CMS platform (WordPress, Webflow, custom, etc.)
- Analytics platform (GA4, Mixpanel, Heap, Amplitude)
- Marketing automation (HubSpot, Marketo, Klaviyo, ActiveCampaign)
- CRM (Salesforce, HubSpot CRM, Pipedrive)
- A/B testing tools (Optimizely, VWO, Convert)
- CDN provider
- Ad pixels installed (Meta Pixel, Google Ads, LinkedIn Insight, TikTok Pixel)
- Live chat or support tooling (Intercom, Drift, Zendesk)
- Review/ratings widgets

---

### 1.3 Core Web Vitals & Technical Health

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://pagespeed.web.dev/report?url=https://{brand-domain}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} wait 8000
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- LCP (Largest Contentful Paint) — mobile and desktop
- FID / INP (Interaction to Next Paint)
- CLS (Cumulative Layout Shift)
- Overall Performance score (mobile vs desktop)
- Top listed opportunities for improvement
- Diagnostics flagged

---

### 1.4 Pricing Page

```bash
agent-browser --session sostac-discovery-{brand-slug} open https://{brand-url}/pricing && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

Handle 404 gracefully — many brands do not publish pricing publicly. If the page does not exist, note "Pricing not publicly available" and move on.

**Extract:**
- Plan/tier names
- Price points (monthly and annual)
- Feature differentiation between tiers
- Whether a free trial or freemium tier is offered
- Money-back guarantee language
- Whether pricing targets SMB, mid-market, or enterprise
- Contact-for-pricing signals (enterprise gating)

---

### 1.5 Historical Messaging (Wayback Machine)

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://web.archive.org/web/2023*/{brand-url}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} snapshot -i
```

**Extract:**
- How hero messaging has changed year over year
- Previous positioning statements
- Past pricing models (if previously public)
- Rebrand signals (name change, logo change, URL changes)
- Whether messaging has moved up-market or down-market over time

---

## Section 2: Google SERP Research

### 2.1 Brand Name SERP

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.google.com/search?q={brand-name}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Knowledge Graph presence (yes/no, what it shows)
- Sitelinks shown in the SERP
- Review stars / aggregate rating in results
- "People also search for" panel — note all brand names listed
- Any news results in the SERP (signals recent press activity)
- Wikipedia or Crunchbase presence

---

### 2.2 Category Keyword SERP

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.google.com/search?q={main-category-keyword}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Which brands rank on page 1 (positions 1–10)
- Whether the subject brand ranks at all
- Featured snippet presence and which brand owns it
- People Also Ask questions — capture all visible questions verbatim
- Whether Google Ads appear at the top (signals commercial intent and competitive ad spend)
- Shopping results presence
- Review site aggregators appearing (G2, Capterra, Trustpilot listicles)

---

### 2.3 Competitor Discovery Queries

Run all three queries to triangulate the competitive set:

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.google.com/search?q={brand-name}+alternatives" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body

agent-browser --session sostac-discovery-{brand-slug} open "https://www.google.com/search?q={brand-name}+vs" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body

agent-browser --session sostac-discovery-{brand-slug} open "https://www.google.com/search?q=best+{category}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- List every competitor name that appears across all three queries
- Tally frequency — brands mentioned across multiple queries are primary competitors
- Identify the top 3–5 competitors that appear most consistently
- Note any review site listicles (G2, Capterra, Software Advice, GetApp) and what brands they rank

---

### 2.4 Google Trends

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://trends.google.com/trends/explore?q={brand-name},{main-category-keyword}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} wait 3000
agent-browser --session sostac-discovery-{brand-slug} screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/screenshots/google-trends.png
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Overall search volume trend direction (growing / declining / stable)
- Seasonal patterns (peaks and troughs by month)
- Geographic interest breakdown (top regions/countries)
- Breakout related queries (fast-growing search terms)
- Top related queries (established high-volume terms)
- Brand name trend vs category keyword trend (is brand growing faster or slower than category?)

---

## Section 3: Competitor Research

Repeat the following subsections for each of the top 3–5 competitors identified in Section 2.3. Use `{n}` as the competitor index (1, 2, 3...) in file naming.

---

### 3.1 Competitor Homepage

```bash
agent-browser --session sostac-discovery-{brand-slug} open https://{competitor-domain} && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
agent-browser --session sostac-discovery-{brand-slug} screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/screenshots/competitor-{n}-homepage.png
```

**Extract:**
- Primary value proposition and hero headline
- Positioning angle (cheapest / best-in-class / easiest / most enterprise)
- Signals about target audience (who they speak to — size, role, industry)
- Key messages and differentiators they emphasise
- Navigation structure and product naming
- Trust signals and social proof

---

### 3.2 SimilarWeb Traffic Estimate

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.similarweb.com/website/{competitor-domain}/" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} wait 3000
agent-browser --session sostac-discovery-{brand-slug} get text body
```

If SimilarWeb shows "insufficient data" or a traffic paywall, note "Traffic estimate unavailable" and move on.

**Extract:**
- Monthly visits estimate
- Traffic source breakdown: organic search / paid search / direct / social / referral / email
- Bounce rate
- Average visit duration
- Pages per visit
- Top countries by traffic share
- Top referring websites (signals partnership/content strategy)

---

### 3.3 Competitor Pricing

```bash
agent-browser --session sostac-discovery-{brand-slug} open https://{competitor-domain}/pricing && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

Handle 404 gracefully. If no public pricing exists, note "No public pricing."

**Extract:**
- Tier names and price points (monthly and annual)
- Free tier or free trial availability
- Feature gating strategy
- Highest listed price point (enterprise ceiling signal)
- Whether pricing is contact-based at the top tier

---

## Section 4: Ad Intelligence

### 4.1 Meta Ad Library (Facebook/Instagram)

Run for the brand, then repeat for each competitor:

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q={brand-name}&search_type=keyword_unordered" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} wait 3000
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Number of active ads currently running
- Ad formats present (image, video, carousel, lead gen)
- How long ads have been running — long-running ads (90+ days) are proven performers and signal what messaging converts
- Dominant themes in ad copy and creative (offer-led, feature-led, testimonial-led, pain-point-led)
- CTAs used in ads
- Landing page URLs from ads (may differ from homepage — reveals funnel strategy)
- Whether the brand is running ads at all (no ads = no paid social investment, or brand relies on organic)

---

### 4.2 Google Ad Transparency

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://adstransparency.google.com/?region=anywhere&query={brand-name}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} wait 3000
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Whether search or display ads are active
- Ad copy examples — note headlines and descriptions verbatim
- Landing page URLs from ads
- Ad formats used (search text, display banner, video)
- Geographic targeting signals (if visible)

---

## Section 5: Review Mining

### 5.1 G2 Reviews

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.g2.com/search?utf8=✓&query={brand-name}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} snapshot -i
# Click into the first result that matches the brand
agent-browser --session sostac-discovery-{brand-slug} get text body
```

If no G2 listing exists, note "No G2 presence found."

**Extract:**
- Overall star rating and total review count
- Top positive themes from reviews (what users consistently praise = real strengths to amplify)
- Top negative themes from reviews (consistent complaints = weaknesses and competitor opportunity)
- Most-mentioned use cases
- User profile mentions (company size, role, industry) — reveals actual customer profile
- Competitor alternatives mentioned by reviewers
- "What do you like best" and "What do you dislike" common patterns

Repeat for top 3 competitors — their weaknesses are the subject brand's opportunity.

---

### 5.2 Trustpilot

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.trustpilot.com/search?query={brand-name}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} snapshot -i
agent-browser --session sostac-discovery-{brand-slug} get text body
```

If no Trustpilot listing, note "No Trustpilot presence found."

**Extract:**
- TrustScore and star rating
- Total review count
- Review volume trend (growing/declining)
- Common complaint themes in 1–2 star reviews
- Common praise themes in 4–5 star reviews
- Brand response behaviour (do they respond to negative reviews?)

---

### 5.3 App Store / Google Play (if applicable)

Only run if the brand has a mobile application:

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://apps.apple.com/us/search?term={brand-name}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- App rating and review count
- Recent review themes (reflects current product quality)
- Most-mentioned features or bugs
- Update frequency (signals engineering investment)

---

## Section 6: Customer Language Mining

### 6.1 Reddit Research

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.reddit.com/search/?q={brand-name}+OR+{category-keyword}&sort=relevance&t=year" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Questions people ask about the brand or category (capture exact phrasing — this is the language of the market)
- Pain points expressed in natural language
- How people describe the problem they are trying to solve
- Competitor mentions alongside the brand
- Subreddits where the topic appears (signals where the audience congregates)
- Upvoted answers — what advice do peers give? (signals what the market values)
- Negative experiences with the brand (unfiltered complaints surface what review sites miss)

---

### 6.2 Quora Research

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.quora.com/search?q={category-keyword}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

**Extract:**
- Question titles (verbatim) — these are buyer questions at research stage
- How people describe their needs and desired outcomes
- Which answers get most upvotes — what the market considers authoritative
- Competitor comparisons that surface organically
- Objections or concerns expressed about the category

---

### 6.3 People Also Ask (from Google)

Already captured in Section 2.2 — extract the PAA questions as customer language signals.

Cross-reference with Reddit and Quora findings. Questions that appear across multiple sources are high-priority signals for content strategy and messaging alignment.

---

## Section 7: LinkedIn Intelligence

### 7.1 Company Page

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.linkedin.com/company/{brand-linkedin-slug}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

Note: LinkedIn may require login for full data. Extract what is publicly visible.

**Extract:**
- Employee headcount (from LinkedIn company page)
- Employee growth trend (growing fast = scaling; declining = restructuring)
- Industry classification
- Company tagline / About summary
- Recent posts and engagement signals (what content they publish, what resonates)
- Follower count

Repeat for top 3 competitors — compare headcount and growth rates as a proxy for company trajectory.

---

### 7.2 Job Postings as Strategic Signals

```bash
agent-browser --session sostac-discovery-{brand-slug} open "https://www.linkedin.com/jobs/search/?keywords={brand-name}&f_C={company-id}" && agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
```

Job postings are one of the best public signals of strategic direction. Interpret as follows:

**Extract and interpret:**
- Performance marketing / paid media roles being hired → scaling paid acquisition
- Data engineering / analytics engineering roles → first-party data or attribution investment
- Sales development reps in a new geography → geographic expansion
- Customer success managers being hired → retention or churn problem
- Product-led roles (PLG, self-serve) → shifting to product-led growth model
- AI / ML engineering → product AI investment
- Content or SEO roles → organic growth bet
- Partnership / channel roles → indirect distribution strategy

---

## Section 8: Output — Auto-Discovery Brief

After all research completes, synthesise all findings into the output file at:

`./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md`

Use the following template:

```markdown
# Auto-Discovery Brief — {Brand Name}
## Research Date: {YYYY-MM-DD}

---

## Brand Intelligence

### Current Positioning (from homepage)
- Hero headline:
- Value proposition:
- Primary CTA:
- Navigation structure:
- Trust signals:
- Pricing page: [visible / not publicly available]

### Technology Stack
- CMS:
- Analytics:
- Marketing automation:
- CRM:
- A/B testing:
- Ad pixels installed:
- Notable tools:

### Core Web Vitals
| Metric | Mobile | Desktop |
|--------|--------|---------|
| Performance score | | |
| LCP | | |
| INP | | |
| CLS | | |

Top improvement opportunities:

### Pricing Model
- Tiers:
- Price range:
- Free trial: [yes / no]
- Pricing model notes:

### Historical Messaging (Wayback Machine)
- Notable positioning changes:
- Previous messaging:

---

## Competitive Landscape

### Identified Competitors
| # | Brand | Website | Positioning | Pricing | Traffic Est. |
|---|-------|---------|-------------|---------|--------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

### Competitor Messaging Comparison
(Summarise how each competitor positions vs the subject brand — who owns which angle)

---

## Market Intelligence

### Category Search Volume Trend (Google Trends)
- Trend direction:
- Seasonal patterns:
- Geographic concentration:
- Breakout related queries:

### Top Category Keywords (from SERP research)
- Primary keywords:
- People Also Ask questions:
  1.
  2.
  3.
  4.
  5.

### Brand vs Category Trend
(Is brand search growing faster or slower than the category?)

---

## Customer Voice

### Common Pain Points (from reviews + Reddit + Quora)
(Use the customer's own language — direct quotes where possible)

### Common Praise Themes
(What users love about this category — what the market values)

### Competitor Weaknesses Found in Reviews
(Complaints about competitors = opportunity for subject brand)

### Language Customers Use
(Key phrases and terminology used by customers to describe the problem and desired outcome)

---

## Ad Activity

### Brand: {brand-name}
- Meta ads running: [yes — N active ads / no]
- Long-running ads: [describe proven performers if found]
- Google ads running: [yes / no]
- Dominant ad themes:

### Competitor Ad Activity
| Competitor | Meta Ads | Google Ads | Dominant Theme |
|------------|----------|------------|----------------|
| | | | |
| | | | |
| | | | |

---

## LinkedIn Intelligence

### Brand Headcount & Growth
- Employees:
- Growth trend:

### Strategic Signals from Job Postings
(Interpret active job postings as strategic signals)

---

## Key Findings for SOSTAC Interview
(5–8 bullets: the most important insights that will shape the marketing plan)

1.
2.
3.
4.
5.
6.
7.
8.

---

## Gaps — What Auto-Discovery Could Not Find
(What remains unknown and must be asked in the SOSTAC interview)

- [ ]
- [ ]
- [ ]

---

## Sources Checked
| Source | Status | Notes |
|--------|--------|-------|
| Homepage | | |
| BuiltWith | | |
| PageSpeed Insights | | |
| Pricing page | | |
| Wayback Machine | | |
| Google SERP — brand | | |
| Google SERP — category | | |
| Google Trends | | |
| SimilarWeb (competitors) | | |
| Meta Ad Library | | |
| Google Ad Transparency | | |
| G2 | | |
| Trustpilot | | |
| Reddit | | |
| Quora | | |
| LinkedIn | | |
```

---

## Section 9: Graceful Degradation

Many sites block scrapers, require login, or return incomplete data. The discovery phase must never fail entirely because of one blocked source.

**Rules:**
- If a page returns a CAPTCHA or access block: log the block, note in findings under "Sources Checked", and move to the next source immediately
- If a pricing page returns 404: note "Pricing not publicly available" — do not retry
- If no G2 or Capterra listing exists: note "No review platform presence found"
- If SimilarWeb shows "insufficient data" or traffic data is paywalled: note "Traffic estimate unavailable"
- If LinkedIn requires login to see full data: extract whatever is publicly visible without logging in
- If Reddit returns no results: try again with category keyword only (remove brand name)
- If Wayback Machine returns no snapshots: note "No historical snapshots available"
- If a site loads but returns very little text (likely JS-rendered): try `agent-browser snapshot -i` to capture the visual state, then note "Limited text extraction — JS-rendered page"
- Never halt the entire discovery run for a single blocked source
- Always compile partial findings — partial intelligence is far more valuable than no intelligence

**Error log format:**
```
[BLOCKED] {source} — {reason} — skipped, continuing
[404] {url} — page not found — noted in output
[CAPTCHA] {source} — access blocked — noted in output
[INSUFFICIENT_DATA] {source} — data unavailable at this traffic level
```

---

## Section 10: Session Management

All discovery research for a brand runs within a single named browser session. This maintains cookies, avoids repeated cold starts, and groups all activity logically.

**Open session at start:**
```bash
agent-browser --session sostac-discovery-{brand-slug} open https://{brand-url}
```

**All subsequent commands in the same session:**
```bash
agent-browser --session sostac-discovery-{brand-slug} open {next-url}
agent-browser --session sostac-discovery-{brand-slug} wait --load networkidle
agent-browser --session sostac-discovery-{brand-slug} get text body
agent-browser --session sostac-discovery-{brand-slug} screenshot {path}
agent-browser --session sostac-discovery-{brand-slug} snapshot -i
```

**Close session on completion:**
```bash
agent-browser --session sostac-discovery-{brand-slug} close
```

**Session naming convention:** `sostac-discovery-{brand-slug}`

Example: for `pawbytes.com`, the slug is `pawbytes`, so the session is `sostac-discovery-pawbytes`.

The brand slug is derived from the brand name: lowercase, spaces replaced with hyphens, special characters removed.

---

## Execution Order

Run sections in this sequence to build context progressively. Competitor names discovered in Section 2 feed into Sections 3, 4, and 5.

```
1. Open session
2. Section 1 — Brand's own digital presence (homepage, tech stack, vitals, pricing, history)
3. Section 2 — Google SERP research (brand SERP, category SERP, competitor queries, Trends)
   → At this point: confirm the top 3–5 competitors to research
4. Section 3 — Competitor research (homepage + SimilarWeb + pricing for each)
5. Section 4 — Ad intelligence (Meta Ad Library + Google Ads Transparency for brand + competitors)
6. Section 5 — Review mining (G2 + Trustpilot + App Store for brand + competitors)
7. Section 6 — Customer language mining (Reddit + Quora + PAA cross-reference)
8. Section 7 — LinkedIn intelligence (company page + job postings for brand + competitors)
9. Section 8 — Synthesise all findings into 00-auto-discovery.md
10. Close session
```

Total estimated run time: 15–40 minutes depending on the number of competitors and how many sources respond without blocking.
