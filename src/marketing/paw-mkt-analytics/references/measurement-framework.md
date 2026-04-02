# Measurement Framework

Build a structured hierarchy mapping business goals to daily operational metrics.

## KPI Hierarchy

| Tier | Purpose | Audience | Examples |
|---|---|---|---|
| Primary KPIs (1-2) | Directly measure SOSTAC objectives | Executive, founder | Revenue, MQLs, active users |
| Secondary KPIs (3-5) | Progress indicators feeding primary | Marketing lead | Traffic, conversion rate, CAC |
| Diagnostic KPIs (per channel) | Optimization levers | Channel specialist | CTR, CPC, bounce rate, open rate |

## Metric Definitions

For each KPI, document:
- What it measures and why
- Formula (numerator/denominator with inclusion/exclusion criteria)
- Data source and measurement tool
- Review cadence and owner
- Numeric target with deadline (from SOSTAC objectives)
- Action threshold (the value triggering investigation)

## North Star Metric

Identify the single metric that best captures customer value. All other metrics ladder up to this.

**Examples:**
- Weekly active users (SaaS)
- Monthly repeat purchase rate (e-commerce)
- Qualified leads per month (B2B)

## Output

Save as `./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/measurement-plan-{YYYY-MM-DD}.md`

**Structure:**
- North Star Metric (definition, baseline, target)
- KPI Hierarchy tables (primary/secondary/diagnostic)
- Event Tracking Spec
- UTM Convention
- Data Sources and Tools
- Consent and Privacy notes