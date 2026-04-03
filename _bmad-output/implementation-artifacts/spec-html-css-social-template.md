---
title: 'HTML/CSS Social Media Post Template'
type: 'feature'
created: '2026-04-02T00:00:00.000Z'
status: 'done'
baseline_commit: 'e260972cf54b0ef57841845a6813b23dbbd22139'
context: ['e:/pawbytes/agents/pawbytes-skill-suites/.agents/skills/taste-design/SKILL.md']
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** The `src/creative/paw-cra-design-social` module lacks a standardized HTML/CSS design template for ready-to-use social media posts that aligns with premium UI standards.

**Approach:** Build a reusable HTML/CSS template that strictly adheres to the `taste-design` standards (strict typography, calibrated colors, asymmetric layouts, and premium aesthetics) to generate high-quality social media assets.

## Boundaries & Constraints

**Always:** 
- Adhere to the `taste-design` principles.
- Use distinctive modern sans-serif or serif fonts (e.g., `Geist`, `Cabinet Grotesk`, `Fraunces`), avoiding `Inter` or generic serifs.
- Ensure high-contrast singular accents with absolute neutral bases (Zinc/Slate).
- Implement asymmetric layouts where applicable, avoiding centered symmetry or 3-column generic grids.

**Ask First:** 
- If adding any complex micro-interactions or motion that might not translate well to static social media post exports.

**Never:** 
- Use pure black (`#000000`); use Off-Black, Zinc-950, or Charcoal instead.
- Use neon outer glows, oversaturated accents, or AI copywriting clichés (e.g., "Elevate", "Seamless").
- Overlap elements; every element must occupy its own clear spatial zone.

</frozen-after-approval>

## Code Map

- `src/creative/paw-cra-design-social/template.html` -- The structural semantic HTML layout for the social media post.
- `src/creative/paw-cra-design-social/styles.css` -- The premium, taste-design compliant stylesheet defining typography, colors, and spatial arrangements.

## Tasks & Acceptance

**Execution:**
- [x] `src/creative/paw-cra-design-social/template.html` -- Scaffold the HTML layout with designated zones for imagery, headlines, and secondary text, avoiding generic filler content.
- [x] `src/creative/paw-cra-design-social/styles.css` -- Implement CSS that enforces max-width constraints, calibrated neutral palettes, precise typographic scaling (via `clamp()` where appropriate), and clean spatial separation.

**Acceptance Criteria:**
- Given the template files, when rendered in a browser, then the layout displays a premium, asymmetrical, and highly readable social media post design without overlapping elements or generic aesthetics.

## Design Notes

- **Typography Strategy:** Use a distinctive modern font stack. Headlines must be track-tight and rely on weight/color for hierarchy rather than just massive size. 
- **Color Palette:**
  - Charcoal Ink (`#18181B`) for primary text.
  - Canvas White (`#F9FAFB`) for the primary background surface.
  - A single desaturated accent color (e.g., Rust or Muted Indigo) for highlights.
- **Layout:** Utilize CSS Grid. Avoid `calc()` percentage hacks. Ensure the design collapses gracefully if resized, though social media posts are typically fixed aspect ratios (e.g., 1080x1080 or 1080x1350).

## Suggested Review Order

**Semantic Structure & Taste Design Elements**
- Defines the asymmetrical split, typography hierarchy, and inline photo element.
  [template.html:15](../../src/creative/paw-cra-design-social/template.html#L15)
- Defines the credit section structure with no filler/cliché AI copy.
  [template.html:36](../../src/creative/paw-cra-design-social/template.html#L36)

**Aesthetics & Constraints Enforcement**
- Taste Design variables: no pure black, single accent rust color.
  [styles.css:12](../../src/creative/paw-cra-design-social/styles.css#L12)
- Asymmetrical layout (55% / 45%) and typography architecture rules.
  [styles.css:48](../../src/creative/paw-cra-design-social/styles.css#L48)
- Exact inline photo rules applied to Hero text.
  [styles.css:84](../../src/creative/paw-cra-design-social/styles.css#L84)
