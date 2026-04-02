# Automation Workflows

Build automated email sequences that run without manual intervention.

## Trigger-Action Logic

Every automation follows this structure:

```
Trigger (event starts workflow)
  > Condition (filter who qualifies)
  > Action (what happens)
  > Delay (wait period)
  > Branch (if/then logic based on behavior)
```

## Core Automation Workflows

### Lead Capture to Nurture

```
Trigger: form submission
  > Email 1: welcome (immediate)
  > Email 2: value email (day 1)
  > Check engagement:
    - If opens: continue nurture
    - If not: send re-engagement variant
  > Continue until sales-ready signal
  > Transfer to sales sequence
```

### Abandoned Cart Recovery

```
Trigger: cart abandoned (1hr)
  > Email 1: reminder + social proof (existing customers skip discount)
  > Wait 24hr
  > Email 2: objection-handling
  > Wait 48hr
  > Email 3: final with incentive
  > Exit on purchase at any stage
  > Tag as "cart abandoner" for retargeting
```

### Post-Purchase Loyalty Loop

```
Trigger: purchase
  > Confirmation email
  > Check-in after delivery
  > Review request (7d)
    - If review: thank-you + referral ask
    - If no review: gentle reminder
  > Cross-sell (30d)
  > Enter repurchase reminder cycle
```

### Engagement-Based Scoring

```
Track behavior:
  +1 open
  +3 click
  +5 pricing page visit
  +10 demo/trial request

Score > 20: transfer to sales sequence
No engagement 30d: enter re-engagement sequence
```

## Workflow Best Practices

- **Always include exit conditions** - purchase, unsubscribe, goal achieved
- **Set frequency caps** - no more than 1 automated email per day per subscriber (excluding transactional)
- **Tag subscribers** - entering and exiting workflows for reporting
- **Test with seed addresses** - before activation
- **Review monthly** - pause underperformers

## Frequency Caps Across Workflows

| Subscriber State | Max Emails/Day |
|---|---|
| Active in multiple workflows | 1 automated (exclude transactional) |
| Transactional only | No limit |
| Re-engagement sequence | 1 per 3 days minimum |