# Brand and custom styles

## From brand guidelines

Read the guideline PDF, logo files and any font files in `{project}/brand/`. Pick the catalog look closest to the brand's character as the base (it supplies layout traits, imagery treatment and pitfalls), then override:

- **Colours:** map the brand's colours to roles. The darkest neutral is usually `ink`, the lightest `bg`, the signature colour `accent`. Run `styles.py contrast FG BG` for each pair; when the signature colour fails as text or under white, keep it as `accent` (a fill) and set `on_accent` to whichever of ink or white passes, or derive a text tint and record it in `--notes` as a contrast-derived tint.
- **Fonts:** a brand face on Google Fonts goes in with `--display "Family:700,800"` / `--text "Family:400,600"`. A licensed face goes in as `--font-source local --font-file 700=brand/fonts/Brand-Bold.woff2 ...`; confirm the licence allows web embedding, since the renderer embeds it, and prefer woff2. Missing brand fonts: pick the closest catalog pairing, say it is a stand-in, and note it.
- **Logo:** note the clear-space rule and minimum size from the guidelines in `--notes`; layout and compose read them. Never recolour or distort a logo beyond the variants the guidelines allow.
- **Tone words** ("confident, warm, never jokey") go in `--notes` too; concept and compose use them.

## From references

When the user brings images or links instead of a brand, describe what they share in traits (type classification and weight, palette temperature and contrast, density, imagery kind and treatment, shape language), pick the nearest catalog look as a base and override from those traits. Copy local reference images into `{project}/style/refs/` and pass them with `--reference` so imagery can condition on them.

## Multilingual projects

Check the pairing's `scripts` covers the copy's writing system. For CJK, Arabic or Indic copy use the `noto` pairing and set the matching Noto family as `--text` (Noto Sans JP, Noto Sans Arabic, Noto Sans Devanagari); right-to-left copy also mirrors the layout, which layout handles.
