# Gate reviews

A gate passes when the user, having seen the artifact, says yes. Your job at a gate is to show what matters, judge what the stage skill cannot judge for itself, and record the decision with `production.py` (`approve`, `skip --reason`, `reopen`, `enable`; `status` shows where things stand). The stage skill often records an approval itself when the user approves in its session; check `status` before recording twice.

Each stage skill runs its own validators before it submits (copy deck, style lock, layout, image picks, design QC, export QC). When a check is in doubt, invoke that stage skill to re-run it rather than running its scripts from here, since they live in its folder.

## What each gate must prove

| Gate | Show | Judge before asking for a yes |
|---|---|---|
| concept | The proposition, the chosen route, the headline with its hook, the deck per piece | One message per asset; every claim has its proof or source; the brief's fixed lines are in the deck's `mandatory` list |
| style | `style/style-tile.png`, the pairing, the palette with its ratios | The look fits the audience and placement; brand colours kept as fills where they fail as text |
| layout | `layout/wireframes/sheet.png`, one tile per frame | A clear reading order per frame; each extra placement re-laid out for its shape, not stretched |
| imagery | Each pick beside the greybox it serves | Copy space where the type goes; products are real photos; nothing reads as stock or AI cliché |
| compose | The final renders (the sheet for sets) and `compose/review.md` | No rubric score at 2 or below; carousel slides and ad sizes read as one set |
| deliver | `deliver/qc.json`, the files per placement, `deliver/alt-text.md` | `qc.json` shows `ok`, or every failure is listed with a fix the user accepted; print files flagged for CMYK conversion when the printer needs it |

## Skips, refusals and reopens

- Soft gates can be skipped when the user chooses; record their reason with `skip`. Say what the next stage loses ("no layout gate means sizes are guessed at compose time"). A type-only design skips imagery. `compose` cannot be skipped: it is the design.
- When `production.py`, an image call or an export refuses, report its reasons as given.
- Over budget: offer the levers (fewer takes, the Codex image provider, user photos, a type-led design) before a higher cap; an accepted overage is `ack-budget --reason --cap-usd`.
- Before a `reopen`, tell the user what will need redoing: a new headline restales layout (copy length moves boxes) and everything after it.
- A stale stage is re-reviewed against the upstream change: when it still holds, `approve` it as is; when it does not, route to its skill, which reworks and resubmits.
