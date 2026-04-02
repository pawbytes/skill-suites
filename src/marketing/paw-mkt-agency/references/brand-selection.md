# Brand Selection

## Purpose
Present available brands when multiple exist in portfolio.

## Discovery Pattern

Use Glob to find brands: `.pawbytes/marketing-suites/brands/*/brand-context.md`

Each match represents one brand. Extract the brand slug from the path (the directory name between `brands/` and `brand-context.md`).

## Selection Prompt Format

When multiple brands exist, present:

```
I found {N} brands in your portfolio:

  1. {Brand Name 1} — {one-liner from brand-context.md}
     Status: SOSTAC {X/6 complete} | {N} active campaigns

  2. {Brand Name 2} — {one-liner from brand-context.md}
     Status: SOSTAC not started

  3. {Brand Name 3} — {one-liner from brand-context.md}
     Status: SOSTAC complete | Implementing

Which brand would you like to work on? (Enter number, name, or "new" to create)
```

## Building the List

1. Use Glob pattern `.pawbytes/marketing-suites/brands/*/brand-context.md` to discover all brands
2. For each match, extract brand slug from path and read the `brand-context.md` for name and description
3. Check SOSTAC status (see `./sostac-status.md`) for progress summary
4. Check `campaigns/` for active campaign count

## Handling Responses

| Response | Action |
|---|---|---|
| Number | Select corresponding brand, load context |
| Name (exact match) | Load that brand |
| Name (partial match) | Clarify which brand, or offer closest match |
| "new" | Start Brand Onboarding |
| "all" or multiple | Offer to work sequentially or set comparison view |