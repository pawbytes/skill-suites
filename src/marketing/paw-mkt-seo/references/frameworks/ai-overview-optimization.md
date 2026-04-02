# AI Overview Optimization

### What Is AI Overview Optimization?
Optimizing content to be cited, referenced, or surfaced by AI-powered search features (Google AI Overviews, Bing Copilot, ChatGPT search, Perplexity, Claude).

### Content Structure for AI Citation
- [ ] Use clear, direct answers in the first 1-2 sentences of each section
- [ ] Structure content with question-based H2/H3 headings (matching how people ask questions)
- [ ] Provide concise definitions before detailed explanations
- [ ] Use numbered lists and bullet points for step-by-step content
- [ ] Include data, statistics, and specific numbers (AI prefers citable facts)
- [ ] Write in a neutral, authoritative tone (encyclopedia-like for factual content)
- [ ] Cover topics comprehensively (AI prefers thorough, single-source answers)

### Technical Optimization for AI Search
- [ ] Implement FAQ schema for question-answer content
- [ ] Implement HowTo schema for procedural content
- [ ] Use descriptive, semantic HTML (proper heading hierarchy, `<article>`, `<section>`)
- [ ] Ensure fast page loading (AI crawlers prioritize accessible content)
- [ ] Allow AI crawlers in robots.txt (do NOT block GPTBot, Anthropic-ai, PerplexityBot, Google-Extended unless intentional)
- [ ] Include author credentials and expertise signals (E-E-A-T)
- [ ] Keep content up to date (AI systems weight freshness)

### AI Crawler Robots.txt Reference
```
# Allow AI crawlers (default: allowed if not blocked)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: ClaudeBot
Allow: /

# To block specific AI crawlers:
# User-agent: GPTBot
# Disallow: /
```

### Content Patterns That Get Cited by AI
1. **Definition + Context**: "X is [clear definition]. It is used for [context]. For example, [example]."
2. **Comparison tables**: AI loves structured comparisons for "X vs Y" queries
3. **Numbered step-by-step**: "To do X: 1. [step], 2. [step], 3. [step]"
4. **Data-backed claims**: "According to [source], X is Y% more effective than Z."
5. **Pros and cons lists**: Balanced assessments get cited for evaluation queries
6. **Direct answers followed by depth**: Answer first, explain after

### AI Overview Trigger Queries
AI Overviews are most likely to appear for:
- Informational queries ("What is...", "How to...", "Why does...")
- Comparison queries ("X vs Y", "Best X for Y")
- Definition queries ("Define...", "[Term] meaning")
- Process queries ("Steps to...", "How do I...")
- Recommendation queries ("Best...", "Top...")

### Monitoring AI Visibility
- **Google Search Console**: Track impressions/clicks for queries with AI Overviews
- **Perplexity**: Search your target queries to see if you are cited
- **ChatGPT / Claude**: Ask about your topic areas and see if your brand is mentioned
- **Otterly.ai**: Automated AI citation monitoring (third-party tool)
- **Profound**: AI search analytics platform
- **Manual spot-checks**: Weekly search for 10-20 key queries across AI platforms
