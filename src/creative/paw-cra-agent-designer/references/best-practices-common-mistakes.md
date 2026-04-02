---
name: best-practices-common-mistakes
description: Critical design patterns, safe zones, and common mistakes to avoid for production-quality social media graphics
---

# Best Practices & Common Mistakes

This reference contains battle-tested patterns and critical mistakes to avoid. Every design decision should pass through these guidelines before output.

---

## Rendering HTML Templates: The White Gap Problem

### The Problem

When rendering HTML templates to images, a common issue is **white gaps or extra whitespace** appearing in the output. This happens when:

1. Using `fullPage: true` in Playwright/Puppeteer
2. The viewport doesn't match the intended design dimensions
3. The HTML body has default margins/padding
4. Taking a page screenshot instead of element screenshot

### The Solution

**Always use element-specific screenshots, not full-page screenshots.**

```javascript
// ❌ WRONG: Captures entire page including whitespace
await page.screenshot({ path: 'output.png', fullPage: true });

// ✅ CORRECT: Captures only the design container
const element = await page.$('.design-container');
await element.screenshot({ path: 'output.png' });
```

### HTML Template Structure for Clean Renders

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

### Playwright Screenshot Best Practices

```javascript
async function renderTemplate(url, outputPath, width, height) {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width, height }
  });

  await page.goto(url, { waitUntil: 'networkidle' });

  // Wait for fonts
  await page.evaluate(() => document.fonts.ready);

  // Wait for images
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

---

## Platform Safe Zones

Critical content must stay within safe zones to avoid cropping on different devices.

### Instagram Carousel (1080×1080 or 1080×1350)

| Zone | Pixels from Edge | Content Type |
|------|-----------------|--------------|
| **Critical Safe Zone** | 60px all sides | Text, logos, faces |
| **Safe for Elements** | 30px all sides | Decorative elements |
| **Full Bleed** | 0px | Background images only |

```
┌────────────────────────────────────┐
│  ▲ 60px                           │
│  │                                │
│  │    ┌──────────────────────┐    │
│  │    │                      │    │
│ 60px  │   SAFE ZONE          │    │
│  │    │   Text, logos,       │    │
│  │    │   key visuals        │    │
│  │    │                      │    │
│  │    └──────────────────────┘    │
│  ▼                                │
└────────────────────────────────────┘
```

### LinkedIn Banner (1584×396 personal, 1128×191 company)

**Personal Profile Banner:**
- Safe zone: 40px from all edges
- Note: Profile photo covers left side (~280px)
- Critical content: Right 60% of banner

**Company Page Banner:**
- Safe zone: 50px from all edges
- Logo appears in bottom-left corner
- Keep critical content centered

### YouTube Banner (2560×1440 with complex safe zones)

| Device | Visible Area |
|--------|-------------|
| **TV** | Full 2560×1440 |
| **Desktop** | Center 2560×423 strip |
| **Mobile** | Center 1546×423 strip |
| **Safe Zone** | Center 1235×338 for all devices |

```
┌────────────────────────────────────────────────┐
│                                                │  ▲
│                                                │  │
│     ┌─────────────────────────────────┐       │  │
│     │                                 │       │  │
│     │   SAFE ZONE (1235×338)          │       │ 423px
│     │   Works on ALL devices          │       │  │
│     │                                 │       │  │
│     └─────────────────────────────────┘       │  │
│                                                │  ▼
└────────────────────────────────────────────────┘
      ◄────────────── 2560px ──────────────►
```

### Flyer Print Safe Zones

| Format | Dimensions | Bleed | Safe Zone |
|--------|-----------|-------|-----------|
| **A4** | 210×297mm | 3mm all sides | 10mm from trim |
| **A5** | 148×210mm | 3mm all sides | 8mm from trim |
| **Letter** | 8.5×11" | 0.125" all sides | 0.25" from trim |

---

## Typography for Social Media

### Minimum Sizes for Mobile Readability

| Element | Minimum Size | Recommended |
|---------|-------------|-------------|
| **Headlines** | 32px | 40-60px |
| **Body text** | 24px | 28-32px |
| **Captions** | 18px | 20-24px |
| **Fine print** | 14px | 16px |

### Line Length & Spacing

| Measurement | Rule |
|-------------|------|
| **Line length** | 45-75 characters maximum |
| **Line height** | 1.4-1.6× font size |
| **Paragraph spacing** | 1-1.5× font size |

### Font Pairing (Maximum 2-3 families)

| Strategy | Example | Best For |
|----------|---------|----------|
| Serif + Sans-serif | Playfair + Inter | Professional, elegant |
| Bold + Light weight | Montserrat Bold + Light | Modern, clean |
| Condensed + Standard | Bebas Neue + Roboto | Impact headlines |

---

## Carousel Design Rules

### Critical Rules

1. **All slides MUST have identical dimensions** — Mixed aspect ratios break the carousel
2. **First slide is a 2-second audition** — Hook or lose the viewer
3. **One idea per slide** — No complex multi-point slides
4. **Swipe cues on every slide** — Arrows, progress indicators, or visual flow
5. **CTA on final slide** — But can be hinted earlier

### Optimal Slide Count

| Slides | Use Case |
|--------|----------|
| **5-7** | Quick tips, listicles, simple concepts |
| **8-10** | Tutorials, detailed explanations |
| **10** | Maximum allowed — use only for comprehensive guides |

### Narrative Structure

```
Slide 1: HOOK — Problem statement or bold promise
Slide 2: AGITATE — Why this matters
Slide 3-N: VALUE — One key insight per slide
Slide N-1: PROOF — Example, testimonial, data
Slide N: CTA — Clear next step
```

---

## Common Mistakes to Avoid

### 1. White Gaps in Rendered Output

**Mistake:** Using `fullPage: true` or page screenshot
**Fix:** Use element-specific screenshot on the design container

### 2. Text Cut Off by Platform Cropping

**Mistake:** Placing text at edges (outside safe zone)
**Fix:** Keep all text 60px from edges for Instagram, 40px for LinkedIn

### 3. Unreadable Text on Mobile

**Mistake:** Body text below 24px
**Fix:** Minimum 24px for body, 32px for headlines on social posts

### 4. Inconsistent Carousel Dimensions

**Mistake:** Slide 1 at 1080×1080, Slide 2 at 1080×1350
**Fix:** All slides must be exact same dimensions before upload

### 5. Missing Fonts in Rendered Output

**Mistake:** Not waiting for font load before screenshot
**Fix:** `await page.evaluate(() => document.fonts.ready)`

### 6. Low-Quality AI Images

**Mistake:** Using low-resolution or compressed AI output
**Fix:** Always generate at 2K or higher, export PNG at quality 90+

### 7. Competing Visual Hierarchy

**Mistake:** Multiple bold elements fighting for attention
**Fix:** One dominant element per slide — headline OR image, not both bold

### 8. No Swipe Cues

**Mistake:** User doesn't know it's a carousel
**Fix:** Add arrow, "swipe →", or progress dots on first slide

### 9. CTA Only on Final Slide

**Mistake:** Users who don't swipe all the way miss the action
**Fix:** Strategic CTAs throughout — "Save this" on valuable slides

### 10. Wrong Aspect Ratio for Platform

**Mistake:** Using 1:1 for Instagram Stories (should be 9:16)
**Fix:** Check platform specs before designing

---

## Quality Checklist Before Export

### Visual Design

- [ ] Visual hierarchy is clear (one dominant element)
- [ ] All text within safe zones
- [ ] Body text minimum 24px
- [ ] Line height 1.4-1.6×
- [ ] Maximum 2-3 font families
- [ ] Brand colors applied correctly

### Technical

- [ ] Dimensions match platform specification
- [ ] All carousel slides identical dimensions
- [ ] Fonts loaded before screenshot
- [ ] Images loaded before screenshot
- [ ] Element screenshot (not page screenshot)
- [ ] PNG for graphics, JPEG for photos

### Platform-Specific

- [ ] Instagram: 60px safe zone
- [ ] LinkedIn: Account for profile photo overlap
- [ ] YouTube: Content in center safe zone (1235×338)
- [ ] Print: Bleed and safe zones set

---

## Platform Specifications Quick Reference

| Platform | Post Size | Carousel | Stories | Banner |
|----------|-----------|----------|---------|--------|
| **Instagram Feed** | 1080×1080 / 1080×1350 | 1080×1080 / 1080×1350 | 1080×1920 | — |
| **LinkedIn Personal** | 1200×1200 | 1080×1080 / 1920×1080 | 1080×1920 | 1584×396 |
| **LinkedIn Company** | 1200×1200 | 1080×1080 | — | 1128×191 |
| **X/Twitter** | 1200×675 | 1200×675 | 1080×1920 | 1500×500 |
| **Facebook** | 1080×1080 / 1200×630 | 1080×1080 | 1080×1920 | 820×312 |
| **YouTube** | 1280×720 | — | — | 2560×1440 |