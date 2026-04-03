# Persona Construction

## Purpose

Build practical, actionable buyer and user profiles that go beyond demographics to reveal motivations, pains, and buying logic.

## When to Use

- User asks "who would buy this?"
- Need to define target audience for a product
- Segmenting broad audiences into specific personas
- Creating messaging targets
- Preparing for marketing or sales

## Prerequisites

- Product context loaded from product-context.md
- Any existing audience data from audience-intelligence.md

## Method

### Step 1: Identify Segments

Start with broad categories, then narrow:

1. **List potential segments** based on product type and market:
   - Who has the problem this product solves?
   - Who has money to pay for a solution?
   - Who has the authority to buy?

2. **Prioritize segments** by:
   - Size of opportunity
   - Accessibility
   - Alignment with product vision

3. **Select primary and secondary personas:**
   - Primary: The main buyer/user, highest value
   - Secondary: Influencers, champions, or adjacent users

### Step 2: Gather Signals

Sources for persona data:

| Source | What It Reveals |
|--------|-----------------|
| User interviews | Direct pain language, buying logic |
| Sales calls | Objections, questions, decision process |
| Support tickets | Frustrations, feature requests, use cases |
| Reviews of competitors | What they value, what they hate |
| Forum/Reddit discussions | Unfiltered language, common complaints |
| Social media | Interests, influences, communities |
| Market research reports | Demographic trends, market size |

**If research is thin:**
- Use logical inference from product context
- Mark assumptions clearly for future validation
- Offer to route to Research agent for deeper data

### Step 3: Build Persona Profile

Structure each persona document:

#### Header
- **Name:** Give them a memorable name (e.g., "Solo Sarah", "Enterprise Eric")
- **Role/Title:** Primary job function
- **Segment:** Primary/Secondary
- **Confidence:** Validated (research-backed) or Assumed (inferred)

#### Demographics (Table Stakes)
- Industry/vertical
- Company size
- Role seniority
- Age range (if relevant)
- Location (if relevant)

**Important:** Demographics alone don't create a persona. This is the baseline, not the insight.

#### Psychographics (The Real Insight)
- **Values:** What do they care about deeply?
- **Beliefs:** What do they believe about the world/their work?
- **Worldview:** How do they see their situation?
- **Identity:** How do they see themselves?

#### Pains (The Core)
- **Acute pains:** Urgent problems demanding immediate solutions
- **Chronic pains:** Persistent frustrations they've learned to live with
- **Aspirational pains:** Gaps between current and desired state

For each pain, capture:
- How it manifests in their daily work
- What they've tried to solve it
- Why existing solutions fall short

#### Desired Outcomes
- **Functional outcomes:** What they need to accomplish
- **Emotional outcomes:** How they want to feel
- **Social outcomes:** How they want to be perceived

Use outcome language: "I want to feel [emotion] when I [action] so that [result]."

#### Buying Logic
- **Decision process:** How do they evaluate options?
- **Decision criteria:** What factors matter most?
- **Influencers:** Who do they trust for advice?
- **Objections:** What fears or concerns arise?
- **Trigger events:** What prompts them to start looking?

#### Language Profile
- **Words they use:** Vocabulary specific to their role/industry
- **Metaphors that resonate:** Analogies that click
- **Words to avoid:** Jargon that alienates or terms that trigger skepticism

### Step 4: Validate or Flag Assumptions

For each persona element, note confidence level:

| Confidence | Meaning | Action |
|------------|---------|--------|
| Validated | Direct evidence from research | Use confidently |
| Inferred | Logical deduction from context | Use, but plan validation |
| Assumed | Best guess based on patterns | Flag for research |

### Step 5: Create Persona Summary

Condense each persona into a memorable summary:

**Format:**
> [Name] is a [role] at [company type] who [key characteristic]. They struggle with [primary pain] and want [desired outcome]. They decide based on [criteria] and fear [primary objection].

**Example:**
> Solo Sarah is an independent therapist transitioning from agency work to private practice. She struggles with the business side of therapy (billing, scheduling, client acquisition) and wants to feel confident running her practice without sacrificing client care. She decides based on peer recommendations and fears looking unprofessional or wasting money on tools she won't use.

## Output

### Files Created

1. **Primary Persona:** `{product-slug}/audience/personas/primary-persona.md`
2. **Secondary Personas:** `{product-slug}/audience/personas/secondary-personas.md` (if applicable)

### Memory Update

Update `curated/audience-intelligence.md`:
- Add persona summaries to Personas section
- Update Gaps & Assumptions table
- Log activity in daily file

## Quality Checklist

Before finalizing persona:

- [ ] Goes beyond demographics to psychographics
- [ ] Includes specific pains, not just general needs
- [ ] Captures emotional drivers, not just functional
- [ ] Documents buying logic and objections
- [ ] Uses language the audience would recognize
- [ ] Flags assumptions for validation
- [ ] Memorable enough to guide product decisions

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| "Small business owners" | "Solo therapists in private practice" |
| "Wants to save time" | "Dreads Sunday nights because of billing" |
| "Price-sensitive" | "Has $50/month budget and needs to justify to spouse" |
| "Tech-savvy" | "Uses iPhone, Chrome, and gets nervous about API integrations" |
| Listing features they want | Describing outcomes they seek |

## Handoff

When persona construction is complete:
- **Route to Strategist** if ready for product definition
- **Route to Research** if personas need validation with market data
- **Continue with Problem Discovery** to deepen pain mapping