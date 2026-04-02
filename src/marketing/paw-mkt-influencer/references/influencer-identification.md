# Influencer Identification and Vetting

> Capability prompt for paw-mkt-influencer skill. Load when user needs creator discovery, shortlists, or vetting criteria.

---

## Discovery Methods

- **Hashtag and keyword search**: Search brand-relevant hashtags and keywords on each platform. Check who creates top content.
- **Competitor analysis**: Identify who is already partnering with or posting about competitors.
- **Audience overlap**: Ask existing customers which creators they follow. Survey or social listening.
- **Platform tools**: TikTok Creator Marketplace, Instagram Creator Marketplace, YouTube BrandConnect.
- **Third-party platforms**: Aspire, Grin, CreatorIQ, Upfluence, Modash, HypeAuditor, Heepsy.
- **Organic brand fans**: Creators already mentioning the brand are the highest-value targets.
- **Industry events**: Speakers, panelists, and active voices in niche communities.

---

## Research Mode: Influencer Discovery

Use agent-browser to find and vet creators before building shortlists. Check `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md` for influencer data already collected.

**Influencer Research Commands:**

```bash
# TikTok Creator Search
agent-browser --session influencer-research open "https://www.tiktok.com/search/user?q={niche-keyword}" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body

# Instagram Hashtag Research (find active creators)
agent-browser --session influencer-research open "https://www.instagram.com/explore/tags/{niche-hashtag}/" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/channels/influencer/content/hashtag-research.png

# YouTube Creator Search
agent-browser --session influencer-research open "https://www.youtube.com/results?search_query={niche-keyword}+review" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body

# Check an influencer's engagement (public profile)
agent-browser --session influencer-research open "https://www.instagram.com/{influencer-handle}/" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: follower count, average post likes/comments (calculate engagement rate = (likes+comments)/followers x 100)
```

Close session when done: `agent-browser --session influencer-research close`

---

## Vetting Criteria

| Criterion | Green Flag | Red Flag |
|---|---|---|
| Engagement rate | At or above tier average | Below 1% IG, below 2% TikTok |
| Audience quality | Matches brand target demographics and geography | Irrelevant geographies or demographics |
| Content quality | Strong aesthetic, authentic voice, consistent | Low effort, inconsistent, overly templated |
| Brand alignment | Natural fit with category and values | Conflicting values, competitor partnerships |
| Audience authenticity | Steady organic growth, real comments | Sudden spikes, generic/emoji-only comments |
| Posting consistency | Regular cadence, active community | Long gaps, declining activity |
| Past partnerships | Professional execution, clear disclosures | Sloppy integrations, missing disclosures |

---

## Red Flags: Fake Followers and Bots

Warning signs:
- Follower-to-engagement ratio far below tier averages
- Sudden follower spikes without viral content
- Generic or off-topic comments
- High follower count but very low Story views (expect 3-7% on Instagram)
- Audience demographics mismatched with content language/niche
- Staircase-pattern growth charts (bulk purchases)

**Verification tools**: HypeAuditor, Modash, Social Blade, manual spot-checks of comment quality.

---

## Influencer Scoring

For detailed scoring rubric, read `./references/frameworks/influencer-scoring.md` from the indexed frameworks.

Quick-score checklist:
1. Engagement rate within tier norms? (Yes/No)
2. Audience demographics match target? (Yes/No)
3. Content quality consistent? (Yes/No)
4. No competing brand partnerships? (Yes/No)
5. Growth pattern organic (no sudden spikes)? (Yes/No)
6. Disclosure compliance in past partnerships? (Yes/No)

Score: 5-6 Yes = High fit. 3-4 Yes = Medium fit. 0-2 Yes = Low fit, skip.

---

## Outcome

Deliver an influencer shortlist table:
- Creator name and handle
- Platform
- Followers
- Engagement rate
- Niche/category
- Fit score (High/Medium/Low)
- Estimated cost
- Rationale for inclusion

Save to resolved path as `influencer-shortlist-{YYYY-MM-DD}.md`.