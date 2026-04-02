# Meta Ads Strategy

Comprehensive guidance for Facebook and Instagram advertising. For extended best practices on Advantage+ campaigns, creative diversification, and CAPI implementation, see `./references/best-practices.md`.

---

## 1. Campaign Structure

### CBO (Campaign Budget Optimization)
- Default for 3+ ad sets
- Let Meta allocate budget to best performers
- Set minimum spend per ad set if needed

### ABO (Ad Set Budget)
- Use when testing new audiences at controlled spend
- Use for retargeting with fixed daily budgets

### Naming Convention
`{brand}_{objective}_{audience}_{placement}_{creative-type}_{date}` - consistent naming enables reporting

---

## 2. Advantage+ Campaigns

### Advantage+ Shopping
- Feed-based, provide 150+ catalog items
- Minimal audience restrictions
- Algorithmic creative and audience optimization
- Best for e-commerce with conversion pixel data

### Advantage+ App Campaigns
- Mobile app installs with automated creative combinations

### Advantage+ Audience
- Expanded targeting using audience suggestions as signals
- Replaces detailed targeting expansion

---

## 3. Audience Targeting

### Cold (Prospecting)
- Interest stacking
- Broad targeting with strong creative
- Lookalike audiences (1-3% for quality, 3-5% for scale, 5-10% for broad reach)

### Warm (Consideration)
- Website visitors (30/60/90/180 day windows)
- Video viewers (25/50/75/95% watched)
- Social engagers, email list matches

### Hot (Conversion/Retargeting)
- Add-to-cart abandoners (1-7 days)
- Checkout initiators
- Past purchasers for cross-sell/upsell
- High-value customer lookalikes

### Exclusions
- Always exclude converters from prospecting
- Exclude existing customers from acquisition campaigns unless cross-selling

---

## 4. Ad Formats and Creative

### Single Image
- 1080x1080 (feed), 1080x1920 (Stories/Reels)
- Primary text under 125 chars for above-fold
- Headline under 40 chars

### Carousel
- 3-10 cards, tell a story or showcase products
- First card must hook, last card = CTA

### Video
- 15-30s optimal for feed, 6-15s for Reels
- Hook in first 3 seconds
- Captions mandatory (85% watch muted)
- Square 1:1 for feed, 9:16 for Stories/Reels

### Collection
- Hero image/video + product catalog below
- Instant Experience landing page
- Best for e-commerce

### Reels Ads
- Native-feeling, vertical, fast-paced
- UGC-style outperforms polished
- Trending audio when possible

---

## 5. Conversion API (CAPI)

- Set up server-side event tracking alongside the pixel (redundant tracking)
- Deduplicate events using event_id
- Track: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase, Lead, CompleteRegistration
- Match quality score target: 6+
- Use partner integrations (Shopify, WordPress, etc.) for simplified setup
- For full server-side tracking setup and consent mode details, see `./references/privacy-tracking.md`

---

## 6. Retargeting Funnels

```
Awareness (Cold)     -->  Video Views, Engagement
    |
Consideration (Warm) -->  ViewContent retarget, Video viewer retarget
    |
Conversion (Hot)     -->  AddToCart abandoner, Checkout abandoner
    |
Retention            -->  Past purchaser cross-sell, Loyalty offers
```

**Window compression:**
- 180 days awareness
- 30 days consideration
- 7 days conversion

**Frequency caps:** 2-3x/week for retargeting