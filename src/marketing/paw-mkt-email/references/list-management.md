# List Management

Build, segment, and maintain a healthy email list.

## Segmentation Strategies

| Segment Type | Criteria | Use Case |
|---|---|---|
| Demographic | Age, location, job title, company size | Content personalization |
| Behavioral | Opens, clicks, purchases, site visits | Engagement-based targeting |
| Lifecycle | Subscriber, lead, customer, lapsed | Journey-appropriate messaging |
| Purchase | Product category, order value, frequency | Cross-sell, upsell, VIP |
| Engagement | Active (30d), passive (30-90d), inactive (90d+) | Re-engagement, list hygiene |
| Preference | Self-selected topics, frequency choices | Respect subscriber control |

**Start with**: Engagement-based segmentation (active vs inactive)
**Add as data accumulates**: Lifecycle and purchase segments

## List Hygiene

### Immediate Actions

- Remove hard bounces immediately
- Suppress soft bounces after 3-5 consecutive failures
- Run re-engagement on 90-day inactive subscribers
- Remove non-responders to protect sender reputation

### Ongoing Practices

- Validate email addresses at signup (syntax, MX record, disposable domain detection)
- Clean full list quarterly with verification service
- Target metrics: bounce rate under 2%, unsubscribe rate under 0.5%, complaint rate under 0.1%

## List Growth Tactics

### Lead Magnets

Must deliver immediate, specific value:
- Checklists, templates, guides
- Calculators, free tools, quizzes
- Exclusive reports

### Website Opt-ins

| Type | Conversion Rate |
|---|---|
| Exit intent popup | 2-5% |
| Scroll-triggered slide-in | 1-3% |
| Inline forms | 1-2% |
| Content upgrades | 5-15% |
| Landing pages | 10-30% |

### Social and Partnerships

- Promote magnets in bio links and posts
- Run lead gen ads
- Partner with complementary brands for cross-promotion

### Events and Referrals

- Webinars, workshops, challenges (registration = opt-in with consent)
- Incentivize subscribers to share (SparkLoop, ReferralHero)

## Compliance

### CAN-SPAM (US)

- Physical mailing address in footer
- Clear unsubscribe mechanism (10-day honor window)
- No misleading headers or subjects

### GDPR (EU/UK)

- Explicit opt-in consent required
- Recorded consent history
- Right to access/correct/delete
- Privacy policy link
- Data processing agreement with ESP

### CASL (Canada)

- Express consent required
- Implied consent expires after 2 years
- Sender identification required
- Unsubscribe mechanism required

### Universal Best Practices

- Double opt-in for all lists
- Preference center over binary unsubscribe
- One-click List-Unsubscribe header
- Never buy or rent lists
- Honor unsubscribes within 24 hours

For full compliance checklist, see `./references/best-practices.md`.