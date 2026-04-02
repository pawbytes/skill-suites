# Stage 1: Brief Intake

## Purpose

Capture the user's initial idea, audience context, and goals. Create the foundation for discovery research.

## Duration

5-10 minutes of conversation

## Process

### 1. Welcome and Context Setting

Open with a warm, guided introduction:

> "Let's create your webinar together. We'll work through this in stages: first I'll understand your idea, then we'll research and find the right angle, and finally we'll produce your slide deck outline and script. You're in Stage 1 of 4."

### 2. Topic Capture

Ask the core question:

> "What's the webinar about? Give me your initial idea — it's okay if it's vague or rough."

Listen for:
- Topic area
- Initial angle or perspective
- What excites them about it
- Why they want to do this webinar

### 3. Audience Context

Probe for audience understanding:

> "Who's this webinar for? Tell me about your target audience."

Capture:
- Job titles or roles
- Company size or industry if relevant
- Their current challenges or goals
- What they already know about this topic
- What they need to learn

### 4. Goals and Outcomes

Understand success criteria:

> "What do you want attendees to walk away with? What's the outcome you're aiming for?"

Listen for:
- Knowledge outcomes (learn X, understand Y)
- Action outcomes (be able to do Z)
- Business outcomes (generate leads, establish authority)
- Personal/professional outcomes (build reputation, share expertise)

### 5. Timeline and Constraints

Check for practical constraints:

> "Any timeline I should know about? When are you planning to present this?"

Note:
- Target presentation date
- Webinar length expectations
- Any hard deadlines or events tied to this

### 6. User Expertise Assessment

Understand what the user brings:

> "What's your background with this topic? Do you have existing content, case studies, or unique experiences we should incorporate?"

Capture:
- Their expertise level
- Existing content that could be leveraged
- Unique perspectives or experiences
- Credibility markers (credentials, projects, results)

### 7. Generate Webinar Slug

Create a filesystem-safe identifier from the topic:

1. Extract key words from the topic (remove stop words: a, an, the, for, to, etc.)
2. Normalize unicode (NFKD decomposition)
3. Convert to lowercase
4. Remove diacritics and special characters
5. Replace whitespace and non-alphanumeric characters with hyphens
6. Collapse consecutive hyphens into single hyphen
7. Trim leading and trailing hyphens
8. Truncate base to 41 characters maximum (leaving room for `-webinar` suffix)
9. Append `-webinar` suffix
10. If result is empty, use `untitled-webinar`
11. Ensure uniqueness by checking for existing directories (append `-2`, `-3`, etc. if needed)

**Examples:**
- "Email Automation 101" → `email-automation-101-webinar`
- "AI/ML for Business: What's Next?" → `ai-ml-for-business-whats-next-webinar`
- "How to Build a Personal Brand on LinkedIn" → `build-personal-brand-on-linkedin-webinar`

### 8. Create Brief File

Write `brief.md` to `{webinar-slug}/brief.md`:

```markdown
# Webinar Brief: [Topic]

## Overview
[User's initial idea - 2-3 sentences in their words]

## Target Audience
- **Who:** [Job titles, roles, company types]
- **Current state:** [What they know now, their challenges]
- **Desired state:** [What they need to learn or be able to do]

## Goals
- [Primary goal]
- [Secondary goal if applicable]
- [Business outcome if relevant]

## Timeline
- **Target date:** [Date or timeframe]
- **Expected length:** [Duration]

## User Expertise
- **Background:** [Their credentials/experience with topic]
- **Existing content:** [Blog posts, videos, case studies mentioned]
- **Unique angle:** [Their distinctive perspective or experience]

## Constraints
- [Any technical, time, or resource constraints]

## Status
- [ ] Brief captured
- [ ] Discovery phase pending
- [ ] Production phase pending
- [ ] Complete
```

### 9. Create Workspace Structure

Initialize the webinar workspace:

```text
.pawbytes/webinar-suites/webinars/{webinar-slug}/
├── brief.md          # Just created
```

### 10. Confirm and Gate

Summarize and get confirmation:

> "Here's what I've captured:
> 
> **Topic:** [topic]
> **Audience:** [audience summary]
> **Goal:** [primary goal]
> 
> I've saved this to your webinar workspace. Next, we'll move into the Discovery phase where I'll research your topic, find the right angle, and identify the hook that will make your webinar compelling.
> 
> Ready to start discovery? (yes / I need to adjust something first)"

## Progression Criteria

Move to Stage 2 when:
- Brief is captured with topic, audience, and goals
- `brief.md` is saved
- User confirms readiness to proceed

## Output

| Output | Location |
|--------|----------|
| Brief file | `{webinar-slug}/brief.md` |
| Workspace structure | `{webinar-slug}/` directory |
| Webinar slug | Generated identifier |

## Handling Edge Cases

### User Has Existing Brief

If user says "I have a brief already":

1. Ask them to share it (paste or file path)
2. Review for completeness
3. Fill any gaps through follow-up questions
4. Save to `brief.md`

### User Is Unsure About Topic

If the topic is genuinely vague:

1. Offer a quick exploration: "Let me ask a few questions to help clarify..."
2. Probe: "What's the problem you're solving?" or "What's the change you want to create?"
3. Reflect back what you hear
4. Help them articulate it more clearly

### User Wants Multiple Webinars

If the scope seems too large:

1. Flag it: "This sounds like it could be a series. Let's focus on one webinar first."
2. Help them choose: "Which aspect is most important to cover first?"
3. Note the series potential for future sessions