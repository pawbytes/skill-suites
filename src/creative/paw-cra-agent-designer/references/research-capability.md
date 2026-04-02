---
name: research-capability
description: Research new platforms, formats, and design trends to expand the Designer's knowledge base
---

# Research Capability

The Designer can research new platforms, formats, and design trends to maintain up-to-date knowledge without requiring skill updates.

## When to Research

Trigger research when:

- User requests a platform not in `platform-specifications.md`
- New social media feature or format launched (e.g., Instagram adds new carousel size)
- Design trend or technique unfamiliar
- Technical rendering issue unresolved
- User asks about emerging platforms (e.g., Threads, Bluesky, new apps)

## Research Process

### 1. Identify Research Need

Clarify what needs research:

| Category | Example Questions |
|----------|-------------------|
| **Platform Specs** | "What are the image sizes for Threads?" |
| **Safe Zones** | "What's the safe zone for TikTok shop ads?" |
| **Best Practices** | "What carousel design performs best on LinkedIn in 2026?" |
| **Technical Issues** | "Why are my HTML renders showing white gaps?" |
| **Design Trends** | "What color trends are popular in Q1 2026?" |

### 2. Search Authoritative Sources

Use web search to find:

- **Official documentation** — Platform help centers, developer docs
- **Design authority blogs** — Hootsuite, Buffer, Sprout Social, Canva
- **Industry reports** — Social media marketing reports, trend analyses
- **Technical documentation** — Playwright/Puppeteer docs, browser rendering guides

### 3. Extract Key Information

Extract and structure:

| Data Type | What to Capture |
|-----------|-----------------|
| **Dimensions** | Exact pixel sizes, aspect ratios |
| **Safe Zones** | Pixels from edges, device variations |
| **Best Practices** | Platform-specific tips, common mistakes |
| **Technical Specs** | File formats, size limits, color modes |
| **Trends** | Current patterns, what's working |

### 4. Save to Knowledge Base

Save findings to `.pawbytes/creative-suites/knowledge/`:

```markdown
---
name: {platform}-specifications
researched: YYYY-MM-DD
source: {primary URL}
expires: YYYY-MM-DD (optional, for time-sensitive data)
---

# {Platform} Specifications

## Image Dimensions

| Format | Dimensions | Aspect Ratio | Notes |
|--------|------------|--------------|-------|
| ... | ... | ... | ... |

## Safe Zones

{Description or diagram}

## Best Practices

- {Practice 1}
- {Practice 2}

## Common Mistakes

- {Mistake 1}: {How to avoid}

## Technical Notes

{Any rendering or export considerations}
```

### 5. Update Memory Index

Add entry to `.pawbytes/creative-suites/knowledge/index.md`:

```markdown
# Designer Knowledge Base

## Platform Specifications

| Platform | File | Last Updated |
|----------|------|--------------|
| Instagram | `instagram-specs.md` | 2026-04-01 |
| LinkedIn | `linkedin-specs.md` | 2026-04-01 |
| {New Platform} | `{platform}-specs.md` | YYYY-MM-DD |

## Technical Guides

| Topic | File | Last Updated |
|-------|------|--------------|
| Rendering HTML Templates | `html-rendering.md` | 2026-04-01 |
```

## Research Output Format

When research completes, inform the user:

```
**Research Complete: {Topic}**

Key findings:
- {Finding 1}
- {Finding 2}
- {Finding 3}

Saved to: `.pawbytes/creative-suites/knowledge/{filename}.md`

I'll now apply these specifications to your design.
```

## Knowledge Expiration

Some research expires quickly:

| Type | Refresh Frequency |
|------|-------------------|
| Platform dimensions | Annually or when platform announces changes |
| Safe zones | Annually |
| Best practices | Quarterly |
| Trend data | Monthly |
| Technical specs | As needed |

When using expired research, note to user: "This data was researched on {date}. Would you like me to refresh it?"

## Example Research Sessions

### Example 1: New Platform

> User: "I need to create posts for Bluesky"

Research process:
1. Search "Bluesky social media image dimensions 2026"
2. Find official Bluesky docs and marketing guides
3. Extract: Profile banner size, post image size, avatar size
4. Save to `knowledge/bluesky-specs.md`
5. Update knowledge index

### Example 2: Technical Issue

> User: "My carousel renders have white gaps between slides"

Research process:
1. Search "Playwright screenshot white gap issue"
2. Find documentation on element vs page screenshots
3. Extract root cause and solution
4. Update `best-practices-common-mistakes.md` if not already covered
5. Apply fix to rendering process

### Example 3: Design Trend

> User: "What carousel designs are trending on LinkedIn right now?"

Research process:
1. Search "LinkedIn carousel design trends 2026 engagement"
2. Find recent case studies and marketing reports
3. Extract patterns: color usage, typography, narrative structure
4. Save findings to `knowledge/linkedin-carousel-trends-2026-q1.md`
5. Apply insights to design recommendations

## Integration with Other Capabilities

Research integrates with:

- **Social Post Design** — Use researched specs for new platforms
- **Carousel Design** — Apply researched best practices
- **Template Creation** — Use researched dimensions
- **Save Memory** — Persist research findings

## Avoiding Redundant Research

Before researching:
1. Check `.pawbytes/creative-suites/knowledge/` for existing data
2. Check `platform-specifications.md` for known platforms
3. Check `best-practices-common-mistakes.md` for known issues

Only research if:
- Topic not in existing knowledge
- Existing data is expired or outdated
- User specifically requests fresh research