# Research Compression Template

## Overview

Raw research is too much context for the Producer agent to consume efficiently. Compression transforms hours of research into a focused, producer-ready document that contains exactly what's needed for content creation — no more, no less.

## Compression Principles

### What to Include
- Key statistics with sources
- Differentiation opportunities (gaps in the market)
- Audience pain points in their words
- Common themes (what everyone says)
- User's unique perspective/expertise
- Hook seeds and angle ideas

### What to Exclude
- Raw search results and URLs
- Full article text or transcripts
- Redundant findings
- Interesting-but-irrelevant tangents
- Low-quality sources

### Compression Ratio Target
Aim for 10:1 compression. 30 minutes of research should compress to ~3 minutes of reading for the Producer.

## Template Structure

```markdown
# Research Context: {Webinar Title/Topic}

**Webinar Kind:** [Thought Leadership | Product Demo | Lead Generation | Internal Training]
**Target Audience:** [Specific audience description]
**Research Date:** [YYYY-MM-DD]
**Sources Consulted:** [Number]

---

## Executive Summary

[2-3 sentences capturing the core insight from research. What's the opportunity?]

---

## Key Statistics

| Statistic | Source | Hook Potential |
|-----------|--------|----------------|
| [Number and claim] | [Source, date] | [How it could be used] |
| ... | ... | ... |

Include 5-10 of the most compelling, credible statistics.

---

## Audience Pain Points

Based on forum discussions, social media, and customer feedback:

1. **[Pain Point 1]** — "[Direct quote or close paraphrase]"
   - Evidence: [Where found]
   - Emotional intensity: [High/Medium/Low]

2. **[Pain Point 2]** — "[Direct quote or close paraphrase]"
   - Evidence: [Where found]
   - Emotional intensity: [High/Medium/Low]

[Continue for 3-5 main pain points]

---

## Competitive Landscape

### Key Voices
| Who | Their Angle | Gap/Opportunity |
|-----|-------------|-----------------|
| [Name/Organization] | [Their position] | [What they miss] |

### Content Saturation
- **Oversaturated themes:** [What everyone covers]
- **Underserved angles:** [What's missing]
- **Opportunity spaces:** [Where to differentiate]

---

## Common Themes (What Everyone Says)

1. [Theme 1] — [Brief note on how commonly it appears]
2. [Theme 2] — [Brief note]
3. [Theme 3] — [Brief note]

These are areas to avoid repeating or to explicitly challenge.

---

## User's Unique Perspective

### Expertise Highlights
- [Unique insight 1 from user]
- [Unique insight 2 from user]
- [Proprietary framework/methodology]

### Stories and Examples
- [Story 1 brief — details in separate file if needed]
- [Story 2 brief]

### Contrarian Positions
- [Where user disagrees with common advice]
- [Why — brief justification]

---

## Hook Seeds

Initial angles that emerged from research:

1. **[Hook idea 1]** — [Technique: Contrarian/Data/Story/etc.]
   - Why it works: [Reasoning]
   - Risk: [What could make it fail]

2. **[Hook idea 2]** — [Technique]
   - Why it works: [Reasoning]
   - Risk: [What could make it fail]

[Continue for 5-10 seeds — these get refined in hook generation]

---

## Research Gaps (If Any)

Areas that need more investigation:
- [Gap 1]
- [Gap 2]

Note if any gaps are critical enough to extend research.

---

## Sources Reference

Quick reference for Producer to access sources if needed:

| Type | Source | Key Finding |
|------|--------|-------------|
| [Article] | [URL/Title] | [What it contributed] |
| [Report] | [Source] | [What it contributed] |

[Keep this minimal — full URLs in separate file if needed]
```

## Compression Process

### Step 1: Filter Ruthlessly

Review all raw research notes. For each finding, ask:
- Does this inform the hook?
- Is this unique or redundant?
- Will the Producer need this?

Discard anything that doesn't pass.

### Step 2: Categorize

Sort remaining findings into:
- Statistics → Key Statistics table
- Quotes/pain points → Audience Pain Points
- Competitive info → Competitive Landscape
- Repeated advice → Common Themes
- User input → User's Unique Perspective
- Initial ideas → Hook Seeds

### Step 3: Summarize, Don't Copy

Rewrite findings in compressed form:
- Full paragraph → 1-2 sentences
- Article → Key takeaway
- Statistics → Table row with source

### Step 4: Add Structure

Apply the template structure. Ensure:
- Tables are scannable
- Bullet points are consistent
- Sections are clearly labeled
- Reading time is 2-3 minutes

### Step 5: Validate Completeness

Check that compressed context includes:
- [ ] Clear audience definition
- [ ] 5-10 key statistics
- [ ] 3-5 pain points with evidence
- [ ] Competitive landscape overview
- [ ] Common themes to avoid or challenge
- [ ] User's unique perspective captured
- [ ] Initial hook ideas planted

## File Location

Save compressed research to:
```
{project-root}/.pawbytes/webinar-suites/webinars/{webinar-slug}/research-context.md
```

## Producer Consumption

The Producer agent reads this file during activation to understand:

1. **What hook was chosen** — Read `hook-selected.md`
2. **Why it was chosen** — Reasoning in that file
3. **Research backing** — This `research-context.md` file
4. **What to emphasize** — User's unique perspective section
5. **What to avoid** — Common themes section

## Example Compression

### Raw Research (excerpt):
> "I found 15 blog posts about email automation. Most say you should segment your list. One from Mailchimp in 2023 says segmented campaigns get 14.31% higher opens. Another from Campaign Monitor says 760% increase in revenue from segmentation. There's a HubSpot article about behavior triggers that got a lot of shares. Forums show people struggling with 'what to automate' more than 'how to automate.' A Reddit thread had 200+ upvotes asking about automation mistakes. User mentioned they've seen companies over-automate and lose personal touch."

### Compressed:
> **Key Statistics:**
> - Segmented campaigns: 14.31% higher opens (Mailchimp, 2023)
> - Segmentation impact: 760% revenue increase (Campaign Monitor)
>
> **Audience Pain Points:**
> - "What should I automate?" — confusion on strategy, not tactics (Reddit, 200+ upvotes)
>
> **Common Themes:**
> - Segment your list (nearly universal advice)
> - Use behavior triggers
>
> **User's Unique Perspective:**
> - Over-automation risks losing personal touch
> - Has witnessed companies go too far with automation

This compression reduces ~150 words to ~60 words while preserving all actionable insights.