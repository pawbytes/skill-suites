# GA4 Setup Checklist & Event Taxonomy

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
