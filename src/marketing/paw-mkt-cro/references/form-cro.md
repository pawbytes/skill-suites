# Form CRO Reference: Lead Gen Forms, Contact Forms, Demo Requests, Quote Forms

**Purpose:** Frameworks, copy templates, and test ideas for optimizing forms used to capture leads, book demos, request quotes, or initiate contact — specifically in a marketing context. Read this file when the user is optimizing a lead generation form, contact form, demo request form, or quote request form on a marketing page or landing page.

**Scope distinction from `signup-cro.md`:** This file covers forms that collect information from a prospect before they have an account — the handoff from marketing to sales, or the moment a visitor raises their hand. `signup-cro.md` covers account creation and trial activation forms where the user is becoming a user of the product. The psychology, field logic, and optimization strategies are materially different. Do not conflate them.

**What this file does NOT cover:** E-commerce checkout forms, payment forms, in-product account settings forms, or survey forms. Those have distinct optimization logic.

---

## 1. Field Audit Protocol

### The Core Question for Every Field

Before auditing a form, internalize this: every field you ask for is a tax on the visitor's willingness to convert. The burden of proof is on keeping a field, not on removing it.

For every field on the form, ask:
1. **What do we do with this data?** If it goes into a CRM field that no one looks at, delete the field.
2. **Does this data change what happens next?** If the routing, qualification, or follow-up is identical regardless of the answer, the field has no functional value.
3. **Does asking this question cost us more conversions than the data is worth?** A phone number field reduces form completions by 5-30%. If your sales team needs phone for follow-up, quantify: how many more leads do you generate without phone, and what % of those you could still close via email first?
4. **Can this be collected after the conversion, not before it?** If the data is for personalization or segmentation, it can be collected on the thank-you page, in a follow-up email, or by the sales rep on the first call.
5. **Can this be inferred?** Company name from email domain. Country from IP. Company size from LinkedIn enrichment (Clearbit, Apollo, 6sense). If it can be inferred with >80% accuracy, do not ask it.

### Field Necessity Classification

| Classification | Decision |
|---|---|
| Required for routing/qualification and cannot be inferred | Keep, make required |
| Required for follow-up and cannot be obtained post-conversion | Keep, but evaluate if required or optional |
| Useful for segmentation but not required | Make optional, or move to thank-you page survey |
| Enrichable from email/IP | Remove from form, enrich programmatically |
| "Nice to have" for marketing analytics | Remove. Not worth the conversion cost. |
| Asked because "sales likes to know" | Challenge it. If sales closes deals without it in the first call, it is not needed on the form. |

### Standard Lead Gen Form: Field Audit Starting Point

| Field | Default recommendation | Exception |
|---|---|---|
| First name | Keep | — |
| Last name | Keep | Can be combined into single "Full name" field to reduce perceived length |
| Work email | Keep, make required | Personal email ok for SMB/consumer; work email for enterprise qualification |
| Phone number | Remove unless required for routing | Keep if sales team requires for initial outreach and volume justifies the conversion cost |
| Company name | Keep for B2B | Can often be inferred from email domain; make optional if auto-fill is available |
| Job title | Remove unless used for qualification routing | Keep if it determines which SDR or product the lead is routed to |
| Company size | Remove unless gates access to a tier | Use post-conversion survey or data enrichment |
| Industry | Remove unless determines product fit | Same as above |
| How did you hear about us? | Remove from lead form | This is an analytics question, not a sales question. Collect via UTM parameters instead. |
| Message / describe your needs | Remove from high-volume lead forms | Keep for contact forms and enterprise/custom quote forms where context is needed for a meaningful response |
| Country | Remove unless routing to regional teams | Use IP geolocation if needed for routing |

### Minimum Viable Form by Form Type

| Form type | Minimum viable fields |
|---|---|
| Content download / gated asset | Email only (or first name + email) |
| Newsletter signup | Email only |
| Demo request (self-serve, low-touch) | First name + email (+ optional: company) |
| Demo request (enterprise, high-touch) | First name + last name + work email + company name |
| Contact / general inquiry | Name + email + message |
| Quote request | Name + email + message describing scope (minimum); company + phone optional |
| Event registration | Name + email; additional fields only if operationally required for the event |

---

## 2. Field Type Optimization

### Text Input Fields

Use a standard single-line text input for: name, email, company name, job title, city.

Best practices:
- Use the correct `type` attribute: `type="email"` triggers email keyboard on mobile and enables browser-level format validation. `type="tel"` triggers numeric keyboard for phone. `type="text"` for everything else.
- Enable autocomplete. The `autocomplete` attribute (e.g., `autocomplete="email"`, `autocomplete="name"`) allows browsers and password managers to pre-fill. This meaningfully reduces effort on mobile.
- Single-field name entry ("Full name") reduces visual length but can cause issues with personalization tokens. If your email system merges first name separately, keep two fields — or parse the full name field programmatically.
- For email: inline format validation on blur (not on every keystroke). Green checkmark for valid. Red error message for invalid. Do not wait until form submission to surface this error.

### Dropdowns

Use dropdowns when:
- There are 5+ options that would be unwieldy as radio buttons
- The options are well-known and standardized (country list, industry list, company size band)
- You want to control input values precisely (no free-text variation in your CRM)

Avoid dropdowns when:
- There are 4 or fewer options (use radio buttons — they are faster to parse)
- The options require scrolling through a long list on mobile (a searchable select or typeahead is better)
- The user needs to see all options at a glance to make a decision (radio buttons show everything immediately)

Dropdown optimization:
- Default to an empty state ("Select your industry") not the first option in the list. Pre-selecting the first option leads to people not noticing the field and submitting incorrect data.
- Put the most common selections first, not alphabetically ordered. If 60% of leads are from "Software / Technology," put it at the top.
- For long country lists: detect country from IP and pre-select it. The user can change it if wrong. This removes the most laborious dropdown interaction from the form.

### Radio Buttons and Checkboxes

Use radio buttons when:
- There are 2-4 mutually exclusive options
- You want the user to consciously choose one option (vs. overlooking a dropdown default)
- The option selection provides qualification information that changes routing

Use checkboxes when:
- Multiple selections are valid (interested in: [Product A] [Product B] [Product C])
- A single consent or confirmation is needed ("I agree to the privacy policy")

Radio button and checkbox optimization:
- Make the click/tap target the entire label text, not just the button itself. Label should be wrapped in a `<label for="...">` element linked to the input ID.
- Pre-select the most common option for radio buttons where there is a strong default (e.g., "Company size: [1-10] [11-50] [51-250] [250+]" — pre-select based on IP/domain data if available).
- Do not use checkboxes for consent where the legal requirement is an active opt-in. A pre-checked consent checkbox is not valid consent under GDPR and similar regulations.

### Message / Textarea Fields

For contact forms and quote forms where a message field is appropriate:
- Label it specifically: "Describe your project" or "What would you like to discuss?" rather than "Message."
- Set a visible character minimum (e.g., "Please describe in at least 20 characters") only if you genuinely need context — this filters out low-effort submissions.
- Set a rows attribute that shows approximately 3-4 lines of text. Too small feels cramped; too large feels intimidating.
- Do not use a message field as a generic catch-all. If you have specific questions you want answered, ask them as structured fields. An open text field invites irrelevant responses and makes CRM enrichment impossible.

---

## 3. Form Layout Principles

### Single Column vs. Multi-Column

**Default: single column.**

Single-column forms are faster to complete and have higher completion rates. Eye-tracking research consistently shows that multi-column layouts cause users to scan horizontally, miss fields, and make submission errors.

**Acceptable multi-column use cases:**
- Side-by-side name fields (First name | Last name) when both are collected — this is a natural pair users expect to see together
- Short qualifier pairs (Company name | Job title) on a high-intent form where skimmers are not a concern
- Desktop-only forms for a technical audience comfortable with dense layouts (developer tools, financial products)

**Never multi-column:**
- Any form on mobile (or a form without a responsive layout that collapses to single-column on mobile)
- Forms with 3+ columns at any width
- Email and password fields (always single column, always full width)

### Label Placement

**Top-aligned labels (above the field) are the fastest to complete** and the recommended default for all form types. Eye tracking studies show top-aligned labels minimize eye movement and allow users to fill forms faster than left-aligned (side) labels.

Left-aligned labels (next to the field) should be used only when vertical space is the primary constraint and the form has fewer than 5 fields. On mobile, always use top-aligned labels.

**Placeholder text as labels is an anti-pattern.** Do not use the placeholder attribute as the sole label for a field. Once the user begins typing, the label disappears, and users must clear the field to remember what was being asked. Use placeholder text for format hints only ("john@company.com" or "e.g., 10-50 employees").

### Field Ordering

Order fields to reduce psychological friction:
1. **Start with the easiest fields** (name fields are faster to fill than company size or message fields). Build momentum.
2. **Put high-friction fields later.** Phone number, message field, and any field the user might hesitate on should come after the easy wins.
3. **Email last vs. email first:** Testing shows mixed results. Test your audience. The conventional wisdom is email first (so partial completions capture the email even if the user abandons). The counter-argument is email last reduces bounce when users see email and assume spam before experiencing the form's value.
4. **Group related fields.** If you have first name, last name, and email — group them as personal information. If you have company name and job title — group them as company information. Logical grouping reduces cognitive overhead.

### Form Width and Sizing

- Full-width input fields (100% of form container width) outperform short-width fields on mobile.
- On desktop, a form container of 480-600px is optimal. Wider than 600px makes fields feel over-sized; narrower than 400px feels cramped on desktop.
- Input field height: minimum 44px touch target on mobile. 40-48px is the standard range. Fields smaller than 40px cause tap errors on mobile.
- Submit button: full-width on mobile. On desktop, can match the width of the form container or be a natural CTA button width (200-300px).

---

## 4. Multi-Step Forms

### When to Use a Multi-Step Form

Multi-step forms are appropriate when:
- The total number of fields exceeds 6-7, and a single-page form would appear overwhelming
- There is a logical grouping of questions that represents a conceptual step (personal info → company info → project details)
- The form's conversion rate is poor and evidence suggests field count is the primary barrier
- The form qualifies leads (early steps identify qualification criteria; later steps collect enrichment data only for qualified leads)

Multi-step forms typically increase form start rate (by hiding the full complexity) but may reduce completion rate if the later steps are perceived as too burdensome. The net effect on leads delivered depends heavily on implementation.

### How to Structure Steps

**Step 1: The commitment step.** First step should be the easiest fields (usually name and email). The psychological commitment effect: once a user completes step 1, they are significantly more likely to complete subsequent steps. Capture email in step 1 so partial completions are recoverable via follow-up automation.

**Step 2: Qualification fields.** Fields that determine whether this lead is worth routing to sales, and if so, to which team or rep. Company size, role, use case. These can be radio buttons or dropdowns for fast completion.

**Step 3: Context or enrichment.** Phone number (if required), message/project description, timeline. The hardest fields go last, after commitment is established.

**Step 3 alternative: Do not have a step 3.** If you can capture the qualification you need in two steps, stop at two. Every additional step is a drop-off point.

### Progress Indicators on Multi-Step Forms

- Always show a progress indicator. "Step 1 of 3" or a progress bar. Users who cannot see how far they have to go are more likely to abandon.
- "Step X of Y" (numbered) outperforms percentage bars for most audiences because steps feel more concrete than percentages.
- Back button: always include. Users who cannot go back to correct an error will often abandon rather than resubmit.
- Never show "Step 1 of 7." If your form has 7 steps, restructure it. Maximum of 3-4 steps is the practical limit for acceptable completion rates.

### Conditional Logic

Conditional logic (showing or hiding fields based on earlier answers) is one of the highest-impact improvements available on multi-step forms:

- If "Company size" = 1-10, skip the "How many licenses do you need?" field
- If "Role" = Individual Contributor, skip the "Team budget" question
- If "Country" = United States, show state/region field; otherwise skip it
- If "I have a specific question" = selected, show message field; otherwise hide it

Conditional logic reduces form length for most users while preserving data collection from users for whom it is relevant. It requires a form platform that supports logic (Typeform, HubSpot forms, Webflow forms with custom JS, or a custom implementation).

---

## 5. Microcopy

### Placeholder Text

Placeholder text appears inside the field before the user starts typing. It is for format hints and examples — not labels.

Good placeholder use:
- Email: `work@company.com`
- Phone: `+1 (555) 000-0000`
- Company: `Acme Corporation`
- Message: `Briefly describe your project or question...`

Bad placeholder use:
- Using the placeholder as the only label (anti-pattern as described above)
- Long instructional text that disappears when the user starts typing ("Please enter your full legal business name as it appears on your registration documents" — no)
- Filler text like "Type here" or "Enter your answer"

### Helper Text

Helper text appears below the field label (not inside the field) and is permanently visible. Use it when:
- The field has a specific format requirement ("Must be a work email — we'll send your access link here")
- The field has a privacy concern that needs preemptive addressing ("We'll only use this to send your report. No spam.")
- The field requires context to answer correctly ("Your current monthly ad spend, not including agency fees")

Helper text should be short (under 15 words) and positioned immediately below the label, not below the input field (where it may be obscured by autofill dropdown).

### Error Messages

Error messages are the highest-friction microcopy moment on any form. Poor error messages are a measurable conversion killer.

**Error message principles:**
1. Be specific about what went wrong. "Email is invalid" is not specific. "Please use a work email address (we can't send access links to Gmail or Hotmail)" is specific.
2. Tell the user how to fix it. "Phone number must include country code (e.g., +1 for US)" tells the user exactly what to do next.
3. Show the error inline, next to the field, not in a banner at the top of the form. The user should not have to hunt for where the problem is.
4. Use red for error states (widely understood convention) but accompany it with text — do not rely on color alone (accessibility).
5. Trigger validation on blur (when user leaves the field), not on submit. On-submit validation requires the user to scroll back up and find errors. On-blur validation catches problems immediately.
6. Never say "Invalid input." Tell them what valid input looks like.

**Error copy examples:**

| Bad error message | Better error message |
|---|---|
| "This field is required." | "Please enter your first name so we know who to contact." |
| "Email is invalid." | "Please check your email — something looks off (try: name@company.com)." |
| "Phone number is invalid." | "Phone number should be 10 digits, like 5550001234 (no spaces or dashes needed)." |
| "Please complete all required fields." | (Highlight each unfilled required field individually with a specific message.) |

### Submit Button Copy

The submit button is the last microcopy touchpoint before conversion. "Submit" is the worst possible copy — it describes a technical action, not the value the user receives.

**Framework:** "Submit button copy = what the user gets immediately after clicking"

| Form type | Generic copy (avoid) | Better copy |
|---|---|---|
| Demo request | Submit / Book Demo | Get My Demo / Schedule Your Demo / Book a 30-Min Demo |
| Lead gen / content | Download / Submit | Download the Guide / Get Instant Access / Send Me the Report |
| Contact form | Send / Submit | Send My Message / Get in Touch |
| Quote request | Submit / Request | Get My Quote / Request a Custom Quote |
| Newsletter | Subscribe / Submit | Join the Newsletter / Get Weekly Updates |
| Webinar registration | Register / Submit | Save My Spot / Register for Free |

First-person button copy ("Get My Demo" vs. "Get Your Demo") has mixed test results — test both, but first-person phrasing tends to outperform in high-intent contexts.

---

## 6. Trust Signals on Forms

### What to Include

**Privacy statement:** A single sentence immediately below the submit button. Not a link to the full privacy policy — a plain-language statement. "We respect your privacy. No spam, ever." or "Your information is never sold or shared." This is the highest-impact single trust addition to any lead gen form.

**SSL indicator:** Most modern browsers show the lock icon in the address bar, but adding a "Secured by SSL" text or icon near the form submission area reinforces security for non-technical audiences. Relevant on landing pages embedded in iframes or on domains that might be less familiar.

**Social proof proximity:** A testimonial or customer logo strip placed immediately adjacent to the form (not above the fold — right next to the submit button area) catches the last-second hesitation before submission. The testimonial should be from someone matching the visitor's profile. A quote from a VP of Marketing converts better for marketing audiences than a quote from a CEO.

**Specific social proof numbers:** "Trusted by 4,200 marketing teams" or "Join 12,000 subscribers" adjacent to the form provides peer validation at the decision moment.

**Response time promise:** For demo and contact forms, a line stating "We'll respond within 1 business day" or "Expect a response within 2 hours on business days" reduces the uncertainty about what happens after submission. This reduces the "is anyone actually there?" hesitation.

### Where to Place Trust Signals

The optimal placement is the space immediately surrounding the submit button — the zone of highest attention at the conversion moment.

| Trust signal type | Optimal placement |
|---|---|
| Privacy statement | Directly below the submit button (within 8px) |
| Response time promise | Directly below the submit button or as a form header note |
| Customer logos | Directly below the form container or in the column adjacent to the form |
| Single testimonial | Adjacent to the form (sidebar) or directly below the form |
| Review badge (G2, etc.) | Adjacent to or below the form — not above it (above-fold placement is for page-level trust) |
| SSL badge | Near submit button or in form footer |

### What NOT to Include on a Form

- **Too many trust badges at once.** Three or more badges clustered together create visual noise and can paradoxically signal insecurity ("why does this page need to prove itself so hard?"). Pick the one most credible to your audience.
- **Full terms of service text.** Link to it, do not embed it. Visible walls of legal text near the CTA are associated with lower conversion rates.
- **Award badges from obscure organizations.** If the visitor does not recognize the awarding body, the badge is noise.
- **A privacy policy link as the only trust signal.** It implies "we are legally required to tell you this" rather than "we actually respect your privacy."
- **Testimonials that reference the company name rather than the product's specific benefit.** "Great company!" does nothing. "We cut our lead qualification time by 60% in the first month" does everything.
- **Fake urgency.** "Only 3 demo slots remaining this week" when slots are not actually limited. Visitors who notice it is false (and many do) lose all trust in the form and the brand.

---

## 7. Thank You Page Strategy

### Why Thank You Pages Are Massively Under-Optimized

The thank you page is shown to your highest-intent visitors — people who have already converted. Yet the overwhelming majority of thank you pages do one of two things: display a generic "Thanks, we'll be in touch" message, or redirect to the homepage.

Both are enormous missed opportunities. A visitor who has just filled out a demo request form is at peak interest. They have committed to a next step. The psychological state is: "I've decided. What else can I do while I'm here?"

The thank you page is the best moment to:
- Advance the relationship before the sales contact happens
- Gather additional qualification data when the visitor is in a cooperative mindset
- Drive secondary conversions (content consumption, social follow, community join)
- Set expectations that reduce no-show rates for scheduled demos

### Thank You Page Framework by Form Type

**After a demo request form:**
1. Confirmation: "Your demo request is confirmed. [Name] from our team will reach out within [timeframe]."
2. Expectation-setting: What to expect on the demo call. Duration, what will be covered, who will be on the call.
3. Qualification question: "While you wait, one quick question: What's your biggest challenge with [problem area]?" One question, 4 radio button answers. This data reaches the sales rep before the call and improves call quality. Completion rates on this single question are typically 40-70% because the visitor is already in a cooperative state.
4. Preparation resource: "To get the most from your demo, here's a 3-minute overview of [key feature area]." Link to a short video or product tour.
5. Calendar integration: If using a self-scheduling tool (Calendly, Chili Piper), embed or link the scheduling UI directly on the thank you page. Removing the scheduling step from the sales rep's follow-up task and giving the prospect immediate control reduces time-to-meeting significantly.

**After a content download / gated asset:**
1. Confirmation with direct access: "Your [report/guide] is ready. [Download it here]." Do not make them wait for an email if the asset can be served immediately.
2. Related content: 2-3 pieces of related content that extend the topic they just expressed interest in. Label them clearly. This is your highest-intent audience for content — use it.
3. CTA upgrade: "Interested in how [Product] helps you act on these insights? [Book a 15-minute conversation]." This is a soft next-step CTA for leads who expressed enough interest to fill out a form.

**After a contact form:**
1. Confirmation and timeline: "Message received. We'll reply to [email address] within [X hours/days]."
2. FAQ or self-serve resource: If the contact form submission frequently generates questions that could be answered by existing documentation or an FAQ page, link to it here. Reduces support volume for routine questions.
3. Social follow or community join: "While you wait, follow us on [platform] for [specific value — not 'updates' but 'weekly tactical marketing breakdowns']." This is the right moment to capture a social follow because the visitor has already demonstrated trust.

**After a quote request:**
1. Confirmation with realistic timeline: "Your quote request is in. Our team typically responds within [X] business days with a detailed proposal."
2. Relevant case study: "While we prepare your quote, see how we helped [similar client] achieve [specific outcome]." Pick the case study most closely matching the prospect's profile.
3. Pre-qualification survey (optional): "To help us prepare the most accurate quote, could you share [1-2 clarifying questions]?" If the quote form was minimal (to maximize submissions), this is the right place to collect additional context.

### Thank You Page Metrics to Track

- Time on thank you page (benchmark: >45 seconds indicates engagement with post-submission content)
- Click-through rate on the secondary CTA
- Survey completion rate (if a qualification question is included)
- Demo no-show rate correlation: pages with expectation-setting content typically show 10-20% lower no-show rates

---

## 8. A/B Test Ideas for Forms

For each hypothesis: the change is specific, the primary metric is the single number that determines the winner, and the rationale is based on a behavioral mechanism — not "best practice."

| # | Hypothesis | Change | Primary metric | Rationale |
|---|---|---|---|---|
| 1 | Removing the phone number field will increase form completions | Remove phone number field; collect via sales rep on first call | Form completion rate | Phone number is the single highest-friction field on most B2B forms. Cost in completions typically exceeds the operational value of the data pre-call. |
| 2 | First-person CTA copy will increase clicks | "Get My Demo" vs. "Get Your Demo" vs. "Book a Demo" | CTA click rate | First-person possessive copy creates stronger identity connection with the conversion action. Test all three. |
| 3 | A single social proof testimonial adjacent to the form will increase submissions | Add a 2-sentence customer quote with name, title, and company photo next to the submit button | Form submission rate | Social proof at the conversion point addresses last-second hesitation with evidence from a peer. |
| 4 | A multi-step form will have higher completion rate than a single-page form of equal field count | Split 6 fields across 2 steps (name + email first; company + role + inquiry type second) | Form completion rate | Hiding total form length reduces initial abandonment. The commitment effect from completing step 1 increases step 2 completion. |
| 5 | Inline error validation (on blur) will increase completions vs. on-submit error validation | Validate each field as the user leaves it vs. validating all fields on submit | Form completion rate (especially on mobile) | On-submit validation requires users to scroll and hunt for errors. On-blur validation catches and corrects problems at the moment they occur, before the user moves on. |
| 6 | A response time guarantee below the submit button will increase submissions | "Our team responds within 4 business hours" below the CTA button | Form submission rate | Uncertainty about what happens after submission is a documented barrier for contact and demo forms. Specific timeframe reduces this uncertainty. |
| 7 | Removing the form from a modal and embedding it directly on the page will increase completions | Inline form vs. click-to-open modal form | Total form completions from page (not completion rate of opened forms) | Modal forms have a two-step friction: click to open, then fill. Inline forms have one step. High-intent users are fine with modals; mid-intent users may not bother clicking. |
| 8 | A single conditional logic question replacing two unconditional questions will increase completions | Replace "Company size" + "Number of licenses" with conditional: show "Number of licenses" only if company size > 10 | Form completion rate | Reducing perceived form length for users for whom a field is irrelevant reduces abandonment without reducing data quality. |
| 9 | Short-form (3 fields) vs. long-form (7 fields) on a high-traffic top-of-funnel page | Name + email + inquiry type vs. name + email + company + role + size + inquiry + phone | Qualified leads per 1,000 visitors (not completion rate alone) | Short forms generate more completions; long forms generate fewer but more qualified leads. The question is which yields more pipeline per visitor, not just more submissions. |
| 10 | A thank you page with a self-scheduling CTA will reduce time-to-meeting vs. rep-scheduled follow-up | Add Calendly embed to demo request thank you page | Average hours from form submission to booked meeting | Immediate self-scheduling removes the back-and-forth email exchange and capitalizes on peak intent at the post-conversion moment. |

---

## 9. Benchmark Conversion Rates by Form Type

These benchmarks represent conversion rates from qualified page visits to form submission. They account for traffic quality variation and should be used as directional anchors, not precise targets. Your specific mix of traffic temperature, offer quality, and page context will determine where you land within each range.

### Lead Gen Forms

| Form type | Industry / Context | Typical conversion rate | Notes |
|---|---|---|---|
| Gated content (whitepaper, report) | B2B SaaS | 3-8% of page visitors | Rate heavily influenced by relevance of the offer to the audience |
| Gated content | B2B professional services | 2-5% | |
| Newsletter signup | B2B content sites | 1-3% | Inline form; popup forms typically 2-5x higher but inflate numbers with lower-intent subscribers |
| Newsletter signup (popup, exit-intent) | Content / media | 3-8% | High subscribe rate; expect lower open rates from popup-driven subscribers |
| Webinar registration | B2B SaaS | 10-25% of email-driven traffic; 2-6% of cold/paid traffic | Email-driven registrations dominate; cold traffic webinar CVR is low |

### Demo Request Forms

| Form type | Traffic source | Typical conversion rate | Notes |
|---|---|---|---|
| Demo request (dedicated landing page) | Paid search / brand | 5-15% | High-intent traffic; dedicated page with no nav outperforms embedded forms |
| Demo request (dedicated landing page) | Paid social / cold | 1-4% | Cold traffic needs significantly more trust-building before form |
| Demo request (embedded on pricing page) | Organic / direct | 3-8% | Pricing page visitors are high-intent; form placement on the page matters significantly |
| Demo request (embedded on homepage) | Mixed | 1-3% | Homepage traffic is mixed-intent; form competes with other CTAs |

### Contact Forms

| Form type | Typical conversion rate | Notes |
|---|---|---|
| General contact form | 1-3% of visitors reaching the contact page | "Contact us" pages are often visited by existing customers and job seekers, diluting conversion metrics |
| Sales inquiry contact form | 3-7% of qualified traffic | When the form is purpose-built for sales inquiries with clear context-setting |
| Support / help request | 10-25% of visitors reaching the support page | Higher intent — visitors to this page have a specific need and a high motivation to submit |

### Quote Request Forms

| Form type | Industry | Typical conversion rate | Notes |
|---|---|---|---|
| Instant quote (calculator-style) | Insurance, web hosting, SaaS | 5-20% | Real-time value delivery increases completion rate dramatically |
| Custom quote request (form to human review) | Agency, professional services | 2-6% of qualified page traffic | Lower CVR is acceptable because each lead has high average deal value |
| E-commerce shipping / bulk quote | B2B e-commerce | 3-8% | Conversion rate depends heavily on product catalog complexity |

### Conversion Rate Improvement Benchmarks

As directional targets for optimization efforts:

| Optimization lever | Typical conversion lift range |
|---|---|
| Removing one required field | 5-15% |
| Switching from "Submit" to specific CTA copy | 5-20% |
| Adding a privacy statement below submit button | 3-10% |
| Switching from multi-column to single-column layout | 5-15% (mobile especially) |
| Converting to a multi-step form (from single-page with 6+ fields) | 10-30% on start rate; net effect on completions varies |
| Adding a relevant testimonial adjacent to the form | 5-20% |
| Inline vs. on-submit error validation | 5-25% (highest impact on mobile) |
| A/B testing button copy with specific outcome language | 10-40% (highest variance; headline-level impact) |
