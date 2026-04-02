# Technical SEO Checklist & Quick Reference

> Comprehensive technical SEO audit checklist, schema markup reference, Core Web Vitals optimization guide, and advanced technical SEO considerations.
> Use this as a systematic audit framework and implementation reference.

---

## Table of Contents

1. [Technical SEO Audit Checklist](#technical-seo-audit-checklist)
2. [Schema Markup Quick Reference](#schema-markup-quick-reference)
3. [Core Web Vitals Optimization Guide](#core-web-vitals-optimization-guide)
4. [Internal Linking Strategy Framework](#internal-linking-strategy-framework)
5. [Site Architecture Best Practices](#site-architecture-best-practices)
6. [XML Sitemap & Robots.txt Best Practices](#xml-sitemap--robotstxt-best-practices)
7. [International SEO (hreflang) Quick Reference](#international-seo-hreflang-quick-reference)
8. [JavaScript SEO Considerations](#javascript-seo-considerations)
9. [AI Overview Optimization Checklist (GEO/AEO)](#ai-overview-optimization-checklist-geoaeo)

---

## Technical SEO Audit Checklist

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

---

## Schema Markup Quick Reference

All examples in JSON-LD format (Google's preferred format). Place in `<script type="application/ld+json">` tags in the page `<head>` or `<body>`.

### FAQ Schema
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is [question]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text here]"
      }
    },
    {
      "@type": "Question",
      "name": "How does [question]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text here]"
      }
    }
  ]
}
```
**Use on**: FAQ pages, product pages with Q&A, blog posts with FAQ section.
**Rich result**: Expandable FAQ dropdowns in SERP.

### HowTo Schema
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [task]",
  "description": "[Brief description]",
  "totalTime": "PT30M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "USD",
    "value": "0"
  },
  "step": [
    {
      "@type": "HowToStep",
      "name": "Step 1 title",
      "text": "Step 1 instructions",
      "image": "https://example.com/step1.jpg"
    },
    {
      "@type": "HowToStep",
      "name": "Step 2 title",
      "text": "Step 2 instructions"
    }
  ]
}
```
**Use on**: Tutorial pages, how-to guides, recipe pages.
**Rich result**: Step-by-step carousel in SERP.

### Product Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "Product description",
  "image": "https://example.com/product.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product",
    "priceCurrency": "USD",
    "price": "29.99",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "127"
  }
}
```
**Use on**: Product pages, SaaS pricing pages, e-commerce product listings.
**Rich result**: Price, availability, and star ratings in SERP.

### Review Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "Product",
    "name": "Product Name"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "4",
    "bestRating": "5"
  },
  "author": {
    "@type": "Person",
    "name": "Reviewer Name"
  },
  "reviewBody": "Review text here."
}
```
**Use on**: Review pages, testimonial pages, product comparison pages.

### Article Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title (max 110 chars)",
  "description": "Brief article description",
  "image": "https://example.com/article-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publisher Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2026-03-07",
  "dateModified": "2026-03-07"
}
```
**Use on**: Blog posts, news articles, guides, thought leadership content.
**Rich result**: Article rich result with author, date, and image.

### Organization Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Company description",
  "sameAs": [
    "https://twitter.com/company",
    "https://linkedin.com/company/company",
    "https://facebook.com/company"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-xxx-xxx-xxxx",
    "contactType": "customer service"
  }
}
```
**Use on**: Homepage, about page (site-wide is acceptable).
**Rich result**: Knowledge panel enhancements.

### LocalBusiness Schema
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "image": "https://example.com/storefront.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "ST",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "telephone": "+1-xxx-xxx-xxxx",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  }
}
```
**Use on**: Local business pages, contact pages, location pages.
**Rich result**: Local pack, knowledge panel with hours and location.

### Breadcrumb Schema
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://example.com/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Article Title",
      "item": "https://example.com/blog/article-title"
    }
  ]
}
```
**Use on**: Every page with breadcrumb navigation.
**Rich result**: Breadcrumb trail in SERP replacing raw URL.

### Schema Validation Tools
- **Google Rich Results Test**: https://search.google.com/test/rich-results
- **Schema.org Validator**: https://validator.schema.org
- **Google Search Console**: Enhancements section for schema errors

---

## Core Web Vitals Optimization Guide

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

---

## Internal Linking Strategy Framework

### Internal Linking Goals
1. Distribute page authority (PageRank) to priority pages
2. Help search engines discover and understand site structure
3. Guide users to related content (improve engagement metrics)
4. Establish topical relevance through contextual linking

### Internal Linking Best Practices
- **Anchor text**: Use descriptive, keyword-rich anchor text (not "click here")
- **Contextual links**: Place links within body content, not just navigation
- **Link to deep pages**: Ensure important pages beyond top-level navigation receive links
- **Limit per page**: 100-150 total links maximum (including navigation); focus on 3-10 contextual body links
- **Avoid orphan pages**: Every page should have at least 2-3 internal links pointing to it
- **Prioritize top pages**: Your most important conversion pages should have the most internal links

### Hub-and-Spoke Model
- **Hub page**: Comprehensive pillar page on a broad topic (e.g., "/seo-guide")
- **Spoke pages**: Supporting articles on subtopics (e.g., "/keyword-research", "/technical-seo", "/link-building")
- **Linking pattern**: Hub links to all spokes; all spokes link back to hub; spokes link to each other where relevant
- **SEO benefit**: Establishes topical authority; hub page accumulates authority from all spokes

### Internal Link Audit Checklist
- [ ] All key landing pages have 5+ internal links pointing to them
- [ ] No orphan pages exist (every page has at least one internal link)
- [ ] Anchor text is descriptive and varied (not all identical)
- [ ] Navigation links point to highest-priority pages
- [ ] Blog posts link to related product/service pages
- [ ] Old content is updated with links to new relevant content
- [ ] Broken internal links are identified and fixed

---

## Site Architecture Best Practices

### URL Structure Guidelines
- **Flat is better**: Keep URLs as short and shallow as possible
- **Format**: `domain.com/category/page-name` (maximum 2-3 levels)
- **Characters**: Lowercase, hyphens between words, no underscores or special characters
- **Keywords**: Include primary keyword in URL slug
- **Avoid**: Date-based URLs for evergreen content, parameter-heavy URLs, deep nesting

### URL Examples
```
Good:  example.com/blog/seo-checklist
Good:  example.com/features/analytics
Bad:   example.com/blog/2026/03/07/the-ultimate-seo-checklist-for-beginners
Bad:   example.com/category/subcategory/sub-subcategory/page
Bad:   example.com/p?id=12345&cat=blog&ref=home
```

### Site Depth Rule
- **Homepage**: Depth 0
- **Category/section pages**: Depth 1 (1 click from home)
- **Key content pages**: Depth 2 (2 clicks from home)
- **Supporting pages**: Depth 3 (3 clicks from home)
- **Guideline**: No important page should be more than 3 clicks from the homepage

---

## XML Sitemap & Robots.txt Best Practices

### XML Sitemap Guidelines
- Include only indexable, canonical pages (200 status, no noindex)
- Maximum 50,000 URLs per sitemap file (use sitemap index for larger sites)
- Maximum 50MB uncompressed per sitemap file
- Update `<lastmod>` dates only when content genuinely changes
- Include all important page types: pages, posts, categories, images
- Exclude: noindex pages, paginated pages, parameter URLs, redirect URLs
- Submit to Google Search Console and Bing Webmaster Tools
- Reference in robots.txt: `Sitemap: https://example.com/sitemap.xml`
- Gzip compress sitemaps for large sites

### Robots.txt Best Practices
```
# Example robots.txt
User-agent: *
Allow: /

# Block non-essential paths
Disallow: /admin/
Disallow: /api/
Disallow: /staging/
Disallow: /tmp/
Disallow: /*?utm_*
Disallow: /*?ref=*

# Sitemap reference
Sitemap: https://example.com/sitemap.xml
```

**Rules**:
- Never use robots.txt to hide pages from indexing (use `noindex` meta tag instead)
- Robots.txt blocks crawling but NOT indexing (pages can still appear in SERP)
- Test changes in Google Search Console Robots Testing Tool before deploying
- Keep robots.txt simple; complexity leads to accidental blocking
- Allow CSS and JavaScript files (Googlebot needs them for rendering)

---

## International SEO (hreflang) Quick Reference

### Hreflang Tag Format
```html
<link rel="alternate" hreflang="en-us" href="https://example.com/page" />
<link rel="alternate" hreflang="en-gb" href="https://example.co.uk/page" />
<link rel="alternate" hreflang="es" href="https://example.com/es/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/page" />
```

### Key Rules
- **Always include self-referencing hreflang**: Every page must point to itself
- **Always include x-default**: Fallback for unmatched languages/regions
- **Bidirectional**: If Page A references Page B, Page B must reference Page A
- **Implementation**: HTTP headers, HTML `<link>` tags, or XML sitemap
- **Format**: Language code (ISO 639-1) optionally followed by region code (ISO 3166-1 Alpha 2)
- **Common mistakes**: Missing self-reference, non-reciprocal tags, incorrect language codes

### Common Language-Region Codes
| Code    | Target                  |
|---------|-------------------------|
| `en`    | English (all regions)   |
| `en-us` | English (United States) |
| `en-gb` | English (United Kingdom)|
| `es`    | Spanish (all regions)   |
| `es-mx` | Spanish (Mexico)        |
| `fr`    | French (all regions)    |
| `de`    | German (all regions)    |
| `ja`    | Japanese                |
| `zh`    | Chinese (Simplified)    |
| `pt-br` | Portuguese (Brazil)     |

---

## JavaScript SEO Considerations

### JavaScript Rendering & SEO
- Googlebot uses a Chromium-based renderer (evergreen; kept up to date)
- **Rendering delay**: JS-rendered content may take days to weeks to be indexed
- **Two-wave indexing**: Google crawls HTML first, then renders JS later
- **Recommendation**: Server-side render (SSR) or static site generation (SSG) for critical SEO content

### JavaScript SEO Checklist
- [ ] Critical content (title, H1, body text, links) is in initial HTML or SSR
- [ ] Internal links use `<a href="...">` tags (not `onclick` handlers or JS routing only)
- [ ] Meta tags (title, description, canonical, robots) are server-rendered
- [ ] Structured data is in the initial HTML response
- [ ] JavaScript errors don't prevent content rendering (test with JS disabled)
- [ ] Googlebot can access all JS/CSS resources (not blocked by robots.txt)
- [ ] Infinite scroll has crawlable pagination links
- [ ] Lazy-loaded content uses Intersection Observer (not scroll events)
- [ ] Client-side routing updates the URL and provides `<link rel="canonical">`
- [ ] Check Google Search Console URL Inspection for rendered HTML vs. source HTML

### Framework-Specific Guidance
| Framework       | SEO Approach                               |
|----------------|--------------------------------------------|
| Next.js        | SSR or SSG built-in; use `getStaticProps` or `getServerSideProps` |
| Nuxt.js        | SSR by default; use `nuxt generate` for static |
| SvelteKit      | SSR by default; adapter-auto or adapter-static |
| Gatsby         | SSG by default; good for content sites     |
| React (CSR)    | Add SSR via Next.js or prerendering service |
| Angular        | Angular Universal for SSR                  |
| Vue (CSR)      | Add SSR via Nuxt.js or prerendering service |

---

## AI Overview Optimization Checklist (GEO/AEO)

### What Is AI Overview Optimization?
Optimizing content to be cited, referenced, or surfaced by AI-powered search features (Google AI Overviews, Bing Copilot, ChatGPT search, Perplexity, Claude).

### Content Structure for AI Citation
- [ ] Use clear, direct answers in the first 1-2 sentences of each section
- [ ] Structure content with question-based H2/H3 headings (matching how people ask questions)
- [ ] Provide concise definitions before detailed explanations
- [ ] Use numbered lists and bullet points for step-by-step content
- [ ] Include data, statistics, and specific numbers (AI prefers citable facts)
- [ ] Write in a neutral, authoritative tone (encyclopedia-like for factual content)
- [ ] Cover topics comprehensively (AI prefers thorough, single-source answers)

### Technical Optimization for AI Search
- [ ] Implement FAQ schema for question-answer content
- [ ] Implement HowTo schema for procedural content
- [ ] Use descriptive, semantic HTML (proper heading hierarchy, `<article>`, `<section>`)
- [ ] Ensure fast page loading (AI crawlers prioritize accessible content)
- [ ] Allow AI crawlers in robots.txt (do NOT block GPTBot, Anthropic-ai, PerplexityBot, Google-Extended unless intentional)
- [ ] Include author credentials and expertise signals (E-E-A-T)
- [ ] Keep content up to date (AI systems weight freshness)

### AI Crawler Robots.txt Reference
```
# Allow AI crawlers (default: allowed if not blocked)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: ClaudeBot
Allow: /

# To block specific AI crawlers:
# User-agent: GPTBot
# Disallow: /
```

### Content Patterns That Get Cited by AI
1. **Definition + Context**: "X is [clear definition]. It is used for [context]. For example, [example]."
2. **Comparison tables**: AI loves structured comparisons for "X vs Y" queries
3. **Numbered step-by-step**: "To do X: 1. [step], 2. [step], 3. [step]"
4. **Data-backed claims**: "According to [source], X is Y% more effective than Z."
5. **Pros and cons lists**: Balanced assessments get cited for evaluation queries
6. **Direct answers followed by depth**: Answer first, explain after

### AI Overview Trigger Queries
AI Overviews are most likely to appear for:
- Informational queries ("What is...", "How to...", "Why does...")
- Comparison queries ("X vs Y", "Best X for Y")
- Definition queries ("Define...", "[Term] meaning")
- Process queries ("Steps to...", "How do I...")
- Recommendation queries ("Best...", "Top...")

### Monitoring AI Visibility
- **Google Search Console**: Track impressions/clicks for queries with AI Overviews
- **Perplexity**: Search your target queries to see if you are cited
- **ChatGPT / Claude**: Ask about your topic areas and see if your brand is mentioned
- **Otterly.ai**: Automated AI citation monitoring (third-party tool)
- **Profound**: AI search analytics platform
- **Manual spot-checks**: Weekly search for 10-20 key queries across AI platforms

---

*Technical SEO is the foundation. Without crawlability, indexability, and speed, no amount of content or links will drive organic growth. Audit quarterly, fix issues promptly, and stay ahead of Core Web Vitals thresholds and AI search evolution.*
