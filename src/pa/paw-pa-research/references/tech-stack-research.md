# Tech Stack Research

Loaded when the brief mentions technology, integrations, platforms, or a client domain is known — and web research is enabled (or user pasted tech clues).

## Goal

Document the prospect's **technology footprint** so the proposal speaks their stack and scopes integrations realistically.

## Where to look

1. **Brief requirements** — explicit tech (Shopify, Salesforce, AWS, etc.)
2. **Client website** — page source hints, `/careers` job posts (stack in JDs), `/integrations`, app subdomains
3. **BuiltWith / Wappalyzer-style signals** — if browser tools expose stack data, record what was observed
4. **Job listings** — engineering roles often list stack
5. **Case-study index** — prior work in same stack (cross-reference, cite index path)

## Output shape

```json
"techStack": {
  "summary": "One paragraph on footprint and migration/implication for this project",
  "technologies": [
    {
      "name": "Shopify Plus",
      "evidence": "Careers page lists Shopify theme developer",
      "source": "https://client.com/careers/engineering"
    }
  ]
}
```

## Discipline

- List only technologies with **observed evidence** — not "they probably use React."
- Separate **confirmed** (direct evidence) from **inferred** in evidence text if inference is necessary; prefer omitting to guessing.
- If nothing found, `summary` states: "No public tech footprint observed; scope per brief requirements only" and list brief-mentioned tech with source `brief.md`.

## After gathering

Append to findings JSON. Tech stack feeds generation (approach section) and pricing (integration complexity).
