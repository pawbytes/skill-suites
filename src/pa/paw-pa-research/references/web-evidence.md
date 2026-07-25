# Web Evidence & Industry Benchmarks

Loaded when web research is enabled (`local-browser` or `cursor-ide-browser` mode). External proof points — "here's what the industry shows" — complementing local case-study matches.

## Goal

Find **credible external examples** relevant to the brief's scope: similar project write-ups, vendor case studies, industry reports, methodology benchmarks. Not generic thought leadership unless directly relevant.

## Search strategy

Derive 2–4 search queries from the brief:

- `{serviceType} case study {industry}`
- `{deliverable} implementation benchmark`
- `{technology} migration results`
- RFP/scoping type → add `enterprise`, `compliance`, or `ROI` terms as appropriate

Prefer primary sources: vendor case studies, peer-reviewed or named analyst reports, reputable trade press. Avoid unattributed listicles.

## What to capture

```json
"webEvidence": {
  "summary": "What external proof suggests about approach, outcomes, or risk",
  "examples": [
    {
      "title": "Article or case study title",
      "url": "https://...",
      "relevance": "Why this matters for THIS brief",
      "keyTakeaway": "One concrete fact or outcome cited from the source"
    }
  ]
}
```

Cap at **5 examples** — best relevance, not most results.

## Discipline

- **Every example needs a URL** (or `source: seller-provided` if user pasted).
- **Quote facts, don't invent outcomes.** "40% faster checkout" only if the source says so.
- **Respectful browsing** — read-only, human-paced. No paywall circumvention; if blocked, note in caveats and ask user for paste.
- Record searches attempted in scratch notes for caveats transparency.

## Thin results

If fewer than 2 relevant examples found, say so in `webEvidence.summary` and `caveats`. Pricing and generation will rely more on local matches and brief scope.

## After gathering

Append to findings JSON. Return to SKILL.md **Produce the dossier** when all web flavors complete.
