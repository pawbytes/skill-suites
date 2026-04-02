# Part 3: Meet the Agents

## The Creative Team, In Depth

This guide provides a comprehensive look at each specialist agent. For each agent, you'll learn who they are, what they create, when to call them, and see example conversations.

---

## Aria - The Creative Director

### Who She Is

Aria is your creative director and the orchestrator of the Creative Suite. She is a seasoned creative professional who acts as a trusted partner, not just a tool. She takes ownership of outcomes and proactively guides you toward better creative decisions.

**Her personality:**
- Confident but not arrogant
- Conversational, natural dialogue
- Proactive — suggests next steps, catches issues early
- Clear — avoids jargon, explains trade-offs when relevant

**Her role:**
- Orchestrate, don't execute — she routes work to specialists
- Maintain brand consistency across all work
- Quality-check deliverables before they reach you
- Guide you through the creative process

### What She Does

| Capability | Description |
|------------|-------------|
| **Brand Onboarding** | Guides you through setting up your brand identity |
| **Brief Analysis** | Understands your goals and clarifies requirements |
| **Campaign Planning** | Creates plans for multi-asset campaigns |
| **Agent Routing** | Connects you with the right specialist |
| **Quality Control** | Reviews outputs before delivery |
| **Campaign Orchestration** | Coordinates multiple specialists for complex projects |

### When to Call Aria

**Trigger phrases:**
- "Aria, I need..." (followed by what you need)
- "Help me create..."
- "I want to launch a campaign..."
- "Can you help me figure out..."
- "I'm not sure what I need..."

**Scenarios:**

| Situation | Why Aria |
|-----------|----------|
| Starting a new project | She helps clarify what you actually need |
| Multiple assets needed | She coordinates all specialists |
| Unsure where to start | She guides you through the process |
| Brand setup or updates | She manages your brand information |
| Something went wrong | She troubleshoots and finds solutions |

### What You Get

When you work with Aria on a multi-asset project:

```
brands/your-brand/campaigns/[campaign-name]/
    status.md                    <-- Campaign status
    assets/
        social/
            instagram-1.png
            linkedin-1.png
        video/
            demo-video.mp4
    qa-report.md                 <-- Quality check results
    campaign-manifest.json       <-- Asset inventory
```

### Example Conversation

**Scenario:** You need a product launch campaign.

---

**You:** "Aria, I'm launching a new product next month - it's a project management app for small teams. I need to create some buzz but I'm not sure what I need."

**Aria:** "Congratulations on the launch! Let me help you plan this. A few questions to get started:

1. What makes your app different from other project management tools?
2. Who's your ideal customer - what kind of small teams?
3. What platforms do your customers use most?
4. Do you have a launch date yet?"

---

**You:** "1. It's super simple - no learning curve, teams can start using it in 5 minutes
     2. Small agencies, consultants, freelancers - teams of 2-10 people
     3. They're on LinkedIn and Twitter mostly
     4. Launching in 3 weeks"

**Aria:** "Perfect! Here's what I'd recommend for a 3-week launch campaign:

**Week 1 - Teaser Phase**
- LinkedIn post: 'Something's coming' teaser
- Twitter thread: Problems with current PM tools (set up the problem you solve)

**Week 2 - Reveal Phase**
- LinkedIn carousel: 'Meet [App Name]' - feature walkthrough
- Twitter: Short demo video (30 seconds)

**Launch Week**
- LinkedIn: Full announcement with customer testimonial
- Twitter: Launch thread with screenshots
- TikTok: '5 minute setup' demo video

This gives you 7 assets total. Should I proceed with this plan?"

---

**You:** "That sounds great! Can you also add an Instagram post for launch day?"

**Aria:** "Absolutely! Adding Instagram to launch week. I'll now coordinate our Designer and Video Producer to create all 8 assets. They'll work in parallel, and I'll quality-check everything before delivery.

Starting production now. Estimated completion: 45 minutes."

---

**[45 minutes later]**

**Aria:** "Your campaign is ready! All 8 assets have been created and quality-checked. Here's your campaign folder:

```
brands/your-app/campaigns/launch/
    assets/
        social/
            linkedin-teaser.png
            linkedin-carousel-01-05.png
            linkedin-announcement.png
            twitter-thread-images/
            instagram-launch.png
        video/
            twitter-demo.mp4
            tiktok-setup-demo.mp4
    qa-report.md
```

Each asset follows your brand guidelines and is sized correctly for its platform. Ready to post!"

---

## The Designer - Visual Production Specialist

### Who They Are

The Designer is a detail-oriented visual production expert who creates production-ready assets. They speak in terms of layouts, compositions, visual hierarchy, and aesthetic precision.

**Their personality:**
- Clear and precise about visual decisions
- References design principles when explaining choices
- Direct about technical requirements
- Confident about aesthetic judgments

**Their principles:**
- Brand consistency first — every output verified against brand guidelines
- Platform precision — exact dimensions, correct aspect ratios, proper safe zones
- Visual hierarchy — every design has clear priority
- Production quality — outputs are ready for immediate upload

### What They Create

| Asset Type | Description | Formats |
|------------|-------------|---------|
| **Social Posts** | Single images for any social platform | PNG, JPG |
| **Carousels** | Multi-slide content for Instagram, LinkedIn | PNG slides |
| **Flyers** | Print-ready promotional materials | PNG, PDF |
| **Brand Assets** | Logos, icons, avatars, banners | PNG, SVG |
| **Templates** | Reusable HTML/CSS design templates | HTML/CSS |

### Platform Specifications

| Platform | Dimensions | Aspect Ratio |
|----------|------------|--------------|
| Instagram Feed | 1080 x 1350 px | 4:5 |
| Instagram Story | 1080 x 1920 px | 9:16 |
| Instagram Carousel | 1080 x 1350 px | 4:5 |
| LinkedIn Post | 1200 x 627 px | 1.91:1 |
| LinkedIn Carousel | 1080 x 1080 px | 1:1 |
| Twitter/X | 1600 x 900 px | 16:9 |
| Facebook Post | 1200 x 630 px | 1.91:1 |
| TikTok | 1080 x 1920 px | 9:16 |

### When to Call the Designer

**Trigger phrases:**
- "Create a social post for..."
- "Design a carousel about..."
- "Make a flyer for..."
- "Generate a logo for..."
- "Resize this image for..."
- "I need a visual for..."

**Scenarios:**

| Situation | Output |
|-----------|--------|
| Announce a new product | Social post |
| Share a list or tutorial | Carousel |
| Promote an event | Flyer |
| New brand or rebrand | Logo package |
| Cross-post to multiple platforms | Resized variants |

### What You Get

**For a single social post:**
```
brands/your-brand/social/
    instagram-post-name.png
```

**For a carousel:**
```
brands/your-brand/carousels/[topic]/
    slide-01.png      <-- Upload first
    slide-02.png
    slide-03.png
    slide-04.png
    slide-05.png      <-- Upload last
    manifest.json     <-- Metadata
```

**For a logo package:**
```
brands/your-brand/brand-assets/logo/
    logo-color.png        <-- Full color
    logo-white.png        <-- For dark backgrounds
    logo-black.png        <-- For light backgrounds
    logo.svg              <-- Scalable vector
```

### Example Conversation

**Scenario:** You need a 5-slide Instagram carousel about productivity tips.

---

**You:** "I need a 5-slide Instagram carousel about productivity tips for remote workers"

**Designer:** "I'll create a 5-slide carousel for Instagram (1080 x 1350 pixels). A few questions:

1. What's the main headline for the cover slide?
2. Do you have 5 specific tips, or should I suggest some?
3. Any visual style preference? (minimal, bold, illustrated, photo-based)"

---

**You:** "1. Headline: '5 Ways to Stay Productive While Working From Home'
     2. You can suggest tips - make them practical
     3. Minimal style with some illustration elements"

**Designer:** "Got it! Here's my plan:

**Slide 1 (Cover):** '5 Ways to Stay Productive While Working From Home'
**Slide 2:** Tip 1: Create a dedicated workspace
**Slide 3:** Tip 2: Set clear work hours and stick to them
**Slide 4:** Tip 3: Take scheduled breaks (try the Pomodoro technique)
**Slide 5:** Tip 4: Minimize digital distractions + Tip 5: End your day with a shutdown ritual

Creating all slides now. Using your brand colors with minimal illustrated icons."

---

**[2 minutes later]**

**Designer:** "Here's your carousel! [Shows all 5 slides]

Each slide uses consistent branding, clear visual hierarchy, and the minimal illustration style you requested. The text is sized for mobile readability.

Would you like any changes?"

---

**You:** "Slide 4 looks a bit empty with two tips. Can you split it into two slides?"

**Designer:** "Good catch! That makes it 6 slides total. I'll split those tips."

**[1 minute later]**

**Designer:** "Done! Now it's a 6-slide carousel. Each tip has its own slide for better readability."

---

**You:** "Perfect! Export it please."

**Designer:** "Saved to:
```
brands/your-brand/carousels/productivity-tips/
    slide-01.png
    slide-02.png
    slide-03.png
    slide-04.png
    slide-05.png
    slide-06.png
    manifest.json
```

Upload in order: slide-01 first, slide-06 last."

---

## The Video Producer - Video Production Specialist

### Who They Are

The Video Producer is a technical video production specialist who understands both creative storytelling and video engineering. They speak in terms of scenes, cuts, transitions, render settings, and codec specifications.

**Their personality:**
- Technically precise about video decisions
- Keeps creative intent clear
- References production concepts when explaining choices
- Direct about technical constraints

**Their principles:**
- Platform specs are law — every video meets exact requirements
- Subtitles are non-negotiable — every video includes burned-in subtitles
- Pipeline thinking — sequential production from script to final encode
- Brand consistency — visual style and typography match brand guidelines

### What They Create

| Asset Type | Platforms | Typical Duration |
|------------|-----------|------------------|
| **Short-form Video** | TikTok, Reels, Shorts | 15-60 seconds |
| **Long-form Video** | YouTube, web | 3-10+ minutes |
| **Motion Graphics** | All platforms | Varies |
| **Video Clips** | All platforms | Extracted moments |
| **Voiceover** | Any video | As needed |

### Platform Video Specifications

| Platform | Resolution | Aspect | Duration Limit |
|----------|------------|--------|----------------|
| TikTok | 1080 x 1920 | 9:16 | 15-180 seconds |
| Instagram Reels | 1080 x 1920 | 9:16 | 15-90 seconds |
| YouTube Shorts | 1080 x 1920 | 9:16 | 15-60 seconds |
| YouTube | 1920 x 1080 | 16:9 | No limit |
| LinkedIn | 1920 x 1080 | 16:9 | 3 seconds - 10 minutes |

### When to Call the Video Producer

**Trigger phrases:**
- "Create a TikTok video about..."
- "Make a Reel showing..."
- "Produce a YouTube video for..."
- "Extract clips from this video..."
- "Add subtitles to this video..."
- "Generate a voiceover for..."

**Scenarios:**

| Situation | Output |
|-----------|--------|
| Product demo | Short-form video (TikTok/Reels) |
| Tutorial or how-to | Long-form video (YouTube) |
| Repurpose podcast | Extracted clips |
| Add accessibility | Subtitles |
| No voice talent available | AI voiceover |

### What You Get

**For a short-form video:**
```
brands/your-brand/videos/shortform/[title]/
    video.mp4              <-- Ready to upload
    subtitles.srt          <-- Optional: for manual upload
    video-manifest.json    <-- Metadata
```

**For a long-form video:**
```
brands/your-brand/videos/longform/[title]/
    video.mp4
    thumbnail.png          <-- YouTube thumbnail
    subtitles.srt
    video-manifest.json
```

**For extracted clips:**
```
brands/your-brand/videos/clips/[source]/
    clip-01-name.mp4
    clip-02-name.mp4
    clip-03-name.mp4
    clip-manifest.json
```

### Example Conversation

**Scenario:** You need a 30-second TikTok demo video.

---

**You:** "Create a 30-second TikTok video showing how our app helps freelancers track their time"

**Video Producer:** "I'll create a 30-second TikTok (1080 x 1920, H.264). A few questions:

1. What's the one key feature to highlight?
2. Do you have a script, or should I write one?
3. Any specific visual style? (screen recording style, animated, live action)"

---

**You:** "1. The one-tap timer feature - tap once to start tracking
     2. Write a script please
     3. Screen recording style showing the app interface"

**Video Producer:** "Here's the script I propose:

**[0-3s] Hook:** 'Freelancers! Stop losing billable hours...'
**[3-12s] Problem:** Quick shots of messy spreadsheets, forgotten tasks
**[12-25s] Solution:** Show the one-tap timer in action
**[25-30s] CTA:** 'Download free - link in bio'

Sound good? I'll generate the scenes, add voiceover, and burn in subtitles."

---

**You:** "Perfect, let's do it."

**Video Producer:** "Starting production:

1. Generating AI scenes for the problem shots
2. Creating screen recording visuals for the solution
3. Adding voiceover (female, professional tone)
4. Burning in word-level highlight subtitles

This will take about 10 minutes."

---

**[10 minutes later]**

**Video Producer:** "Your TikTok is ready!

**Video specs:**
- Duration: 30 seconds
- Resolution: 1080 x 1920 (9:16)
- Codec: H.264, 8Mbps
- Subtitles: English, burned in (highlight style)

[Shows video preview]

Ready for TikTok upload. Any changes needed?"

---

**You:** "Can you make the subtitles a bit larger?"

**Video Producer:** "Absolutely! Increasing subtitle size by 20%."

**[1 minute later]**

**Video Producer:** "Done! [Shows updated video] Saved to:
```
brands/your-brand/videos/shortform/time-tracker-demo/
    video.mp4
    subtitles.srt
    video-manifest.json
```"

---

## The Strategist - Research and Content Specialist

### Who They Are

The Strategist is a research-driven content planner who transforms brand goals into actionable strategies. They are methodical and analytical, speaking in terms of audiences, messaging hierarchies, and strategic angles.

**Their personality:**
- Evidence-based — "The data shows..." not "I think..."
- Structured — organizes findings logically
- Insightful — connects dots, finds patterns
- Practical — research leads to actionable recommendations

**Their principles:**
- Research-first — never guess when you can search
- Show your work — cite sources, explain reasoning
- Audience-centric — every piece of content serves a specific audience need
- Review gate discipline — all scripts and copy require user approval before production

### What They Create

| Deliverable | Purpose |
|-------------|---------|
| **Competitor Analysis** | Understand market position and opportunities |
| **Trend Reports** | Discover what's working in your industry |
| **Scripts** | Ready for video production |
| **Copy Drafts** | Ready for visual adaptation |
| **Content Calendars** | Plan your posting schedule |
| **Research Reports** | Deep dives into topics and audiences |

### When to Call the Strategist

**Trigger phrases:**
- "Research my competitors..."
- "Find trending topics in..."
- "Write a script for..."
- "Create a content calendar..."
- "Draft copy for..."
- "What content should I create for..."

**Important:** The Strategist is a **service agent**, not a mandatory gate. Call them when you need research or written content. If you already have your content planned, you can go directly to the Designer or Video Producer.

### Scenarios

| Situation | Output |
|-----------|--------|
| Planning content strategy | Research report + content calendar |
| Writing a video script | Script with scene notes |
| Creating social copy | Copy drafts ready for design |
| Understanding competition | Competitor analysis report |
| Finding content opportunities | Trend report with recommendations |

### What You Get

**For research:**
```
brands/your-brand/research/
    competitor-analysis.md
    trend-report.md
    content-opportunities.md
```

**For scripts and copy:**
```
brands/your-brand/campaigns/[campaign]/
    scripts/
        video-script.md
    copy/
        social-copy-drafts.md
```

**For content calendars:**
```
brands/your-brand/
    content-calendar.md
```

### Example Conversation

**Scenario:** You need to research your competitors and create a content calendar.

---

**You:** "I need to understand what my competitors are doing on Instagram, and then create a content calendar for next month"

**Strategist:** "I'll analyze your competitors' Instagram presence and create a content calendar based on what's working in your industry.

First, who are your main competitors? (Or should I research who they are?)"

---

**You:** "I sell handmade jewelry. My competitors are [Brand A], [Brand B], and [Brand C]. I also see a lot of new brands on TikTok."

**Strategist:** "Got it! I'll analyze:
- [Brand A], [Brand B], [Brand C] on Instagram
- Emerging jewelry brands on TikTok
- Content trends in the handmade jewelry space

This will take about 5 minutes to research. I'll look at:
- Post frequency and timing
- Top-performing content types
- Engagement patterns
- Hashtag strategies"

---

**[5 minutes later]**

**Strategist:** "Research complete! Here's what I found:

**Competitor Analysis Summary:**

| Brand | Posting Frequency | Top Content Types | Avg Engagement |
|-------|-------------------|-------------------|----------------|
| Brand A | 5x/week | Process videos, customer stories | 3.2% |
| Brand B | 7x/week | Product close-ups, tutorials | 2.8% |
| Brand C | 3x/week | Lifestyle shots, UGC reposts | 4.1% |

**Key Insights:**
1. Process videos get 2x more engagement than static posts
2. Posting between 6-8pm gets 40% more engagement
3. 'Behind the scenes' content is underutilized by competitors
4. TikTok creators are winning with packaging/unboxing videos

**Content Opportunities I See:**
1. Create process videos showing your jewelry making
2. Start an unboxing/packaging series
3. Share behind-the-scenes of your workspace

Should I build a content calendar based on these insights?"

---

**You:** "Yes please! Make it for May with a focus on process videos"

**Strategist:** "Here's your May content calendar:

**Week 1: Process Focus**
| Day | Platform | Content | Notes |
|-----|----------|---------|-------|
| Mon | Instagram | Process video: Making a ring | 6pm post |
| Wed | Instagram | Carousel: Tools of the trade | Educational |
| Fri | TikTok | Speed process: Pendant creation | Trending audio |
| Sat | Instagram | Story: Workspace tour | Behind-the-scenes |

**Week 2: Unboxing Focus**
| Day | Platform | Content | Notes |
|-----|----------|---------|-------|
| Mon | TikTok | Unboxing video (customer POV) | Use trending audio |
| Wed | Instagram | Reel: Packaging process | Show care in packaging |
| Fri | Instagram | Customer unboxing repost | UGC |
| Sat | Instagram | Story: Pack with me | Interactive |

[Continues for all 4 weeks...]

**Total:** 16 posts across Instagram and TikTok

Would you like me to pass this calendar to the Designer to start creating the visuals?"

---

**You:** "Yes, start with Week 1 please"

**Strategist:** "Routing to the Designer now. They'll create the Week 1 visuals using your brand guidelines."

---

## Summary: Agent Quick Reference

| Agent | Best For | Trigger Phrase Example |
|-------|----------|------------------------|
| **Aria** | Planning, coordination, campaigns | "Aria, I need a campaign..." |
| **Designer** | Visuals: posts, carousels, logos | "Create an Instagram post..." |
| **Video Producer** | Videos: TikTok, Reels, YouTube | "Make a TikTok video..." |
| **Strategist** | Research, scripts, copy, calendars | "Research my competitors..." |

---

## Next Steps

Now that you know each agent in depth:

| I want to... | Go to |
|--------------|-------|
| Create specific design assets | [Part 4: Design Workflows](./part-4-design-workflows.md) |
| Create video content | [Part 5: Video Workflows](./part-5-video-workflows.md) |
| Run a multi-asset campaign | [Part 6: Campaign Orchestration](./part-6-orchestration.md) |
| Reference platform specs and troubleshooting | [Part 7: Appendices](./part-7-appendices.md) |