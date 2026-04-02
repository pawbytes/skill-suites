# Onboarding CRO Reference: Post-Signup Activation, First-Run Experience, Time-to-Value

**Purpose:** Frameworks, templates, and checklists for improving post-signup onboarding — from the moment a user creates an account through their first meaningful success with the product. Read this file when the user is optimizing an onboarding flow, trying to improve activation rates, reducing time-to-value, fixing drop-off in the first session, or improving day-7 or day-30 retention. This is a companion to `signup-cro.md` (which covers the pre-account flow) and is distinct from it — onboarding begins after the account exists.

---

## 1. The Activation Event

### What Activation Actually Means

Activation is not completing the signup form. It is not logging in for the first time. Activation is the moment a user experiences enough value from the product that they have a concrete reason to return. It is the "aha moment" — the specific action or outcome that strongly predicts long-term retention.

The activation event is different for every product. Getting this definition wrong is the most expensive mistake in onboarding CRO. Optimizing for the wrong event (e.g., "profile completion" when the real predictor is "first team invite sent") wastes every downstream effort.

### How to Identify the Aha Moment

**Step 1: Pull your retention cohort data.**
Segment users by whether they completed specific actions in their first session or first 7 days (whichever is appropriate for your product's usage cycle). Actions to test as candidates:
- Created first [core object] (project, campaign, report, document, contact)
- Connected an integration (calendar, CRM, email, Slack)
- Invited a team member
- Completed a first output (sent a message, published a post, ran a report, booked an appointment)
- Reached a specific usage depth (viewed 5+ pages, used feature X, spent >10 minutes)

**Step 2: Calculate retention rate for each cohort.**
For each action, calculate the 30-day and 90-day retention rate for users who completed it vs. users who did not. The action with the largest gap is your activation event candidate.

**Step 3: Validate causality vs. correlation.**
The action must be something you can cause more users to do — not just something that highly-motivated users naturally do. If "users who invite a team member retain at 3x the rate" but inviting requires an existing team, it may be a selection effect. Test by actively nudging users toward the action and measuring whether it changes retention.

**Step 4: Define a time bound.**
The activation event only predicts retention if it happens within a specific window. Common windows: first session, first 24 hours, first 7 days. Find the window where the completion-retention correlation is strongest. This becomes your activation deadline.

### Measuring Activation Rate

**Core metric:** Activation rate = (users who complete the activation event within the time window) / (users who created an account)

Track this as a funnel in your analytics tool (Mixpanel, Amplitude, Heap, or GA4 with custom events). The step-by-step funnel should be:

```
Account created → First login → [Step 1 of onboarding] → [Step 2] → ... → Activation event
```

Report activation rate weekly, segmented by:
- Acquisition channel (paid vs. organic vs. referral — they often behave very differently)
- Plan type (free vs. trial vs. paid)
- Company size or ICP segment (if known)
- Device type (mobile vs. desktop)
- Signup method (email vs. SSO)

A drop in activation rate that is isolated to one channel or segment tells you where to look first.

### Activation Rate Diagnostic

| Symptom | Likely cause | First thing to check |
|---|---|---|
| High login rate, low activation | Onboarding UI is confusing or empty state is demoralizing | Session recordings of non-activating users in first session |
| Low activation rate uniform across all channels | Aha moment not reached in onboarding — path too long | Funnel analytics: where do >50% of users drop off? |
| High activation, low 30-day retention | Wrong activation event defined — it does not predict value | Recohort: what do retained users do that activated-only users don't? |
| Activation varies by channel | Traffic quality or intent mismatch | Segment activation funnel by channel; check ICP match for each source |
| Activation fine on desktop, low on mobile | First-run experience not designed for mobile | Walk the mobile onboarding flow yourself on a real device |

---

## 2. Onboarding Audit Framework

### Step 1: Map Every Step in the Current Flow

Walk through the onboarding flow yourself using a fresh test account. Document every screen, modal, tooltip, prompt, and email in sequence. Do not rely on product documentation — flows drift. The actual experience is the only truth.

For each step, record:
- Screen name / URL
- The action required of the user
- Whether the step is mandatory or skippable
- Estimated time to complete
- Any decision the user must make (e.g., template selection, plan choice, role selection)

The result is an onboarding map. It will always be longer and more complex than anyone on the team believes.

### Step 2: Friction Inventory

For every step in the map, score it on three dimensions (1-5 each):

| Dimension | What to score |
|---|---|
| Clarity | Does the user know exactly what to do and why? 1 = completely unclear, 5 = completely obvious |
| Effort | How much work does this step require? 1 = major effort (fill form, upload file, wait for processing), 5 = zero effort (click one button) |
| Value visibility | Does completing this step make the product's value clearer? 1 = no visible connection to value, 5 = user can see an immediate benefit |

Steps with low clarity or low value visibility are redesign candidates. Steps with high effort and low value visibility are removal candidates.

### Step 3: Drop-Off Mapping

Pull funnel analytics for each step in the onboarding map. Calculate:
- Completion rate: what % of users who started this step completed it
- Absolute drop: how many users are lost here per week
- Cumulative loss: what % of starting users have already dropped off by this step

The highest-priority step to fix is rarely the one with the lowest completion rate — it is the one with the largest absolute user loss, weighted by how early it appears in the funnel.

**Priority formula:** Priority score = (Absolute weekly user loss at this step) x (Effort score to fix it)

Fix the early, high-loss steps first. A 5% improvement to a step that 90% of users hit is worth more than a 30% improvement to a step only 20% of users reach.

### Step 4: Session Recording Review

Watch 25 session recordings of users who did not activate. Watch specifically for:
- Rage clicks (user clicking repeatedly on something non-interactive)
- Back-and-forth navigation between the same two screens
- Long pauses followed by exit
- Form fields where users stop and do not resume
- Empty states the user stares at then abandons
- The exact moment of exit (what was on screen when the tab closed or session ended)

Tag each recording with the drop-off step. After 25 recordings, patterns become clear. Use these patterns to write your test hypotheses — they will be grounded in real observed behavior.

### Step 5: Qualitative Survey

Send a 1-question survey to users who signed up but did not activate within 7 days. Delivery method: email, sent at day 7 post-signup.

Subject: "Quick question about [Product Name]"
Body: "You signed up for [Product Name] but haven't had a chance to try it yet. What got in the way? (Takes 10 seconds.)"

Answer choices (radio buttons, pick the most relevant for your product):
1. I haven't had time yet
2. I couldn't figure out how to get started
3. I didn't see how it would help me
4. I'm waiting for my team / manager / someone else
5. Something else: [open text]

The distribution of these answers tells you whether the problem is motivation, clarity, or fit.

---

## 3. Empty State Design

### Why Empty States Kill Activation

The most dangerous moment in onboarding is the first time a user lands on a blank screen — an empty dashboard, an empty project list, an empty inbox. The user sees their own lack of engagement reflected back at them as a blank page. Without guidance, the majority will leave.

Empty states are not placeholders. They are the highest-leverage real estate in onboarding.

### The Three Components of an Effective Empty State

**1. Explain what goes here (context).**
The user should immediately understand what this space is for and why it matters. One sentence. Not marketing copy — functional description. "Your campaigns will appear here. Each campaign tracks performance across channels in one view."

**2. Tell them exactly what to do next (action).**
A single, specific, high-contrast CTA that initiates the first action. Button copy describes the output, not the mechanism. Not "Create" — "Create your first campaign." Not "Add" — "Add your first contact."

**3. Show them what it will look like (preview).**
A screenshot, illustration, or demo data showing a populated state. This reduces uncertainty and makes the value concrete. Users who can see what done looks like are significantly more likely to start.

### Empty State Patterns by Context

| Screen type | Recommended empty state pattern |
|---|---|
| Main dashboard | Guided setup prompt + CTA + social proof ("Teams like yours set this up in under 10 minutes") |
| Data table / list view | Sample data rows (greyed out or labeled "example") + CTA to add real data |
| Analytics / reporting | Placeholder charts with "data appears here once you [complete X action]" + deep link to X |
| Inbox / activity feed | Single instructional item showing what a real entry looks like + action prompt |
| Integrations panel | Recommended integrations for this user's profile pre-highlighted + 1-click connect |
| Team / members page | Invite prompt with specific benefit ("Invite a teammate to unlock collaboration features") |

### What Not to Do in Empty States

- Do not use a generic "Nothing here yet" message. It communicates nothing.
- Do not show empty states without a CTA. Every empty state must have a next action.
- Do not auto-populate with real user data until the user has created something. Showing fake "your" data is deceptive.
- Do not hide the empty state behind a modal or overlay. The empty state IS the experience.

### Sample Data vs. Demo Mode

For complex products where the empty state cannot easily communicate value, consider a demo mode or sample data load option:

- **Sample data:** Pre-populate the account with example records that demonstrate the product's full functionality. Clearly labeled as sample data. User can clear it when ready. Effective for project management, CRM, analytics, and reporting products.
- **Sandbox/demo mode:** User can explore the full product without connecting real data. Conversion to real use happens when user explicitly activates their own data. Effective for data-heavy products (BI tools, analytics platforms, financial software).

Sample data increases time-in-first-session and reduces empty-state abandonment. The cost is that some users confuse sample data for real data — label it clearly.

---

## 4. Progress Mechanics

### When to Use a Checklist

Use a setup checklist when the activation path involves 3-8 distinct steps that can be completed in any order, and completion of all steps is the activation event (or strongly correlates with it).

Checklist best practices:
- Show the checklist in a persistent location (sidebar, dashboard banner) — not as a modal that disappears.
- Start with 1-2 items pre-checked. Starting at zero feels daunting; starting with progress already made increases completion.
- Use verbs that describe outcomes, not features. "Connect your calendar" not "Calendar integration." "See your first report" not "Reports."
- Show estimated time per step. "~2 min" next to a step reduces abandonment from time anxiety.
- Celebrate completion. A moment of delight at checklist completion (confetti, congratulations message, CTA to explore) reinforces the behavior and sets a positive emotional anchor for the product.
- Auto-dismiss or collapse the checklist once completed. Do not leave the setup UI permanently visible after it is no longer relevant.

**When checklists fail:** If completion rate is below 40%, the steps are too hard, too unclear, or not perceived as valuable. Audit each step individually — the problem is almost always one or two specific steps that have disproportionate drop-off.

### When to Use a Progress Bar

Use a progress bar for linear, sequential onboarding flows where the user must complete steps in order (wizard-style setup, multi-step configuration, mandatory data entry).

Progress bar best practices:
- Show the number of steps ("Step 2 of 5") alongside or instead of a percentage. Steps feel more concrete.
- Never show a progress bar at 0%. Either skip step 1's progress bar or pre-count the account creation step as step 1 complete.
- Move the bar meaningfully with each step. A bar that jumps from 20% to 80% after one click feels good. A bar that moves 2% per step feels endless.
- Completion percentage should reach 100% before the "aha moment" step — so the user completes setup with momentum, not fatigue.

### When to Use a Guided Tour

Use a guided tour (sequential tooltip overlay) only when the user needs to learn the interface to do anything useful — i.e., when the product is complex enough that a user staring at a populated screen would not know where to start.

Guided tours fail when:
- They show up before the user has any context for why they matter.
- They have more than 5-7 steps (users click through without reading after step 3).
- They auto-replay on every login.
- They block the UI from being used ("you must complete the tour before proceeding").
- They are skippable with no consequence and 80% of users skip them.

Better pattern than a full guided tour: contextual tooltips that appear when a user first visits a new feature area, with a "dismiss" option and a "don't show again" option. These do not interrupt the flow and appear at the moment of maximum relevance.

### When to Use a Video

Embed a short product walkthrough video on the welcome screen or in the empty state for products where:
- The value is difficult to describe in text (visual products, complex workflows)
- The user population is less technical and more comfortable with video
- The product has a strong demo that makes the value immediately obvious

Video rules:
- Under 90 seconds for an overview video. Under 3 minutes for a feature walkthrough.
- Autoplay is off by default. Autoplay with sound is never acceptable.
- Include captions. A significant portion of users watch without sound.
- Show a clear CTA after or overlaid on the video ("Try it yourself →").
- Track video completion rate. If under 40%, the video is too long or not compelling enough.

### Progress Mechanics by Product Type

| Product type | Recommended mechanic | Typical activation steps |
|---|---|---|
| B2B SaaS (complex) | Setup checklist + contextual tooltips | Connect data, invite team, complete first core workflow |
| B2B SaaS (simple) | Linear progress bar | Create first item, customize one setting, share/publish |
| Consumer app (social) | Guided tour + follow suggestions | Build social graph first, content fill follows |
| Consumer app (utility) | Empty state CTA only | Single core action is the entire activation |
| Marketplace | Dual-sided checklist | Seller: list first item. Buyer: complete first purchase |
| Developer tool | Interactive quickstart (code + copy) | First successful API call or integration |

---

## 5. Welcome Email Sequence

### Sequence Architecture

The welcome email sequence runs parallel to in-app onboarding. Its job is to bring non-activating users back, reinforce value for activating users, and handle the time-delayed segment (users who signed up but have not had time to start). Every email in the sequence should have one job and one CTA.

### Day 0: The Welcome Email

Triggered: Immediately on account creation (within 2 minutes).

**Job:** Confirm account creation, set expectations for what comes next, and give the user their primary CTA to enter the product.

**Subject line options:**
- "Welcome to [Product] — here's where to start"
- "Your [Product] account is ready"
- "[First name], you're in — 3 things to do first"

**Body structure:**
1. Personal welcome (1 sentence, human tone — not corporate)
2. One-line reminder of the core value they signed up for (their "why")
3. Single CTA: "Set up your [Product]" → deep link to the first onboarding step, not the homepage
4. Optional: 2-3 bullet points of what they'll be able to do once set up (outcome-focused)
5. Founder/CEO sign-off with real name and optionally a reply prompt ("Hit reply if you have any questions — I actually read these.")

**What to avoid:** Attaching a PDF, linking to documentation, or including multiple CTAs. This email has one job.

### Day 3: The Value Email

Triggered: 72 hours after signup, sent only to users who have NOT yet activated.

**Job:** Re-engage non-activating users by making the value concrete and reducing perceived effort to return.

**Subject line options:**
- "What [Product] can do for you this week"
- "Takes 5 minutes — here's what you get"
- "[First name], your [Product] is waiting"

**Body structure:**
1. Acknowledge they haven't started yet (no guilt, just recognition)
2. One specific outcome or result other users achieve, with a concrete metric ("Our users save an average of 3.5 hours per week on reporting")
3. A customer quote or case study snippet (1-2 sentences, with name and company)
4. Single CTA: "Finish your setup" → deep link to the onboarding checklist or the first incomplete step
5. Objection preempt: "It takes less than 10 minutes to get your first [result]."

### Day 7: The Social Proof / FOMO Email

Triggered: 7 days after signup, sent only to users who have NOT yet activated.

**Job:** Social proof + urgency without false scarcity. Show them what they are missing by not starting.

**Subject line options:**
- "How [Company Name] [achieved outcome] with [Product]"
- "This took them 8 minutes. Here's what happened."
- "What your competitors are doing with [Product]"

**Body structure:**
1. Lead with a specific customer story (name, company, specific result, time to result)
2. 2-3 bullet points of what this customer can now do that they couldn't before
3. One testimonial quote (the more specific the better: "Before [Product] I spent 4 hours every Friday pulling reports. Now it takes 12 minutes.")
4. Single CTA: "See how [Customer Company] did it" → can link to a case study or directly to onboarding

### Day 14: The Last-Chance / Offer Email

Triggered: 14 days after signup, sent only to users who have NOT yet activated.

**Job:** This is the last email in the non-activation sequence. Either rescue the user or gracefully confirm they are not a fit.

**Subject line options:**
- "Still figuring out [Product]? Let's fix that."
- "Should I close your account?"
- "One thing before we stop emailing you"

**Body structure (pattern A — offer help):**
1. Direct acknowledgment: "You signed up X days ago but haven't had a chance to try [Product] yet."
2. Offer: a 15-minute onboarding call / a done-for-you setup / a live demo
3. Remove friction from the offer: calendar embed, 3 available times, no sales pitch promise
4. Single CTA: "Book a 15-minute setup call"

**Body structure (pattern B — the break-up email):**
1. "I'm going to stop emailing you about [Product] — unless you want me to keep going."
2. What they'll lose by not starting (specific, concrete outcome)
3. Simple reply or click to express continued interest
4. If no engagement: remove from onboarding sequence, enter dormant re-engagement cadence (30 days later)

The break-up email has counter-intuitively high response rates (2-5x normal click rates). Its honesty triggers a re-evaluation that polite follow-up emails do not.

---

## 6. In-App Prompts and Tooltips

### Placement Principles

**Principle 1: Appear at the point of action, not before it.**
A tooltip explaining a feature should appear when the user is hovering over or interacting with that feature — not as a startup overlay. Context-triggered prompts have 3-5x higher engagement than scheduled overlays.

**Principle 2: One message per prompt.**
Each tooltip, banner, or modal should have exactly one message and one action. If you have two things to say, create two prompts at two different moments.

**Principle 3: Dismiss without guilt.**
Every in-app prompt must be dismissable with a single click. Never require a user to complete an action to close a prompt. The "X" close button must be visible without hovering.

**Principle 4: Remember dismissal.**
If a user dismisses a prompt, it should not reappear on the next session. Store dismissal state server-side, not in local storage (which clears). A prompt that reappears after dismissal is one of the fastest ways to create a hostile relationship with your product.

**Principle 5: Do not stack prompts.**
Never show more than one tooltip, banner, or modal at a time. If multiple prompts are triggered simultaneously, queue them and show them in sequence — one per session. Alert fatigue kills prompt engagement within 3-4 sessions.

### Copy Length by Prompt Type

| Prompt type | Max recommended copy |
|---|---|
| Tooltip (hover or contextual) | 1-2 sentences (25-40 words) |
| Banner (top of screen) | 1 sentence + CTA (15-20 words) |
| Spotlight modal (feature highlight) | Headline (8-10 words) + 2-3 sentences of body + single CTA |
| Welcome modal (first login) | Headline + 3-5 bullet points + primary CTA + secondary skip link |
| Inline empty state prompt | 1 sentence explaining value + 1 CTA button |

### Contextual vs. Scheduled Triggers

**Contextual triggers** fire based on what the user is doing:
- User visits a feature area for the first time → explain what it does
- User completes a step → congratulate and prompt the next step
- User fails to complete a step after N attempts → offer help
- User reaches an integration page → suggest the most popular integration for their use case
- User creates their 5th [item] → suggest organizing with folders or tags

**Scheduled triggers** fire based on time:
- First login → welcome modal
- Day 3 of free trial, not activated → re-engagement banner
- Day X of trial, approaching expiry → upgrade prompt
- Nth day of weekly usage → feature discovery nudge for advanced features

Contextual triggers are almost always more effective. Use scheduled triggers only when you have no behavioral signal to act on.

### Prompt Copy Principles

- Lead with the benefit, not the feature name. "See how your changes affect performance" not "Analytics is now available."
- Use second person, present tense, active voice. "Invite your team to collaborate" not "Team collaboration can be initiated."
- Make the CTA copy describe what happens next. "See live data" or "Invite your first teammate" not "Learn more" or "Try it."
- Keep it conversational. In-app prompts that sound like press releases create friction. They should sound like a colleague showing you something useful.

---

## 7. Activation Benchmark Table

Use these benchmarks to calibrate expectations and identify outliers. These are industry-derived ranges — your specific product, pricing, and traffic mix will affect where you fall within each range.

### Activation Rate by Product Type

| Product category | Definition of activation used | Typical activation rate | Notes |
|---|---|---|---|
| B2B SaaS (self-serve, SMB) | Completed core workflow within 7 days | 25-45% | Wide range due to variation in product complexity |
| B2B SaaS (enterprise, high-touch) | Connected integration or invited team within 14 days | 40-65% | Higher because of sales-assist and managed onboarding |
| B2B SaaS (dev tools / API) | First successful API call within 7 days | 20-40% | Documentation quality has outsized impact |
| Consumer SaaS (freemium) | Completed first core action in first session | 30-60% | First-session activation is critical; most never return |
| Consumer app (mobile) | Returned on day 2 (D1 retention as proxy) | 25-45% | Varies heavily by category (games vs. utility vs. social) |
| E-commerce (first purchase) | Completed first order within 30 days | 2-8% of site visitors | Different metric basis — of email signups, 15-30% |
| Marketplace (two-sided) | Completed first transaction (buy or sell) within 14 days | 10-25% | Typically measured separately per side |
| PLG (product-led growth) expansion | Upgraded from free to paid within 30 days | 3-8% of free users | Mediated by activation rate — only activated users upgrade |

### First-Session Benchmarks

| Metric | Weak | Average | Strong |
|---|---|---|---|
| First-session completion of onboarding checklist | <15% | 20-35% | >45% |
| Time to activation event (median) | >30 min | 10-20 min | <10 min |
| Second session (D1 return rate) | <20% | 25-40% | >50% |
| Welcome email open rate | <25% | 35-50% | >55% |
| Day-7 activation rate (all signups) | <15% | 25-40% | >50% |

### Activation → Retention Multiplier

The relationship between activation and long-term retention is non-linear. Products with strong activation typically show:
- 2-4x higher 30-day retention for activated vs. non-activated users
- 3-6x higher 90-day retention
- 5-10x higher conversion from free to paid (for freemium products)

These multipliers make activation the highest-ROI area of onboarding investment in almost all cases.

---

## 8. Quick Win Checklist

Ten specific, immediately actionable improvements. Each of these can be implemented within 1-2 weeks and has a strong evidence base.

**1. Add sample data to the empty state dashboard.**
If users land on a blank dashboard after signup, auto-populate it with clearly labeled example data. Target: reduce first-session abandonment by 15-30%.

**2. Pre-check 1-2 items on the onboarding checklist.**
If your checklist starts at 0%, create a "step 0" (account creation) that is pre-checked. Showing progress already made increases checklist completion. Target: 10-20% improvement in checklist start rate.

**3. Change the post-signup redirect to the first onboarding step, not the homepage or dashboard.**
Users who land on a generic dashboard immediately after signup have no clear next action. Deep-link them directly to the first onboarding action. Target: reduce first-step drop-off by 10-25%.

**4. Add time estimates to each onboarding step.**
"~2 minutes" next to each checklist item significantly reduces abandonment caused by time uncertainty. This is a one-line copy change. Target: 5-15% improvement in step completion.

**5. Send the Day 0 welcome email with a deep link to the first onboarding step.**
If the welcome email links to the homepage or generic dashboard, change it to a deep link directly to the next incomplete onboarding step. This removes the "where do I start?" friction on re-entry.

**6. Remove or defer one mandatory field from the post-signup setup flow.**
Every required field in onboarding is a conversion barrier. Identify the field with highest perceived friction (usually "billing info," "team size," or "how did you hear about us") and either defer it or make it optional.

**7. Add a "skip for now" option to every non-critical setup step.**
Users blocked by a step they cannot complete (e.g., "invite your team" when they are solo evaluating) abandon entirely. A skip option lets them reach the activation event without being blocked.

**8. Install Microsoft Clarity (free) and watch 20 session recordings of non-activating users.**
This costs nothing and consistently generates 3-5 high-confidence test hypotheses per audit. There is no faster way to identify friction than watching real users fail.

**9. Rewrite empty state CTAs to describe the output, not the action.**
Change "Create Project" to "Create your first project." Change "Add Contact" to "Add your first contact." This small specificity change reduces perceived effort. Target: 5-10% improvement in empty state CTA click rate.

**10. Add a single-question survey to the Day 7 non-activation email.**
"What got in the way?" with 4 multiple-choice answers takes 2 hours to set up and generates qualitative data that can reshape the entire onboarding strategy. Run it for 4 weeks and read every response before making onboarding changes.
