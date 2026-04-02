# Template Spec

Each template family needs a written spec before content generation.

Include these sections in the spec:

### Intent and query mapping
- Primary keyword pattern
- Supporting modifiers
- Search intent
- Closest competing page type in the current site
- Canonical page for this intent cluster

### URL pattern
Keep URLs predictable, readable, and stable.

Examples:
- `/integrations/salesforce`
- `/services/roof-repair/austin`
- `/directory/accounting-software/quickbooks`

Avoid parameter-heavy or auto-generated slugs with IDs unless required.

### On-page block requirements
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

### Minimum uniqueness threshold
Every template family should define what counts as enough unique value.

Example threshold:
- unique intro paragraph
- at least 3 entity-specific bullets or facts
- one differentiated section that could not be reused unchanged on sibling pages
- at least 3 internal links chosen by relationship logic
- FAQ answers customized to the entity or location

If the page cannot meet the threshold, do not index it.
