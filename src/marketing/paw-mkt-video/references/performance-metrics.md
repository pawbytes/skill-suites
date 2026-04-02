# Performance Metrics

## Purpose
Measure and analyze video performance -- platform-specific metrics, retention analysis, ad performance, and review cadence.

## Process

1. **Load Context**: Read brand KPIs and objectives from SOSTAC
2. **Identify Metrics**: Match metrics to platform and objective
3. **Analyze Retention**: Identify drop-off patterns and improvement opportunities
4. **Evaluate Ad Performance**: Hook rate, hold rate, CTR, ROAS
5. **Recommend Improvements**: Specific adjustments based on data

---

## 1. Key Metrics by Platform

| Metric | YouTube | TikTok | Reels | Shorts |
|--------|---------|--------|-------|--------|
| View-Through Rate | Watch time + retention curve | Watch time % | Plays vs reach | Viewed vs shown |
| Engagement Rate | (Likes+comments+shares) / views | (Likes+comments+shares+saves) / views | Same | Same |
| Click-Through Rate | Thumbnail CTR | Profile visits / views | Profile visits | Subscriber conversion |
| Conversion | Link clicks, subscribers | Bio link, TikTok Shop | Link clicks | Subscriber conversion |

---

## 2. Audience Retention Curves

**Benchmarks**:
- YouTube long-form: 40-60% average retention is good, 60%+ excellent
- Short-form: 70%+ good, 90%+ viral potential

**Common drop-off patterns**:
- Sharp drop at intro (hook failed)
- Mid-video dip (pacing issue)
- Cliff at CTA (too aggressive)

**Improvement process**:
- Analyze retention in YouTube Studio
- Map drop-offs to script sections
- Adjust future scripts at weak points

For detailed benchmarks and retention analysis, see `./benchmarks.md`.

---

## 3. Video Ad Metrics

| Metric | Good | Excellent | Action if Below |
|--------|------|-----------|-----------------|
| Hook rate (3s views / impressions) | 25%+ | 40%+ | Rework first 3 seconds |
| Hold rate (ThruPlay / 3s views) | 15%+ | 25%+ | Improve pacing |
| CTR (link clicks / impressions) | 1%+ | 2%+ | Strengthen CTA and offer |
| Cost per ThruPlay | Under $0.05 | Under $0.02 | Creative or targeting issue |
| ROAS | 3x+ | 5x+ | Full funnel audit |

---

## 4. Review Cadence

**Weekly**:
- Top/bottom 5 videos by views and engagement
- Pattern identification
- Adjust upcoming content

**Monthly**:
- Full performance review
- Growth and retention trends
- Pillar performance
- Conversions

**Quarterly**:
- Strategic review against SOSTAC objectives
- Adjust pillars, platforms, production approach

---

## 5. Output

Deliver:
- **Performance report** with key metrics and trends
- **Retention analysis** with specific drop-off points and recommendations
- **Ad performance evaluation** with optimization suggestions
- **Content adjustments** based on data
- **Save to**: `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/video/content/performance/monthly-report-{YYYY-MM}.md`