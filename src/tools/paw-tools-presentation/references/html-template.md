# Slide Templates Reference

Modular HTML templates for McKinsey-style presentations. Each template is a self-contained slide component with defined placeholders.

## Template Location

```
{skill-dir}/assets/{template_name}/
├── code.html      # The HTML template
└── screen.png     # Visual preview
```

---

## Available Templates

### 1. title_slide_template
**Purpose:** Cover/hero slide establishing visual identity.

**Placeholders:**
- `[Title Placeholder]` — Main presentation title
- `[Subtitle Placeholder]` — Supporting tagline or context
- `[Organization Name]` — Company/brand
- `[Presenter Name]` — Speaker name
- `[Date]` — Presentation date
- `[Confidentiality Marker]` — e.g., "Confidential", "Internal"
- `[Slide Number]` — Slide index

**When to use:** First slide of any presentation.

---

### 2. agenda_template
**Purpose:** Table of contents with numbered sections.

**Placeholders:**
- `Agenda` (fixed title)
- `[Section Title Placeholder]` (x4) — Section names
- `[Brief Description Placeholder]` (x4) — Section summaries
- `[CONFIDENTIALITY MARKER]`
- `[COMPANY/DEPARTMENT NAME]`
- `[SLIDE NUMBER]`

**When to use:** After title slide for presentations with 3+ sections.

---

### 3. executive_summary_scr_template
**Purpose:** SCR (Situation-Complication-Resolution) framework slide.

**Placeholders:**
- `[EXECUTIVE SUMMARY TITLE]` — Section label
- `[Lead Message Placeholder]` — High-level synthesis
- **SITUATION column:**
  - `[Situation Content]` — Current status quo
  - `[Supporting detail or key fact 1/2]`
- **COMPLICATION column:**
  - `[Complication Content]` — Problem/challenge
  - `[Critical risk or pain point 1/2]`
- **RESOLUTION column:**
  - `[Resolution Content]` — Recommended action
  - `[Expected outcome or milestone 1/2]`
- `[SLIDE NUMBER]`
- `[COMPANY NAME] | [DEPARTMENT OR DIVISION]`

**When to use:** Executive summaries, strategic recommendations, problem-solution framing.

---

### 4. section_divider_template
**Purpose:** Section break with full-bleed primary background.

**Placeholders:**
- `[Section Number]` — e.g., "01", "02"
- `[Section Title Placeholder]` — Section name
- `[CONFIDENTIALITY MARKER]`
- `[COMPANY/DEPARTMENT NAME]`
- `[SLIDE NUMBER]`

**When to use:** Between major sections for visual breathing room.

---

### 5. pyramid_content_template
**Purpose:** McKinsey Pyramid Principle — lead message with supporting pillars.

**Placeholders:**
- `[Section Title / Context]` — Contextual label
- `[Action-Oriented Lead Message]` — The governing thought
- `[Key Pillar 1/2/3]` — Supporting argument headers
- `[Supporting Evidence 1/2/3]` — Data/facts for each pillar
- `[Confidentiality Statement]`
- `[Slide Number]`

**When to use:** Argument-building slides, recommendations, strategic analysis.

---

### 6. data_visualization_template
**Purpose:** Data slide with chart area and strategic insights sidebar.

**Placeholders:**
- `[Chart Title Placeholder]`
- `[Data Insight Lead Message]`
- `[Y-Axis Label]`
- `[X-Axis Label]` (x5) — Including projections marked `(P)`
- `[Metric]` — Highlighted value
- `[Strategic Insights]` (section header)
- `[Insight Heading]` (x3)
- `[Strategic Takeaway Placeholder]` (x3)
- `[Benchmark Title]`, `[Value]`, `[Secondary Metric Placeholder]`
- `[Source: Placeholder]`
- `[Slide Number]`

**When to use:** Quantitative analysis, performance metrics, market data.

---

### 7. 2x2_matrix_template
**Purpose:** Strategic quadrant analysis (e.g., priority matrix, BCG matrix).

**Placeholders:**
- `[Contextual Framework Description]` — Framework explanation
- `[Axis Label Placeholder: Vertical Axis]` — Y-axis name
- `[Axis Label Placeholder: Horizontal Axis]` — X-axis name
- `[Quadrant Label Placeholder]` (x4)
- `[Analysis summary for quadrant]` (x4)
- `[CONFIDENTIALITY MARKER]`
- `[COMPANY/DEPARTMENT NAME]`

**When to use:** Prioritization, portfolio analysis, strategic positioning.

---

### 8. team_contact_template
**Purpose:** Team introduction and contact information.

**Placeholders:**
- `Team & Contact` (fixed title)
- `[Name Placeholder]` (x3)
- `[Role Placeholder]` (x3)
- `[Email/Contact Placeholder]` (x3)
- `[Office Address Placeholder]`
- `[City, State, Zip]`
- `[Website Placeholder]`
- `[CONFIDENTIALITY MARKER]`
- `[COMPANY/DEPARTMENT NAME]`
- `[SLIDE NUMBER]`

**When to use:** Closing slides, proposal team introductions.

---

## Design System: "The Architectural Brief"

See `assets/kinetic_insight_colour_template/DESIGN.md` for full specification.

### Core Principles

1. **Intentional Asymmetry:** Break expected grids with wide logic margins.
2. **Typographic Gravity:** Extreme scale shifts signal importance.
3. **Tonal Layering:** Depth through color shifts, not shadows.

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | #001e40 | Headlines, emphasis, dark backgrounds |
| `primary-container` | #003366 | Secondary emphasis, CTAs |
| `surface` | #f8f9fa | Main canvas |
| `surface-container-lowest` | #ffffff | Cards, active content |
| `surface-container-low` | #f3f4f5 | Sectioning |
| `on-primary` | #ffffff | Text on primary bg |
| `on-surface` | #191c1d | Primary text |

### Typography

| Font | Role | Weights |
|------|------|---------|
| **Manrope** | Headlines | 700, 800 |
| **Public Sans** | Body | 300, 400, 600 |
| **Inter** | Labels | 400, 500, 700 |

### Key Rules

- **No rounded corners:** `border-radius: 0px`
- **No 1px borders:** Use tonal shifts or ghost borders (<20% opacity)
- **No pure black:** Use `on-surface` (#191c1d) instead of #000000
- **No drop shadows:** Use surface layering for depth

---

## Template Usage in Generation

### Loading Templates

Read template HTML from:
```
{skill-dir}/assets/{template_name}/code.html
```

### Placeholder Replacement

Replace all `[Placeholder Name]` tokens with actual content. Placeholders are:
- Always wrapped in square brackets
- Case-sensitive
- May appear multiple times (replace all instances)

### Slide Composition Workflow

1. **Determine slide type** based on content structure
2. **Select appropriate template** from available options
3. **Load template HTML** from assets
4. **Replace placeholders** with presentation content
5. **Inject Chart.js** if data visualization required (see below)
6. **Wrap in presentation shell** with PDF export button

---

## Adding New Templates

To add a new template:

1. Create folder: `assets/{template_name}/`
2. Add `code.html` with placeholder tokens in `[brackets]`
3. Add `screen.png` preview
4. Document in this file under "Available Templates"

### Template HTML Requirements

- 16:9 aspect ratio container
- Self-contained styles (Tailwind via CDN + inline CSS)
- Google Fonts loaded in `<head>`
- Material Symbols for icons (if needed)
- All dynamic content as `[Placeholder]` tokens

---

## Chart.js Integration

For `data_visualization_template`, inject Chart.js:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  new Chart(document.getElementById('chart-{id}'), {
    type: 'bar', // or 'line', 'pie', 'doughnut'
    data: { /* chart data */ },
    options: { /* chart options */ }
  });
</script>
```

---

## PDF Export

All presentations must include:

```html
<button class="pdf-btn" onclick="window.print()">Export PDF</button>
<style>
@media print {
  .pdf-btn { display: none; }
  .slide-container { page-break-after: always; }
}
</style>
```

---

## Template Selection Guide

| Content Type | Recommended Template |
|--------------|---------------------|
| Cover/Opening | `title_slide_template` |
| Contents/Overview | `agenda_template` |
| Executive Summary | `executive_summary_scr_template` |
| Section Break | `section_divider_template` |
| Argument/Recommendation | `pyramid_content_template` |
| Data/Charts | `data_visualization_template` |
| Analysis Matrix | `2x2_matrix_template` |
| Team/Contact | `team_contact_template` |