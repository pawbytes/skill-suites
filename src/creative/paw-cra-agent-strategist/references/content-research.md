# Content Research

Discover trending topics, hashtags, and content opportunities using systematic research.

**Related:** Content Pillar framework and Strategic Group Analysis can help identify content gaps. Load `./methodologies.md` for framework details.

## Input

Gather from conversation or brand context:
- Industry or niche
- Target audience
- Content themes of interest
- Platforms to research
- Timeframe (current trends vs. evergreen)

## Research Process

1. **Topic discovery**:
   - Search "{industry} trending topics 2026"
   - Search "what {audience} is talking about"
   - Check platform-specific trends (TikTok, Instagram, YouTube)

2. **Social media deep-dive (Agent-Browser)**:

For platforms requiring login, use agent-browser with authenticated Chrome profile:

```bash
# Instagram Explore (logged in)
agent-browser --state "{project-root}/.pawbytes/creative-suites/.auth/session.json" open https://instagram.com/explore
agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser screenshot --full ./research/instagram-explore.png

# TikTok For You page (logged in)
agent-browser --profile ~/.strategist-profile open https://tiktok.com/foryou
for i in {1..5}; do
    agent-browser scroll down 600
    agent-browser wait 500
    agent-browser screenshot "./research/tiktok-view-$i.png"
done

# LinkedIn feed for B2B insights
agent-browser --profile ~/.strategist-profile open https://linkedin.com/feed
agent-browser get text body > ./research/linkedin-feed-content.txt
```

See `./browser-tools.md` for authentication setup and full command reference.

3. **Hashtag research**:
   - Identify high-volume, relevant hashtags
   - Find niche hashtags with less competition
   - Note trending hashtag formats

4. **Content format analysis**:
   - What formats are performing well?
   - What hooks are working?
   - What content gaps exist?

5. **Audience pain points**:
   - Search for questions being asked
   - Identify recurring problems
   - Note language and terminology used

## Output

Create `{brand-name}/research/content-opportunities.md`:

```markdown
# Content Opportunities: {Brand}
## Executive Summary
## Trending Topics
| Topic | Relevance | Opportunity Score |
|-------|-----------|-------------------|
| {topic} | {why relevant} | {1-10} |

## Hashtag Strategy
### High-Volume Tags
- #{hashtag} - {context}
### Niche Tags
- #{hashtag} - {context}

## Content Formats
- {Format 1}: {why it works, examples}
- {Format 2}: {why it works, examples}

## Audience Questions
- "{question}" - {where it appears, search volume}
- "{question}" - {where it appears, search volume}

## Content Ideas
1. {Specific idea with hook, format, and angle}
2. {Specific idea with hook, format, and angle}

## Sources
- [Source 1](url)
```

## Completion Criteria

Research is complete when:
- [ ] Trending topics identified with relevance scores
- [ ] Hashtag strategy defined (high-volume + niche)
- [ ] Content formats analyzed with performance insights
- [ ] At least 5 actionable content ideas generated
- [ ] Sources cited for all data points

## Quality Standard

- Prioritize actionable content ideas over raw data
- Include specific hooks and angles, not just topics
- Note seasonal vs. evergreen opportunities
- Align opportunities with brand voice and positioning