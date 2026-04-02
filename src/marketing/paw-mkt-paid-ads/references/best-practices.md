# Paid Advertising Best Practices -- Modern and Emerging Practices

Comprehensive reference for modern paid advertising across all major platforms. Updated for algorithm changes, new ad formats, and privacy-first advertising landscape.

---

## 1. Google Ads Best Practices

### 1.1 Performance Max (PMax) Campaigns

Performance Max is Google's flagship AI-driven campaign type, running across Search, Display, YouTube, Discover, Gmail, and Maps from a single campaign.

**Asset requirements for strong performance:**
- 20+ high-quality images (landscape 1200x628, square 1200x1200, portrait 960x1200)
- 5+ video assets (horizontal, vertical, square; 10s, 15s, 30s+ lengths)
- 15 headlines (30 char max each): mix of keyword-rich, benefit-driven, CTA, social proof, and urgency variants
- 5 long headlines (90 char max): more descriptive, benefit-focused
- 5 descriptions (90 char max): elaborate on unique value propositions
- Business name and logo (1200x1200 square, 1200x300 landscape)
- Final URL and display path

**Asset group strategy:**
- Create separate asset groups per product line, service category, or audience segment
- Never combine unrelated products in a single asset group
- Each asset group should have its own audience signals, assets, and final URL
- Monitor asset performance ratings (Low, Good, Best) and replace Low-rated assets within 14 days

**Audience signals (critical for PMax guidance):**
- Custom segments: Add 10-15 high-intent search terms competitors' URLs and apps your audience uses
- Your data: Upload customer match lists segmented by value tier (top 20% customers as primary signal)
- Interests and demographics: Layer in-market and affinity audiences relevant to your product
- Audience signals are suggestions, not restrictions -- the algorithm will explore beyond them

**PMax pitfalls to avoid:**
- Brand cannibalization: PMax will claim brand search conversions. Add brand exclusions at the campaign level via Google rep or API
- Placement quality: Use account-level placement exclusions. Run placement reports via Google Ads scripts to identify MFA sites and mobile apps consuming budget
- URL expansion: Disable if you want traffic only on specific landing pages. Enable only if all site pages are conversion-optimized
- New customer acquisition: Enable the "new customer value" setting and assign a value premium to new customers to bias the algorithm toward prospecting

### 1.2 Broad Match + Smart Bidding

Broad match has fundamentally changed. Combined with smart bidding, it uses real-time signals (location, device, time, query context, audience lists) to determine which queries to enter.

**When to use broad match:**
- Campaign has 30+ conversions per month (ideally 50+)
- Smart bidding strategy is active (tCPA, tROAS, or maximize conversions/value)
- Strong negative keyword lists are in place
- Conversion tracking is accurate and comprehensive

**Implementation approach:**
- Do not flip all keywords to broad match overnight
- Start with top 5-10 highest-volume exact/phrase keywords, duplicate them as broad match in a separate ad group or experiment
- Run for 14-21 days comparing CPA/ROAS between match types
- Review search terms report twice weekly during the test
- Expand broad match adoption to remaining keywords once validated

**Negative keyword management for broad match:**
- Maintain account-level negative keyword lists (up to 1000 terms)
- Create campaign-level lists for campaign-specific exclusions
- Review search terms daily during the first 2 weeks of broad match adoption
- Common exclusion categories: job-related (salary, hiring, careers), informational (what is, how to, definition), competitor brand names (unless running competitor campaigns), free/cheap (for premium brands)

### 1.3 Responsive Search Ads (RSAs)

RSAs are the only standard search ad format. Google tests combinations of your headlines and descriptions to find the best performers.

**Headline strategy (15 available slots):**
- Headlines 1-3: Primary keyword variations (pinned to position 1 or 2 if needed)
- Headlines 4-6: Benefit statements (save time, increase revenue, reduce costs)
- Headlines 7-9: Social proof (trusted by X customers, rated 4.8 stars, award-winning)
- Headlines 10-12: CTAs (Get Started Today, Free Trial, Request a Demo, Shop Now)
- Headlines 13-15: Urgency/scarcity (Limited Time, Ends Friday, Only X Left)

**Description strategy (4 available slots):**
- Description 1: Core value proposition with primary keyword
- Description 2: Supporting benefit with differentiator
- Description 3: Social proof or trust signal
- Description 4: CTA with urgency element

**Pinning guidelines:**
- Pin sparingly -- every pin reduces Google's optimization ability
- Pin only when brand compliance requires specific messaging in position 1
- If pinning, pin 2-3 headlines to the same position to allow some rotation
- Never pin all positions -- defeats the purpose of RSAs

**Ad strength indicator:**
- Target "Good" or "Excellent" ad strength
- Add more unique headlines to improve (avoid repetitive messaging)
- Use all 15 headline slots and all 4 description slots
- Include keywords naturally without keyword stuffing

### 1.4 Demand Gen Campaigns

Demand Gen replaced Discovery campaigns and runs across YouTube (in-feed, in-stream, Shorts), Discover feed, and Gmail.

**Best practices:**
- Provide both image and video assets for maximum reach
- Use high-quality lifestyle imagery (not product-on-white-background)
- Video assets: include 6s bumpers, 15s shorts, and 30-60s longer cuts
- Audience targeting: use lookalike segments seeded from converters (not all site visitors)
- Bidding: start with maximize clicks to build data, graduate to maximize conversions or tCPA after 50 conversions
- Creative refresh every 3-4 weeks to prevent fatigue

### 1.5 YouTube Ads (including Shorts and CTV)

**YouTube Shorts Ads (2025-2026 priority format):**
- Vertical 9:16 format, under 60 seconds
- Native creator-style content outperforms polished brand ads
- Hook within first 1-2 seconds (Shorts audience scrolls fast)
- Text overlays for key messages (many viewers watch without sound)
- Add clear CTA overlay and end card
- Can run via Video Action campaigns or Demand Gen

**Connected TV (CTV) via YouTube:**
- Non-skippable 15s and 30s in-stream on YouTube CTV apps
- Massive reach: YouTube is the #1 streaming platform on connected TVs
- Target by household demographics, content interests, and custom segments
- Creative must work on large screen -- high production value, readable text, strong audio
- Measure via brand lift studies, search lift, and conversion path analysis

**In-Stream skippable best practices:**
- Brand visible by second 3 (before skip button appears at second 5)
- Deliver core message within first 15 seconds
- Include CTA both verbally and as on-screen element at 15s and 30s marks
- Optimal length: 15-60 seconds (30s sweet spot for most objectives)
- Add companion banners for additional real estate

### 1.6 Conversion Tracking

**Enhanced Conversions:**
- Sends hashed first-party customer data (email, phone, name, address) alongside conversion tags
- Improves conversion attribution accuracy by 5-15%
- Implemented via Google Tag or GTM with user-provided data variables
- Requires customer consent under applicable privacy laws
- Enable in Google Ads settings under Conversions > Settings > Enhanced Conversions

**Consent Mode v2 (mandatory in EEA/UK):**
- Two required parameters: ad_storage and analytics_storage
- Two new parameters added in v2: ad_user_data and ad_personalization
- Default state should be "denied" until user grants consent
- When consent is denied, Google models conversions using aggregated anonymized data
- Implement via CMP (Consent Management Platform) integrated with Google Tag
- Non-compliance risks: loss of remarketing audiences, conversion modeling, and personalization in EEA

**Offline conversion tracking:**
- Import CRM conversion data via Google Click ID (GCLID)
- Upload scheduled imports daily or use API for real-time
- Critical for B2B where sales cycles are long and conversions happen offline
- Enhanced conversions for leads: pass hashed lead data at form submission, match to downstream conversion

---

## 2. Meta Ads Best Practices

### 2.1 Advantage+ Shopping Campaigns (ASC)

Meta's most automated campaign type for e-commerce advertisers.

**Setup requirements:**
- Active Meta Pixel with purchase events firing consistently
- Product catalog with 150+ items (works with fewer, but algorithm needs variety)
- Minimum 100 purchases in the past 28 days for optimal performance
- CAPI (Conversions API) sending redundant server-side events

**Optimization approach:**
- Set "existing customer budget cap" to limit spend on retargeting (typically 20-30%)
- Upload existing customer lists so Meta can identify and cap spend on them
- Provide 10+ creative assets mixing formats (static, video, carousel, UGC)
- Allow 7 days of learning before evaluating performance
- Scale budget by 20% every 3-5 days, not more

**When ASC is NOT the right choice:**
- Fewer than 50 purchases/month (insufficient data for algorithm optimization)
- Highly seasonal products requiring precise audience control
- B2B with long sales cycles and low conversion volume
- When you need granular audience testing and isolation

### 2.2 Creative Diversification Strategy

Meta's algorithm performs best when given creative variety. The platform's AI matches different creatives to different audience segments automatically.

**The 3-5-3 framework:**
- 3-5 distinct creative concepts (different hooks, angles, or value propositions)
- 3+ formats per concept (static image, video, carousel, UGC, collection)
- 3 copy variations per ad (different lengths and tones)

**Creative concept categories:**
- Problem/solution: Lead with the pain point, present your product as the fix
- Social proof: Customer testimonials, reviews, before/after, case studies
- Product demo: Show the product in action, unboxing, features walkthrough
- Lifestyle: Aspirational content showing life with the product
- Offer-led: Discount, bundle, limited-time, free shipping emphasis
- Creator/UGC: Authentic, face-to-camera, "I tried this product" format

**Creative fatigue signals:**
- CTR drops 20%+ from peak over 7 days
- CPM increases 30%+ without audience changes
- Frequency exceeds 3.0 in prospecting or 6.0 in retargeting
- ROAS declines 25%+ week-over-week with stable budgets
- Action: pause fatigued ads, introduce new creative, rotate angles

### 2.3 Account Simplification

Meta's algorithm works best with consolidated campaign structures that maximize data density per ad set.

**Simplified structure guidelines:**
- 2-4 campaigns per objective (not dozens of micro-campaigns)
- Use CBO (Campaign Budget Optimization) as default for 3+ ad sets
- Consolidate overlapping audiences rather than running separate narrow ad sets
- Minimum 50 conversions per week per ad set for optimal algorithm learning
- Fewer, broader ad sets outperform many narrow ones in 2025-2026

**Audience consolidation approach:**
- Merge interests into single "stacked" interest ad sets rather than one-interest-per-ad-set
- Use Advantage+ Audience (expanded targeting) for prospecting -- provide audience suggestions as signals
- Separate only when audiences truly need different messaging (e.g., B2B vs B2C, different languages)

### 2.4 Meta Conversions API (CAPI)

Server-side event tracking that sends conversion data directly from your server to Meta, bypassing browser limitations.

**Implementation priority (high to low):**
1. Purchase / Lead (primary conversion events)
2. InitiateCheckout / AddToCart (mid-funnel)
3. ViewContent / AddToWishlist (upper-funnel)
4. PageView (base-level)

**Technical requirements:**
- Deduplicate events using event_id parameter (prevent double-counting with pixel)
- Event match quality (EMQ) score target: 6.0+ (higher = better match rate)
- Pass user parameters: email (hashed), phone (hashed), first name, last name, city, state, zip, country, external ID
- Use partner integrations for simplified setup: Shopify, WooCommerce, WordPress, Zapier, or GTM server-side

**Impact of CAPI:**
- Recovers 10-25% of conversion events lost due to browser restrictions, ad blockers, and iOS ATT
- Improves audience building accuracy for custom audiences and lookalikes
- Better optimization data leads to lower CPA and higher ROAS over time

### 2.5 Reels Placements

Reels inventory continues to grow as Meta's fastest-growing ad surface.

**Creative specifications:**
- 9:16 vertical format (1080x1920)
- 5-30 seconds optimal (15s is the sweet spot)
- Safe zones: keep text and key visuals within center 80% (top/bottom contain UI overlays)
- Audio is expected: use music, voiceover, or trending sounds
- Captions/subtitles still needed for accessibility

**Performance patterns:**
- UGC and creator-style content achieves 2-3x higher engagement than polished brand ads
- Hook in first 1-2 seconds is critical (thumb-stopping visual or statement)
- Reels-first creative outperforms repurposed feed ads by 30-50% in Reels placement
- Fastest creative fatigue of any placement: refresh every 7-10 days

---

## 3. TikTok Ads Best Practices

### 3.1 Smart Performance Campaigns (SPC)

TikTok's most automated campaign type, similar to Meta's Advantage+ and Google's PMax.

**How SPC works:**
- Minimal targeting inputs: provide country, budget, optimization goal, and creative
- Algorithm handles audience finding, bid optimization, and placement
- Best for advertisers with strong conversion data and high creative volume

**When to use SPC:**
- 50+ conversions per week on TikTok pixel
- Proven creative assets (test in standard campaigns first)
- Scaling phase when manual targeting has been validated

### 3.2 TikTok Shop Ads

Shoppable ads integrated with TikTok's in-app commerce platform.

**Ad formats:**
- Video Shopping Ads: shoppable product cards overlaid on video content
- LIVE Shopping Ads: promote live shopping events to targeted audiences
- Product Shopping Ads: catalog-based ads similar to dynamic product ads
- Creator affiliate: partner with TikTok creators who earn commission on sales

**Best practices:**
- In-app checkout reduces friction dramatically compared to external landing pages
- Product feed quality matters: clear images, accurate titles, competitive pricing
- Creator content driving to TikTok Shop outperforms brand-produced content
- Combine organic TikTok Shop presence with paid amplification via Spark Ads

### 3.3 Spark Ads

Spark Ads allow brands to boost organic TikTok posts (their own or a creator's) as paid ads while retaining all social proof.

**Advantages:**
- Higher engagement rates vs standard in-feed ads (social proof effect)
- Retains likes, comments, shares, and view counts from organic performance
- Creator authorization via unique code (no need for Business Center access)
- Combine with landing page link or TikTok Shop product page

**Creator partnership framework:**
- Brief creators with product samples and 3-5 key talking points (not scripts)
- Request 3+ content variations per creator
- Test creator content as Spark Ads with small budgets ($20-50/day per creative)
- Scale winners to $100-500/day based on CPA performance
- Negotiate usage rights for 60-90 days minimum

### 3.4 Creative Best Practices for TikTok

**The hook (first 1-3 seconds) is everything:**
- Bold opening statement: "Stop scrolling if you..."
- Visual pattern interrupt: unexpected visual, fast movement, color contrast
- Question that creates curiosity gap
- Before/after reveal tease
- "POV" or "Things I wish I knew" format

**Native feel principles:**
- Shot on phone (or made to look like it)
- Natural lighting, real environments
- Conversational tone, not "advertising voice"
- Creator/face-to-camera increases trust
- Show product in use within first 3 seconds
- Trending sounds boost distribution (check TikTok Creative Center for trends)

**Creative refresh cadence:**
- New creative every 7-14 days (TikTok creative fatigue is the fastest of any platform)
- Maintain 3-5 active creatives per ad group at all times
- Kill underperformers within 3-5 days if CPA is 2x+ target
- Repurpose winning hooks with new body content for extended life

### 3.5 TikTok Search Ads

TikTok Search Ads appear in TikTok search results, capturing high-intent users who are actively searching for products, reviews, and recommendations.

**Key details:**
- Keyword-targeted ad placements in TikTok search results
- Toggle on "Search Ads" within existing in-feed campaigns
- High intent signal: users searching on TikTok have purchase intent similar to Google
- Creative should answer the search query directly (not just brand awareness content)
- Monitor search term reports and add negative keywords for irrelevant queries

---

## 4. LinkedIn Ads Best Practices

### 4.1 Document Ads

Native document ads allow users to swipe through PDF-style content directly in the LinkedIn feed.

**Best practices:**
- 5-10 pages optimal (enough value, not overwhelming)
- First page is the hook: bold headline, clear value proposition
- Each page should deliver standalone value (users may not swipe through all)
- Gate the document behind a Lead Gen Form after 3-5 pages for lead capture
- Content types that work: industry reports, how-to guides, benchmark data, frameworks, checklists
- Design for mobile: large text (16pt+), simple layouts, high-contrast colors

### 4.2 Thought Leader Ads

Promote posts from individual employees' personal LinkedIn profiles as sponsored content.

**Why they work:**
- 2-3x higher CTR than standard company page sponsored content
- Personal posts feel authentic and trustworthy in the LinkedIn feed
- Great for executive positioning, culture showcase, and expertise demonstration
- Available for single-image, video, and text-only post formats

**Implementation:**
- Employee must be a verified page admin or their post must be selected in Campaign Manager
- Original post remains on the individual's profile (boosts their personal brand too)
- Best for C-suite, subject matter experts, and customer-facing team members
- Combine with Lead Gen Forms for direct lead capture

### 4.3 B2B Targeting Precision

**High-value targeting combinations:**
- Job function + seniority level (e.g., Marketing + Director and above)
- Company size + industry (e.g., 200-500 employees + SaaS)
- Skills + job title (e.g., "Salesforce" skill + "Revenue Operations" title)
- Member groups (niche professional communities)

**ABM (Account-Based Marketing) approach:**
- Upload target account list (CSV with company names and domains)
- Create matched audience, then layer job function and seniority
- Minimum audience size: 300+ matched members for delivery
- Run awareness campaigns (Thought Leader Ads, Document Ads) 2-4 weeks before lead gen

### 4.4 Revenue Attribution for Long B2B Sales Cycles

**Challenge:** B2B sales cycles are 3-12 months. Platform attribution windows (90 days max) miss most downstream revenue.

**Solutions:**
- Pass LinkedIn Click ID (li_fat_id) to CRM via hidden form fields
- Match CRM closed-won deals back to LinkedIn campaigns manually or via integration
- Use LinkedIn Revenue Attribution Report (connects to CRM data)
- Implement MMM (Marketing Mix Modeling) for holistic channel contribution
- Track leading indicators: MQL rate, SQL rate, pipeline value generated, not just last-click leads

---

## 5. Programmatic Best Practices

### 5.1 Connected TV (CTV) Advertising

CTV is the fastest-growing programmatic channel, reaching cord-cutters on streaming platforms.

**Inventory sources:**
- Premium streaming: Hulu, Peacock, Paramount+, Max (ad-supported tiers), Tubi, Pluto TV, Roku Channel
- YouTube CTV: largest CTV reach via YouTube app on smart TVs
- Programmatic via DSPs: The Trade Desk, DV360, Amazon DSP

**Creative specifications:**
- 15-second and 30-second non-skippable spots
- 16:9 horizontal format, 1920x1080 minimum resolution
- High production value required (big-screen viewing context)
- Audio is critical: CTV is a lean-back, sound-on experience
- Include clear branding throughout (not just end card)
- Add QR codes for direct response campaigns (scannable on phone while watching TV)

**Measurement:**
- Brand lift studies (awareness, consideration, purchase intent)
- Search lift: measure increase in branded search queries post-CTV exposure
- Website visit lift: compare exposed vs control household visit rates
- Cross-device retargeting: serve display/social ads to CTV-exposed households

### 5.2 Retail Media Networks (RMN)

Retail media is advertising on retailer-owned properties using first-party purchase data.

**Major networks (2025-2026):**
- Amazon Ads: Sponsored Products, Sponsored Brands, Sponsored Display, Amazon DSP
- Walmart Connect: on-site search ads, display, and off-site programmatic
- Target Roundel (Roundel by Target): on-site and off-site, strong audience data
- Kroger Precision Marketing: grocery-specific purchase data
- Instacart Ads: CPG and grocery brands
- Best Buy Ads, Home Depot, Ulta Beauty, and more launching or expanding

**Why RMNs matter:**
- First-party purchase data enables closed-loop attribution (ad exposure to purchase)
- Advertising at point of purchase captures high-intent shoppers
- Privacy-safe: based on retailer first-party data, not third-party cookies
- Critical for CPG, food/beverage, electronics, beauty, and home goods brands

### 5.3 Contextual Targeting (Post-Cookie)

With third-party cookie deprecation (Google maintaining cookies but with user controls and Privacy Sandbox), contextual targeting has re-emerged as a privacy-safe alternative.

**Modern contextual capabilities:**
- AI-powered page content analysis (not just keyword matching)
- Sentiment analysis: understand the emotional tone of content surrounding ads
- Image and video content recognition: match ads to visual page content
- Custom contextual segments: define category combinations relevant to your brand
- Predictive contextual: correlate content categories with conversion likelihood

**Best practices:**
- Layer contextual with first-party data for the strongest results
- Use inclusion lists (curated publisher lists) alongside contextual targeting
- Test contextual segments against behavioral segments to compare performance
- Exclude sensitive content categories (violence, politics, misinformation)
- Monitor brand safety with third-party verification (IAS, DoubleVerify)

---

## 6. Cross-Platform Best Practices

### 6.1 Creative Production Pipeline

To sustain paid ads across multiple platforms, establish a content production system.

**Monthly creative production targets by spend level:**
- Under $5K/month: 5-10 new creatives/month (1-2 concepts, multiple formats)
- $5K-$25K/month: 15-25 new creatives/month (3-4 concepts, multiple formats)
- $25K-$100K/month: 30-50 new creatives/month (5-8 concepts, multiple formats and iterations)
- $100K+/month: 50-100+ new creatives/month (dedicated creative team or agency)

### 6.2 Landing Page Alignment

Paid ads are only as good as the landing page they drive to.

**Landing page essentials:**
- Message match: headline on landing page mirrors ad headline
- Single CTA (do not distract with navigation or multiple offers)
- Load time under 3 seconds on mobile
- Above-the-fold: headline, value prop, CTA, hero image/video
- Social proof: testimonials, logos, ratings, case study snippets
- Mobile-first design: 70%+ of paid social traffic is mobile

### 6.3 Budget Reallocation Signals

**Scale up a campaign when:**
- CPA is 20%+ below target for 7+ consecutive days
- ROAS is 20%+ above target consistently
- Impression share is below 70% (search) -- budget is limiting reach
- Creative is still performing (CTR stable, frequency below threshold)

**Scale down or pause when:**
- CPA exceeds target by 30%+ for 5+ consecutive days after learning period
- Frequency exceeds 3.0 in prospecting or 8.0 in retargeting
- CTR has declined 40%+ from peak (creative fatigue confirmed)
- Zero conversions after spending 3x the target CPA amount

---

## 7. Emerging Trends

### 7.1 AI-Generated Creative at Scale
- Google and Meta both offer AI-generated ad creative (image generation, text suggestions)
- Use AI-generated variants as a starting point, then refine with brand-specific elements
- Test AI-generated vs human-created creative head-to-head

### 7.2 First-Party Data Monetization
- Brands building owned data assets (email lists, app users, loyalty programs) gain targeting advantages
- Customer match audiences on Google, Meta, and TikTok are increasingly important as third-party signals degrade
- Data clean rooms enable privacy-safe collaboration between brands and publishers

### 7.3 Incrementality Measurement
- Move beyond last-click attribution to understand true ad impact
- Conversion lift studies (available on Google and Meta) measure incremental conversions
- Geo-holdout tests: run ads in test markets, withhold in control markets, compare
- Marketing mix modeling (MMM) for budget allocation across all channels

### 7.4 Cross-Channel Frequency Management
- Use DSPs with cross-channel reach to manage how often a user sees your ads across platforms
- Over-frequency is the top driver of ad fatigue and brand annoyance
- Target 4-8 total exposures per user per week across all platforms combined

### 7.5 Automation and Feed-Based Advertising
- Product feed quality is the new competitive advantage (titles, descriptions, images, attributes)
- Feed management tools (Feedonomics, DataFeedWatch, Channable) enable multi-platform feed optimization
- Automated rules and scripts reduce manual optimization work: implement pause rules, bid adjustments, and alerts
