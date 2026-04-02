# Technical SEO Audit Checklist

### Crawlability
- [ ] Robots.txt is accessible at `/robots.txt` and not blocking important pages
- [ ] XML sitemap is submitted to Google Search Console and Bing Webmaster Tools
- [ ] No orphan pages (every important page has at least one internal link)
- [ ] Crawl budget is not wasted on parameter URLs, faceted navigation, or duplicate pages
- [ ] Server responds with proper HTTP status codes (200, 301, 404, 410)
- [ ] No redirect chains (more than 2 hops); resolve to final destination
- [ ] No redirect loops
- [ ] Crawl depth: Important pages are within 3 clicks of homepage
- [ ] Log file analysis confirms Googlebot is crawling priority pages
- [ ] Pagination is implemented correctly (rel=next/prev or load-more with crawlable links)

### Indexation
- [ ] Important pages are indexed (check `site:domain.com` and Search Console Index Coverage)
- [ ] No accidental `noindex` tags on important pages
- [ ] Canonical tags are correct on all pages (self-referencing or pointing to correct canonical)
- [ ] No duplicate content issues (check with `site:domain.com/page-title`)
- [ ] Thin content pages are either improved, noindexed, or consolidated
- [ ] Hreflang tags are correct for international/multilingual pages
- [ ] Google Search Console Index Coverage report shows no critical errors
- [ ] URL parameters are handled correctly (GSC URL Parameters tool or canonical tags)
- [ ] Soft 404s are identified and fixed (pages returning 200 but displaying error content)

### Site Speed
- [ ] Page load time under 3 seconds on mobile (3G connection)
- [ ] Core Web Vitals pass assessment (LCP, CLS, INP)
- [ ] Images are compressed and served in modern formats (WebP, AVIF)
- [ ] Lazy loading implemented for below-the-fold images and videos
- [ ] CSS and JavaScript are minified and compressed (gzip/Brotli)
- [ ] Render-blocking resources are deferred or async
- [ ] CDN is configured for static assets
- [ ] Browser caching headers are set (Cache-Control, ETag)
- [ ] Server response time (TTFB) is under 200ms
- [ ] Third-party scripts are audited for performance impact
- [ ] Font loading is optimized (font-display: swap, preload critical fonts)

### Mobile
- [ ] Site is mobile-responsive (passes Google Mobile-Friendly Test)
- [ ] No mobile usability errors in Google Search Console
- [ ] Tap targets are appropriately sized (minimum 48x48px, 8px spacing)
- [ ] Text is readable without zooming (16px minimum font size)
- [ ] No horizontal scrolling on mobile devices
- [ ] Viewport meta tag is set correctly: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Mobile and desktop content parity (same content on both versions)
- [ ] Interstitials and popups comply with Google's guidelines

### Security
- [ ] HTTPS is enforced site-wide (HTTP redirects to HTTPS)
- [ ] SSL certificate is valid and not expired
- [ ] Mixed content warnings resolved (no HTTP resources on HTTPS pages)
- [ ] Security headers configured (HSTS, X-Content-Type-Options, X-Frame-Options)
- [ ] No malware or security warnings in Google Search Console

### On-Page SEO (Technical)
- [ ] Title tags are unique, under 60 characters, and include primary keyword
- [ ] Meta descriptions are unique, under 155 characters, and include a CTA
- [ ] H1 tag present and unique on every page (one H1 per page)
- [ ] Heading hierarchy is logical (H1 > H2 > H3, no skipping levels)
- [ ] Image alt text is descriptive and includes keywords where natural
- [ ] URLs are clean, lowercase, hyphen-separated, and keyword-descriptive
- [ ] Open Graph and Twitter Card meta tags are set for social sharing
- [ ] Structured data (schema markup) is implemented and validated
