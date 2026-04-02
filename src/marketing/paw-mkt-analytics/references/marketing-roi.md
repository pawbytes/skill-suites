# Marketing ROI

Calculate customer acquisition costs, lifetime value, and channel-level efficiency metrics.

## Core Calculations

| Metric | Formula | Target |
|---|---|---|
| CAC | Total Marketing Spend / New Customers | Lower is better |
| LTV (subscription) | ARPU x Gross Margin % x (1 / Monthly Churn) | Higher is better |
| LTV (e-commerce) | AOV x Purchase Frequency x Lifespan x Margin % | Higher is better |
| LTV:CAC Ratio | LTV / CAC | 3:1 or higher |
| Payback Period | CAC / (ARPU x Gross Margin %) | Under 12 months |

Calculate blended CAC (all channels) and channel-specific CAC. Include ad spend, tools, and allocated salaries.

## LTV:CAC Benchmarks

| Ratio | Meaning | Action |
|---|---|---|
| < 1:1 | Losing money per customer | Fix unit economics urgently |
| 1:1 - 2:1 | Barely sustainable | Optimize CAC or increase LTV |
| 3:1 | Healthy target | Maintain and optimize |
| 5:1+ | Under-investing in growth | Spend more on acquisition |
| 10:1+ | Significantly under-investing | Scale aggressively |

**LTV Example:**
$50/mo ARPU x 80% Gross Margin x (1 / 5% Monthly Churn) = $800 LTV

## Channel ROI

Per channel:
- Channel CAC (spend / customers)
- ROAS (revenue / spend)
- ROI % ((revenue - spend) / spend x 100)
- Contribution Margin (revenue - variable costs - spend)

Awareness channels may have low direct ROI but enable lower-funnel channels.

## Blended vs Channel-Specific

| Metric Type | Use For |
|---|---|---|
| Platform metrics | Within-channel optimization (but over-counts) |
| GA4 attribution | Cross-channel view (but under-counts view-through) |
| Blended metrics | Budget allocation, executive reporting (most accurate efficiency) |

**Marketing Efficiency Ratio (MER):**
```
MER = Total Revenue / Total Marketing Spend
```
- Healthy: 3-5x for DTC ecommerce, 5-10x for SaaS
- Track weekly as sanity check against platform-reported ROAS

## Output

Save as `./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/roi-report-{YYYY-MM}.md`

**Structure:**
- Summary
- Blended Metrics (CAC, LTV, LTV:CAC, Payback, ROAS)
- Channel ROI table
- Funnel Performance
- Cohort Comparison
- Recommendations

For LTV calculation methods, see `customer-ltv` in frameworks-index.csv.