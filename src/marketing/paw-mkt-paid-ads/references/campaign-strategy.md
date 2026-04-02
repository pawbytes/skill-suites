# Campaign Strategy

Full-funnel campaign architecture, budget allocation, bidding strategy, and scaling guidance. For benchmark data to inform targets, see `./references/benchmarks.md`.

---

## 1. Full-Funnel Architecture

| Stage | Objective | Platforms | Audiences | KPI |
|-------|------------|-----------|-----------|-----|
| Awareness | Reach, Video Views | Meta, TikTok, YouTube, Display | Broad, Lookalike, Interest | CPM, VTR, Reach |
| Consideration | Traffic, Engagement | Meta, Google, LinkedIn, TikTok | Engagers, Video viewers | CPC, CTR, Engagement |
| Conversion | Leads, Sales | Google Search, Meta, LinkedIn | Retargeting, High-intent | CPA, ROAS, Conv Rate |
| Retention | Repeat, LTV | Meta, Email, Google | Past purchasers, CRM | Repeat rate, LTV, ROAS |

---

## 2. Budget Allocation

### By Business Stage
| Stage | Conversion | Consideration | Awareness | Retention |
|-------|------------|---------------|-----------|-----------|
| New brands / no data | 70% | 20% | 10% | - |
| Established brands | 50% | 30% | 20% | - |
| Scaling phase | 40% | 30% | 30% | - |

### Cross-Platform Split
Allocate based on where the target audience lives (from SOSTAC strategy), not evenly.

---

## 3. Bidding Strategy Selection

1. **Start manual/conservative:** Understand baseline CPCs and CPAs before automating
2. **Graduate to automated:** Once 30+ conversions per month, switch to target CPA or target ROAS
3. **Set realistic targets:** Use current CPA/ROAS as starting target. Improve by 10-15% increments, not 50%
4. **Budget-to-bid alignment:** Daily budget should support 5-10x the target CPA to exit learning phase

---

## 4. Attribution

### Google
- Data-driven attribution (default)
- Last-click as fallback for low-volume

### Meta
- 7-day click, 1-day view default
- Compare against 1-day click for conservative view
- Use Conversion Lift studies for incrementality

### Cross-Platform
- UTM parameters on all ad URLs
- GA4 as central source of truth
- Compare platform-reported vs GA4 attribution
- Understand each platform over-reports

---

## 5. Audience Strategy

### Cold Audiences
- Broad targeting with strong creative
- Lookalikes from best customers
- Interest stacking on Meta
- Custom intent on Google

### Warm Audiences
- Site visitors (segment by pages visited, time on site)
- Video viewers, social engagers
- Email openers

### Hot Audiences
- Cart abandoners
- Pricing page visitors
- Demo requesters, free trial users
- Past purchasers for upsell

### Exclusion Hygiene
- Exclude converters from acquisition
- Exclude employees
- Exclude irrelevant geographies
- Suppress unsubscribed contacts

---

## 6. Scaling Strategies

### Vertical Scaling
- Increase budget 15-20% every 3-5 days on winning campaigns
- Avoid increasing more than 2x in a single change - large jumps reset learning and spike CPA
- Monitor CPA drift after each increase

### Horizontal Scaling
- Duplicate winning campaigns to new audiences
- Test new platforms
- Expand to new geographies
- Launch new creative angles to same audiences

### Creative Scaling
- The number one scaling bottleneck is creative fatigue
- Produce 5-10 new creatives per week when scaling aggressively
- Rotate creative every 7-14 days on Meta and TikTok