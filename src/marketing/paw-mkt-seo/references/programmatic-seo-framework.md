# Programmatic SEO Framework

**Purpose:** Operating framework for programmatic SEO (pSEO) inside the paw-mkt-seo skill. Use when the user wants to scale SEO through template-driven pages such as location pages, catalog pages, integration pages, directories, comparison hubs, statistics pages, or other repeatable entity-based page sets.

Read this reference selectively:
1. Qualification -- decide whether pSEO should exist at all.
2. Page archetypes -- choose the right model for the page family.
3. Data contract and template spec -- define what each page needs before launch.
4. Launch and QA -- prevent thin-page rollouts.
5. Monitoring and pruning -- keep the index healthy after launch.

---

## 1. Qualification: Should This Be Programmatic SEO?

Programmatic SEO works when a page family sits at the overlap of:
- **repeatable demand** -- many closely related searches exist
- **structured data** -- the business has reliable fields to populate pages
- **real usefulness** -- each page can help a user complete a real job better than a generic page

Use this qualification table before recommending pSEO:

| Check | Pass Signal | Fail Signal |
|---|---|---|
| Search demand pattern | Many long-tail variations with clear intent | Only a handful of keywords or unclear intent |
| Data availability | Clean, current source data with stable fields | Sparse, stale, manual-only data |
| Unique value per page | Local proof, proprietary data, comparisons, examples, reviews, availability, FAQs | Mostly token swaps with no differentiated value |
| Business value | The page family supports acquisition, conversions, or defensible topic coverage | Vanity traffic only |
| Operational support | Team can QA, monitor, refresh, and prune | Team can publish but not maintain |

### Reject pSEO when:
- The plan depends on spinning near-duplicate pages.
- The only difference between pages is a city, keyword, or product name.
- The data source is incomplete, unreliable, or updates too slowly for the query.
- The business cannot maintain indexation rules, content refreshes, and pruning.

### A simple go / no-go heuristic
Recommend pSEO only if you can clearly answer all four:
1. Why does this page deserve to exist separately?
2. What unique information will appear on each page?
3. How will users discover sibling pages through internal linking?
4. How will weak pages be found, fixed, or removed later?

---

## 2. Page Archetypes That Commonly Fit pSEO

Choose the page family first. Do not start with a generic template.

### 2.1 Location + Service Pages
**Pattern:** `/services/{service}/{city}` or `/locations/{city}/{service}`

Use when the brand truly serves the location and can prove it with:
- localized proof points
- area-specific FAQs
- case studies or testimonials
- service constraints, availability, or regulations by location

Do not generate one page per city unless there is real operational coverage and meaningful local differentiation.

### 2.2 Marketplace / Directory Pages
**Pattern:** `/directory/{category}/{entity}` or `/vendors/{vendor}`

Use when each entity page can include:
- complete profiles
- filters and comparisons
- trust data (reviews, certifications, awards, pricing ranges)
- related entities and alternatives

### 2.3 Integration / Template / Use-Case Pages
**Pattern:** `/integrations/{tool}` or `/templates/{template-name}` or `/use-cases/{segment}`

Strong fit when each page can include:
- setup details
- examples
- common workflows
- compatibility notes
- FAQs tied to the tool or use case

### 2.4 Comparison Pages
**Pattern:** `/{brand}-vs-{competitor}` or `/compare/{a}-vs-{b}`

Use carefully. Comparison pages need balanced, specific content and ongoing updates. Avoid mass-generating comparisons without meaningful distinctions.

### 2.5 Statistics / Glossary / Reference Pages
**Pattern:** `/statistics/{topic}` or `/glossary/{term}`

Use when the site can become a citation source via:
- original or curated statistics
- consistent updates
- methodology notes
- data visual summaries

### 2.6 Catalog / Inventory Pages
**Pattern:** `/products/{category}/{item}` or `/collections/{attribute}`

Best fit when inventory, price, availability, specs, and comparison logic are reliable and can be updated automatically.

---

## 3. Opportunity Mapping

Before drafting templates, produce an opportunity map for the page family.

Include:
- **page family name**
- **target search pattern**
- **search intent**
- **primary conversion action**
- **source data owner**
- **estimated scale** (launch set and total possible set)
- **uniqueness levers**
- **main indexation risks**
- **main cannibalization risks**

### Opportunity map template
| Field | Notes |
|---|---|
| Page family | e.g. "CRM integration pages" |
| Search pattern | e.g. "[brand] + [integration]" |
| Intent | Informational / commercial / transactional |
| Core user task | What the user wants to figure out or do |
| Conversion | Demo, signup, lead, purchase, referral click |
| Required data | Fields needed for each page |
| Uniqueness levers | What changes meaningfully by entity |
| Risks | Thin pages, overlap, stale data, low inventory |

Do not recommend page counts until the opportunity map is complete.

---

## 4. Data Contract

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

---

## 5. Template Specification

Each template family needs a written spec before content generation.

Include these sections in the spec:

### 5.1 Intent and query mapping
- Primary keyword pattern
- Supporting modifiers
- Search intent
- Closest competing page type in the current site
- Canonical page for this intent cluster

### 5.2 URL pattern
Keep URLs predictable, readable, and stable.

Examples:
- `/integrations/salesforce`
- `/services/roof-repair/austin`
- `/directory/accounting-software/quickbooks`

Avoid parameter-heavy or auto-generated slugs with IDs unless required.

### 5.3 On-page block requirements
For each block, define:
- content purpose
- data source
- whether it is required
- what makes it unique

Recommended block types:
- concise intro answering intent directly
- entity-specific overview
- use cases / scenarios
- comparison or alternatives section
- FAQ section
- proof section (reviews, stats, testimonials, examples)
- related pages / sibling entities
- conversion CTA tied to intent

### 5.4 Minimum uniqueness threshold
Every template family should define what counts as enough unique value.

Example threshold:
- unique intro paragraph
- at least 3 entity-specific bullets or facts
- one differentiated section that could not be reused unchanged on sibling pages
- at least 3 internal links chosen by relationship logic
- FAQ answers customized to the entity or location

If the page cannot meet the threshold, do not index it.

---

## 6. Internal Linking for pSEO

Internal linking is not a cleanup step. It is part of the page system design.

Use a layered model:
1. **Hub pages** -- category or parent pages linking to child pages
2. **Child pages** -- link back to hub and to relevant siblings
3. **Relationship links** -- alternatives, adjacent categories, nearby locations, compatible integrations
4. **Editorial links** -- blog, guides, documentation, and conversion pages feeding the page family

### Linking rules
- Every generated page must have a parent hub.
- Every generated page should link to 2-5 relevant siblings or alternatives.
- Use relationship logic, not random "related pages" widgets.
- Keep important template families within reasonable click depth.
- Ensure the sitemap and internal links reinforce the same hierarchy.

### Relationship logic examples
- directory pages: same category, adjacent price band, highest-rated alternatives
- location pages: nearest service areas, same service other cities, local guides
- integrations: same category, common workflow pairs, migration alternatives

---

## 7. Indexation, Canonicals, and Crawl Control

Programmatic SEO needs explicit indexation policy before launch.

For each template family define:
- **indexable pages**
- **noindex pages**
- **canonical targets**
- **sitemap inclusion rules**
- **pruning triggers**

### Canonical rules
- Self-canonicalize pages that are genuinely distinct.
- Canonical filtered, sorted, parameterized, or near-duplicate variants to the clean version.
- Do not canonicalize materially different pages to a parent page just to hide duplication problems.

### Indexation rules
Index only when pages meet the minimum quality threshold and business value threshold.

Common noindex cases:
- sparse entity profiles
- empty inventory or unavailable listings
- low-information near-duplicate filters
- location pages with no real local proof
- auto-generated pages pending enrichment

### Sitemap rules
- Include only canonical, indexable, 200-status URLs.
- Split large pSEO families into dedicated sitemaps by template type or cohort.
- Remove pruned or noindexed URLs from sitemaps quickly.

---

## 8. Launch Strategy

Do not launch all pages at once by default. Launch in batches.

### Recommended launch sequence
1. Pilot set of highest-confidence pages
2. QA sample across template variants
3. Check crawl, indexation, and user behavior
4. Expand to next cohort only if the first cohort performs acceptably

### Batch launch checklist
- title tags and H1s read naturally
- intros answer intent directly
- required data fields present
- schema valid and matches visible content
- canonicals correct
- internal links resolve correctly
- analytics and conversions tracked
- XML sitemap updated
- pages accessible in rendered HTML
- no obvious thin or soft-404 pages in the sample

### QA sampling guidance
Review a sample from:
- top-value entities
- low-data entities
- edge-case entities
- each template variant
- each important locale or taxonomy branch

---

## 9. Monitoring Framework

Track performance at the **template-family** level, not just page by page.

### Core KPIs
| KPI | Why it matters |
|---|---|
| Indexed pages / submitted pages | Shows whether Google accepts the cohort |
| Impressions by template family | Confirms the family is entering the SERP |
| Click-through rate by template family | Reveals snippet and intent alignment |
| Landing page conversions | Measures commercial value, not just traffic |
| Crawl frequency | Indicates whether Google considers the family important |
| Soft 404 / duplicate signals | Early warning for low-value rollouts |
| Content freshness coverage | Shows whether data updates are keeping up |

### Watch for these patterns
- Many pages crawled but few indexed -> quality or duplication issue
- Indexed pages with no impressions -> demand or internal-linking issue
- Impressions but weak CTR -> title/meta mismatch or poor SERP positioning
- Traffic without conversions -> wrong intent or weak CTA alignment
- Strong pages mixed with dead cohorts -> expand winners, prune losers

---

## 10. Refresh and Pruning Rules

pSEO is a portfolio. Weak cohorts should not remain indexed forever.

### Refresh triggers
- data fields changed materially
- rankings decayed for high-value pages
- new FAQs, comparisons, or proof available
- competitor templates improved significantly

### Prune triggers
- page remains unindexed after repeated crawl opportunities
- page gets indexed but earns no meaningful impressions over a defined review window
- entity is outdated, discontinued, unsupported, or empty
- page falls below the minimum uniqueness threshold after data decay

### Prune actions
- enrich and keep indexed
- merge into a stronger page and 301 redirect
- noindex but keep live for UX reasons
- remove and return 410/301 if no longer useful

Document prune logic in the monitoring plan so the page system does not grow unchecked.

---

## 11. Anti-Cannibalization Rules

Programmatic SEO often fails because multiple templates target the same intent.

Prevent this by defining:
- one primary intent per template family
- one canonical page type for each keyword cluster
- clear boundaries between editorial, commercial, directory, and local pages

### Examples
- If `/integrations/{tool}` owns the integration-intent query, blog posts should support it, not compete with it.
- If `/services/{service}/{city}` exists, a generic blog post titled "Best {service} in {city}" may cannibalize unless intentionally differentiated.
- If comparison pages exist, category pages should target broader selection intent rather than exact "A vs B" intent.

When in doubt, map keywords to templates before launch.

---

## 12. Response Protocol for pSEO Requests

When the user asks about programmatic SEO:
1. Check whether the request is strategy, architecture, content system design, or performance diagnosis.
2. Qualify whether pSEO is appropriate using the criteria in Section 1.
3. Identify the page family and the search intent.
4. Build an opportunity map before recommending scale.
5. Define the data contract and template spec before discussing generation.
6. Recommend launch, indexation, and monitoring rules together -- not separately.
7. Warn clearly if the plan risks thin content, duplicate pages, cannibalization, or crawl waste.
8. Produce concrete deliverables: opportunity map, template spec, launch checklist, and monitoring plan.

---

## 13. What Good pSEO Recommendations Look Like

Strong pSEO recommendations are:
- specific about page families and search intent
- strict about data quality and uniqueness
- explicit about indexation and pruning
- realistic about operational overhead
- tied to business value, not just page count

Weak pSEO recommendations sound like:
- "Create 10,000 pages for long-tail traffic"
- "Use one template and swap keywords"
- "Index everything and see what ranks"
- "Fix duplication later"

If the recommendation would be dangerous without ongoing QA and pruning, say so directly.
