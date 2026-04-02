# Technology and Tools

Select and configure platforms for referral, affiliate, and partnership programs.

## Referral Program Tools

| Tool | Best For | Key Features | Pricing Model |
|---|---|---|---|
| ReferralCandy | E-commerce referral programs | Shopify/WooCommerce native, automated rewards, analytics | Monthly fee + commission |
| Rewardful | SaaS affiliate and referral | Stripe integration, recurring commissions, affiliate portal | Monthly subscription |
| GrowSurf | SaaS and B2B referral | Waitlist referrals, in-app widgets, milestone rewards | Monthly subscription |
| FirstPromoter | SaaS affiliate management | Stripe/Paddle integration, multi-tier, custom portals | Monthly subscription |
| Viral Loops | Pre-launch and waitlist referrals | Waitlist campaigns, referral contests, milestone rewards | Monthly subscription |
| Custom-built | Full control, unique mechanics | Unlimited customization, own data, product integration | Engineering investment |

**Selection criteria**: Integration with existing tech stack (payment processor, e-commerce platform, CRM), referral type supported (customer referral vs affiliate vs both), reward flexibility, tracking reliability, and scalability.

## Affiliate Platforms

| Platform | Best For | Key Features | Cost |
|---|---|---|---|
| Impact | Enterprise, multi-channel partnerships | Partner discovery, cross-device tracking, automation | Custom pricing |
| PartnerStack | B2B SaaS partnerships | Partner types (referral, affiliate, reseller), marketplace | Monthly + percentage |
| ShareASale | E-commerce affiliate marketing | Large affiliate network, robust tracking, merchant tools | Setup fee + commission |
| CJ Affiliate | Large-scale affiliate programs | Global reach, advanced reporting, deep linking | Custom pricing |
| Refersion | E-commerce, Shopify-native | Shopify integration, influencer + affiliate, easy setup | Monthly subscription |
| Post Affiliate Pro | Self-hosted affiliate tracking | Full control, white-label, multi-tier commissions | Monthly subscription |

## Tracking Setup

- **Conversion pixel or server-side API**: Fire on referral/purchase event. Server-side preferred as browser privacy tightens.
- **UTM parameters**: `utm_source=referral&utm_medium=link&utm_campaign={program}&utm_content={referrer_id}`.
- **Unique referral identifiers**: Per-user codes or links persisting through the conversion journey.
- **Cookie + fallback**: First-party cookie for web, coupon code fallback for cross-device.
- **CRM integration**: Sync referral source to CRM for lifetime attribution and LTV analysis.