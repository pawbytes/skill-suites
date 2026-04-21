# Trigger Phrases

How trigger phrases work for skill discovery and activation. This document explains the trigger phrase system and best practices for writing effective triggers.

---

## How Triggers Work

Trigger phrases are keywords and phrases included in a skill's `description` frontmatter. When a user's request matches a trigger, the skill system can discover and activate the appropriate skill.

### Discovery Flow

```
User Request: "I need an SEO audit"
        |
        v
Skill System searches description fields
        |
        v
Matches trigger: "SEO" in paw-mkt-seo
        |
        v
Activates paw-mkt-seo skill
```

### Where Triggers Live

Triggers are embedded in the YAML frontmatter of `SKILL.md`:

```yaml
---
name: paw-mkt-seo
description: SEO specialist for technical audits, keyword strategy, local SEO, link building, pSEO, and GEO optimization. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability', 'pSEO', 'GEO', 'search rankings', 'link building'.
---
```

---

## Trigger Phrase Format

### Description Structure

The `description` field should:

1. Start with a brief capability statement
2. Include trigger phrases at the end
3. Use clear delimiter: `Triggers:` or `Use when:`

**Format:**
```
{Capability summary}. {Trigger indicator}: '{phrase1}', '{phrase2}', '{phrase3}'.
```

### Examples by Skill Type

**Agent Skill (Coordinator):**
```yaml
description: Creative director who orchestrates the Aria Creative Suite. Use when the user asks for Aria, wants creative direction, campaign planning, brand setup, or doesn't know which specialist to call.
```

**Agent Skill (Specialist):**
```yaml
description: Visual production expert for production-ready social posts, carousels, flyers, brand assets, and code-based templates. Trigger when user requests 'create social post', 'design carousel', 'make flyer', 'generate logo', 'resize image', or 'create template'.
```

**Workflow Skill:**
```yaml
description: Short-form video pipeline for Reels, TikTok, and Shorts. Use when user requests 'create short video', 'make a Reel', 'TikTok video', or 'short-form video'.
```

**Utility Skill:**
```yaml
description: Automates software releases from version bump to GitHub release. Use when the user requests to 'create a release', 'cut a release', 'publish a new version', or 'prepare a release'.
```

---

## Best Practices

### 1. Use User-Friendly Phrases

Write phrases that users would naturally say, not technical jargon.

**Good:**
```yaml
description: SEO specialist. Triggers: 'SEO', 'keyword research', 'rank higher', 'Google search'.
```

**Bad:**
```yaml
description: SEO specialist. Triggers: 'SERP optimization', 'algorithmic search enhancement'.
```

### 2. Cover All Entry Points

Include triggers for:
- What the user wants (outcome)
- What the user might ask for (deliverable)
- Domain terminology (keywords)
- Common variations

**Example:**
```yaml
description: Email marketing specialist. Triggers: 'email campaign', 'newsletter', 'email sequence', 'drip campaign', 'email automation', 'welcome series'.
```

### 3. Be Specific Enough

Avoid overly broad triggers that could match multiple skills.

**Too broad:**
```yaml
description: Marketing skill. Triggers: 'marketing'.
```

**Better:**
```yaml
description: SEO specialist for search optimization. Triggers: 'SEO', 'search rankings', 'keyword research', 'technical audit', 'schema markup'.
```

### 4. Use Consistent Delimiters

Choose one format and use it consistently:

- `Triggers: 'phrase1', 'phrase2'`
- `Use when user says 'phrase1', 'phrase2'`
- `Trigger when user requests 'phrase1', 'phrase2'`

### 5. Include Natural Variations

Users phrase things differently. Include common variations:

**Example:**
```yaml
description: Short-form video pipeline. Use when user requests 'create short video', 'make a Reel', 'TikTok video', 'short-form video', 'vertical video', '9:16 video'.
```

---

## Trigger Categories

### Outcome-Based Triggers

Focus on what the user wants to achieve:

```yaml
description: CRO specialist. Triggers: 'increase conversions', 'improve conversion rate', 'optimize landing page', 'A/B test'.
```

### Deliverable-Based Triggers

Focus on what the user wants produced:

```yaml
description: Presentation generator. Triggers: 'create presentation', 'build a deck', 'generate slides', 'make slides', 'create report'.
```

### Domain-Based Triggers

Focus on the domain or specialty:

```yaml
description: PR specialist. Triggers: 'PR', 'press release', 'media coverage', 'journalist', 'public relations'.
```

### Action-Based Triggers

Focus on the action the user wants to take:

```yaml
description: Release automation. Triggers: 'create a release', 'cut a release', 'publish version', 'ship release'.
```

---

## Trigger Examples from Existing Skills

### Marketing Module

| Skill | Trigger Phrases |
|-------|-----------------|
| `paw-mkt-agent-agency` | `marketing plan`, `brand strategy`, `campaign management`, `SOSTAC`, `ambiguous marketing requests` |
| `paw-mkt-seo` | `SEO`, `keyword research`, `schema markup`, `crawlability`, `pSEO`, `GEO`, `search rankings`, `link building` |
| `paw-mkt-content` | `content strategy`, `editorial calendar`, `blog post`, `content plan` |
| `paw-mkt-email` | `email campaign`, `newsletter`, `email sequence`, `drip campaign` |
| `paw-mkt-social` | `social media`, `social strategy`, `community management`, `social posts` |
| `paw-mkt-paid-ads` | `PPC`, `paid ads`, `Google Ads`, `Meta Ads`, `retargeting` |
| `paw-mkt-launch` | `product launch`, `GTM`, `go-to-market`, `Product Hunt` |
| `paw-mkt-analytics` | `analytics`, `tracking`, `dashboards`, `metrics`, `reporting` |

### Creative Module

| Skill | Trigger Phrases |
|-------|-----------------|
| `paw-cra-agent-creative-director` | `Aria`, `creative direction`, `campaign planning`, `brand setup` |
| `paw-cra-agent-designer` | `create social post`, `design carousel`, `make flyer`, `generate logo`, `resize image`, `create template` |
| `paw-cra-agent-video-producer` | `video production`, `create video`, `video edit`, `motion graphics` |
| `paw-cra-video-shortform` | `create short video`, `make a Reel`, `TikTok video`, `short-form video` |
| `paw-cra-video-longform` | `YouTube video`, `long-form video`, `webinar`, `tutorial video` |
| `paw-cra-design-social` | `social post design`, `Instagram post`, `carousel design` |
| `paw-cra-quality-control` | `quality check`, `QC`, `review campaign`, `final check` |

### Tools Module

| Skill | Trigger Phrases |
|-------|-----------------|
| `paw-tools-release` | `create a release`, `cut a release`, `publish a new version`, `prepare a release` |
| `paw-tools-presentation` | `create a presentation`, `generate a report`, `build a deck` |
| `paw-tools-setup` | `install tools module`, `configure Pawbytes Tools`, `setup tools` |

---

## Coordinator vs Specialist Triggers

### Coordinator Triggers

Coordinator skills (agency, creative-director) have broader triggers that capture ambiguous requests:

```yaml
---
name: paw-mkt-agent-agency
description: "Multi-channel marketing coordination. Use when marketing plan, brand strategy, campaign management, SOSTAC, ambiguous marketing requests."
---
```

```yaml
---
name: paw-cra-agent-creative-director
description: Creative director who orchestrates the Aria Creative Suite. Use when the user asks for Aria, wants creative direction, campaign planning, brand setup, or doesn't know which specialist to call.
---
```

### Specialist Triggers

Specialist skills have specific triggers for their domain:

```yaml
---
name: paw-mkt-seo
description: SEO specialist for technical audits, keyword strategy, local SEO, link building, pSEO, and GEO optimization. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability', 'pSEO', 'GEO', 'search rankings', 'link building'.
---
```

The coordinator routes to specialists when the request matches a specific domain.

---

## Writing Effective Triggers

### Checklist

- [ ] Phrases are what users would naturally say
- [ ] Covers the main use cases for the skill
- [ ] Includes common variations and synonyms
- [ ] Not too broad (matches only this skill's domain)
- [ ] Not too narrow (misses common requests)
- [ ] Uses consistent delimiter format
- [ ] Includes both outcome and deliverable triggers

### Process

1. **List user requests** - Write down all the ways users might ask for this skill
2. **Group by category** - Outcome, deliverable, domain, action
3. **Select top phrases** - 5-10 most common/representative phrases
4. **Write description** - Combine capability summary with trigger phrases
5. **Test mentally** - Would this phrase match my skill? Would it incorrectly match other skills?

---

## Common Mistakes

### Mistake 1: Too Generic

```yaml
description: Marketing tool. Triggers: 'marketing'.
```

**Problem:** Matches every marketing request, no specificity.

**Fix:** Add domain-specific triggers:
```yaml
description: SEO specialist for search optimization. Triggers: 'SEO', 'keyword research', 'technical audit', 'search rankings'.
```

### Mistake 2: Missing Common Phrases

```yaml
description: Email specialist. Triggers: 'email automation'.
```

**Problem:** Misses users who say "newsletter" or "drip campaign".

**Fix:** Include variations:
```yaml
description: Email marketing specialist. Triggers: 'email campaign', 'newsletter', 'email sequence', 'drip campaign', 'email automation'.
```

### Mistake 3: Technical Jargon

```yaml
description: CRO specialist. Triggers: 'conversion rate optimization', 'CRO methodology'.
```

**Problem:** Users don't say "CRO methodology".

**Fix:** Use user-friendly phrases:
```yaml
description: CRO specialist. Triggers: 'increase conversions', 'improve conversion rate', 'optimize landing page', 'A/B test', 'CRO'.
```

### Mistake 4: Inconsistent Format

```yaml
description: Video creation for short-form content. You can say 'TikTok', or maybe 'Reels' or 'shorts'.
```

**Problem:** Inconsistent, hard to parse.

**Fix:** Use consistent delimiter:
```yaml
description: Short-form video pipeline. Use when user requests 'create short video', 'make a Reel', 'TikTok video', 'short-form video'.
```

---

## Trigger Testing

To test if your triggers are effective:

1. **Role-play user requests** - "I want to rank higher on Google" -> Should match `paw-mkt-seo`
2. **Check for overlaps** - Does "create video" match both shortform and longform? (Intentional overlap is OK)
3. **Verify coordinator fallback** - Ambiguous requests should match coordinator
4. **Confirm specificity** - Specific requests should match specialist, not just coordinator

---

## Summary

| Aspect | Guideline |
|--------|-----------|
| **Location** | YAML frontmatter `description` field |
| **Format** | `{Capability}. {Trigger indicator}: '{phrase1}', '{phrase2}'.` |
| **Quantity** | 5-10 phrases (not exhaustive, representative) |
| **Style** | User-friendly, natural language |
| **Categories** | Outcome, deliverable, domain, action |
| **Consistency** | Use same delimiter format across all skills |

Effective triggers balance specificity with discoverability - they should match the right requests without being so narrow that users can't find the skill.