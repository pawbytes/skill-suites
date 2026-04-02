# Part 7: Output Reference

## Chapter 22: Types of Deliverables

### 22.1 Strategic Documents

Strategic documents provide the foundation for all marketing activities. They're created during the planning phases and referenced throughout execution.

**SOSTAC Phase Documents**

| Document | Purpose | Typical Length |
|----------|---------|----------------|
| 01-situation.md | Market position, competitive analysis, SWOT | 2,000-4,000 words |
| 02-objectives.md | SMART goals, OKRs, KPIs | 1,500-2,500 words |
| 03-strategy.md | Positioning, segments, channels | 2,000-3,500 words |
| 04-tactics.md | Channel plans, campaigns, budget | 2,500-4,000 words |
| 05-action.md | Roadmap, RACI, timeline | 1,500-2,500 words |
| 06-control.md | Dashboards, metrics, review cadence | 1,500-2,500 words |

**Positioning Statements**
- Clear articulation of who, what, why, and how
- Used across all marketing materials
- Reference document for brand consistency

**Strategy Briefs**
- Campaign-specific strategic direction
- Audience, objectives, key messages
- Channel selection and rationale

### 22.2 Tactical Plans

Tactical plans translate strategy into actionable execution plans.

**Campaign Plans**
```
Campaign Brief Structure:
├── Campaign name and type
├── Objectives and KPIs
├── Target audience
├── Key messages
├── Channel mix
├── Budget allocation
├── Timeline
├── Creative requirements
└── Success metrics
```

**Content Calendars**
- 30/60/90-day planning horizons
- Platform-specific posting schedules
- Content themes mapped to funnel stages
- Publication dates and owners

**Channel Strategies**
- Platform-specific tactics
- Budget allocation
- Success metrics
- Optimization triggers

### 22.3 Ready-to-Use Content

Content that can be directly published or deployed.

**Blog Posts**
- SEO-optimized with target keywords
- Structured with H2/H3 hierarchy
- Include meta descriptions
- CTAs and internal links
- 1,500-3,000 words typical

**Email Sequences**
- Subject lines with A/B variants
- Body copy ready for ESP
- Timing and triggers defined
- CTAs and links
- 5-7 emails typical for welcome sequences

**Video Scripts**
- Platform-specific format
- Timecodes for each section
- Visual direction notes
- Hook and CTA defined
- Short-form: 60 seconds; Long-form: 8-15 minutes

**Ad Copy**
- Headlines (multiple variants)
- Primary text
- CTA options
- Audience targeting specs
- Creative direction

### 22.4 Implementation Guides

Technical specifications and step-by-step instructions.

**Technical Specs**
- Tracking code placement
- Schema markup (copy-paste ready)
- Integration configurations
- Platform setup instructions

**Step-by-Step Instructions**
- Numbered action items
- Screenshots where helpful
- Prerequisites noted
- Expected outcomes

**Checklists**
- Pre-launch checklists
- Audit checklists
- Optimization checklists
- Quality assurance

---

## Chapter 23: File Structure Reference

### 23.1 Complete Directory Map

```
brands/
├── {brand-slug}/
│   ├── brand-context.md           # Brand identity, voice, audience
│   ├── product-marketing-context.md # Deep positioning document
│   │
│   ├── sostac/                    # Strategic planning
│   │   ├── README.md              # Phase tracker
│   │   ├── 00-auto-discovery.md   # Research findings
│   │   ├── 01-situation.md
│   │   ├── 02-objectives.md
│   │   ├── 03-strategy.md
│   │   ├── 04-tactics.md
│   │   ├── 05-action.md
│   │   ├── 06-control.md
│   │   └── plan-summary.md
│   │
│   ├── campaigns/                 # Campaign-specific work
│   │   └── {type}-{campaign-slug}/
│   │       ├── strategy.md
│   │       ├── channels/
│   │       │   ├── blog/content/
│   │       │   ├── email/content/
│   │       │   ├── paid-ads/content/
│   │       │   ├── seo/content/
│   │       │   ├── social/content/
│   │       │   └── video/content/
│   │       └── launch/
│   │
│   ├── channels/                  # Evergreen/standalone work
│   │   ├── blog/content/
│   │   ├── email/content/
│   │   ├── paid-ads/content/
│   │   ├── seo/content/
│   │   ├── social/content/
│   │   └── video/content/
│   │
│   └── operations/                # Ongoing operations
│       ├── community/
│       ├── launch/
│       ├── pricing/
│       ├── referral/
│       ├── retention/
│       └── sales/
```

### 23.2 File Naming Conventions

**SOSTAC Documents**
- `01-situation.md`, `02-objectives.md`, etc. (numbered by phase)

**Content Files**
- `{type}-{topic}-{date}.md` (e.g., `blog-ai-marketing-2024-01.md`)
- `{type}-{sequence-name}/` (e.g., `welcome-sequence/`)

**Campaign Folders**
- `{type}-{campaign-slug}/` (e.g., `launch-product-v2/`)
- Types: `launch`, `campaign`, `promotion`, `event`

### 23.3 Finding Your Work

**By Skill**
| Skill | Primary Save Location |
|-------|----------------------|
| SOSTAC | `brands/{slug}/sostac/` |
| Content | `brands/{slug}/channels/blog/content/` |
| Email | `brands/{slug}/channels/email/content/` |
| Social | `brands/{slug}/channels/social/content/` |
| Video | `brands/{slug}/channels/video/content/` |
| SEO | `brands/{slug}/channels/seo/content/` |
| Paid Ads | `brands/{slug}/channels/paid-ads/content/` |
| Launch | `brands/{slug}/operations/launch/` |
| PR | `brands/{slug}/channels/pr/content/` |
| Retention | `brands/{slug}/operations/retention/` |

**By Campaign**
All campaign work is in `brands/{slug}/campaigns/{type}-{campaign-slug}/`

### 23.4 Legacy Path Handling

If you have content in old directory structures, the skills will:
1. Detect the legacy path
2. Save new work to the correct structure
3. Suggest migration of existing files

Legacy paths that will be migrated:
- `brands/{slug}/content/` → `brands/{slug}/channels/{type}/content/`
- `brands/{slug}/campaigns/{channel}/` → `brands/{slug}/campaigns/{campaign}/channels/{channel}/`

---

# Part 8: Tips & Best Practices

## Chapter 24: Getting the Best Results

### 24.1 How to Phrase Requests

**Good Requests (Specific and Contextual)**:
- "Create a welcome email sequence for new SaaS trial users"
- "Build a 90-day content calendar for our B2B marketing blog"
- "Audit my landing page for conversion optimization"
- "Help me plan a Product Hunt launch for next month"

**Poor Requests (Vague and Unfocused)**:
- "Help with marketing"
- "Write some content"
- "Make my emails better"
- "I need more customers"

**The Formula**: [Action] + [Specific Asset/Channel] + [Context/Audience]

### 24.2 Providing Context

The more context you provide, the better the output:

**Before (Minimal Context)**:
> "Write me a blog post about productivity"

**After (Rich Context)**:
> "Write a blog post about productivity for remote teams. We're a project management SaaS targeting startups with 5-20 employees. Our key differentiator is AI-powered task automation. Include our customer voice: 'I used to spend 4 hours a day in meetings, now it's 1 hour.' Link to our feature page for AI scheduling."

**Context Checklist**:
- [ ] Who is the target audience?
- [ ] What's the key differentiator?
- [ ] What action should they take?
- [ ] Any existing brand language or quotes?

### 24.3 Iterating on Outputs

First outputs are rarely final. Iterate effectively:

**Step 1: Request the initial output**
**Step 2: Request specific changes**
> "Make the tone more conversational, add a section about ROI, and change the CTA to 'Start Free Trial'"

**Step 3: Request alternatives**
> "Give me 3 subject line options for this email"

**Step 4: Request refinements**
> "Combine option 1's opening with option 2's urgency"

### 24.4 Combining Multiple Skills

Complex projects benefit from sequential skill activation:

**Example: Full Funnel Content Program**
```
1. SOSTAC → Strategic foundation
2. Product Marketing Context → Messaging and positioning
3. Content Marketing → Content strategy and calendar
4. SEO → Keyword research and optimization
5. Email → Nurture sequences
6. Social → Distribution and engagement
```

**Example: Product Launch**
```
1. SOSTAC → Launch objectives and strategy
2. Launch Specialist → Launch timeline and ORB strategy
3. PR → Press release and media outreach
4. Content → Launch blog posts
5. Email → Launch sequences
6. Social → Social announcement plan
7. Paid Ads → Launch campaign
```

### 24.5 Working with Existing Content

When you have existing content to improve:

**For optimization requests**:
- Share the current content
- Explain what's not working
- Provide the goal/metric you're trying to improve

**For repurposing**:
- Share the source content
- Specify the target format
- Note any changes in audience or purpose

---

## Chapter 25: Common Mistakes to Avoid

### 25.1 Skipping Strategy

**The Mistake**: Jumping straight to tactics (e.g., "Write me a blog post") without strategic foundation.

**Why It's Problematic**: Content created without strategy:
- Misses the target audience
- Lacks differentiation
- Doesn't connect to business goals
- Fails to convert

**The Solution**: Always start with SOSTAC and product marketing context, even a light version.

### 25.2 Ignoring Brand Context

**The Mistake**: Treating each request as standalone, not building on previous work.

**Why It's Problematic**:
- Inconsistent messaging across channels
- Wasted effort re-answering the same questions
- Generic output that doesn't reflect your brand

**The Solution**: Let the skill read your brand files. If you don't have them, create them first.

### 25.3 Requesting Without Context

**The Mistake**: "Write me an email" with no further details.

**Why It's Problematic**: The skill has to make assumptions that may not match your needs.

**The Solution**: Provide the who, what, why, and desired action.

### 25.4 Not Saving Deliverables

**The Mistake**: Reviewing output but not having it saved to your brand workspace.

**Why It's Problematic**:
- Can't find the work later
- No record of what was created
- Can't build on previous work

**The Solution**: Always confirm "Save this to [path]" before moving on.

### 25.5 Overlooking Escalation Suggestions

**The Mistake**: Ignoring when a skill recommends escalating to another specialist.

**Why It's Problematic**: Missing valuable insights and improvements that a specialist would catch.

**The Solution**: Pay attention to escalation signals:
- "This content is driving traffic but not converting → consider CRO"
- "Your pricing might be causing churn → consider pricing review"

---

## Chapter 26: Troubleshooting Guide

### 26.1 "I don't know where to start"

**Solution**: Start with the Marketing Agency Coordinator:
> "Help me get started with marketing for my business"

It will:
1. Check for existing brand workspaces
2. Guide you through brand creation if needed
3. Recommend the right first steps
4. Route you to the appropriate skill

### 26.2 "The output isn't specific enough"

**Possible Causes**:
- Missing brand context
- Vague initial request
- Skill didn't have enough information

**Solutions**:
1. Provide more specific context about your business
2. Share existing brand materials
3. Request a specific format: "Give me a detailed breakdown with specific examples"
4. Ask for alternatives: "Give me 3 options for this"

### 26.3 "I need to change direction"

**Scenario**: Partway through a SOSTAC plan, you want to pivot.

**Solution**:
1. Tell the skill what's changed
2. Ask it to update the relevant phase document
3. It will propagate changes through dependent phases

**Example**:
> "We've decided to target enterprise instead of SMBs. Update the strategy phase and show me what changes in tactics."

### 26.4 "I can't find my saved work"

**Check These Locations**:
1. `brands/{brand-slug}/sostac/` - for planning documents
2. `brands/{brand-slug}/channels/{type}/content/` - for content
3. `brands/{brand-slug}/campaigns/{campaign}/` - for campaign work
4. `brands/{brand-slug}/operations/{type}/` - for operational work

**If still missing**: The skill can regenerate by checking what files exist in your brand workspace.

### 26.5 "I need to work across multiple brands"

**Solution**: Specify the brand in your request:
> "For [Brand A], create a blog post about..."

The Marketing Agency Coordinator can also show all brands and their status:
> "Show me all my brands and their SOSTAC progress"

### 26.6 "The skill asked me questions I can't answer"

**This is normal** - it means the skill found genuine gaps it couldn't research.

**Options**:
1. **Provide your best guess**: "I don't have exact data, but I estimate..."
2. **Ask for a benchmark**: "What's typical for my industry?"
3. **Defer**: "Let me find that information and come back"

The skill will make reasonable assumptions and clearly state them.

---

# Part 9: Glossary

## Marketing Terms

**Acquisition**: The process of gaining new customers or users for a product or service.

**Activation**: The stage where a user takes a key action that indicates they've found value (e.g., completing onboarding, making first purchase).

**Retention**: The ability to keep customers over time; measured as the percentage of customers who continue using a product.

**Churn**: The rate at which customers stop doing business with you; typically measured monthly or annually.

**Revenue**: The income generated from customers; in SaaS often measured as ARR (Annual Recurring Revenue) or MRR (Monthly Recurring Revenue).

**Referral**: When existing customers recommend your product to others, often incentivized through programs.

**Attribution Models**: Methods for determining which marketing touchpoints contributed to a conversion:
- First-touch: Credits the first interaction
- Last-touch: Credits the final interaction
- Multi-touch: Distributes credit across multiple touchpoints

**CAC (Customer Acquisition Cost)**: Total cost to acquire a customer, including marketing and sales expenses.

**LTV (Lifetime Value)**: Total revenue expected from a customer over their entire relationship with your business.

**ROI (Return on Investment)**: The profit generated relative to the investment made; (Revenue - Cost) / Cost.

**Conversion Funnel**: The journey users take from awareness to action, typically visualized as stages with decreasing numbers.

**Customer Journey**: The complete experience a customer has with your brand, from first awareness through purchase and beyond.

**Positioning**: How you define your product's place in the market relative to competitors and alternatives.

**Segmentation**: Dividing your market into distinct groups with similar needs, behaviors, or characteristics.

**Value Proposition**: The unique benefit your product provides that makes it valuable to customers.

**Dunning**: The process of communicating with customers whose payments have failed, attempting to recover the revenue.

## Technical Terms

**Progressive Disclosure**: A design pattern where information is revealed incrementally as needed, rather than all at once. In this system, frameworks are loaded on-demand rather than all upfront.

**Framework Indexing**: A system for organizing frameworks in a searchable index with metadata (like `best_for`) to enable quick lookups.

**Context Routing**: The process of determining which skill should handle a request based on the user's intent and current state.

**Escalation Signals**: Indicators that suggest another specialist skill would be better suited to handle part of the work.

**Brand Workspace**: The file-based storage structure where all brand-related documents, plans, and deliverables are saved.

## Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **SOSTAC** | Situation, Objectives, Strategy, Tactics, Action, Control | Marketing planning framework by PR Smith |
| **CRO** | Conversion Rate Optimization | The process of increasing the percentage of visitors who convert |
| **SEO** | Search Engine Optimization | Improving visibility in organic search results |
| **GEO** | Generative Engine Optimization | Optimizing content to appear in AI-generated answers |
| **KPI** | Key Performance Indicator | A measurable value indicating success |
| **OKR** | Objectives and Key Results | Goal-setting framework with qualitative objectives and quantitative results |
| **UTM** | Urchin Tracking Module | Parameters added to URLs for tracking campaign performance |
| **AARRR** | Acquisition, Activation, Retention, Revenue, Referral | Pirate metrics framework for growth |
| **SWOT** | Strengths, Weaknesses, Opportunities, Threats | Strategic analysis framework |
| **TOWS** | Threats, Opportunities, Weaknesses, Strengths | Strategic options derived from SWOT |
| **PESTLE** | Political, Economic, Social, Technological, Legal, Environmental | Macro-environmental analysis framework |
| **TAM** | Total Addressable Market | Maximum potential market size |
| **SAM** | Serviceable Addressable Market | Market you can realistically reach |
| **SOM** | Serviceable Obtainable Market | Market you can realistically capture |
| **ORB** | Owned, Rented, Borrowed | Channel categorization framework |
| **RACI** | Responsible, Accountable, Consulted, Informed | Responsibility assignment matrix |
| **PDCA** | Plan, Do, Check, Act | Continuous improvement cycle |
| **ICE** | Impact, Confidence, Ease | Prioritization scoring framework |
| **PIE** | Potential, Importance, Ease | CRO prioritization framework |
| **JTBD** | Jobs to Be Done | Framework for understanding customer motivation |
| **STP** | Segmentation, Targeting, Positioning | Core marketing strategy framework |
| **OVP** | Online Value Proposition | Unique value delivered through digital channels |

---

# Appendices

## Appendix A: Quick Reference Cards

### A.1 Skill Trigger Phrases Cheat Sheet

| Skill | Trigger Phrases |
|-------|----------------|
| **Marketing Agency Coordinator** | marketing plan, brand strategy, campaign management, ambiguous marketing requests |
| **SOSTAC Plan Builder** | SOSTAC, marketing plan, situation analysis, marketing strategy, marketing objectives |
| **Product Marketing Context** | positioning, target audience, differentiation, proof points, ICP, buyer persona |
| **Content Marketing** | blog, article, whitepaper, case study, editorial calendar, content strategy |
| **Email Marketing** | email sequence, newsletter, drip campaign, welcome email, cold email |
| **Social Media** | social media, social calendar, hashtag strategy, Instagram, TikTok, LinkedIn |
| **Video Marketing** | video strategy, YouTube, video script, Reels, video SEO, thumbnail |
| **SEO Specialist** | SEO, keyword research, schema markup, crawlability, pSEO, GEO, link building |
| **CRO Specialist** | CRO, conversion rate, landing page, signup flow, A/B test, form optimization |
| **Retention Specialist** | churn, cancel flow, dunning, win-back, failed payment, retention rate |
| **Referral Specialist** | referral program, affiliate, partner program, refer-a-friend, word-of-mouth |
| **Product Launch** | product launch, GTM, go-to-market, Product Hunt, beta launch, launch checklist |
| **PR & Media Relations** | press release, media outreach, journalist pitch, crisis comms, reputation |
| **Paid Advertising** | PPC, paid ads, Google Ads, Meta Ads, retargeting, ad creative, ad budget |
| **Influencer Marketing** | influencer, brand ambassador, creator partnership, UGC program, sponsored content |
| **Marketing Analytics** | GA4, GTM, analytics, dashboard, attribution, measurement, tracking setup |
| **Pricing Strategy** | pricing tiers, freemium, value metric, pricing page, willing to pay |
| **Marketing Psychology** | cognitive bias, loss aversion, social proof, scarcity, Cialdini, persuasion |
| **Community Building** | Discord community, Slack community, community platform, community-led growth |
| **Guerrilla Marketing** | growth hack, viral campaign, guerrilla marketing, low-budget marketing |
| **Sales Enablement** | sales deck, pitch deck, one-pager, demo script, objection handling, battle card |

### A.2 Workflow Decision Tree

```
START
  │
  ├── Do you have a marketing plan?
  │   ├── No → Start with SOSTAC Marketing Plan Builder
  │   └── Yes → Do you have positioning defined?
  │       ├── No → Use Product Marketing Context Builder
  │       └── Yes → What do you need?
  │
  ├── Creating content?
  │   ├── Blog/Articles → Content Marketing Specialist
  │   ├── Emails → Email Marketing Specialist
  │   ├── Social Posts → Social Media Specialist
  │   └── Video → Video Marketing Specialist
  │
  ├── Improving conversions?
  │   ├── Landing pages → CRO Specialist
  │   ├── Signups → CRO Specialist
  │   └── Pricing page → Pricing Strategy Specialist
  │
  ├── Launching something?
  │   ├── Product → Product Launch Specialist
  │   ├── PR needed → PR & Media Relations
  │   └── Paid promotion → Paid Advertising Specialist
  │
  ├── Growing existing customers?
  │   ├── Reducing churn → Retention Specialist
  │   ├── Referral program → Referral Specialist
  │   └── Community → Community Building Specialist
  │
  └── Tracking performance?
      └── Marketing Analytics Specialist
```

### A.3 SOSTAC Phase Checklist

**Phase 1 - Situation Analysis** ☐
- [ ] Internal audit complete
- [ ] Competitor analysis done
- [ ] SWOT/TOWS matrix created
- [ ] Market size estimated (TAM/SAM/SOM)
- [ ] Current performance baselined

**Phase 2 - Objectives** ☐
- [ ] Business objectives defined
- [ ] Marketing objectives aligned
- [ ] SMART goals written
- [ ] KPIs selected with targets
- [ ] Timeline established

**Phase 3 - Strategy** ☐
- [ ] Target segments defined
- [ ] Positioning statement written
- [ ] Value proposition clear
- [ ] Channel selection made
- [ ] Budget allocated

**Phase 4 - Tactics** ☐
- [ ] Channel plans detailed
- [ ] Campaign structures defined
- [ ] Content themes mapped
- [ ] Tools/platforms selected
- [ ] Timeline by tactic

**Phase 5 - Action** ☐
- [ ] Detailed timeline created
- [ ] RACI assignments made
- [ ] Resource requirements listed
- [ ] Dependencies mapped
- [ ] Launch dates set

**Phase 6 - Control** ☐
- [ ] Dashboard designed
- [ ] Metrics defined per channel
- [ ] Review cadence set
- [ ] Optimization triggers defined
- [ ] Reporting template ready

---

## Appendix B: Framework Quick Reference

### B.1 Complete Framework Index

**SOSTAC Frameworks by Phase**:

| Phase | Framework | Best For |
|-------|-----------|----------|
| Situation | SWOT + TOWS | Strategic direction generation |
| Situation | PESTLE | Macro-environment scanning |
| Situation | Porter's Five Forces | Competitive dynamics |
| Situation | TAM/SAM/SOM | Market sizing |
| Situation | Jobs to Be Done | Customer motivation |
| Situation | Digital Maturity 5S | Capability assessment |
| Objectives | OKR Framework | Stretch goals with measurable outcomes |
| Objectives | RACE Framework | Funnel stage coverage |
| Objectives | 5S Objectives | Beyond-revenue objectives |
| Objectives | Objective Cascade | Revenue-to-channel targets |
| Strategy | STP | Segmentation, targeting, positioning |
| Strategy | Positioning Statement | Differentiation messaging |
| Strategy | Ansoff Matrix | Growth direction |
| Strategy | Porter's Generic Strategies | Competitive advantage |
| Strategy | Blue Ocean | Uncontested market space |
| Strategy | Value Proposition Canvas | Product-market fit |
| Tactics | AARRR Pirate Metrics | Funnel diagnostics |
| Tactics | ICE Scoring | Experiment prioritization |
| Tactics | PIE Framework | CRO prioritization |
| Tactics | Hub-Hero-Help | Content tiers |
| Tactics | Pillar-Cluster | SEO architecture |
| Tactics | 7P Marketing Mix | Tactical coverage |
| Tactics | 70/20/10 Budget | Resource allocation |
| Action | RACI Matrix | Responsibility assignment |
| Action | Agile Sprints | Execution structure |
| Action | Objective-Task Budgeting | Evidence-based budgets |
| Control | Attribution Models | Channel credit |
| Control | North Star Metric | Core value metric |
| Control | Leading/Lagging Indicators | Dashboard design |
| Control | PDCA Cycle | Continuous improvement |

### B.2 Framework Selection by Situation

| Your Situation | Recommended Framework(s) |
|----------------|-------------------------|
| Starting from scratch | SOSTAC + SWOT + STP |
| Entering new market | TAM/SAM/SOM + Porter's Five Forces |
| Competing on price | Porter's Generic Strategies (Cost Leadership) |
| Low growth | AARRR + ICE Scoring |
| High churn | JTBD + Retention frameworks |
| Complex buyer journey | Customer Journey Mapping + TOFU/MOFU/BOFU |
| Limited budget | 70/20/10 Budget + Bullseye Framework |
| Launching product | ORB Channel Strategy + Launch Phases |
| Scaling content | Hub-Hero-Help + Pillar-Cluster |

---

## Appendix C: Platform-Specific Guides

### C.1 Social Media Platform Characteristics

| Platform | Best For | Post Frequency | Best Post Times | Key Metric |
|----------|----------|----------------|-----------------|------------|
| Instagram | B2C, lifestyle, visual | 4-7/week + daily Stories | 11am-1pm, 7-9pm | Engagement Rate |
| TikTok | B2C, viral, younger | 1-3/day (growth phase) | 7am, 12pm, 7pm | Views + Completion |
| LinkedIn | B2B, professional | 3-5/week | 7-8am, 12pm, 5-6pm | Comments + Shares |
| X/Twitter | News, commentary | 3-5/day | 8am, 12pm, 6pm | Impressions |
| YouTube | Education, tutorials | 1-2/week | 2-4pm weekdays | Watch Time |
| Facebook | Community, older demo | 1-2/day | 1-4pm, 6-9pm | Shares |

### C.2 Ad Platform Comparison

| Platform | Best For | Min Budget | Avg CPC | Key Strength |
|----------|----------|------------|---------|--------------|
| Google Search | High intent | $10/day | $1-2 | Capture demand |
| Meta (FB/IG) | Awareness, retargeting | $5/day | $0.50-1.50 | Precise targeting |
| LinkedIn | B2B, decision-makers | $10/day | $5-10 | Professional targeting |
| TikTok | Brand awareness, young | $20/day | $0.25-1 | Viral potential |
| YouTube | Awareness, education | $10/day | $0.10-0.30 | Video engagement |

### C.3 Community Platform Selection

| Platform | Best For | Cost | Moderation | Member Limit |
|----------|----------|------|------------|--------------|
| Discord | Gaming, tech, younger | Free | Strong tools | Unlimited |
| Slack | B2B, professionals | Free-$12.50/user/mo | Basic | 10k messages (free) |
| Circle | Creators, courses | $49-399/mo | Strong | Unlimited |
| Skool | Courses, coaching | $99/mo | Built-in | Unlimited |
| Facebook Groups | General, older demo | Free | Basic | Unlimited |
| Reddit | Niche interests | Free | Subreddit rules | Unlimited |

---

## Appendix D: Benchmark Reference

### D.1 Email Benchmarks

| Industry | Open Rate | Click Rate | Unsubscribe Rate |
|----------|-----------|------------|------------------|
| SaaS | 25-30% | 2.5-4% | <0.5% |
| E-commerce | 15-25% | 2-3.5% | <0.3% |
| Finance | 20-25% | 2-3% | <0.2% |
| Healthcare | 22-28% | 2-4% | <0.3% |
| Media | 20-25% | 3-5% | <0.5% |
| **Good Target** | **>25%** | **>3%** | **<0.5%** |

### D.2 Social Media Benchmarks

| Platform | Good Engagement Rate | Good Follower Growth |
|----------|---------------------|---------------------|
| Instagram | 3-6% | 5-10%/month |
| TikTok | 5-10% | 10-20%/month |
| LinkedIn | 2-4% | 3-5%/month |
| X/Twitter | 0.5-1% | 2-5%/month |
| YouTube | 4-8% (CTR) | 5-10%/month |

### D.3 Conversion Benchmarks

| Page Type | Good Conversion Rate | Excellent Rate |
|-----------|---------------------|----------------|
| Landing Page | 2-5% | 5-10%+ |
| Signup Flow | 25-40% | 50%+ |
| Free Trial → Paid | 10-25% | 30%+ |
| E-commerce Checkout | 60-70% | 75%+ |
| Lead Gen Form | 10-20% | 25%+ |

### D.4 SEO Benchmarks

| Metric | Good | Excellent |
|--------|------|-----------|
| Organic CTR (Position 1) | 25-30% | 30%+ |
| Organic CTR (Position 3) | 10-15% | 15%+ |
| Bounce Rate | 40-60% | <40% |
| Time on Page | 2-3 min | 4+ min |
| Pages per Session | 2-3 | 4+ |
| Core Web Vitals (LCP) | <2.5s | <1.5s |

---

## Appendix E: Template Library

### E.1 Campaign Brief Template

```markdown
# Campaign Brief: [Campaign Name]

## Overview
- **Campaign Type**: [Launch/Promotion/Event/Evergreen]
- **Duration**: [Start Date] - [End Date]
- **Budget**: [Total Budget]

## Objectives
1. Primary: [Main goal with specific metric]
2. Secondary: [Supporting goal]
3. KPIs: [List 3-5 metrics]

## Target Audience
- **Primary Persona**: [Name]
- **Demographics**: [Age, location, role]
- **Pain Points**: [What problem are they solving?]
- **Current Solution**: [What do they use now?]

## Key Messages
1. [Primary message]
2. [Supporting message]
3. [Proof point]

## Channel Mix
| Channel | Purpose | Budget % |
|---------|---------|----------|
| [Channel 1] | [Purpose] | [%] |
| [Channel 2] | [Purpose] | [%] |

## Creative Requirements
- [ ] Blog posts: [Number]
- [ ] Emails: [Number]
- [ ] Social posts: [Number]
- [ ] Ad creatives: [Number]

## Timeline
- **Week 1-2**: [Activities]
- **Week 3-4**: [Activities]
- **Launch**: [Date]
- **Post-launch**: [Activities]

## Success Metrics
| Metric | Target | Actual |
|--------|--------|--------|
| [Metric 1] | [Target] | [Post-campaign] |
| [Metric 2] | [Target] | [Post-campaign] |
```

### E.2 Content Calendar Template

```markdown
# Content Calendar: [Month/Quarter]

## Content Pillars
1. [Pillar 1] - [% of content]
2. [Pillar 2] - [% of content]
3. [Pillar 3] - [% of content]

## Calendar

| Date | Title | Pillar | Funnel Stage | Keyword | Status | Owner |
|------|-------|--------|--------------|---------|--------|-------|
| [Date] | [Title] | [Pillar] | [TOFU/MOFU/BOFU] | [Target KW] | [Draft/Review/Published] | [Name] |

## Distribution Checklist
- [ ] Published to blog
- [ ] Shared on LinkedIn
- [ ] Shared on Twitter/X
- [ ] Included in newsletter
- [ ] Repurposed to social quotes
```

### E.3 Email Sequence Template

```markdown
# [Sequence Name] Email Sequence

## Sequence Overview
- **Purpose**: [What this sequence accomplishes]
- **Entry Trigger**: [How someone enters this sequence]
- **Exit Condition**: [How someone exits]
- **Total Emails**: [Number]
- **Duration**: [Days from first to last email]

## Email [N]

### Metadata
- **Send Timing**: [Day X, Time Y after entry]
- **Subject Line**: [Subject]
- **Preview Text**: [Preview text]

### Content
**Opening**: [Hook/opening line]

**Body**: [Main content - bullet points or paragraphs]

**CTA**: [Primary call to action]
- Button text: [Text]
- Link: [URL]

**P.S.** (optional): [Additional nudge or bonus]

### Variants
| Element | Version A | Version B |
|---------|-----------|-----------|
| Subject | [Version A] | [Version B] |
| CTA | [Version A] | [Version B] |
```

### E.4 Landing Page Brief Template

```markdown
# Landing Page Brief: [Page Name]

## Purpose
- **Campaign**: [Associated campaign]
- **Goal**: [Primary conversion goal]
- **Target Audience**: [Who is this page for?]

## Key Elements

### Hero Section
- **Headline**: [Main headline]
- **Subheadline**: [Supporting copy]
- **Primary CTA**: [Button text]
- **Hero Image**: [Description or reference]

### Social Proof
- [ ] Testimonials: [Number needed]
- [ ] Logos: [Companies to feature]
- [ ] Stats: [Key numbers]

### Features/Benefits
1. [Feature] → [Benefit]
2. [Feature] → [Benefit]
3. [Feature] → [Benefit]

### Objection Handling
| Objection | Response |
|-----------|----------|
| [Objection 1] | [Response] |
| [Objection 2] | [Response] |

### Technical Requirements
- [ ] Form fields: [List fields]
- [ ] Integration: [CRM/ESP]
- [ ] Tracking: [Conversion events]

## Success Metrics
- Target conversion rate: [%]
- Traffic source: [Where traffic comes from]
```

### E.5 Press Release Template

```markdown
# Press Release

**FOR IMMEDIATE RELEASE**

## [Headline - Action-Oriented, Newsworthy]

[City, State] – [Date] – [Opening paragraph with who, what, when, where, why]

[Second paragraph expanding on the news with relevant details and quotes]

"[Quote from CEO or key spokesperson]," said [Name], [Title] at [Company]. "[Additional quote content]."

[Third paragraph with supporting facts, context, or statistics]

[Fourth paragraph about the company - boilerplate]

### About [Company Name]
[1-2 sentence company description]

**Media Contact:**
[Name]
[Title]
[Email]
[Phone]
[Website]

###
[End marker]
```