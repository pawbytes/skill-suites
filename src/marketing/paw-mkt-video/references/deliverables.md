# Deliverables & Outputs

## Purpose
Define standard deliverable formats, file naming, and save paths for all video marketing outputs.

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** -- working within a named campaign:
- Save to: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/video/content/`
- Read campaign strategy at: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
- Save to: `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/video/content/`

**Legacy fallback** -- old directory structure detected:
- Save to: `./.pawbytes/marketing-suites/brands/{brand-slug}/content/video/`
- Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## File Organization

```
## Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/video/content/
  video-calendar-{YYYY-MM}.md
  youtube-strategy-{YYYY-MM-DD}.md
  scripts/
    script-{slug}-{YYYY-MM-DD}.md
  briefs/
    video-brief-{slug}-{YYYY-MM-DD}.md

## Standalone mode (default for evergreen work):
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/video/content/
  video-calendar-{YYYY-MM}.md
  youtube-strategy-{YYYY-MM-DD}.md
  scripts/
    script-{slug}-{YYYY-MM-DD}.md
  briefs/
    video-brief-{slug}-{YYYY-MM-DD}.md
  storyboards/
    storyboard-{slug}-{YYYY-MM-DD}.md
  ad-scripts/
    ad-script-{platform}-{slug}-{YYYY-MM-DD}.md
  performance/
    monthly-report-{YYYY-MM}.md
```

---

## Deliverable Types

### 1. Video Script

**Filename**: `./scripts/script-{slug}-{YYYY-MM-DD}.md`

**Sections**:
- Meta (platform, length, type, audience, objective)
- Script table (timecode, visual, audio/dialogue)
- B-Roll List
- Music/Sound Effects
- Text Overlays
- CTA
- Thumbnail Concept
- Distribution Plan

### 2. Video Content Calendar

**Filename**: `video-calendar-{YYYY-MM}.md`

**Sections**:
- Monthly Theme
- Platforms
- Key Dates
- Weekly Breakdown table (day, platform, format, topic, hook, script status, asset status)
- Production Schedule table (batch, shoot date, videos, location)
- Repurposing Plan table (source, derivative, platform, date)

### 3. YouTube Channel Strategy

**Filename**: `youtube-strategy-{YYYY-MM-DD}.md`

**Sections**:
- Channel Positioning
- Content Pillars table
- Upload Schedule
- Branding (banner, profile, trailer, playlists)
- SEO Approach
- Thumbnail Style Guide
- Growth Plan (Month 1-3, 4-6, 7-12)
- KPIs and Targets table
- Shorts Strategy
- Community Engagement Plan

### 4. Video Brief

**Filename**: `briefs/video-brief-{slug}-{YYYY-MM-DD}.md`

**Sections**:
- Objective
- Platform and Format
- Target Audience
- Key Message
- Hook Concept
- Talking Points/Outline
- Visual Direction
- Music/Audio Direction
- CTA
- References
- Production Notes (location, talent, equipment, timeline)
- Distribution Plan

### 5. Storyboard Outline

**Filename**: `storyboards/storyboard-{slug}-{YYYY-MM-DD}.md`

**Sections**:
- Video Meta (platform, length, type, audience)
- Scene Breakdown (per scene: visual, audio, text overlay, camera angle/movement)
- Transition Notes
- Production Requirements

### 6. Ad Script

**Filename**: `ad-scripts/ad-script-{platform}-{slug}-{YYYY-MM-DD}.md`

**Sections**:
- Platform and Format
- Campaign Objective
- Target Audience
- Script (timecoded)
- Production Direction (UGC vs polished)
- Creative Refresh Schedule

### 7. Performance Report

**Filename**: `performance/monthly-report-{YYYY-MM}.md`

**Sections**:
- Executive Summary
- Key Metrics by Platform
- Top Performing Videos
- Retention Analysis
- Ad Performance (if applicable)
- Recommendations for Next Month

---

## Output Contract

Every video marketing deliverable includes:
- **Video type**: short-form, long-form, live stream, ad, or explainer
- **Platform**: TikTok, Instagram Reels, YouTube, YouTube Shorts, etc.
- **Script/outline**: complete script or structured outline with hooks and CTAs
- **Production notes**: format specs, duration, visual direction, audio guidance
- **Distribution plan**: where and when to publish
- **File saved to**: path where the deliverable was written