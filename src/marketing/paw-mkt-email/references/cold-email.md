# Cold and Outbound B2B Email

Cold email is distinct from lifecycle and newsletter email. Different rules apply.

## Cold Email Voice and Mindset

- **Write like a peer, not a marketer** - no ALL CAPS, no "exciting opportunity," no corporate enthusiasm
- **Lead with their world, not your product** - open with something true about prospect's situation
- **Ruthlessly short** - 5-9 sentences max. Every sentence must earn its place
- **One ask per email** - one clear, low-friction action

## Subject Lines and Structure

Subject lines: 2-4 words, lowercase (`quick question`, `{company} + {their company}`).
No clickbait, exclamation marks, or emojis.

```
Subject: {2-4 words, lowercase}

{Opening: one sentence grounded in their world}

{Body: 1-3 sentences - your value in their terms}

{CTA: one low-friction ask - "worth a quick chat?"}

{Name}
{Title, Company}
```

**Avoid**: long intros, feature lists, "I hope this email finds you well," links or attachments in email 1.

## CTA Friction Ladder

| Friction Level | Example CTA |
|---|---|
| Lowest | "Worth a quick chat?" |
| Medium | "Open to a 15-min call?" |
| Higher | "Can I send you a demo?" (only with established relevance) |

No calendar links in the first email.

## Follow-Up Sequence (3-5 emails)

Cold email rarely converts on email 1. Sequences work. Each follow-up needs a **fresh angle** - do not just say "following up."

| Email | Timing | Angle |
|---|---|---|
| 1 | Day 0 | Lead with their world, introduce your value |
| 2 | Day 3-4 | Different angle: social proof, case study result, reframed pain |
| 3 | Day 7-9 | Pivot: ask if this is even a priority right now |
| 4 | Day 14-16 | Value-add: share relevant resource, insight, or data point |
| 5 | Day 21-28 | Breakup: "Not the right time - I'll close the loop here" |

**Key rule**: After 5 emails with no reply, remove from sequence. Continuing damages deliverability and reputation.

## Personalization at Scale

Effective cold email feels personal. For scale, personalize in tiers:

| Tier | Approach | Use Case |
|---|---|
| Tier 1 (top accounts) | Fully bespoke | Research company, reference something specific |
| Tier 2 (mid-tier) | Segment-personalized | Custom first line per industry vertical or role |
| Tier 3 (high volume) | Template + merge fields | Company name, job title, industry inserted dynamically |

## Technical Hygiene for Cold Email

- Use separate sending domain (e.g., `trybrand.com`) to protect main domain reputation
- Warm up new domains 3-4 weeks before scaling
- Send plain-text or minimal HTML
- Monitor reply rates (aim 5-15%), bounce rates (under 3%), spam complaints
- Comply with CAN-SPAM, GDPR, CASL - B2B cold email to relevant prospects is permitted with proper opt-out

## Output Format

When writing cold email sequences, produce:

1. Full email copy for each step (subject + body)
2. Notes on angle used per email and why
3. Personalization variables to fill per prospect or segment
4. CTA instructions (next step in sales process when they respond)

Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/email/content/cold-outbound-{campaign-name}-{YYYY-MM-DD}.md`