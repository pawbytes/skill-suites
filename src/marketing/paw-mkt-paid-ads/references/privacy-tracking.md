# Privacy, Tracking & Attribution (2025-2026)

**Purpose:** Reference for privacy-compliant tracking setup, server-side tracking, attribution models, and the post-cookie landscape.

---

## 1. Third-Party Cookie Deprecation

### Current Status (2025-2026)
- **Chrome**: Google has delayed and modified its approach multiple times. As of 2025, Chrome is implementing a user-choice model where users opt in/out of third-party cookies rather than a blanket deprecation. Regardless, the trajectory is clear: third-party cookie reliance is declining.
- **Safari**: Third-party cookies blocked since 2020 (ITP). ~20% of web traffic.
- **Firefox**: Third-party cookies blocked since 2023 (ETP). ~3-4% of web traffic.
- **Impact**: Roughly 40-50% of web users already have third-party cookies blocked or restricted.

### Practical Impact on Paid Ads
| Area | Impact | Mitigation |
|------|--------|-----------|
| Remarketing audiences | Shrinking audience pools (30-40% smaller) | First-party data, customer lists, server-side tracking |
| Conversion tracking | Under-reporting (15-30% of conversions missed) | Server-side tracking, enhanced conversions, conversion APIs |
| Lookalike audiences | Reduced seed data quality | Larger seed audiences, first-party data enrichment |
| Cross-device tracking | Less reliable | Logged-in user data, probabilistic matching |
| Attribution | Last-click over-credited, display/social under-credited | Multi-touch attribution, incrementality testing, MMM |

---

## 2. Server-Side Tracking

### Google Tag Manager Server-Side (sGTM)
- **What**: A server-side container that processes tags on your server instead of the user's browser
- **Benefits**: Bypasses ad blockers (15-30% of users), improves page speed (fewer client-side scripts), better data quality, privacy-compliant (you control data before sending to platforms)
- **Setup requirements**: Cloud hosting (Google Cloud Run recommended), domain mapping (e.g., `track.yourdomain.com`), client-side GTM sends to server container, server container routes to Google Ads, GA4, Meta, etc.
- **Cost**: $50-200/month for hosting depending on traffic volume
- **Data recovery**: Typically recovers 10-20% additional conversion data vs client-side only

### Meta Conversion API (CAPI)
- **What**: Server-to-server event tracking, independent of browser
- **Implementation options**:
  - Partner integrations (Shopify, WooCommerce, WordPress plugins) — easiest
  - Google Tag Manager server-side — moderate complexity, most flexible
  - Direct API — most control, requires development resources
- **Event deduplication**: Critical. Use `event_id` parameter matching between pixel and CAPI events to prevent double-counting.
- **Event Match Quality (EMQ)**: Target score of 6.0+. Send hashed email, phone, first name, last name, city, state, zip, country with events.
- **Impact**: Recovers 15-30% of conversions lost to browser restrictions and ad blockers

### TikTok Events API
- Similar concept to Meta CAPI — server-side event tracking
- **Implementation**: Via TikTok partner integrations or direct API
- **Recommended events**: ViewContent, AddToCart, InitiateCheckout, CompletePayment, SubmitForm

### Google Enhanced Conversions
- **What**: Hashes first-party customer data (email, phone, address) and sends to Google for improved conversion matching
- **Two types**:
  - Enhanced Conversions for Web: Matches website conversions to Google users
  - Enhanced Conversions for Leads: Matches offline conversions (CRM) to Google ad clicks
- **Implementation**: Via GTM tag, Google tag (gtag.js), or Google Ads API
- **Impact**: Recovers 5-15% additional conversions

---

## 3. Google Consent Mode v2

### What It Is
A framework that adjusts Google tag behavior based on user consent status. Required for advertisers targeting EEA users to continue using audience features.

### Two New Parameters (Added 2024)
| Parameter | What It Controls | Impact If Denied |
|-----------|-----------------|-----------------|
| `ad_user_data` | Whether user data can be sent to Google for ad purposes | No remarketing, no customer match |
| `ad_personalization` | Whether personalized ads can be shown | No remarketing ads, no dynamic ads |
| `analytics_storage` | GA4 cookie setting | Modeled data instead of observed |
| `ad_storage` | Google Ads cookie setting | Modeled conversions instead of observed |

### Implementation
1. Choose a Google-certified Consent Management Platform (CMP): Cookiebot, OneTrust, Usercentrics, Iubenda
2. Install CMP on website
3. Configure GTM tags to respect consent signals
4. Set default consent state (denied for EEA visitors, granted for others — depends on legal advice)
5. Enable Consent Mode in GTM container settings
6. **Advanced mode** (recommended): Tags fire in restricted mode when consent denied — Google still models conversions using aggregate data. Basic mode blocks tags entirely.

### Modeled Data
When users deny consent, Google uses machine learning to model the conversions and behavior that would have occurred. Typically 60-80% accuracy compared to observed data. Accept that some measurement uncertainty is permanent in the privacy era.

---

## 4. iOS App Tracking Transparency (ATT)

### Impact (Since iOS 14.5, 2021)
- ~75-80% of iOS users opt out of tracking
- iOS represents ~27% of global mobile, ~55% in US
- Meta Ads most impacted: estimated 15-30% revenue impact for advertisers

### Current Workarounds
| Solution | What It Does | Effectiveness |
|----------|-------------|---------------|
| Meta CAPI | Server-side tracking bypasses some ATT limitations | Recovers 15-30% of conversions |
| Aggregated Event Measurement (AEM) | Meta's privacy-safe conversion tracking | Limited to 8 events per domain |
| SKAdNetwork (SKAN) | Apple's privacy-safe attribution for app installs | Limited, delayed, aggregated data |
| Broad targeting | Let Meta's algorithm find users without relying on pixel data | Often outperforms narrow targeting post-ATT |
| Creative testing | Better creative compensates for targeting loss | Most effective long-term strategy |
| First-party data | Customer lists, email-based audiences | Not impacted by ATT |

---

## 5. Attribution Models

### Model Comparison
| Model | How It Works | Best For | Limitation |
|-------|-------------|---------|-----------|
| Last-click | 100% credit to final touchpoint | Direct response, bottom-funnel optimization | Ignores awareness and consideration |
| First-click | 100% credit to first touchpoint | Understanding acquisition sources | Ignores nurturing and conversion |
| Linear | Equal credit to all touchpoints | Simple multi-touch understanding | Treats all touches equally |
| Time-decay | More credit to recent touchpoints | Long consideration cycles (B2B) | Undervalues awareness |
| Position-based (U-shaped) | 40% first, 40% last, 20% middle | Balanced view of acquisition + conversion | Arbitrary weight distribution |
| Data-driven (Google) | ML-based credit assignment | Large accounts (300+ conv/month) | Black box, Google-ecosystem only |
| W-shaped | 30% first, 30% lead creation, 30% last, 10% middle | B2B with clear lead stages | Complex to implement |

### Incrementality Testing
The gold standard for understanding true causal impact of marketing spend.

**Methods:**
- **Geographic holdout**: Run ads in some regions, not others. Compare performance.
- **Ghost ads / PSA test**: Show a public service ad instead of your ad to a control group. Compare conversion rates.
- **Conversion lift studies**: Platform-native (Meta, Google offer these). Randomized control trial within the platform.
- **Budget on/off testing**: Turn a channel off for 2-4 weeks, measure impact on overall conversions.

**When to use**: Annually for major channels, or when considering significant budget changes.

### Marketing Mix Modeling (MMM)
- **What**: Statistical analysis of how each marketing channel contributes to business outcomes
- **Data needed**: 2+ years of weekly spend and results data by channel, plus external factors (seasonality, promotions, competitor activity)
- **Tools**: Google Meridian (open-source), Meta Robyn (open-source), custom R/Python models, agency-built models
- **Best for**: Budget allocation decisions across channels, understanding offline media impact
- **Limitation**: Requires significant data, statistical expertise, and doesn't help with real-time optimization

---

## 6. First-Party Data Strategies

### Building First-Party Audiences
| Data Source | How to Collect | Use in Paid Ads |
|------------|---------------|----------------|
| Email list | Opt-in forms, lead magnets, purchase | Customer match audiences, seed for lookalikes |
| Purchase data | Ecommerce transactions, CRM | High-value customer segments, RFM-based audiences |
| Website behavior | GA4 events, scroll depth, content engagement | Custom audiences based on engagement signals |
| App data | In-app events, feature usage | App-based custom audiences |
| Survey/quiz data | Interactive content, preference centers | Zero-party data for segmentation |
| CRM data | Lead scoring, deal stage, customer attributes | Offline conversion import, lead-value optimization |

### Customer Data Platform (CDP)
- **What**: Unified customer database that connects data from all sources (website, email, CRM, support, product)
- **When needed**: When you have 3+ data sources, 10,000+ customers, and attribution is a priority
- **Options**: Segment (developer-friendly), mParticle, Tealium, Rudderstack (open-source), Bloomreach
- **Budget alternative**: GA4 + BigQuery export + CRM integration covers basic needs

---

## 7. Privacy Sandbox APIs (Chrome)

### Topics API
- **Replaces**: Third-party cookie-based interest targeting
- **How it works**: Browser assigns users to interest categories (topics) based on browsing history. Advertisers target topics, not individual users.
- **Status**: Available in Chrome, adoption by ad platforms is gradual
- **Impact**: Broader targeting than cookies, less precise. Think "category targeting" rather than "individual targeting."

### Attribution Reporting API
- **Replaces**: Third-party cookie-based conversion tracking
- **How it works**: Browser-mediated conversion attribution with privacy-preserving noise added to reports
- **Two report types**: Event-level (limited data, delayed) and summary (aggregated, more timely)
- **Impact**: Workable but less precise than current cookie-based attribution

### Protected Audience API (formerly FLEDGE)
- **Replaces**: Third-party cookie-based remarketing
- **How it works**: On-device auction for remarketing ads. User's interest groups stay on their device.
- **Status**: Available in Chrome, limited adoption
- **Impact**: Remarketing remains possible but with less control and transparency

---

## 8. Tracking Setup Checklist

### Essential (Day 1)
- [ ] GA4 with key events configured (form submissions, purchases, signups)
- [ ] Google Ads conversion tracking with enhanced conversions
- [ ] Meta Pixel with standard events + CAPI
- [ ] UTM parameters on all campaign links
- [ ] Consent banner (required for GDPR/CCPA compliance)

### Recommended (Month 1)
- [ ] Google Tag Manager (client-side) for tag management
- [ ] TikTok Pixel + Events API (if running TikTok Ads)
- [ ] LinkedIn Insight Tag (if running LinkedIn Ads)
- [ ] Consent Mode v2 (if targeting EU)
- [ ] Cross-domain tracking (if multiple domains in conversion path)

### Advanced (Quarter 1-2)
- [ ] Google Tag Manager server-side container
- [ ] Customer Data Platform or GA4 + BigQuery
- [ ] Offline conversion import (CRM → Google Ads, Meta)
- [ ] Marketing mix modeling or incrementality testing program
- [ ] Data clean room setup (for advanced audience collaboration)
