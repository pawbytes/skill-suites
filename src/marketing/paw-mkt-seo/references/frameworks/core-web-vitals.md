# Core Web Vitals

### Metric Targets (2025-2026)

| Metric | Good        | Needs Improvement | Poor         |
|--------|-------------|-------------------|--------------|
| LCP    | <= 2.5s     | 2.5s - 4.0s      | > 4.0s       |
| CLS    | <= 0.1      | 0.1 - 0.25       | > 0.25       |
| INP    | <= 200ms    | 200ms - 500ms    | > 500ms      |

### LCP (Largest Contentful Paint) Optimization
**What it measures**: Time for the largest visible content element to render.

**Common LCP elements**: Hero images, headline text blocks, video thumbnails.

**Fixes (ordered by impact)**:
1. **Optimize the LCP image**: Compress, use WebP/AVIF, set explicit width/height, preload with `<link rel="preload" as="image">`
2. **Reduce server response time**: Upgrade hosting, use CDN, implement caching, optimize database queries
3. **Eliminate render-blocking resources**: Defer non-critical CSS/JS, inline critical CSS
4. **Optimize web fonts**: Use `font-display: swap`, preload critical fonts, limit font variations
5. **Preconnect to required origins**: `<link rel="preconnect" href="https://cdn.example.com">`
6. **Use responsive images**: `srcset` and `sizes` attributes for appropriate image sizes
7. **Remove lazy loading from LCP image**: Above-the-fold images should load eagerly

### CLS (Cumulative Layout Shift) Optimization
**What it measures**: Visual stability; how much page content shifts during loading.

**Fixes (ordered by impact)**:
1. **Set explicit dimensions on images and videos**: Always include `width` and `height` attributes
2. **Reserve space for ads/embeds**: Use CSS `min-height` or `aspect-ratio` for dynamic content
3. **Avoid inserting content above existing content**: Load banners, popups, and injected elements below the fold or in fixed positions
4. **Use `transform` animations**: Instead of `top`, `left`, `width`, `height` for animations
5. **Preload web fonts**: Prevent FOUT (Flash of Unstyled Text) layout shifts
6. **Avoid dynamic content injection**: Headers, CTAs, and consent banners should be reserved in layout
7. **Use `content-visibility: auto`** carefully: Can cause CLS if not combined with `contain-intrinsic-size`

### INP (Interaction to Next Paint) Optimization
**What it measures**: Responsiveness; time from user interaction to visual response.

**Fixes (ordered by impact)**:
1. **Break up long tasks**: Split JavaScript tasks longer than 50ms using `requestIdleCallback` or `scheduler.yield()`
2. **Reduce JavaScript execution time**: Code-split, tree-shake, remove unused JS
3. **Optimize event handlers**: Debounce scroll/resize handlers, use passive event listeners
4. **Minimize main thread work**: Move heavy computation to Web Workers
5. **Reduce DOM size**: Keep under 1,500 nodes; simplify deeply nested structures
6. **Avoid layout thrashing**: Batch DOM reads and writes separately
7. **Use CSS containment**: `contain: layout style paint` on complex components

### Core Web Vitals Testing Tools
- **PageSpeed Insights**: https://pagespeed.web.dev (lab + field data)
- **Google Search Console**: Core Web Vitals report (field data)
- **Chrome DevTools**: Performance panel (lab data)
- **Web Vitals Extension**: Chrome extension for real-time CWV monitoring
- **WebPageTest**: https://webpagetest.org (detailed waterfall analysis)
