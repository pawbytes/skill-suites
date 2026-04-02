# Check Existing Context

Before building or updating product marketing context, check what already exists.

## Step 1 — Existing Product Marketing Context?

Look for `./.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md`.

| Condition | Action |
|-----------|--------|
| **Found** | Read it. Present: "Your product marketing context was last updated {date}. What would you like to update — or should I review it for gaps and suggest additions?" |
| **Not found** | Proceed to Step 2 |

## Step 2 — SOSTAC Files Available?

Scan `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/` for completed phase files:

| SOSTAC File | Rich content to extract |
|-------------|-------------------------|
| `01-situation.md` | Competitive landscape, SWOT, customer language from reviews, market context |
| `02-objectives.md` | Goals, target metrics, success definition |
| `03-strategy.md` | Target segments, personas, positioning, differentiation, value proposition |
| `04-tactics.md` | Objections addressed in channel strategy, proof points referenced |

| Condition | Action |
|-----------|--------|
| **SOSTAC files exist** | Go to Auto-Extract capability |
| **No SOSTAC files** | Go to Focused Interview capability |

## Starting Context Router

Before building or updating, identify the strongest context the user is starting from:

| Context Type | Approach |
|--------------|----------|
| **Blank page / new brand** | Use focused interview to surface positioning, audience, objections, proof without pretending strategy is already defined. |
| **Existing repo, docs, brand materials** | Treat sources as evidence of current product and messaging. Translate into sharper market context rather than implementation advice. |
| **Live URL or public presence** | Use public site and messaging as inputs for positioning analysis, gap-finding, and clarification. |

If some sources are missing, continue with best available context instead of blocking progress.