# Part 5: Video Workflows

This guide covers step-by-step workflows for creating video content with the Video Producer. Each workflow produces upload-ready MP4 files with subtitles included.

---

## Workflow 1: Short-Form Video (Reels/TikTok/Shorts)

### When to Use This

You need a vertical video (9:16 aspect ratio) between 15-60 seconds for TikTok, Instagram Reels, or YouTube Shorts. This is the most popular video format for social media -- perfect for tutorials, product demos, tips, trending content, and quick storytelling.

### Prerequisites

- Brand context loaded
- A rough idea of your content (or a script ready)
- Target platform in mind

### Platform Specifications

| Platform | Max Duration | Resolution | Aspect Ratio | Max File Size |
|----------|-------------|------------|--------------|---------------|
| TikTok | 60 seconds | 1080x1920 | 9:16 | 287 MB |
| Instagram Reels | 90 seconds | 1080x1920 | 9:16 | 250 MB |
| YouTube Shorts | 60 seconds | 1080x1920 | 9:16 | 256 MB |

### Video Types

| Type | Best For | Example |
|------|----------|---------|
| **Explainer** | Teaching something | "3 Excel Tricks You Need" |
| **Product Demo** | Showing a product | "How Our App Saves You Time" |
| **Trend-Based** | Viral formats | Popular sounds, challenges |
| **Story** | Narrative arc | "From Idea to Launch in 30 Days" |
| **List** | Quick tips | "5 Morning Habits of Successful People" |

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "Create a [platform] video about [topic]" | The Video Producer activates and asks about video type |
| 2 | Choose your video type | Explainer, demo, trend, story, or list |
| 3 | Provide content | Either paste your script OR describe key points and let the Video Producer write the script |
| 4 | Review the storyboard | Scene-by-scene breakdown with timing and visual direction |
| 5 | Production | AI generates each scene, voiceover is added, subtitles are burned in |
| 6 | Review and export | Watch the final video, request changes, then export |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/videos/shortform/
  video-title_2024-04-02.mp4       <-- Ready to upload (1080x1920)
  subtitles.srt                     <-- Optional: for manual subtitle upload
  video-manifest.json               <-- Production details
```

### Video Components Included

Every short-form video includes:

| Component | Description |
|-----------|-------------|
| **AI-Generated Scenes** | Visual content matching your script |
| **Voiceover** | AI narration (if requested) |
| **Subtitles** | Burned into the video (always on, always readable) |
| **Safe Zones** | Text placed to avoid platform UI overlays |
| **Branding** | Logo placement per your brand guidelines |

### Time Required

**15-30 minutes** for a 30-second video. Longer videos or complex scenes may take up to 45 minutes.

### End-to-End Example: Product Demo

**You**: "I need a 30-second TikTok video showing how our budgeting app helps people save money automatically"

**Video Producer**: "Great idea! What type of demo works best?
1. **Explainer** -- Walk through the feature step-by-step
2. **Before/After** -- Show the problem, then the solution
3. **Quick Tips** -- Fast-paced benefits showcase"

**You**: "Before/After -- show someone struggling with saving, then the app solving it"

**Video Producer**: "Perfect! Here's my script plan:

**0-5s (Hook)**: 'Can't seem to save money? You're not alone.' [Visual: frustrated person]
**5-20s (Problem)**: Show the struggle -- checking account, sighing, unexpected expenses
**20-28s (Solution)**: Our app automatically rounds up purchases and saves the difference
**28-30s (CTA)**: 'Link in bio to start saving today'

Want me to produce this, or adjust the script first?"

**You**: "The script is good, but make the hook punchier: 'Saving money feels impossible. Until now.'"

**Video Producer**: [Updates script and creates storyboard]

"Here's the production plan with your updated hook. Ready to generate?"

**You**: "Go for it"

**Video Producer**: [Production runs -- scenes generated, voiceover added, subtitles burned in]

"Your video is ready! Here's the 30-second MP4:
- Hook: Punchy opening
- Middle: Relatable struggle + solution demo
- End: Clear call-to-action
- Subtitles: Always visible for silent viewing

Want any changes?"

**You**: "Can you add our logo in the corner for the last 10 seconds?"

**Video Producer**: [Adds branded watermark]

"Done! Final video with logo watermark saved to `brands/yourbrand/videos/shortform/auto-savings-demo_2024-04-02.mp4`"

---

## Workflow 2: Long-Form Video (YouTube)

### When to Use This

You need a horizontal video (16:9 aspect ratio) between 1-10 minutes for YouTube, your website, or other web platforms. Long-form is ideal for tutorials, deep dives, interviews, documentaries, and content that needs more time to develop.

### Prerequisites

- Brand context loaded
- A clear topic and target duration
- Either a full script OR a detailed outline

### Platform Specifications

| Platform | Resolution | Aspect Ratio | Recommended Duration |
|----------|------------|--------------|----------------------|
| YouTube | 1920x1080 | 16:9 | 3-10 minutes |
| Web Embed | 1920x1080 | 16:9 | 1-10 minutes |
| Presentation | 1920x1080 | 16:9 | 2-5 minutes |

### Long-Form Video Structure

A well-structured long-form video follows this pattern:

| Section | Duration | Purpose |
|---------|----------|---------|
| **Hook** | 0-15 seconds | Grab attention immediately |
| **Intro** | 15-45 seconds | Introduce topic and what viewer will learn |
| **Main Content** | Variable | The core information (broken into sections) |
| **Recap** | 30-60 seconds | Summarize key points |
| **CTA** | 15-30 seconds | What to do next (subscribe, link, etc.) |

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "Create a YouTube video about [topic]" | The Video Producer activates and asks about duration and format |
| 2 | Collaborate on script | Either provide your script OR work with the Video Producer to develop one |
| 3 | Review scene plan | Scene-by-scene breakdown with visual approach for each |
| 4 | Production runs | AI generates scenes, voiceover is created, B-roll is integrated, everything is assembled |
| 5 | Review full video | Watch the complete video, request revisions |
| 6 | Finalize and export | Final MP4 with subtitles, thumbnail, and manifest |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/videos/longform/
  video-title_2024-04-02.mp4       <-- Full video (1920x1080)
  thumbnail.jpg                     <-- YouTube thumbnail suggestion
  subtitles.srt                     <-- Subtitle file
  video-manifest.json               <-- Production details
```

### Additional Outputs Available

Ask for these during your request:

| Output | How to Request |
|--------|----------------|
| **Thumbnail options** | "Generate 3 thumbnail concepts" |
| **YouTube description** | "Write the YouTube description" |
| **Tags/keywords** | "Suggest tags for this video" |
| **Chapters** | "Add timestamp chapters" |

### Time Required

**30-90 minutes** depending on video length and complexity. A 5-minute video typically takes about 45-60 minutes.

### End-to-End Example: Educational YouTube Video

**You**: "I need a 5-minute YouTube video for my cooking channel about making perfect pasta every time"

**Video Producer**: "Great topic! Let me understand the scope:
1. Who's the audience? (Beginners, home cooks, foodies?)
2. What should they learn? (Just the basics, or advanced techniques too?)
3. Any specific pasta types to cover?"

**You**: "Home cooks who struggle with pasta. Cover the 3 most common mistakes and how to fix them. Focus on spaghetti and penne."

**Video Producer**: "Perfect! Here's my script outline:

**Hook (0-15s)**: 'Your pasta is probably wrong. Here's how to fix it.'
**Intro (15-45s)**: What we'll cover -- the 3 mistakes and solutions
**Mistake 1 (45s-2min)**: Not salting the water enough -- show the difference
**Mistake 2 (2min-3:30)**: Oversaucing -- ratio demo
**Mistake 3 (3:30-4:30)**: Not reserving pasta water -- why it matters
**Recap (4:30-5min)**: Quick summary + subscribe reminder

This structure works for 5 minutes. Want me to proceed with this script, or adjust?"

**You**: "Looks good! Add a tip about checking pasta doneness in mistake 1"

**Video Producer**: [Refines script and creates detailed scene plan]

"Script updated with the doneness tip in section 1. Scene plan ready:

- Scene 1: Hook in kitchen
- Scenes 2-4: Intro graphics
- Scenes 5-8: Mistake 1 with salt comparison
- Scenes 9-12: Mistake 2 with sauce ratios
- Scenes 13-16: Mistake 3 with pasta water demo
- Scenes 17-18: Recap and CTA

Total: 18 scenes, ~5 minutes. Ready for production?"

**You**: "Let's do it"

**Video Producer**: [Production runs -- this takes 30-45 minutes for a 5-minute video]

"Your video is complete! Here's what you have:

- **5-minute MP4** at 1080p with smooth transitions
- **Subtitles** burned in for accessibility
- **Thumbnail suggestion** attached
- **Recommended title**: '3 Pasta Mistakes You're Making (And How to Fix Them)'

Saved to `brands/cookingchannel/videos/longform/perfect-pasta_2024-04-02.mp4`"

**You**: "Can you also write the YouTube description?"

**Video Producer**: "Absolutely! Here's an optimized description:

---
Do your pasta dishes turn out sticky, bland, or just... off? You're probably making one of these 3 common mistakes. In this video, I'll show you exactly how to fix them for perfect pasta every time.

**TIMESTAMPS**
0:00 - Hook
0:15 - Introduction
0:45 - Mistake #1: Water Temperature
2:00 - Mistake #2: Oversaucing
3:30 - Mistake #3: Pasta Water
4:30 - Recap

**TIPS COVERED**
- How much salt is actually enough
- The perfect pasta-to-sauce ratio
- Why pasta water is liquid gold

**INGREDIENTS USED**
- Spaghetti
- Penne
- Salt
- Your favorite sauce

#pastatips #cookingtips #homecooking

---

Want me to save this description to the video folder?"

---

## Workflow 3: Extracting Clips from Long Video

### When to Use This

You have an existing long-form video (podcast, webinar, YouTube video, interview) and want to create short clips for social media. This repurposes one piece of content into multiple platform-ready clips.

### Prerequisites

- Source video file or URL
- Brand context loaded
- An idea of what moments you want (or let AI discover them)

### Clip Detection Methods

| Method | Best For | Example |
|--------|----------|---------|
| **AI Detection** | Long content where you don't know the best moments | "Find the top 5 clips from my podcast" |
| **Timestamp Specification** | You know exactly what you want | "Clip 12:30 to 13:00" |
| **Topic Search** | Find all mentions of a topic | "Find all clips about pricing" |

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "Extract clips from [video file/URL]" | The Video Producer asks about detection method |
| 2 | Choose detection method | AI find best moments, specify timestamps, or search by topic |
| 3 | Review detected moments | The Video Producer shows each potential clip with timestamps and why it's compelling |
| 4 | Select clips | Choose which moments to produce as clips |
| 5 | Production | Each clip is extracted, reframed to vertical, subtitles added |
| 6 | Export | All clips saved with descriptive filenames |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/videos/clips/
  source-video_2024-04-02/
    clip-01_tip-about-productivity.mp4      <-- Vertical, ready for TikTok
    clip-02_key-insight-on-focus.mp4
    clip-03_funny-moment.mp4
    clip-04_inspirational-quote.mp4
    clip-manifest.json
```

### Clip-Manifest.json Contents

```json
{
  "sourceVideo": "podcast-episode-45.mp4",
  "totalDuration": "45:00",
  "clipsExtracted": 4,
  "clips": [
    {
      "filename": "clip-01_tip-about-productivity.mp4",
      "sourceTimestamp": "12:30-13:05",
      "duration": "35s",
      "reason": "Actionable productivity tip with high engagement potential",
      "platform": "tiktok, reels, shorts"
    }
  ]
}
```

### Time Required

**5-10 minutes** for AI detection and selection, then **2-5 minutes per clip** for production. A 45-minute video with 5 clips takes about 30-40 minutes total.

### End-to-End Example: Podcast to TikTok Clips

**You**: "I have a 45-minute podcast episode. Can you make TikToks from it? The file is at `podcasts/episode-45-interview.mp4`"

**Video Producer**: "I'll analyze your episode for the most compelling moments. This takes a few minutes...

[Analyzing video...]

Here are the top 5 moments I found:

| # | Timestamp | What Happens | Why It Works |
|---|-----------|--------------|--------------|
| 1 | 12:30-13:05 | Story about overcoming failure | High emotion, relatable |
| 2 | 23:45-24:15 | Productivity tip about morning routines | Actionable value |
| 3 | 31:00-31:45 | Controversial take on 4-day work weeks | Discussion starter |
| 4 | 38:20-38:50 | Funny anecdote about a client | Entertainment |
| 5 | 42:10-43:00 | Key lesson: 'Done is better than perfect' | Inspirational |

Which clips would you like me to create?"

**You**: "1, 2, and 5 please. Make them all under 45 seconds."

**Video Producer**: "Creating 3 clips from your selections...

[Production runs -- each clip is extracted, reframed to 9:16 vertical format, subtitles burned in]

**All 3 clips ready!**

- **Clip 1** (33s): Failure story -- emotional hook, great for engagement
- **Clip 2** (28s): Morning routine tip -- high save potential
- **Clip 3** (48s -- trimmed to 45s): Inspirational quote -- shareable

All clips are vertical (1080x1920) with subtitles burned in. Saved to `brands/yourbrand/videos/clips/episode-45/`"

**You**: "Perfect! Can you also make clip 2 into a horizontal version for YouTube Shorts thumbnail?"

**Video Producer**: "The clips are already vertical (9:16), which is exactly what Shorts uses. Did you want a 16:9 landscape version for regular YouTube? Or did you mean a thumbnail image?"

**You**: "Oh right, Shorts is vertical! I meant a thumbnail image for the clip"

**Video Producer**: [Generates thumbnail from best frame]

"Thumbnail saved as `clip-02_thumbnail.jpg`. It shows the guest with an engaging expression and the tip headline overlaid."

---

## Quick Reference: Which Video Workflow to Use

| I Need... | Use This Workflow |
|-----------|-------------------|
| Vertical video under 60 seconds | Short-Form Video |
| Horizontal video 1-10 minutes | Long-Form Video |
| Multiple clips from one long video | Extract Clips |
| Same video for multiple platforms | Create once, then ask for platform exports |

---

## Platform Export Variants

After creating any video, you can request platform-specific exports:

**You**: "Export this for all short-form platforms"

**Video Producer**: Creates:
- `video_tiktok.mp4` (same as original if already vertical)
- `video_reels.mp4` (same format, separate file for tracking)
- `video_shorts.mp4` (same format, separate file for tracking)

For long-form to short-form conversion:

**You**: "Make a 60-second TikTok version of my 5-minute YouTube video"

**Video Producer**: Extracts the best moments, creates a condensed version in vertical format.

---

## Troubleshooting

### The video generation is taking too long

AI video generation is inherently slow. A 30-second video with multiple scenes can take 15-30 minutes. This is normal. The Video Producer saves progress regularly so work is not lost.

### The AI-generated scenes do not match my vision

Be specific in your descriptions. Instead of "show someone cooking," say "overhead shot of hands chopping vegetables on a wooden board, warm lighting, modern kitchen."

### I want to use my own footage instead of AI generation

Provide the file path: "Use my footage at `videos/raw/my-video.mp4` for the opening scene." The Video Producer will incorporate your clips.

### The subtitles are hard to read

The Video Producer positions subtitles in safe zones, but you can request adjustments: "Make subtitles larger" or "Add a dark background behind subtitles."

### I need music in my video

Provide the audio file: "Add background music from `audio/upbeat-track.mp3` at 20% volume." The Video Producer will mix it in during assembly.

---

## Video Quality Checklist

Before exporting, the Video Producer verifies:

- [ ] Resolution matches platform specs (1080x1920 or 1920x1080)
- [ ] Codec is H.264 for universal compatibility
- [ ] Duration is within platform limits
- [ ] File size is under platform maximum
- [ ] Subtitles are burned in and readable
- [ ] Audio levels are normalized
- [ ] Brand elements (logo, colors) are applied correctly

---

## Video Best Practices

### The First 3 Seconds Matter Most

On TikTok and Reels, viewers scroll past content in under 3 seconds. Your hook must grab attention immediately.

**Good hooks**:
- A surprising statement: "You've been doing this wrong your whole life"
- A compelling question: "What if I told you..."
- A visual intrigue: Something unexpected happening on screen
- A clear promise: "In 30 seconds, you'll learn..."

**Bad hooks**:
- Slow introductions
- Long logo animations
- Unrelated content before the main topic
- Anything that doesn't immediately relate to the title/topic

### Subtitles Are Non-Negotiable

**Why subtitles matter**:
- 85% of social videos are watched without sound
- Subtitles increase watch time by 25-40%
- They make content accessible to hearing-impaired viewers
- Many viewers scroll in sound-sensitive environments

**Subtitle best practices**:
- Maximum 2 lines per screen
- Large, readable font (minimum 24px)
- High contrast with background
- Positioned in safe zone (not covered by platform UI)

### Pacing and Energy

**Short-form video pacing**:
- Cut to a new scene every 2-5 seconds
- Vary shot types (close-up, medium, wide)
- Use transitions purposefully, not randomly
- Match visual energy to the content

**Long-form video pacing**:
- Front-load value -- don't save the good stuff for the end
- Use "pattern interrupts" every 2-3 minutes (visual changes, on-screen text, etc.)
- Break content into clear sections with transitions
- Recap key points at the end

### Sound Design

Even for AI-generated videos, sound matters:

| Audio Element | Purpose | How to Request |
|---------------|---------|----------------|
| **Background music** | Sets mood and energy | "Add upbeat background music at low volume" |
| **Sound effects** | Emphasize key moments | "Add a 'ding' sound when the tip appears" |
| **Voiceover** | Narration and explanation | "Use a calm, professional voice for narration" |
| **Silence** | Emphasis and breathing room | "Add a 1-second pause before the reveal" |

---

## Common Mistakes to Avoid

### Mistake 1: No Hook

**Problem**: Starting with "Hi, I'm [name] and today we're going to talk about..." causes viewers to scroll past.

**Solution**: Start with the most interesting moment or a compelling statement.

**Example**:
- **Bad**: "Hi everyone, welcome back to my channel. Today I want to share some tips about productivity."
- **Good**: "This one habit doubled my productivity in 30 days."

### Mistake 2: Too Long for Platform

**Problem**: A 55-second video on TikTok loses viewers. A 90-second YouTube Short can't be uploaded.

**Solution**: Match video length to platform expectations.

| Platform | Optimal Length | Maximum |
|----------|---------------|---------|
| TikTok | 21-34 seconds | 60 seconds |
| Instagram Reels | 15-30 seconds | 90 seconds |
| YouTube Shorts | 30-45 seconds | 60 seconds |
| YouTube Long-form | 5-10 minutes | No hard limit |

### Mistake 3: No Call-to-Action

**Problem**: Viewers watch your video but don't know what to do next.

**Solution**: End with a clear CTA.

**Effective CTAs**:
- "Follow for more tips like this"
- "Save this video for later"
- "Link in bio to learn more"
- "Comment below with your experience"

### Mistake 4: Inconsistent Branding

**Problem**: Each video looks like it's from a different creator.

**Solution**: Maintain consistent:
- Intro/outro sequences
- Color palette
- Logo placement
- Typography for subtitles and text overlays
- Voiceover style/tone

### Mistake 5: Ignoring Safe Zones

**Problem**: Important content gets covered by platform UI (buttons, text, profile pictures).

**Solution**: Keep critical elements in the center of the frame.

**Safe zone guidelines**:
- **TikTok**: Avoid right side (interaction buttons) and bottom (caption area)
- **Reels**: Avoid bottom 15% and right side
- **Shorts**: Avoid bottom (title/description) and right side (subscribe button)

---

## Advanced Techniques

### Creating a Video Series

Series perform well because they bring viewers back for the next episode.

**To create a series**:

**You**: "I want a 5-part YouTube series about building healthy habits. Each episode should be 3-4 minutes."

**Video Producer**: "I'll create a consistent structure for the series:
- Same intro/outro for all episodes
- Consistent visual style across all episodes
- Sequential episode numbering
- A 'next episode' teaser at the end of each

What are the 5 habit topics?"

### B-Roll Integration

B-roll is supplementary footage that covers voiceover or adds visual variety.

**When to use B-roll**:
- During voiceover narration
- To show examples of what you're discussing
- To break up a talking head shot
- To illustrate abstract concepts

**To request B-roll**:

**You**: "For the section about morning routines, add B-roll of someone making coffee, stretching, and writing in a journal."

**Video Producer**: Will source appropriate footage and integrate it into the scene.

### Custom Thumbnails

Thumbnails are critical for YouTube -- they're often the deciding factor in whether someone clicks.

**Thumbnail best practices**:
- High contrast, readable text
- Expressive faces (surprise, excitement)
- Bright, eye-catching colors
- Consistent style across all videos
- Text limited to 3-5 words

**To request thumbnails**:

**You**: "Generate 3 thumbnail options for this video. Make the title pop and include an expressive reaction shot."

### Multi-Platform Repurposing

One video can become many:

| Source | TikTok | Reels | Shorts | YouTube |
|--------|--------|-------|--------|---------|
| Long-form video | Extract clips | Extract clips | Extract clips | Full video |
| Short-form video | Post directly | Post directly | Post directly | N/A (too short) |
| Podcast | Extract clips | Extract clips | Extract clips | Full audio + visuals |

**To request repurposing**:

**You**: "I have a 10-minute YouTube video. Create: 3 TikTok clips, 1 Reel from the best section, and a 60-second Shorts summary."

---

## Working with the Video Producer: Tips and Tricks

### Describing Visual Scenes

Be specific about what you want to see:

| Vague Request | Better Request |
|---------------|----------------|
| "Show a person working" | "Overhead shot of a person typing on a laptop in a bright, modern home office with plants" |
| "Make it look professional" | "Use clean, minimal aesthetic with white background, subtle shadows, and smooth camera movements" |
| "Show the product" | "Close-up of the product on a wooden table, rotating slowly to show all angles, soft lighting" |

### Script Writing Tips

When providing scripts:

1. **Write for speaking, not reading**: Use contractions, short sentences, conversational tone
2. **Include visual notes**: [Visual: product close-up] or [Cut to: user smiling]
3. **Time your script**: Read it aloud to check duration
4. **Front-load value**: Put the most important information early

**Example script format**:

```
[0-5s] HOOK: "You've been charging your phone wrong."
[Visual: person frustrated with dead phone]

[5-15s] PROBLEM: "Most people wait until 0% to charge..."
[Visual: battery icon at 0%]

[15-45s] SOLUTION: "Here's the right way..."
[Visual: charging demonstration]

[45-60s] CTA: "Follow for more tech tips."
[Visual: follow button animation]
```

### Iterative Refinement

Videos are easier to refine than create from scratch. After your first version:

**You**: "The pacing feels slow. Can you trim the intro to 10 seconds?"

**Video Producer**: Adjusts the edit and re-exports.

**You**: "The middle section needs more visual variety."

**Video Producer**: Adds B-roll or scene changes.

### Using Headless Mode

For batch production or when you know exactly what you want, use headless mode:

**You**: "Create a 30-second TikTok about our new product launch in headless mode. Brand: Thrive. Key message: New app helps you build habits. CTA: Link in bio."

**Video Producer**: Produces the entire video without asking questions, using best practices and brand context.

---

## Video Performance Checklist

Before considering a video complete:

**Technical Quality**:
- [ ] Resolution is correct (1080x1920 for short-form, 1920x1080 for long-form)
- [ ] File size is under platform maximum
- [ ] Video plays smoothly without stuttering
- [ ] Audio is clear and at consistent volume
- [ ] Subtitles are readable and in sync

**Content Quality**:
- [ ] Hook grabs attention in first 3 seconds
- [ ] Message is clear and easy to understand
- [ ] CTA tells viewers what to do next
- [ ] Brand elements are present but not overwhelming
- [ ] Video length matches platform expectations

**Engagement Optimization**:
- [ ] Text in safe zones (not covered by UI)
- [ ] Visual variety throughout (no static 10-second shots)
- [ ] Energy matches platform culture
- [ ] Subtitles work for silent viewing

---

## Next Steps

- **Part 6**: Learn how to orchestrate multi-asset campaigns
- **Part 7**: Reference appendices with platform specs and troubleshooting
- **Skill Reference**: Detailed capability list for each video skill