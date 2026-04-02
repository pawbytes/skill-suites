# Ad Creative Strategy

Framework for developing high-performing ad creative across platforms. For platform-specific creative best practices, see `./references/best-practices.md`.

---

## 1. Copywriting Formulas

| Formula | Structure | Best For |
|---------|-----------|----------|
| PAS | Pain > Agitate > Solution | Problem-aware audiences |
| AIDA | Attention > Interest > Desire > Action | Classic full-funnel |
| BAB | Before > After > Bridge | Transformation-focused |
| 4U | Useful, Urgent, Unique, Ultra-specific | Headlines |

---

## 2. Headline Optimization

- Lead with the benefit, not the feature
- Include numbers when possible
- Use power words (free, new, proven, instant, secret, limited)
- Test question vs statement vs command

### Character Limits
| Platform | Field | Limit |
|----------|-------|-------|
| Google RSA | Headline | 30 chars |
| Google RSA | Description | 90 chars |
| Meta | Primary text | 125 chars visible |
| Meta | Headline | 40 chars |
| LinkedIn | Intro text | 150 chars recommended |
| LinkedIn | Headline | 70 chars |
| TikTok | Ad description | 80 chars |

Always verify character counts before submitting.

---

## 3. Video Ad Script Framework

```
0-3s:  HOOK -- Pattern interrupt, bold claim, question, or visual surprise
3-10s: PROBLEM -- Agitate the pain point the audience feels
10-20s: SOLUTION -- Introduce product as the answer
20-25s: PROOF -- Testimonial, result, social proof
25-30s: CTA -- Clear next step with urgency
```

**UGC-style scripts:** Casual tone, face-to-camera, "I found this thing that..." format. Outperforms polished creative 2-3x on Meta and TikTok.

---

## 4. Angle-Based Creative Generation

Before writing headlines, identify 3-5 distinct **angles** for the offer. An angle is the specific lens through which you present the product.

### The 5 Core Angle Types

| Angle | Targets | Example Hook |
|-------|---------|--------------|
| Pain | Current problem | "Still copying data between tools manually?" |
| Outcome | Desired result | "10x your leads without doubling ad spend" |
| Social Proof | Evidence of success | "1,400 teams switched from [Competitor] this year" |
| Curiosity | Intrigue without revealing | "The metric most marketers ignore (it predicts churn)" |
| Urgency/Stakes | Cost of inaction | "Every day without this is costing you {outcome}" |

### Testing Process
1. Write 1 headline + 1 primary text per angle before any testing
2. Keep offer, CTA, and landing page constant across angles - only vary the angle
3. Test all angles simultaneously in Phase 1 (wide targeting, equal budget split)
4. Identify winning angle by lowest CPA or highest CTR after 100+ conversions
5. Move to Phase 2: iterate within winning angle (hook variations, visuals, copy length, CTA)
6. Move to Phase 3: test winning message across formats (static, carousel, video, UGC)

---

## 5. Creative Testing Methodology

### Phase 1 - Concept Testing
- Test 3-5 distinct angles with equal budget
- Wide targeting
- Winner = lowest CPA or highest CTR

### Phase 2 - Iteration
- Take winning angle
- Test variations (hooks, visuals, copy length, CTA)

### Phase 3 - Format Testing
- Test winning message across formats
- Static, carousel, video, UGC

### Statistical Significance
- Minimum 100 conversions or 1000 clicks per variant
- Run tests for 7+ days to account for day-of-week variation

---

## 6. Dynamic Creative Optimization (DCO)

- Provide multiple headlines, images, descriptions, CTAs
- Platform tests combinations algorithmically
- Use on Meta (Dynamic Creative), Google (Responsive Search/Display Ads)
- Best for high-volume campaigns
- Review asset-level performance and replace underperformers

---

## 7. Creative Iteration Log

Document every creative test. Save as `creative/iteration-log-{platform}-{YYYY-MM-DD}.md`.

| Round | Angle | Format | Variant | Metric | Result | Decision | Learning |
|-------|-------|--------|---------|--------|--------|----------|----------|
| 1 | Pain | Static | Hook A | CTR | 2.1% | Loser | Negative framing underperformed |
| 1 | Outcome | Static | Hook B | CTR | 3.8% | Winner | Benefit-led outperforms problem-led |
| 2 | Outcome | Video 15s | Hook B remix | CPA | $12.40 | Winner | Video 2x efficiency vs static |

**Patterns to watch:**
- Which angle types consistently win for this brand/audience?
- Which formats win at each funnel stage?
- What hooks perform best on which platform?
- At what frequency does fatigue begin?