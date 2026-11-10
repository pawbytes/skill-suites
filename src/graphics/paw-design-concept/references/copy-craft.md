# Copy craft for graphics

Distilled from the 2026-11 research (NN/g, OAAA, Meta, Google Ads, IAB, FTC, large carousel and headline studies). Numbers are defaults the scripts also enforce; break one on purpose and say why in `notes`.

## Roles

| Role | Job | Length |
|---|---|---|
| proposition (not printed) | The one thing the viewer must take away; everything on the canvas supports it or goes | 1 sentence |
| eyebrow | Category or kicker above the headline; caps are fine here | 1–3 words |
| headline | Hook and message; must work alone | 3–10 words, by format |
| subhead | Reason to believe, qualifier, the how; says something the headline does not | 6–15 words |
| body / bullets | Detail for the viewer who stops; bullets beat paragraphs | ≤30 words per slide |
| cta | The next action, verb first, naming what they get | 2–5 words |
| fine_print | Handle, source, legal qualifier, sponsor line | as needed |

Word budgets per format and role come from `copydeck.py budgets`, which the validator applies. A headline that only fits by shrinking the type is too long; cut words.

## Headlines

- Sentence case, numerals ("7", not "seven"), concrete nouns. If a reader takes only the first two words, they should get the gist.
- Never promise what the asset or landing page does not deliver; misleading packaging is penalised on YouTube and erodes trust everywhere.
- Thumbnails add a second hook beside the video title and never repeat it; 3–7 words readable at about 168 px wide.

## CTAs

- Verb plus a specific outcome: "Get the checklist", "Book a 15-minute demo", "Register free". Not "Click here", "Learn more", "Submit". First person ("Start my free trial") is a test candidate, not a rule.
- On Meta, TikTok and LinkedIn ads the platform draws the real button. Put the CTA in the ad's text fields and keep a button-shaped CTA out of the image, where it sits under the real one.
- Uploaded display banners expect a button-shaped CTA in the same position on every size.
- Posters and flyers: action plus channel ("Scan to register" beside a QR code and a short URL). Long URLs and phone numbers do not survive outdoor viewing.

## Carousels

Arc: hook (1), why it matters (2), one idea per slide (3 to N-2), summary (N-1), single CTA (N). The cover is a promise readable in under two seconds, 6–10 words, an honest number, not logo-first. The closer repeats the cover's look and the brand mark, because Instagram can re-serve a carousel from a later slide. LinkedIn document links do not click in-feed, so URLs go in the post text. `hooks.py carousel` lists cover patterns, swipe cues and closers.

## Posters and flyers

Event hierarchy, by size: what (the name or hook, largest), when (weekday, date, time; "Sat 14 Mar 2027, 7 pm", never 03/04), where (venue and city), how (tickets or registration: QR, short URL, price or "free"), who (headliners, organisers), then fine print (sponsors, accessibility, age limits). Flyer fronts work alone like a poster; backs carry the details (3–5 bullets, proof, schedule or pricing, how to act, address, legal, logo).

## Claims, proof and disclaimers

- Every stat carries a source on the canvas or in the caption; every superlative has proof nearby.
- A disclaimer sits next to its claim, on the same canvas, at least the smallest legal text size, and inside the safe zone. On Meta Reels with a disclaimer, keep the bottom 40% clear.
- Urgency and scarcity only when real; fake deadlines, invented testimonials and unsourced numbers are legal risks (FTC rules on fake reviews apply since October 2024).
- Finance, health, alcohol, political and other regulated categories: flag the deck for the user's legal review and do not invent disclaimer wording.

## Captions and alt text

Essential facts (dates, prices, deadlines, URLs, legal lines) also belong in the post caption or landing page, because screen readers cannot read pixels. Note in `notes` anything the caption must carry; deliver writes the alt text from the deck.
