# Signup CRO Reference: Signup Flows, Registration Pages, Trial Activation

**Purpose:** Specific frameworks, field-by-field optimization, and test ideas for improving signup, account creation, and trial start flows. Read this file when the user is optimizing a signup page, registration form, or trial activation flow.

---

## 1. Core Principles

### Principle 1: Minimize Required Fields
Every additional field reduces signup completion. Research baseline: each extra required field costs 10-20% completion rate. The minimum viable signup is: email + password. Everything else should be questioned, deferred, or made optional.

Ask about every field: "Do we need this to create the account, or do we just want it?"
- Need to create the account: keep it required.
- Want for marketing segmentation: make it optional or defer to onboarding.
- Want for product personalization: defer to post-signup setup flow.
- Can be inferred: infer it (company from email domain, country from IP).

### Principle 2: Show Value Before Asking for Commitment
What can a visitor see, do, or experience before they are required to sign up? Freemium demos, interactive product previews, and case study pages all reduce the perceived risk of signing up.

The sequence should feel like: "I want that → I'll sign up to get it" not "Sign up first, then maybe you'll find out if this is for you."

### Principle 3: Reduce Perceived Effort
- Progress indicators communicate that the form has a definable end.
- Smart defaults pre-fill what can be inferred (locale, timezone, plan from referral URL).
- Password requirements shown upfront prevent validation errors mid-flow.
- Allow paste in all fields (many users paste email addresses and passwords from password managers).

### Principle 4: Remove Uncertainty
The visitor's mental model at the signup form is: "What am I committing to? What happens next? Will they spam me? Do I need a credit card?" Address all of these at the form, not just on the landing page above it.

---

## 2. Field-by-Field Optimization

### Email field
- Single field, full width.
- Use `type="email"` to trigger email keyboard on mobile and enable browser validation.
- Inline validation: confirm valid format as the user types (green checkmark), flag errors immediately (do not wait until submit).
- Typo detection: detect common typos (gmial.com → gmail.com, yaho.com → yahoo.com) and suggest corrections inline.
- Placeholder text: "you@company.com" sets context for expected format; remove the placeholder when the user starts typing.

### Password field
- Show/hide toggle (the eye icon) is now standard — must include.
- Show password requirements before the user starts typing, not after their first error.
- Never block paste — users with password managers will abandon if paste is blocked.
- Minimum requirements: 8 characters, mix of character types. Do not make requirements so complex that users give up.
- Consider passwordless options (magic link, passkey) for B2C products with less-technical audiences.

### Name field
- Single "Full name" field outperforms First Name + Last Name fields in most tests. First/Last adds a field; Full Name is one field.
- Exception: if personalization requires the split (e.g., "Hi [first name]" in email), then split — but consider splitting programmatically from a single input.
- Consider making name optional for self-serve, low-touch products. Many users give fake names anyway.

### Social authentication (Google, Apple, SSO)
- B2C products: prioritize Google Sign-In and Apple Sign-In (for iOS users) above the email form. SSO dramatically reduces friction.
- B2B products: Google Sign-In and Microsoft Sign-In. Enterprise buyers increasingly expect SSO (SAML/OIDC) — include an "Enterprise SSO" link.
- Visual treatment: SSO buttons should be as prominent as the email form, not secondary links.
- One-click social auth consistently outperforms email/password for products where speed of signup matters.

### Company name field
- Often asked too early. Defer to post-signup onboarding when possible.
- If required: use autocomplete with a company database (Clearbit Autocomplete is free) — users want to select, not type.
- Infer from email domain when the domain is a business domain (not gmail, hotmail, outlook, etc.).

### Role / team size dropdowns
- Almost always deferrable to onboarding. Remove from the signup form unless required for routing (e.g., enterprise vs. self-serve split).
- If present: 5 options maximum, pre-select the most common option.

### Phone number
- B2B: avoid unless required for SMS 2FA or sales routing. Phone fields cause significant abandonment.
- If required for 2FA: explain why ("We'll use this to secure your account — no marketing texts").
- If you must include it: make it optional with a clear label ("Optional — for account security").

---

## 3. Single-Step vs. Multi-Step Decision

### Use single-step when:
- 3 or fewer fields total.
- Traffic is high-intent (branded search, trial CTA from pricing page).
- Product is self-serve with no segmentation needed.

### Use multi-step when:
- 4+ fields are genuinely required.
- B2B product needs segmentation for routing (enterprise vs. SMB, or sales vs. self-serve).
- You want to collect email first so partial completions can be followed up.

### Progressive commitment (multi-step best practice):

```
Step 1: Email only → "Continue with email"
  -- Capture email for re-engagement if they drop off here --

Step 2: Password + Full name → "Create account"
  -- Account created, user is now registered even if they stop --

Step 3: Personalization / segmentation questions (optional)
  "Help us personalize your experience"
  Company size / role / use case (3 questions max)
  -- Skip link available: "I'll do this later" --

Step 4: Welcome screen + immediate product entry
```

Capturing email on Step 1 means every abandonment after that can be followed up via email automation.

### Progress indicator rules:
- Show step X of Y ("Step 1 of 3").
- Dots, numbered circles, or a progress bar all work — pick one, keep it consistent.
- Do not show steps the user cannot see or predict (hidden steps feel like a bait-and-switch).

---

## 4. Trust Signals at the Signup Form

These belong at the form level, not just on the page above it:

| Signal | Where to place it | Example copy |
|---|---|---|
| No credit card | Directly below the primary CTA button | "No credit card required" |
| Free trial clarity | Below CTA or in the heading | "14-day free trial, then $49/month" |
| Cancel anytime | Below CTA | "Cancel anytime, no lock-in" |
| Privacy assurance | Below email field | "No spam. Unsubscribe anytime." or a link to privacy policy |
| Security | Near the form | SOC 2, GDPR badge, SSL padlock |
| Company count | Above or near the form | "Join 12,000+ teams already using [Product]" |

Do not cluster all of these — pick the 2-3 most relevant to the primary objection for this audience. B2B security-conscious buyers need different signals than B2C consumers.

---

## 5. Post-Submit Experience

The moment after clicking the CTA button is high-stakes. Users are in peak commitment mode. Do not waste it.

### Email and password signup (immediate account creation):
- Redirect immediately to the product with a welcome message.
- If email verification is required: explain clearly what happens, show an easy resend button, allow partial product access while verifying.
- Do NOT show a blank dashboard. Show an onboarding step immediately (see onboarding-cro.md).

### Email verification flow (when required):
```
"Check your inbox — we sent a confirmation link to [email]"
  [Resend email] button (visible immediately, not after 60 seconds)
  [Change email address] link
  "Can't find it? Check your spam folder."
  Optional: allow limited product access before verification
```

### Social auth (OAuth):
- Return immediately to product after OAuth handshake.
- First-time users: show a brief "Complete your profile" step if any required fields are missing.
- Returning users (re-auth): redirect to last page visited, not the dashboard root.

### Confirmation page:
- If redirecting to a confirmation page (rare, but happens): include a clear "Open my email" button that deep-links to the user's email provider (Gmail, Outlook).
- Always include the product CTA even on the confirmation page — some users verify email much later.

---

## 6. Social Auth vs. Email Form Layout

### Layout A: SSO Prominent
```
[Sign in with Google]
[Sign in with Microsoft]
──── or ────
[Email form]
```
Best for: B2C products, developer tools, modern SaaS with younger audiences.

### Layout B: Email Form Prominent
```
[Email form]
──── or ────
[Sign in with Google]
```
Best for: Enterprise products where SSO/SAML is a different flow, email-centric products.

### Layout C: Unified (recommended for most products)
```
[Email field]
[Continue]
  → Backend detects: SSO domain? Route to SSO.
  → Regular email? Show password field.
```
This "smart email-first" pattern is used by Notion, Linear, Figma. Reduces visual clutter. Works well for B2B where some users have SSO and others do not.

---

## 7. Test Hypotheses for Signup CRO

| Hypothesis | Primary metric | Effort |
|---|---|---|
| Removing company name field increases signup completion | Signup completion rate | Low |
| "Continue with Google" as the primary CTA above the email form | Signup completion rate | Medium |
| Multi-step flow (email first) vs. single-step improves re-engagement of partial signups | 7-day activation rate | Medium |
| "No credit card required" added directly below the CTA | Signup start rate | Low |
| Single "Full name" field vs. "First name + Last name" | Signup completion rate | Low |
| Passwordless / magic link for B2C | Signup completion rate | High |
| Pre-selected plan based on referral URL (e.g., from pricing page Pro CTA) | Signup-to-trial-upgrade | Medium |
| CTA copy: "Create Account" vs. "Start Free Trial" vs. "Get Started" | Signup start rate | Low |

---

## 8. Signup Form Quick Wins Checklist

Changes that require no development time:

- [ ] Add "No credit card required" directly below the signup button
- [ ] Remove any non-essential fields (phone, company size, role) from the initial form
- [ ] Add show/hide toggle to password field
- [ ] Show password requirements before user starts typing (not after their first error)
- [ ] Change CTA button copy from "Sign Up" or "Submit" to "Start Free Trial" or "Create My Account"
- [ ] Add a privacy assurance note below the email field
- [ ] Confirm email field uses `type="email"` (triggers correct mobile keyboard)
- [ ] Remove `autocomplete="off"` from any fields (it blocks password managers)
- [ ] Add a "Sign in with Google" button if not already present
- [ ] Ensure the submit button is visible without scrolling on mobile (390px viewport)

---

## 9. Signup Benchmarks

| Product type | Typical signup CVR | Notes |
|---|---|---|
| Self-serve SaaS (freemium) | 25-45% of landing page visitors | Highly dependent on traffic quality |
| Self-serve SaaS (free trial, CC required) | 2-8% of landing page visitors | CC requirement reduces volume significantly |
| Self-serve SaaS (free trial, no CC) | 10-25% of landing page visitors | Volume is higher; quality varies |
| B2B (demo-led) | 1-5% of landing page visitors | Intentional filter — lower volume, higher quality |
| E-commerce account creation | 20-50% at checkout | Context matters: forced vs. optional |

**Note:** These are landing-page-to-signup rates. Form-start-to-form-complete rates (for visitors who click the CTA and begin the form) should be 50-80% for a well-optimized flow. Below 50% completion after starting the form indicates significant friction in the form itself.
