# Feature Definition

## Outcome

Define the product's core value and feature set with enough specificity that developers can build without clarification sessions.

## Trigger

User requests feature definition, feature specification, or "what should this product do?"

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Product context | `curated/product-context.md` | Yes |
| Audience intelligence | `curated/audience-intelligence.md` | Yes |
| Market intelligence | `curated/market-intelligence.md` | Optional |

## Process

### 1. Establish Value Proposition

Before defining features, articulate the core value:

- **Primary value**: What is the main problem this product solves?
- **Target user**: Who experiences this problem most acutely?
- **Key differentiator**: Why would they choose this over alternatives?
- **Success metric**: How do we know the product is working?

Write this as a single paragraph. If you can't, the product needs more definition.

### 2. Define Feature Categories

Group features into logical categories that reflect user mental models:

```
Category: [Name]
Purpose: [What this category enables]
Priority: [Core / Important / Nice-to-have]
Features:
  - Feature A: [Description]
  - Feature B: [Description]
  - Feature C: [Description]
```

**Common categories for SaaS:**
- Onboarding & Account
- Core Workflow
- Data & Reporting
- Settings & Configuration
- Collaboration & Sharing
- Billing & Administration

**Common categories for AI Tools:**
- Input & Prompting
- Generation & Processing
- Output & Export
- Management & Organization
- Integration & API

### 3. Write Feature Specifications

For each feature, define:

```markdown
## Feature: [Name]

**Priority**: [P0 - Critical / P1 - Important / P2 - Nice-to-have]
**Category**: [Category name]
**Status**: [Defined / Needs Decision / Blocked]

### Description
[One paragraph describing what this feature does and why it matters]

### User Story
As a [user type], I want to [action] so that [benefit].

### Acceptance Criteria
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

### Scope
**In scope:**
- [What this feature includes]

**Out of scope:**
- [What this feature explicitly excludes]

### Dependencies
- [Other features or systems this depends on]

### Technical Notes
[Any technical constraints or considerations]
```

### 4. Prioritize with MoSCoW

Apply MoSCoW prioritization to all features:

| Priority | Definition | Criteria |
|----------|------------|----------|
| **Must Have** | Non-negotiable for launch | Core value prop depends on it |
| **Should Have** | Important but not critical | Significant user value, workarounds exist |
| **Could Have** | Nice to have if time permits | Enhances experience, not essential |
| **Won't Have** | Explicitly excluded for now | Documented for future consideration |

### 5. Create Feature Dependency Map

Identify relationships between features:

```
[Feature A] → enables → [Feature B]
[Feature C] → depends on → [Feature A]
[Feature D] → conflicts with → [Feature E]
```

This informs build order and MVP scoping.

## Output

**Format:** Markdown document

**Structure:**
1. Value proposition
2. Feature categories (grouped)
3. Feature specifications (detailed)
4. Priority matrix (MoSCoW)
5. Dependency map

**Location:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/feature-spec.md`

**Naming:** `feature-spec.md`

## Quality Checklist

Before delivery, verify:

- [ ] Value proposition is single-paragraph clear
- [ ] Every feature has a user story
- [ ] Every feature has acceptance criteria
- [ ] Scope boundaries are explicit (in/out)
- [ ] Priorities are assigned with reasoning
- [ ] Dependencies are mapped
- [ ] No feature requires clarification to understand

## Common Mistakes

1. **Feature creep** — Defining too many features before validating core value
2. **Vague acceptance criteria** — "User can manage settings" is not testable
3. **Missing scope boundaries** — What's excluded is as important as what's included
4. **Ignoring dependencies** — Build order matters
5. **Prioritizing everything high** — If everything is critical, nothing is

## Example Output

```markdown
## Feature: User Authentication

**Priority**: P0 - Critical
**Category**: Onboarding & Account
**Status**: Defined

### Description
Enables users to create accounts, authenticate securely, and manage their identity within the product. This is foundational for personalized experiences and data security.

### User Story
As a new user, I want to create an account with my email so that I can access my data across devices.

### Acceptance Criteria
- [ ] Given a valid email and password, when user submits signup form, then account is created and verification email is sent
- [ ] Given valid credentials, when user attempts login, then session is established and user is redirected to dashboard
- [ ] Given a registered email, when user requests password reset, then reset link is sent to email

### Scope
**In scope:**
- Email/password signup and login
- Email verification
- Password reset flow
- Session management
- Logout

**Out of scope:**
- Social login (Google, GitHub)
- SSO integration
- Two-factor authentication
- Magic link login

### Dependencies
- Email service provider (SendGrid/Postmark)
- Session storage (Redis/database)

### Technical Notes
- Use bcrypt for password hashing
- JWT for session tokens with 7-day expiry
- Rate limit login attempts (5 per minute)
```

## Escalation

If product context is unclear, escalate to `paw-ps-strategist` for product definition work before proceeding with feature definition.