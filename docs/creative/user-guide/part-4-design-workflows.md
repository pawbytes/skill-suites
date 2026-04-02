# Part 4: Design Workflows

This guide covers step-by-step workflows for creating visual assets with the Designer. Each workflow produces upload-ready files saved to your brand folder.

---

## Workflow 1: Single Social Post

### When to Use This

You need one visual post for a specific social media platform. This is the most common design task -- perfect for announcements, promotions, quotes, or any single-image social content.

### Prerequisites

- Your brand context loaded (the Designer loads this automatically when you mention your brand)
- A rough idea of what you want to post

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "Create an Instagram post for [brand name] about [topic]" | The Designer activates and loads your brand context |
| 2 | Describe your message or paste your copy | The Designer asks clarifying questions if needed (style preferences, specific text, call-to-action) |
| 3 | Review the generated preview | The Designer shows you the image at exact platform dimensions |
| 4 | Request changes (optional) | Type feedback like "make the text larger" or "try a different background" -- the Designer revises |
| 5 | Confirm and export | Type "looks good" or "export it" -- the file is saved to your brand folder |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/assets/social/
  instagram_post_2024-04-02.png     <-- Ready to upload
  design-manifest.json              <-- Record of what was created
```

### Platform Dimensions Reference

| Platform | Dimensions | Aspect Ratio |
|----------|------------|--------------|
| Instagram Feed | 1080x1350 px | 4:5 (portrait) |
| Instagram Square | 1080x1080 px | 1:1 (square) |
| LinkedIn | 1200x627 px | 1.91:1 (landscape) |
| Twitter/X | 1200x675 px | 16:9 (landscape) |
| Facebook | 1200x630 px | 1.91:1 (landscape) |
| TikTok | 1080x1920 px | 9:16 (vertical) |

### Time Required

**5-10 minutes** from request to final file.

### End-to-End Example: Product Launch Post

**You**: "Create an Instagram post for my coffee shop Morning Brew about our new lavender latte launching tomorrow"

**Designer**: "I'll create that for Morning Brew. A few quick questions:
1. Any specific text you want on the post?
2. Should I include the price?
3. What vibe -- minimal/cozy/bold?"

**You**: "Text: 'Lavender Latte -- Available Tomorrow'. No price. Cozy, warm aesthetic."

**Designer**: [Generates the post with brand colors and cozy styling]

"Here's your post! The lavender colors complement your brand's earth tones. Want any adjustments?"

**You**: "Can you make 'Tomorrow' bigger?"

**Designer**: [Revises with larger emphasis on 'Tomorrow']

"Updated! Ready to export?"

**You**: "Looks good, export it"

**Designer**: "Done! Saved to `brands/morning-brew/assets/social/instagram_post_2024-04-02.png`"

---

## Workflow 2: Instagram Carousel

### When to Use This

You want to tell a story, share a list, or provide step-by-step content across multiple slides. Carousels get higher engagement because people swipe through them, spending more time with your content.

### Prerequisites

- Brand context loaded
- An idea of your content structure (listicle, tutorial, or story)

### Carousel Formats

| Format | Best For | Example |
|--------|----------|---------|
| **Listicle** | Tips, mistakes, reasons | "5 Ways to Save Money" |
| **Tutorial** | How-to guides | "How to Brew the Perfect Cup" |
| **Story** | Narrative journeys | "Our Journey from Garage to 50 Stores" |
| **Showcase** | Product/features | "Meet Our New Collection" |

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "Create an Instagram carousel about [topic]" | The Designer activates and asks about format |
| 2 | Choose your format | Listicle, tutorial, story, or showcase |
| 3 | Provide content for each slide | Main headline, key points per slide, call-to-action for final slide |
| 4 | Review all slides | The Designer shows each slide with consistent branding across all |
| 5 | Request changes (optional) | Adjust individual slides or overall styling |
| 6 | Confirm and export | All slides saved with numbered filenames for easy upload |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/assets/social/carousels/
  instagram_carousel_topic_2024-04-02_slide01.png   <-- Upload first
  instagram_carousel_topic_2024-04-02_slide02.png
  instagram_carousel_topic_2024-04-02_slide03.png
  instagram_carousel_topic_2024-04-02_slide04.png
  instagram_carousel_topic_2024-04-02_slide05.png   <-- Upload last
  design-manifest.json
```

### Pro Tips

- **Upload in order**: Slides are numbered for a reason. Upload slide01 first.
- **First slide matters**: This is what people see in their feed. Make it compelling.
- **Final slide = CTA**: Always end with what you want people to do next.
- **Keep it consistent**: The Designer maintains the same style across all slides automatically.

### Time Required

**10-15 minutes** for a 5-slide carousel.

### End-to-End Example: Tips Carousel

**You**: "I need a 5-slide Instagram carousel for my fitness brand about morning workout tips"

**Designer**: "Great topic! Which format works best?
1. Listicle: '5 Morning Workout Tips'
2. Tutorial: 'How to Build a Morning Workout Habit'
3. Story: 'My Morning Routine Transformation'"

**You**: "Listicle -- 5 tips"

**Designer**: "Perfect. What are your 5 tips? Also, what should the final call-to-action say?"

**You**: "Tips: 1) Prep clothes the night before, 2) Drink water first, 3) Start with stretching, 4) No phone for 30 mins, 5) Celebrate small wins. CTA: 'Save this for tomorrow morning!'"

**Designer**: [Creates all 5 slides with consistent styling]

"Here's your carousel! Each tip has its own slide with your brand colors. The final slide has the save reminder. Any adjustments?"

**You**: "Can you add a swipe indicator on slides 1-4?"

**Designer**: [Adds "Swipe for more -->" on slides 1-4]

"Updated! Ready to export?"

**You**: "Perfect, export it"

**Designer**: "Done! 5 slides saved to `brands/fitlife/assets/social/carousels/`. Upload slide01 first!"

---

## Workflow 3: Brand Logo

### When to Use This

You are starting a new brand, refreshing your visual identity, or need a logo for a sub-brand, product line, or campaign. This workflow produces professional logo files in multiple formats.

### Prerequisites

- A clear idea of your brand or product name
- Some sense of the style you want (the Designer can help you explore)

### Logo Types

| Type | Description | Best For |
|------|-------------|----------|
| **Pictorial** | Icon + brand name | Brands wanting a recognizable symbol |
| **Wordmark** | Styled text only | Brands with distinctive names |
| **Abstract** | Geometric/abstract mark | Modern, minimal brands |
| **Combination** | Icon + text that work together | Most brands -- versatile |

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "Create a logo for [brand name]" | The Designer activates and asks discovery questions |
| 2 | Answer style questions | What does your brand do? What feeling should it convey? Any style preferences? |
| 3 | Review logo options | The Designer generates 3-5 different options for you to choose from |
| 4 | Select and refine | Pick your favorite and request adjustments |
| 5 | Finalize | The Designer exports in multiple formats for all use cases |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/assets/brand-identity/logo/
  logo-full-color-512.png       <-- Digital use, smaller
  logo-full-color-1024.png      <-- Digital use, larger
  logo-full-color.svg           <-- Scalable vector (infinite size)
  logo-white.png                <-- For dark backgrounds
  logo-black.png                <-- For light backgrounds
  logo-monochrome.svg           <-- Single color version
  design-manifest.json
```

### Logo File Formats Explained

| Format | Use Case |
|--------|----------|
| **PNG** | Digital -- websites, social media, presentations |
| **SVG** | Scalable -- print, large signs, any size |
| **White/Black** | Versatility -- works on any background |

### Time Required

**15-25 minutes** including exploration and refinement.

### End-to-End Example: New Business Logo

**You**: "Create a logo for my new business called 'Thrive' -- it's a wellness coaching practice"

**Designer**: "Exciting! I'd love to help create your logo. A few questions:

1. What makes Thrive different from other wellness coaches?
2. What feeling should the logo evoke? (calm, energetic, premium, approachable?)
3. Any colors you're drawn to or want to avoid?
4. Any symbols that resonate? (plants, sun, abstract shapes?)"

**You**: "I focus on sustainable lifestyle changes, not quick fixes. The logo should feel calm but empowering. I like greens and earth tones, no neon. A leaf or growth symbol could work."

**Designer**: [Generates 4 logo options]

"Here are 4 directions:
1. **Growth** -- Leaf icon with modern wordmark
2. **Balance** -- Abstract circular form suggesting wholeness
3. **Rise** -- Upward-pointing leaf with elegant typography
4. **Root** -- Tree/leaf combination with grounded feel

Which resonates most?"

**You**: "I love option 3, Rise! Can you make the leaf a bit more minimal and try a darker green?"

**Designer**: [Refines option 3]

"Updated! The leaf is now simpler and I've used a forest green from your preferred palette. How's this?"

**You**: "Perfect! Export it"

**Designer**: "Done! You now have:
- Full color PNG (2 sizes) for digital use
- SVG vector for print and scaling
- White and black versions for any background

All saved to `brands/thrive/assets/brand-identity/logo/`"

---

## Workflow 4: Batch Content Creation

### When to Use This

You have a content calendar or need multiple assets for a campaign. Instead of creating each post individually, you describe everything at once and the Designer produces all assets in one organized batch.

### Prerequisites

- A content calendar, campaign brief, or list of posts needed
- Brand context loaded

### Steps

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Say: "I need batch content for [time period/campaign]" | The Designer asks for your content calendar or brief |
| 2 | Share your content plan | Paste your calendar, describe your posts, or upload a brief file |
| 3 | Confirm the production queue | The Designer shows you a summary: how many posts, which platforms, what content |
| 4 | Production runs | All assets are created with consistent branding |
| 5 | Review the batch | All posts organized by date and platform |
| 6 | Export | Everything saved to an organized folder structure |

### What You Get

```
.pawbytes/creative-suites/brands/your-brand/campaigns/april-content/batch-2024-04-02/
  instagram/
    2024-04-03_product-launch.png
    2024-04-04_tip-tuesday.png
    2024-04-05_behind-scenes.png
  linkedin/
    2024-04-03_announcement.png
    2024-04-04_industry-insight.png
  tiktok/
    2024-04-03_product-teaser.png
  batch-manifest.json              <-- Machine-readable record of all assets
```

### Batch-Manifest.json Contents

The manifest file tracks every asset produced:

```json
{
  "campaign": "april-content",
  "brand": "your-brand",
  "created": "2024-04-02",
  "totalAssets": 6,
  "platforms": ["instagram", "linkedin", "tiktok"],
  "assets": [
    {
      "filename": "2024-04-03_product-launch.png",
      "platform": "instagram",
      "dimensions": "1080x1350",
      "status": "success"
    }
  ]
}
```

### Time Required

**Varies by batch size**: Approximately 5 minutes per asset (vs. 10+ minutes individually). A week's worth of content (10-15 posts) takes about 45-60 minutes.

### End-to-End Example: Weekly Content Batch

**You**: "I need social posts for next week. Here's my content calendar:

**Monday**: Product launch announcement -- Instagram + LinkedIn
**Tuesday**: Tip Tuesday about productivity -- Instagram + TikTok
**Wednesday**: Behind the scenes photo -- Instagram
**Thursday**: Customer testimonial quote -- Instagram + LinkedIn
**Friday**: Weekend mood/fun post -- Instagram"

**Designer**: "Got it! Let me confirm the production queue:

| Day | Platform | Content |
|-----|----------|---------|
| Mon | Instagram, LinkedIn | Product launch |
| Tue | Instagram, TikTok | Productivity tip |
| Wed | Instagram | Behind the scenes |
| Thu | Instagram, LinkedIn | Testimonial quote |
| Fri | Instagram | Weekend mood |

**Total: 8 posts across 3 platforms**

Ready to produce all 8?"

**You**: "Yes, and for the testimonial, use this quote: 'This changed how I work -- Sarah M.'"

**Designer**: "Perfect! Starting batch production...

[Production runs -- each asset generated with consistent brand styling]

**Batch complete!** All 8 posts created:

- Instagram: 5 posts
- LinkedIn: 2 posts
- TikTok: 1 post

All files saved to `brands/yourbrand/campaigns/weekly-content/batch-2024-04-02/`

Any posts need revision, or does everything look good?"

**You**: "Can you make the Monday LinkedIn post more professional, less colorful?"

**Designer**: [Revises that specific post]

"Updated! The LinkedIn announcement now has a more corporate feel while keeping brand consistency."

**You**: "Perfect, that's everything"

**Designer**: "All set! Your weekly content is ready. Each file is named by date for easy scheduling."

---

## Quick Reference: Which Workflow to Use

| I Need... | Use This Workflow |
|-----------|-------------------|
| One post for one platform | Single Social Post |
| Multiple slides for one post | Instagram Carousel |
| A logo or brand mark | Brand Logo |
| Multiple posts at once | Batch Content Creation |

---

## Troubleshooting

### The Designer asks too many questions

If you want faster results, provide more detail upfront:

**Vague**: "Create a post"
**Better**: "Create an Instagram post for [brand] about [topic] with [text] in [style]"

### The generated image does not match my brand

The Designer loads brand context automatically, but if you have not set up brand guidelines yet, say: "Use these brand colors: [colors] and this style: [description]"

### I need the same post for multiple platforms

After creating a post, say: "Export this for [other platform] too" -- the Designer will resize and adjust for the new platform.

### I want to edit a generated image

Describe exactly what to change: "Make the headline larger" or "Move the logo to the top right" or "Change the background color to blue."

---

## Design Best Practices

### Text on Images

- **Minimum font size**: 24px for readability on mobile
- **Contrast ratio**: 4.5:1 minimum between text and background
- **Text-safe zones**: Keep important text away from edges (20px minimum)
- **Line length**: Maximum 2-3 lines per section for social posts

### Color and Contrast

- **Brand colors first**: Always use your brand's primary colors
- **Avoid pure black on white**: Use dark gray (#333) instead for softer contrast
- **Test on mobile**: Colors appear differently on phone screens vs. monitors
- **Accessibility**: Ensure sufficient contrast for visually impaired users

### Image Composition

- **Rule of thirds**: Position key elements at intersection points
- **Negative space**: Leave breathing room around text and logos
- **Visual hierarchy**: Most important element should be largest/brightest
- **Consistent style**: All posts in a series should feel cohesive

### Platform-Specific Tips

| Platform | Do | Don't |
|----------|-----|-------|
| Instagram | Use portrait (4:5) for more screen space | Put text near bottom (covered by caption) |
| LinkedIn | Keep it professional, minimal colors | Use trendy fonts or slang |
| TikTok | Bold, high-contrast visuals | Small text (hard to read on phone) |
| Twitter/X | Simple, single focal point | Busy backgrounds with text |

---

## Common Mistakes to Avoid

### Mistake 1: Too Much Text

**Problem**: Cramming paragraphs of text onto an image makes it unreadable on mobile.

**Solution**: Limit to 10-15 words maximum per social post. Use carousels for more content.

**Example**:
- **Bad**: "We are excited to announce that our new product is launching next week on Tuesday at 9am and it's going to be amazing!"
- **Good**: "New Product. Tuesday 9am."

### Mistake 2: Ignoring Safe Zones

**Problem**: Text gets cut off by platform UI (profile picture, timestamps, buttons).

**Solution**: Keep important content in the center 80% of the image.

**Platform Safe Zones**:
- Instagram Feed: Avoid bottom 100px
- TikTok: Avoid right side (interaction buttons)
- LinkedIn: Avoid bottom 80px (engagement buttons)

### Mistake 3: Inconsistent Branding

**Problem**: Each post looks like it's from a different company.

**Solution**: Always use brand colors, fonts, and logo placement consistently. The Designer handles this automatically when brand context is loaded.

### Mistake 4: Wrong Dimensions

**Problem**: Image gets cropped awkwardly or has black bars.

**Solution**: Specify your platform upfront, or reference the dimensions table above.

### Mistake 5: Low Contrast

**Problem**: Text is hard to read against the background.

**Solution**: Add a semi-transparent overlay behind text, or use text with a drop shadow.

---

## Advanced Techniques

### Creating Visual Consistency Across Posts

For a cohesive feed, use these techniques:

1. **Template approach**: Use the same layout structure for recurring post types
2. **Color coding**: Different content types use different accent colors from your palette
3. **Signature element**: Always include a small brand mark or pattern
4. **Consistent filters**: Apply the same style treatment to all photos

**To request this**: "Create a template for my weekly tip posts that I can reuse"

### Designing for Accessibility

Make your content accessible to everyone:

- **Alt text**: Describe the image for screen readers (ask the Designer to generate this)
- **High contrast**: Ensure text is readable
- **Avoid text-in-image only**: Critical information should be in the caption too
- **Color blindness**: Don't rely on color alone to convey meaning

**To request this**: "Add alt text for accessibility" after generating an image

### A/B Testing Variations

Create multiple versions to test which performs better:

**You**: "Create 3 variations of this post: one with the headline at the top, one in the center, and one at the bottom"

**Designer**: Creates all 3 versions for you to test

### Seasonal and Thematic Updates

Refresh your visuals for seasons, holidays, or campaigns:

**You**: "Update my logo with a holiday theme for December -- subtle snow or winter elements"

**Designer**: Creates a seasonal variant while maintaining brand recognition

---

## Working with the Designer: Tips and Tricks

### Getting Faster Results

Provide complete briefs to reduce back-and-forth:

**Complete Brief Example**: "Create an Instagram post for Thrive Wellness about our new meditation class starting next Monday. Text: 'Find Your Calm - Mondays 7pm'. Use brand colors (sage green, cream). Style: minimal, serene. Include subtle lotus icon."

This gives the Designer everything needed in one message.

### Describing Visual Style

Use specific style keywords:

| Style | Keywords to Use |
|-------|-----------------|
| Minimal | Clean, simple, whitespace, modern |
| Bold | High contrast, large text, vibrant |
| Cozy | Warm tones, soft, inviting |
| Professional | Corporate, clean, structured |
| Playful | Fun, colorful, rounded shapes |
| Premium | Elegant, sophisticated, refined |

### Revision Requests

Be specific about what to change:

| Vague Request | Better Request |
|---------------|----------------|
| "Make it pop" | "Increase the contrast and make the headline 20% larger" |
| "Change the vibe" | "Make it feel more premium -- use darker colors and elegant typography" |
| "Fix the text" | "Move the subtext up 30px and change it to white" |

### Requesting Variations

After getting a design you like:

- "Show me this with a different background"
- "Try it with the logo in the top right instead"
- "Make a version without the icon"
- "Create a landscape version for LinkedIn"

---

## Platform-Specific Deep Dives

### Instagram

Instagram is a highly visual platform where aesthetics matter enormously.

**Feed Posts**:
- Portrait (4:5) gives 25% more screen space than square
- Text should be minimal -- save details for the caption
- Carousel posts get 1.4x more reach than single images

**Stories**:
- 1080x1920 (full screen vertical)
- Interactive elements (polls, questions, sliders) boost engagement
- Design for sound-off viewing

**Reels Cover**:
- 1080x1920 but the visible area is 1080x1350 in profile
- Choose a frame that looks good as a thumbnail

### LinkedIn

Professional audience expects professional visuals.

**Best Practices**:
- Use more restrained color palettes
- Keep text professional and industry-appropriate
- Data visualization (charts, graphs) performs well
- Avoid trendy fonts or overly casual language

**Dimensions**:
- Feed post: 1200x627 (landscape) or 1080x1080 (square)
- Carousel: 1080x1080 per slide (PDF format also accepted)

### TikTok

TikTok has its own visual language that differs from other platforms.

**TikTok Aesthetic**:
- Bold, high-contrast visuals work best
- Text overlays are expected and encouraged
- Fast-paced visual changes match the platform's energy
- Less polished, more authentic content often performs better

**Safe Zones**:
- Right side: Interaction buttons (like, comment, share)
- Bottom: Caption and sound information
- Left: Profile picture and follow button

### Twitter/X

Twitter images are seen briefly in a fast-moving feed.

**Best Practices**:
- Single, clear focal point
- Minimal text (people scroll quickly)
- High contrast for small-screen viewing
- Memes and timely content perform well

**Dimensions**:
- 1200x675 (16:9 landscape)
- Images appear cropped in feed; tap to see full image

---

## Output File Reference

### Design Manifest Schema

Every design workflow produces a `design-manifest.json` that tracks what was created:

```json
{
  "workflow": "paw-cra-design-social",
  "brand": "your-brand",
  "created": "2024-04-02T14:30:00Z",
  "assets": [
    {
      "type": "social-post",
      "platform": "instagram",
      "filename": "instagram_post_2024-04-02.png",
      "dimensions": "1080x1350",
      "fileSize": "245KB",
      "colorMode": "RGB"
    }
  ],
  "validation": {
    "brandConsistency": "pass",
    "platformSpecs": "pass"
  }
}
```

### Folder Structure Overview

```
.pawbytes/creative-suites/
  brands/
    {your-brand}/
      assets/
        brand-identity/
          logo/
          icons/
          avatars/
        social/
          posts/
          carousels/
          stories/
        flyers/
        banners/
      campaigns/
        {campaign-name}/
          assets/
          brief.md
          status.md
  daily/
    2024-04-02.md
```

---

## Next Steps

- **Part 5**: Learn video workflows for TikTok, Reels, and YouTube
- **Part 6**: See how campaigns combine multiple assets
- **Part 7**: Reference appendices with platform specs and troubleshooting
- **Skill Reference**: Detailed capability list for each design skill