# Bounded AI Visuals

Optional visuals that strengthen the proposal without becoming a design project. Scope is intentionally narrow — serious mockups and wireframes belong in the Creative Suite.

## What's in scope (generation skill)

| Visual type | When to use | Output |
|-------------|-------------|--------|
| **Hero image** | Pitch cover, executive summary opener | `visuals/hero.{png,webp}` |
| **Process diagram** | Approach section — 3–7 step flow | `visuals/process-diagram.{png,svg}` |
| **Architecture diagram** | Technical/scoping proposals with system components | `visuals/architecture.{png,svg}` |
| **Pricing chart** | Tiered pricing comparison or milestone timeline | `visuals/pricing-chart.{png,svg}` |

## What's out of scope (hand off)

| Visual type | Hand off to | Note in proposal |
|-------------|-------------|------------------|
| UI mockups | `paw-cra-agent-designer` | "Detailed UI mockups available upon request — produced by our design team." |
| Wireframes | `paw-cra-agent-designer` | Same |
| Brand identity work | `paw-cra-design-brand` | N/A for proposals |
| Video / motion | `paw-cra-video-*` | N/A for proposals |
| Complex data dashboards | Manual or defer | Note as future deliverable |

## Generation rules

1. **Bounded count** — max 3 visuals per proposal (hero + 2 supporting). More is clutter.
2. **Brand-aligned** — use colors from `brand/identity.md`; never clash with seller palette.
3. **Simple** — diagrams should read in 5 seconds. No dense architecture dumps.
4. **Referenced in draft** — embed with relative paths: `![Process](visuals/process-diagram.png)`
5. **Alt text** — always include descriptive alt text for accessibility.
6. **No fabricated UI** — do not generate fake screenshots of products you haven't built.

## CRA handoff workflow

When the brief or user requests mockups/wireframes:

1. Do **not** generate them in this skill.
2. Write a handoff brief to `{run-folder}/cra-handoff.md`:

```markdown
# CRA Design Handoff — {project name}

**Requested by:** paw-pa-generation
**Client:** {client name}
**Deliverable:** {mockups | wireframes | both}
**Screens/flows:** {list from brief}
**Brand ref:** {memory-root}/brand/identity.md
**Context:** {link to draft-v1.md approach section}
**Deadline note:** {if any}
```

3. Set `craHandoff` in `generation-summary.json` to the handoff path.
4. In the proposal, reference: "We recommend a design workshop to validate UI direction — our design team can produce mockups within {N} business days of kickoff."

Invoke `paw-cra-agent-designer` separately if the user wants to proceed now.

## Hero image brief template

When generating a hero image:

- **Subject:** Abstract representation of the client's industry/problem — not literal client branding unless they provided assets.
- **Style:** Clean, professional, matches brand colors. No stock-photo clichés (handshakes, puzzle pieces).
- **Dimensions:** 1200×400px landscape for HTML header; also works as section divider.
- **Text:** No text baked into the image — titles live in markdown.

## Diagram brief template

For process/architecture diagrams:

- **Nodes:** 3–7 labeled boxes max.
- **Flow:** Left-to-right or top-to-bottom; numbered steps.
- **Labels:** From the approach section — use the same terminology as the proposal body.
- **Format:** Prefer SVG for crisp print; PNG acceptable for hero.

## Pricing chart brief template

For tiered pricing:

- **Type:** Horizontal bar comparison or simple column chart.
- **Data:** From `pricing.json` tiers — names and totals only (no internal cost breakdown).
- **Highlight:** Recommended tier visually emphasized (accent color).
- **No misleading scale** — honest proportional representation.

## Skip visuals when

- User says no visuals.
- RFP forbids non-essential graphics.
- Brand identity is incomplete (no colors) — fix brand first or skip.
- Time-critical autonomous run with no visual request — prose is sufficient.

Record skipped visuals in `generation-summary.json`: `"visuals": []`.
