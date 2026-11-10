# Adapting to a new placement

A late size is new design work on one frame, not a resize. The approved frames stay untouched, so nothing is reopened; the new frame goes through the same checks they did.

1. Add the placement: `production.py set --project {project} placements=<existing,...,new>` (keeps the history honest). `specs.py show <new>` gives size, safe zone, class floors and keep-clear areas.
2. Add a frame per piece to `layout/layout.json`, id `<piece>--<new-placement>`, laid out for the new shape from the master's elements. Wide strips (728×90, 970×90, 468×60) run left to right: logo, message, CTA, one line of copy. Columns (160×600, 300×600) stack image, message, CTA, logo. Rectangles keep image or colour field, headline, CTA button and a corner logo. Mobile banners (320×50, 320×100) keep message and CTA only. Square, 4:5 and 9:16 versions keep the type stack and the image's focal point and move the copy band to where the shape has room, inside its safe zone. Same copy refs; cut a field only when the shape cannot carry it, never shrink type below the class floor, and note the cut on the frame (`"note": "subhead dropped at 320x50"`).
3. `frames.py validate` the layout, then `frames.py scaffold` the new frame into `compose/<frame>/design.html` and carry over the master's design decisions (colours, scrims, treatment, shapes) by copying its `<style>` rules and adjusting positions.
4. Images: compare each picked image's pixels (in `imagery/assets.json`) with the new box at export size. When it would be upscaled more than 1.5× or lose its subject at that crop, invoke the `paw-design-imagery` skill to make and pick a variant under a new name.
5. Render with `--measure`, `qc.py design` until clean, look at it beside the master, then `export.py run --project {project} --frame <frame>`, which merges into the existing reports.

Show the user the new frame beside the master before exporting the rest of a set.
