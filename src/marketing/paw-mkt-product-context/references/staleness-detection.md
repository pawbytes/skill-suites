# Staleness Detection and Freshness Signals

Product marketing context must stay current. Stale context produces stale marketing.

## Document Freshness Header

Every `paw-mkt-product-context.md` must include a freshness header:

```markdown
---
last_updated: YYYY-MM-DD
next_review: YYYY-MM-DD (quarterly from last_updated)
validation_status: current | needs_review | stale
---
```

## Validation Status Definitions

| Status | Condition |
|--------|-----------|
| `current` | Updated within last 90 days, no major market changes flagged |
| `needs_review` | 90+ days since update, or downstream specialist flagged a gap |
| `stale` | 180+ days since update, or major market change detected |

## When Downstream Specialists Should Flag Staleness

| Signal | What It Looks Like | Action |
|--------|--------------------|--------|
| Customer language mismatch | Copy using phrases from §9 gets poor response | Flag §9 for refresh with new customer interviews |
| Competitor not in document | Lost deal to competitor not in §5 | Flag §5 for competitive update |
| Proof point outdated | Achievement in §11 no longer impressive | Flag §11 for fresh case study data |
| Objection not covered | New objection in sales calls not in §7 | Flag §7 for objection expansion |
| Persona doesn't match | Leads from target persona not converting | Flag §3 for persona validation |
| Market shift | New regulation, technology, or trend affecting positioning | Flag entire document for strategic review |

**How to flag:** When working in any specialist skill, if `paw-mkt-product-context.md` seems misaligned with reality, add a comment:

> **Note:** The paw-mkt-product-context.md may need updating — [specific signal observed]. Consider running the paw-mkt-product-context skill to refresh.

## Quarterly Review Trigger

Every 90 days, review the document:

### Review Process

1. **Quick scan (15 min)** — Read the document. Note anything outdated.
2. **Sales and support check** — Ask for recent customer language, new objections, fresh proof points from customer-facing teams.
3. **Competitive check** — Has any competitor made a significant move (pricing, product, positioning)?
4. **Update if needed** — If 2+ sections have meaningful changes, run update process.
5. **Refresh dates** — Update `last_updated` and `next_review` even if no changes made — signals active maintenance.

## Automatic Staleness Indicators

Document becomes `stale` automatically when:

- 180+ days since `last_updated`
- Major product change (new core feature, significant pricing change, market expansion)
- Company pivot or rebrand
- New funding round or acquisition

When stale, downstream specialists should explicitly recommend refreshing before proceeding with major campaign work.