# Competitive Context

Loaded when web research is enabled or the user names competitors/alternatives. Power-user section — skip if brief is thin and user didn't ask, but note "competitive context not researched" in caveats.

## Goal

Clarify **what the client might compare this proposal against** and how the seller differentiates — agencies, freelancers, in-house hire, SaaS DIY, status quo.

## Sources

- Brief `constraints[]` and `clientContext` (incumbent vendor, prior bad experience)
- Web search: `{client industry} {serviceType} providers`, RFP competitor lists if public
- Seller's positioning from `{memory-root}/brand/identity.md` voice/positioning if present
- Local case-study outcomes as differentiation proof (cross-ref match IDs)

## Output shape

```json
"competitiveContext": {
  "summary": "Likely alternatives and seller's edge for THIS deal",
  "alternatives": [
    {
      "name": "Full-service digital agency",
      "differentiator": "Breadth vs seller's specialist depth and faster timeline",
      "source": "brief.md constraint: prior agency over budget"
    }
  ]
}
```

## Discipline

- Name real alternative **categories** or named competitors only when brief or public RFP cites them — do not invent competitor names.
- Differentiators must tie to **evidence** (local case study, brief constraint, observed market gap).
- Keep actionable for generation — feeds objection pre-emption, not a market essay.

## After gathering

Append to findings JSON. Write one sentence in `recommendation` (top-level findings field) on competitive positioning if relevant.
