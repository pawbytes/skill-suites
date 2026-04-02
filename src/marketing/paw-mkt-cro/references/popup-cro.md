# Popup and Modal CRO Reference: Exit-Intent, Email Capture, Slide-Ins, Promotional Banners

**Purpose:** Specific frameworks, targeting logic, offer design principles, and test priorities for optimizing popups and modals. Read this file when the user is implementing, auditing, or improving any on-site overlay — exit-intent popups, email capture modals, slide-in widgets, or promotional banners. Not for cookie consent banners (brief note in Section 9).

---

## 1. Popup Type Taxonomy

### Exit-Intent Popup
**Trigger:** JavaScript detects upward mouse movement toward the browser chrome (desktop) or a back-gesture / tab-switching signal (mobile approximations).

**When to use:**
- Final retention attempt on a high-intent page (pricing, product page, checkout) where the user is about to leave without converting.
- Lead capture on blog posts and content pages where organic traffic is high and session value is otherwise zero.
- Abandoned cart recovery (e-commerce) — show a discount or scarcity reminder at exit.

**When NOT to use:**
- On pages where the user has just converted (thank you pages, order confirmation pages). Exit intent here is intentional — let them leave.
- Immediately after another popup was already shown in the same session.
- On pages where the natural next action is to leave (blog post "back to blog" flow — user is done reading, the session was a success).

**Performance profile:** Highest conversion rate of all popup types when targeted to high-intent segments. Industry median: 3-5% of triggered sessions. Top quartile: 8-12%.

---

### Scroll-Triggered Popup
**Trigger:** User scrolls past a defined percentage of page depth (commonly 50-70%).

**When to use:**
- Content upgrades on blog posts — the user who reached 60% scroll has demonstrated genuine engagement.
- Long-form landing pages — trigger after the user has read the core value proposition.
- Article content where a "get more like this" offer is genuinely relevant to what they just read.

**When NOT to use:**
- Short pages (under 600px scrollable height). The trigger fires immediately and is indistinguishable from an entry popup.
- Pages where the user is actively scrolling to find something specific (documentation, FAQ pages). Interrupting task-focused behavior is guaranteed to annoy.

**Performance profile:** Conversion rates 2-4% on blog content. Higher (4-7%) when the popup is directly thematically matched to the article (content upgrade with a downloadable checklist matching the article topic).

---

### Time-Delayed Popup
**Trigger:** Fires after a defined number of seconds on the page (common values: 15s, 30s, 60s).

**When to use:**
- General newsletter capture on sites where engagement is shallow (users bounce quickly — exit intent may not fire consistently).
- Low-commitment offers where timing matters less than getting the offer in front of the user.

**When NOT to use:**
- Do not set delay below 10 seconds. Popups under 10 seconds feel like an immediate door-block and reliably increase bounce rate.
- Do not use on high-urgency transactional pages (checkout, signup) — any distraction here costs you a conversion.
- Do not stack a time-delayed popup on a page that already has an exit-intent popup. One per session per page.

**Performance profile:** Lowest conversion rate of all non-entry types. Median 1-2%. Works best when combined with session rules (do not show to returning subscribers).

---

### Click-Triggered Popup (On-Click Modal)
**Trigger:** User explicitly clicks a button, link, or inline CTA ("Download the checklist," "See pricing," "Get the coupon").

**When to use:**
- Any form that follows a user-initiated action. This is the highest-consent popup type.
- Inline content upgrades (article sidebar: "Download the full template").
- Pricing page plan selection (clicking "Get started" opens a signup or payment modal inline).

**When NOT to use:**
- There is almost never a reason not to use this type. The user chose to open it.
- One exception: do not use a modal for complex multi-step checkout flows — friction here is expensive. Use a dedicated page.

**Performance profile:** Best performing type — users who click to open a popup convert at 20-50% because they self-selected. Benchmark is meaningless compared to the other types; always track form-start-to-complete rate (target: 70%+).

---

### Entry Overlay (Welcome Mat / Splash)
**Trigger:** Fires immediately on page load, covers the full screen or a large portion of it.

**When to use:**
- Time-sensitive announcements (site-wide sale, event starting today, critical service notice).
- Age verification or legal gates where compliance requires acknowledgment before access.
- Extremely high-value, one-time offers where email capture is the primary business goal of the session (dedicated lead-gen landing pages).

**When NOT to use:**
- Almost every other context. Entry overlays are the most disruptive popup type. Google's mobile interstitial penalty applies to popups that cover the main content on mobile immediately after a search click.
- Do not use on pages receiving significant organic search traffic — the SEO penalty risk is real and documented.
- Do not use on new visitor first sessions unless the offer is so compelling that conversion is near-guaranteed.

**Performance profile:** High raw conversion rates (5-10% of sessions) due to visibility, but inflated by users who dismiss without engaging. Net list quality is lower than scroll or exit-intent triggered popups.

---

### Slide-In (Corner Widget)
**Trigger:** Slides in from a corner (typically bottom-right) after scroll or time delay. Does not block content.

**When to use:**
- Persistent offers (live chat prompts, newsletter subscribe) that should be available throughout the session without interrupting.
- Retargeting prompts for users who have visited 2+ times without converting.
- Low-friction offers that benefit from visibility but do not require urgency.

**When NOT to use:**
- Do not show simultaneously with a full popup. One overlay at a time.
- On mobile, a slide-in that covers the bottom navigation creates accessibility failures. Test on 390px before deploying.

**Performance profile:** 0.5-1.5% of sessions. Intended to be ambient, not urgent — do not optimize for high popup conversion rate; optimize for low dismissal and positive engagement.

---

## 2. Targeting Logic

Untargeted popups convert poorly and damage user experience. Every popup deployment decision should answer four targeting questions before launch.

### URL Targeting

| Rule type | Use case | Example |
|---|---|---|
| Exact URL match | Specific campaign landing page | `/trial-start` |
| Path contains | Section-specific targeting | URL contains `/blog/` |
| Path starts with | Category targeting | URL starts with `/pricing` |
| Regex match | Complex multi-path rules | `/(pricing|plans|upgrade)/` |
| Exclude URL | Prevent duplicates | Exclude `/thank-you`, `/checkout` |

**Critical exclusions to always configure:**
- All post-conversion pages (thank-you, order confirmation, dashboard root for logged-in users).
- Checkout and payment pages.
- Pages where another popup is already active.

---

### Visitor Segment Targeting

| Segment | Rule | Recommended popup behavior |
|---|---|---|
| First-time visitor | Cookie not present / session count = 1 | Welcome offer or soft content capture |
| Returning visitor (2-3 visits) | Session count = 2-3 | Stronger offer, "You've been here before" angle |
| Existing subscriber | Email cookie or list membership flag | Do NOT show email capture. Show a different offer or suppress entirely. |
| Paid customer (logged in) | User role / cookie | Suppress all acquisition popups. Show upgrade or cross-sell only if relevant. |
| Cart abandoner (e-commerce) | Items in cart + exit intent | Discount or free shipping offer specifically tied to the cart. |

**Suppressing known subscribers:** If your popup tool connects to your ESP (Klaviyo, Mailchimp), configure list membership suppression. Showing an email capture popup to an existing subscriber is a trust-damaging error.

---

### Device Targeting

| Device | Key rules |
|---|---|
| Desktop | All popup types viable. Full exit-intent detection. |
| Mobile | Avoid full-screen entry overlays (Google penalty). Use slide-ins and bottom-of-screen bars instead. Exit intent via back-gesture is inconsistent — use scroll depth or time delay. |
| Tablet | Treat as mobile for sizing. Desktop exit-intent detection can work. |

**Mobile-specific sizing requirements:**
- Modal width: 90% of viewport (never fixed pixel width that causes horizontal scroll).
- CTA button: minimum 48px height, full width.
- Text: minimum 16px body, 20px headline.
- Close button: minimum 44x44px tap target, positioned in corner with clear visibility.

---

### Session-Based Rules

Layer these rules on top of URL and segment targeting to control frequency and fatigue:

| Rule | Recommended default |
|---|---|
| Show delay after page load | Minimum 8 seconds (even for exit-intent, allow time for exit-intent JS to initialize) |
| Show frequency per session | Once per session per popup type |
| Show frequency per visitor | Once every 30 days after dismiss (7 days if user started but did not complete the form) |
| Do not show after conversion | Always suppress after email capture for this popup's goal |
| Suppress on return visit within 24h | Yes — if user dismissed yesterday, give them a day off |

---

## 3. Trigger Timing — The Research

### Scroll Depth Timing

Academic and practitioner research on scroll-triggered offers converges on: users who have scrolled 50-70% of a page are in the highest-intent zone before they reach the end (where intent has been resolved). Key findings:

- **Under 30% scroll:** User is orienting. Too early. Conversion rate at this point is 30-50% lower than at 50-70%.
- **50-60% scroll:** Optimal for most blog content — user has consumed enough to know they are interested but has not finished.
- **70-80% scroll:** Better for long-form content (guides, whitepapers) where a content upgrade at the end feels like a natural continuation.
- **100% scroll (end of post):** High intent signal. Use for "get the checklist" content upgrades. User just finished — offer the companion resource.

**Recommendation by page type:**

| Page type | Scroll trigger % |
|---|---|
| Short blog post (under 800 words) | 70% |
| Long blog post (1500+ words) | 55% |
| Long-form pillar page / guide | 60% |
| Product page | 50% |
| Pricing page | 40% (user is already evaluating — intervene earlier) |

---

### Time on Page Timing

Time delay should be calibrated to the expected "time to value" on the page — when would a genuinely interested user have finished absorbing the page content?

| Page type | Recommended delay |
|---|---|
| Simple landing page | 20-30 seconds |
| Average blog post | 45-60 seconds |
| Long-form guide | 90-120 seconds |
| E-commerce product page | 15-20 seconds (purchase intent is faster) |

Using time delays shorter than 8 seconds on any page produces high raw impressions and low quality. Never set below 8 seconds.

---

### Exit-Intent Distance

Exit-intent detection typically fires when the cursor moves toward the top 5-10% of the viewport. Key calibration notes:

- **Detection threshold matters:** Tools that detect at 5% from top convert better than those detecting at 10% — users who reach 5% are genuinely leaving, reducing false positives.
- **Delay after page load before exit-intent activates:** Set to 10-15 seconds minimum. Otherwise the popup fires for users who opened the tab and switched away immediately (low intent, high irrelevance).
- **Mobile exit-intent:** True exit-intent (cursor-based) does not exist on mobile. Use time-on-page + scroll depth as a proxy. A user who spent 30+ seconds and reached 50%+ scroll but is about to leave is a good proxy target.

---

## 4. Offer Design

The offer is the primary lever on popup conversion rate. Copy and design matter, but a weak offer cannot be saved by good copy.

### Offer Type Performance Ranking

| Offer type | Typical popup CVR | Best context |
|---|---|---|
| High-value content upgrade (directly matches article) | 5-12% | Blog posts, guides |
| Discount with urgency (e-commerce, time-boxed) | 4-10% | Product pages, cart abandonment |
| Free tool / calculator / template | 4-8% | Broad content audiences |
| Webinar / event registration | 3-7% | Niche, topic-specific audiences |
| Email newsletter (general) | 1-3% | Low — requires strong brand |
| "Stay updated" / generic newsletter | 0.5-1.5% | Avoid — too vague to work |

---

### Content Upgrade Design

A content upgrade is a resource that extends the value of the page the user is currently on. It is the highest-converting popup offer type for content-driven sites.

**Strong content upgrades:**
- Checklist version of a how-to article ("Download the 12-step checklist")
- Spreadsheet template complementing a financial or operational guide
- PDF version of a long guide ("Get the full guide as a PDF")
- Bonus examples beyond what the article covers ("7 more examples not in the article")
- Email course that expands on the topic (5-day sequence)

**Weak content upgrades:**
- Generic lead magnets unrelated to the page ("Download our free ebook")
- Repurposed sales collateral (pricing sheets, product brochures)
- Content that is obviously available for free elsewhere without the email
- Anything gated that the user did not signal interest in

---

### Discount Framing for E-Commerce

When the offer is a discount, framing determines whether it feels like a gift or a manipulation tactic:

| Framing type | Example | When it works |
|---|---|---|
| Percentage savings | "Save 15% on your first order" | High-AOV products where % is meaningful |
| Absolute amount | "Get $20 off your first order" | Low-to-mid AOV where $20 sounds large |
| Free shipping | "Free shipping on your first order" | When shipping cost is the #1 checkout drop-off reason |
| Bundle unlock | "Add one more item — get free shipping" | Cart value near the free-shipping threshold |
| Scarcity + discount | "10% off — offer ends at midnight" | When the urgency is real and not manufactured |

**Manufactured urgency caveat:** "Offer expires in 10 minutes" countdown timers that reset on page reload are widely recognized by consumers. They damage trust and brand credibility. Use real urgency (actual sale end dates) or no urgency at all.

---

### What Feels Spammy (and Why)

These patterns reliably reduce list quality and damage brand perception even when they generate email addresses:

- Offer text that is clearly the same as the site's standard newsletter, reframed as exclusive
- Countdown timers that are not real
- Dismiss copy that is passive-aggressive ("No thanks, I don't want to save money")
- Showing a popup on the first page, then another on the second page, then another on exit
- Auto-checked "subscribe to our newsletter" box hidden in the form
- Offering a discount, then making the code difficult to find after email submission

---

## 5. Copy and Design Principles

### Headline

The popup headline has approximately 2 seconds to capture attention. It must communicate the offer's specific value, not the category.

**Weak headlines:**
- "Subscribe to our newsletter" (category, not value)
- "Don't miss out!" (vague, no specificity)
- "Wait! Before you go..." (pure manipulation framing without substance)

**Strong headlines:**
- "Get the exact email sequence we used to close $200k in B2B deals" (specific, outcome-framed)
- "Download: The 47-point landing page checklist" (concrete, titled resource)
- "15% off your first order — grab it before you go" (clear offer, mild urgency)
- "The free Notion template 14,000 founders use for quarterly planning" (social proof in headline)

**Headline formula:** "[What they get] + [Specific value / outcome / social proof]"

---

### Body Copy

- Maximum 2 sentences. Popups are not essays.
- Expand on the headline benefit — do not repeat it.
- Address the primary objection pre-emptively: "No spam. One email per week, unsubscribe anytime."
- If the offer is a download, describe what is inside: "12 pages. 47 checks. Downloadable PDF."

---

### CTA Button Copy

Apply the same rules as page CTAs (see page-cro.md Section 3) but optimized for specificity to the popup offer:

| Popup offer | Weak CTA | Strong CTA |
|---|---|---|
| Lead magnet download | "Submit" | "Send me the checklist" |
| Discount code | "Get offer" | "Unlock 15% off" |
| Newsletter | "Subscribe" | "Get weekly templates" |
| Webinar | "Sign up" | "Save my seat" |
| Content upgrade | "Download" | "Download the PDF guide" |

First-person possessive ("Send me," "Get my," "Save my") consistently outperforms second-person ("Get your") in A/B tests. Difference is typically 10-20% lift on click rate.

---

### Dismiss Copy

The close/dismiss option is required. The design and copy of the dismiss element matters:

**Acceptable dismiss options:**
- X button (top right, minimum 44x44px tap target)
- Text link: "No thanks" / "Close" / "Not now"

**Dismiss copy to avoid:**
- "No thanks, I don't want [outcome]" — e.g., "No thanks, I don't want to grow my business." This is condescending and user-hostile. It has become a meme. Stop using it.
- Making the dismiss option very small, very low contrast, or difficult to find. Users who cannot dismiss easily will bounce from the site. The dismiss is not your enemy — users who dismiss were not going to convert anyway.

---

### Visual Hierarchy Checklist for Popups

- [ ] Headline is the largest text element in the popup. 22-28px minimum on desktop.
- [ ] CTA button has a unique color from the rest of the popup and is the most visually prominent element after the headline.
- [ ] Form field(s) are clearly labeled or use descriptive placeholder text.
- [ ] Trust micro-copy ("No spam," "Unsubscribe anytime") is visible but not competing with the headline or CTA.
- [ ] Popup width: 480-600px desktop, 90% viewport width mobile.
- [ ] Background overlay: dark enough to focus attention on the popup (70-80% opacity), not so dark the page is invisible.
- [ ] Image or illustration: use only if it directly reinforces the offer. Stock photos add no value and dilute credibility.
- [ ] Close button is visible on first glance. Do not hide it.

---

## 6. Form Fields in Popups

### The Single-Field Case

Every additional field in a popup form reduces completion. For email capture popups specifically, research from Sumo (analysis of 2 billion popup impressions), Privy, and Klaviyo consistently shows:

- **Email only:** Median popup conversion rate 3-5%
- **Email + First Name:** Median 2-3% (approximately 30-40% reduction)
- **Email + Name + Phone:** Median under 1%

The argument for adding first name ("so we can personalize emails") is usually overstated. Most ESPs allow personalized emails with first name after collection, but the uplift in email open rates from personalization (typically +5-15% on open rate) does not offset the 30-40% reduction in form completions.

**Single-field rule:** Unless you have a specific, tested business reason to collect more data at the popup stage, use email only.

---

### When Multi-Field Popups Are Justified

| Scenario | Additional field justified |
|---|---|
| Webinar registration where first name is needed for the confirmation email and attendance system | First name |
| Lead gen where routing depends on company size (enterprise vs. SMB) | Company size dropdown (5 options max) |
| Physical product delivery offer where address is required | Skip the popup — use a dedicated page |
| Qualification for a high-value offer (e.g., free audit, personalized demo) | Role + Company — but use a separate page, not a popup |

---

### Phone Number in Popups

Avoid entirely. Phone field in a popup is the single highest abandonment-causing field across every documented study. Even "optional" phone fields reduce form completion because they signal a sales follow-up call, which most users do not want from a popup.

Exception: SMS marketing opt-in popups where the offer explicitly delivers value via SMS (coupon to phone, order updates). In this case: phone only, explicit SMS consent language required, and TCPA/GDPR compliance must be confirmed.

---

## 7. A/B Testing Priorities for Popups

Run tests in this order. Do not jump to low-impact variables before the high-impact ones have been resolved.

### Priority 1: The Offer (Expected lift: 50-200%)

This is the most important test. Before testing headline copy or button color, confirm the offer itself is the strongest possible.

- Test: Content upgrade specific to the article vs. generic newsletter opt-in
- Test: Discount amount (10% vs. 15% vs. free shipping)
- Test: Free tool/template vs. email course (sequence)

Minimum sample size: 500 conversions per variant before concluding. Offer tests have high variance.

---

### Priority 2: Trigger Timing (Expected lift: 20-60%)

The same offer shown at the wrong time converts far below potential.

- Test: Exit intent vs. 60% scroll depth (on blog posts)
- Test: 15-second delay vs. 45-second delay (for time-based triggers)
- Test: First session only vs. first and second session (frequency rules)

---

### Priority 3: Headline Copy (Expected lift: 15-40%)

After confirming the offer and timing are correct, test headline framing.

- Test: Benefit-led headline vs. offer-led headline ("Grow your email list faster" vs. "Download: The 47-point email checklist")
- Test: Headline with social proof number vs. without ("Used by 14,000 founders" vs. no number)
- Test: Question format vs. statement format

---

### Priority 4: CTA Button Copy (Expected lift: 10-25%)

- Test: First-person possessive ("Get my checklist") vs. second-person ("Get your checklist")
- Test: Specific verb ("Download the guide") vs. generic verb ("Get started")
- Test: CTA with implicit commitment ("Try it free") vs. explicit value ("Get the free guide")

---

### Priority 5: Form Fields (Expected lift: 10-40% on completion, negative on lead quality)

- Test: Email only vs. email + first name
- Test: Single-step form vs. two-step (button click opens form, rather than form always visible)

The two-step approach (Zeigarnik effect / micro-commitment) consistently increases completions: showing a CTA button first, then revealing the form on click, can lift completions 20-40% by reducing perceived friction at first glance.

---

### Priority 6: Visual Design (Expected lift: 5-15%)

Test design only after offer, timing, headline, and CTA have been validated:

- Test: With image vs. without image
- Test: CTA button color variants (high-contrast vs. brand color)
- Test: Popup width (compact 400px vs. standard 560px)

---

### What NOT to Test (Until Everything Above Is Done)

- Background color of the popup body
- Font weight variations
- Exact word substitutions within a validated headline
- Animation style (fade vs. slide)

These micro-optimizations are real but small. They do not offset a weak offer or wrong trigger timing.

---

## 8. Popup Tools Comparison

| Tool | Best for | Email capture | Targeting depth | A/B testing | Price |
|---|---|---|---|---|---|
| **Privy** | E-commerce (Shopify) | Native + ESP sync | Good — cart value, visit count, device | Yes, built-in | Free tier; paid from ~$30/mo |
| **OptinMonster** | Agency / multi-site deployments | ESP integrations (50+) | Excellent — full rule builder, AdBlock detection | Yes, built-in | From $16/mo (basic) to $49/mo (growth) |
| **Klaviyo Forms** | Klaviyo email users (e-commerce) | Native to Klaviyo — no sync needed | Good — segment-based, device | Limited A/B | Included with Klaviyo |
| **Sumo** | Content sites, blogs | ESP integrations | Basic — URL, device, scroll % | Yes | Free tier; paid from $39/mo |
| **ConvertKit Forms** | Creator / newsletter businesses | Native to ConvertKit | Basic — URL matching, device | Limited | Included with ConvertKit |
| **Wisepops** | Mid-market e-commerce + SaaS | ESP integrations | Excellent — JS conditions, UTM, user properties | Yes | From $49/mo |
| **Getsitecontrol** | Simple deployments | ESP integrations | Good | Yes | From $9/mo |

**Agency recommendation:** OptinMonster for clients needing maximum targeting sophistication and multi-site management. Privy for Shopify-first e-commerce clients (native integration reduces setup friction). Klaviyo Forms for clients already on Klaviyo — avoids a second tool for simple email capture.

---

## 9. Benchmarks

### Popup Conversion Rate by Type

| Popup type | Median CVR | Top quartile | Bottom quartile |
|---|---|---|---|
| Click-triggered (on-click modal) | 25-45% of openers | 55%+ | Under 15% |
| Exit-intent (targeted) | 3-5% of triggered sessions | 8-12% | Under 1.5% |
| Scroll-triggered (content upgrade) | 4-7% of triggered sessions | 10-15% | Under 2% |
| Time-delayed (general offer) | 1-3% of triggered sessions | 5-8% | Under 0.5% |
| Slide-in widget | 0.5-1.5% of sessions | 3-5% | Under 0.2% |
| Entry overlay (full-screen) | 5-10% of sessions | 12-18% | Under 2% |

*CVR = form completions / popup triggered impressions. "Bottom quartile" = result indicating the popup is suppressing rather than supporting conversion.*

---

### Popup Conversion Rate by Industry

| Industry | Expected popup CVR (email capture) | Notes |
|---|---|---|
| E-commerce | 3-8% | Discount offer required to hit top end |
| B2B SaaS / content | 2-5% | Content upgrades needed for top end |
| Media / publishing | 1-4% | General newsletter; brand strength matters |
| Agency / services | 1-3% | High-value lead gen — quality over quantity |
| Education / creator | 3-7% | Strong affinity audiences respond well |

---

### What "Good" Looks Like

A popup is performing well when:
- Conversion rate is at or above the industry median for its type and offer.
- Unsubscribe rate from popup-acquired emails is below 2% per send (high unsubscribes indicate misaligned offer — users subscribed for something they are not getting).
- Bounce rate on pages with popups is not materially higher than on equivalent pages without popups (a popup that damages bounce rate is hurting SEO and session quality).
- Email engagement (open rate, click rate) from popup-captured subscribers is within 20% of organically acquired subscribers.

A popup is underperforming when conversion rate is below the bottom quartile for its type, or when bounce rate increases more than 5% after popup deployment.

---

### Note on Cookie Consent Banners

Cookie consent banners (GDPR, CCPA) are not conversion optimization surfaces in the traditional sense — they are legal compliance tools. Do not apply popup CRO optimization logic to consent banners. Key compliance rules: consent must be freely given, specific, informed, and unambiguous. Pre-ticked boxes are not valid consent under GDPR. Reject All must be as easy to click as Accept All. Optimize these for compliance and accessibility, not conversion rate.
