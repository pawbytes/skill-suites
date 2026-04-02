# Batch Manifest Schema

The `batch-manifest.json` is the machine-readable record of everything produced in a batch run. It lives at the root of the organized bundle folder.

## Schema

```json
{
  "manifest_version": "1.0",
  "campaign": {
    "name": "summer-sale-2026",
    "brand": "acme-corp",
    "date_produced": "2026-04-01",
    "produced_by": "paw-cra-design-batch"
  },
  "summary": {
    "total_assets": 15,
    "successful": 13,
    "failed": 2,
    "skipped": 0,
    "platforms": ["instagram", "linkedin", "tiktok", "x-twitter"],
    "formats": ["post", "carousel", "story"]
  },
  "assets": [
    {
      "id": 1,
      "filename": "summer-sale_instagram_post_001.png",
      "path": "instagram/posts/summer-sale_instagram_post_001.png",
      "platform": "instagram",
      "format": "post",
      "dimensions": { "width": 1080, "height": 1350 },
      "file_size_bytes": 245000,
      "generation_model": "fal-ai/nano-banana-pro",
      "status": "success",
      "brand_validated": true,
      "brand_notes": "",
      "content": {
        "headline": "Summer Sale — 40% Off",
        "body": "This weekend only",
        "cta": "Link in bio"
      },
      "generated_at": "2026-04-01T14:30:00Z"
    },
    {
      "id": 2,
      "filename": null,
      "path": null,
      "platform": "instagram",
      "format": "carousel",
      "dimensions": { "width": 1080, "height": 1350 },
      "file_size_bytes": 0,
      "generation_model": "fal-ai/flux-2-flex",
      "status": "failed",
      "error": "API timeout after 60s",
      "brand_validated": false,
      "brand_notes": "Not generated",
      "content": {},
      "generated_at": null
    }
  ]
}
```

## Field Reference

### Campaign Object

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Campaign identifier |
| `brand` | string | Brand name matching shared memory |
| `date_produced` | string | ISO date of batch production |
| `produced_by` | string | Always `paw-cra-design-batch` |

### Summary Object

| Field | Type | Description |
|-------|------|-------------|
| `total_assets` | integer | Total assets in the production queue |
| `successful` | integer | Assets that completed successfully |
| `failed` | integer | Assets that failed generation or validation |
| `skipped` | integer | Assets skipped (e.g., already exists) |
| `platforms` | array | Unique platforms in the batch |
| `formats` | array | Unique formats in the batch |

### Asset Entry

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Asset ID from the production queue |
| `filename` | string/null | Final filename (null if failed) |
| `path` | string/null | Relative path within bundle (null if failed) |
| `platform` | string | Target platform |
| `format` | string | Asset format (post, carousel, story, etc.) |
| `dimensions` | object | `{width, height}` in pixels |
| `file_size_bytes` | integer | File size (0 if failed) |
| `generation_model` | string | fal.ai model used |
| `status` | string | `success`, `failed`, or `skipped` |
| `error` | string | Error message (only present if failed) |
| `brand_validated` | boolean | Whether brand validation passed |
| `brand_notes` | string | Validation notes or warnings |
| `content` | object | Text content used in the asset |
| `generated_at` | string/null | ISO timestamp of generation |

## Carousel Handling

Carousel assets produce multiple files. In the manifest, carousels are represented as a single entry with a `slides` array:

```json
{
  "id": 3,
  "filename": "summer-sale_instagram_carousel_001",
  "path": "instagram/carousels/summer-sale_instagram_carousel_001/",
  "platform": "instagram",
  "format": "carousel",
  "slides": [
    { "filename": "slide_01.png", "file_size_bytes": 230000 },
    { "filename": "slide_02.png", "file_size_bytes": 215000 },
    { "filename": "slide_03.png", "file_size_bytes": 240000 }
  ],
  "status": "success",
  "brand_validated": true
}
```
