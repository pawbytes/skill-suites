# Context Router

## Purpose
Determine the strongest starting context and route appropriately.

## Starting Context Options

### Blank-Page / Strategy Mode
If user is starting from zero, use agency workflow to establish brand context, SOSTAC planning, and channel priorities.

### Codebase / Local Project Mode
If user references a repo, product, site, or asks for implementation:
1. Inspect repo first
2. Use repo as concrete context and source-of-truth for strategic recommendations
3. If implementation not requested, still use repo as context

### Live URL / Profile Audit Mode
If user gives website, landing page, store, or social/profile URL:
1. Audit live presence first
2. Use as starting context

## Routing Decision Tree

### Step 1 — Identify Working Context

1. Check if user started with repo, local implementation request, live URL, profile, or existing brand in conversation
2. If repo/implementation request → inspect repo first, use as immediate working context
3. If live URL/profile → audit first, use as immediate working context
4. If no repo/URL → scan `./.pawbytes/marketing-suites/brands/` for existing brand directories
5. Based on findings:

| Situation | Action |
|---|---|
| `./.pawbytes/marketing-suites/brands/` does not exist or empty | Ask: "No brands found. Would you like to start marketing for a new brand?" → Brand Onboarding |
| Exactly one brand exists | Auto-select, confirm with user → Step 2 |
| Multiple brands exist | Present numbered list (Brand Selection) → Step 2 |
| User explicitly names brand | Match existing or offer to create |

### Step 2 — Read Brand Context

Brand context shapes every recommendation. Without it, output is generic and misaligned.

When brand workspace is active context, read before substantial work:

```
./.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md                  — Read first
./.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md      — Read if exists (deep positioning)
./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/                           — Check phase file existence
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/                        — Check named campaigns
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/                         — Check standalone channel work
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/                       — Check operational work
```

If `paw-mkt-product-context.md` missing and brand has active campaigns or complete SOSTAC, note: "I notice there's no product marketing context document yet — this helps specialists produce on-brand output. Want to create one?"

### Step 3 — Determine Workflow

After reading brand context, evaluate SOSTAC status and route:

| SOSTAC Status | User Intent | Route |
|---|---|---|
| No SOSTAC folder or empty | Any | Start SOSTAC planning |
| SOSTAC in progress (phases missing) | Continue planning | Resume at next incomplete phase |
| SOSTAC in progress | Wants to implement anyway | Warn incomplete, offer to finish first |
| SOSTAC complete (6 phases) | Wants to implement | Spawn implementation team |
| SOSTAC complete | Wants to update plan | Re-open specific phase |
| SOSTAC complete, campaigns active | Check progress | Progress tracking |

### Step 4 — Handle Specific Requests

For targeted requests (e.g., "write a blog post for Acme Corp"):
1. Select and load brand (Steps 1-2)
2. Check SOSTAC status (Step 3)
3. If plan exists → spawn only relevant specialist
4. If no plan → recommend planning first, respect user's choice to proceed without