# Platform Specs Quick Reference

Condensed lookup table for batch queue building. For full specs with best practices, see the Designer agent's `platform-specifications.md`.

## Social Media Dimensions

| Platform | Format | Width | Height | Ratio | Export |
|----------|--------|-------|--------|-------|--------|
| Instagram | Post (portrait) | 1080 | 1350 | 4:5 | PNG/JPG |
| Instagram | Post (square) | 1080 | 1080 | 1:1 | PNG/JPG |
| Instagram | Carousel | 1080 | 1350 | 4:5 | PNG |
| Instagram | Story | 1080 | 1920 | 9:16 | PNG/JPG |
| Instagram | Reels Cover | 1080 | 1920 | 9:16 | JPG |
| LinkedIn | Post | 1200 | 627 | 1.91:1 | JPG |
| LinkedIn | Carousel (PDF) | 1080 | 1080 | 1:1 | PDF |
| TikTok | Cover | 1080 | 1920 | 9:16 | JPG |
| X/Twitter | Post | 1200 | 675 | 16:9 | JPG |
| Facebook | Post | 1200 | 630 | 1.91:1 | JPG |
| Facebook | Story | 1080 | 1920 | 9:16 | PNG/JPG |
| YouTube | Thumbnail | 1280 | 720 | 16:9 | JPG/PNG |
| Pinterest | Pin | 1000 | 1500 | 2:3 | JPG/PNG |

## Safe Zones (px from edge)

| Platform | Top | Bottom | Left | Right | Notes |
|----------|-----|--------|------|-------|-------|
| Instagram | 60 | 60 | 60 | 60 | All formats |
| LinkedIn | 50 | 50 | 50 | 50 | Professional |
| TikTok | 50 | 150 | 50 | 50 | Bottom reserved for UI |
| X/Twitter | 40 | 40 | 40 | 40 | Minimal |
| Facebook | 50 | 50 | 50 | 50 | Standard |
| YouTube | 50 | 50 | 50 | 50 | Thumbnail |

## Print Dimensions (300 DPI)

| Size | Width (px) | Height (px) | Width (mm) | Height (mm) |
|------|-----------|-------------|-----------|-------------|
| A4 | 2480 | 3508 | 210 | 297 |
| A5 | 1748 | 2480 | 148 | 210 |
| Letter | 2550 | 3300 | 216 | 279 |
| DL | 1169 | 2480 | 99 | 210 |

Print requires 3mm bleed on all sides. Add 36px (at 300dpi) to each dimension.
