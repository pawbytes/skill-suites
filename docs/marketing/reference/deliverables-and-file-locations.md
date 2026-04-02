# Reference: Deliverables and File Locations

This page shows where the major outputs go.

## Strategic files

```text
.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md
.pawbytes/marketing-suites/brands/{brand-slug}/paw-mkt-product-context.md
.pawbytes/marketing-suites/brands/{brand-slug}/sostac/
```

## SOSTAC outputs

```text
.pawbytes/marketing-suites/brands/{brand-slug}/sostac/
├── 00-auto-discovery.md
├── 01-situation.md
├── 02-objectives.md
├── 03-strategy.md
├── 04-tactics.md
├── 05-action.md
├── 06-control.md
└── plan-summary.md
```

## Channel-oriented skills (standalone mode)

For evergreen or independent work, outputs go to the `channels/` subtree:

### SEO
```text
.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/
```

### Social
```text
.pawbytes/marketing-suites/brands/{brand-slug}/channels/social/
```

### Video
```text
.pawbytes/marketing-suites/brands/{brand-slug}/channels/video/
```

### Analytics
```text
.pawbytes/marketing-suites/brands/{brand-slug}/channels/analytics/
```

## Content-oriented skills

### Content
```text
.pawbytes/marketing-suites/brands/{brand-slug}/content/
```

### Email
```text
.pawbytes/marketing-suites/brands/{brand-slug}/content/email/
```

## Campaign-oriented skills

For work tied to a specific campaign, outputs go under:

```text
.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/{channel}/
```

Or for simple campaigns without slug namespacing:

### CRO
```text
brands/{brand-slug}/campaigns/cro/
```

### Paid ads
```text
brands/{brand-slug}/campaigns/paid-ads/
```

### PR
```text
brands/{brand-slug}/campaigns/pr/
```

### Influencer
```text
brands/{brand-slug}/campaigns/influencer/
```

### Referral
```text
brands/{brand-slug}/campaigns/referral/
```

### Community
```text
brands/{brand-slug}/campaigns/community/
```

### Guerrilla
```text
brands/{brand-slug}/campaigns/guerrilla/
```

### Launch
```text
brands/{brand-slug}/campaigns/launch/
```

### Pricing
```text
brands/{brand-slug}/campaigns/pricing/
```

### Retention
```text
brands/{brand-slug}/campaigns/retention/
```

### Sales
```text
brands/{brand-slug}/campaigns/sales/
```

## Analytics

```text
brands/{brand-slug}/analytics/
```

## Legacy paths

Some skills support a legacy fallback when old directory structures are detected (e.g., `brands/{brand-slug}/content/seo/`). When detected, the skill will suggest migrating to the newer structure.

## Important exceptions

- `paw-mkt-product-context.md` lives at the brand root, not under `campaigns/` or `content/`, because it is shared by every specialist.
- SOSTAC files live under `.pawbytes/marketing-suites/brands/{brand-slug}/sostac/` regardless of campaign structure.
