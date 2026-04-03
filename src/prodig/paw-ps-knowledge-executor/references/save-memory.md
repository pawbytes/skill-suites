# Save Memory

Protocol for writing to sidecar memory to maintain context and enable continuity across sessions.

## Purpose

Ensure all significant work is persisted to memory so future sessions can build on progress and maintain context continuity.

## Memory Structure

```
.pawbytes/prodig-suites/memory/paw-ps-sidecar/
├── index.md                          # Memory index
├── curated/                          # Curated, processed intelligence
│   ├── product-context.md
│   ├── audience-intelligence.md
│   ├── output-standards.md
│   ├── product-types/
│   │   └── knowledge-products.md
│   └── product-decisions.md
├── artifacts/                        # Produced artifacts
│   └── {product-slug}/
├── daily/                            # Daily logs
│   └── YYYY-MM-DD.md
└── research/                         # Raw research notes (optional)
```

## Write Triggers

Write to memory when:

1. **Completing a significant artifact** — Course curriculum, ebook outline, membership framework
2. **Making important decisions** — Structure choices, scope boundaries, key design decisions
3. **Updating context** — New understanding of audience, product, or standards
4. **Ending a session** — Summary of what was accomplished
5. **Refining guidance** — New learnings about knowledge product types

## Write Locations

### 1. Artifacts

Write produced artifacts to:

```
{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/
```

**Naming Convention:**
- Courses: `{product-slug}-curriculum.md`, `{product-slug}-lessons.md`
- Ebooks: `{product-slug}-outline.md`, `{product-slug}-draft-{section}.md`
- Memberships: `{product-slug}-framework.md`, `{product-slug}-content-plan.md`

### 2. Product-Type Guidance

Refine and update knowledge product guidance:

```
{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types/knowledge-products.md
```

Update when:
- New patterns emerge from creation work
- Quality criteria are refined
- Common mistakes are identified
- Best practices are validated

### 3. Daily Log

Log daily activity to:

```
{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md
```

**Log Format:**

```markdown
# {YYYY-MM-DD}

## Activity Summary
Brief description of what was worked on.

## Artifacts Created
- {artifact name} — {path}

## Key Decisions
- {decision} — {rationale}

## Insights Captured
- {insight about knowledge products}

## Next Steps
- {what to do next}
```

## Update Protocol

### Updating the Index

After writing new files, update `index.md`:

```markdown
# Sidecar Memory Index

## Curated Intelligence
| File | Purpose | Last Updated |
|------|---------|--------------|
| product-context.md | Current product context | YYYY-MM-DD |
| audience-intelligence.md | Audience insights | YYYY-MM-DD |
| output-standards.md | Quality standards | YYYY-MM-DD |
| product-types/knowledge-products.md | Knowledge product guidance | YYYY-MM-DD |

## Active Artifacts
| Product | Type | Status | Path |
|---------|------|--------|------|
| {name} | course/ebook/membership | in-progress/complete | artifacts/{slug}/ |

## Recent Activity
| Date | Activity | Artifacts |
|------|----------|-----------|
| YYYY-MM-DD | {description} | {count} files |
```

### Updating Product-Type Guidance

When refining knowledge-product guidance:

1. Read current `curated/product-types/knowledge-products.md`
2. Identify what to add or update
3. Append new learnings with date
4. Keep file concise and actionable

**Example Addition:**

```markdown
## Refinement: {YYYY-MM-DD}

### New Learning
{What was learned from creation work}

### Pattern Identified
{Pattern that should be applied to future products}

### Quality Criteria Added
- {new criteria}
```

## Memory Discipline

### DO

- Write artifacts after completion
- Update index when adding files
- Log daily activity
- Refine guidance based on learnings
- Keep curated files focused and current

### DON'T

- Don't write raw notes to curated
- Don't duplicate information across files
- Don't let artifacts accumulate without indexing
- Don't skip daily logging
- Don't let guidance become stale

## Read Before Write

Before writing, always read the current state:

1. Read `index.md` to understand current state
2. Read relevant curated files
3. Check for existing artifacts in the same space
4. Avoid duplicating or overwriting without intention

## Continuity Guarantee

Following this protocol ensures:

- Future sessions can pick up where you left off
- Context is preserved across sessions
- Learnings are captured and applied
- Progress is visible and trackable
- Quality improves over time