# Layout patterns

Distilled from the 2026-11 research (NN/g hierarchy and scanning studies, OAAA, Meta, TikTok, Google and IAB creative specs, practitioner grids). Safe zones and keep-clear areas live in `specs.py show <id>`; this file is about composition.

## Hierarchy

- One focal element, then headline, then CTA; the logo is present but outside that ranking. At most three type sizes and two large elements per canvas.
- Sparse canvases (posters, ads, banners) read in a Z: brand or hook top-left, across, diagonally through the focal image, CTA bottom-right at the end of the Z. Text-heavy canvases read in an F: front-load headings and line starts. Mirror both for right-to-left languages.
- Place the focal point on a third; put copy in the opposite third. Content sits slightly above the geometric centre; bottom margins slightly larger than top.
- Related items sit closer than unrelated ones: space between groups at least twice the space within them. One dominant alignment per canvas; centre only three short lines or fewer.
- Margins: 6–9% of the width on social (60–100 px at 1080), at least 8–12 px on a 300×250, 3–5 mm inside the trim on print (10 mm on A2 and up). Gaps and padding on one spacing scale (8, 16, 24, 32, 48, 64, 96 at 1080).

## Patterns by format

| Format | Patterns that work | Watch |
|---|---|---|
| Social post 4:5 | Type top, image below; image full-bleed with a copy band; split left/right; oversized type only | Keep key content inside the central 3:4 band (the profile grid crops about 34 px a side) |
| Carousel | One template for every slide: same grid, margins, type sizes and colour roles; cover with the promise, body slides one idea each, closer with the CTA | A swipe cue on the cover (arrow chip at the right edge, progress "1/8", or an element crossing into slide 2); a small brand mark on every slide |
| Story / 9:16 | One central column inside the safe band; headline upper-middle | Meta keeps top 14%, bottom 35% and 6% sides clear (40% bottom with a disclaimer); TikTok adds a right-hand button rail. Build to the strictest platform when one master serves several. No CTA in the bottom zone, where the platform's own sits |
| Poster | Big headline band top or centre, one focal image, the info stack (what, when, where, how) in a clear block, QR and URL bottom | Size type for the viewing distance: about 0.83 cm of cap height per metre (1 inch per 10 ft); at 3 m, caps of 2.5 cm or more. Set poster headlines with `size_pt` |
| Flyer | Front: poster logic, Z pattern. Back: headings and bullets in an F, how-to-act block, address and logo | 3 mm bleed, 3–5 mm safe margin, body 9–12 pt |
| Web hero / cover banners | Copy on one side, image on the other; text inside the central band responsive crops keep | Covers have avatars and buttons overlapping corners; check `notes` in the spec |
| Display ads | Logo, message, CTA in the same relative positions on every size | Re-lay out per shape (below); a 1px contrasting border when the background is white or black |
| YouTube thumbnail | One close-up subject on a third, 3–7 words of type opposite, thick outline on type over photos | Bottom-right keeps clear for the timestamp; avoid white backgrounds and YouTube red |
| LinkedIn document | Single column, big type (24 pt-equivalent body at 1080), page numbers | Same size on every page; nothing confidential (viewers can download it) |

## Re-laying out a set of sizes

Each placement of a different shape gets its own frame, laid out for that shape, because a 728×90 is a strip and a 300×600 a column; scaling or cropping the master breaks both.

- Leaderboards and other wide strips (728×90, 970×90, 468×60): left to right, logo | message | CTA, one line of copy.
- Skyscrapers and half-pages (160×600, 300×600): vertical stack, image top, message, CTA low, logo bottom.
- Rectangles (300×250, 336×280): image or colour field, headline, CTA button bottom-left or bottom-centre, logo in a corner.
- Mobile banners (320×50, 320×100): message and CTA only; drop the subhead and the image.
- Square, 4:5 and 9:16 versions of a social master: keep the type stack and the image's focal point, move the copy band to where each shape has room, and honour each placement's safe zone.

Keep the copy identical across sizes unless a size cannot carry it; then cut, never shrink below the class floor, and note the cut in the frame (`"note": "subhead dropped at 320x50"`).
