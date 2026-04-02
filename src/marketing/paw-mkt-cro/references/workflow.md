# CRO Workflow

This reference defines the standard workflow, priority framework, diagnostic questions, output format, and testing methodology that applies to all CRO domains.

---

## Universal CRO Priority Framework

Apply this priority framework to every page or flow, regardless of domain. Work through each level before moving to the next — a weak value proposition cannot be fixed by a better CTA button color.

### Priority 1: Value Proposition Clarity

The most common reason pages fail to convert. Can a first-time visitor understand what this product does, who it is for, and why it matters — in under 5 seconds?

- Write the headline for the most skeptical version of your ideal customer.
- The value prop must be specific, not generic. "Save time" is weak. "Cut reporting time from 4 hours to 20 minutes" is strong.
- Eliminate insider language, acronyms, and feature-first copy that assumes context visitors do not have.
- The visitor's first question is always "Is this for me?" — answer it in the headline or subheadline.

### Priority 2: Headline Effectiveness

- Does the headline lead with the outcome the customer cares about, not the mechanism?
- Is there a specific number, timeframe, or comparison that makes the claim concrete?
- Does it speak directly to the primary traffic source persona (cold traffic needs more context; retargeting can be more direct)?
- Failing headline test: reads like a company tagline. Passing: reads like what a customer would say after using the product.

### Priority 3: CTA Placement and Copy

- Default to one primary CTA above the fold -- multiple CTAs split attention and reduce clarity. Exception: comparison or pricing pages where multiple plans each need their own CTA.
- CTA copy should describe what happens next ("Start My Free Trial") not what the user does ("Click Here").
- Button contrast: the primary CTA button should be the most visually distinct element on the page.
- Repeat the CTA at every natural decision point — after the value prop, after social proof, after objection handling, at the bottom.
- Remove competing CTAs that split attention (secondary links, navigation items, social icons near the primary CTA).

### Priority 4: Visual Hierarchy

- Scanners (80% of visitors) must be able to extract the core message from headlines, subheadlines, and bullet points alone — without reading a single paragraph.
- F-pattern reading: front-load the most important words in every headline and bullet.
- Whitespace is a conversion tool. Crowded pages create cognitive overload.
- Hero image or video must reinforce the value prop — if it does not add context, it reduces conversion.
- Font size hierarchy: H1 -> H2 -> body should be visually distinct (minimum 4-6px step-down).

### Priority 5: Trust Signals

- Customer logos (recognizable brands from the target audience's world).
- Testimonials must have: real name, photo, company, and a specific outcome — not generic praise.
- Review counts with star ratings (G2, Capterra, Trustpilot, App Store rating — choose the platform most credible to your audience).
- Security badges near forms and payment fields (SSL, SOC 2, GDPR, payment processor logos).
- Usage numbers ("10,000+ teams" or "2.3M reports generated") only when the numbers are meaningful and verifiable.

### Priority 6: Objection Handling

- List the top 5 objections from customer interviews, support tickets, and sales call notes. Then check: does the page address all 5?
- Price objection: money-back guarantee, free trial, "cancel anytime," or pricing transparency.
- Risk objection: case studies with similar company profiles, named customer logos in the same industry.
- Effort objection: "Up and running in 5 minutes," setup guide, onboarding support promise.
- Relevance objection: use-case segmentation ("Built for [role]" sections), industry-specific testimonials.
- FAQ section: address objections as questions, not as features. "Will this work for a team of 3?" not "Team Features."

### Priority 7: Friction Points

- Form fields: audit every field. Remove anything that does not directly serve conversion.
- Navigation: hide or remove site navigation from standalone landing pages. Navigation is an escape hatch.
- Mobile: test on a real device. Zoom-required text, mis-sized tap targets, and hidden CTAs are conversion killers.
- Load time: every 1-second delay costs approximately 7% in conversion rate. Target under 3 seconds on mobile.
- Decision fatigue: too many plan options, too many testimonials stacked without structure, walls of text.

---

## Diagnostic Questions

Ask these before producing any CRO recommendation. Recommendations without this data are guesses.

1. **Current state**: What is the current conversion rate? What is the goal conversion rate? How is it being measured?
2. **Traffic**: What are the primary traffic sources (paid search, organic, email, direct)? What is the monthly visitor volume on this page or flow?
3. **Drop-off data**: Where do users drop off? (Funnel analytics, heatmaps, session recordings, form analytics.) What tool is in place?
4. **Test history**: What has already been tested? What worked? What did not? (Avoid re-testing known losers.)
5. **Platform and constraints**: What platform or CMS is the page built on? What changes can be made without a developer? What requires engineering time?
6. **Audience context**: Are visitors arriving cold (first visit) or warm (retargeting, email)? What do they already know about the product?
7. **Business constraint**: Is the conversion goal a lead, a trial signup, a purchase, or something else? What happens immediately after conversion?

If the user cannot answer questions 1-3, recommend installing analytics and heat mapping before running tests. CRO without measurement is renovation without blueprints.

---

## Research Before Recommendations

Strong CRO recommendations come from understanding actual user behavior, not from applying a checklist.

### Quantitative data sources (what users do):

- **Funnel analytics**: Google Analytics 4 or Mixpanel funnel reports — where does the funnel lose the most volume?
- **Heatmaps**: Hotjar, Microsoft Clarity (free), or FullStory — where do users click, scroll, and ignore?
- **Form analytics**: Hotjar forms or Funnellytics — which fields cause abandonment? Which fields take longest to fill?
- **Session recordings**: Watch 20-50 sessions of users who did NOT convert. Look for confusion patterns, rage clicks, and abandonment moments.
- **A/B test results**: Check prior test history before recommending anything. Avoid re-testing confirmed losers unless the audience, offer, or context has changed significantly enough to invalidate the prior result.

### Qualitative data sources (why users do it):

- **Post-signup surveys**: "What almost stopped you from signing up?" (Typeform or in-product survey, ask 3-7 days after signup to engaged users.)
- **Exit-intent survey**: "What stopped you from signing up today?" — one question, 4 multiple-choice answers the team has hypothesized, plus an "other" free text.
- **Support ticket analysis**: Common questions and objections are a CRO research goldmine.
- **Sales call recordings**: What objections does the sales team handle on every call?
- **User interviews**: 5-7 conversations with recently converted users reveal the real decision-making journey.

### When to use which:

- Start with heatmaps and funnel analytics to identify WHERE the problem is.
- Use session recordings and surveys to understand WHY it is happening.
- Use that understanding to write better A/B test hypotheses.

---

## Output Format

Every CRO audit or recommendation must be structured in this format. Do not deviate.

### Quick Wins (same-day, no developer required)

Changes that can be made in the CMS, landing page builder, or no-code tool without engineering involvement. Headline rewrites, CTA copy changes, trust signal additions, removing distracting elements, adding FAQ items. Ship these immediately.

### High-Impact Changes (1-5 day effort, significant lift expected)

Changes that require design or developer involvement but have strong evidence of impact. New page section, redesigned hero, form field reduction, social proof overhaul, mobile experience fix. Prioritize by expected impact vs. implementation effort (use an ICE score: Impact, Confidence, Ease — 1-10 each).

### Test Hypotheses (A/B test candidates)

For each test hypothesis, provide:
- **Hypothesis**: "If we [change X], then [metric Y] will improve because [user behavior reason Z]."
- **Primary metric**: The single number that determines the winner.
- **Secondary metrics**: Guard rails (e.g., "signup rate should not drop while we test headline").
- **Minimum sample size**: See A/B Testing Primer section for calculation guidance.
- **Expected duration**: Based on current traffic volume.

### Copy Alternatives

Provide 2-3 variants for headlines, subheadlines, or CTAs — with a brief rationale for each variant's approach (outcome-focused, social proof angle, urgency angle, etc.). Always explain the strategic reasoning, not just the copy.

---

## A/B Testing Primer

### When to run an A/B test vs. just ship the change

- **Just ship it**: The current version is clearly broken (missing CTA, illegible on mobile, wrong headline). No need to test obvious fixes.
- **Run an A/B test**: The change is a hypothesis with uncertain outcome, the page has sufficient traffic, and the current version is performing reasonably.

### Minimum sample size

Rule of thumb: 1,000 conversions per variant minimum for 95% statistical confidence on a 5% relative lift. For lower-traffic pages, use a larger relative lift expectation or run tests longer.

Calculate with a sample size calculator (Evan Miller's is the standard). Inputs: current conversion rate, minimum detectable effect (the smallest lift you care about), confidence level (95% standard), and statistical power (80% minimum).

| Current CVR | Min detectable lift | Visitors needed per variant |
|---|---|---|
| 1% | 20% relative | ~47,000 |
| 3% | 15% relative | ~12,000 |
| 5% | 10% relative | ~15,000 |
| 10% | 10% relative | ~7,500 |

Low-traffic pages (under 500 conversions/month) should not run A/B tests. Use qualitative methods to generate high-confidence hypotheses, then ship the best variant and measure uplift over 30-60 days via before/after comparison.

### Test priority order (highest to lowest expected impact)

1. Value proposition / headline (largest potential swing)
2. CTA copy and placement
3. Form length (removing fields)
4. Social proof type and placement
5. Pricing page structure and anchoring
6. Page layout and visual hierarchy
7. Button color, size, shape (smallest impact — test last)

### Testing hygiene

- One change per test variant. Multi-variate requires dramatically more traffic.
- Run tests for a minimum of 2 business cycles (typically 2 weeks minimum) to account for day-of-week variation.
- Do not stop tests early because one variant looks like a winner — regression to the mean is real.
- Document every test: hypothesis, date range, traffic split, results, confidence level, and decision made.

---

## CRO by Traffic Source

The same page can need completely different optimization depending on where visitors are arriving from. Design and copy for the coldest, least-informed traffic source hitting that URL.

### Cold traffic (paid social, display, broad paid search)

- Visitors have no prior awareness of the brand.
- Must establish credibility and context immediately.
- Longer pages perform better — more space to build trust and address objections.
- Social proof must include recognizable reference points (logos, industries, role titles).
- Headline: lead with the pain or problem, not the solution name.

### Warm traffic (retargeting, branded search, email list)

- Visitors have seen the brand at least once.
- Skip the basic explanation — get to the compelling offer faster.
- Shorter, more direct pages often outperform.
- Headline can reference their prior action ("Still thinking about [product name]?").
- Stronger urgency or specific incentive (limited-time offer, bonus content) can close the gap.

### High-intent traffic (competitor keyword search, review site referrals, pricing page direct)

- Visitors are actively evaluating — they are in buy mode.
- Comparison content, guarantee language, and risk reduction are highest priority.
- Minimize steps between landing and conversion. Remove all friction.
- Live chat or demo booking CTAs can dramatically improve conversion at this stage.

### Referral and partner traffic

- Visitors arrive with context from the referring source. Leverage it.
- Custom landing pages per referral source outperform generic pages by 20-40%.
- Match the message to the referring context ("Welcome, [Partner Name] customers").

---

## Ethics: Persuasion Without Manipulation

CRO relies on psychological techniques—urgency, social proof, loss framing, friction reduction. These tools are powerful and can be misused. This section defines the ethical line.

### Ethical CRO Practices

Ethical optimization helps visitors make decisions that align with their genuine interests. The converted customer should be glad they converted.

- **Genuine urgency**: Time-limited offers actually expire. "2 spots left" means two spots. Countdowns do not reset.
- **Real social proof**: Testimonials from actual customers with verifiable outcomes. Customer counts are accurate.
- **Honest friction reduction**: Removing obstacles to help users do something that benefits them—streamlining signup, clarifying value, reducing cognitive load.
- **Transparent pricing**: No hidden fees revealed only at checkout. Trial terms are clear before the user enters payment info.
- **Clear CTA language**: The button describes what actually happens next. "Start Free Trial" starts a free trial—not a hidden paid subscription.

### Dark Patterns to Avoid

| Pattern | Description | Why It Harms |
|---|---|---|
| Fake scarcity | Countdown timers that reset; inventory numbers fabricated | Destroys trust when discovered; FTC enforcement risk |
| Hidden fees | Price revealed after form submission or at final step | Chargebacks, churn, regulatory risk |
| Forced continuity | Free trial auto-converts to paid without clear disclosure | Negative reviews, chargebacks, legal exposure |
| Roach motel | Easy to sign up, deliberately difficult to cancel | Social media backlash, churn anger |
| Confirmshaming | "No thanks, I don't want more customers" opt-out labels | Creates resentment, not conversion |
| Misdirection | Visual design that hides the option the user actually wants | Short-term gain, long-term brand damage |
| Trick questions | Confusing language that tricks users into opting in | Trust destruction, potential legal liability |

### The Long-Term Case for Ethics

Dark patterns convert in the short term and destroy brands in the long term. The user who feels manipulated:
- Churns at the first opportunity
- Leaves negative reviews
- Warns others
- Never refers

The user who feels well-served:
- Retains and expands
- Reviews positively
- Refers others
- Becomes an advocate

Before implementing any CRO technique, ask: **If the customer understood exactly what was happening, would they still feel well-served?** If the answer is no, do not implement it.

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** — working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/cro/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** — evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/cro/`

**Legacy fallback** — old directory structure detected:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/cro/`
  -> Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All CRO work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Page Audit | `audit-{page-name}-{YYYY-MM-DD}.md` | Current state, screenshots, CRO priority framework assessment, Quick Wins, High-Impact Changes, Test Hypotheses, Copy Alternatives |
| A/B Test Brief | `test-brief-{hypothesis-slug}-{YYYY-MM-DD}.md` | Hypothesis, variants (with copy/design specs), primary metric, secondary metrics, sample size, duration, success criteria |
| Signup Flow Audit | `audit-signup-{YYYY-MM-DD}.md` | Field audit, step analysis, friction map, Quick Wins, test plan |
| Onboarding Audit | `audit-onboarding-{YYYY-MM-DD}.md` | Activation metric, step analysis, empty state review, email sequence alignment, retention correlation findings |
| CRO Roadmap | `cro-roadmap-{YYYY-MM-DD}.md` | Prioritized backlog (ICE scored), test calendar, estimated lift per initiative, owner and timeline |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/cro/
  audit-{page-name}-{YYYY-MM-DD}.md
  audit-signup-{YYYY-MM-DD}.md
  audit-onboarding-{YYYY-MM-DD}.md
  test-brief-{hypothesis-slug}-{YYYY-MM-DD}.md
  cro-roadmap-{YYYY-MM-DD}.md
  screenshots/

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/cro/
  (same structure as above)
```

---

## Response Protocol

When the user requests CRO work:

1. **Route the starting context** (see `./references/shared-patterns.md` for Starting Context Router). Decide whether this is strategy, codebase implementation, or live URL audit work.
2. **Read the strongest available context** (Pre-Flight): brand and SOSTAC first when available; otherwise use the existing codebase or live page.
3. **Identify the CRO domain**. Read the appropriate domain reference file before producing recommendations:
   - Landing page -> `./references/page-cro.md`
   - Signup flow -> `./references/signup-cro.md`
   - Onboarding -> `./references/onboarding-cro.md`
   - Forms -> `./references/form-cro.md`
   - Popups -> `./references/popup-cro.md`
   - Paywalls -> `./references/paywall-cro.md`
4. **Ask the diagnostic questions** if the user has not already provided this information. Do not produce recommendations without knowing current CVR and traffic source unless the task is explicitly a first-pass audit.
5. **Research the page or implementation**: use agent-browser for live URLs; inspect current flow, components, instrumentation, and constraints for codebase work.
6. **Apply the universal priority framework**. Start with value proposition, not button colors.
7. **Deliver structured output**. Quick Wins first, then High-Impact, then Test Hypotheses, then Copy Alternatives.
8. **Save deliverables** to the resolved path (see Path Resolution).
9. **Recommend next steps**: What to ship immediately, what to test, when to review results.

### When to escalate

- Significant UX redesign or new page build -- recommend involving a designer and developer; CRO brief can define the conversion requirements.
- Paid traffic strategy (the ads sending traffic to the page) -- route to paw-mkt-paid-ads skill.
- Email nurture for leads captured via forms -- route to paw-mkt-email skill.
- SEO implications of page changes (meta, structure, content) -- route to paw-mkt-seo skill.
- Brand messaging or positioning questions that surface during CRO audit -- route to paw-mkt-product-context or brand-context update.