# Part 7: Appendices

This section provides quick reference materials for troubleshooting, platform specifications, file formats, and terminology.

---

## Table of Contents

1. [Troubleshooting Guide](#troubleshooting-guide)
2. [Platform Dimension Reference](#platform-dimension-reference)
3. [File Format Guide](#file-format-guide)
4. [Quality Checklist](#quality-checklist)
5. [Glossary](#glossary)

---

## Troubleshooting Guide

When something doesn't work as expected, check this guide for common issues and solutions.

### Campaign Issues

#### Problem: Campaign won't start

| Possible Cause | Solution |
|----------------|----------|
| Missing campaign brief | Create a brief.md file in your campaign folder, or provide details in your request |
| Brand context not loaded | Mention your brand name, or run brand setup first |
| Unclear deliverables | Specify exactly what assets you need (e.g., "3 Instagram posts and 1 TikTok video") |

#### Problem: Assets are inconsistent

| Possible Cause | Solution |
|----------------|----------|
| Brand guidelines incomplete | Add more detail to your brand guidelines (colors, fonts, style preferences) |
| Multiple brands mixed | Confirm which brand the campaign is for |
| Conflicting style requests | Be consistent with style descriptions across requests |

#### Problem: Quality check fails

| Issue Type | What It Means | How to Fix |
|------------|---------------|------------|
| Wrong dimensions | Asset doesn't match platform requirements | Asset will be auto-fixed, or request a remake |
| Off-brand colors | Colors don't match brand palette | Designer will revise using brand colors |
| Missing logo | Logo not applied to asset | Request logo addition |
| Text too small | Text may be unreadable on mobile | Request larger text |

### Export Issues

#### Problem: Export fails to start

| Possible Cause | Solution |
|----------------|----------|
| Source file not found | Verify the file path is correct |
| Unsupported format | Convert to PNG, JPG, or MP4 first |
| ffmpeg not installed | Install ffmpeg: `winget install ffmpeg` (Windows) or `brew install ffmpeg` (Mac) |

#### Problem: Export quality is poor

| Possible Cause | Solution |
|----------------|----------|
| Source resolution too low | Use a higher-resolution source image |
| Aggressive compression needed | Source file may be very large; quality is reduced to meet platform limits |
| Upscaling required | Original image is smaller than target; use a larger source if possible |

#### Problem: Content is cut off in export

| Possible Cause | Solution |
|----------------|----------|
| Safe zone violation | Important content is too close to edges; reposition in original or accept letterboxing |
| Aspect ratio mismatch | Different platforms need different ratios; some cropping may occur |

### Video Issues

#### Problem: Video too long for platform

| Platform | Max Duration | Solution |
|----------|--------------|----------|
| TikTok | 10 minutes (60s optimal) | Trim video or create shorter clips |
| Instagram Reels | 90 seconds | Trim video or create shorter clips |
| YouTube Shorts | 60 seconds | Trim video or create shorter clips |
| Twitter/X | 2 minutes 20 seconds | Trim video or post as thread |

**What happens:** The system warns you but does not auto-trim. You decide whether to trim or skip that platform.

#### Problem: Subtitles not appearing

| Possible Cause | Solution |
|----------------|----------|
| Subtitles not generated | Request subtitles: "Add subtitles to this video" |
| Subtitle file not uploaded | Manually upload the .srt file to the platform |
| Platform doesn't support captions | Burn subtitles into video instead |

### Design Issues

#### Problem: Generated image doesn't match request

| Possible Cause | Solution |
|----------------|----------|
| Vague description | Provide more specific details about what you want |
| Conflicting instructions | Remove contradictory requirements |
| Style mismatch | Provide reference images or describe the style more precisely |

#### Problem: Text is hard to read

| Possible Cause | Solution |
|----------------|----------|
| Low contrast | Request higher contrast between text and background |
| Font too small | Request larger text |
| Busy background | Request simpler background or text area overlay |

---

## Platform Dimension Reference

### Image Dimensions by Platform

| Platform | Format | Dimensions (px) | Aspect Ratio | Notes |
|----------|--------|-----------------|--------------|-------|
| Instagram | Feed Square | 1080 x 1080 | 1:1 | Classic square format |
| Instagram | Feed Portrait | 1080 x 1350 | 4:5 | More vertical space |
| Instagram | Feed Landscape | 1080 x 566 | 16:9 | Less common |
| Instagram | Story | 1080 x 1920 | 9:16 | Full screen vertical |
| Instagram | Reel Cover | 1080 x 1920 | 9:16 | Same as Story |
| TikTok | Feed Video | 1080 x 1920 | 9:16 | Vertical only |
| TikTok | PFP | 200 x 200 | 1:1 | Profile picture |
| YouTube | Thumbnail | 1280 x 720 | 16:9 | Required for all videos |
| YouTube | Channel Art | 2560 x 1440 | 16:9 | Banner image |
| YouTube | Short | 1080 x 1920 | 9:16 | Vertical video |
| LinkedIn | Feed Image | 1200 x 627 | 1.91:1 | Shared link preview |
| LinkedIn | Feed Article | 1200 x 628 | 1.91:1 | Article thumbnail |
| LinkedIn | Story | 1080 x 1920 | 9:16 | Mobile only |
| Twitter/X | Feed Image | 1600 x 900 | 16:9 | Single image optimal |
| Twitter/X | Card Image | 800 x 418 | 1.91:1 | Link preview |
| Twitter/X | Header | 1500 x 500 | 3:1 | Profile banner |
| Facebook | Feed Image | 1200 x 630 | 1.91:1 | Link preview |
| Facebook | Story | 1080 x 1920 | 9:16 | Full screen |
| Facebook | Cover | 820 x 312 | 2.7:1 | Page banner |
| Pinterest | Pin | 1000 x 1500 | 2:3 | Standard pin |
| Pinterest | Square Pin | 1000 x 1000 | 1:1 | Alternative format |
| Pinterest | Story Pin | 1080 x 1920 | 9:16 | Full screen |
| Google Business | Post | 720 x 720 | 1:1 | Square recommended |
| Google Business | Cover | 1080 x 608 | 16:9 | Business profile |

### Video Dimensions by Platform

| Platform | Resolution | Aspect Ratio | Max Duration | Max File Size |
|----------|------------|--------------|--------------|---------------|
| Instagram Reels | 1080 x 1920 | 9:16 | 90 seconds | 4 GB |
| Instagram Feed | 1080 x 1080 | 1:1 | 60 seconds | 4 GB |
| Instagram Feed | 1080 x 1350 | 4:5 | 60 seconds | 4 GB |
| TikTok | 1080 x 1920 | 9:16 | 10 minutes | 500 MB (mobile) |
| YouTube | 1920 x 1080 | 16:9 | 12 hours | 256 GB |
| YouTube Shorts | 1080 x 1920 | 9:16 | 60 seconds | 256 GB |
| LinkedIn | 1920 x 1080 | 16:9 | 10 minutes | 5 GB |
| Twitter/X | 1920 x 1080 | 16:9 | 2m 20s | 512 MB |
| Facebook | 1920 x 1080 | 16:9 | 240 minutes | 10 GB |
| Facebook Reels | 1080 x 1920 | 9:16 | 90 seconds | 4 GB |

### Safe Zone Reference

Safe zones indicate areas where platform UI (buttons, captions, overlays) may cover your content. Keep important elements inside the safe zone.

| Platform | Format | Top | Bottom | Left | Right |
|----------|--------|-----|--------|------|-------|
| Instagram | Feed | 0px | 0px | 0px | 0px |
| Instagram | Story | 120px | 200px | 60px | 60px |
| Instagram | Reels | 50px | 150px | 20px | 20px |
| TikTok | Feed | 50px | 150px | 20px | 20px |
| YouTube | Video | 0px | 40px | 0px | 0px |
| Facebook | Feed | 0px | 60px | 0px | 0px |
| Facebook | Story | 120px | 200px | 60px | 60px |
| LinkedIn | Feed | 0px | 50px | 0px | 0px |
| Twitter/X | Feed | 0px | 0px | 0px | 0px |
| Pinterest | Pin | 0px | 50px | 0px | 0px |
| Google Business | Post | 0px | 0px | 0px | 0px |

**Tip:** For vertical video platforms (TikTok, Reels, Stories), the bottom 150-200 pixels are usually covered by usernames, captions, and action buttons. Never place important text or logos there.

---

## File Format Guide

### Image Formats

| Format | Best For | Transparency | File Size | Quality |
|--------|----------|--------------|-----------|---------|
| PNG | Graphics, logos, text-heavy images | Yes | Larger | Excellent |
| JPG/JPEG | Photos, complex images | No | Smaller | Good |
| WebP | Web use, modern platforms | Yes | Smallest | Excellent |
| SVG | Logos, icons, scalable graphics | Yes | Tiny | Perfect |
| PDF | Print materials | No | Varies | Excellent |

### When to Use Each Format

| Use PNG When... | Use JPG When... |
|-----------------|-----------------|
| Image has text | Image is a photograph |
| You need transparency | File size matters |
| Quality is priority | Image has many colors |
| Creating logos | Creating social photos |

| Use WebP When... | Use SVG When... |
|------------------|-----------------|
| Target platform supports it | You need infinite scaling |
| File size is critical | Creating icons |
| Modern web use | Creating logos |

### Video Formats

| Format | Best For | Platforms | Quality |
|--------|----------|-----------|---------|
| MP4 (H.264) | Universal video | All platforms | Excellent |
| MOV | Apple ecosystem | Most platforms | Excellent |
| WebM | Web embedding | Modern platforms | Good |
| AVI | Editing/archiving | Limited | Excellent |

**Recommended:** MP4 with H.264 codec and AAC audio is the most universally compatible format. All platforms accept it.

### Video Codec Quick Guide

| Codec | Description | Recommendation |
|-------|-------------|----------------|
| H.264 | Most compatible, good compression | Use for all exports |
| H.265/HEVC | Better compression, less compatible | Use for storage, not social |
| VP9 | Google/WebM format | Use for YouTube |
| ProRes | High quality, large files | Use for editing, not export |

### Audio Codec Quick Guide

| Codec | Description | Recommendation |
|-------|-------------|----------------|
| AAC | Most compatible, good quality | Use for all exports |
| MP3 | Universally compatible | Acceptable alternative |
| WAV | Uncompressed, large files | Use for editing only |

---

## Quality Checklist

Use this checklist before publishing any asset.

### Visual Assets

| Check | Question | Pass If... |
|-------|----------|------------|
| Resolution | Is the image high enough resolution? | At least 1080px on shortest side |
| Clarity | Is the image sharp, not blurry? | No visible pixelation |
| Text legibility | Can you read all text easily? | Text is clear on mobile screens |
| Color accuracy | Do colors match your brand? | Consistent with brand guidelines |
| Logo placement | Is your logo visible and positioned correctly? | Logo is clear, not cut off |
| Contrast | Is there enough contrast between elements? | Text stands out from background |
| Safe zones | Is important content away from edges? | Nothing critical in safe zones |

### Video Assets

| Check | Question | Pass If... |
|-------|----------|------------|
| Resolution | Is video at least 1080p? | 1920x1080 or 1080x1920 minimum |
| Duration | Is video within platform limits? | Under platform max duration |
| Audio | Is audio clear and balanced? | No distortion, consistent volume |
| Subtitles | Are subtitles accurate and readable? | Synced and legible |
| Hook | Does the first 3 seconds grab attention? | Clear value proposition |
| Branding | Is brand visible? | Logo or brand colors present |
| Safe zones | Is important content away from edges? | Nothing critical in bottom 200px for vertical |

### Campaign Assets

| Check | Question | Pass If... |
|-------|----------|------------|
| Consistency | Do all assets look like they belong together? | Same colors, fonts, style |
| Cross-platform | Are all required platforms covered? | Each platform has correct format |
| Timeline | Are assets ready for posting schedule? | All assets ready before posting dates |
| Call-to-action | Does each asset have a clear purpose? | Obvious next step for viewer |
| Accessibility | Can content be understood without audio? | Subtitles on videos, alt text ready |

---

## Glossary

### General Terms

| Term | Definition |
|------|------------|
| Asset | Any creative file produced by the system (image, video, document) |
| Campaign | A coordinated set of marketing assets with a shared goal |
| Deliverable | A specific asset requested as part of a project |
| Hero Asset | The main version of an asset, used as source for platform variants |
| Variant | A modified version of an asset for a specific platform or use |

### Platform Terms

| Term | Definition |
|------|------------|
| Aspect Ratio | The proportional relationship between width and height (e.g., 16:9, 1:1) |
| Safe Zone | Area where important content should be placed to avoid platform UI overlays |
| Feed | The main scrolling content area in a social app |
| Story | Temporary, full-screen vertical content (usually 24 hours) |
| Reel | Short-form vertical video (Instagram) |
| Short | Short-form vertical video (YouTube) |
| Carousel | Multiple images or slides in a single post (Instagram, LinkedIn) |

### Design Terms

| Term | Definition |
|------|------------|
| PNG | Portable Network Graphics; supports transparency, best for graphics |
| JPG/JPEG | Joint Photographic Experts Group; compressed format, best for photos |
| SVG | Scalable Vector Graphics; infinitely scalable, best for logos and icons |
| DPI/PPI | Dots/Pixels Per Inch; measure of print resolution |
| RGB | Red-Green-Blue; color mode for digital displays |
| CMYK | Cyan-Magenta-Yellow-Key; color mode for print |
| Hex Code | Six-character code representing a color (e.g., #FF5500) |

### Video Terms

| Term | Definition |
|------|------------|
| MP4 | MPEG-4 Part 14; most universal video format |
| Codec | Method of encoding/decoding video (e.g., H.264) |
| Bitrate | Amount of data processed per second; affects quality and file size |
| Frame Rate | Frames per second (fps); common rates are 24, 30, 60 |
| 4K | Resolution of approximately 3840 x 2160 pixels |
| 1080p | Resolution of 1920 x 1080 pixels (Full HD) |
| 720p | Resolution of 1280 x 720 pixels (HD) |
| Letterbox | Black bars added above and below video to fit different aspect ratios |
| Pillarbox | Black bars added to sides of video to fit different aspect ratios |

### Campaign Terms

| Term | Definition |
|------|------------|
| Brief | Document describing the campaign goals, deliverables, and requirements |
| Manifest | Machine-readable file listing all assets in a campaign or export |
| QC (Quality Control) | Process of verifying assets meet requirements |
| Severity Level | Classification of issue importance (Critical, Warning, Info) |
| Dispatch | Sending work to a specialist agent for production |
| Track | A parallel production path (e.g., design track, video track) |

### Agent Terms

| Term | Definition |
|------|------------|
| Aria | The Creative Director agent; orchestrates work and manages campaigns |
| Designer | The visual production agent; creates images, logos, carousels |
| Video Producer | The video production agent; creates short-form and long-form videos |
| Strategist | The research and content strategy agent; provides research and copy |
| Brand Context | Stored information about a brand (colors, fonts, style, voice) |

---

## Quick Reference Cards

### Aspect Ratios at a Glance

| Ratio | Use | Platforms |
|-------|-----|-----------|
| 1:1 | Square | Instagram Feed, LinkedIn, Twitter, Facebook |
| 4:5 | Portrait | Instagram Feed (optimal) |
| 9:16 | Vertical Full Screen | Stories, Reels, TikTok, Shorts |
| 16:9 | Horizontal Standard | YouTube, Twitter, LinkedIn Video |
| 2:3 | Pinterest Portrait | Pinterest Pins |
| 1.91:1 | Link Preview | Facebook, LinkedIn shared links |

### File Size Limits at a Glance

| Platform | Image Max | Video Max |
|----------|-----------|-----------|
| Instagram | 30 MB | 4 GB |
| TikTok | 20 MB | 500 MB (mobile), 1 GB (web) |
| YouTube | 2 MB (thumbnail) | 256 GB |
| LinkedIn | 8 MB | 5 GB |
| Twitter/X | 5 MB | 512 MB |
| Facebook | 4 MB | 10 GB |
| Pinterest | 32 MB | N/A |

---

## Getting Help

If you encounter issues not covered in this guide:

1. **Check the status file** - Campaign status files contain error messages and progress details
2. **Review the manifest** - Export manifests list warnings and skipped files
3. **Ask Aria** - Describe the issue and Aria can help troubleshoot
4. **Check platform requirements** - Platform specs change; verify current requirements

---

*This appendix is updated as platforms change their specifications. Last updated: April 2026.*