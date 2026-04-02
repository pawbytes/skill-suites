# Flyer Rendering

HTML/CSS template architecture and Puppeteer/Playwright rendering pipeline for flyers with text overlays. Loaded during Step 5 when producing flyers or banners with text content.

## Architecture

Flyers combine an AI-generated background image with a code-based text overlay. This hybrid approach gives precise control over typography, layout, and brand consistency while leveraging AI for visual richness.

```
AI Background (FLUX Pro)  +  HTML/CSS Text Overlay  ->  Puppeteer Render  ->  Final PNG/PDF
```

## HTML Template Structure

Every flyer template uses a fixed-dimension container with the AI background and brand-styled text elements:

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: {width}px;
      height: {height}px;
      overflow: hidden;
    }
    .design-container {
      width: {width}px;
      height: {height}px;
      position: relative;
      background-image: url('{background_image_path}');
      background-size: cover;
      background-position: center;
    }
    .overlay {
      position: absolute;
      inset: 0;
      background: {overlay_gradient};
      display: flex;
      flex-direction: column;
      justify-content: {layout_justification};
      padding: {safety_margin}px;
    }
    .headline {
      font-family: '{brand_heading_font}', sans-serif;
      font-size: {headline_size}px;
      font-weight: 700;
      color: {headline_color};
      line-height: 1.1;
      margin-bottom: 24px;
    }
    .body-text {
      font-family: '{brand_body_font}', sans-serif;
      font-size: {body_size}px;
      color: {body_color};
      line-height: 1.5;
      margin-bottom: 16px;
    }
    .cta {
      display: inline-block;
      background: {cta_bg_color};
      color: {cta_text_color};
      padding: 16px 32px;
      font-family: '{brand_heading_font}', sans-serif;
      font-size: {cta_size}px;
      font-weight: 600;
      border-radius: 8px;
    }
    .brand-bar {
      position: absolute;
      bottom: {safety_margin}px;
      left: {safety_margin}px;
      right: {safety_margin}px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-bar img { height: 40px; }
  </style>
</head>
<body>
  <div class="design-container">
    <div class="overlay">
      <h1 class="headline">{headline}</h1>
      <p class="body-text">{body_copy}</p>
      <div class="details">{event_details_or_offer}</div>
      <span class="cta">{cta_text}</span>
    </div>
    <div class="brand-bar">
      <img src="{logo_path}" alt="{brand_name}" />
      <span class="body-text">{contact_info}</span>
    </div>
  </div>
</body>
</html>
```

Adapt this structure to the specific flyer type (event, promotional, informational). The template variables come from the brief and brand guidelines.

## Overlay Strategies

Control text readability over AI backgrounds:

| Strategy | CSS | Best For |
|----------|-----|----------|
| **Dark gradient** | `linear-gradient(to bottom, rgba(0,0,0,0.7), rgba(0,0,0,0.3))` | Light/busy backgrounds |
| **Light gradient** | `linear-gradient(to bottom, rgba(255,255,255,0.85), rgba(255,255,255,0.5))` | Dark backgrounds |
| **Brand color wash** | `linear-gradient(to bottom, {brand_primary}cc, {brand_primary}66)` | On-brand tinting |
| **Solid panel** | Opaque `div` over part of the image | Maximum readability |
| **No overlay** | Background has built-in negative space | Clean AI backgrounds |

Choose based on the AI-generated background. If the background is busy, use a stronger overlay. If it has natural negative space (as requested in the prompt), a lighter approach works.

## Dimensions Reference

### Digital Flyers

| Format | Pixels | Notes |
|--------|--------|-------|
| Instagram (4:5) | 1080 x 1350 | Most versatile digital size |
| Square | 1080 x 1080 | Social media friendly |
| Story (9:16) | 1080 x 1920 | Vertical digital |
| Web banner (16:9) | 1920 x 1080 | Website/email |

### Print Flyers (300 DPI)

| Format | Trim (px) | With Bleed (px) | Safety Margin |
|--------|-----------|-----------------|---------------|
| A4 | 2480 x 3508 | 2552 x 3580 | 36px from trim |
| Letter | 2550 x 3300 | 2625 x 3375 | 38px from trim |
| A5 | 1748 x 2480 | 1820 x 2552 | 36px from trim |
| DL | 1169 x 2480 | 1241 x 2552 | 36px from trim |

For print: set the HTML container to the **with bleed** dimensions, and keep all critical content inside the **safety margin**.

## Rendering

**Critical rule:** Always use element-specific screenshots on `.design-container`. Never use `fullPage: true` or page-level screenshots -- these produce white gaps.

### Puppeteer Rendering

```javascript
const browser = await puppeteer.launch();
const page = await browser.newPage();

await page.setViewport({ width: {width}, height: {height} });
await page.goto('file://{template_path}', { waitUntil: 'networkidle0' });

// Wait for fonts and images
await page.evaluate(() => document.fonts.ready);
await page.evaluate(async () => {
  const images = Array.from(document.images);
  await Promise.all(images.map(img =>
    img.complete ? Promise.resolve() :
    new Promise(r => { img.onload = r; img.onerror = r; })
  ));
});

// CRITICAL: Element screenshot, not page screenshot
const container = await page.$('.design-container');
await container.screenshot({ path: '{output_path}', type: 'png' });

await browser.close();
```

### Playwright Rendering (Alternative)

```javascript
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: {width}, height: {height} } });

await page.goto('file://{template_path}', { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const container = await page.$('.design-container');
await container.screenshot({ path: '{output_path}', type: 'png' });

await browser.close();
```

## Typography Rules for Flyers

| Element | Digital Min Size | Print Min Size (at 300 DPI) |
|---------|------------------|-----------------------------|
| Headline | 48px | 120px (maps to ~14pt) |
| Subheadline | 32px | 80px |
| Body text | 24px | 60px (maps to ~7pt) |
| Fine print | 16px | 40px |
| CTA button text | 28px | 70px |

Ensure contrast ratio of 4.5:1 minimum between text and its background (including any overlay).

## Font Loading

If using custom brand fonts, either:
1. Embed via `@font-face` with a local file path
2. Use Google Fonts via `<link>` tag (requires network during render)
3. Fall back to system fonts that match the brand aesthetic

Always wait for `document.fonts.ready` before taking the screenshot.
