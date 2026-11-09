# Building designs in HTML

## What the renderer and QC rely on

- `<meta name="canvas" content="1080x1350">` sets the viewport; print uses `content="297x420mm"` plus `<meta name="bleed" content="3mm">`, and the page is authored at trim plus bleed (`html, body` sized in mm), with the art running to the outer edge and type kept inside the safe margin. The scaffold writes both.
- Every text element, the logo and the CTA carry `data-role` and `data-id`. `render.py measure` reads only those: boxes, the smallest font size inside, colour, overflow, whether the font rendered, and contrast against the pixels behind once text is hidden. Text without a `data-role` is invisible to QC, so nothing gets set outside one.
- Text colour must be a real colour on the `data-role` element or its children. Gradient or `background-clip: text` lettering cannot be measured; QC flags it for an eye check, so keep it to display words over flat fields.
- Paths are relative to the design file (`../../imagery/...`, `../../style/tokens.css`). Everything is local except Google Fonts, which `tokens.css` imports; a render with `fonts_missing` is wrong, not slightly off.
- Keep it static: no scripts that change layout after load, no animations (the renderer freezes them), no external images.
- Element boxes keep `box-sizing: border-box`. Text that must not wrap gets `white-space: nowrap` deliberately, never as a fix for overflow.

## Type

- Headlines: `text-wrap: balance`, tight leading (0.95–1.1), slight negative tracking at large sizes (−0.01 to −0.03 em), weights 700+. Body: `text-wrap: pretty`, leading 1.3–1.45, 20–40 characters per line on portrait social, 45–75 in print columns.
- All caps only for kickers and labels, tracked +0.05–0.12 em (`--caps-tracking`).
- Real punctuation: curly quotes, en and em dashes, the ellipsis character, ™ and ®. No widows in headlines.
- Script and decorative faces for a word or two, never dates, prices or the CTA.

## Type over images

Try in this order, then measure, because only the pixels behind each line decide:

| Technique | CSS sketch |
|---|---|
| Composition: type in the plate's copy space | none |
| Gradient scrim from the type's edge | `background: linear-gradient(to top, rgba(0,0,0,.65), rgba(0,0,0,0) 55%)` on a shape under the text |
| Full overlay on a busy photo | `background: rgba(0,0,0,.35)` to `.55` over the image |
| Blur plate | `backdrop-filter: blur(16px); background: rgba(255,255,255,.6)` |
| Solid panel or strip in a palette colour | a `shape` element behind the text block |
| Text shadow or stroke | supplementary only (`text-shadow: 0 2px 12px rgba(0,0,0,.5)`; `paint-order: stroke` for thumbnail outlines) |

## Patterns worth knowing

- Contact shadow under a cutout: an absolutely positioned ellipse, `background: radial-gradient(closest-side, rgba(0,0,0,.3), transparent); filter: blur(6px)`.
- Unifying mismatched plates: a full-size `shape` in a palette colour with `mix-blend-mode: multiply` at low opacity.
- Duotone: the image in greyscale (`filter: grayscale(1) contrast(1.1)`) under a colour layer with `mix-blend-mode: screen` or `multiply`.
- Grain: an inline SVG `feTurbulence` noise as a background at 5–8% opacity; check banner file weight after.
- Swipe cue: an arrow chip inside the right margin, or a shape whose box runs past the right edge and continues on the next slide.
- Charts: build bars, dots and axes from the deck's real numbers in HTML or inline SVG, label every series, and keep colour from carrying meaning alone.
- Pixel art: `image-rendering: pixelated`.

## Placement specifics

- Display ads: a 1px border in `--muted` or `--ink` around the canvas whenever the background is white or black (QC checks the edge); the CTA is a filled button, the highest-contrast element, in the same position on every size; no fake play, close or download buttons.
- Platform ads (Meta, TikTok, LinkedIn): no button-shaped CTA in the image.
- Thumbnails: nothing in the bottom-right corner; text over photo gets a thick outline or a panel.
- Print: sizes in `pt` or `mm` read naturally; large solid black fields are rich black at the printer, text stays pure black (`#000`). Playwright's PDF is RGB; deliver flags the CMYK conversion.
- Right-to-left copy: `dir="rtl"` on the `html` element and the layout mirrored.
