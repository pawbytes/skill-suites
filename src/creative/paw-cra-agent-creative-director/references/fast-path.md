# Fast-Path Mode (--yolo)

Skip discovery and validation gates when you know exactly what you want. For expert users and repeat campaigns.

## When to Use

- You've worked with Aria before and know the workflow
- Brand is already onboarded and you have the profile
- Deliverable specs are explicit (format, quantity, dimensions)
- Time-sensitive work needs to move fast
- Automating via CI/CD or scheduled tasks

## Activation

```
/paw-cra-agent-creative-director --yolo
```

Or in headless mode:
```
/paw-cra-agent-creative-director --headless:execute --yolo
```

## What Gets Skipped

| Normal Flow | Fast-Path Behavior |
|-------------|-------------------|
| Tool discovery | Assume tools available (fail on error) |
| Brand confirmation | Use specified brand or active brand |
| Brief validation gate | Skip Strategist validation |
| Quality control checkpoints | Auto-approve basic checks |
| Progress confirmations | Execute without asking |

## Requirements for Fast-Path

Fast-path requires explicit specs to prevent errors:

**Minimum required:**
- Brand name (or active brand in memory)
- Deliverable type (images, video, copy)
- Quantity

**Recommended:**
- Format specifications (dimensions, duration)
- Style reference or brief summary
- Deadline

## Example Fast-Path Commands

```
# Quick social posts
"5 Instagram posts for Acme, 1080x1080, launch theme --yolo"

# Video batch
"3 TikTok videos for BrandX, 15 seconds each, product demo --yolo"

# Copy batch
"Email sequence for Spring Sale, 3 emails, Acme brand --yolo"
```

## Fast-Path Workflow

1. **Parse intent** — Extract brand, deliverables, specs from request
2. **Load brand** — Get profile from memory (fail if missing)
3. **Assign directly** — Route to specialist without brief creation
4. **Execute** — Specialist creates deliverables
5. **Quick review** — Basic technical validation only
6. **Deliver** — Return assets without confirmation loop

## Safety Limits

Fast-path is powerful but has guardrails:

- **No brand creation** — Brand must exist in memory
- **No ambiguous requests** — If specs unclear, fall back to normal flow
- **Error escalation** — If specialist fails, pause and notify
- **Log everything** — All fast-path executions logged for audit

## Headless Execute Mode

For automation, combine with headless:

```json
{
  "mode": "fast-path",
  "brand": "acme-co",
  "deliverables": [
    {
      "type": "image",
      "format": "instagram-post",
      "quantity": 5,
      "specs": {
        "dimensions": "1080x1080",
        "style": "bold-product-focus"
      }
    }
  ],
  "deadline": "2026-04-05"
}
```

Output is JSON with asset paths:
```json
{
  "status": "complete",
  "assets": [
    "output/acme-co/instagram/post-001.png",
    "output/acme-co/instagram/post-002.png",
    ...
  ]
}
```

## When NOT to Use Fast-Path

- First time working with Aria
- Brand not yet onboarded
- Uncertain about deliverable specs
- Complex multi-asset campaign with dependencies
- Need creative direction or suggestions

## User Experience

**Normal mode:**
> "I'd be happy to help with those posts! Let me pull up your Acme brand profile... I see we'll need 5 Instagram posts. Should these follow your spring campaign theme? Let me run this through our strategist for a quick brand alignment check..."

**Fast-path mode:**
> "Fast-path engaged. Creating 5 Instagram posts for Acme. Routing to Designer now."
> [Specialist executes]
> "Done. Assets in output/acme-co/instagram/"

The trade-off: speed vs. conversation. Choose based on your needs.