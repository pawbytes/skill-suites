# Launch Type Assessment

Before building any plan, determine the launch type. The type drives the scope of resources, content, and channel activation required.

## Launch Category

| Category | Description | Examples | Full ORB Activation? |
|---|---|---|---|
| New Product | First public release of an entirely new product | v1.0, new SaaS tool, new physical product | Yes — full treatment |
| Major Feature | Significant capability that expands the product's value proposition | New pricing tier, API, core workflow change | Yes — full treatment |
| Minor Feature | Useful addition that improves existing workflows | New integration, UI improvement, new template | Partial — blog + email + social |
| Patch / Fix | Bug fixes, performance, security improvements | v1.1.3 hotfix | Minimal — changelog + tweet |
| Category Entry | Entering a new market or use-case segment | Expanding from SMB to enterprise, new vertical | Yes — full treatment + new positioning |
| Partnership | Joint launch with a partner brand | Comarketing, platform integration | Yes — coordinated cross-brand |

## Launch Tier Decision

Ask or confirm based on SOSTAC context:

- **Tier 1 (Major launch — full treatment)**: New product, major feature, category entry, or partnership. Full ORB channel activation, Product Hunt strategy, press outreach, launch content suite, phased timeline.
- **Tier 2 (Minor launch — scaled treatment)**: Monthly minor feature or improvement. Blog announcement, email to user base, 3-5 social posts. No press release, no Product Hunt.
- **Tier 3 (Patch cadence)**: Weekly or biweekly changelog update, one social post, in-app notification if relevant.

Key principle: The best companies do not just launch once. They launch again and again. Build a repeatable announcement cadence from day one, and reserve the full Tier 1 treatment for moments that earn it.

## Questions to Clarify

Before building the plan, confirm if not clear from SOSTAC files:

1. What is the specific product or feature being launched?
2. Is this a Tier 1, 2, or 3 launch?
3. What is the target launch date?
4. What channels does the brand currently own (email list size, social accounts, community)?
5. Is Product Hunt being considered? Does the brand have a support network that can vote?
6. Is there a PR / press budget or existing journalist relationships?
7. Are there any partners, influencers, or early users to activate?

## Research Mode: Launch Intelligence

Use agent-browser to research the competitive landscape, Product Hunt dynamics, and community conversation before finalizing launch strategy. Check `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md` for research already collected.

See `./references/shared-patterns.md` for agent-browser setup instructions.

### Product Hunt Research

```bash
# Product Hunt — top products in the category
agent-browser --session launch-research open "https://www.producthunt.com/topics/{category}" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: top products, vote counts, taglines, gallery approach, comment themes

# Product Hunt — recent launches in category (past 7 days)
agent-browser --session launch-research open "https://www.producthunt.com" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: positioning patterns, what hunters are commenting on, upvote leaders

# Top hunters by category
agent-browser --session launch-research open "https://www.producthunt.com/leaderboard/monthly" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: active hunters with high follower counts in relevant categories
```

### Competitor Launch Research

```bash
# Competitor blog — find recent launch announcements
agent-browser --session launch-research open "https://{competitor-domain}/blog" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: launch framing, feature messaging, timing patterns, calls to action

# Competitor social — LinkedIn recent posts
agent-browser --session launch-research open "https://www.linkedin.com/company/{competitor-slug}/posts/" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: announcement style, engagement counts, audience reaction

# Reddit — brand/category discussions
agent-browser --session launch-research open "https://www.reddit.com/search/?q={category+product+type}&sort=new" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: user language, pain points, how competitors are discussed, what people wish existed

# Indie Hackers — product launch milestones in category
agent-browser --session launch-research open "https://www.indiehackers.com/products?category={category}" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: revenue milestones, launch stories, what worked, community response
```

Close session when done: `agent-browser --session launch-research close`