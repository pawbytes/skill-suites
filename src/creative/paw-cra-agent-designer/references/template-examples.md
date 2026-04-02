---
name: template-examples
description: Full HTML/CSS code examples for template implementation - load only when creating new templates
---

# Template Code Examples

**Load this file only when implementing new templates.** For architecture overview, see `template-system.md`.

---

## Base Template Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../shared/base-styles.css">
  <link rel="stylesheet" href="../shared/brand-variables.css">
  <style>
    .container {
      width: 1080px;
      height: 1350px;
      position: relative;
      overflow: hidden;
    }
    .background {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      z-index: 1;
    }
    .content {
      position: relative;
      z-index: 2;
      padding: 80px 60px;
      display: flex;
      flex-direction: column;
      height: 100%;
    }
  </style>
</head>
<body>
  <div class="container">
    <img class="background" src="{{background_image}}" alt="">
    <div class="content">
      <div class="header">
        <div class="brand-logo">{{brand_logo}}</div>
      </div>
      <div class="main-content">
        <h1 class="headline">{{headline}}</h1>
        <p class="subheadline">{{subheadline}}</p>
        <div class="cta-button">{{cta_text}}</div>
      </div>
      <div class="footer">
        <div class="brand-tagline">{{brand_tagline}}</div>
      </div>
    </div>
  </div>
</body>
</html>
```

---

## Brand Variables CSS Template

```css
:root {
  /* Brand Colors */
  --brand-primary: {{brand_primary_color}};
  --brand-secondary: {{brand_secondary_color}};
  --brand-accent: {{brand_accent_color}};
  --brand-background: {{brand_background_color}};
  --brand-text: {{brand_text_color}};

  /* Typography */
  --font-heading: {{brand_heading_font}};
  --font-body: {{brand_body_font}};

  /* Font Sizes */
  --size-display: 64px;
  --size-h1: 48px;
  --size-h2: 36px;
  --size-body: 24px;

  /* Spacing */
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 40px;

  /* Layout */
  --safe-zone: 60px;
  --border-radius: {{brand_border_radius}};
}
```

---

## Carousel Slide Templates

### Cover Slide

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="../shared/base-styles.css">
  <style>
    .carousel-cover {
      width: 1080px; height: 1350px;
      position: relative;
    }
    .cover-content {
      position: absolute;
      bottom: 100px; left: 60px; right: 60px;
    }
    .cover-headline {
      font-size: 56px; font-weight: 800;
      line-height: 1.1; margin-bottom: 20px;
    }
    .cover-number {
      font-size: 120px; font-weight: 900;
      opacity: 0.15;
      position: absolute; top: 60px; right: 60px;
    }
    .swipe-indicator {
      position: absolute; bottom: 40px; right: 60px;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="carousel-cover">
    <img class="background" src="{{background_image}}" alt="">
    <div class="cover-number">{{item_count}}</div>
    <div class="cover-content">
      <div class="category-tag">{{category}}</div>
      <h1 class="cover-headline">{{headline}}</h1>
      <p class="cover-subtitle">{{subtitle}}</p>
    </div>
    <div class="swipe-indicator">Swipe →</div>
  </div>
</body>
</html>
```

### Content Slide

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="../shared/base-styles.css">
  <style>
    .carousel-content {
      width: 1080px; height: 1350px;
      display: grid;
      grid-template-rows: auto 1fr auto;
    }
    .slide-number {
      font-size: 80px; font-weight: 900;
      opacity: 0.1;
    }
    .slide-body {
      padding: 0 60px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .item-title { font-size: 42px; font-weight: 700; margin-bottom: 24px; }
    .item-description { font-size: 26px; line-height: 1.5; }
  </style>
</head>
<body>
  <div class="carousel-content">
    <img class="background" src="{{background_image}}" alt="">
    <div class="slide-header">
      <img src="{{brand_logo}}" class="brand-logo-small">
      <span class="slide-number">{{slide_number}}</span>
    </div>
    <div class="slide-body">
      <h2 class="item-title">{{item_title}}</h2>
      <p class="item-description">{{item_description}}</p>
    </div>
    <div class="slide-footer">
      <div class="progress-dots">{{progress_dots}}</div>
      <div class="brand-handle">{{brand_handle}}</div>
    </div>
  </div>
</body>
</html>
```

### CTA Slide

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="../shared/base-styles.css">
  <style>
    .carousel-cta {
      width: 1080px; height: 1350px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }
    .cta-headline { font-size: 48px; font-weight: 700; margin-bottom: 24px; }
    .cta-subtext { font-size: 28px; margin-bottom: 40px; opacity: 0.9; }
    .cta-button {
      display: inline-block;
      padding: 20px 48px;
      font-size: 28px; font-weight: 600;
      border-radius: 60px;
    }
  </style>
</head>
<body>
  <div class="carousel-cta">
    <img class="background" src="{{background_image}}" alt="">
    <div class="cta-content">
      <h2 class="cta-headline">{{cta_headline}}</h2>
      <p class="cta-subtext">{{cta_subtext}}</p>
      <a class="cta-button" href="{{cta_link}}">{{cta_button_text}}</a>
      <div class="cta-contact">
        <span>{{website}}</span>
        <span>{{email}}</span>
      </div>
    </div>
  </div>
</body>
</html>
```

---

## Render Script (Puppeteer)

```javascript
const puppeteer = require('puppeteer');
const fs = require('fs');

async function renderTemplate(templatePath, variables, outputPath) {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({
    width: variables.width || 1080,
    height: variables.height || 1350,
    deviceScaleFactor: 1
  });

  const templateHtml = fs.readFileSync(templatePath, 'utf8');
  const renderedHtml = injectVariables(templateHtml, variables);

  await page.setContent(renderedHtml, { waitUntil: 'networkidle0' });
  await page.evaluateHandle('document.fonts.ready');
  await page.screenshot({ path: outputPath, type: 'png' });

  await browser.close();
  return outputPath;
}

function injectVariables(html, variables) {
  let result = html;
  for (const [key, value] of Object.entries(variables)) {
    result = result.replaceAll(`{{${key}}}`, value);
  }
  return result;
}

module.exports = { renderTemplate };
```

---

## Background Generation Integration

```javascript
const fal = require('@fal-ai/client');

async function generateBackground(theme, slideType, brandColors) {
  const slideModifiers = {
    cover: 'bold, eye-catching, strong visual impact',
    content: 'subtle, not distracting, clean space for text',
    cta: 'warm, inviting, action-oriented'
  };

  const prompt = `${theme} themed background, abstract, subtle texture, gradient, minimalist, professional, dominant colors: ${brandColors.primary}, ${brandColors.secondary}, ${slideModifiers[slideType]}`;

  const result = await fal.subscribe('fal-ai/flux-pro/v1.1', {
    input: {
      prompt: prompt,
      image_size: 'portrait_4_5',
      seed: getConsistentSeed(theme)
    }
  });

  return result.images[0].url;
}
```