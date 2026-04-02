# Retention Research Playbook

> `agent-browser` commands for live competitive and benchmark research on cancel flows, dunning patterns, and industry retention data.

> **Setup:** Before running research, check if `agent-browser` is available (`agent-browser --version`). If the command is not found, install it: `npm install -g agent-browser && npx playwright install chromium`. If installation fails, use `WebFetch` and `WebSearch` tools as alternatives for all research tasks in this playbook.

---

## 1. Competitor Cancel Flow Research

```bash
# Examine a competitor's cancellation experience (requires having an account or trial)
agent-browser --session retention-research open "https://{competitor}.com/settings/cancel" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser screenshot ./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/retention/competitor-cancel-flow-{competitor}.png
agent-browser get text body
# Look for: exit survey questions, offer types, pause options, friction tactics, UX tone
```

---

## 2. Industry Cancel Flow Examples (Churnkey Blog & Case Studies)

```bash
agent-browser --session retention-research open "https://churnkey.co/blog" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: save rates benchmarks, offer types that work by industry, UX best practices
```

---

## 3. Dunning Email Examples & Patterns (Really Good Emails)

```bash
agent-browser --session retention-research open "https://reallygoodemails.com/emails/type/dunning" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
# Extract: subject line patterns, tone (urgent vs friendly), CTA patterns, timing notes
```

---

## 4. Retention Benchmark Data (Baremetrics Open Benchmarks)

```bash
agent-browser --session retention-research open "https://baremetrics.com/benchmarks" && agent-browser wait --load networkidle && agent-browser wait 3000
agent-browser get text body
# Extract: median churn rates by ARR band, trial conversion rates, MRR growth rates
```

---

## 5. ProsperStack / Churnkey Feature Research

```bash
agent-browser --session retention-research open "https://prosperstack.com/features" && agent-browser wait --load networkidle
agent-browser get text body
# Extract: cancel flow capability comparison, pricing signals, integration options

agent-browser --session retention-research open "https://churnkey.co/features" && agent-browser wait --load networkidle
agent-browser get text body
```

---

## 6. Stripe Smart Retries Documentation

```bash
agent-browser --session retention-research open "https://stripe.com/docs/billing/revenue-recovery" && agent-browser wait --load networkidle && agent-browser wait 2000
agent-browser get text body
# Extract: Smart Retry logic, card updater, dunning configuration options
```

---

Close the research session when done: `agent-browser --session retention-research close`
