# Stage 1: Gather Inputs

## Objective

Collect all available research and discovery outputs from the product workspace for synthesis into the product brief.

---

## Input Paths

Read from the product workspace in order of priority:

| Priority | Source | Expected Path |
|----------|--------|---------------|
| 1 | Discovery | `.pawbytes/prodig-suites/products/{product-slug}/product-context.md` |
| 2 | Market Intelligence | `.pawbytes/prodig-suites/products/{product-slug}/market-intelligence.md` |
| 3 | Audience Intelligence | `.pawbytes/prodig-suites/products/{product-slug}/audience-intelligence.md` |

---

## Procedure

### Step 1: Identify Product Workspace

1. Check for active product marker at `.pawbytes/prodig-suites/active-product.md`
2. Read the product slug from the marker file
3. Construct the product workspace path: `.pawbytes/prodig-suites/products/{product-slug}/`

If no active product marker exists:
- **Interactive mode:** Prompt user for product slug
- **Headless mode:** Scan `.pawbytes/prodig-suites/products/` for most recently modified directory

### Step 2: Scan for Input Files

For each expected input path:
1. Check if file exists
2. Record file status (found/not found)
3. If found, read and parse content

### Step 3: Extract Key Data

From each located file, extract:

**From product-context.md (Discovery):**
- Problem statement
- Product vision
- Success criteria
- Constraints and assumptions
- Stakeholder information

**From market-intelligence.md (Market Research):**
- Market size and opportunity
- Competitive landscape
- Market trends
- Positioning insights
- Risk factors

**From audience-intelligence.md (Audience Research):**
- Target personas
- User segments
- Pain points and needs
- Behavioral patterns
- Journey insights

---

## Output Artifact

Create an in-memory collection containing:

```markdown
## Input Summary

### Product: {product-slug}

| Source | Status | Key Sections |
|--------|--------|--------------|
| product-context.md | found/not found | [list sections] |
| market-intelligence.md | found/not found | [list sections] |
| audience-intelligence.md | found/not found | [list sections] |

### Content Preview
[Brief summary of each located file's contents]
```

---

## Progression Criteria

**Proceed to Stage 2 when:**
- At least 1 of 3 input files is located AND readable
- Content extraction completes without critical errors

**Block if:**
- No input files found
- Product workspace does not exist
- Located files are empty or unreadable

---

## Error Handling

| Error | Action |
|-------|--------|
| Product workspace not found | Interactive: prompt for correct slug; Headless: exit with error code 1 |
| No input files found | Interactive: prompt to run research skills first; Headless: exit with error code 1 |
| File read error | Log error, continue with available files, note in signal preservation |