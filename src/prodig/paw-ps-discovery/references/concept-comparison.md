# Concept Comparison

Compare multiple product directions to help users decide which to pursue.

## When to Use

- User has 2-5 viable concepts and can't choose
- User wants to see trade-offs between directions
- User needs help articulating why one feels better
- Decision paralysis between good options

## Input

Gather from conversation:
- The concepts to compare (should already be somewhat shaped)
- User's goals and constraints
- What the user has said about each concept
- Any existing preferences or leanings

## Comparison Process

### Step 1: Clarify Each Concept

Ensure each concept is concrete enough to compare:

```markdown
## Concept A: [Name]
- **Core premise:** [One sentence]
- **Format:** [Course/template/tool/service]
- **Audience:** [Target]
- **Key differentiator:** [What makes it unique]
```

Repeat for each concept.

### Step 2: Identify Comparison Dimensions

Choose relevant comparison axes:

| Dimension | When Relevant |
|-----------|---------------|
| **Market size** | User cares about scale |
| **Effort to build** | User has time constraints |
| **Uniqueness** | User wants differentiation |
| **Personal fit** | User's skills/interests matter |
| **Revenue potential** | User has income goals |
| **Time to market** | User wants speed |
| **Passion factor** | User cares about enjoyment |
| **Audience access** | User has existing audience |
| **Validation ease** | User wants to test quickly |

Select 4-6 dimensions that matter most to this user.

### Step 3: Map Each Concept

Score or describe each concept on each dimension:

```markdown
## Comparison Matrix

| Dimension | Concept A | Concept B | Concept C |
|-----------|-----------|-----------|-----------|
| Market size | Large (broad appeal) | Medium (niche) | Small (micro-niche) |
| Build effort | High (comprehensive) | Medium (focused) | Low (MVP-friendly) |
| Uniqueness | Medium (crowded space) | High (fresh angle) | High (novel approach) |
| Personal fit | High (expertise) | Medium (interest) | Low (learning curve) |
| Time to market | Long (6+ months) | Medium (3 months) | Short (4 weeks) |

## Quick Take
- **Concept A** = Big swing, bigger investment
- **Concept B** = Balanced risk/reward
- **Concept C** = Fast test, smaller upside
```

### Step 4: Reveal Trade-offs

Highlight the real choices:

```markdown
## Trade-off Summary

**If you choose Concept A:**
- You're betting on scale and comprehensive value
- You'll need 6+ months and significant effort
- The market is proven but competitive
- You have the expertise to stand out

**If you choose Concept B:**
- You're balancing uniqueness with accessibility
- 3 months to launch feels achievable
- Less crowded but smaller initial audience
- Good fit for your interests

**If you choose Concept C:**
- You're prioritizing speed and learning
- Fast validation of the core idea
- Lower risk but smaller potential upside
- Good for testing the waters
```

### Step 5: Surface User Preferences

Help the user articulate what matters:

- "Looking at these trade-offs, which dimension matters most to you right now?"
- "If you could only have two of these benefits, which would you choose?"
- "What would you regret not trying?"

## Output

Create a comparison document:

```markdown
# Concept Comparison: [Topic]

## Concepts Overview
[Brief description of each concept being compared]

## Comparison Matrix
[Dimension-by-dimension analysis]

## Trade-off Summary
[What each choice means in practice]

## User Preference Signals
- [What the user has indicated they value]
- [Any constraints or non-negotiables]

## Recommendation
Based on [preferences], **Concept [X]** appears to best match your goals because [reason]. However, if [condition], then Concept [Y] might be worth considering.

## Next Steps
- [ ] Validate Concept [X] with research
- [ ] Explore hybrid possibilities
- [ ] Run quick experiments for top 2
```

## Quality Standard

Comparison is complete when:
- [ ] Each concept clearly described
- [ ] 4-6 relevant dimensions compared
- [ ] Trade-offs made explicit
- [ ] User has expressed a preference or narrowing
- [ ] Next step identified (validate, hybridize, or decide)

## Example Dialogue

**User:** "I have three ideas and I can't decide which to pursue."

**Discovery Agent:** "Let's lay them out side by side. Can you give me a quick sentence on each?"

[User describes]

**Discovery Agent:** "Great. Let me map these on the dimensions that usually matter — market size, effort, uniqueness, and how well each fits you..."

[Creates matrix]

"Now the trade-offs become clear. Concept A is your big swing, B is the balanced play, and C is your quick test. What matters most to you right now — scale, speed, or uniqueness?"

## Decision Frameworks

When comparison alone doesn't create clarity:

| Framework | Best For |
|-----------|----------|
| **Elimination by constraint** | Remove options that violate non-negotiables |
| **Regret minimization** | "Which would you regret not doing?" |
| **Timeline thinking** | "Where do you want to be in 6 months?" |
| **Energy check** | "Which one energizes you most when you think about working on it?" |
| **Coin flip test** | "Flip a coin for each pair — what do you hope it lands on?" |

## Completion Trigger

When the user expresses a clear preference:
- Confirm the choice
- Ask: "Ready to validate this direction, or want to explore hybrid possibilities?"
- Route to research or strategist