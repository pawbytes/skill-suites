# Carousel Design

## Outcome

Create multi-slide posts that tell a story, teach a concept, or showcase products through sequential visual narrative with consistent styling across all slides.

## Trigger

User requests a carousel, slide deck, multi-slide post, or sequential visual story.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Script/storyboard | Brief or Strategist output | Yes |
| Platform | User specification | Yes |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | Yes |
| Number of slides | User specification or deduced from content | Yes |

## Process

### 1. Analyze Content Structure

Determine optimal carousel structure from the content:

| Pattern | Best For | Structure |
|---------|----------|-----------|
| Problem → Solution → Proof | Persuasive content | Hook → Solution steps → Results → CTA |
| Listicle | Tips, features, recommendations | Title → One item per slide → Summary/CTA |
| Tutorial | How-to content | Outcome preview → Steps → Final result → CTA |
| Myth vs Fact | Educational content | Myth statement → Reveal truth → Repeat |
| Transformation | Before/after, progressions | Before → Process → After → CTA |

### 2. Define Specifications

Reference `./platform-specifications.md` for full details:

| Platform | Dimensions | Max Slides |
|----------|------------|------------|
| Instagram Carousel | 1080×1080px or 1080×1350px | 20 |
| LinkedIn PDF Carousel | 1080×1080px or 1920×1080px | 10 |

**Critical:** All slides must have identical aspect ratio.

### 3. Design System Setup

Create consistent visual language for all slides:

- **Master color palette** — Primary, secondary, accent from brand
- **Typography scale** — Headline, subhead, body sizes
- **Grid structure** — Content zones consistent across slides
- **Visual elements** — Recurring shapes, icons, dividers

### 4. Slide-by-Slide Design

**First Slide (The Hook):**
- Attention-grabbing headline
- High contrast for scroll-stopping power
- Clear value proposition (<12 words)
- Visual cue to swipe (arrow, "swipe →")

**Interior Slides:**
- One key idea per slide
- Consistent layout with varied content
- Progressive information reveal
- Strategic CTA placement (not just final slide)

**Final Slide:**
- Clear call-to-action
- Contact/handle information
- Branding reinforcement

### 5. Consistency Check

- [ ] All slides identical aspect ratio
- [ ] Typography consistent (font, size, weight)
- [ ] Color usage consistent
- [ ] Visual style unified
- [ ] Slide numbers or progress indicators present
- [ ] Swipe cues visible

## Output

**Format:** PNG/JPG sequence (numbered files)
**Location:** `.pawbytes/creative-suites/brands/{brand}/assets/{campaign}/carousels/`
**Naming:** `{carousel-name}_slide{01-N}.{ext}`

## Optimal Slide Count

| Slides | Best For |
|--------|----------|
| 5-7 | Quick tips, simple concepts |
| 8-10 | Tutorials, detailed explanations |
| 10-20 | Comprehensive guides, courses |

**Note:** Every slide must add value. No filler.

## Example Usage

> "Create a 7-slide Instagram carousel about '5 Productivity Hacks for Remote Workers.' Use the listicle structure. Brand colors, clean typography, minimal icons."

## Escalation

If content doesn't naturally divide into slides, recommend restructuring. If platform limits would be exceeded, suggest breaking into multiple carousels.