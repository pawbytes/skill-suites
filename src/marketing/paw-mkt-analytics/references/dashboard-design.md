# Dashboard Design

Create dashboards that answer the viewer's question, not showcase available data.

## Dashboard Types

| Dashboard | Audience | Refresh | Focus |
|---|---|---|---|
| Executive / KPI | Founder, leadership | Weekly | Primary KPIs, revenue, ROI, trends |
| Channel Performance | Marketing lead | Daily/Weekly | Per-channel metrics, spend, CPA, ROAS |
| Campaign | Channel specialist | Daily | Active campaign metrics, creative performance, pacing |
| Funnel | Growth / product | Weekly | Stage-by-stage conversion, drop-off, cohorts |
| Content | Content team | Weekly | Traffic by content, engagement, conversions per piece |

## Dashboard Components

Every dashboard includes:
- Date range selector with comparison period
- Scorecard row (3-5 metrics with trend arrows and vs-target indicators)
- Trend chart for the primary metric (30/60/90 day)
- Breakdown table by channel/campaign/audience
- Conversion funnel visualization where applicable
- Annotations for key events (launches, algorithm changes, promotions)

## Visualization Best Practices

- One metric per chart
- Line charts for trends, bar charts for comparisons, tables for detail, scorecards for KPIs
- Consistent color coding: green = on target, red = below, grey = benchmark
- No 3D charts, no pie charts beyond 4 segments, no dual axes unless essential

## Tool Recommendations

| Tool | Best For | Cost |
|---|---|---|
| Looker Studio | GA4 native, free, shareable | Free |
| Tableau | Enterprise, complex data blending | $$$ |
| Power BI | Microsoft ecosystem, internal teams | $$ |
| Metabase/Grafana | Self-hosted, full control, data warehouse | Free-$$ |

**Default:** Start with Looker Studio. Graduate to Tableau or custom when data warehouse is established.

## Channel Dashboard Structure

For each active channel from SOSTAC tactics:
- Spend pacing
- Primary KPI
- Secondary metrics
- Top performers
- Trend vs prior period

## Output

Save as `./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/dashboard-spec-{type}-{YYYY-MM-DD}.md`

**Structure:**
- Purpose and Audience
- Data Sources
- Metrics and Visualizations table
- Layout description
- Filters and Controls
- Refresh Cadence
- Access and Sharing