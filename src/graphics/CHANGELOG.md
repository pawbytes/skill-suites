# Changelog — PawBytes Graphics Suite

## 0.1.0 — 2026-11-05

- New suite `paw-design`: Iris the Art Director plus six stage skills (concept, style, layout, imagery, compose, deliver) and setup. Projects land in `paw-suites/graphics/<slug>/`.
- Gated pipeline with eight format profiles (social post, carousel, story, poster, flyer, banner, ad set, thumbnail) and placements from a researched catalog of 66 platform and print specs (sizes, safe zones, keep-clear areas, file caps, bleed, dpi, per-class type floors and word budgets), researched 2026-11-04.
- Hooks: 22 headline formulas, 16 visual hooks and carousel cover, swipe-cue and closer patterns in `paw-design-concept/assets/hooks.json`; `hooks.py suggest` ranks them per goal and format and `hooks.py lint` checks a headline against the research (word band, caps, question covers, filler openers). `copydeck.py` validates the copy deck's schema, hook ids and word budgets.
- Style: 29 graphic styles and 25 Google Fonts pairings; `styles.py` locks a style with brand overrides, refuses palettes that fail contrast, writes `tokens.css` and a style tile.
- Layout: `frames.py` validates layouts against safe zones and the copy deck, writes greybox wireframes with the real copy at the locked type sizes, scaffolds design HTML, and tiles contact sheets.
- Imagery: text-free plates on fal.ai or the Codex CLI (shared `fal.py` and `codex_image.py`, adapted from paw-vid); `assets.py` imports user photos untouched and checks every slot's resolution and crop.
- Render and QC: `render.py` renders HTML to PNG, JPEG within a file cap, or print PDF at trim plus bleed, and measures every text element (box, smallest size, overflow, font fallback, contrast against the pixels behind it); `qc.py` checks renders and exports against the placement spec, including the 1px border display ads need.
- Delivery: `export.py` exports every frame per placement, merges LinkedIn document PDFs, writes manifest and QC reports, and zips the package.
- Shared files are canonical in `_shared/` and bundled per skill by `_shared/sync.py`; `tests/` covers the manifest, catalog contracts, shared copies and an end-to-end pipeline with real renders.
