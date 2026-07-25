# Completeness Rules

Run after structured extraction, before writing `brief.md`. Output feeds `completenessReport` and (in autonomous mode) `assumptions[]`.

## Scoring model

Start at `1.0`. Subtract per unresolved gap:

| Severity | Weight | Examples |
|----------|--------|----------|
| **critical** | −0.25 each | Missing `clientName`, `projectDescription`, or empty `requirements` |
| **high** | −0.15 each | Missing `budget` (pricing), hard `timeline` deadline (RFP), missing `decisionMaker` for enterprise deal |
| **medium** | −0.10 each | Thin `clientContext`, no `constraints` when integration mentioned, vague scope |
| **low** | −0.05 each | Missing optional enrichment, no `successCriteria` for scoping |

Floor at `0.0`. Round `score` to two decimals.

## `readyForPipeline`

`true` when:

- No **critical** gaps remain unresolved, AND
- `score` ≥ `0.60`, AND
- Either all **high** gaps are resolved OR (autonomous mode AND each high gap has a matching `assumptions[]` entry)

`false` otherwise — orchestrator should clarify (guided) or surface assumptions prominently (autonomous).

## Gap catalog

Check each field; emit a gap object when missing or too thin:

```yaml
- field: budget
  severity: high
  message: "Budget not stated — pricing cannot calibrate"
  resolved: false
  suggestion: "Ask: 'What's the budget range or approval band for this work?'"
```

### Universal checks (all proposal types)

| Field | Gap if | Default severity |
|-------|--------|------------------|
| `clientName` | empty | critical |
| `projectDescription` | empty or &lt; 40 chars | critical |
| `requirements` | empty array | critical |
| `clientContext` | empty | medium |
| `budget` | null/empty | high |
| `timeline` | null/empty | medium |
| `decisionMaker` | null/empty | medium |

### Type-specific checks

**pitch**

| Field | Gap if | Severity |
|-------|--------|----------|
| Problem/outcome clarity | `projectDescription` lacks identifiable pain + outcome | high |
| `budget` | missing | high |

**rfp**

| Field | Gap if | Severity |
|-------|--------|----------|
| Submission deadline | not in `timeline` or `constraints` | critical |
| `complianceRequirements` | empty when source mentions compliance/evaluation | high |
| `requirements` | &lt; 3 items for large RFP paste | medium |

**scoping**

| Field | Gap if | Severity |
|-------|--------|----------|
| `deliverables` | empty | high |
| `milestones` | empty | medium |
| `successCriteria` | empty | medium |

## Thin-brief detection

Flag `thinBrief: true` in `completenessReport` when:

- Source text &lt; 100 words AND `score` &lt; 0.70, OR
- More than 3 **high** or **critical** gaps

Orchestrator uses this to trigger clarification in guided mode.

## Guided vs autonomous

### Guided mode

1. Present gaps grouped by severity (critical → high → medium → low).
2. Ask targeted questions — one cluster at a time, not a form dump.
3. Update `brief.md` fields and set `resolved: true` on cleared gaps.
4. Re-score after each clarification round.
5. Do **not** populate `assumptions[]` unless the user explicitly says "assume X".

### Autonomous mode

For every gap that remains after extraction:

1. Add `assumptions[]` entry with conservative `assumedValue`.
2. Set `rationale` citing what was missing and why the assumption is reasonable.
3. Keep the gap in `completenessReport.gaps[]` with `resolved: false` but note `assumedInAutonomous: true`.
4. Never assume budget as a precise number — use ranges or "TBD — priced at standard rate card".

**Forbidden autonomous assumptions:** legal/compliance commitments, guaranteed timelines without any anchor, client names not mentioned in source.

## Completeness report shape

```yaml
completenessReport:
  score: 0.72
  readyForPipeline: true
  thinBrief: false
  gapCount: 3
  criticalCount: 0
  highCount: 1
  mediumCount: 2
  lowCount: 0
  gaps:
    - field: budget
      severity: high
      message: "..."
      resolved: false
      assumedInAutonomous: true
      suggestion: "..."
```

## Re-intake / merge

When updating an existing `brief.md`:

1. Load prior frontmatter.
2. Merge new extraction — new non-empty fields override; arrays union with dedup.
3. Re-run completeness on merged state.
4. Append to `intakeHistory` in frontmatter (optional): `{date, inputType, sourceInputRef}`.
