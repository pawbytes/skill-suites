# First-Run Setup for Designer

Welcome! Setting up the Designer workspace.

## Tool Verification

Checking required tools:

- [ ] **fal.ai API Key** — Required for AI image generation (FLUX, Kontext)
- [ ] **ffmpeg** — Required for animated carousels and video conversion
- [ ] **loopwind CLI** — Optional, for template-based generation

## Memory Location

The Designer shares memory with the Aria Creative Suite at:
`.pawbytes/creative-suites/`

## Shared Memory Structure

The agency memory contains:

```
.pawbytes/creative-suites/
├── index.md                    # Active brands, campaigns
├── brands/
│   └── {brand-name}/
│       ├── guidelines.md       # Colors, fonts, voice, logo
│       ├── assets/
│       └── campaigns/
│           └── {campaign}/
│               ├── brief.md
│               └── assets/
└── daily/
    └── {YYYY-MM-DD}.md         # Activity log
```

## Initial Questions

1. **Do you have an existing brand I should work with?**
   - If yes, I'll load those guidelines
   - If no, we can create brand guidelines together

2. **What primary platform(s) will you create content for?**
   - Instagram, LinkedIn, TikTok, X, Facebook, YouTube, Pinterest, Print

3. **Do you have a fal.ai API key configured?**
   - Required for AI image generation
   - Can be set in `.pawbytes/config/config.user.yaml` under `cra.fal_key`

## Ready

Once setup is complete, I can:
- Design social posts for any platform
- Create multi-slide carousels
- Produce print-ready flyers
- Generate brand assets (logos, icons)
- Resize assets for multiple platforms

What would you like to create?