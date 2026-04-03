# Memory Discipline

How this agent reads from and writes to shared memory.

## Read Locations

### Sidecar Index
**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md`

**Purpose:** Orientation file showing current product context and recent activity.

**When to read:** On every activation.

**What to extract:**
- Current active product (if any)
- Stage of development
- Recent decisions
- Key contacts and roles

### Product Context
**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-context.md`

**Purpose:** Deep context about the current product being explored.

**When to read:** When product context exists and is relevant to discovery.

**What to extract:**
- Problem space and opportunity
- Target audience hints
- Constraints and preferences
- Prior exploration notes

### Daily Logs
**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md`

**Purpose:** Session-by-session record of what was explored.

**When to read:** On activation to understand recent sessions; before writing to append.

**What to extract:**
- Ideas explored recently
- User preferences expressed
- Open threads to continue
- Decisions made

### Market Intelligence
**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/market-intelligence.md`

**Purpose:** Research synthesis about market and competition.

**When to read:** When discovery needs grounding in market reality.

**What to extract:**
- Competitive landscape
- Market gaps identified
- Audience insights

## Write Locations

### Daily Log
**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md`

**Purpose:** Capture session outputs and insights.

**When to write:** After every discovery session.

**Format:**
```markdown
# [YYYY-MM-DD] Discovery Session

## Session Type
[Idea expansion / Opportunity framing / Concept comparison]

## Ideas Explored
- [Idea 1]: [Brief description]
- [Idea 2]: [Brief description]
- [Idea 3]: [Brief description]

## User Signals
- Showed excitement about: [X]
- Hesitated on: [Y]
- Wants to explore further: [Z]

## Key Outputs
- [Any framed opportunities or ranked concepts]

## Next Steps
- [Recommended direction or action]

## Duration
[Approximate session length]
```

**Append pattern:** Read existing file, append new session with timestamp.

### Product Decisions
**Path:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-decisions.md`

**Purpose:** Record significant direction decisions.

**When to write:** When user commits to a concept direction.

**Format:**
```markdown
## [YYYY-MM-DD] Direction Chosen: [Concept Name]

**Decision:** [What was chosen and why]

**Concept summary:** [Brief description]

**Key characteristics:**
- [Characteristic 1]
- [Characteristic 2]

**Next validation needed:** [What to test or research]

**Confidence level:** [High/Medium/Low]
```

**Append pattern:** Read existing file, append new decision entry.

## Memory Hygiene

### Session Start Checklist
- [ ] Read index.md for orientation
- [ ] Check for product-context.md if relevant
- [ ] Review recent daily logs (last 3 days)
- [ ] Note any open threads to continue

### Session End Checklist
- [ ] Write daily log entry
- [ ] Append product decision if significant
- [ ] Note any context that should be preserved

### What NOT to Write
- Every word of conversation (summarize instead)
- Rejected ideas without reason (unless instructive)
- Premature decisions (wait for user confirmation)
- Duplicate information (check before writing)

## Handoff Protocol

When routing to another specialist:

1. Summarize session outputs
2. Write final state to daily log
3. Note what the next specialist should know
4. Include relevant file paths in handoff

Example handoff note:
```markdown
## Handoff to Research: [Concept Name]

**What was explored:** [Summary of discovery session]

**Why this direction:** [User's reasoning]

**Key questions to validate:**
- [Question 1]
- [Question 2]

**Context files:**
- Daily log: [path]
- Product context: [path]
```

## Privacy Considerations

- User ideas are theirs — don't share externally
- Write enough for continuity, not everything
- Respect sensitive information
- Ask before recording if unsure