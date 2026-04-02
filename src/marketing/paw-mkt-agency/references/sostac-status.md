# SOSTAC Status Check

## Purpose
Determine which SOSTAC phases are complete and identify next phase.

## Phase Files

Check for existence AND content in `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/`:

| Phase | File | Complete When |
|---|---|---|
| Situation Analysis | `01-situation.md` | File exists with content beyond template header |
| Objectives | `02-objectives.md` | File exists with content beyond template header |
| Strategy | `03-strategy.md` | File exists with content beyond template header |
| Tactics | `04-tactics.md` | File exists with content beyond template header |
| Action | `05-action.md` | File exists with content beyond template header |
| Control | `06-control.md` | File exists with content beyond template header |

## Status Interpretation

| Status | Meaning |
|---|---|---|
| 0/6 complete | Brand new to planning. Start from Situation Analysis |
| 1-5/6 complete | Plan in progress. Resume at next incomplete phase |
| 6/6 complete | Plan ready for implementation |

## Using sostac/README.md

If `sostac/README.md` exists:
- Contains status table maintained by SOSTAC skill
- Use as primary status source
- Verify against actual file existence

## Determining Next Phase

SOSTAC phases are strictly sequential:
- Next phase = first one (by number) that is not yet complete
- Never skip phases
- If user wants to jump ahead, explain dependency and recommend in-order completion

## Quick Check Command

```
Check: ./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/
  - 01-situation.md exists? content beyond header?
  - 02-objectives.md exists? content beyond header?
  - ... (repeat for all 6)
Result: X/6 complete, next phase: {phase name}
```