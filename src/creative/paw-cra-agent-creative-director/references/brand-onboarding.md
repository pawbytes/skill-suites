# Brand Onboarding

Guide the user through creating a comprehensive brand profile. This becomes the foundation for all creative work.

## Goal

Create a brand profile that captures enough detail for any specialist to produce on-brand work without additional clarification.

## Process

1. **Start with the basics:**
   - Brand name
   - Industry/sector
   - Target audience (who are they trying to reach?)

2. **Establish visual identity:**
   - Logo files or description
   - Color palette (hex codes preferred)
   - Typography (font names or style descriptors)
   - Existing brand guidelines or examples

3. **Capture voice and tone:**
   - How does the brand speak? (professional, playful, bold, warm...)
   - What does the brand never do? (words to avoid, tones to avoid)
   - Example copy that captures the brand voice

4. **Define positioning:**
   - What makes this brand different?
   - Key messages or taglines
   - Competitors or inspirations

5. **Identify assets:**
   - What brand assets already exist? (logos, templates, photos)
   - Where are they stored?

## Output

Create a brand profile in memory: `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/profile.md`

Use this structure:

```markdown
# {Brand Name}

## Visual Identity
- Colors: {hex codes}
- Typography: {fonts}
- Logo: {path or description}

## Voice & Tone
- Style: {descriptor}
- Do: {examples}
- Don't: {examples}

## Positioning
- Differentiator: {what makes them unique}
- Key messages: {bullets}
- Audience: {description}

## Assets
- Location: {path}
- Available: {list}
```

## After Creation

- Set as active brand in memory index
- Offer to create a test asset to validate the profile
- Ask if they want to onboard another brand or start a project