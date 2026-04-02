# Stage 2: Outline

**Goal:** Generate a Pyramid Principle-structured outline and get user approval before any HTML is written.

## McKinsey Pyramid Principle Structure

Every section follows: **Situation → Complication → Resolution** with one governing key message per section. Supporting points are beneath, not parallel to, the key message.

**Standard presentation structure:**

1. **Executive Summary** — The governing idea: situation, what changed, and the recommended action
2. **Situation** — Current state, market context, what's true today
3. **Complication** — The tension, gap, or challenge that demands a response
4. **Key Findings** — Supporting evidence (data-backed; flag which ones become charts)
5. **Recommendations** — MECE options or a single recommended path, with rationale
6. **Next Steps** — Owners, timelines, success metrics
7. **Appendix** *(optional)* — Supporting data, methodology, reference material

Adapt this to the actual input — not every section will always apply. Add sections if the content clearly warrants them (e.g. a Budget slide for paid ads plans, a Channels slide for a full marketing strategy).

## Outline Format

Present the outline as a numbered section list. For each section, show:
- Section title
- Key message (one sentence — the governing claim)
- 2-4 supporting bullets
- Chart flag if applicable: `[Chart: type — what it shows]`
- Image flag for cover/hero sections: `[Image: cover/section-header]`

**Example:**
```
1. Executive Summary
   Key message: Q3 growth is being held back by awareness, not conversion — we should double paid reach.
   • Current CVR is 4.2% (strong)
   • Awareness funnel drops off at top of search
   • Recommended: +40% paid budget toward top-of-funnel
   [Image: cover]

2. Situation
   Key message: We have strong conversion but thin awareness — the market opportunity is real.
   • Monthly search volume: 180K (category)
   • Brand share of voice: 6%
   [Chart: bar — brand vs competitor share of voice]
```

## User Review

Present the full outline and ask:
> "Here's your outline. You can edit any section — change the key message, add/remove bullets, add a section, or remove one. Just describe the changes or paste an edited version. Type 'looks good' or 'approved' to generate."

Wait for approval. Apply any edits. Re-confirm if changes are significant.

## Image Source Choice (interactive only)

If image flags are present in the outline, ask once:
> "For hero/cover images, would you like to use:
> - **Gen AI** (DALL-E or Gemini Imagen — requires API key in config)
> - **Stock photos** (Pexels — requires `pexels_api_key` in config)
> - **Skip images** — text and charts only"

If headless: default to skip images (no API keys to prompt for).
Record the choice as `{image_source}` for Stage 3.

## Proceed

Once approved, load `./references/03-generate.md` with the finalized outline and `{image_source}` in context.