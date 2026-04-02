# Privacy & Compliance

Implement privacy-first measurement compliant with GDPR, CCPA, and cookieless tracking requirements.

## Cookieless Tracking

Third-party cookies are deprecated. Strategies:
- Server-side tracking
- First-party cookies (GA4 default)
- Login-based tracking
- Privacy-preserving APIs (Topics, Attribution Reporting)
- Modeled conversions (Google/Meta gap-fill from consented users)

## Consent Management

Implement a CMP before tracking (Cookiebot, OneTrust, Iubenda, Usercentrics).

**Requirements:**
- Block non-essential tags until consent
- Use GTM Consent Mode v2 (required for Google Ads in EEA)
- GA4 Consent Mode models conversions for declining users (up to 70% signal recovery)

**Two settings:**
- `analytics_storage`
- `ad_storage`

## GDPR Requirements

- Consent before tracking
- Data access/deletion rights
- DPAs with vendors
- IP anonymization
- Genuine-choice cookie banners

## CCPA/CPRA Requirements

- "Do Not Sell" link
- Respect Global Privacy Control

## General Requirements

- Privacy policy listing all tracking
- Retention policies
- Regular audits

## First-Party Data Strategy

**Build:**
- Email addresses
- Purchase history
- On-site behavior
- Surveys and preferences
- CRM records

**Activate through:**
- CRM audiences for ad targeting
- Personalized experiences
- Lookalike modeling
- Cohort analysis

## Privacy-Focused Tools

| Tool | Type | Privacy Level | Cost |
|---|---|---|---|
| GA4 | Full analytics | Medium (consent required in EU) | Free |
| Plausible | Privacy-focused | High (no cookies, GDPR compliant) | $9-99/mo |
| Fathom | Privacy-focused | High (no cookies) | $14-44/mo |
| PostHog | Product analytics | High (self-hosted option) | Free-$450+/mo |
| Matomo | Full analytics | High (self-hosted, GDPR compliant) | Free-$229+/mo |