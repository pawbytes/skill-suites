# Competitive Research Capability

**Outcome:** Gather live competitor positioning data before building comparison slides, battle cards, or champion kits.

---

## When to Use

Use `agent-browser` for live competitive intelligence when:
- Building battle cards for specific competitors
- Creating comparison slides for sales deck
- Preparing champion kit competitive sections
- Updating stale competitive positioning

---

## Research Targets

### 1. Competitor Pricing and Positioning

**What to find:** Tier names, price points, annual discount, included features per tier, free trial/freemium availability.

**Command:**
```bash
agent-browser --session sales-research open "https://{competitor-domain}/pricing" && agent-browser wait --load networkidle
agent-browser get text body
agent-browser screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/operations/sales/research/competitor-{n}-pricing.png
```

### 2. Competitor Comparison Pages

**What to find:** Which differentiators competitors claim, how they position against others, what pain points they lead with.

**Command:**
```bash
agent-browser --session sales-research open "https://www.google.com/search?q={competitor-name}+vs+alternatives+OR+comparison" && agent-browser wait --load networkidle
agent-browser get text body
```

### 3. G2 / Capterra Reviews

**What to find:** Top-rated cons, recurring complaints, missing features — these become differentiation talking points.

**Command:**
```bash
agent-browser --session sales-research open "https://www.g2.com/products/{competitor-slug}/reviews" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
```

### 4. Competitor Case Studies

**What to find:** Industries served, customer size, metrics cited, proof format — benchmark against your proof.

**Command:**
```bash
agent-browser --session sales-research open "https://{competitor-domain}/customers" && agent-browser wait --load networkidle
agent-browser get text body
```

### 5. Your Own Review Profile

**What to find:** Top-cited pros (for deck/one-pager), top-cited cons (address in objection handling), verbatim quotes.

**Command:**
```bash
agent-browser --session sales-research open "https://www.g2.com/products/{brand-slug}/reviews" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
```

### 6. LinkedIn Ad Library

**What to find:** Offer type (demo, trial, content), messaging angle, target seniority/function.

**Command:**
```bash
agent-browser --session sales-research open "https://www.linkedin.com/ad-library/search?q={competitor-name}" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
```

---

## Session Management

**Start named session:** `agent-browser --session sales-research open ...`
**Close session:** `agent-browser --session sales-research close`

---

## Fallback

If `agent-browser` unavailable, use `WebFetch` and `WebSearch` tools for all research tasks. See `./shared-patterns.md` for installation instructions.