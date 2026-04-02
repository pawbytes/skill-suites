# Capability: Auto-Discovery

**Outcome:** Gather all publicly available intelligence about a brand and its competitors BEFORE the SOSTAC interview begins.

**Output:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md`

## Purpose

Reduce burden on the user — they should not explain what is already discoverable. The SOSTAC interview focuses on internal knowledge, strategic intent, and context only the client can provide.

## Activation

Before running research:
1. Check if `agent-browser` is available (`agent-browser --version`)
2. If not found, install: `npm install -g agent-browser && npx playwright install chromium`
3. If installation fails, use `WebFetch` and `WebSearch` tools as alternatives

## Research Sequence

Full command sequences are in `./references/auto-discovery.md`. Execute in this order:

### Section 1: Brand's Own Digital Presence
- Homepage analysis (headline, value prop, CTA, trust signals)
- Technology stack detection (BuiltWith)
- Core Web Vitals (PageSpeed Insights)
- Pricing page
- Historical messaging (Wayback Machine)

### Section 2: Google SERP Research
- Brand name SERP (Knowledge Graph, sitelinks, reviews)
- Category keyword SERP (rankings, featured snippets, PAA)
- Competitor discovery queries ("alternatives", "vs", "best")
- Google Trends

### Section 3: Competitor Research
- For top 3-5 competitors: homepage, SimilarWeb traffic, pricing

### Section 4: Ad Intelligence
- Meta Ad Library (brand + competitors)
- Google Ad Transparency

### Section 5: Review Mining
- G2, Trustpilot, App Store (brand + competitors)

### Section 6: Customer Language Mining
- Reddit, Quora, People Also Ask

### Section 7: LinkedIn Intelligence
- Company page, job postings as strategic signals

## Synthesis

After research, produce a discovery brief AND an initial insights presentation:

> "I've done deep research on your brand and market. Here are the most important things I found:"

**3-5 key insights** — each with evidence and what it means for the marketing plan

**Competitive positioning map** — where you sit vs competitors and where gaps are

**Customer language themes** — how real customers describe the problem you solve

**Immediate opportunities** — quick wins spotted from research

Then: "Before we build the full plan, let me confirm a few things I couldn't determine from research alone..."

**2-3 targeted questions** — only what research couldn't answer

## Graceful Degradation

If sources block or fail:
- Log the block and move to next source
- Note in findings under "Sources Checked"
- Never halt the entire discovery run for a single blocked source
- Partial intelligence is more valuable than no intelligence

## Error Handling

```
[BLOCKED] {source} — {reason} — skipped, continuing
[404] {url} — page not found — noted in output
[CAPTCHA] {source} — access blocked — noted in output
[INSUFFICIENT_DATA] {source} — data unavailable
```

## Session Management

All research runs in a named session: `sostac-discovery-{brand-slug}`

```bash
agent-browser --session sostac-discovery-{brand-slug} open https://{brand-url}
# ... all subsequent commands in same session ...
agent-browser --session sostac-discovery-{brand-slug} close
```

## Output Template

See full template in `./references/auto-discovery.md` Section 8.

Key sections:
- Brand Intelligence (positioning, tech stack, vitals, pricing)
- Competitive Landscape (identified competitors, messaging comparison)
- Market Intelligence (search trends, keywords, PAA questions)
- Customer Voice (pain points, praise themes, language)
- Ad Activity (brand + competitor ads)
- LinkedIn Intelligence (headcount, job signals)
- Key Findings for SOSTAC Interview (5-8 bullets)
- Gaps — What Auto-Discovery Could Not Find