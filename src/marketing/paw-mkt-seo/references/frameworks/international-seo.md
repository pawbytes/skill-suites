# International SEO

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
