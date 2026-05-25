# Customer Motivation Map: DDFF

DDFF captures the customer motivation layer that downstream specialists use for copy, offers, campaigns, and sales messaging. Treat it as evidence-informed positioning input, not invented persona fiction.

## DDFF Fields

| Field | What to Capture | Useful Evidence |
|-------|-----------------|-----------------|
| Desires | The concrete outcomes, wins, or states they actively want | Feature requests, purchase triggers, success metrics, jobs-to-be-done |
| Dreams | The bigger future the customer hopes to reach | Aspirational interview quotes, transformation language, long-term goals |
| Fears | The risks, losses, embarrassment, or regret they want to avoid | Objections, churn reasons, sales hesitations, review complaints |
| Frustrations | The repeated irritations and blockers in their current reality | Support tickets, Reddit/G2 complaints, workflow pain, manual workarounds |

## Confidence Labels

Use confidence labels when the evidence is uneven:

- **High**: repeated across multiple sources or segments
- **Medium**: appears in some evidence but needs more validation
- **Low**: plausible hypothesis that should be tested before heavy use

## Recommended Output Format

Use this format inside `paw-mkt-product-context.md`:

```markdown
## Customer Motivation Map: DDFF

### Desires

- [Concrete outcome they are pursuing]

### Dreams

- [Future state they want, with quote or evidence]

### Fears

- [Risk, loss, embarrassment, or regret they want to avoid]

### Frustrations

- [Current pain, blocker, or recurring irritation]

### Highest-Leverage Motivation

**Primary emotional driver:** [desire/dream/fear/frustration]
**Evidence:** [quote, source, pattern, or confidence level]
**Messaging implication:** [how specialists should use this]
```

## Audience Pain Research Workflow

Use this workflow before finalizing DDFF when the audience is under-researched or the product context needs deeper pain, motivation, and customer-language inputs. Adapt the prompts to the target segment, geography, and category.

| Step | Research Focus | Feeds Into |
|------|----------------|------------|
| 1 | Physical pain points and daily routine struggles | Frustrations, Fears |
| 2 | Emotional and mental pain points | Fears, Frustrations, limbic inputs |
| 3 | Financial pain points and opportunity costs | Fears, Frustrations, reptilian inputs |
| 4 | Social and community pain points | Fears, Desires, limbic inputs |
| 5 | Information overload and conflicting advice | Frustrations, Fears |
| 6 | Aspirations and hidden desires | Desires, Dreams |
| 7 | Synthesis into target audience profile | Persona, DDFF map, customer language, hot-button map |

Final synthesis prompt:

```text
Merge all research above into a comprehensive target audience profile. Identify the top 3 deepest pain points, their emotional triggers, and the exact language customers use to describe their struggles.
```

## Example: Parents Of Toddlers In Urban Indonesia

```text
Step 1: Research the top physical and daily routine struggles parents face when raising toddlers aged 1-3. Focus on sleep deprivation, feeding difficulties, and physical exhaustion.

Step 2: Research the emotional and psychological burdens of parenting toddlers. Include mom guilt, identity loss, anxiety, and relationship strain with partner.

Step 3: Research financial pressures specific to parents with toddlers in Indonesia. Include daycare costs, formula, healthcare, and opportunity cost of career breaks.

Step 4: Research the social isolation and support system gaps experienced by young parents with toddlers, especially in urban Indonesia.

Step 5: Research how parents with toddlers are overwhelmed by conflicting parenting advice from doctors, social media, family, and AI tools.

Step 6: Research what parents with toddlers secretly wish for -- not just problems, but dreams, identity, and what they want to become.

Final synthesis: Merge all research above into a comprehensive target audience profile. Identify the top 3 deepest pain points, their emotional triggers, and the exact language they use to describe their struggles.
```
