# UTM Parameter Standards & Naming Conventions

> Definitive reference for consistent UTM tagging across all marketing channels.
> Consistent UTM parameters are critical for accurate attribution, reporting, and optimization.

---

## Table of Contents

1. [UTM Parameter Overview](#utm-parameter-overview)
2. [Naming Convention Rules](#naming-convention-rules)
3. [Source/Medium Taxonomy](#sourcemedium-taxonomy)
4. [Campaign Naming Convention](#campaign-naming-convention)
5. [UTM Builder Template](#utm-builder-template)
6. [Common UTM Mistakes](#common-utm-mistakes)
7. [Integration with GA4 Reporting](#integration-with-ga4-reporting)
8. [UTM Governance & Documentation](#utm-governance--documentation)

---

## UTM Parameter Overview

### The Five UTM Parameters

| Parameter        | Required | Purpose                              | GA4 Dimension          |
|------------------|----------|--------------------------------------|------------------------|
| `utm_source`     | Yes      | Identifies the traffic source        | Session source         |
| `utm_medium`     | Yes      | Identifies the marketing channel     | Session medium         |
| `utm_campaign`   | Yes      | Identifies the specific campaign     | Session campaign       |
| `utm_term`       | No       | Identifies paid search keywords      | Session manual term    |
| `utm_content`    | No       | Differentiates creative or placement | Session manual content |

### URL Structure
```
https://yoursite.com/page?utm_source=SOURCE&utm_medium=MEDIUM&utm_campaign=CAMPAIGN&utm_term=TERM&utm_content=CONTENT
```

---

## Naming Convention Rules

### Golden Rules
1. **Always lowercase**: `facebook` not `Facebook` or `FACEBOOK`
2. **Use hyphens as separators**: `spring-sale` not `spring_sale` or `springsale`
3. **No spaces**: Spaces encode as `%20` and break analytics
4. **Be descriptive but concise**: `blog-header-cta` not `b-h-c` or `the-call-to-action-button-in-the-blog-header`
5. **Be consistent**: Once you choose a convention, never deviate
6. **Document everything**: Maintain a central UTM dictionary
7. **Use utm_id for GA4**: Include `utm_id` for campaign-level data import

### Character Rules
- **Allowed**: lowercase letters (a-z), numbers (0-9), hyphens (-)
- **Avoid**: uppercase letters, underscores, spaces, special characters
- **Maximum length**: Keep each parameter under 50 characters
- **Encoding**: Never use characters that require URL encoding

---

## Source/Medium Taxonomy

### Standard Source Values

#### Search
| Source          | When to Use                              |
|-----------------|------------------------------------------|
| `google`        | Google Ads, Google organic (auto-tagged)  |
| `bing`          | Microsoft/Bing Ads                       |
| `duckduckgo`    | DuckDuckGo traffic                       |
| `yahoo`         | Yahoo search traffic                     |
| `baidu`         | Baidu search (Chinese market)            |

#### Social Platforms
| Source          | When to Use                              |
|-----------------|------------------------------------------|
| `facebook`      | Facebook organic and paid                |
| `instagram`     | Instagram organic and paid               |
| `linkedin`      | LinkedIn organic and paid                |
| `twitter`       | X/Twitter organic and paid               |
| `tiktok`        | TikTok organic and paid                  |
| `youtube`       | YouTube organic and paid                 |
| `pinterest`     | Pinterest organic and paid               |
| `reddit`        | Reddit organic and paid                  |
| `threads`       | Threads posts                            |
| `bluesky`       | Bluesky posts                            |

#### Email
| Source          | When to Use                              |
|-----------------|------------------------------------------|
| `mailchimp`     | Mailchimp email campaigns                |
| `hubspot`       | HubSpot email campaigns                  |
| `convertkit`    | ConvertKit email campaigns               |
| `sendgrid`      | SendGrid transactional/marketing email   |
| `newsletter`    | Generic newsletter (when ESP varies)     |

#### Referral & Other
| Source          | When to Use                              |
|-----------------|------------------------------------------|
| `partner-name`  | Specific partner referrals               |
| `podcast-name`  | Podcast promo links                      |
| `event-name`    | Event/conference links                   |
| `qr`            | QR code scans                            |
| `sms`           | SMS/text message campaigns               |
| `slack`         | Slack community links                    |
| `discord`       | Discord community links                  |

### Standard Medium Values

| Medium          | When to Use                                      |
|-----------------|--------------------------------------------------|
| `cpc`           | Cost-per-click paid search ads                   |
| `cpm`           | Cost-per-impression display/programmatic ads     |
| `paid-social`   | Paid social media advertising                    |
| `social`        | Organic social media posts                       |
| `email`         | Email campaigns (marketing)                      |
| `transactional` | Transactional email (receipts, notifications)    |
| `referral`      | Partner referral links                           |
| `affiliate`     | Affiliate program links                          |
| `display`       | Display/banner advertising                       |
| `retargeting`   | Retargeting/remarketing campaigns                |
| `video`         | Video advertising (pre-roll, mid-roll)           |
| `podcast`       | Podcast sponsorship or mention                   |
| `sms`           | SMS/text message campaigns                       |
| `push`          | Push notification campaigns                      |
| `qr`            | QR code scans                                    |
| `organic`       | Organic search (usually auto-detected)           |
| `pr`            | Digital PR placements                            |
| `influencer`    | Influencer partnership content                   |
| `community`     | Community platform links (Discord, Slack, forums)|
| `print`         | Print advertising (use with QR/vanity URL)       |
| `event`         | Event/conference marketing                       |

### Source/Medium Combinations (Common Patterns)
```
google / cpc              (Google Ads search)
google / cpm              (Google Display Network)
facebook / paid-social    (Facebook Ads)
facebook / social         (Facebook organic posts)
instagram / paid-social   (Instagram Ads)
instagram / social        (Instagram organic)
linkedin / paid-social    (LinkedIn Ads)
linkedin / social         (LinkedIn organic)
tiktok / paid-social      (TikTok Ads)
tiktok / social           (TikTok organic)
newsletter / email        (Newsletter sends)
hubspot / email           (HubSpot email campaigns)
partner-acme / referral   (Partner referral)
podcast-name / podcast    (Podcast mention)
```

---

## Campaign Naming Convention

### Campaign Name Structure
```
[category]-[name]-[date]-[variant]
```

### Category Prefixes
| Prefix      | Category              | Example                          |
|-------------|----------------------|----------------------------------|
| `brand`     | Brand awareness       | `brand-launch-2026q1`           |
| `acq`       | Acquisition/growth    | `acq-free-trial-2026q1`         |
| `ret`       | Retargeting           | `ret-cart-abandon-2026q1`       |
| `nurture`   | Lead nurture          | `nurture-onboarding-2026q1`     |
| `promo`     | Promotions/sales      | `promo-spring-sale-202603`      |
| `product`   | Product launch        | `product-v3-launch-202603`      |
| `event`     | Events                | `event-webinar-seo-202603`      |
| `partner`   | Partnerships          | `partner-acme-collab-2026q1`    |
| `content`   | Content promotion     | `content-guide-seo-202603`      |
| `seasonal`  | Seasonal campaigns    | `seasonal-bfcm-2026`           |

### Date Format in Campaigns
- **Quarter**: `2026q1`, `2026q2`
- **Month**: `202601`, `202603`
- **Specific date**: `20260315` (for one-day events/launches)
- **Ongoing**: `evergreen` (for always-on campaigns)

### Examples of Complete Campaign Names
```
acq-free-trial-2026q1
promo-spring-sale-202603
brand-awareness-video-2026q1
ret-pricing-page-visitors-evergreen
nurture-welcome-series-evergreen
product-v3-launch-20260315
event-webinar-analytics-202603
content-seo-guide-202603
```

---

## UTM Builder Template

### Spreadsheet Column Structure
| Column           | Description                          | Example                    |
|------------------|--------------------------------------|----------------------------|
| Campaign Name    | Internal campaign reference          | Spring Sale 2026           |
| Landing Page URL | Destination URL (no params)          | https://site.com/pricing   |
| utm_source       | Traffic source                       | facebook                   |
| utm_medium       | Channel type                         | paid-social                |
| utm_campaign     | Campaign identifier                  | promo-spring-sale-202603   |
| utm_term         | Keyword (paid search only)           | marketing-automation       |
| utm_content      | Creative/placement variant           | carousel-v2-blue           |
| Final URL        | Auto-generated tagged URL            | (formula concatenation)    |
| Short URL        | Shortened version (for social/print) | https://bit.ly/xyz123      |
| Owner            | Person responsible                   | Jane Smith                 |
| Date Created     | When the UTM was generated           | 2026-03-07                 |

### utm_content Best Practices
Use `utm_content` to differentiate:
- **Ad creative variations**: `video-v1`, `static-v2`, `carousel-v3`
- **CTA variations**: `hero-cta`, `sidebar-cta`, `footer-cta`
- **Placement**: `feed`, `stories`, `reels`, `sidebar`
- **Audience segment**: `lookalike-1pct`, `retarget-30d`, `interest-marketing`
- **Design elements**: `blue-banner`, `red-button`, `minimal-layout`

---

## Common UTM Mistakes

### Mistake 1: Inconsistent Capitalization
- **Wrong**: `utm_source=Facebook`, `utm_source=facebook`, `utm_source=FACEBOOK`
- **Right**: Always `utm_source=facebook`
- **Impact**: GA4 treats these as three separate sources; splits your data

### Mistake 2: Using Spaces
- **Wrong**: `utm_campaign=spring sale 2026`
- **Right**: `utm_campaign=spring-sale-2026`
- **Impact**: Spaces encode as `%20`, creating messy and error-prone URLs

### Mistake 3: Tagging Internal Links
- **Wrong**: UTM parameters on links within your own site
- **Right**: Only use UTMs on external links pointing TO your site
- **Impact**: Overwrites the original source/medium attribution; inflates self-referrals

### Mistake 4: Missing Parameters
- **Wrong**: Only including `utm_source` without `utm_medium`
- **Right**: Always include source, medium, and campaign together
- **Impact**: Incomplete attribution data; traffic falls into "(not set)" buckets

### Mistake 5: Not Using a Central UTM Log
- **Wrong**: Each team member creates UTMs independently
- **Right**: Shared UTM builder spreadsheet with approval process
- **Impact**: Inconsistent naming, duplicate campaigns, unreliable reporting

### Mistake 6: Overly Complex or Cryptic Names
- **Wrong**: `utm_campaign=fb-rtg-lal-1-v2-b-202603-js-test3`
- **Right**: `utm_campaign=ret-lookalike-1pct-202603` with utm_content for creative variant
- **Impact**: Impossible to read in reports; no one remembers what the codes mean

### Mistake 7: Not Shortening URLs for Social/Print
- **Wrong**: Posting a 200-character URL with UTMs visible on social media
- **Right**: Use URL shortener (Bitly, Short.io) or platform-native link tracking
- **Impact**: Looks unprofessional; users may not trust long parameter-heavy URLs

### Mistake 8: Forgetting to Update Seasonal Parameters
- **Wrong**: Running `promo-spring-sale-2025` campaigns in 2026
- **Right**: Update date portions when campaigns are renewed
- **Impact**: Misleading historical data; impossible to compare year-over-year

---

## Integration with GA4 Reporting

### Where UTM Data Appears in GA4
- **Reports > Acquisition > Traffic acquisition**: Session-level source/medium/campaign
- **Reports > Acquisition > User acquisition**: First-touch source/medium/campaign
- **Explore > Free-form**: Custom reports with any UTM dimension
- **Explore > Funnel exploration**: Funnel by source/medium or campaign

### GA4 Default Channel Grouping
GA4 automatically classifies traffic into channels based on source/medium:

| Channel Group     | Matching Rule (source/medium)               |
|-------------------|----------------------------------------------|
| Organic Search    | medium = organic                             |
| Paid Search       | medium = cpc, ppc, or paid-search            |
| Display           | medium = display, cpm, or banner             |
| Paid Social       | medium = paid-social (social network source) |
| Organic Social    | medium = social (social network source)      |
| Email             | medium = email                               |
| Affiliates        | medium = affiliate                           |
| Referral          | medium = referral                            |
| Direct            | source = (direct) and medium = (none)        |
| Unassigned        | Does not match any other channel rule        |

### Ensuring Correct Channel Classification
- Use `cpc` for paid search (maps to "Paid Search")
- Use `paid-social` for paid social ads (maps to "Paid Social")
- Use `social` for organic social (maps to "Organic Social")
- Use `email` for email campaigns (maps to "Email")
- Use `display` for display ads (maps to "Display")
- Use `affiliate` for affiliate links (maps to "Affiliates")
- Use `referral` for partner referrals (maps to "Referral")

### Custom Channel Groups in GA4
If your naming convention does not match GA4 defaults, create custom channel groups:
1. Go to Admin > Data display > Channel groups
2. Create a new channel group
3. Define rules based on your source/medium taxonomy
4. Apply the custom channel group in reports and explorations

### UTM Data in GA4 Explorations
- **Dimension: Session source**: Maps to `utm_source`
- **Dimension: Session medium**: Maps to `utm_medium`
- **Dimension: Session campaign**: Maps to `utm_campaign`
- **Dimension: Session manual term**: Maps to `utm_term`
- **Dimension: Session manual ad content**: Maps to `utm_content`
- **Dimension: First user source**: First-touch `utm_source`
- **Dimension: First user medium**: First-touch `utm_medium`
- **Dimension: First user campaign**: First-touch `utm_campaign`

---

## UTM Governance & Documentation

### Governance Checklist
- [ ] Central UTM builder spreadsheet accessible to all team members
- [ ] Naming convention document (this file) shared and acknowledged
- [ ] Quarterly audit of UTM usage in GA4 (check for inconsistencies)
- [ ] New team member onboarding includes UTM training
- [ ] Campaign naming approval process for major campaigns
- [ ] Regular cleanup of "(not set)" and "unassigned" traffic in reports

### UTM Audit Process (Quarterly)
1. Export GA4 source/medium/campaign report for the quarter
2. Identify any non-standard source or medium values
3. Trace non-standard values to their origin (which team, which link)
4. Correct the source and update the UTM builder
5. Communicate corrections to the team
6. Update naming convention documentation if new patterns are needed

---

*Consistent UTM tagging is the foundation of accurate marketing measurement. When in doubt, check this reference before creating any tagged URL. A few minutes of discipline saves hours of data cleanup later.*
