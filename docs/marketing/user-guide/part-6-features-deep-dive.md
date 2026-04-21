# Part 6: Features & Capabilities Deep Dive

This part provides a comprehensive technical deep dive into the Agentic Marketing Skills system's core features. Understanding these mechanisms will help you leverage the system more effectively and troubleshoot when needed.

---

## Chapter 18: Smart Framework Selection

### 18.1 What Are Marketing Frameworks?

Marketing frameworks are structured methodologies that provide proven approaches to specific marketing challenges. Rather than starting from scratch with every request, the Agentic Marketing system draws from a curated library of battle-tested frameworks developed by marketing practitioners, academics, and strategists.

Each framework serves as a thinking tool that:

- **Structures analysis** — Guides systematic exploration of complex problems
- **Provides shortcuts** — Offers pre-built approaches to common challenges
- **Ensures completeness** — Prevents overlooking critical elements
- **Enables communication** — Creates shared vocabulary for strategy discussions

The system does not apply frameworks mechanically. Instead, it uses them as foundational structures that are adapted to your specific brand context, audience, and goals.

---

### 18.2 The Progressive Disclosure System

#### The Problem: Token Efficiency

Large language models have context limits. Loading every framework document for every request would:

- Consume tokens unnecessarily
- Slow response times
- Dilute focus with irrelevant information
- Increase costs

#### The Solution: Progressive Disclosure

The system uses a three-stage lookup protocol that loads only what's needed:

```
Stage 1: Read the index (~40 rows)
         |
         v
Stage 2: Match situation to best_for column
         |
         v
Stage 3: Load ONLY matched framework file(s)
```

**Example in action:**

1. You request a situation analysis
2. System reads `frameworks-index.csv` (a lightweight table)
3. Matches your situation to frameworks where `best_for` contains "situation analysis"
4. Loads only `swot-tows.md`, `pestle.md`, and `porters-five-forces.md`
5. Never touches the other 35+ framework files

This approach typically reduces token usage by 80-90% compared to bulk-loading all frameworks.

#### Index Structure

Each frameworks index contains these columns:

| Column | Purpose |
|--------|---------|
| `id` | Unique identifier for reference |
| `name` | Framework display name |
| `description` | Brief explanation of what it does |
| `best_for` | Situations where this framework excels (used for matching) |
| `phase` / `category` | SOSTAC phase or functional category |
| `file` | Path to the full framework document |
| `tags` | Keywords for additional filtering |

---

### 18.3 Complete Framework Catalog

#### 18.3.1 SOSTAC Frameworks (38 Frameworks)

These frameworks support the 6-phase SOSTAC marketing planning process.

##### Situation Phase Frameworks (7)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **SWOT + TOWS Analysis** | Maps internal strengths/weaknesses against external opportunities/threats; crosses quadrants to generate strategic options | Comprehensive situation assessment; strategic direction generation |
| **PESTLE Analysis** | Scans macro-environment across Political, Economic, Social, Technological, Legal, Environmental dimensions | Identifying external forces; regulatory scanning |
| **Porter's Five Forces** | Assesses structural industry attractiveness by rating five competitive forces | Understanding competitive dynamics; industry profitability drivers |
| **TAM/SAM/SOM Market Sizing** | Estimates addressable market at three levels using bottom-up calculation | Sizing market opportunity; setting realistic share targets |
| **Jobs-to-be-Done (JTBD)** | Frames customer motivation as functional, emotional, and social jobs | Understanding customer motivation; positioning input |
| **Digital Maturity Model (5S)** | Baseline assessment of digital marketing maturity across Sell, Serve, Speak, Save, Sizzle dimensions | Scoring current digital capability; identifying gaps |
| **Customer Journey Mapping** | Visual representation of every step from problem recognition to advocacy | Identifying journey pain points; touchpoint analysis |

##### Objectives Phase Frameworks (4)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **OKR Framework** | Objectives and Key Results — qualitative inspiring objective paired with quantitative time-bound key results | Setting stretch goals; cross-team alignment |
| **RACE Framework** | Digital marketing planning covering Reach, Act, Convert, Engage lifecycle stages | Ensuring objectives cover all funnel stages |
| **PR Smith's 5S Objectives** | Five objective categories — Sell, Serve, Speak, Save, Sizzle | Broadening objective scope beyond sales metrics |
| **Objective Cascade Method** | Works backwards from business revenue goal through marketing contribution to channel-level sub-objectives | Building bottom-up channel targets |

##### Strategy Phase Frameworks (7)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **STP: Segmentation Targeting Positioning** | Core strategic sequence — divide market, choose segments, define positioning | Defining target segments; competitive positioning |
| **Moore's Positioning Statement** | Fill-in-the-blank template for writing a precise, differentiated positioning statement | Crafting defensible positioning; differentiation messaging |
| **Ansoff Matrix** | 2x2 growth strategy matrix across existing/new markets and existing/new products | Determining growth direction; assessing risk level |
| **Porter's Generic Strategies** | Three fundamental competitive advantage approaches — Cost Leadership, Differentiation, or Focus | Choosing competitive strategy; aligning messaging |
| **Blue Ocean Strategy — 4 Actions** | Finding uncontested market space by eliminating, reducing, raising, and creating factors | Breaking out of commoditized markets |
| **Value Proposition Canvas** | Maps offerings against customer jobs, pains, and gains to ensure product-market fit | Ensuring features connect to real needs |
| **Online Value Proposition (OVP)** | Articulates why a customer should engage with the brand online versus alternatives | Defining unique digital experience advantage |

##### Tactics Phase Frameworks (9)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **AARRR Pirate Metrics** | Five-stage funnel model — Acquisition, Activation, Retention, Revenue, Referral | Identifying biggest funnel leak; growth diagnostics |
| **ICE Scoring** | Prioritization framework scoring tactics on Impact, Confidence, and Ease | Ranking candidate tactics into prioritized backlog |
| **PIE Framework** | CRO-specific prioritization scoring pages/experiments on Potential, Importance, and Ease | Prioritizing conversion rate optimization experiments |
| **Hub-Hero-Help Content Model** | Three-tier content strategy allocating content types by audience scale, frequency, and intent | Structuring content production cadence |
| **Pillar-Cluster SEO Model** | Site architecture with broad pillar pages and supporting cluster pages | Building topical authority; internal linking strategy |
| **TOFU/MOFU/BOFU** | Content classification aligned to buyer decision journey stages | Auditing content coverage by funnel stage |
| **7P Marketing Mix** | Expanded marketing mix — Product, Price, Place, Promotion, People, Process, Physical Evidence | Ensuring tactics address all 7Ps |
| **70/20/10 Budget Rule** | Budget allocation — 70% proven core, 20% emerging, 10% experimental | Allocating channel budget with risk distribution |
| **Situational Framework Router** | Three-layer router selecting one of 9 playbooks with channel-framework pairings | Determining the right tactical playbook |

##### Action Phase Frameworks (4)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **RACI Matrix** | Responsibility assignment — Responsible, Accountable, Consulted, Informed | Assigning clear ownership; preventing bottlenecks |
| **Agile Marketing Sprints** | Scrum-adapted 2-week marketing sprints with planning, standup, review, retrospective | Structuring execution into time-boxed cycles |
| **Objective-and-Task Budgeting** | Bottom-up budget built by defining the objective, then costing required tasks | Building evidence-based budgets |
| **Kotter's 8-Step Change Model** | Organizational change framework for overcoming resistance | Addressing leadership misalignment; structural barriers |

##### Control Phase Frameworks (6)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Attribution Models Comparison** | Comparison of attribution models — first-touch, last-touch, linear, time-decay, position-based, data-driven | Selecting the right attribution model |
| **North Star Metric** | Single metric capturing core customer value — if it grows, revenue and retention follow | Selecting the one metric that predicts long-term health |
| **Leading vs Lagging Indicators** | Pairs leading predictive indicators with lagging outcome indicators per channel | Building dashboards that drive decisions |
| **PDCA Cycle** | Four-stage iterative improvement loop — Plan, Do, Check, Act | Establishing operating rhythm for optimization |
| **Balanced Scorecard for Marketing** | Maps marketing KPIs across Financial, Customer, Internal Process, Learning & Growth perspectives | Preventing over-optimization on financial KPIs |
| **OKR Review Cadence** | Structured rhythm for reviewing OKR progress — weekly, monthly, quarterly, annually | Maintaining alignment; enabling course-correction |

---

#### 18.3.2 Agency Frameworks (11 Frameworks)

General-purpose frameworks for marketing agency coordination and channel selection.

| Framework | Description | Best For |
|-----------|-------------|----------|
| **RACE Framework** | Customer lifecycle framework covering full journey from awareness to advocacy | Full lifecycle marketing plan; campaign structure |
| **See-Think-Do-Care** | Audience-intent framework mapping content and channels to customer mindset across four stages | Audience-intent content strategy; content-channel mapping |
| **Growth Loops vs. Funnels** | Compares linear funnel models with self-reinforcing growth loops | Self-reinforcing growth strategy; product-led growth |
| **Bullseye Framework** | Systematic 3-ring approach testing 19 traction channels to find the best growth channel | Channel discovery and prioritization; startup channel strategy |
| **ICE Scoring** | Fast scoring method for ranking marketing experiments | Experiment prioritization; sprint planning |
| **AARRR Pirate Metrics** | Five-stage lifecycle measurement framework | Product-led growth metrics; lifecycle measurement |
| **Customer Journey Mapping** | Process for visualizing complete customer experience | Understanding customer experience; touchpoint analysis |
| **Marketing Maturity Model** | 5-stage assessment of marketing sophistication from Ad Hoc to Optimized | Assessing marketing sophistication; client readiness |
| **Budget Allocation Models** | 70/20/10 rule plus business-stage allocation models | Budget planning; channel mix optimization |
| **Framework Selection Guide** | Decision tree for choosing the right framework plus recommended combining stack | Choosing which framework to apply |
| **Situational Router** | Three-layer router selecting tactical playbooks based on brand situation | Determining the right tactical playbook |

---

#### 18.3.3 Video Viral Frameworks (27 Frameworks)

These frameworks are specifically designed for creating viral short-form video content.

##### Hook Frameworks (5)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Dual-Sensory Hook** | Combine visual interrupts with audio anchors in the first 3 seconds for maximum scroll-stop power | TikTok/Reels openings; first-3-seconds optimization |
| **Pattern-Interrupt Curiosity Loop** | Break the scroll pattern with unexpected visuals then immediately open a curiosity loop | Hooks; attention capture; pattern breaking |
| **Fake UI Pattern Interrupt** | Use interface-like graphics that break expectations to stop the scroll | Visual hooks; UI-based content; attention grabbing |
| **4-Pillar Hook Matrix** | Structure hooks across four pillars: curiosity, risk, surprise, and meaning | Hook strategy; multi-dimensional hooks |
| **Silent Scroll-Stopper** | Use dynamic physical movements before speaking to capture attention without audio | Talking head content; first-second optimization |

##### Structure Frameworks (8)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Tension-Twist-Payoff Stack** | Build tension through contrast, deliver an unexpected twist, then provide satisfying payoff | Storytelling content; engagement hooks |
| **Value-Hook-Repeat Engine** | Alternate between delivering value and re-hooking to maintain retention throughout | Retention; mid-video engagement |
| **Shock & Loop Framework** | Create a shocking or confusing opening that resolves into a satisfying loop | Loop content; replays; viral potential |
| **Outcome-Pain-Solution (OPS)** | Lead with the outcome, expose the pain of not having it, then present your solution | Conversion content; sales videos |
| **Cinematic Underdog** | Combine wide-angle visual hooks with negative-then-positive underdog storytelling | Personal brands; journey documentation |
| **Frustration-Replay Loop** | Create impossible interactive challenges that force multiple full-video rewatches | Product showcases; gaming; loop content |
| **Problem-Motion-Win Stack** | Hook with micro-problem, hold with movement, deliver single actionable win | Education; tips content; shareability |
| **Hidden Psychology Reveal** | Expose secret manipulation tactics through paradox hooks and quantifiable case studies | Edutainment; business; psychology education |

##### Format Frameworks (9)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Visual Contrast Listicle** | Use split-screen A/B comparisons with visual heuristics for instant comprehension | Educational content; tips/hacks; save-worthy posts |
| **Prop Effect Framework** | Use highly visual physical props to represent abstract concepts | Educational content; abstract concepts; high retention |
| **Voyeuristic Reveal** | Open with raw bystander footage then transition to polished cinematic reveal | Lifestyle; music; storytelling with production value |
| **Gated Magic Engagement Loop** | Offer high-value result for free but gate essential tool behind comment engagement | AI/Tech content; lead generation; engagement hacking |
| **Controlled Distraction** | Perform mundane physical tasks while speaking to increase cognitive load and retention | Talking head; storytelling; spoken-word content |
| **Unpolished Friend** | Use raw face-to-camera conversation style to build trust | Personal brands; coaches; consultants; trust building |
| **Mistake-to-Mastery** | Use negative framing hooks and visual bad/good contrast cycles to establish authority | Educational creators; design; marketing; consultants |
| **Everyday Paradox Breakdown** | Reveal business logic behind universally relatable counter-intuitive observations | Edutainment; business trivia; how the world works |
| **Premium Perception Stack** | Break aspirational goals into 3 actionable secrets with emotional pivots and rulebooks | B2B creators; agencies; design consultants; e-commerce |

##### Replication Frameworks (3)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Outlier Replication (Viral Hack)** | Find videos with 5x views-to-followers ratio and replicate their structural pattern | Finding proven formats; data-backed content ideas |
| **Relatable Pattern Replicator** | Replicate proven viral formats with universal pain points in new settings | Comedy content; relatable humor; trend participation |
| **Viral Blueprint Repurpose** | Extract structural blueprint from a viral video and repurpose with your own content | Content adaptation; format extraction |

##### Series Frameworks (2)

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Hook & Binge Series** | Pair scroll-stopping hooks with serialized content to drive repeat viewership | Content series; building loyal followers |
| **Borrowed Attention Stitch** | Leverage trending audio or viral content structures to borrow existing audience attention | Trend participation; audio trends; format riding |

---

#### 18.3.4 Psychology Frameworks (10 Frameworks)

These frameworks apply behavioral science and persuasion principles to marketing decisions.

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Strategic Mental Models** | Thinking frameworks for better strategic marketing decisions — first principles, JTBD, flywheel, theory of constraints | Strategic planning and reasoning clarity |
| **Expanded Cognitive Biases** | 15 cognitive biases with definitions and marketing-specific worked examples | Diagnosing conversion problems; psychology-informed copy |
| **Copy Rewrite Examples** | Five before-and-after copy rewrites showing psychological principles applied | Learning by example; creating psychology-informed copy |
| **Quick-Reference Table** | 20 marketing challenges mapped to primary principle and supporting principle with tactics | Rapid diagnostic for any marketing problem |
| **Cialdini Six Principles** | Reciprocity, commitment-consistency, social proof, authority, liking, scarcity — with marketing applications | Designing persuasion-dependent assets |
| **Psychology by Context** | Channel-by-channel guidance for paid ads, landing pages, email, pricing pages, onboarding | Choosing which principles to apply by channel |
| **Pricing Psychology** | Charm pricing, decoy pricing, price anchoring, Rule of 100, mental accounting | Designing pricing pages and presenting prices |
| **Behavioral Design** | BJ Fogg B=MAP model; friction reduction; tiny habits; prompt design | Diagnosing why behaviors don't happen |
| **Ethics and Dark Patterns** | Ethical persuasion principles; dark pattern identification | Ensuring techniques remain ethical |
| **Diagnostic and Protocol** | How to use this skill; problem-specific vs audit mode; response protocol | Understanding how to apply the skill |

---

### 18.4 How Frameworks Are Automatically Selected

The `best_for` column is the key to automatic framework selection. When you make a request, the system:

1. **Analyzes your request** — Identifies keywords, context, and intent
2. **Scans the index** — Looks for matching terms in `best_for` and `tags` columns
3. **Ranks matches** — Prioritizes frameworks with the closest fit
4. **Loads top matches** — Reads only the most relevant framework files

**Matching examples:**

| Your Request | Matches `best_for` | Frameworks Selected |
|--------------|-------------------|---------------------|
| "I need to understand my competitive position" | "competitive dynamics", "competitive analysis" | Porter's Five Forces, SWOT+TOWS |
| "Help me set goals for next quarter" | "goal-setting", "stretch targets" | OKR Framework, 5S Objectives |
| "Which channels should I prioritize?" | "channel discovery", "prioritization" | Bullseye Framework, ICE Scoring |
| "My TikTok videos aren't getting views" | "hooks", "TikTok", "scroll-stop" | Dual-Sensory Hook, 4-Pillar Hook Matrix |

---

### 18.5 Combining Frameworks Effectively

The system often combines multiple frameworks to address complex requests. Common combinations include:

#### Situation Analysis Stack
```
SWOT + TOWS + PESTLE + Porter's Five Forces
= Internal assessment + External scanning + Industry structure
```

#### Growth Strategy Stack
```
Ansoff Matrix + Bullseye Framework + AARRR Metrics
= Growth direction + Channel selection + Measurement framework
```

#### Content Strategy Stack
```
Hub-Hero-Help + Pillar-Cluster + TOFU/MOFU/BOFU
= Content tiers + Site architecture + Funnel mapping
```

#### Launch Planning Stack
```
OKR Framework + RACI Matrix + PDCA Cycle
= Goals + Responsibilities + Continuous improvement
```

---

## Chapter 19: Research-First Approach

### 19.1 The Research-Recommend-Validate Pattern

Every SOSTAC phase follows a consistent five-step pattern:

```
1. RESEARCH
   - Read previous phases
   - Conduct fresh web research
   - Analyze competitors and benchmarks
   |
   v
2. ANALYZE & RECOMMEND
   - Apply relevant frameworks
   - Produce concrete recommendations
   - Support with evidence
   |
   v
3. PRESENT FINDINGS
   - Share 3-5 most important insights
   - Explain strategic implications
   |
   v
4. VALIDATE & REFINE
   - Ask 2-4 targeted questions
   - Fill genuine gaps only
   - Incorporate feedback
   |
   v
5. SAVE AND ADVANCE
   - Write phase document
   - Update README tracker
   - Preview next phase
```

**Key principle:** The user should feel like they hired a strategist who shows up prepared — not someone asking them to do the research.

---

### 19.2 Auto-Discovery Capabilities

Before any SOSTAC planning begins, the system can run comprehensive auto-discovery to gather publicly available intelligence about a brand and its competitors.

#### What Auto-Discovery Covers

| Section | Intelligence Gathered |
|---------|----------------------|
| **Brand Digital Presence** | Homepage analysis, technology stack, Core Web Vitals, pricing model, historical messaging |
| **Google SERP Research** | Brand SERP, category keywords, competitor discovery queries, Google Trends |
| **Competitor Research** | Homepage positioning, SimilarWeb traffic estimates, pricing analysis |
| **Ad Intelligence** | Meta Ad Library (Facebook/Instagram), Google Ad Transparency |
| **Review Mining** | G2 reviews, Trustpilot, App Store reviews |
| **Customer Language** | Reddit discussions, Quora questions, People Also Ask data |
| **LinkedIn Intelligence** | Company pages, job postings as strategic signals |

#### Output Location

All findings are saved to:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md
```

This document becomes the foundation for the SOSTAC interview, reducing the burden on the user to explain what's already discoverable.

---

### 19.3 Competitor Analysis Methods

The system uses multiple methods to identify and analyze competitors:

#### Discovery Methods

1. **SERP Analysis** — Searches for "{brand} alternatives" and "{brand} vs" queries
2. **Category Keywords** — Analyzes "best {category}" search results
3. **Review Platforms** — Identifies competitors mentioned in G2/Capterra comparisons
4. **Ad Libraries** — Finds brands running similar ads

#### Analysis Dimensions

| Dimension | What's Extracted |
|-----------|-----------------|
| **Positioning** | Hero headline, value proposition, target audience signals |
| **Pricing** | Tiers, price points, free trial availability |
| **Traffic** | Monthly visits, traffic sources, geographic distribution |
| **Technology** | CMS, analytics, marketing automation, CRM |
| **Ad Activity** | Active campaigns, dominant themes, proven performers |
| **Reviews** | Strengths praised, weaknesses criticized, customer profile |

---

### 19.4 Benchmark Data Sources

The system draws benchmark data from multiple sources:

| Data Type | Sources |
|-----------|---------|
| **Traffic Estimates** | SimilarWeb, Semrush |
| **Search Volume** | Google Trends, Keyword Planner data |
| **Performance Metrics** | Industry benchmark databases, platform-specific benchmarks |
| **Pricing Intelligence** | Public pricing pages, review platform data |
| **Review Signals** | G2, Trustpilot, Capterra, App Store |
| **Ad Performance** | Meta Ad Library (duration as quality signal), Google Ad Transparency |

---

### 19.5 Browser Automation Integration

For deep research, the system integrates with `agent-browser` — a browser automation CLI designed for AI agents.

#### Setup

Check if agent-browser is available:
```bash
agent-browser --version
```

If not installed:
```bash
# Install the CLI directly
npm install -g agent-browser && npx playwright install chromium
```

#### Fallback

If installation fails, the system automatically uses `WebFetch` and `WebSearch` tools as alternatives for all research tasks.

#### Session Management

All browser research runs in named sessions:
```bash
agent-browser --session sostac-discovery-{brand-slug} open {url}
```

Sessions maintain cookies, avoid repeated cold starts, and group all activity logically.

---

## Chapter 20: Progressive Delivery System

### 20.1 How Outputs Are Saved

Every skill saves its outputs to a structured directory within the brand workspace. This creates an audit trail, enables resumption, and allows cross-skill references.

**Core principle:** Files are the source of truth. Critical information gets written to files, not just displayed in chat.

---

### 20.2 File Organization Patterns

The system uses two primary modes for organizing deliverables:

#### Campaign Mode

When work is part of a named campaign:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/
  strategy.md                    # Campaign strategy
  channels/
    email/content/               # Email deliverables
    social/content/              # Social deliverables
    paid-ads/content/            # Ad creatives
    seo/content/                 # SEO deliverables
    blog/content/                # Blog posts
    video/content/               # Video scripts
    pr/content/                  # PR deliverables
    influencer/content/          # Influencer briefs
  cro/                           # CRO work
  retention/                     # Retention work
  sales/                         # Sales enablement
  performance/                   # Performance reports
```

#### Standalone Mode

For evergreen or independent work:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/
  email/content/
  social/content/
  blog/content/
  seo/content/
  video/content/
  paid-ads/content/

./.pawbytes/marketing-suites/brands/{brand-slug}/operations/
  cro/
  retention/
  sales/
  pricing/
  community/
```

#### Campaign Type Prefixes

Campaign folders use standardized prefixes:
- `launch-` — Product launches
- `evergreen-` — Ongoing programs
- `seasonal-` — Time-bound campaigns
- `promotion-` — Sales/promotions
- `awareness-` — Brand awareness
- `growth-` — Growth initiatives
- `retention-` — Retention campaigns
- `event-` — Event-related campaigns

---

### 20.3 Naming Conventions

Consistent naming makes files discoverable and sortable.

#### Date Formats

| Type | Format | Example |
|------|--------|---------|
| Datestamp | `YYYY-MM-DD` | `2024-03-15` |
| Month | `YYYY-MM` | `2024-03` |

#### File Naming Patterns

| Deliverable | Pattern | Example |
|-------------|---------|---------|
| Video script | `script-{slug}-{YYYY-MM-DD}.md` | `script-product-demo-2024-03-15.md` |
| Video brief | `video-brief-{slug}-{YYYY-MM-DD}.md` | `video-brief-launch-teaser-2024-03-15.md` |
| Content calendar | `video-calendar-{YYYY-MM}.md` | `video-calendar-2024-03.md` |
| YouTube strategy | `youtube-strategy-{YYYY-MM-DD}.md` | `youtube-strategy-2024-03-15.md` |
| Ad script | `ad-script-{platform}-{slug}-{YYYY-MM-DD}.md` | `ad-script-meta-summer-sale-2024-03-15.md` |
| Performance report | `monthly-report-{YYYY-MM}.md` | `monthly-report-2024-03.md` |
| Blog post | `blog-{slug}-{YYYY-MM-DD}.md` | `blog-seo-guide-2024-03-15.md` |
| Email sequence | `sequence-{type}-{slug}.md` | `sequence-welcome-new-signups.md` |

#### Slug Rules

Slugs are URL-friendly identifiers:
- Lowercase letters only
- Hyphens instead of spaces
- No special characters
- Concise but descriptive

---

### 20.4 Version Control Integration

The file-based system integrates naturally with git:

```
# View history of a deliverable
git log --oneline .pawbytes/marketing-suites/brands/acme/sostac/03-strategy.md

# Compare versions
git diff HEAD~1 .pawbytes/marketing-suites/brands/acme/channels/video/content/scripts/

# Track campaign evolution
git log --oneline .pawbytes/marketing-suites/brands/acme/campaigns/launch-spring-2024/
```

**Best practices:**
- Commit after each phase completion
- Use descriptive commit messages
- Review diffs before committing
- Tag major milestones

---

### 20.5 Deliverable Templates

Each skill defines standard templates for its outputs. For example, a video script includes:

```markdown
## Video Script: {Title}

### Meta
- Platform: [TikTok/YouTube/Instagram/etc.]
- Length: [duration]
- Type: [tutorial/promotional/educational/etc.]
- Audience: [target segment]
- Objective: [what this video achieves]

### Script

| Timecode | Visual | Audio/Dialogue |
|----------|--------|----------------|
| 0:00-0:03 | [visual direction] | [hook/opening line] |
| ... | ... | ... |

### B-Roll List
- [List of secondary footage needed]

### Music/Sound Effects
- [Audio direction]

### Text Overlays
- [On-screen text specifications]

### CTA
- [Call to action]

### Thumbnail Concept
- [Thumbnail direction]

### Distribution Plan
- [Where and when to publish]
```

---

## Chapter 21: Escalation System

### 21.1 Signal Detection Mechanisms

Each specialist skill includes explicit "escalation signals" — conditions that trigger a handoff to another skill.

**How it works:**

1. During analysis, the skill monitors for specific patterns
2. When a signal matches, it flags the issue
3. The system recommends escalation to the appropriate skill
4. Context is preserved through file references

**Example signals from various skills:**

| Signal | Detected By | Escalates To |
|--------|-------------|--------------|
| Content driving traffic but not conversions | marketing-content | marketing-cro |
| High-value topic requiring nurture depth | marketing-content | marketing-email |
| Pricing/positioning mismatch | marketing-retention | marketing-pricing |
| Traffic source quality issue | marketing-retention | marketing-paid-ads |
| Low deliverability despite compliance | marketing-email | marketing-pr |
| Engagement drop after campaign | marketing-email | marketing-analytics |

---

### 21.2 Complete Escalation Map

The following diagram shows all skills and their escalation routes:

```
                                    ┌─────────────────────┐
                                    │  paw-mkt-agent-agency   │
                                    │    (Coordinator)    │
                                    └─────────┬───────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
                    v                         v                         v
           ┌────────────────┐       ┌────────────────┐       ┌────────────────┐
           │ marketing-sostac│       │ marketing-seo  │       │marketing-content│
           └───────┬────────┘       └───────┬────────┘       └───────┬────────┘
                   │                        │                        │
         ┌─────────┼─────────┐      ┌───────┼───────┐       ┌────────┼────────┐
         │         │         │      │       │       │       │        │        │
         v         v         v      v       v       v       v        v        v
    ┌─────────┐ ┌─────────┐ ┌──────────┐ │  ┌─────────┐  ┌─────────┐ ┌─────────┐
    │ paid-ads│ │ social  │ │  email   │ │  │   cro   │  │analytics│ │   seo   │
    └────┬────┘ └────┬────┘ └────┬─────┘ │  └────┬────┘  └────┬────┘ └────┬────┘
         │          │           │       │       │            │           │
         v          v           v       └───────┼────────────┼───────────┘
    ┌─────────┐ ┌─────────┐ ┌─────────┐         │            │
    │influencer│ │ video  │ │retention│    ┌────┴────┐  ┌─────┴─────┐
    └────┬────┘ └────┬────┘ └────┬────┘    │ pricing │  │ psychology│
         │          │           │         └────┬────┘  └─────┬─────┘
         │          │           │              │             │
         v          v           v              v             v
    ┌─────────────────────────────────────────────────────────────┐
    │                     Specialist Skills                        │
    │  launch • community • guerrilla • referral • pr • sales     │
    └─────────────────────────────────────────────────────────────┘
```

---

### 21.3 When Skills Hand Off to Each Other

Each skill defines explicit escalation routes. Here are the key handoff patterns:

#### From marketing-content

| Signal Detected | Escalate To | Reason |
|-----------------|-------------|--------|
| Content driving traffic but not conversions | marketing-cro | Conversion path optimization needed |
| High-value topic requiring nurture depth | marketing-email | Adapt into email sequence |
| Research/data with PR potential | marketing-pr | Earned media opportunity |
| Content gaps in specific funnel stage | marketing-analytics | Funnel analysis needed |
| SEO keyword research needed | marketing-seo | Keyword research and technical SEO |
| Social distribution needed | marketing-social | Social distribution and engagement |
| Video production beyond scripting | marketing-video | Video production support |

#### From marketing-video

| Signal Detected | Escalate To | Reason |
|-----------------|-------------|--------|
| Social media strategy beyond video | marketing-social | Broader social strategy |
| Paid video ad campaign setup | marketing-paid-ads | Budget and campaign structure |
| Written content from transcripts | marketing-content | Blog/article creation |
| Influencer video collaborations | marketing-influencer | Influencer management |
| Video SEO technical implementation | marketing-seo | Schema, site embeds |
| No brand presence yet | marketing-sostac | Foundational setup needed |

#### From marketing-email

| Signal Detected | Escalate To | Reason |
|-----------------|-------------|--------|
| Low deliverability despite compliance | marketing-pr | Reputation/recovery needed |
| High unsubscribe on specific content | marketing-content | Content strategy issue |
| Engagement drop after campaign | marketing-analytics | Performance analysis |
| Win-back showing product exits | marketing-retention | Retention intervention |
| Lead magnet conversion declining | marketing-cro | Landing page optimization |
| High intent segment not converting | marketing-sales | Sales enablement needed |

#### From marketing-retention

| Signal Detected | Escalate To | Reason |
|-----------------|-------------|--------|
| Pricing/positioning mismatch | marketing-pricing | Pricing strategy issue |
| Traffic source quality issue | marketing-paid-ads | Acquisition quality |
| Onboarding activation failure | marketing-cro | Activation optimization |
| Email deliverability issues | marketing-email | Technical delivery |
| Educational content gap | marketing-content | Content to reduce churn |

#### From marketing-launch

| Signal Detected | Escalate To | Reason |
|-----------------|-------------|--------|
| Press release and journalist outreach | marketing-pr | Media relations |
| Post-launch email sequences | marketing-email | Email marketing |
| Paid retargeting | marketing-paid-ads | Paid media |
| Influencer seeding | marketing-influencer | Influencer management |
| Community building | marketing-community | Community strategy |
| SEO optimization | marketing-seo | Technical SEO |
| Video production | marketing-video | Video production |
| Analytics and attribution | marketing-analytics | Measurement |
| No SOSTAC plan exists | marketing-sostac | Strategy foundation |

---

### 21.4 Seamless Transition Examples

#### Example 1: Content to CRO

**Scenario:** You're working on blog content, but the system detects low conversion rates.

```
Skill: marketing-content
Status: Blog post draft delivered

Signal Detected: Your analytics show this content drives traffic
but conversion rate is 0.5% vs 2% industry benchmark.

Recommendation: Route to marketing-cro for landing page optimization.
Shall I proceed with the CRO analysis?
```

**Transition:**
- marketing-cro reads the content, brand context, and analytics
- Focuses on CTAs, conversion paths, and page optimization
- Returns specific recommendations to improve conversion

#### Example 2: Video to Paid Ads

**Scenario:** You're creating video scripts, but need paid distribution strategy.

```
Skill: marketing-video
Status: Video ad script completed

Signal Detected: This script is designed for paid distribution.
The creative is ready, but campaign structure and budget
planning require marketing-paid-ads.

Recommendation: Route to marketing-paid-ads for campaign setup.
```

**Transition:**
- marketing-paid-ads reads the video brief and brand context
- Develops platform strategy, targeting, and budget allocation
- Coordinates with the video deliverables

---

### 21.5 Bidirectional Escalation

Escalation is not one-way. Skills can send work back when conditions change.

#### Example: Email to Content and Back

1. **marketing-email** creates a welcome sequence
2. Detects that the brand story email needs deeper content
3. Escalates to **marketing-content** for brand story article
4. **marketing-content** delivers the article
5. **marketing-email** adapts it into the sequence

#### Example: Retention to Pricing and Back

1. **marketing-retention** analyzes churn
2. Detects pricing sensitivity in exit surveys
3. Escalates to **marketing-pricing** for pricing analysis
4. **marketing-pricing** recommends adjustment
5. **marketing-retention** designs win-back offers around new pricing

This bidirectional flow ensures each skill contributes its expertise while maintaining overall coherence.

---

## Summary

The Agentic Marketing Skills system provides sophisticated capabilities through:

- **Smart Framework Selection** — Progressive disclosure ensures efficient, relevant framework loading
- **Research-First Approach** — Comprehensive auto-discovery reduces user burden
- **Progressive Delivery** — File-based outputs create audit trails and enable resumption
- **Intelligent Escalation** — Signal detection routes work to the right specialist

Understanding these mechanisms helps you work more effectively with the system and leverage its full potential.

---

*Next: Part 7 — Troubleshooting & FAQ*