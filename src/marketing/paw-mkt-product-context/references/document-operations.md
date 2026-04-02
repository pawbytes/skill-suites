# Document Operations

Writing and updating the product marketing context document.

## Writing the Document

**Template:** See `./references/document-template.md` for the full 12-section structure.

**Save location:** `./.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md`

## After Writing

### 1. Summarize What Was Captured

Present sections completed, anything marked incomplete, what would strengthen it:

```
Saved to: ./.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md

Sections completed: 11 of 12
Incomplete: Section 9 (Customer Language) — only 2 quotes
Suggestion: The more verbatim phrases you add over time, the better every campaign gets.
```

### 2. Sync with Brand Context

If anything in `paw-mkt-product-context.md` expands or contradicts `brand-context.md`, update `brand-context.md` to stay consistent. They should agree, not diverge.

### 3. Explain Usage

```
Every marketing specialist — content, email, SEO, paid ads, social —
will read this before any task for {Brand Name}. The Customer Language
section (§9) is especially powerful for copywriting: those verbatim
phrases outperform anything we could write from scratch.

Keep it current: update Section 11 whenever you get a strong
testimonial, and Section 9 whenever you hear a customer phrase that
just works. Fresh context = better output from every specialist.
```

### 4. Recommend Next Step

| Situation | Recommendation |
|-----------|----------------|
| No SOSTAC plan yet | "Want to run a full SOSTAC plan to build your complete marketing strategy?" |
| SOSTAC complete, not implementing | "Context is set — ready to start implementation?" |
| Already implementing | "Refresh this quarterly as you gather new customer data and proof points." |

## Updating the Document

When the user asks to refresh or update:

1. **Read the current** `paw-mkt-product-context.md`
2. **Ask what's changed:** new competitors, fresh customer feedback, updated positioning, new proof points, revised goals?
3. **Edit only relevant sections** — don't regenerate the whole document
4. **Update the "Last updated" date**
5. **Add changelog if significant:** If changes are significant (new positioning, new primary persona), note a brief changelog at the top of the file

## Changelog Format

For significant changes, add to document header:

```markdown
---
last_updated: YYYY-MM-DD
next_review: YYYY-MM-DD
validation_status: current
---

## Recent Changes

- 2024-03-15: Updated primary persona based on sales data
- 2024-02-01: Added 3 new proof points from recent case studies
```