# Schema Markup

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
