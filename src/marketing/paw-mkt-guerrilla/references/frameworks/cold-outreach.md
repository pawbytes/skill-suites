# Cold Outreach at Scale

### Goal
Generate qualified leads through personalized cold outreach at scale, achieving 5%+ reply rates.

### Prerequisites
- Clear ICP (Ideal Customer Profile) definition.
- Value proposition that solves a specific, urgent problem.
- Email infrastructure: warmed sending domains, proper SPF/DKIM/DMARC configuration.
- Data enrichment tools (Apollo, Clearbit, LinkedIn Sales Navigator).
- AI personalization capability (Claude, GPT-4, or dedicated AI SDR tool).

### Step 1: Build Your Prospect List

1. Define your ICP: company size, industry, role, technology, funding stage, geography.
2. Build a list of 500-2,000 prospects using LinkedIn Sales Navigator, Apollo, or similar.
3. Enrich each prospect with: company news, recent LinkedIn posts, tech stack, hiring activity, funding events.
4. Segment the list into 3-5 sub-segments based on likely pain points.

### Step 2: Craft Personalization Layers

**Layer 1 (Minimum)**: Company + role context.
**Layer 2 (Good)**: Recent company news or prospect's LinkedIn activity.
**Layer 3 (Great)**: Specific pain point inferred from job postings, reviews, or public statements.
**Layer 4 (Best)**: Mutual connections, shared experiences, or specific content the prospect created.

Use AI to generate personalized opening lines for each prospect:
```
Prompt: "Given the following prospect data [data], write a personalized
opening line that references something specific about their situation.
Do not use generic phrases like 'I noticed you work at.' Be specific
and genuine. Maximum 2 sentences."
```

**Human review**: Spot-check 10-20% of AI-generated personalization. AI hallucinates 3-8% of the time (references nonexistent roles, incorrect company details).

### Step 3: Write the Sequence

**Email 1 (Day 1) -- Value-First**:
```
Subject: [Specific, relevant question -- 4-7 words]

[Personalized opening line referencing their specific context]

[1-2 sentences connecting their situation to a problem you solve]

[Value offer: a resource, insight, or tool -- NOT a demo request]

[Soft CTA: "Would it be useful if I shared [resource]?"]
```

**Email 2 (Day 4) -- Follow-Up with Value**:
```
Subject: Re: [original subject]

[Reference to Email 1 briefly]

[New value: a case study, data point, or insight relevant to their specific situation]

[Slightly stronger CTA: "Would a 15-minute call to discuss [specific topic] be worth your time?"]
```

**Email 3 (Day 8) -- Social Proof**:
```
Subject: Re: [original subject]

[Brief reference to previous emails]

[Social proof: "We helped [similar company] achieve [specific result]"]

[Direct CTA: "I'd love to show you how. Any time work this week?"]
```

**Email 4 (Day 14) -- Breakup**:
```
Subject: Re: [original subject]

[Acknowledge you have not heard back -- no guilt]

[One final value statement]

[Respectful close: "If timing isn't right, no worries. I'll follow your work and reach out if something changes."]
```

### Step 4: Multi-Channel Touchpoints

Between emails, add LinkedIn touchpoints:
- Day 2: Send LinkedIn connection request with a personalized note (not a pitch).
- Day 6: Like or comment on their recent LinkedIn post with a genuine, substantive comment.
- Day 10: Share a relevant article or resource via LinkedIn DM (only if connected).

### Step 5: Optimize and Iterate

- Track open rates, reply rates, and positive reply rates per segment.
- A/B test subject lines (send 50 with version A, 50 with version B).
- A/B test opening lines, CTAs, and value offers.
- Drop segments or approaches with reply rates below 2% after 200+ sends.
- Double down on segments or approaches with reply rates above 5%.

### Benchmarks (2026)
- Generic cold email: <1% reply rate.
- Basic personalization (name + company): 2-4% reply rate.
- AI-personalized with 2+ layers: 4-12% reply rate.
- Hyper-personalized with 3+ layers: 15-42% reply rate.
