---
name: template-system
description: Code-based template architecture for reusable social media designs combining AI-generated backgrounds with HTML/CSS layouts
---

# Template System Architecture

Templates combine AI-generated backgrounds with HTML/CSS overlays for reusable, customizable designs. This enables hybrid workflows: AI creates visual assets, code handles text/layout precision.

## Architecture

```
DESIGN OUTPUT
├── AI-Generated Background (FLUX, Nano Banana, Recraft)
├── HTML/CSS Overlay (Text, Shapes, Brand Elements)
└── Renderer (Puppeteer/Playwright) → Final Image (PNG/JPG)
```

## Template Types

### Social Post Templates

| Template | Use Case | Dimensions |
|----------|----------|------------|
| `single-post-hero` | Hero image with headline | 1080×1350, 1080×1080 |
| `single-post-quote` | Quote graphic with attribution | 1080×1350, 1080×1080 |
| `single-post-announcement` | Event/product announcement | 1080×1350, 1080×1080 |
| `single-post-stat` | Data/statistic highlight | 1080×1350, 1080×1080 |

### Carousel Templates

| Template | Structure | Slides |
|----------|-----------|--------|
| `carousel-listicle` | Cover → Items → CTA | 5-10 |
| `carousel-tutorial` | Outcome → Steps → CTA | 5-8 |
| `carousel-story` | Narrative progression | 5-10 |
| `carousel-myth-fact` | Myth/Truth pairs | Even number |

### Flyer & Brand Templates

| Template | Use Case |
|----------|----------|
| `flyer-event` | Event promotion (A4, Letter, A5) |
| `flyer-promo` | Sale/promotion |
| `logo-lockup` | Logo with tagline (PNG/SVG) |
| `social-avatar` | Profile picture (400×400) |

## File Structure

```
.pawbytes/creative-suites/templates/
├── social-posts/
│   ├── single-post-hero.html
│   └── single-post-quote.html
├── carousels/
│   └── carousel-listicle/
│       ├── slide-1-cover.html
│       ├── slide-content.html
│       └── slide-final-cta.html
├── shared/
│   ├── base-styles.css
│   └── brand-variables.css
└── render-config.json
```

## Template Variable System

Templates use `{{variable_name}}` placeholders for dynamic content:

| Variable | Purpose |
|----------|---------|
| `{{background_image}}` | AI-generated or provided image path |
| `{{brand_logo}}` | Path to brand logo |
| `{{headline}}` | Main headline text |
| `{{subheadline}}` | Supporting text |
| `{{cta_text}}` | Call-to-action text |
| `{{brand_primary_color}}` | Hex color code |

## Brand Variables CSS

Create `brand-variables.css` from brand guidelines:

```css
:root {
  --brand-primary: {{brand_primary_color}};
  --brand-secondary: {{brand_secondary_color}};
  --font-heading: {{brand_heading_font}};
  --size-h1: 48px;
  --safe-zone-top: 60px;
}
```

## Render Pipeline

1. Load brand variables into template
2. Generate AI background (see `ai-models-guide.md` for model selection)
3. Inject variables into HTML
4. Render via Puppeteer/Playwright at exact dimensions
5. Export as PNG/JPG

### CRITICAL: Avoiding White Gaps in Rendered Output

**The Problem:** When rendering HTML templates, white gaps or extra whitespace often appear in the output. This is the most common rendering issue.

**Root Causes:**
1. Using `fullPage: true` — captures entire page including whitespace
2. Using page screenshot instead of element screenshot
3. HTML body has default margins/padding
4. Viewport doesn't match design dimensions

**The Solution:** Always use element-specific screenshots.

```javascript
// ❌ WRONG: Captures entire page including whitespace
await page.screenshot({ path: 'output.png', fullPage: true });

// ✅ CORRECT: Captures only the design container
const element = await page.$('.design-container');
await element.screenshot({ path: 'output.png' });
```

### Proper HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    html, body {
      width: 1080px;      /* Exact target width */
      height: 1350px;     /* Exact target height */
      overflow: hidden;   /* Prevent scrollbars */
    }
    .design-container {
      width: 1080px;
      height: 1350px;
      position: relative;
      background: var(--brand-primary);
      /* Your design here */
    }
  </style>
</head>
<body>
  <div class="design-container">
    <!-- All content inside this container -->
  </div>
</body>
</html>
```

### Complete Render Function

```javascript
async function renderTemplate(url, outputPath, width, height) {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width, height }
  });

  await page.goto(url, { waitUntil: 'networkidle' });

  // Wait for fonts to load
  await page.evaluate(() => document.fonts.ready);

  // Wait for images to load
  await page.evaluate(async () => {
    const images = Array.from(document.images);
    await Promise.all(images.map(img => {
      if (img.complete) return Promise.resolve();
      return new Promise(resolve => {
        img.onload = resolve;
        img.onerror = resolve;
      });
    }));
  });

  // CRITICAL: Screenshot the element, not the page
  const container = await page.$('.design-container');
  await container.screenshot({ path: outputPath, type: 'png' });

  await browser.close();
}
```

## Quality Standards

- **Text readability:** Minimum 24px body text for social media
- **Safe zones:** 60px from edges for Instagram, 40px for LinkedIn
- **Contrast:** 4.5:1 minimum for text accessibility
- **Aspect ratios:** All carousel slides must match exactly
- **No white gaps:** Use element screenshots, not page screenshots

## Creating Custom Templates

When creating new templates:

1. Define exact dimensions (reference `platform-specifications.md`)
2. Set safe zones for critical content
3. Use brand CSS variables for colors/typography
4. Test with various content lengths
5. Validate across render engines

For full HTML/CSS template examples, see `./template-examples.md`.