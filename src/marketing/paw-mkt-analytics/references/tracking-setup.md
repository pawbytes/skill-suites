# Tracking Setup

Implement comprehensive tracking across GA4, GTM, ad platforms, and server-side infrastructure.

## GA4 Configuration

**Data Streams:** One web stream per domain. Enable enhanced measurement (page views, scrolls, outbound clicks, site search, video engagement, file downloads).

**Events Architecture:**

| Event Type | Examples | Setup |
|---|---|---|
| Automatically collected | page_view, first_visit, session_start | No config needed |
| Enhanced measurement | scroll, click, file_download, video_start | Toggle in admin |
| Recommended events | login, sign_up, purchase, add_to_cart, begin_checkout | Implement per Google naming conventions |
| Custom events | form_submit, cta_click, pricing_page_view, demo_request | Define based on brand conversion points |

**Conversions:** Mark key events as conversions (max 30). Prioritize: purchase, lead form, sign-up, add-to-cart, demo request. Assign monetary values where possible.

**E-commerce:** Implement the full flow: view_item, add_to_cart, begin_checkout, add_payment_info, purchase with item parameters (item_id, item_name, price, quantity, category).

**Settings:**
- Data retention: 14 months
- Enable Google Signals
- Link to Google Ads, Search Console, and BigQuery

For full checklist, see `ga4-setup` in frameworks-index.csv.

## Google Tag Manager (GTM)

**Container:** One per domain. Naming: `{platform} - {event type} - {description}`

**Essential Tags:**

| Tag | Trigger | Purpose |
|---|---|---|
| GA4 Configuration | All Pages | Base tracking |
| GA4 Event -- form_submit | Form Submission | Lead tracking |
| Meta Pixel -- PageView | All Pages | Meta base tracking |
| Meta Pixel -- Lead | Form Submission | Meta conversion |
| Google Ads Conversion | Thank You Page | Ads conversion |
| LinkedIn Insight | All Pages | LinkedIn tracking |

**Data Layer:** Define a spec document listing every event and its parameters. Push structured data from the website for GTM to consume.

## UTM Parameter Strategy

| Parameter | Purpose | Convention |
|---|---|---|
| utm_source | Traffic origin | `google`, `meta`, `linkedin`, `newsletter` |
| utm_medium | Marketing medium | `cpc`, `organic`, `email`, `social`, `referral`, `display` |
| utm_campaign | Campaign ID | `{year}-{month}-{campaign-name}`: `2026-03-spring-launch` |
| utm_content | Creative variant | `banner-a`, `cta-red`, `video-15s` |
| utm_term | Keyword (paid search) | The keyword or audience targeted |

**Rules:** All lowercase, hyphens not spaces, no special characters, consistent across team.

For full UTM taxonomy, see `./references/utm-standards.md`.

## Event Naming Convention

**Format:** `object_action` — lowercase, underscores, no spaces, no hyphens.

```
object = the thing being acted on (noun)
action = what happened (past-tense verb)
```

**Examples:**
- `user_signed_up` not `SignUp` or `sign-up`
- `plan_upgraded` not `upgrade` or `planUpgrade`
- `checkout_started` not `beginCheckout`
- `form_submitted` not `form_submit`

**Essential properties on every event:**

| Property | Type | Example | Purpose |
|---|---|---|---|
| `user_id` | string | `u_1234abc` | Link events to users for cohort analysis |
| `session_id` | string | `s_xyz789` | Group events within a session |
| `timestamp` | ISO 8601 | `2026-03-07T14:30:00Z` | Precise sequencing |
| `page_url` | string | `/pricing` | Where the event occurred |
| `source` / `utm_source` | string | `google` | Traffic attribution |

## Tool Selection Guide

| Tool | Best For | When to Use |
|---|---|---|
| **GA4 + GTM** | All web properties | Default for any brand with a website |
| **Mixpanel** | Product analytics, funnels | SaaS or apps needing in-product behavior |
| **Amplitude** | Product analytics at scale | Larger product teams, deeper behavioral analysis |
| **PostHog** | Self-hosted analytics | Privacy/compliance, analytics + experimentation |
| **Segment** | Data routing / CDP | Sending same event data to 5+ tools |

**Decision framework:**
- **Early stage**: GA4 + GTM only
- **Product-led growth**: Add Mixpanel or PostHog
- **Scaling (5+ tools)**: Add Segment as event router
- **Self-hosted/privacy-first**: PostHog
- **Enterprise**: Amplitude or Mixpanel + data warehouse

## Server-Side Tracking

Browser-based tracking loses 20-40% of events due to ad blockers, ITP, and cookie restrictions.

**Options:** GA4 server-side via Google Cloud, Meta Conversions API (CAPI), server-side GTM container, CDPs (Segment, RudderStack).

**Implementation:** High-value conversion events first. Run parallel with client-side. Deduplicate using event IDs.

## Ad Platform Pixels

| Platform | Pixel/Tag | Key Events | Server-Side |
|---|---|---|---|
| Meta | Meta Pixel + CAPI | PageView, ViewContent, AddToCart, Purchase, Lead | Conversions API |
| Google Ads | Google Ads tag | Purchase, lead, sign-up conversions | Enhanced conversions |
| LinkedIn | Insight Tag | Page views, conversions, lead gen submits | CAPI (beta) |
| TikTok | TikTok Pixel | PageView, ViewContent, AddToCart, Purchase | Events API |

Meta match quality target: 6+.