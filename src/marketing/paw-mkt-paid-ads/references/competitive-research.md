# Competitive Ad Research

Use browser automation to gather live competitor ad data before building campaigns. This capability provides market intelligence on competitor messaging, creative approaches, and offer structures.

## Research Sessions

Start a named session to share context across research commands:

```bash
agent-browser --session ads-research open "https://..."
```

Close the session when done: `agent-browser --session ads-research close`

---

## 1. Meta Ad Library - Competitor Ad Research

**Purpose:** Discover competitor active ads, formats, copy themes, and proven performers.

```bash
agent-browser --session ads-research open "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q={competitor-name}&search_type=keyword_unordered" && agent-browser wait --load networkidle && agent-browser wait 4000
agent-browser screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/channels/paid-ads/content/competitor-{n}-meta-ads.png
agent-browser get text body
```

**Extract:**
- Number of active ads
- Ad formats in use
- Copy themes and angles
- Offer types and CTAs
- Long-running ads (months) = proven performers - note these specifically

---

## 2. Google Ad Transparency Center

**Purpose:** View competitor Google ad activity across search and display.

```bash
agent-browser --session ads-research open "https://adstransparency.google.com/?region=anywhere&query={competitor-name}" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
```

**Extract:**
- Active ad types (search, display, video)
- Copy examples
- Landing page URLs

---

## 3. TikTok Creative Center - Trending Ads

**Purpose:** Identify top-performing ad formats and creative styles in your category.

```bash
agent-browser --session ads-research open "https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
```

**Extract:**
- Top performing ad formats
- Creative styles and hooks
- Trending approaches in category

---

## 4. Competitor Landing Page Analysis

**Purpose:** Understand competitor conversion strategy and offer presentation.

```bash
agent-browser --session ads-research open {competitor-landing-page-url} && agent-browser wait --load networkidle
agent-browser get text body
agent-browser screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/channels/paid-ads/content/competitor-{n}-landing-page.png
```

**Extract:**
- Headline and value proposition
- Form fields (indicates lead qualification)
- CTA placement and copy
- Trust signals (testimonials, logos, guarantees)
- Offer structure and urgency elements

---

## 5. Competitor Pricing Research

**Purpose:** Understand competitive pricing and packaging strategy.

```bash
agent-browser --session ads-research open "https://{competitor-domain}/pricing" && agent-browser wait --load networkidle
agent-browser get text body
```

**Extract:**
- Tier names and positioning
- Price points
- Annual vs monthly discount
- Feature differentiation between tiers

---

## 6. LinkedIn Ad Library (B2B)

**Purpose:** Research B2B competitor advertising on LinkedIn.

```bash
agent-browser --session ads-research open "https://www.linkedin.com/ad-library/search?q={competitor-name}" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
```

**Extract:**
- B2B ad formats in use
- Targeting signals inferred from creative
- Offer types (content, demo, trial)

---

## Alternative: WebFetch and WebSearch

If `agent-browser` is unavailable, use `WebFetch` and `WebSearch` tools for research tasks. While less interactive, they can extract publicly available content from ad libraries and competitor pages.

---

## Research Output

Save research findings to:
`./.pawbytes/marketing-suites/brands/{brand-slug}/channels/paid-ads/content/competitor-research-{YYYY-MM-DD}.md`

Include:
- Competitor name and profile
- Active ad inventory summary
- Notable creative patterns
- Winning ad elements identified
- Opportunities for differentiation