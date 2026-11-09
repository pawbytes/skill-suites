# Design review rubric

Score each frame 1–5 on every criterion; 3 ships, any criterion at 2 or below sends the frame back. Write the scores to `compose/review.md` as a table per frame, with one line on each criterion below 4. Criteria 5 and 6 come from the scripts, not the eye: 5 when `qc.py design` has no contrast warnings, 3 with warnings only, 1 on a fail; 6 likewise from the copy deck's word-budget result.

| # | Criterion | 5 | 3 | 1 |
|---|---|---|---|---|
| 1 | Hook strength | Specific, benefit- or curiosity-led; the first two words carry meaning | Clear but generic | Vague ("Tips for X") |
| 2 | Single message | One idea; everything supports it | One idea plus minor extras | Competing messages |
| 3 | Hierarchy | Blurred, the intended focal element still wins, then headline, then CTA | Order mostly right, one competitor | No entry point |
| 4 | Legibility at size | Headline readable on the thumbnail (feed size) and in context | Readable full size only | Unreadable at phone size |
| 5 | Contrast | QC clean; every line comfortably over 4.5:1 | Passes with marginal spots | Any line under 3:1 |
| 6 | Text density | Within the format's word budget | Up to 20% over | More than 50% over |
| 7 | CTA | One verb-first, specific CTA, prominent, the right mechanism for the placement | Present but weak | Missing, several, or a fake button |
| 8 | Brand fit | Fonts, colours, logo use and tone match the lock | Minor deviations | Off-brand |
| 9 | Alignment and grid | Every element on the grid, margins and spacing scale | One or two off | Random |
| 10 | Imagery | Specific to the message, sharp, copy space respected, no artefacts | Relevant but generic | Irrelevant, artefacts, soft |
| 11 | Platform fit | Right canvas, safe zones clear, border where required | Something near an edge | Under platform UI or wrong size |
| 12 | Accessibility | Facts not image-only, colour-blind safe, sizes above floors | Minor size issues | Information carried by colour alone |
| 13 | Set consistency | Slides or sizes read as one campaign | Small drift | Look like different campaigns |
| 14 | Truthfulness | Claims sourced, disclaimers by their claims, AI imagery noted | Minor gaps | Unsourced claims, fake urgency |

## Tests to run on the render

- **Squint:** look at the render small and soft (the `.thumb.png`, or the PNG blurred in your mind's eye at arm's length). The focal element must stay the strongest shape and groups must still read as groups.
- **Thumbnail:** at a third of full size (phone feed) the headline reads; for YouTube, at about 168 px wide; for a carousel cover, also as the 3:4 grid tile.
- **Greyscale:** headline and CTA still separate from the background without colour, which also covers most colour-blindness.
- **Three seconds** (posters, banners): after a three-second look, can you say the brand, the offer and the action?
- **Common faults:** two messages fighting; a headline shrunk to fit instead of cut; logo as the biggest thing; thin weights or tiny handles; drift between slides; generic stock or AI clichés; a disclaimer far from its claim.
