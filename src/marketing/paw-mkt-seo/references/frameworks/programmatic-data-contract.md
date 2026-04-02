# Data Contract

Programmatic SEO fails when the template is designed before the data contract.

For every template family, define:
- **required fields** -- page cannot publish without these
- **optional fields** -- enrich page quality when present
- **derived fields** -- computed from raw data
- **freshness rules** -- how often each field updates
- **fallback behavior** -- what happens when data is missing

### Example data contract skeleton
| Field | Required? | Example | Notes |
|---|---|---|---|
| Entity name | Yes | HubSpot | Used in title, H1, intro |
| Category | Yes | CRM | Used for taxonomy and linking |
| Description | Yes | CRM for SMB sales teams | Must be human-reviewed or sourced |
| Pricing | Optional | Starts at $20/user | Timestamp and source required |
| Review count | Optional | 182 | Should include source |
| Use cases | Yes | Lead routing, pipeline sync | Fuels body content |
| Location proof | Optional | Austin service area | Needed for local pages |
| Last updated | Yes | 2026-03-01 | Freshness and QA |

### Rules for missing data
- Do not publish if required fields are missing.
- Avoid generic fallback copy such as "Information coming soon."
- If optional fields are sparse, reduce template scope or noindex the page until enriched.
- If many entities fail the contract, the page family is not ready.
