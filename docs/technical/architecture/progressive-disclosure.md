# Progressive Disclosure

This document explains how skills load domain knowledge efficiently using the progressive disclosure pattern.

## The Problem

Skills contain extensive domain knowledge (frameworks, methodologies, checklists). Loading all content at once causes issues:

| Issue | Impact |
|-------|--------|
| Context bloat | Wastes context window with irrelevant content |
| Slower responses | More tokens to process |
| Reduced relevance | Harder to focus on user's specific situation |
| Higher costs | More tokens consumed |

## The Solution

**Progressive disclosure** loads only what's needed, when it's needed:

1. Read a lightweight index first
2. Match to user's situation
3. Load only matched files

```
┌────────────────────────────────────────────────────────────┐
│                    Without Progressive Disclosure           │
│                                                            │
│  Load ALL frameworks (500KB+) ──────► Process everything  │
│                                                            │
│  Result: Slow, bloated, expensive                          │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                    With Progressive Disclosure              │
│                                                            │
│  Load index (2KB) ──► Match ──► Load 1-2 files (10KB)     │
│                                                            │
│  Result: Fast, focused, efficient                          │
└────────────────────────────────────────────────────────────┘
```

## How It Works

### Two-Step Loading Process

```
┌─────────────────────────────────────┐
│      frameworks-index.csv           │
│      (~20-30 rows, ~2KB)            │
│                                     │
│  id,name,description,best_for,file │
│  ─────────────────────────────────  │
│  technical-audit,...,Site audits,...│
│  schema-markup,...,Structured data,.│
│  core-web-vitals,...,Page speed,... │
│  ...                                │
└────────────────┬────────────────────┘
                 │
                 │ 1. Read index first
                 │ 2. Match user situation to best_for column
                 │
                 ▼
┌─────────────────────────────────────┐
│   frameworks/specific-framework.md  │
│   (Full methodology, ~10-20KB)      │
│                                     │
│   # Technical Audit Framework       │
│                                     │
│   ## Process                        │
│   1. Crawl analysis                 │
│   2. Index check                    │
│   3. Speed audit                    │
│   ...                               │
└─────────────────────────────────────┘
```

### Framework Index Format

```csv
id,name,description,best_for,file,tags
technical-audit,Technical Audit,"Crawlability, indexation, speed",Site audits; diagnosing crawl issues,frameworks/technical-audit.md,"audit,technical"
schema-markup,Schema Markup,"JSON-LD examples for rich results",Implementing structured data,frameworks/schema-markup.md,"schema,json-ld"
core-web-vitals,Core Web Vitals,"LCP, CLS, INP optimization",Page speed audits; CWV failures,frameworks/core-web-vitals.md,"cwv,performance"
internal-linking,Internal Linking,"Hub-and-spoke model",Internal link audits; topic clusters,frameworks/internal-linking.md,"links,architecture"
```

### Required Columns

| Column | Purpose |
|--------|---------|
| `id` | Unique identifier |
| `name` | Display name |
| `description` | Brief description |
| `best_for` | When to use this framework (matching criteria) |
| `file` | Path to framework file |
| `tags` | Searchable keywords (comma-separated) |

## Implementation in Skills

### Reference Lookup Protocol

Skills define the progressive disclosure pattern in their SKILL.md:

```markdown
## Reference Lookup Protocol

This skill uses progressive disclosure to save tokens.

1. Read `./references/frameworks-index.csv` -- lightweight index (~24 rows)
2. Match the user's situation to the `best_for` column
3. Read ONLY the matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files
```

### Matching Logic

The matching process:

```
User Request: "My site is slow, I need to audit performance"

Step 1: Read frameworks-index.csv
        ↓
Step 2: Scan best_for column for matches
        - "Site audits" → technical-audit
        - "Page speed audits" → core-web-vitals
        ↓
Step 3: Load matched files
        - frameworks/technical-audit.md
        - frameworks/core-web-vitals.md
        ↓
Step 4: Execute methodology from loaded frameworks
```

## Directory Structure

```
skill-folder/
├── SKILL.md
│
└── references/
    ├── frameworks-index.csv      # Index file (required)
    │
    ├── frameworks/               # Framework files
    │   ├── framework-1.md
    │   ├── framework-2.md
    │   └── framework-3.md
    │
    ├── capability-1.md           # Direct-load references
    └── capability-2.md           # (not indexed)
```

### Frameworks vs Direct References

| Type | Indexed | When to Use |
|------|---------|-------------|
| **Framework** | Yes | Multiple methodologies, match by situation |
| **Direct Reference** | No | Always needed, single methodology |

**Frameworks** use progressive disclosure via index.
**Direct references** are always loaded when capability is matched.

## Example: SEO Skill

### Directory Structure

```
paw-mkt-seo/
├── SKILL.md
│
└── references/
    ├── frameworks-index.csv        # 24 frameworks indexed
    │
    ├── frameworks/
    │   ├── technical-audit.md
    │   ├── schema-markup.md
    │   ├── core-web-vitals.md
    │   ├── internal-linking.md
    │   ├── site-architecture.md
    │   ├── international-seo.md
    │   ├── javascript-seo.md
    │   ├── ai-overview-optimization.md
    │   ├── programmatic-*.md       # 12 pSEO frameworks
    │   └── ...
    │
    ├── capability-technical-seo.md  # Direct-load
    ├── capability-content-seo.md    # Direct-load
    ├── capability-local-seo.md      # Direct-load
    └── shared-patterns.md           # Direct-load
```

### Loading Sequence

```
User: "I need to optimize my Core Web Vitals"

1. Load capability-technical-seo.md (direct reference)
   - Identifies this as a performance issue
   - Points to core-web-vitals framework

2. Read frameworks-index.csv (~24 rows)
   - Match "Page speed audits; CWV failures" in best_for
   - Find: core-web-vitals

3. Load frameworks/core-web-vitals.md
   - Full methodology for LCP, CLS, INP
   - Optimization steps
   - Testing tools

4. Execute framework methodology
   - Audit current metrics
   - Identify issues
   - Recommend fixes

Result: Only 2 files loaded (index + 1 framework)
        Instead of all 24 frameworks
```

## Best Practices

### For Framework Index

1. **Keep rows concise** — Aim for 10-30 rows
2. **Use specific `best_for`** — Clear matching criteria
3. **Tag appropriately** — Enable discovery via keywords
4. **Test matching** — Verify best_for values match real queries

### For Framework Files

1. **Include process** — Step-by-step methodology
2. **Add checklists** — Actionable items
3. **Provide examples** — Concrete scenarios
4. **Define output** — What the framework produces

```markdown
# Framework Name

## When to Use
Specific scenarios where this framework applies.

## Process
1. Step one
2. Step two
3. Step three

## Checklist
- [ ] Item 1
- [ ] Item 2

## Examples
Concrete examples of the framework in action.

## Output
What this framework produces when executed.
```

### For Skill Authors

1. **Never bulk-load** — Always use index first
2. **Document the protocol** — Include Reference Lookup Protocol section
3. **Test with real queries** — Verify matching works
4. **Keep index small** — Split if over 30 rows

## Anti-Patterns to Avoid

### Bulk Loading

```markdown
❌ WRONG:

Read ALL files in ./references/frameworks/
```

```markdown
✅ CORRECT:

Read ./references/frameworks-index.csv first,
then load only matched files.
```

### Missing Index

```markdown
❌ WRONG:

references/
└── frameworks/
    ├── framework-1.md
    ├── framework-2.md
    └── framework-3.md
    # No index file!
```

```markdown
✅ CORRECT:

references/
├── frameworks-index.csv    # Index required
└── frameworks/
    ├── framework-1.md
    ├── framework-2.md
    └── framework-3.md
```

### Vague best_for

```csv
❌ WRONG:
id,name,best_for
audit,Audit,when you need to check things
```

```csv
✅ CORRECT:
id,name,best_for
technical-audit,Technical Audit,Site audits; diagnosing crawl/index/speed issues; quarterly health checks
```

## Token Savings Example

**Scenario:** User needs Core Web Vitals optimization

| Approach | Files Loaded | Approximate Tokens |
|----------|--------------|-------------------|
| Bulk load all | 24 frameworks | ~150,000 tokens |
| Progressive disclosure | 1 index + 1 framework | ~8,000 tokens |
| **Savings** | — | **~95% reduction** |

## Summary

Progressive disclosure is a core pattern for efficient skill execution:

1. **Index first** — Read `frameworks-index.csv`
2. **Match situation** — Use `best_for` column
3. **Load selectively** — Only matched files
4. **Never bulk-load** — Always follow the pattern

This pattern keeps context lean, responses focused, and costs low.