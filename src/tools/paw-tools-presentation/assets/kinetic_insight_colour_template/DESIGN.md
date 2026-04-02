# Design System Specification: The Executive Editorial

## 1. Overview & Creative North Star
**Creative North Star: "The Architectural Brief"**

This design system is engineered to move beyond the "corporate template" and into the realm of high-end editorial intelligence. Inspired by the rigorous clarity of top-tier management consultancy, the system avoids decorative fluff in favor of **Structural Authority**. 

We achieve a premium feel through "The Architectural Brief" philosophy: 
*   **Intentional Asymmetry:** Breaking the expected 12-column grid with wide "logic margins" (using `spacing-24` for hero offsets) to allow content to breathe.
*   **Typographic Gravity:** Using extreme scale shifts between `display-lg` and `body-md` to signal importance without needing bold colors.
*   **Layered Analytical Depth:** Moving away from flat 2D layouts toward a system of "stacked intelligence" where information is nested in tonal containers.

## 2. Colors: The Tonal Authority
The palette is anchored in `primary` (#001e40) and `primary-container` (#003366), evoking deep-sea stability and intellectual rigor.

### The "No-Line" Rule
To maintain a high-end editorial feel, **1px solid borders are prohibited for sectioning.** Boundaries must be defined solely through background color shifts. 
*   Place a `surface-container-lowest` card on a `surface-container-low` background to create a "soft edge."
*   Use `surface-bright` for the main canvas to ensure the "white space" feels intentional and premium rather than empty.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers of fine stationery. 
*   **Base:** `surface` (#f8f9fa)
*   **Sectioning:** `surface-container-low` (#f3f4f5)
*   **Active Content/Cards:** `surface-container-lowest` (#ffffff)
*   **Secondary Context:** `surface-container-high` (#e7e8e9)

### The Glass & Gradient Rule
While the brand is minimalist, pure flat colors can feel "default." 
*   **CTAs:** Use a subtle linear gradient from `primary` to `primary-container` (135-degree angle) to add a microscopic sense of curvature and "soul."
*   **Floating Navigation:** Apply `surface-container-lowest` with 80% opacity and a `20px` backdrop-blur to create a "frosted glass" effect that allows background data to peek through, maintaining the analytical context.

## 3. Typography: The Voice of Reason
The typography utilizes a tripartite sans-serif strategy to balance authority with modern readability.

*   **Display & Headlines (Manrope):** Chosen for its geometric precision. Use `display-lg` for key insights. Letter-spacing should be set to `-0.02em` for headlines to create a "tight," authoritative lockup.
*   **Title & Body (Public Sans):** A neutral, "workhorse" typeface that disappears to let the data speak. Use `title-lg` for section headers and `body-lg` for executive summaries.
*   **Labels (Inter):** Reserved for micro-data, captions, and UI controls. Inter’s high x-height ensures readability even at the `label-sm` (0.6875rem) scale.

## 4. Elevation & Depth
In this design system, depth is a function of **Tonal Layering**, not physical shadows.

*   **The Layering Principle:** Avoid "Drop Shadows." Instead, stack `surface-container-lowest` on `surface-container-low`. The 2% difference in hex value provides a sophisticated, "barely-there" lift.
*   **Ambient Shadows:** If a floating modal is required, use an ultra-diffused shadow: `box-shadow: 0 20px 50px rgba(0, 30, 64, 0.05);`. Note the use of a `primary` tint in the shadow rather than pure black.
*   **The "Ghost Border" Fallback:** If accessibility requires a container edge (e.g., on a white-on-white edge), use `outline-variant` at **15% opacity**. This creates a "hairline" guide that guides the eye without cluttering the interface.

## 5. Components

### Buttons (The "Precision Trigger")
*   **Primary:** Solid `primary` background. Corner radius is strictly `0px` (Square). High-contrast `on-primary` text in `label-md`.
*   **Secondary:** `surface-container-highest` background. No border.
*   **Tertiary:** Text-only in `primary` color. Use `spacing-1` for underline offset if required.

### Cards & Lists
*   **Constraint:** Forbid all divider lines.
*   **Implementation:** Use `spacing-8` to `spacing-12` of vertical white space to separate list items. Use a `surface-container-low` background on hover to define the interactive area.
*   **Data Cards:** Must use `surface-container-lowest` with a "Ghost Border" top-accent in `primary` (2px height) to denote importance.

### Analytical Data Chips
*   **Style:** Small, square-edged containers using `secondary-container`. Text in `on-secondary-container`. Use these for tagging report sectors or data types.

### Input Fields
*   **Style:** Minimalist "Underline" style. A 1px line in `outline-variant` that transitions to 2px `primary` on focus. No background fill, utilizing the natural `surface` color to maintain transparency.

## 6. Do's and Don'ts

### Do:
*   **Embrace Asymmetry:** Align the main body text to a 6-column center-right grid, leaving the left for "Executive Summaries" or "Key Stats."
*   **Use High-Scale Contrasts:** Pair a `display-lg` metric with a `body-sm` caption immediately below it.
*   **Mind the Gutters:** Use `spacing-6` (2rem) as your minimum margin between unrelated logical blocks.

### Don't:
*   **No Rounded Corners:** `0px` is the standard. Rounding suggests "consumer-friendly" softness; square edges suggest "corporate-grade" precision.
*   **No Pure Black:** Never use `#000000`. Use `on-surface` (#191c1d) for text to maintain a high-end ink-on-paper feel.
*   **No 1px Borders:** Unless it is a "Ghost Border" at <20% opacity, avoid it. Use white space or tonal shifts instead.