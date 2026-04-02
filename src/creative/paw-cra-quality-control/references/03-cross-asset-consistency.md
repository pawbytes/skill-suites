# Stage 3: Cross-Asset Consistency

Verify that all campaign assets work together as a cohesive set. This is the check that no individual production workflow can perform --- it requires seeing the full picture.

## Goal

Ensure visual and tonal consistency across the entire campaign asset set. A campaign should feel like one unified creative effort, not a collection of unrelated pieces.

## Why This Stage Exists

Individual production workflows validate assets in isolation --- the Designer checks that a social post matches brand colors; the Video Producer checks codec and resolution. But neither can verify that the Instagram carousel and the YouTube thumbnail use the same color treatment, or that the video intro and the static banner use consistent typography. This stage catches drift between independently produced assets.

## Consistency Checks

**Color Palette Consistency**
- All assets draw from the same brand color palette
- Color application is consistent --- primary color usage, accent placement, background treatments
- No asset introduces off-palette colors that break the campaign look
- Photography/imagery uses consistent color grading or filter treatment

**Typography Consistency**
- Font families are consistent across all assets (headlines, body, captions)
- Text sizing follows a consistent hierarchy across platforms (adjusted for platform, but proportionally consistent)
- Text treatments (shadows, outlines, backgrounds) are consistent

**Visual Style Consistency**
- Image style is cohesive --- same illustration style, same photo treatment, same graphic approach
- Layout patterns are consistent where applicable (similar grid, similar element placement)
- Graphic elements (borders, shapes, icons) use consistent styling
- Any brand device (logo placement, tagline position) is consistent

**Cross-Format Coherence**
- Video thumbnails match the visual style of static assets
- Video content style matches the campaign's visual language
- Carousel slides maintain internal consistency AND match standalone posts
- Multi-platform adaptations preserve core design while respecting platform norms

**Voice & Tone in Text**
- All text across assets (headlines, captions, CTAs, subtitles) uses consistent brand voice
- Messaging aligns with brief objectives
- No conflicting claims or inconsistent product descriptions across assets

## Evaluation Approach

Review assets in groups:
1. All visual assets together --- look for the odd one out
2. All video assets together --- look for style breaks
3. Visual vs video --- verify they feel like the same campaign
4. Platform variants of the same content --- verify adaptation preserved intent

Flag issues as:
- **Critical** --- Asset clearly belongs to a different campaign or brand (wrong color scheme, different visual style entirely)
- **Warning** --- Minor inconsistency that a viewer might notice (slightly different shade, inconsistent text treatment)
- **Info** --- Suggestion for tighter cohesion (could match better but not a real problem)

## Recording Findings

Append to `qa-report.md`:

```markdown
## Cross-Asset Consistency

### Overall Cohesion: {STRONG / ACCEPTABLE / WEAK}

### Findings
- [{severity}] {description} --- affects: {list of asset filenames}
```

## Progression

Proceed to Stage 4 to compile the final report and route revision tickets.
