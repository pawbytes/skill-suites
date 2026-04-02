# Trend Spotting

Identify emerging trends relevant to the brand using structured signal detection.

**Key Methodologies:** Signal Detection Process, Trend Classification (Fad/Trend/Movement), Priority Matrix. Load `./methodologies.md` for complete methodology details.

## Trend Classification

| Category | Lifespan | Action |
|----------|----------|--------|
| **Fad** | <3 months | Jump on quickly if aligned, don't over-invest |
| **Trend** | 6-18 months | Plan content series, build expertise |
| **Movement** | 2+ years | Build brand authority, cornerstone content |
| **Declining** | Past peak | Avoid or use ironically |

## Input

Gather from conversation or brand context:
- Industry keywords
- Target audience
- Trend timeframe (immediate, seasonal, yearly)
- Content types of interest (formats, aesthetics, topics)

## Research Process

1. **Broad trend scan**:
   - Search "{industry} trends 2026"
   - Search "emerging {industry} trends"
   - Look for year-ahead predictions

2. **Platform-specific trends (Agent-Browser)**:

Access trend data behind login gates using authenticated Chrome profile:

```bash
# TikTok Creative Center / For You page
agent-browser --profile ~/.strategist-profile open https://tiktok.com/foryou
agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser screenshot ./research/tiktok-trends-current.png

# Instagram Explore and Reels
agent-browser --state "{project-root}/.pawbytes/creative-suites/.auth/session.json" open https://instagram.com/explore
agent-browser screenshot --full ./research/instagram-explore-trends.png

# Twitter/X trending topics
agent-browser --profile ~/.strategist-profile open https://twitter.com/explore
agent-browser get text body > ./research/twitter-trending.txt
```

For TikTok Creative Center (public): `https://creativecenter.tiktok.com/trends`

See `./browser-tools.md` for authentication setup.

3. **Cultural signals**:
   - What's entering mainstream?
   - What's declining?
   - What's niche but growing?

4. **Relevance filtering**:
   - Which trends fit brand voice?
   - Which align with audience interests?
   - Which have staying power vs. flash-in-pan?

## Output

Create `{brand-name}/research/trend-analysis.md`:

```markdown
# Trend Analysis: {Brand}
## Executive Summary
## Emerging Trends
### {Trend 1}
- **What it is:** {description}
- **Why it matters:** {relevance to audience/industry}
- **How to leverage:** {specific content ideas}
- **Velocity:** {growing/stable/declining}

### {Trend 2}
...

## Declining Trends
- {Trend to avoid and why}

## Platform-Specific Insights
### TikTok
- {trending formats, sounds, hooks}

### Instagram
- {trending formats, aesthetics, features}

### YouTube
- {trending formats, topics, thumbnails}

## Recommendation Priority
| Trend | Relevance | Ease | Impact | Priority |
|-------|-----------|------|--------|----------|
| {trend} | {high/med/low} | {easy/medium/hard} | {high/med/low} | {1-5} |

## Sources
- [Source 1](url)
```

## Completion Criteria

Analysis is complete when:
- [ ] Emerging trends classified by type (fad/trend/movement)
- [ ] At least 3 trends with specific participation guidance
- [ ] Declining trends flagged for avoidance
- [ ] Platform-specific insights for each target platform
- [ ] Priority matrix with actionable recommendations

## Quality Standard

- Distinguish between fads and sustainable trends
- Include specific "how to participate" guidance
- Note when to jump on a trend (timing matters)
- Flag trends that don't fit brand voice