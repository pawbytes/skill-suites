# Emerging Analytics

Modern analytics approaches: AI-powered insights, server-side dominance, data warehouses, and reverse ETL.

## AI-Powered Analytics

**Anomaly detection:** GA4 and Narrative BI auto-detect metric shifts.

**Predictive analytics:** GA4 predictive audiences (likely purchasers, churners) for proactive remarketing.

**Natural language querying:** Looker Studio, Tableau AI, Power BI Copilot.

**Automated insights:** AI summaries of what changed, why, and what to do (Narrative BI, Pecan AI).

## Privacy-First Measurement

Cookie-based tracking captures 60-70% of reality. Triangulate across:
- Direct tracking (consented first-party)
- Modeled conversions (platform gap-filling)
- Incrementality testing (causal)
- MMM (statistical)

No single method suffices.

## Server-Side Dominance

Server-side is the default for serious analytics. Client-side is supplementary.

**Benefits:**
- Bypasses ad blockers and ITP
- Better match rates
- More accurate data
- Better compliance

**Platforms:** GA4 server-side, Meta CAPI, TikTok Events API, LinkedIn CAPI.

## Marketing Data Warehouses

Centralize in BigQuery, Snowflake, or Databricks.

**Stack:**
- ETL: Fivetran, Airbyte
- Transform: dbt
- Visualize: Looker, Tableau, Metabase

**Benefits:**
- Single source of truth
- Cross-channel analysis
- Custom attribution
- Retention beyond platform limits

## Reverse ETL

Push warehouse data back into tools:
- Enriched segments to ad platforms
- Lead scores to CRM
- Recommendations to email

**Tools:** Census, Hightouch, RudderStack

Closes the loop between insight and activation.