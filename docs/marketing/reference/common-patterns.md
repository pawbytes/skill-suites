# Reference: Common Patterns

The suite follows a few consistent patterns across skills.

## 1. Brand-first workflow

Most skills expect you to select or confirm a brand before they do any real work.

## 2. Read context before writing

Common input order:
1. `brand-context.md`
2. `paw-mkt-product-context.md` if it exists
3. relevant SOSTAC files
4. existing channel outputs in `campaigns/`, `content/`, or `analytics/`

## 3. Strategy before scale

Many specialist skills can do one-off work without a full plan, but they work best when a SOSTAC plan exists.

## 4. Files over chat-only output

The suite prefers saving deliverables to files, so work can continue across sessions.

## 5. Product marketing context as a multiplier

`paw-mkt-product-context.md` is one of the highest-leverage files in the system because it improves downstream copy, messaging, objections handling, and persona targeting.

## 6. Handoffs are intentional

Examples:
- SOSTAC -> product marketing context -> specialists
- Content -> SEO, email, social, video
- Launch -> PR, paid ads, email, social, sales
- CRO -> analytics and paid ads
- Retention -> email, referral, analytics

## 7. Output roots stay predictable

Most outputs live in one of three places:
- strategy docs in brand root or `sostac/`
- campaign execution in `campaigns/`
- content production in `content/`

## 8. Quick tasks are allowed

You do not need to complete the whole system before asking for one asset. The suite supports fast, narrow tasks when needed.

## 9. Progressive disclosure via CSV-indexed frameworks

Every skill uses a lightweight `frameworks-index.csv` to avoid loading all framework files into context. Skills read the index first, match the user's situation to the `best_for` column, then read only the relevant framework file(s). This reduces token use by 80–90% per lookup compared to a monolithic file. Each skill's framework files live in `references/frameworks/`.
