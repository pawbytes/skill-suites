# Research Report Template

Use `{document_output_language}` for all content. Structure the report for scanning — busy creative teams read the angle shortlist first and dig into details only when needed.

## Document Structure

```markdown
---
created: {timestamp}
brand: {brand-name}
scope: {scope}
type: research
platforms: [{target platforms}]
angles_identified: {count}
---

# Content Research Report: {Brand Name}

## Executive Summary

{3-5 bullet points covering the most important findings. Lead with the biggest opportunity.}

---

## Angle Shortlist

{This is the most important section. 5-10 specific content angles, ranked by opportunity size.}

| # | Angle | Format | Platform | Why It Works | Priority |
|---|-------|--------|----------|--------------|----------|
| 1 | {angle} | {carousel/reel/etc} | {platform} | {gap + trend} | {high/med/low} |
| 2 | ... | ... | ... | ... | ... |

---

## Competitor Landscape

### {Competitor 1}
- **Platforms:** {active platforms}
- **Content Strategy:** {summary}
- **Visual Style:** {description}
- **Video Approach:** {description}
- **Gap:** {what they're missing}

### {Competitor 2}
...

### Competitive Gaps Summary
{Table or bullets summarizing the exploitable gaps}

---

## Trend Landscape

### Emerging Trends
| Trend | Classification | Relevance | Action |
|-------|---------------|-----------|--------|
| {trend} | {fad/trend/movement} | {why relevant} | {what to do} |

### Visual & Format Trends
{Current aesthetic and format movements relevant to the brand}

### Declining Trends
{What to avoid and why}

---

## Production Recommendations

### Design Briefs
{Detailed briefs for Designer — see production-recommendations.md for format}

### Video Briefs
{Detailed briefs for Video Producer — see production-recommendations.md for format}

---

## Platform Playbooks

### {Platform 1}
{Content mix, posting cadence, hashtag strategy, timing, features}

### {Platform 2}
...

---

## Sources

- [{Source title}]({url})
- [{Source title}]({url})
```

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `created` | Yes | ISO 8601 timestamp |
| `brand` | Yes | Brand name |
| `scope` | Yes | Research scope (competitor, trend, content, all) |
| `type` | Yes | Always "research" |
| `platforms` | Yes | Target platforms researched |
| `angles_identified` | Yes | Count of angles in shortlist |

## Writing Standards

- **Executive Summary:** Write last, after all research is complete. Lead with the single most actionable finding.
- **Angle Shortlist:** Every angle must be specific enough to brief a designer or video producer. "Post more carousels" is not an angle. "Before/after carousel showing {topic} transformation using split-frame layout with bold stat overlay" is an angle.
- **Sources:** Every factual claim must cite a URL. No citation = no credibility = report is not useful.
- **Length:** Aim for completeness over brevity. A thorough 2000-word report with sources is more valuable than a tight 500-word summary without evidence.
