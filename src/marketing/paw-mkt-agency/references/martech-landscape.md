# MarTech Stack Guide (2025-2026)

> Reference guide for the paw-mkt-agency skill. Covers marketing technology recommendations
> by business stage, category leaders, integration architecture, AI tools, and stack audit
> guidance. Based on 2025-2026 market data and industry benchmarks.

---

## Market Context

- The MarTech landscape includes 15,400+ solutions across 49 categories (2025 count).
- Average company uses 80+ MarTech tools; yet MarTech utilization has dropped to 49% (Gartner 2025).
- The challenge in 2026 is not adding more tools — it is building a stack that makes execution simpler, faster, and more measurable.
- SaaS prices rose 11.4% YoY (Vertice SaaS Inflation Index), making stack efficiency critical.
- Marketing budgets remain flat at 7.7% of company revenue (Gartner CMO Survey 2025).

---

## 1. Stack by Business Stage

### Startup Stack ($0-50/month)

**Goal**: Validate product-market fit, build initial audience, track basic metrics.

| Category | Tool | Cost | Notes |
|---|---|---|---|
| Website / CMS | WordPress.com or Carrd | Free-$12/mo | Quick launch, SEO-friendly |
| Analytics | Google Analytics 4 (GA4) | Free | Essential from day one |
| Search Console | Google Search Console | Free | Monitor organic search |
| Email | Mailchimp (free tier) | Free (up to 500 contacts) | Basic automations |
| Social Scheduling | Buffer (free tier) | Free (3 channels) | Schedule and publish |
| CRM | HubSpot CRM (free tier) | Free | Contact management, pipeline |
| Design | Canva (free tier) | Free | Social graphics, basic design |
| SEO Research | Ubersuggest (free tier) or Google Keyword Planner | Free | Basic keyword research |
| Forms / Surveys | Google Forms or Tally | Free | Lead capture, surveys |
| Project Management | Notion (free) or Trello (free) | Free | Task tracking, docs |

**Total**: $0-$12/month
**Priority**: Analytics setup, email capture, one or two social channels, basic content.

### Growth Stack ($50-500/month)

**Goal**: Scale proven channels, automate workflows, build a data-driven marketing engine.

| Category | Tool | Cost | Notes |
|---|---|---|---|
| Website / CMS | WordPress + hosting (SiteGround/Cloudways) or Webflow | $15-$40/mo | Full control, scalable |
| Analytics | GA4 + Hotjar (Basic) | Free-$32/mo | Heatmaps, session recordings |
| Email & Automation | ConvertKit or Mailchimp Standard | $25-$60/mo | Sequences, segmentation |
| CRM | HubSpot Starter or Pipedrive | $15-$50/mo | Deal tracking, automation |
| SEO | Ahrefs Lite or SEMrush Pro (shared via agency) | $29-$130/mo | Rank tracking, audits |
| Social Management | Buffer Pro or Later | $15-$25/mo | Multi-channel scheduling |
| Design | Canva Pro | $13/mo | Brand kit, templates |
| Ads | Google Ads + Meta Ads Manager | Variable (ad spend) | Self-serve platforms |
| Landing Pages | Carrd Pro or Unbounce Starter | $8-$90/mo | Conversion-focused pages |
| Project Management | Asana Starter or ClickUp | $7-$11/user/mo | Team collaboration |

**Total**: $50-$500/month (excluding ad spend)
**Priority**: Marketing automation, proper CRM, SEO tooling, conversion tracking, A/B testing.

### Scale Stack ($500-5,000/month)

**Goal**: Optimize across channels, implement advanced personalization, build data infrastructure.

| Category | Tool | Cost | Notes |
|---|---|---|---|
| CMS | WordPress (custom) or Webflow | $30-$100/mo | Enterprise-grade |
| Analytics | GA4 + Mixpanel or Amplitude | $0-$500/mo | Product + marketing analytics |
| Marketing Automation | HubSpot Professional or ActiveCampaign Plus | $100-$800/mo | Advanced workflows, scoring |
| CRM | HubSpot Professional or Salesforce Essentials | $100-$300/mo | Full pipeline management |
| Email | Klaviyo (ecom) or ActiveCampaign | $60-$500/mo | Advanced segmentation, AI |
| SEO | Ahrefs Standard or SEMrush Guru | $130-$250/mo | Full suite, site audit |
| Social | Sprout Social or Hootsuite Professional | $99-$249/mo | Analytics, listening, inbox |
| Ads Management | Google Ads + Meta + LinkedIn Ads | Variable | Multi-platform campaigns |
| CRO | Optimizely or VWO | $50-$500/mo | A/B testing, personalization |
| CDP / Data | Segment (free tier) or RudderStack | $0-$500/mo | Unified customer data |
| Reporting | AgencyAnalytics or Databox | $50-$200/mo | Client dashboards |
| Project Management | Asana Business or Monday Pro | $20-$25/user/mo | Advanced features |
| Design | Figma + Canva Pro | $15-$45/mo | Design system + daily content |
| Chat / Support | Intercom Starter or Drift | $74-$200/mo | Lead capture, support |

**Total**: $500-$5,000/month (excluding ad spend)
**Priority**: CDP layer, advanced automation, attribution modeling, cross-channel optimization.

### Enterprise Stack ($5,000+/month)

**Goal**: Full marketing operations platform, predictive analytics, real-time personalization, global scale.

| Category | Tool | Cost | Notes |
|---|---|---|---|
| Marketing Platform | HubSpot Enterprise or Marketo (Adobe) | $800-$5,000+/mo | Full marketing suite |
| CRM | Salesforce Sales Cloud or HubSpot Enterprise | $300-$2,000+/mo | Enterprise CRM |
| CDP | Segment Business or Treasure Data or Tealium | $500-$5,000+/mo | Enterprise data unification |
| Email | Braze or Iterable | $1,000-$5,000+/mo | Real-time messaging at scale |
| Analytics | Amplitude or Mixpanel + Looker (BI) | $500-$3,000+/mo | Deep product analytics |
| SEO | Ahrefs Enterprise or Conductor or BrightEdge | $500-$3,000+/mo | Enterprise SEO platform |
| Social | Sprout Social Advanced or Brandwatch | $300-$1,000+/mo | Social listening, analytics |
| Personalization | Dynamic Yield or Optimizely | $500-$5,000+/mo | Real-time personalization |
| Attribution | Triple Whale (ecom) or Rockerbox or Northbeam | $200-$2,000+/mo | Multi-touch attribution |
| Data Warehouse | BigQuery or Snowflake | $100-$2,000+/mo | Central data repository |
| Reverse ETL | Census or Hightouch | $200-$1,000+/mo | Activate warehouse data |
| DAM | Canto or Bynder | $500-$2,000+/mo | Digital asset management |
| Project Management | Wrike or Workfront (Adobe) | $25-$50/user/mo | Enterprise PM |

**Total**: $5,000-$25,000+/month
**Priority**: Data infrastructure (CDP + warehouse), real-time personalization, attribution, marketing operations automation.

---

## 2. Category Leaders (2025-2026)

### CRM
| Tool | Best For | Starting Price | Key Differentiator |
|---|---|---|---|
| HubSpot | SMB to mid-market, all-in-one | Free-$800/mo | Integrated marketing + sales + service |
| Salesforce | Enterprise, complex B2B | $25-$300/user/mo | Customization, ecosystem, AppExchange |
| Pipedrive | Sales-focused SMBs | $14-$99/user/mo | Visual pipeline, ease of use |
| Zoho CRM | Budget-conscious teams | $14-$52/user/mo | Value, Zoho ecosystem integration |
| Close | Inside sales teams | $29-$139/user/mo | Built-in calling, email sequences |

### Email Marketing & Automation
| Tool | Best For | Starting Price | Key Differentiator |
|---|---|---|---|
| Klaviyo | Ecommerce (Shopify, BigCommerce) | Free-$60+/mo | Revenue attribution, predictive analytics |
| Mailchimp | Small business generalists | Free-$20+/mo | Ease of use, broad integrations |
| ConvertKit (Kit) | Creators and solopreneurs | Free-$25+/mo | Creator-focused, visual automations |
| ActiveCampaign | Automation-heavy SMBs | $29+/mo | Advanced workflows, CRM included |
| Braze | Enterprise real-time messaging | Custom pricing | Cross-channel, real-time, AI optimization |
| Beehiiv | Newsletter-first businesses | Free-$42+/mo | Newsletter monetization, growth tools |

### Analytics
| Tool | Best For | Starting Price | Key Differentiator |
|---|---|---|---|
| Google Analytics 4 | Universal web analytics | Free | Google ecosystem, event-based model |
| Mixpanel | Product analytics (SaaS, apps) | Free-$28+/mo | Event tracking, funnels, retention |
| Amplitude | Product-led growth analytics | Free-$49+/mo | Behavioral cohorts, experimentation |
| Heap | Auto-capture analytics | Custom pricing | Retroactive analytics, no manual tagging |
| PostHog | Open-source product analytics | Free-$450+/mo | Self-hosted option, feature flags |
| Plausible | Privacy-focused web analytics | $9+/mo | Lightweight, GDPR-compliant, no cookies |

### SEO
| Tool | Best For | Starting Price | Key Differentiator |
|---|---|---|---|
| Ahrefs | Backlink analysis, content research | $29-$449/mo | Best backlink index, content explorer |
| SEMrush | All-in-one SEO + PPC + content | $130-$500/mo | Broadest feature set, competitive intel |
| Moz Pro | Beginner-friendly SEO | $49-$299/mo | Domain Authority, local SEO |
| Screaming Frog | Technical SEO audits | Free-$259/yr | Deep crawl analysis |
| Surfer SEO | Content optimization | $69-$219/mo | SERP-based content scoring |
| Clearscope | Enterprise content optimization | $170+/mo | NLP-powered content grading |

### Social Media Management
| Tool | Best For | Starting Price | Key Differentiator |
|---|---|---|---|
| Buffer | Small teams, simple scheduling | Free-$6/channel/mo | Clean UI, affordable |
| Hootsuite | Mid-market, multi-channel | $99+/mo | Comprehensive, social listening |
| Sprout Social | Enterprise, analytics-heavy | $199+/seat/mo | Best analytics, employee advocacy |
| Later | Visual-first (Instagram, TikTok) | $16+/mo | Visual planner, Linkin.bio |
| Metricool | Budget-conscious teams | Free-$22+/mo | Affordable, competitor tracking |

### Advertising Platforms
| Platform | Best For | Minimum Spend | Key Use Case |
|---|---|---|---|
| Google Ads | Intent-based search + shopping | No minimum | Capture existing demand |
| Meta Ads (Facebook/Instagram) | Awareness + conversion, B2C | No minimum | Audience targeting, creative testing |
| LinkedIn Ads | B2B lead generation | $10/day recommended | Professional targeting, ABM |
| TikTok Ads | Younger demos, awareness | $50/day minimum campaign | Short-form video, viral potential |
| Microsoft Ads (Bing) | Older/professional demos | No minimum | Lower CPC, audience from LinkedIn |
| Reddit Ads | Niche communities | $5/day minimum | Interest-based targeting |
| Programmatic (DV360, The Trade Desk) | Enterprise, scale | $10K+/mo typically | Automated media buying, vast reach |

### CMS / Website Builders
| Tool | Best For | Starting Price | Key Differentiator |
|---|---|---|---|
| WordPress | Blogs, content-heavy sites | Free (self-hosted) | Ecosystem, flexibility, SEO |
| Webflow | Design-led marketing sites | $14-$39/mo | Visual builder, CMS, no code |
| Framer | Modern marketing sites | $5-$15/mo | Fast, design-focused, AI generation |
| Shopify | Ecommerce | $29-$299/mo | Best ecom ecosystem |
| Ghost | Newsletter + content sites | $9-$199/mo | Clean, fast, built-in memberships |
| Squarespace | Portfolio / small business | $16-$49/mo | Templates, ease of use |

---

## 3. Integration Architecture

### Core Integration Patterns

**Pattern 1: Simple Stack (Startup/Growth)**
```
Website (WordPress/Webflow)
    |
    v
Analytics (GA4) <--> Email (Mailchimp/ConvertKit)
    |
    v
CRM (HubSpot Free) <--> Forms (Native/Typeform)
```
- Direct integrations between tools (native connectors or Zapier).
- No middleware needed at this stage.
- Zapier/Make.com for bridging gaps: $20-$100/month.

**Pattern 2: Growth Stack (Integration Layer)**
```
Website  -->  CDP (Segment/RudderStack)  -->  Data Warehouse (BigQuery)
                     |                              |
                     v                              v
          Email Automation                   BI / Reporting
          CRM                                (Looker Studio)
          Ad Platforms (via Audiences)
          Analytics (Mixpanel/Amplitude)
```
- CDP acts as the "data spine" — collects events from all touchpoints, routes to all tools.
- Data warehouse stores historical data for advanced analysis.
- Cost: $200-$1,000/month for CDP + warehouse.

**Pattern 3: Enterprise Stack (Full Data Infrastructure)**
```
All Touchpoints  -->  CDP (Segment/Tealium)  -->  Data Warehouse (Snowflake/BigQuery)
                                                          |
                                                    Reverse ETL (Census/Hightouch)
                                                          |
                              +---------------------------+---------------------------+
                              |              |              |              |
                          CRM/MAP      Ad Platforms    Personalization  Analytics/BI
                       (Salesforce/    (Google/Meta/     (Dynamic       (Looker/
                        Marketo)       LinkedIn)          Yield)        Tableau)
```
- Reverse ETL activates warehouse data back into operational tools.
- Identity resolution layer unifies customer profiles across touchpoints.
- Marketing mix modeling (MMM) and multi-touch attribution run on warehouse data.

### Key Integration Tools
| Tool | Category | Cost | Purpose |
|---|---|---|---|
| Segment | CDP | Free-$120+/mo | Event collection, audience routing |
| RudderStack | CDP (open-source option) | Free-$500+/mo | Self-hosted CDP alternative |
| Zapier | Automation | $20-$100+/mo | No-code tool connections |
| Make (Integromat) | Automation | $9-$29+/mo | Advanced workflow automation |
| n8n | Automation (self-hosted) | Free-$20+/mo | Open-source alternative to Zapier |
| Fivetran | ETL / data pipeline | $100+/mo | Database to warehouse sync |
| Census | Reverse ETL | $200+/mo | Warehouse to SaaS sync |
| Hightouch | Reverse ETL | Free-$350+/mo | Activate warehouse audiences |

---

## 4. AI Marketing Tools (2025-2026)

### Content Creation & Copywriting
| Tool | Use Case | Cost | Notes |
|---|---|---|---|
| Jasper | Long-form AI copywriting | $39-$99+/mo | Brand voice training, campaigns |
| Copy.ai | Short-form copy, workflows | $36-$186+/mo | GTM workflows, lead enrichment |
| Writer | Enterprise content governance | Custom pricing | Brand consistency, compliance |
| ChatGPT (OpenAI) | General-purpose writing, ideation | $20+/mo | Versatile, plugins ecosystem |
| Claude (Anthropic) | Research, analysis, long-form | $20+/mo | Strong reasoning, large context |
| Surfer AI | SEO-optimized articles | $69+/mo | SERP-driven content generation |

### Design & Visual Content
| Tool | Use Case | Cost | Notes |
|---|---|---|---|
| Canva AI (Magic Studio) | Graphic design, AI generation | $13/mo (Pro) | Text-to-image, magic resize |
| Midjourney | AI image generation | $10-$60/mo | High-quality creative images |
| Adobe Firefly | AI design within Creative Cloud | Included in CC ($55/mo) | Commercially safe AI images |
| Runway | AI video generation and editing | $12-$76+/mo | Text/image to video |
| LTX Studio | AI video creation | Free-$30+/mo | Script to video, marketing focus |
| Descript | Video/podcast editing with AI | $24-$33/mo | Text-based editing, transcription |

### Analytics & Intelligence
| Tool | Use Case | Cost | Notes |
|---|---|---|---|
| Amplitude AI | Predictive analytics | Included in paid plans | Anomaly detection, forecasting |
| Obviously AI | No-code predictive analytics | $75+/mo | Predict churn, LTV, conversions |
| Pecan AI | Predictive marketing models | Custom pricing | Low-code ML for marketers |
| Crayon | Competitive intelligence | Custom pricing | AI-powered competitor monitoring |
| SparkToro | Audience research | Free-$50+/mo | Discover where audiences engage |

### Personalization & Optimization
| Tool | Use Case | Cost | Notes |
|---|---|---|---|
| Dynamic Yield (Mastercard) | Real-time personalization | Custom pricing | Web, app, email personalization |
| Optimizely | A/B testing + personalization | Custom pricing | Feature flags, experimentation |
| Mutiny | B2B website personalization | Custom pricing | ABM-focused personalization |
| Intellimize | AI-driven CRO | Custom pricing | Autonomous A/B testing |

### AI Agents & Automation (Emerging 2025-2026)
- AI marketing agents that autonomously manage campaigns are emerging but still early.
- Common use cases in 2026: automated ad bidding (Google Performance Max, Meta Advantage+), AI-driven email send-time optimization, automated content briefs, dynamic audience segmentation.
- Key trend: "Agentic AI" — autonomous systems that plan, execute, and optimize marketing tasks with minimal human input.
- Caution: Keep human oversight for strategy, brand voice, compliance, and high-stakes decisions.

---

## 5. Build vs. Buy Decision Framework

### When to Buy (SaaS)
- The capability is not a core competitive differentiator.
- A mature SaaS solution exists with strong reviews and integrations.
- Time to value matters more than customization.
- The team lacks engineering resources for build and maintenance.
- Compliance and security are handled by the vendor.
- Total cost of ownership (TCO) of buy is lower than build over 3 years.

### When to Build (Custom)
- The capability is a core competitive differentiator.
- No SaaS solution fits the unique workflow or data model.
- Integration requirements are too complex for off-the-shelf connectors.
- Data sensitivity or regulatory requirements demand full control.
- The organization has engineering capacity and will maintain it long-term.
- Scale economics favor custom (high-volume, low-marginal-cost).

### Evaluation Criteria Matrix
| Criterion | Weight | SaaS Option (Score 1-5) | Custom Build (Score 1-5) |
|---|---|---|---|
| Time to deploy | 20% | | |
| Total cost (3-year TCO) | 20% | | |
| Customization needs | 15% | | |
| Integration with existing stack | 15% | | |
| Maintenance burden | 10% | | |
| Data control / security | 10% | | |
| Vendor lock-in risk | 5% | | |
| Team capability to build | 5% | | |
| **Weighted Score** | | | |

### Common Build vs. Buy Decisions
| Capability | Typical Decision | Reasoning |
|---|---|---|
| CRM | Buy | Mature market, complex to build, strong SaaS options |
| Email platform | Buy | Deliverability requires infrastructure; buy expertise |
| Analytics | Buy + customize | Buy platform (GA4/Mixpanel), customize dashboards |
| Landing pages | Buy | Webflow/Unbounce faster than custom builds |
| Attribution model | Build (on warehouse) | Custom models on your data > generic SaaS attribution |
| Content management | Buy (usually) | WordPress/Webflow unless highly custom needs |
| CDP | Buy (usually) | Segment/RudderStack unless massive scale justifies build |
| AI content tools | Buy | Fast-evolving space; build becomes outdated quickly |
| Data warehouse | Buy (managed) | BigQuery/Snowflake; never build your own warehouse |
| Internal dashboards | Build (on BI tools) | Custom dashboards on Looker Studio or Metabase |

---

## 6. Stack Audit Checklist

### When to Audit
- Annually (at minimum), or when:
  - Marketing budget is under pressure.
  - Team reports tool fatigue or confusion.
  - Data is inconsistent across tools.
  - New strategic initiative requires new capabilities.
  - Post-merger or acquisition (stack consolidation).

### Overlap Detection
- [ ] List all tools by category. Identify any categories with 2+ tools doing similar things.
- [ ] Common overlaps: CRM + marketing automation, multiple analytics tools, multiple social schedulers, overlapping project management tools.
- [ ] For each overlap: Compare features used, data quality, team preference. Consolidate to one.
- [ ] Check if platform upgrades can replace point solutions (e.g., HubSpot Professional replacing separate email + CRM + landing page tools).

### Cost Optimization
- [ ] Calculate total MarTech spend per month / per year.
- [ ] Calculate cost per tool per active user per month.
- [ ] Identify tools with annual contracts coming up for renewal — negotiate or evaluate alternatives.
- [ ] Check for unused seats (users who have not logged in for 60+ days).
- [ ] Look for free-tier or open-source alternatives for non-critical tools.
- [ ] Aggregate negotiation: Many vendors offer discounts for multi-year commits or bundled products.
- [ ] Target: MarTech spend below 5-8% of total marketing budget.

### Underutilization Signals
- [ ] Tool adoption below 50% of paid features / capabilities.
- [ ] Users logging in less than once per week for daily-use tools.
- [ ] Manual workarounds existing for tasks the tool should automate.
- [ ] Reports being exported and manipulated in spreadsheets instead of used natively.
- [ ] Integrations configured but not actively used for data flow.
- [ ] Training not conducted in the past 12 months.

### Data Quality Check
- [ ] Is customer data consistent across CRM, email, and analytics?
- [ ] Are UTM parameters standardized and consistently applied?
- [ ] Is GA4 event tracking complete and accurate?
- [ ] Are lead sources properly attributed across all tools?
- [ ] Is there a single source of truth for customer records (ideally CRM or CDP)?
- [ ] Are duplicate records being identified and merged?

### Security & Compliance
- [ ] All tools compliant with relevant regulations (GDPR, CCPA, HIPAA if applicable).
- [ ] Consent management platform (CMP) in place and properly configured.
- [ ] Data processing agreements (DPAs) signed with all vendors.
- [ ] Access controls reviewed: remove ex-employees, limit admin access.
- [ ] Two-factor authentication enabled on all marketing platforms.
- [ ] Regular audit of API keys and integrations.

### Stack Health Score
Rate each dimension 1-5 and calculate an average:

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Coverage (all needs met) | | |
| Integration quality | | |
| Data consistency | | |
| Team adoption | | |
| Cost efficiency | | |
| Scalability | | |
| Security / compliance | | |
| Vendor support quality | | |
| **Average Stack Health** | | |

Interpretation:
- 4.0-5.0: Healthy stack. Minor optimizations only.
- 3.0-3.9: Functional but has gaps. Prioritize top issues.
- 2.0-2.9: Significant problems. Plan a systematic overhaul.
- 1.0-1.9: Critical. Stack is actively hindering marketing performance.

---

## 7. Tool Selection Process

### Step-by-Step Evaluation
1. **Define Requirements**: Document must-have vs. nice-to-have features. Get input from all users.
2. **Research Options**: Identify 3-5 candidates per category. Use G2, Capterra, and peer recommendations.
3. **Shortlist**: Narrow to 2-3 based on feature fit, pricing, and reviews.
4. **Demo / Trial**: Request demos. Run free trials with real workflows (not just sandbox data).
5. **Integration Test**: Verify it connects with your existing stack. Test actual data flow.
6. **Reference Check**: Talk to current customers in similar industries or company sizes.
7. **Negotiate**: Ask for annual discounts, startup pricing, or pilot programs.
8. **Decision**: Score against criteria matrix. Present recommendation to stakeholders.
9. **Implementation Plan**: Document timeline, data migration, training, and success metrics.
10. **Post-Implementation Review**: Check adoption and value after 30, 60, and 90 days.

### Red Flags During Evaluation
- Vendor cannot provide references from similar-size companies.
- No native integration with your core tools (CRM, analytics).
- Pricing jumps dramatically at next tier.
- Contract requires 2+ year commitment with no exit clause.
- Support is email-only with no SLA for response times.
- Data export is difficult or proprietary format only.
- Product roadmap is unclear or focused on features you do not need.
