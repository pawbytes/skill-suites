# Content Research Capability

## Overview
Use browser automation to research content gaps, audience questions, and competitive content. Check `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md` first -- data may already be collected.

---

## agent-browser Setup

Before running browser-based research, check if `agent-browser` is available (`agent-browser --version`). If not found, install:

```bash
npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
```

If installation fails, use `WebFetch` and `WebSearch` tools as alternatives.

---

## Research Commands

### Google PAA (People Also Ask) -- Content Opportunities

```bash
agent-browser --session content-research open "https://www.google.com/search?q={topic-keyword}" && agent-browser wait --load networkidle
agent-browser get text body
```
Extract: PAA questions = content opportunities, featured snippets = format benchmarks

### Answer The Public -- Question Map

```bash
agent-browser --session content-research open "https://answerthepublic.com/" && agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser get text body
```

### Competitor Blog Research

```bash
agent-browser --session content-research open "https://{competitor-domain}/blog" && agent-browser wait --load networkidle
agent-browser get text body
```
Extract: content categories, publishing frequency, formats, popular topics

### Reddit -- Top Questions by Upvotes

```bash
agent-browser --session content-research open "https://www.reddit.com/search/?q={niche-keyword}&sort=top&t=year" && agent-browser wait --load networkidle
agent-browser get text body
```
Extract: top discussions = highest-value content topics

### Quora -- Question Volume in Category

```bash
agent-browser --session content-research open "https://www.quora.com/search?q={topic}" && agent-browser wait --load networkidle
agent-browser get text body
```

---

## Close Session

```bash
agent-browser --session content-research close
```

See the agent-browser skill for full command reference.

---

## Research Synthesis

After research, synthesize findings into:
- **Topic opportunities**: High-value keywords and questions with content potential
- **Format benchmarks**: What content types perform for this topic
- **Competitive gaps**: Topics competitors haven't covered or covered poorly
- **Audience pain points**: Real questions people are asking

Feed insights into content strategy and editorial calendar planning.