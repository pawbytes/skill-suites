# Competitor Scan

Analyze 3-5 competitors in the brand's space using Exa MCP tools. Focus on content and creative strategy, not corporate profiles.

## Competitor Discovery

If competitors are not specified in the request or brand guidelines:

1. Search "{industry} brands" and "{industry} content creators" via `web_search_exa`
2. Look for brands with active social/content presence (not just large companies)
3. Include 1-2 aspirational competitors (brands doing content exceptionally well, even if different scale)

## Research Dimensions

For each competitor, investigate:

### Content Strategy
- What platforms are they active on?
- How often do they post? What's the content mix (educational, promotional, entertaining)?
- What content formats dominate (carousel, reel, static, long-form video)?
- What are their top-performing content themes?

### Visual Language
- Color palette and photography style
- Typography choices (bold/minimal, serif/sans)
- Layout patterns (grid, editorial, collage)
- Brand consistency across platforms

### Video Strategy
- Video formats used (talking head, B-roll montage, motion graphics, UGC style)
- Average video length by platform
- Subtitle/caption approach
- Hook and retention techniques
- Music and audio choices

### Messaging & Positioning
- Brand voice (formal, casual, edgy, warm)
- Key messages and value propositions
- Call-to-action patterns
- Community engagement approach

## Production-Focused Synthesis

For each competitor, conclude with:

| What They Do Well | What's Missing | Production Opportunity |
|-------------------|----------------|----------------------|
| {specific tactic} | {gap we can fill} | {brief for Designer or Video Producer} |

The "Production Opportunity" column is the key output — it feeds directly into the angle shortlist and production recommendations.

## Search Queries

Effective Exa queries for competitor research:

```
"{competitor name}" content strategy
"{competitor name}" social media marketing
"{competitor name}" instagram OR tiktok OR youtube
site:{competitor-domain} blog OR content
"{industry}" best content marketing examples
```

Use `crawling_exa` to extract detailed content from competitor blogs, about pages, and social landing pages.

## Agent-Browser for Social Analysis

If `agent-browser` is available with auth sessions, use it for:
- Scrolling competitor Instagram feeds to capture visual patterns
- Checking TikTok profiles for video format and engagement data
- Reviewing LinkedIn company pages for B2B content strategy

This is optional — Exa-based research covers most needs.
