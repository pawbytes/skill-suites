# Sitemap and Robots.txt

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
