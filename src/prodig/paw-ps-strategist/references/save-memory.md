# Save Memory

Persist decisions and updates to sidecar memory following discipline rules.

## Save Operations

### 1. Save Product Decisions

**When:** After completing any strategic decision (shaping, scoping, packaging, handoff)

**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-decisions.md`

**Method:** Append new sections, update existing sections, maintain decision log

```markdown
## {Section Name} - Updated {date}

{Content}

---

### Decision Log Entry
| Date | Decision | Rationale |
|------|----------|-----------|
| {date} | {decision} | {why} |
```

### 2. Update Product Context

**When:** When new constraints or context are established

**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-context.md`

**Method:** Update relevant sections, append new context

```markdown
## Context Update - {date}

{New context or constraints}

### Active Constraints
- {constraint 1}
- {constraint 2}
```

### 3. Log Daily Activity

**When:** After every action

**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md`

**Method:** Append to existing file or create new

```markdown
## [Strategist] HH:MM - {Activity}

**Type:** {shaping/scoping/packaging/handoff}

**Input:**
- {intelligence consumed}

**Decisions:**
- {key decisions made}

**Output:**
- {artifacts produced}

**Files Written:**
- {path 1}
- {path 2}

**Next Steps:**
- {recommended next actions}
```

### 4. Update Sidecar Index

**When:** When status changes or work is complete

**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md`

**Method:** Update status section

```markdown
## Agent Status

| Agent | Status | Last Active |
|-------|--------|-------------|
| Strategist | {active/idle} | {date} |
```

## Write Sequence

For each capability completion:

1. **Write decisions** → `product-decisions.md`
2. **Update context** → `product-context.md`
3. **Log activity** → `daily/YYYY-MM-DD.md`
4. **Update index** → `index.md`

## Verification

After writing, verify:

- [ ] File exists at expected path
- [ ] Content is formatted correctly
- [ ] No overwrites of other agents' content
- [ ] Timestamps are accurate
- [ ] Decision log is updated

## Error Handling

If write fails:
1. Log error in daily file
2. Report to user
3. Do not proceed with handoff until memory is saved