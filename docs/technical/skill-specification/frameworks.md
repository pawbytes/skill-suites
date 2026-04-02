# Framework Files

## Purpose

Frameworks are domain-specific methodologies loaded progressively during skill execution. They provide structured approaches to specific tasks without loading all domain knowledge at once.

## Why Progressive Disclosure?

Loading all domain knowledge at once:
- Wastes context window
- Slows response time
- Reduces relevance

Progressive disclosure solution:
- Load only what's needed
- When it's needed
- Keep context lean and focused

## Structure

```
references/
├── frameworks-index.csv    # Index file (required for frameworks)
└── frameworks/
    ├── framework-1.md
    ├── framework-2.md
    └── framework-3.md
```

## Framework Index (CSV)

The `frameworks-index.csv` is the lookup table for progressive disclosure. Always read first.

### Required Columns

| Column | Purpose | Example |
|--------|---------|---------|
| `id` | Unique identifier | `technical-audit` |
| `name` | Display name | `Technical Audit` |
| `description` | Brief description | `Crawlability, indexation, speed...` |
| `best_for` | When to use this framework | `Site audits; diagnosing crawl issues` |
| `file` | Path to framework file | `frameworks/technical-audit.md` |
| `tags` | Searchable tags (comma-separated) | `"audit, crawlability, indexation"` |

### Example CSV

```csv
id,name,description,best_for,file,tags
technical-audit,Technical Audit,"Crawlability, indexation, speed, mobile, security",Site audits; diagnosing crawl/index/speed issues,frameworks/technical-audit.md,"audit, crawlability, indexation"
schema-markup,Schema Markup,"JSON-LD examples for FAQ, HowTo, Product, Review",Implementing or auditing structured data,frameworks/schema-markup.md,"schema, json-ld, structured-data"
core-web-vitals,Core Web Vitals,"LCP, CLS, INP targets and optimization fixes",Page speed audits; diagnosing CWV failures,frameworks/core-web-vitals.md,"cwv, lcp, cls, performance"
```

### CSV Best Practices

1. **Keep index concise** - Aim for 10-30 rows maximum
2. **Use specific `best_for`** - Helps matching accuracy
3. **Tag appropriately** - Enables discovery
4. **Use quotes for commas** - Fields with commas must be quoted

## Framework File Format

Each framework file follows a consistent structure:

```markdown
# Framework Name

## When to Use
Specific scenarios where this framework applies.

## Prerequisites
Any requirements before using this framework.

## Process
Step-by-step methodology.

1. **Step 1**: Description
2. **Step 2**: Description
3. **Step 3**: Description

## Checklist
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

## Examples
Concrete examples of application.

## Output
What this framework produces.

## Related Frameworks
Links to related frameworks.
```

### Example Framework

```markdown
# Technical Audit

## When to Use
- Quarterly SEO health checks
- Diagnosing crawl or indexation issues
- After site migrations
- Core Web Vitals failures

## Prerequisites
- Site URL or domain access
- Google Search Console access (recommended)

## Process

1. **Crawlability Check**
   - Test robots.txt for unintended blocks
   - Verify XML sitemap coverage
   - Check for crawl budget waste

2. **Indexation Audit**
   - Compare indexed vs submitted pages
   - Identify orphan pages
   - Check canonical implementation

3. **Performance Audit**
   - Measure Core Web Vitals
   - Identify render-blocking resources
   - Check image optimization

## Checklist
- [ ] Robots.txt reviewed
- [ ] XML sitemap validated
- [ ] Indexed pages compared to submitted
- [ ] Core Web Vitals measured
- [ ] Internal linking audited

## Output
- Prioritized issue list (P1/P2/P3)
- Specific fix recommendations
- Expected impact per fix
```

## Progressive Loading Protocol

Skills must follow this protocol:

```
1. Read frameworks-index.csv
   │
   │  (~10-30 rows, minimal token cost)
   │
   ▼
2. Match user situation to best_for column
   │
   │  Find rows where best_for matches user context
   │
   ▼
3. Load ONLY matched framework files
   │
   │  Read specific file(s) from frameworks/
   │
   ▼
4. Execute methodology
   │
   │  Follow the framework's process
   │
   ▼
5. Never bulk-read all frameworks
```

## Implementation in SKILL.md

Include the Reference Lookup Protocol section:

```markdown
## Reference Lookup Protocol

This skill uses progressive disclosure to save tokens.

1. Read `./references/frameworks-index.csv` -- lightweight index (~24 rows)
2. Match the user's situation to the `best_for` column
3. Read ONLY the matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files

General references (best-practices.md, shared-patterns.md) are read directly -- not indexed.
```

## When to Use Frameworks

| Use Frameworks When | Don't Use Frameworks When |
|---------------------|---------------------------|
| Multiple methodologies exist | Single approach applies |
| Domain has structured processes | Content is reference-only |
| Selective loading is valuable | All content is always needed |
| 5+ distinct approaches exist | < 3 distinct approaches |

## Real-World Example

The `paw-mkt-seo` skill has 24 frameworks covering:

| Domain | Frameworks |
|--------|------------|
| Technical SEO | technical-audit, schema-markup, core-web-vitals, internal-linking, site-architecture, sitemap-robots, international-seo, javascript-seo |
| Programmatic SEO | qualification, page-archetypes, opportunity-mapping, data-contract, template-spec, internal-linking, indexation, launch-strategy, monitoring, refresh-pruning, anti-cannibalization, response-protocol, good-recommendations |
| Content SEO | ai-overview-optimization |

The CSV index allows the skill to load only relevant frameworks based on user context.