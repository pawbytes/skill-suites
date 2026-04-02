# First-Run Setup for Video Producer

Welcome! Setting up the Video Producer workspace.

## Tool Verification

Checking required tools:

- [ ] **ffmpeg** -- Required for all video processing (assembly, encoding, subtitles)
- [ ] **fal.ai API Key** -- Required for AI video generation (Veo, Kling)
- [ ] **ElevenLabs API Key** -- Optional, for AI voiceover generation
- [ ] **egaki CLI** -- Optional, for multi-provider video generation
- [ ] **Remotion** -- Optional, for programmatic React-based video
- [ ] **OpenShorts** -- Optional, for clip extraction and viral detection

## Memory Location

The Video Producer shares memory with the Aria Creative Suite at:
`.pawbytes/creative-suites/`

## Shared Memory Structure

The agency memory contains:

```
.pawbytes/creative-suites/
├── index.md                    # Active brands, campaigns
├── brands/
│   └── {brand-name}/
│       ├── guidelines.md       # Colors, fonts, voice, logo
│       ├── videos/
│       └── campaigns/
│           └── {campaign}/
│               ├── brief.md
│               ├── scripts/
│               └── videos/
└── daily/
    └── {YYYY-MM-DD}.md         # Activity log
```

## Initial Questions

1. **Do you have an existing brand I should work with?**
   - If yes, I'll load those guidelines
   - If no, we can set up brand context together or work without brand constraints

2. **What type of video are you looking to produce?**
   - Short-form vertical (TikTok, Reels, Shorts)
   - Long-form horizontal (YouTube, web)
   - Motion graphics (intros, animations)
   - Clip extraction from existing content

3. **Do you have ffmpeg installed?**
   - Required for all video processing
   - Install: `winget install ffmpeg` (Windows) or `brew install ffmpeg` (macOS)

4. **Do you have a fal.ai API key configured?**
   - Required for AI video generation
   - Can be set in `{project-root}/.pawbytes/config/config.user.yaml` under `cra.fal_key`

## Ready

Once setup is complete, I can:
- Produce short-form videos for TikTok, Reels, and Shorts
- Create long-form YouTube and web videos
- Build episodic video series
- Generate motion graphics (intros, outros, title cards)
- Extract and repackage clips from existing content
- Generate AI voiceover
- Burn styled subtitles into any video
- Assemble clips with transitions, overlays, and audio

What would you like to produce?
