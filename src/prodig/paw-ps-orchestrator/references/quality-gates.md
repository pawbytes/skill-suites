# Quality Gates

## Purpose

Define quality checkpoints that must be passed before proceeding to certain stages.

## Gate Philosophy

Quality gates exist to:
- Prevent premature execution
- Ensure sufficient context for good outputs
- Catch issues early when they're cheaper to fix
- Maintain product quality across the journey

## Gate Structure

Each gate has:
- **Trigger**: When the gate is checked
- **Requirements**: What must be true to pass
- **Bypass conditions**: When the gate can be skipped
- **Consequence**: What happens if failed

## Gates

### Gate 1: Discovery → Research

**Trigger:** User wants to proceed to research stage

**Requirements:**
- [ ] Product concept clearly stated
- [ ] Product type identified (or exploration scope defined)
- [ ] Initial goals or outcomes mentioned

**Bypass:** Never bypass — minimum context required

**Failure action:** Route to discovery agent for concept refinement

---

### Gate 2: Research → Audience

**Trigger:** User wants to proceed to audience stage

**Requirements:**
- [ ] market-intelligence.md exists OR user explicitly skips research
- [ ] Basic market understanding documented OR acknowledgment that proceeding without it

**Bypass:** Allowed if user explicitly chooses to skip research

**Failure action:** Offer research agent or allow bypass with acknowledgment

**Bypass message:**
```markdown
"Research is recommended but optional. Proceeding without it means:
- Less validated market understanding
- Higher risk of misaligned product

Proceed anyway?"
```

---

### Gate 3: Audience → Strategy

**Trigger:** User wants to proceed to strategy stage

**Requirements:**
- [ ] Target customer has been defined (even if basic)
- [ ] Problem/pain points identified OR acknowledgment to proceed

**Bypass:** Allowed with acknowledgment

**Failure action:** Offer audience agent or allow bypass

---

### Gate 4: Strategy → Execution

**Trigger:** User wants to proceed to execution

**Requirements:**
- [ ] Product brief exists OR equivalent context captured
- [ ] Scope defined (what's in, what's out)
- [ ] Product family confirmed
- [ ] Key decisions logged

**Bypass:** NOT RECOMMENDED — execution without strategy produces inconsistent outputs

**Failure action:** Route to strategist for brief creation

**Warning message:**
```markdown
⚠️ **Strategy gate not passed**

Execution without a clear product brief typically results in:
- Inconsistent outputs
- Scope creep
- Rework later

Recommended: Complete strategy first (15-30 min).

Override and proceed anyway?
```

---

### Gate 5: Execution → Packaging

**Trigger:** User wants to package the product

**Requirements:**
- [ ] Core artifacts created (varies by product type)
- [ ] Execution stage marked substantially complete

**Minimum artifacts by type:**

| Product Type | Minimum Artifacts |
|--------------|-------------------|
| Knowledge | Curriculum + module outlines OR chapter structure |
| Template | Template files + usage guide |
| Software | Feature spec + user flow OR PRD-lite |
| Service | Offer structure + deliverable list |

**Bypass:** Not recommended — incomplete products can't be properly packaged

**Failure action:** Show missing artifacts, offer to continue execution

---

### Gate 6: Packaging → Readiness

**Trigger:** User wants readiness review

**Requirements:**
- [ ] Product bundle exists
- [ ] All artifacts organized in bundle structure

**Bypass:** Not applicable — packaging is required for readiness check

**Failure action:** Route to package assembler workflow

---

### Gate 7: Readiness → Launch

**Trigger:** User asks if product is ready to sell

**Requirements:**
- [ ] Readiness report shows "sellable-ready" OR user accepts current state
- [ ] Critical gaps resolved OR explicitly accepted

**Bypass:** User can always proceed — readiness is advisory

**Note:** Launch/marketing is OUT OF SCOPE for Prodig Suites

## Gate Enforcement

### Strict vs Advisory Gates

| Gate | Type | Reason |
|------|------|--------|
| Discovery → Research | **Strict** | Minimum context required |
| Research → Audience | Advisory | Can skip research |
| Audience → Strategy | Advisory | Can skip audience |
| Strategy → Execution | **Strict** | Prevents poor outputs |
| Execution → Packaging | **Strict** | Can't package nothing |
| Packaging → Readiness | **Strict** | Packaging required for review |
| Readiness → Launch | Advisory | User decision |

### Strict Gate Behavior

For strict gates (Strategy → Execution):

```markdown
**Gate Check: Strategy → Execution**

❌ Not passed: Product brief missing

This gate is strict — execution requires strategy.

Options:
1. Create brief now (→ Strategist) — Recommended
2. Override (not recommended) — May produce poor outputs
```

### Advisory Gate Behavior

For advisory gates:

```markdown
**Gate Check: Research → Audience**

⚠️ Recommended but optional: Research not complete

You can proceed, but audience profiles may be less grounded.

Proceed to audience discovery?
```

## Quality Criteria by Stage

### Discovery Quality

- Concept is specific enough to evaluate
- Not just "make something" or "I want to create"
- Direction is identifiable

### Research Quality

- At least 3 competitors analyzed OR reason documented
- Demand signals captured OR gap statement
- Key findings documented

### Audience Quality

- Primary persona defined
- At least 3 pain points or problems identified
- Some language/messaging captured

### Strategy Quality

- Clear product definition
- Scope boundaries stated
- Decisions logged with rationale
- Executor can understand what to build

### Execution Quality

- Artifacts are complete enough for product type
- Outputs match strategy intent
- No placeholder or TODO content

### Packaging Quality

- Files organized logically
- Naming conventions followed
- Ready for delivery

### Readiness Quality

- No critical gaps
- Sellable-ready criteria met OR documented exceptions

## Gate Bypass Logging

When a gate is bypassed, log it:

```markdown
### {timestamp} - Gate Bypass

**Gate:** {stage} → {stage}
**Reason:** {user choice}
**Acknowledgment:** User accepted risks

**Implications:**
- {what this means for downstream work}
```

This ensures future agents understand why certain context may be missing.