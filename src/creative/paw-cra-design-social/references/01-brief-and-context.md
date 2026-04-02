# Stage 1: Brief & Context

## Outcome

A fully resolved brief with all parameters needed for visual production: platform, format, exact dimensions, copy/text content, brand context, and design direction.

## Brief Intake

Accept the brief in any format -- structured or freeform. Extract these required fields:

| Field | Required | Source |
|-------|----------|--------|
| **Platform** | Yes | User specifies (Instagram, LinkedIn, TikTok, X, Facebook) |
| **Format** | Yes | Single post or carousel (infer from content if not stated) |
| **Content/copy** | Yes | User provides, or invoke Strategist |
| **Brand** | Yes | User specifies, or use active brand from memory |
| **Campaign** | No | Links to existing campaign context if available |
| **Visual direction** | No | Style notes, mood, reference images |

If the brief is incomplete:
- **Headless:** Infer from context. Use active brand from `.pawbytes/creative-suites/index.md`. Default to Instagram 4:5 portrait if platform unspecified.
- **Interactive:** Ask the user for missing fields before proceeding.

## Platform Spec Lookup

Load the Designer's platform specifications from the parent agent reference at `{project-root}/skills/paw-cra-agent-designer/references/platform-specifications.md`.

Resolve exact dimensions for the target platform and format:

| Platform + Format | Dimensions | Safe Zone |
|-------------------|------------|-----------|
| Instagram Feed (portrait) | 1080x1350 | 60px all sides |
| Instagram Feed (square) | 1080x1080 | 60px all sides |
| Instagram Carousel | 1080x1080 or 1080x1350 | 60px all sides |
| Instagram Story | 1080x1920 | 60px sides, 250px top/bottom |
| LinkedIn Post | 1200x627 | 50px all sides |
| LinkedIn Carousel (PDF) | 1080x1080 or 1920x1080 | 50px all sides |
| TikTok | 1080x1920 | 50px top, 150px bottom |
| X Post | 1200x675 | 40px all sides |
| Facebook Post | 1200x630 | 40px all sides |

**For carousels:** All slides MUST use identical dimensions. Confirm slide count (5-10 typical, up to 20 for Instagram).

## Best-Practice Preload

Load the Designer's best practices from `{project-root}/skills/paw-cra-agent-designer/references/best-practices-common-mistakes.md`.

Key rules to enforce throughout production:
- Minimum 24px body text, 32px headlines for mobile readability
- Safe zone compliance -- no critical content near edges
- Element-specific screenshots when rendering HTML (never `fullPage: true`)
- One dominant visual element per slide (no competing hierarchy)
- Swipe cues on carousel slides

## Copy Resolution

**If copy/text is provided in the brief:** Use it directly. Verify it fits the platform format (character count, line count for the visual layout).

**If copy/text is missing:** Two options depending on mode:
- **Headless with campaign context:** Check `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/` for existing copy assets
- **Interactive or no existing copy:** Invoke the Strategist (`paw-cra-agent-strategist`) for copy drafting. Provide: platform, format, brand guidelines, visual context. The Strategist returns copy variations -- select the best fit for the visual format.
- **Last resort (headless, no strategist):** Generate placeholder copy and flag it in the manifest as `copy_source: "auto-generated"` for human review.

## Brief Validation

Before proceeding to production, confirm the brief is complete:

- [ ] Platform identified with exact dimensions
- [ ] Format confirmed (single post or carousel with slide count)
- [ ] Copy/text content available
- [ ] Brand guidelines loaded (colors, typography, logo rules)
- [ ] Safe zones identified for target platform

**Interactive:** Present the resolved brief summary and ask for confirmation.
**Headless:** Log the resolved brief to the daily log and proceed.
