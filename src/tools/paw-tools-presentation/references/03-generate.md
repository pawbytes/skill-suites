# Stage 3: Generate

**Goal:** Produce a complete, self-contained HTML presentation using modular slide templates.

## Output Location

Write to: `{project-root}/.pawbytes/tools-output/presentations/{sanitized-title}.html`

Sanitize title: lowercase, spaces to hyphens, remove special characters.

Create the output directory if it doesn't exist.

## Template-Based Generation

Presentations are built by composing modular HTML templates from `assets/`. Each slide uses a template matched to its content type.

### Template Selection

| Slide Type | Template |
|------------|----------|
| Cover/Opening | `title_slide_template` |
| Contents/Overview | `agenda_template` |
| Executive Summary (SCR) | `executive_summary_scr_template` |
| Section Break | `section_divider_template` |
| Argument/Recommendation | `pyramid_content_template` |
| Data/Charts | `data_visualization_template` |
| Strategic Matrix | `2x2_matrix_template` |
| Team/Contact | `team_contact_template` |

### Generation Workflow

1. **Map outline sections to templates** — Match each slide to appropriate template
2. **Load template HTML** — Read from `assets/{template_name}/code.html`
3. **Replace placeholders** — All `[Placeholder Name]` tokens with actual content
4. **Inject Chart.js** — For data slides, add chart configurations
5. **Compose into single HTML** — Wrap all slides in presentation shell
6. **Add PDF export** — Include print button and styles

## Design System

All templates follow "The Architectural Brief" design system. See:
- `assets/kinetic_insight_colour_template/DESIGN.md` — Full specification

### Core Principles Applied During Generation

- **Tonal layering:** Depth through color shifts, not shadows
- **Intentional asymmetry:** Content breathes with generous margins
- **Typographic gravity:** Scale shifts signal importance
- **No borders:** Use surface color shifts for separation

### Brand Override

If `{project-root}/.pawbytes/tools-output/paw-mkt-setup/brand-config.json` exists:

1. Read brand colors, typography, voice
2. Replace template color tokens with brand palette
3. Swap fonts if brand specifies alternatives
4. Maintain template structure — only override visual tokens

## Placeholder Replacement

Templates contain `[Placeholder Name]` tokens. Replace all instances:

```
[Title Placeholder] → "Q4 Strategic Review"
[Section Title Placeholder] → "Market Analysis"
[Supporting Evidence 1] → "Revenue grew 23% YoY"
```

**Rules:**
- Replace ALL occurrences of each placeholder
- Placeholders are case-sensitive
- Remove any unused optional placeholders (e.g., extra agenda items)

## Chart.js Integration

For `data_visualization_template`, inject charts after HTML composition:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  // One chart config per chart placeholder
  new Chart(document.getElementById('chart-1'), {
    type: 'bar',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      datasets: [{
        label: 'Revenue',
        data: [120, 145, 162, 198],
        backgroundColor: '#001e40'
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } }
    }
  });
</script>
```

See `./references/chart-patterns.md` for more patterns.

## Image Handling

### From Templates

Some templates include placeholder image URLs (e.g., `team_contact_template`). Replace with:
- Actual team photos if available
- Generated images via Pexels/fal.ai APIs
- Or remove image elements if not needed

### Hero Images

For title slide backgrounds or section headers:

1. **Pexels API** — Search based on content theme, requires `pexels_api_key`
2. **fal.ai** — AI-generated images, requires `fal_api_key`
3. **Skip** — Use solid color/gradient background from design system

## Presentation Shell

Wrap all slides in a container with navigation and PDF export:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{presentation-title}</title>
  <!-- Fonts & Tailwind from templates -->
</head>
<body>
  <div class="presentation-container">
    <!-- Slide 1 -->
    <!-- Slide 2 -->
    <!-- ... -->
  </div>
  
  <button class="pdf-btn" onclick="window.print()">Export PDF</button>
  
  <style>
  @media print {
    .pdf-btn { display: none; }
    .slide-container { page-break-after: always; }
  }
  </style>
</body>
</html>
```

## Output Validation

Before writing, verify:

- [ ] All outline sections have corresponding slides
- [ ] All placeholders replaced (no `[` brackets remaining)
- [ ] Charts render correctly with data
- [ ] PDF export button functions
- [ ] Print styles produce clean output
- [ ] Slide order matches outline structure

## Completion

Display:

> "Presentation generated: `{output-path}`"

If headless: return only the output path.

Note any skipped elements (e.g., "Images skipped — no API key configured").

## Adding New Templates

When new templates are added to `assets/`:

1. Document in `./references/html-template.md` under "Available Templates"
2. Add to template selection guide above
3. Define placeholder mapping rules
4. Update this file's template selection table