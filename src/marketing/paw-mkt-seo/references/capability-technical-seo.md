# Technical SEO Capability

## Overview
Audit and optimize site infrastructure for search engine crawling, indexing, and ranking. Covers Core Web Vitals, crawlability, site architecture, schema markup, mobile compliance, and JavaScript SEO.

## When to Use
- Site speed and performance issues
- Crawl errors or indexation problems
- Schema markup implementation
- Mobile-first compliance
- JavaScript rendering issues
- Site architecture redesign

## Framework Lookup
Read `./references/frameworks-index.csv` and load relevant frameworks by `seo_domain` = "Technical SEO":
- Technical Audit (`frameworks/technical-audit.md`)
- Schema Markup (`frameworks/schema-markup.md`)
- Core Web Vitals (`frameworks/core-web-vitals.md`)
- Internal Linking (`frameworks/internal-linking.md`)
- Site Architecture (`frameworks/site-architecture.md`)
- Sitemap and Robots (`frameworks/sitemap-robots.md`)
- International SEO (`frameworks/international-seo.md`)
- JavaScript SEO (`frameworks/javascript-seo.md`)

## Capability Workflow

### 1.1 Core Web Vitals and Site Speed

Audit LCP (Largest Contentful Paint), INP (Interaction to Next Paint), and CLS (Cumulative Layout Shift).

Recommend specific fixes:
- Image optimization (WebP/AVIF, lazy loading, proper sizing)
- Critical CSS inlining
- Font loading strategy (font-display: swap)
- JavaScript defer/async
- Server response time (TTFB)

Prioritize by impact: fixes that improve multiple CWV metrics first.

Tools: PageSpeed Insights, Chrome UX Report, WebPageTest, Lighthouse.

### 1.2 Crawlability and Indexation

- Audit robots.txt for unintentional blocks
- Check XML sitemap: all important URLs included, no 4xx/5xx URLs, proper lastmod dates
- Review crawl budget allocation for large sites (1000+ pages)
- Check GSC Coverage report for errors, warnings, excluded pages
- Identify orphan pages (no internal links pointing to them)
- Audit crawl depth -- critical pages within 3 clicks of homepage

### 1.3 Site Architecture and Internal Linking

- Design or audit topic-based hierarchy: Homepage > Category > Subcategory > Page
- Internal linking strategy: contextual links, hub-and-spoke model for topic clusters, breadcrumb navigation
- Link equity distribution: high-priority pages receive the most internal links
- Flat architecture: minimize click depth for important pages

### 1.4 Schema Markup (JSON-LD)

Provide ready-to-use JSON-LD for:
- Organization, LocalBusiness
- Product, Article/BlogPosting
- FAQ (critical for AI search and featured snippets)
- HowTo, BreadcrumbList
- Review/AggregateRating
- Event, VideoObject

Always validate with Google Rich Results Test.

### 1.5 Mobile, Security, and Technical Hygiene

- Mobile-first indexing compliance: identical content on mobile and desktop
- Responsive audit: no horizontal scroll, 48x48px tap targets, 16px+ fonts
- SSL audit: proper installation, no mixed content
- Canonical tag audit: self-referencing canonicals
- Duplicate content resolution
- Hreflang for international/multilingual sites
- 404 and redirect audit: max 2-hop redirect chains

### 1.6 JavaScript SEO

- Audit whether critical content requires client-side JS rendering
- Recommend SSR/SSG for content-heavy pages
- Verify Google can render JS content (URL Inspection tool in GSC)
- Dynamic rendering as fallback if full SSR is not feasible

## Output

Technical SEO deliverables:
- `seo-audit-{YYYY-MM-DD}.md` with prioritized checklist
- `schema/{type}-{YYYY-MM-DD}.json` with implementation-ready JSON-LD
- Implementation notes: where to place code, how to test, how to verify in GSC