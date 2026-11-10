# Prompting images for graphic design

Distilled from the 2026-11 research (Black Forest Labs, fal.ai model pages, 2026 text-rendering benchmarks, Google Ads image guidance, practitioner copy-space guides).

## Why text-free

Type is set in HTML above the image, so every plate is generated without words. Even the best 2026 models change digits, drop dots from URLs and invent unrequested copy ("free shipping"); real type stays spelled right, on-brand, accessible, translatable, and one plate serves many headlines and sizes. When the user wants lettering that is part of the scene (a neon sign, carved stone, packaging), generate it only for headline-length words, quote them exactly with "no other text", proof every character, and never rely on it for prices, dates, URLs or legal lines.

## Prompt anatomy

Earlier words weigh more. In order:

1. **Purpose and format:** "Vertical 4:5 social ad background for a skincare launch."
2. **Layout and copy space:** where the subject sits and what the empty area physically is. "Product group in the lower-right third; the upper-left half is a smooth, low-detail soft sage gradient (#C9D6C3) reserved for a two-line dark headline." An undescribed empty area collects props; name its surface and the edge props must not cross. Size the space from the greybox, not a guess: space for three words will not hold a three-line headline.
3. **Subject:** concrete and specific to the message.
4. **Light:** "soft diffused key light from upper left, gentle grounded contact shadow". State the light direction whenever a cutout will be placed on the plate, so the two agree.
5. **Camera:** lens, height, depth of field.
6. **Palette:** the lock's colours bound to objects with hex ("the backdrop is #0E3B43" works better than "use #0E3B43"); three hues plus neutrals at most.
7. **Style and medium:** the lock's `prompt_anchors` and treatment.
8. **Exclusions, phrased positively:** "clean unmarked surfaces, unbranded, text-free". FLUX models ignore negative prompts, so say what is there instead ("empty deserted street", not "no people"). Endpoints whose schema has a `negative_prompt` field take the lock's `negative_anchors` plus "text, letters, watermark, logo, border, frame, extra fingers" there.
9. **Output lock:** "one complete flat image filling the canvas edge to edge, no border, no mock-up frame" (some models default to a framed mock-up on grey).

Match tone to type: dark text needs a light, even zone; white text a dark, low-detail zone. Faces turn toward the copy zone. Overlay heroes want 40–60% clean area.

## Size and shape

Generate at the slot's aspect (`assets.py check` lists each slot's pixel need) and at least its export size, 2K or more for social and web. Print slots need the box at 300 dpi (150 dpi for A1 and larger): an A3 full-bleed plate is about 3600×5000 px, so generate large and use an upscaler endpoint deliberately, then check at 100%. One wide plate sliced across slides gives a seamless carousel; check that seams miss faces and type.

## Choosing a model

Models change monthly, so search live (`fal.py models --q ...`) and read each schema before the first call. As of November 2026: GPT Image 2 and 2.5, Nano Banana Pro and 2 (Gemini image), Seedream 5.0 Pro and Qwen Image 3 lead on exact text and photoreal scenes; Ideogram V4 gives the best layout control; Recraft V4.1 makes editable vector (SVG) output for icons and wordmarks; FLUX.2 is fast and cheap for plates. Background removal for cutouts: search "background removal" (BiRefNet-class endpoints). Upscaling: search "upscale". Check each endpoint's commercial-use licence; some open weights are non-commercial.

## Cutouts

Use the user's product photo, remove the background, and place the PNG over a plate generated with matching light. Compose adds a soft contact shadow (a blurred ellipse at 20–35% opacity) rather than a hard drop shadow. Google responsive display images discourage products on all-white or obviously composite backgrounds; prefer a real-feeling setting there.

## A consistent series

Carousels and ad sets share one descriptor block (style anchors, palette hexes bound to objects, lens and light), the same aspect, a seed where the endpoint takes one, and reference-image conditioning from the first approved take. Generate the set in one session. Compose can unify plates that drift with a CSS grade layer (a brand colour at `mix-blend-mode: multiply`).

## Provenance, IP and licences

- Keep prompts free of living artists, "in the style of" a studio, brands, logos or packaging the client does not own, characters, celebrities and real people; describe traits instead. Check outputs for brand-like marks the model added unprompted.
- Record provenance on every pick: model, what was generated, what is a real photo. Ad platforms label AI imagery: TikTok ads must disclose fully or substantially AI-generated images; Meta auto-detects AI content in ads since June 2026; Google requires labels for some AI assets in ads targeting the EU, India and New York since July 2026; YouTube does not require disclosure for AI-assisted thumbnails. Deliver surfaces these from the provenance.
- Identifiable people need a model release; client photos need confirmed rights; stock needs its licence noted (`--licence`), and editorial-only images never go in ads.
