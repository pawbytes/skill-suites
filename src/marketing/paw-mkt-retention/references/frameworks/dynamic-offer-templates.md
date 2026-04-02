# Dynamic Offer Templates by Cancellation Reason

> Production-ready offer copy matched to each exit survey cancellation reason.
> All copy uses `[Brand]`, `[Product]`, `[Name]`, and `[Plan]` as placeholders.
> Adapt tone, voice, and specifics to match brand-context.md before using.

---

## Offer Screen Wrapper Copy

**Header above the offer card** (after survey selection):
- "Wait -- before you go, we have something for you."
- "Based on what you told us, here's what we can do."
- "We'd like to make this right."

**Decline link below offer** (always present):
- "No thanks, I still want to cancel" (styled as plain text link, not a button)

---

## Scenario 1: "It's too expensive"

**Offer type**: Discount (20-30% for 3 months) or Plan Downgrade

**Offer card headline options:**
- "Stay for [X]% less for the next 3 months"
- "We can reduce your bill by [X]% right now"
- "What if [Product] cost less?"

**Offer card body copy:**
```
We get it -- budget matters.

Here's what we can do: drop your [Plan] price by [X]% for the
next 3 months, then return to your regular rate.

No changes to your plan. No hidden conditions. Just a lower bill
while you see the full value [Product] can deliver.

[Apply [X]% Discount -- Keep My Account]
```

**Downgrade alternative (below the main offer):**
"Or, would a smaller plan at $[price]/month work better? [See all plans]"

**Pause alternative (below the main offer):**
"Not ready to commit? [Pause your account for 1-3 months] instead of cancelling."

**Acceptance confirmation copy:**
"Done. Your new rate of $[price]/month applies immediately. Your next invoice will reflect this discount. See you on the inside."

---

## Scenario 2: "Not using it enough"

**Offer type**: Free 1:1 onboarding session + Pause option

**Offer card headline options:**
- "Let's get [Product] actually working for you -- on us"
- "30 minutes with our team could change everything"
- "You're not stuck. We can help."

**Offer card body copy:**
```
Not using [Product] enough usually means one thing: you haven't
found your "aha moment" yet. That's on us.

Our team will personally walk through your account, understand
your specific goal, and set up [Product] to get you results --
for free, in one 30-minute session.

Customers who complete a setup session retain 3x longer and see
results within their first week.

[Book My Free Setup Session]
```

**Pause alternative:**
```
Not ready for a call right now?

Pause your account for up to 3 months instead. Your data stays
safe, your plan stays active, and you can unpause any time.
No charge while paused.

[Pause My Account Instead]
```

**Acceptance confirmation (session booked):**
"Your setup session is confirmed. You'll receive a calendar invite shortly. We're looking forward to helping you get real results from [Product]."

**Acceptance confirmation (pause selected):**
"Your account is paused. We won't charge you while you're paused. Resume any time from your account settings -- your data will be right where you left it."

---

## Scenario 3: "Missing a feature I need"

**Offer type**: Roadmap acknowledgment + Workaround + Pause

**Offer card headline options:**
- "Tell us what you need -- it matters"
- "That feature might be closer than you think"
- "We're building it. Here's where we are."

**Offer card body copy (roadmap version -- use when feature is planned):**
```
We hear you -- [feature] is something our team is actively
working on.

Current status: [On roadmap / In development / Launching in Q{X}]

If you can wait, we'd love to keep your account active. In the
meantime, here's a workaround that some customers use to
approximate [feature]: [brief workaround description or link].

Would a 2-month pause give us time to ship this for you?

[Pause My Account for 2 Months]    [View the Roadmap]
```

**Offer card body copy (feature not yet planned -- honest version):**
```
We don't have [feature] yet, and we want to be honest with you.

Your feedback has been sent directly to our product team. Features
that reach a certain threshold of requests get prioritised. Yours
counts.

If you want to stay and be notified the moment this ships,
we'll email you immediately. Otherwise, we understand.

[Stay and Notify Me When It Ships]
```

**Acceptance confirmation:**
"You've been added to the notify list for [feature]. We'll email you the moment it's available. Thank you for your patience -- feedback like yours shapes our roadmap."

---

## Scenario 4: "Switching to another tool"

**Offer type**: Direct comparison + Differentiation + 1-month free trial extension

**Offer card headline options:**
- "Before you switch -- a quick comparison"
- "We'd like the chance to show you what makes [Product] different"
- "Switching costs are real. Let's make sure it's worth it."

**Offer card body copy:**
```
Switching tools is a significant decision -- time, migration,
retraining, and integration work.

Before you go, here's how [Product] compares to the most common
alternatives our customers consider:

[Product]               vs    [Competitor A]
  [Differentiator 1]            [Gap or tradeoff]
  [Differentiator 2]            [Gap or tradeoff]
  [Differentiator 3]            [Gap or tradeoff]

If you've already decided, we respect that. But if you're still
evaluating, take one more month on us -- free -- to compare
fairly.

[Try 1 More Month Free]    [Read Full Comparison]
```

**Acceptance confirmation:**
"Your account has been extended by one month at no charge. We hope the extra time helps you make the best decision for your team -- whatever that turns out to be."

---

## Scenario 5: "I had a technical problem"

**Offer type**: Immediate escalation to senior support + Account credit

**Offer card headline options:**
- "Let us fix this -- right now"
- "This should never have happened. We want to make it right."
- "Our senior team will personally resolve this today"

**Offer card body copy:**
```
A technical problem is the worst reason to lose you as a
customer -- because it's fixable.

Here's what happens next:

1. A senior member of our engineering team will review your
   account within 2 hours.
2. We'll contact you directly at [email] with a resolution.
3. Your account will be credited for [X days/amount] for the
   disruption.

You don't need to do anything except give us the chance to fix it.

[Yes, Please Fix This]
```

**Immediate action on acceptance:**
Trigger internal alert to CS/engineering immediately. Do not route through standard support queue. Personal response within 2 hours is the expectation set.

**Acceptance confirmation:**
"Our senior team has been notified and will reach out within 2 hours. In the meantime, we've applied a [X]-day credit to your account. We're sorry this happened."

---

## Scenario 6: "Something else" (open text)

**Offer type**: Manager callback + General discount or pause option

**Offer card headline options:**
- "Can we call you? We'd like to understand."
- "Let's talk -- your situation is unique"
- "A real conversation might help"

**Offer card body copy:**
```
Not everything fits into a list. Whatever's going on, we'd like
to understand before you go.

If you're open to it, request a quick call with one of our
senior team members -- someone with the authority to actually
help, not just read from a script.

If a call doesn't work, we can also offer you a [X]% discount
or a [1-3 month] pause while you sort things out.

[Request a Quick Call]    [Get [X]% Off Instead]    [Pause Instead]
```
