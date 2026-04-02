# Brief Intake

Parse the incoming content calendar or campaign brief into a structured asset list.

## Content Calendar Format

A content calendar typically arrives as a table, markdown, CSV, or structured list. Each row represents one piece of content that needs a visual asset.

**Extract per row:**
- **Date/slot** — when the content publishes (used for priority ordering)
- **Platform** — Instagram, LinkedIn, TikTok, X, Facebook, YouTube, Pinterest, or print
- **Format** — post, carousel, story, reel cover, flyer, banner, thumbnail
- **Content/copy** — the text, headline, CTA that appears on the asset
- **Visual direction** — any notes on imagery, mood, style, or specific elements
- **Notes** — additional requirements (e.g., "use product photo", "match last week's style")

## Campaign Brief Format

A campaign brief describes deliverables as a group. Decompose into individual assets.

**Extract from brief:**
- **Campaign name** — used for folder naming and manifest
- **Brand** — which brand guidelines to load
- **Deliverable list** — parse each deliverable into platform + format + content
- **Campaign theme/direction** — global visual direction applied to all assets
- **Timeline** — if dates are specified, use for ordering

## Structured Output

After parsing, produce a structured asset list:

```json
{
  "campaign": "summer-sale-2026",
  "brand": "acme-corp",
  "theme": "Bold summer colors, beach vibes, promotional urgency",
  "assets": [
    {
      "id": 1,
      "platform": "instagram",
      "format": "post",
      "content": {
        "headline": "Summer Sale — 40% Off Everything",
        "body": "This weekend only. Shop now.",
        "cta": "Link in bio"
      },
      "visual_direction": "Beach sunset background, bold white text",
      "date": "2026-06-15",
      "notes": ""
    }
  ]
}
```

## Validation

Before proceeding to queue building:
- Every asset must have a platform and format
- Content should be present for text-heavy formats (posts, carousels, flyers)
- Brand must resolve to an existing brand in shared memory, or user must provide guidelines inline
- Flag any ambiguous entries for clarification (interactive) or best-guess resolution (headless)
