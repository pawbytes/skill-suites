# Product Launch Checklists

> Reference document for the paw-mkt-launch skill. Updated March 2026.
> Sources: Product Hunt launch playbooks, Reforge product launch frameworks, Andrew Chen's distribution playbook, Lenny Rachitsky's go-to-market guides, practitioner post-mortems from Indie Hackers and First Round Review.

---

## 1. Pre-Launch Checklist

Itemized tasks from T-8 weeks through T-1 day. Mark each item complete before the gate to the next phase.

### T-8 Weeks: Strategy and Messaging Lock

**Strategy**
- [ ] Launch type confirmed (new product / major feature / minor feature / patch)
- [ ] Launch tier decided (Tier 1 / Tier 2 / Tier 3)
- [ ] Target launch date set and agreed by leadership and engineering
- [ ] SOSTAC plan reviewed: launch objectives, target segments, success metrics confirmed
- [ ] ORB channel plan drafted: owned channels listed, rented channels identified, borrowed channels confirmed
- [ ] Budget allocated per channel (paid support, influencer gifting, wire distribution if any)
- [ ] Launch team roles assigned: content owner, social owner, email owner, PH owner, press owner, dev contact for launch day issues

**Messaging**
- [ ] Core value proposition finalized (one sentence: "We help {audience} {achieve outcome} by {differentiator}")
- [ ] Tagline drafted (3-5 variants for testing, final selected before T-4)
- [ ] Key benefits list (3-5 outcomes, not features -- written in customer language)
- [ ] Primary objections identified and addressed in messaging
- [ ] Competitor differentiation documented (what we do better, what we do differently)
- [ ] Pricing and packaging confirmed (no surprises at launch)
- [ ] Brand voice guidelines reviewed for tone calibration across all launch content

**Borrowed Channel Briefings**
- [ ] Journalist outreach list built (10-30 contacts, tiered by priority)
- [ ] Initial journalist briefings sent under embargo (give them 6-8 weeks for feature stories)
- [ ] Podcast appearance slots booked for T-4 to T-2 window
- [ ] Influencer or creator seeding list identified (5-15 accounts with ICP audience)
- [ ] Partner co-announcement discussions initiated (if applicable)

---

### T-6 Weeks: Alpha Launch Gate

**Product Readiness**
- [ ] Alpha environment deployed and stable
- [ ] Core user flow tested end-to-end by internal team (sign up → aha moment)
- [ ] All P0/P1 bugs resolved
- [ ] Onboarding flow achieves aha moment within 5 minutes (validated internally)
- [ ] Analytics events firing correctly: signup, activation, core action, conversion
- [ ] Payment processing tested (if applicable): successful charge, failed charge, refund
- [ ] Email sequences set up: welcome email, onboarding series (bridge to paw-mkt-email)
- [ ] Support documentation: FAQ, getting started guide, at least one help article per core feature

**Alpha User Invitations**
- [ ] Alpha user list built: 50-200 names with contact info and why they were chosen
- [ ] Personal invitation messages drafted (not a blast -- individualized or at minimum cohort-specific)
- [ ] Invitations sent
- [ ] Feedback collection method set up (Typeform, Airtable, Google Form, or in-product survey)
- [ ] Testimonial collection process ready (ask permission to use quotes before launch)

**Alpha Gate (before advancing to Beta)**
- [ ] 60-70%+ of alpha users complete core workflow successfully
- [ ] At least 3-5 usable testimonial quotes collected and approved for use
- [ ] No critical UX blocking issues outstanding
- [ ] At least 10 structured feedback responses reviewed and actioned

---

### T-4 Weeks: Beta Launch Gate

**Beta Access and Teaser**
- [ ] Beta waitlist or application landing page live with product promise and social proof from alpha
- [ ] Teaser campaign begun on social: "Something is coming" without full reveal
- [ ] Beta invitations sent (200-1,000 users target)
- [ ] Community posts live in relevant subreddits, Slack groups, Discord servers (genuine context, not spam)
- [ ] Influencer seeding packages sent: early access + brief + what you are asking for (honest review, post, testimonial)

**Content Creation Underway**
- [ ] Launch blog post first draft complete
- [ ] Email announcement first draft complete (subject line variants drafted)
- [ ] X / Twitter thread first draft complete
- [ ] LinkedIn founder post first draft complete
- [ ] Reddit / community post first draft complete
- [ ] Press release first draft complete (Tier 1 only)
- [ ] Product Hunt gallery planning underway: screenshots spec'd, GIF concept decided

**Product Hunt Preparation**
- [ ] Product Hunt hunter identified and confirmed (self-hunt or recruited hunter with 1,000+ followers)
- [ ] Product page created on Product Hunt (mark as "Upcoming" to build notification subscribers)
- [ ] Upcoming page link shared in communities and with supporters
- [ ] Gallery assets in production: 5-8 screenshots at 1270x952px, 1 demo GIF 3-8 seconds
- [ ] Tagline variants written (3+ options)
- [ ] First maker comment draft written

**Beta Gate (before advancing to Early Access)**
- [ ] 10-30 testimonial quotes collected and approved
- [ ] All launch content first drafts complete and in review
- [ ] Product Hunt hunter confirmed and briefed on timing
- [ ] Press pitches sent (for Tier 1: embargo pitches out to all tier-1-2 journalists)
- [ ] Influencer seeding confirmed (at least 3-5 creators have accepted and are using the product)

---

### T-2 Weeks: Early Access Gate

**Public Early Access**
- [ ] Early access landing page live with beta social proof (testimonials, logos, metrics)
- [ ] Public announcement of early access sent via email and social
- [ ] Waitlist growth being tracked daily

**Content Finalization**
- [ ] Launch blog post: final draft reviewed and approved
- [ ] Email announcement: final copy approved, subject line A/B variants set
- [ ] Social posts: all platforms drafted, reviewed, approved, and scheduled in social tool
- [ ] Press release: final version ready to distribute
- [ ] Product Hunt gallery: all assets uploaded and approved (thumbnail, screenshots, GIF, description)
- [ ] Tagline: final selection made
- [ ] First maker comment: final draft approved

**Product Hunt Final Prep**
- [ ] Product Hunt listing fully populated and reviewed by at least two team members
- [ ] Submission set up for 12:01am PT on launch day (confirm exact date and time)
- [ ] Maker's first comment pre-written and ready to paste immediately after submission

**Supporter Coordination**
- [ ] Supporter list finalized: names, email addresses, and relationship context
- [ ] Pre-launch briefing email drafted: what is launching, when, what to do (specific link and action)
- [ ] Pre-launch briefing email sent to supporter list
- [ ] 9am PT upvote-ask email drafted and loaded in ESP ready to send

**Technical Readiness**
- [ ] UTM parameters set up for all launch traffic sources (see Section 9.4 of SKILL.md)
- [ ] GA4 / analytics confirmed: real-time view works, key events tracked, launch UTMs tested
- [ ] Server load capacity assessed: can the site handle 5-10x normal traffic?
- [ ] CDN or caching in place if applicable
- [ ] Status page or fallback landing page ready (in case of traffic surge)
- [ ] On-call engineer or tech lead designated for launch day
- [ ] All scheduled social posts confirmed in scheduling tool

**Early Access Gate (before launch day)**
- [ ] All content approved and scheduled
- [ ] All team members briefed on launch day roles and timing
- [ ] Product Hunt submission ready with confirmed 12:01am PT timing
- [ ] Supporter email loaded and tested
- [ ] Technical readiness confirmed

---

### T-1 Day: Final Checks

- [ ] All social posts confirmed scheduled for correct times
- [ ] Email announcement confirmed scheduled (or ready to send manually)
- [ ] Supporter email confirmed loaded (ready to send at 9am PT)
- [ ] Product Hunt first comment copied to clipboard / notes app for instant paste after submission
- [ ] Launch day schedule distributed to all team members with exact times and owners
- [ ] Backup communication channel set for launch day (team Slack channel or group chat)
- [ ] Product Hunt listing reviewed one final time: no typos, all images load, links work
- [ ] Landing page reviewed: pricing, CTA links, social proof is current
- [ ] All email sequences confirmed active in ESP
- [ ] Journalist embargo time confirmed (if applicable)
- [ ] Analytics real-time view confirmed working
- [ ] Key dashboards bookmarked: GA4, ESP, product signups, Product Hunt position, social mentions
- [ ] Every team member knows what they are doing and when

---

## 2. Launch Day Checklist

Minute-by-minute execution for a full Tier 1 / Product Hunt launch day. Times in Pacific Time.

### Midnight (12:00am-1:00am PT)

- [ ] **12:01am**: Submit Product Hunt listing. Confirm it is live and visible.
- [ ] **12:05am**: Post maker's first comment on the Product Hunt listing.
- [ ] **12:10am**: Share PH link in internal team channel with "We're live!" message.
- [ ] **12:15am**: Verify Product Hunt listing appears in the daily feed (search for the product name).
- [ ] **12:30am**: Check: is the submission on the correct day's feed? Confirm no timezone issues.
- [ ] Sleep (if possible) -- the early hours are low-traffic on Product Hunt.

### Morning (7:00am-10:00am PT)

- [ ] **7:00am**: Wake up and check Product Hunt position. Note current ranking.
- [ ] **7:00am**: Confirm all scheduled social posts are set to fire at the correct times.
- [ ] **7:00am**: Confirm email announcement is loaded and ready.
- [ ] **7:15am**: Check server status: is the site up and responding normally?
- [ ] **7:30am**: Respond to any early Product Hunt comments (overnight comments from EU users).
- [ ] **8:00am**: Send email announcement to full list. Confirm send in ESP.
- [ ] **8:00am**: Confirm X / Twitter launch thread is live (if not pre-scheduled, post now).
- [ ] **8:30am**: Check email delivery: no bounce errors, send confirmed in ESP dashboard.
- [ ] **9:00am**: Send supporter email with Product Hunt upvote ask and direct link.
- [ ] **9:00am**: LinkedIn founder post live (post manually for best timing control).
- [ ] **9:00am**: Post in Reddit / community threads (personal, story-led, not promotional).
- [ ] **9:30am**: Instagram Stories launch sequence live.
- [ ] **9:30am**: Check Product Hunt position. Note ranking. Screenshot for records.
- [ ] **10:00am**: Respond to all Product Hunt comments received so far. Respond to every one.
- [ ] **10:00am**: Check social mentions on X and LinkedIn. Respond to replies.
- [ ] **10:00am**: Check email metrics: open rate, click rate (first hour data).

### Midday (11:00am-1:00pm PT)

- [ ] **11:00am**: Product Hunt position check and screenshot. Note trend.
- [ ] **11:00am**: If Top 10: post milestone update on X and LinkedIn ("We're in the top 10 on Product Hunt!").
- [ ] **11:30am**: Respond to all outstanding Product Hunt comments.
- [ ] **12:00pm**: Mid-day founder update post on X and LinkedIn ("Halfway through launch day -- here's what we're seeing..."). Include early metric or quote if available.
- [ ] **12:00pm**: Check press coverage: any articles live? Share internally and on social.
- [ ] **12:30pm**: Check signup / trial numbers in product dashboard.
- [ ] **12:30pm**: Check GA4 real-time: top traffic sources, top pages, conversion events.
- [ ] **1:00pm**: Reach out to 10-20 additional supporters via personal DM if ranking needs a boost.

### Afternoon (1:00pm-5:00pm PT)

- [ ] **1:00pm**: Post in any remaining community threads not yet covered (different subreddit or Slack group).
- [ ] **2:00pm**: Full social sweep: respond to all X mentions, LinkedIn comments, Instagram replies.
- [ ] **2:00pm**: Product Hunt position check and screenshot.
- [ ] **2:30pm**: Respond to all outstanding Product Hunt comments.
- [ ] **3:00pm**: If Top 5: post milestone celebration on social with screenshot.
- [ ] **3:30pm**: Check if any influencers or creators have posted about the product. Reshare and engage.
- [ ] **4:00pm**: Send personal thank-you DMs or replies to your most supportive community members.
- [ ] **4:30pm**: Final Product Hunt push: post an update comment on PH listing with a new insight, bonus content, or user story.
- [ ] **5:00pm**: End-of-day update post on X, LinkedIn, and Product Hunt: "What a day. Thank you to everyone who voted, tried the product, and shared kind words. Here's where we landed: [position and stats]."
- [ ] **5:00pm**: Check final metrics before PT voting slows significantly.

### Evening / Wrap (5:00pm-11:59pm PT)

- [ ] **6:00pm**: Internal launch debrief meeting or async report: signups, traffic, PH position, press coverage, email metrics, social reach.
- [ ] **6:00pm**: Begin drafting the launch performance report (can be completed over next 48 hours).
- [ ] **7:00pm**: Final Product Hunt comment check and responses.
- [ ] **9:00pm**: PH voting slows significantly after this hour. Monitor but no active push needed.
- [ ] **11:59pm**: Note final Product Hunt position before the day resets at midnight PT.
- [ ] **Post-midnight**: Capture final Product Hunt badge / placement screenshot.

### Launch Day Monitoring Dashboard

Check these sources throughout the day:

| Dashboard | What to Track | How Often |
|---|---|---|
| Product Hunt listing | Ranking, vote count, comment count, trending | Every 30-60 minutes |
| GA4 real-time | Active users, traffic sources, top pages, signups | Every hour |
| Product / CRM | New signups, trial starts, plan selections | Every hour |
| ESP dashboard | Email open rate, click rate, unsubscribes, bounces | 8am, 12pm, 5pm |
| X / Twitter search | Brand name mentions, replies, reshares | Every 30-60 minutes |
| LinkedIn notifications | Post comments, reactions, reshares | Every 60-90 minutes |
| Google Alerts | Press coverage, brand mentions | Set to immediate delivery |
| Server / uptime monitor | Site status, response time | Automated alerts |

---

## 3. Post-Launch Checklist

### Days 1-3: Capture and Convert

- [ ] **Day 1**: Respond to every comment, mention, and DM received during launch day. No channel goes dark.
- [ ] **Day 1**: Update internal team on launch results (signups, PH position, traffic, press coverage).
- [ ] **Day 1**: Pull Product Hunt final position and badge. Screenshot and save to assets folder.
- [ ] **Day 2**: Send thank-you email to all Product Hunt voters who left a comment (if email captured) or post a public PH thank-you comment.
- [ ] **Day 2**: Send "launch recap" internal report to leadership: signups, traffic, top sources, PH position, top press mention, email stats.
- [ ] **Day 2**: Update landing page with social proof from launch: Product Hunt badge, press coverage logos, and any new testimonial quotes from launch day.
- [ ] **Day 2-3**: Collect testimonials from engaged launch-day signups: DM or email the first 20-50 signups and ask for a quick quote.
- [ ] **Day 3**: Publish launch recap blog post: "What happened when we launched on Product Hunt" or "X things we learned from our product launch." Post to Indie Hackers, relevant subreddits, and LinkedIn.
- [ ] **Day 3**: Follow up on press pitches that did not convert yet -- use launch results as the new angle: "We hit #X on Product Hunt and drove Y signups."

### Days 4-7: Activation Push

- [ ] **Day 4**: Send follow-up email to waitlist converts who signed up but have not logged in or completed the core action. Subject: "[First name], did you get a chance to try it yet?"
- [ ] **Day 5**: Check activation metrics: what % of launch signups completed the core workflow within 5 days?
- [ ] **Day 5**: Review onboarding email sequence performance: open rates, click rates, step completion. Flag any issues.
- [ ] **Day 5**: Personal outreach to the top 20-30 most engaged launch users: invite to a brief user interview.
- [ ] **Day 7**: Week 1 report: signups by source, activation rate (users who completed core action), day-7 retention, press coverage count, email metrics, PH referral traffic, top testimonials.
- [ ] **Day 7**: Begin formal post-launch metrics tracking in the performance file.

### Week 2: Growth and Retention

- [ ] Publish first customer case study or success story from a launch user (with permission).
- [ ] Launch retargeting campaigns for launch-day site visitors who did not convert (bridge to paw-mkt-paid-ads).
- [ ] Send newsletter to entire email list with launch recap, product update, and invitation to try or share.
- [ ] Conduct 5-10 user interviews with launch cohort. Document insights in the brand folder.
- [ ] Review Product Hunt page: update screenshots or description if any key messaging improvements emerged from launch feedback.
- [ ] Follow up with any journalists who covered the launch: thank them, share their article, stay connected for future stories.
- [ ] Assess referral / word of mouth: how many signups came from a shared referral link or "heard from a friend"? Consider activating a referral program (bridge to paw-mkt-referral).

### Week 3-4: Consolidation

- [ ] Evaluate launch cohort retention: what is the 21-day retention rate?
- [ ] Survey launch cohort for NPS (simple 0-10 question). Target NPS 40+.
- [ ] Update the product roadmap based on launch feedback themes.
- [ ] Publish a "month in review" post for social media and newsletter: key milestone, user win, next feature coming.
- [ ] Send "one month in" email to launch cohort: product updates since launch, community highlights, and a re-engagement hook for dormant users.
- [ ] Compile full launch performance report and save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/launch-{campaign-slug}/performance/launch-report-{YYYY-MM}.md`.
- [ ] Share learnings with full team. Update the SOSTAC action plan based on launch insights.
- [ ] Plan the next Tier 2 or Tier 3 launch moment to maintain announcement cadence.

---

## 4. Per-Channel Content Checklist

What to create for each channel for a full Tier 1 launch.

### Email

- [ ] Email announcement (full copy with subject line A/B variants, preheader, body, CTA, PS)
- [ ] Supporter briefing email (pre-launch, 1-2 weeks before)
- [ ] Supporter day-of email (9am PT on launch day with PH link and upvote ask)
- [ ] Follow-up email for non-activators (Day 4-7 post-launch)
- [ ] Thank-you email for launch supporters and voters (Day 2 post-launch)
- [ ] Onboarding email sequence for new signups (bridge to paw-mkt-email -- 5-7 email series)
- [ ] "One month in" email for launch cohort (Week 4)

**Quality checks**:
- [ ] Subject lines tested for spam trigger words
- [ ] Email renders correctly in Gmail, Apple Mail, and Outlook (use Litmus or Email on Acid)
- [ ] All links work and are UTM-tagged
- [ ] Unsubscribe link present
- [ ] Plain-text version present
- [ ] Preheader text set (not left blank)
- [ ] From name is personal (founder name, not brand name) for announcement email

### Blog / Website

- [ ] Launch blog post (800-1,500 words, SEO optimized)
- [ ] Landing page updated with: new hero copy, product screenshots, beta testimonials, pricing
- [ ] FAQ page updated with launch-related questions
- [ ] Meta title and description updated for launch keyword
- [ ] Open graph image updated (used for social sharing preview)
- [ ] Launch recap blog post (Day 3 post-launch)
- [ ] First customer case study (Week 2)
- [ ] Press page updated with new coverage and logo bar

**Quality checks**:
- [ ] Blog post internal links to relevant feature pages
- [ ] Blog post CTA links to signup / trial (UTM-tagged)
- [ ] Images have descriptive alt text
- [ ] Page load speed checked (under 3 seconds on mobile)
- [ ] Canonical URL set correctly

### X / Twitter

- [ ] Launch thread (7-10 tweets with hook, problem, solution, proof, CTA)
- [ ] Product Hunt upvote ask tweet (launch day, midday if Top 5)
- [ ] Milestone tweet (if Top 5 or Top 10 of the day)
- [ ] Retweet / quote tweet of significant coverage or influencer posts
- [ ] Thank-you thread for launch day (evening recap)
- [ ] Launch recap tweet (Day 3, linking to recap blog post)
- [ ] Week 1 metric thread ("One week since launch, here's what we learned...")

**Quality checks**:
- [ ] Each tweet stands alone (not dependent on reading previous tweet to make sense)
- [ ] Thread numbered clearly ("1/8", "2/8" etc.)
- [ ] No more than one external link per thread (in final tweet)
- [ ] GIF or screenshot attached to tweet 1 for visual hook
- [ ] Character count checked for each tweet (under 280)

### LinkedIn

- [ ] Founder launch post (personal, story-led, 1,200-1,800 characters)
- [ ] Company page post (brand announcement, links to blog post)
- [ ] Midday launch day update (if Top 5 on Product Hunt)
- [ ] Thank-you post (Day 1 evening)
- [ ] Launch recap article (Day 3-5, native LinkedIn article for extended reach)
- [ ] Week 1 results post ("One week since launch -- here's what the numbers look like")
- [ ] Customer case study post (Week 2)

**Quality checks**:
- [ ] External links moved to first comment (not post body) to avoid LinkedIn suppression
- [ ] Post ends with a question to encourage comments (increases dwell time)
- [ ] Founder post is written in first person, personal voice
- [ ] No more than 3-5 hashtags (relevant, not spammy)
- [ ] Image or video attached for higher reach

### Instagram

- [ ] Feed post: product visual or results screenshot with short caption and CTA to bio link
- [ ] Stories sequence (5-7 frames): countdown, behind-the-scenes, product demo, beta quote, CTA with link sticker
- [ ] Reels: 30-60 second founder "why I built this" or product demo
- [ ] Post-launch Stories: results screenshot, thank-you, link to case study

**Quality checks**:
- [ ] Stories link sticker tested (goes to correct URL)
- [ ] Feed post caption does not exceed 2,200 characters
- [ ] Alt text added to feed post
- [ ] Reels aspect ratio correct (9:16 vertical)
- [ ] Thumbnail set for Reels (shows product or founder face, not a random frame)

### Product Hunt

- [ ] Thumbnail: 240x240px, high contrast, readable at small size
- [ ] Screenshots: 5-8 at 1270x952px, each showing a specific use case or outcome
- [ ] Demo GIF: 3-8 seconds, shows core value moment, loops cleanly
- [ ] Tagline: 260 characters maximum, benefit-led, tested 3+ variants
- [ ] Description: 3-5 paragraphs (problem → solution → who it's for → social proof → CTA)
- [ ] Topics / categories: 3 relevant categories selected
- [ ] Links: product URL, pricing page, Twitter (X) handle
- [ ] Maker's first comment: 200-400 words, personal, story-led, invites questions
- [ ] Hunter confirmed and briefed (submission time, first comment plan)

**Quality checks**:
- [ ] All images load at full resolution in the Product Hunt preview
- [ ] GIF loops seamlessly with no flash or jarring cut
- [ ] Tagline has no typos and reads well out of context
- [ ] Description has no jargon, no hype, no claims without proof
- [ ] All links return 200 status (no broken URLs)
- [ ] Submission time confirmed as 12:01am PT on the correct date

### Press / Media (Tier 1 Only)

- [ ] Press release: full draft, approved, formatted for distribution
- [ ] Embargo pitch emails: sent 4-8 weeks before to tier-1-2 journalists
- [ ] Follow-up pitch emails: sent 3-5 days before launch lift
- [ ] Media list with outreach status tracked (save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/launch-{campaign-slug}/channels/pr/content/media-lists/`)
- [ ] Press kit: product screenshots (high res), founder headshot, company logo (PNG + SVG), boilerplate
- [ ] Embargo lift time confirmed with all journalists who received early access

**Quality checks**:
- [ ] Press release passes the "so what?" test in the first two sentences
- [ ] All statistics and claims are sourced or attributable
- [ ] Company boilerplate is current (team size, HQ, funding if public)
- [ ] Media contact email and phone are correct
- [ ] All journalists have confirmed their embargo lift time in writing

### Communities (Reddit, Indie Hackers, Slack, Discord)

- [ ] Reddit posts drafted for relevant subreddits (story-led, not promotional)
- [ ] Indie Hackers launch post drafted (include revenue/metrics if public, build-in-public angle)
- [ ] Hacker News "Show HN" post drafted (if applicable: technical product or developer tool)
- [ ] Slack/Discord community posts drafted for each relevant community
- [ ] Responses pre-drafted for anticipated questions in each community

**Quality checks**:
- [ ] Each community post is adapted for that community's norms and tone (do not copy-paste the same post)
- [ ] No "go vote for my Product Hunt" as the primary message -- lead with value and story
- [ ] Reddit posts comply with each subreddit's rules (check rules before posting)
- [ ] Hacker News Show HN format correct: "Show HN: {Product Name} -- {one line description}"
- [ ] Team member designated to monitor each community thread for 24-48 hours post-post

---

## 5. Ongoing Announcement Cadence Checklist

For recurring Tier 2 and Tier 3 launches after the initial product launch.

### Tier 2 (Monthly Feature Launch)

- [ ] Feature brief written: what changed, who it benefits, key outcome enabled
- [ ] Blog post written (400-800 words): feature overview, use case, how to use it, CTA
- [ ] Email to user base: subject line, 200-400 word body, CTA to try the feature
- [ ] 3-5 social posts: one per platform, native format per channel
- [ ] In-app announcement or product notification set up
- [ ] Changelog entry published
- [ ] Customer success / support team briefed on the new feature
- [ ] Any updated documentation or help articles published

### Tier 3 (Weekly Patch / Changelog)

- [ ] Changelog entry written: brief, specific, non-technical where possible
- [ ] Changelog published to public changelog page (if applicable: Beamer, Headway, or custom)
- [ ] 1 social post: X or LinkedIn, short, specific, links to changelog
- [ ] In-app notification if the change impacts existing user workflows
- [ ] No email required unless the fix addresses a widely-reported user issue

### Quarterly Major Announcement

- [ ] Evaluate whether anything in the roadmap warrants a Tier 1 launch (new feature, category expansion, major milestone)
- [ ] If yes: begin full pre-launch checklist (T-8 weeks)
- [ ] If no: schedule a "what's coming" content piece (blog post or founder LinkedIn post) to maintain launch momentum
- [ ] Assess Product Hunt re-launch opportunity for major updates (products can re-launch after 6 months)
- [ ] Review launch supporter list: re-engage for the next major launch
- [ ] Update social proof library with new testimonials, metrics, and case studies

---

## 6. Launch Content Templates

Detailed templates and structures for each content type in a Tier 1 launch. For the content type overview, see SKILL.md Section 5.

### 6.1 Launch Blog Post Template

**Structure** (800-1,500 words):
1. **Headline**: Benefit-led or curiosity-driven. "Introducing {Product}: {Core Benefit in one line}." Or lead with the problem.
2. **Opening paragraph**: The problem, told as a story or with a striking data point. Use exact language from `paw-mkt-product-context.md` -- the words real customers use.
3. **The product**: What it does in 2-3 sentences. One clear value statement per paragraph.
4. **Key features**: 3-5 features, each with a "so that" statement. Do not list specs -- lead with outcomes.
5. **Social proof**: 2-3 beta user quotes. A data point if available ("Beta users reduced [X] time by 40%").
6. **Who it's for**: Specific use-case examples. "If you are a {persona} who {situation}, {product} is for you."
7. **Pricing and availability**: Clear, direct, no surprises.
8. **CTA**: One primary action. Link to signup, trial, or Product Hunt.

**SEO**: Optimize for the primary launch keyword identified in `sostac/03-strategy.md` or `paw-mkt-product-context.md`. Include keyword in the title, H1, first 100 words, and meta description.

### 6.2 Email Announcement Template

**Send timing**: Launch day at 8-9am in the primary audience's timezone. Deliver to inbox before the social push.

**Subject line variants** (A/B test with 20% of the list, send winner to remaining 80%):
- Direct: "{Product Name} is live -- start free"
- Benefit-led: "Finally: {core benefit in one phrase}"
- Curiosity: "We've been building something..."
- Social proof: "{Number} people already tried it. Now you can."
- Personalized: "{First name}, it's launch day"

**Email body structure**:
```
Subject: [Variant A or B]
Preheader: [Expand with secondary benefit or urgency, 40-80 chars]

Opening line: [Story hook or striking statement -- not "we're excited to announce"]

Core value: [What the product does in 1-2 sentences. Use customer language.]

What you get:
- [Benefit 1 with specificity]
- [Benefit 2 with specificity]
- [Benefit 3 with specificity]

[Beta user quote -- attributed name and role]

[CTA button: "Try {Product} free" / "Get started" / "See it in action"]

[Secondary note: Product Hunt link with upvote ask, or limited-time offer if applicable]

[Signature: founder name, not brand name]
PS: [Add a personal note, a bonus, or repeat the primary CTA -- the PS is the second most-read element]
```

Bridge to paw-mkt-email for full email sequence strategy and deliverability setup.

### 6.3 Social Post Templates

Write native formats per platform. One brief per platform, written as it will actually be posted.

**X / Twitter -- Launch Thread**:
```
Tweet 1 (hook): Today we're launching {Product}. [One surprising statement about the problem or the solution.]
Tweet 2: The problem: [Story of the pain point in 2-3 sentences. Be specific.]
Tweet 3: What we built: [Product + core mechanic + key differentiator]
Tweet 4: Key things you can do: [3-4 bullet points, each with specificity and outcome]
Tweet 5: [Beta result or testimonial quote]
Tweet 6: Pricing and how to get started: [Direct, no friction]
Tweet 7: [Product Hunt link + upvote ask + gratitude]
Final tweet: [Reply to Tweet 1 with a summary card or demo GIF link]
```

**LinkedIn -- Founder Post**:
- Lead with the human story: why you built it, what problem you personally felt.
- 3-5 paragraphs, no bullet points in the opening hook.
- Pull quote from a beta user as social proof.
- Clear CTA with a link in the first comment (not the post body -- LinkedIn suppresses external links in post).
- Ideal length: 1,200-1,800 characters (stops at "see more" but does not feel truncated).

**Instagram**:
- Stories: behind-the-scenes launch day countdown (5-7 frames), CTA in final frame with link sticker.
- Feed post: product visual or results screenshot, short caption (2-3 sentences), CTA in bio link.
- Reels: 30-60 second demo or founder "here's what we built and why" to camera.

**Relevant Subreddits / Communities**:
- Write a genuine post, not a promotional blast. Lead with value.
- Structure: "I built {product} because {personal problem}. After {time} months and {beta users} users, we're launching. Here's what we learned: [3 specific insights]. Happy to answer any questions."
- Do not lead with "check out my product." Lead with the story or the insight.

### 6.4 Press Release Template (Tier 1 Launches Only)

Follow the structure from paw-mkt-pr SKILL.md Section 3.1. For launch-specific press releases:

- Headline: "Company Name Launches Product Name to Solve Specific Problem for Audience"
- Lead paragraph: What launched, who it serves, and the market context (size, trend, pain point).
- Second paragraph: Key differentiators and 1-2 specific outcomes from beta testing.
- Founder quote: Vision, motivation, market opportunity -- not a feature list.
- Customer/beta user quote: Specific outcome achieved, attributed.
- Pricing, availability, and call to action.
- Boilerplate and media contact.

Pair the press release with targeted journalist pitches. The press release is the supporting document; the pitch email is the hook. Bridge to paw-mkt-pr for full media outreach strategy.
