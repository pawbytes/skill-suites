# Production Queue Builder

Transform the parsed asset list into an ordered, fully-resolved production queue.

## Grouping Strategy

Group assets by platform first, then by format within each platform. This enables:
- Shared style seeds within a platform group (visual consistency)
- Batch template rendering for same-format assets
- Efficient model switching (minimize API overhead)

**Processing order:** Prioritize by date if dates are specified, otherwise process platform groups in this order: Instagram, LinkedIn, TikTok, X/Twitter, Facebook, YouTube, Pinterest, print.

## Per-Asset Resolution

For each queue item, resolve the full production spec:

### Platform Dimensions

| Platform | Format | Dimensions | Aspect Ratio |
|----------|--------|------------|--------------|
| Instagram | Post (portrait) | 1080 x 1350 | 4:5 |
| Instagram | Post (square) | 1080 x 1080 | 1:1 |
| Instagram | Carousel | 1080 x 1350 | 4:5 |
| Instagram | Story | 1080 x 1920 | 9:16 |
| LinkedIn | Post | 1200 x 627 | 1.91:1 |
| LinkedIn | Carousel (PDF) | 1080 x 1080 | 1:1 |
| TikTok | Cover | 1080 x 1920 | 9:16 |
| X/Twitter | Post | 1200 x 675 | 16:9 |
| Facebook | Post | 1200 x 630 | 1.91:1 |
| Facebook | Story | 1080 x 1920 | 9:16 |
| YouTube | Thumbnail | 1280 x 720 | 16:9 |
| Pinterest | Pin | 1000 x 1500 | 2:3 |
| Print | Flyer (A4) | 2480 x 3508 (300dpi) | ~1:1.41 |
| Print | Flyer (Letter) | 2550 x 3300 (300dpi) | ~1:1.29 |

### AI Model Selection

Choose model per asset based on content type:
- **Typography-heavy** (headlines, stats, quotes) — Nano Banana Pro or FLUX.2 [flex]
- **Photography-style** (lifestyle, product, scene) — FLUX.2 [pro] or FLUX.2 [flex]
- **Rapid/bulk** (large batches, prototyping) — FLUX.1 [schnell]
- **Logo/icon work** — Recraft V4 Pro or Ideogram V3

### Naming Convention

Sequential naming: `{campaign}_{platform}_{format}_{NNN}.{ext}`

Examples:
- `summer-sale_instagram_post_001.png`
- `summer-sale_instagram_carousel_001_slide_01.png`
- `summer-sale_linkedin_post_001.jpg`
- `summer-sale_youtube_thumbnail_001.jpg`

### Queue Item Schema

```json
{
  "queue_position": 1,
  "asset_id": 1,
  "platform": "instagram",
  "format": "post",
  "dimensions": { "width": 1080, "height": 1350 },
  "safe_zones": { "top": 60, "bottom": 60, "left": 60, "right": 60 },
  "content": { "headline": "...", "body": "...", "cta": "..." },
  "visual_direction": "...",
  "ai_model": "fal-ai/nano-banana-pro",
  "template": null,
  "export_format": "png",
  "filename": "summer-sale_instagram_post_001.png"
}
```

## Queue Validation

Before starting generation:
- Total queue size logged
- Each item has resolved dimensions and export format
- AI model is selected for each item
- Naming conflicts checked (no duplicate filenames)
- Estimated generation time communicated (interactive mode)
