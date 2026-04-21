# Stage Diagnosis

## Purpose

Determine where the user is in the product creation journey to provide appropriate routing and recommendations.

## The Product Journey

```
┌────────────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐
│ Discovery  │ → │ Research │ → │ Audience │ → │ Strategy  │
│            │   │          │   │          │   │           │
│ Ideation   │   │ Market   │   │ Customer │   │ Product   │
│ Expansion  │   │ Analysis │   │ Insight  │   │ Definition│
└────────────┘   └──────────┘   └──────────┘   └───────────┘
                                              ↓
┌────────────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐
│ Readiness  │ ← │ Packaging│ ← │ Execution│ ← │ Synthesis │
│            │   │          │   │          │   │           │
│ Quality    │   │ Bundle   │   │ Build    │   │ Plan      │
│ Review     │   │ Assembly │   │ Artifacts│   │ Creation  │
└────────────┘   └──────────┘   └──────────┘   └───────────┘
```

## Diagnosis Process

### 1. Check Existing Context

Read sidecar files to understand current state:

| File | Indicates Stage |
|------|-----------------|
| No product-context.md | Pre-discovery (new user) |
| product-context.md has idea only | Discovery |
| market-intelligence.md populated | Research complete |
| audience-intelligence.md populated | Audience complete |
| product-decisions.md has brief | Strategy in progress |
| Artifacts generated | Execution phase |
| Package bundle exists | Packaging phase |

### 2. Ask Diagnostic Questions

If context is unclear, ask 1-3 targeted questions:

**Discovery stage detection:**
- "Do you have a specific product idea, or are you exploring possibilities?"
- "Have you validated this concept with any research?"

**Research stage detection:**
- "Have you looked at competitors or market demand?"
- "Do you know who else is solving this problem?"

**Audience stage detection:**
- "Do you know who your ideal customer is?"
- "Have you mapped their pain points and desired outcomes?"

**Strategy stage detection:**
- "Do you have a product brief or feature list?"
- "Have you decided on scope for version 1?"

**Execution stage detection:**
- "Do you have production-ready artifacts?"
- "What format is your product in?"

### 3. Stage Classification

| Stage | Characteristics | Missing |
|-------|-----------------|---------|
| **Pre-discovery** | No product-context.md | Everything |
| **Discovery** | Idea captured, no validation | Research, audience |
| **Research** | Market analysis done | Audience, strategy |
| **Audience** | Customer profiles done | Strategy |
| **Strategy** | Product brief complete | Execution artifacts |
| **Execution** | Artifacts being built | Packaging |
| **Packaging** | Bundle assembled | Readiness review |
| **Readiness** | Quality verified | Launch (out of scope) |

## Stage-Specific Responses

### Pre-Discovery

"I see you're new to Prodig Suites. Let's start by capturing your product idea. What kind of digital product are you thinking about — a course, template pack, software tool, or service package?"

### Discovery

"Your idea for '{product}' is captured. The next step is to validate this direction. I recommend either:
1. **Discovery** — expand and refine the concept further
2. **Research** — analyze the market and competitors

Which feels right?"

### Research

"You've completed market research for '{product}'. I found:
- {X} competitors analyzed
- Key gaps identified: {gaps}

Next step: **Audience discovery** to understand who you're serving. Ready to proceed?"

### Audience

"Your audience profile for '{product}' is clear:
- Primary persona: {persona}
- Key pain points: {pains}

Next step: **Strategy** to define your product scope and packaging. Shall I route to the strategist?"

### Strategy

"Your product brief is ready:
- Product type: {type}
- Scope: {scope}
- Target: {audience}

Next step: **Execution** — I'll route you to the {type}-executor. Ready to build?"

### Execution

"Building '{product}' — current artifacts:
- {artifact 1}: {status}
- {artifact 2}: {status}

Continue with executor, or check progress?"

### Packaging

"Your product artifacts are ready for packaging. I'll assemble the final bundle and prepare for readiness review."

### Readiness

"Your product has passed readiness review. It's {status} — ready for your next steps (marketing, launch, etc. are outside Prodig Suites scope)."

## Edge Cases

### User Wants to Skip Stages

"I understand you want to move faster. Here's what you'd miss by skipping {stage}:
- {missing insight 1}
- {missing insight 2}

You can proceed, but I recommend at least a quick {minimal action} first. Your choice?"

### User Returns to Earlier Stage

"Welcome back. I see '{product}' was at {old stage}. You want to revisit {new stage}. Let me load that context and we can refine from there."

### Multiple Products

"You have {N} products in progress:
1. {product 1} — {stage}
2. {product 2} — {stage}

Which would you like to continue, or shall we start something new?"