# Tier Structure Design

> Three tiers is optimal for most products. Fewer limits revenue capture. Four or more creates decision paralysis.

---

## 1. The Three-Tier Framework

| Tier | Role | Pricing | Customer Type |
|---|---|---|---|
| Starter / Free | Lead generation, top-of-funnel | Free or very low ($0-$29/mo) | Self-serve, price-sensitive, early-stage |
| Professional / Core | Primary revenue tier, most popular | Mid-range ($49-$299/mo) | Core persona, growing team |
| Business / Enterprise | Maximum value capture | High or custom ($299+/mo or quote) | Power users, large teams, compliance needs |

---

## 2. What to Gate and What to Include

Feature gating strategy determines which tier a customer chooses.

### 2.1 What to Gate

- **Value metric limits** (seats, contacts, API calls, projects)—quantitative gates that create natural upgrade triggers
- **Power features** (advanced analytics, automation, API access, custom integrations)—qualitative gates for advanced users
- **Workflow features** (approval flows, multi-user collaboration, audit logs)—organizational gates for teams and enterprises
- **Support tier** (community-only, email support, priority support, dedicated CSM)—service differentiation
- **Security and compliance** (SSO/SAML, custom data retention, SOC2 docs, SLA)—enterprise table-stakes

### 2.2 What Not to Gate

- Core features that define your product's promise—gating these creates a "crippled free plan" that frustrates users
- Features necessary for the customer to reach their first success moment (aha moment)
- Integration with tools the customer already depends on (unless your integrations are a premium moat)

---

## 3. Tier Naming

Avoid generic names (Basic / Standard / Pro)—they communicate nothing. Use names that reflect the customer's identity or stage:

- **Journey-based**: Starter > Growth > Scale
- **Role-based**: Individual > Team > Enterprise
- **Outcome-based**: Launch > Grow > Dominate
- **Brand-specific**: Name after your brand's personas or values

---

## 4. Decoy Pricing

The middle tier is the decoy. It is priced to make the top tier look reasonable.

```
Starter:      $29/mo  — real option for budget buyers
Professional: $99/mo  — decoy; anchors against Enterprise
Enterprise:   $149/mo — looks like only $50 more than Pro; most choose this
```

The price gap between Professional and Enterprise should be small enough that Enterprise feels like the obvious choice. The Professional tier takes the price shock.

---

## 5. Price Increase Sizing

When raising prices:
- Increases of 10-20% rarely cause significant churn if communicated well.
- Increases of 20-40% require strong justification (major new value delivered).
- Increases over 40% require grandfathering existing customers and a long transition window.

Test price increases on new customers first before rolling out to existing base.

---

## Deliverables

| Deliverable | Filename | Key Sections |
|---|---|---|
| Pricing Strategy | `pricing-strategy-{YYYY-MM-DD}.md` | Tier names, prices, feature gates, rationale, expansion mechanism |