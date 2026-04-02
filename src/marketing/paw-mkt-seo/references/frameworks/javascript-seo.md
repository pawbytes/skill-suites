# JavaScript SEO

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
