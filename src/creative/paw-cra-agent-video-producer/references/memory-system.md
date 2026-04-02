# Memory System for Video Producer

**Memory location:** `.pawbytes/creative-suites/` (Shared Agency Memory)

## Core Principle

The Video Producer shares memory with all agents in the Aria Creative Suite. This ensures brand consistency across all creative outputs -- when the Strategist defines brand voice, the Video Producer uses exactly that voice. When the Designer creates visual assets, the Video Producer can animate them.

## Shared Memory Structure

```
.pawbytes/creative-suites/
├── index.md                    # Agency roster, active campaigns, status
├── brands/
│   └── {brand-name}/
│       ├── guidelines.md       # Colors, fonts, logo, visual identity
│       ├── research/           # Strategist research reports
│       ├── campaigns/
│       │   └── {campaign}/
│       │       ├── brief.md    # Approved creative brief
│       │       ├── scripts/    # Approved scripts, copy
│       │       ├── assets/     # Visual assets (Designer output)
│       │       └── videos/     # Video assets (Video Producer output)
│       ├── assets/             # Brand-level visual assets
│       └── videos/             # Brand-level video assets
│           ├── short-form/
│           ├── long-form/
│           ├── series/
│           ├── clips/
│           └── motion-graphics/
├── knowledge/
│   └── index.md                # Research index (platform specs, guides)
└── daily/
    └── {YYYY-MM-DD}.md         # Activity log
```

## What to Read

| File | When to Read | Contains |
|------|-------------|----------|
| `index.md` | Every activation | Active brand, current campaigns |
| `brands/{brand}/guidelines.md` | Before every video task | Colors, typography, visual style |
| `brands/{brand}/campaigns/{campaign}/brief.md` | When working on campaign | Requirements, deliverables |
| `brands/{brand}/campaigns/{campaign}/scripts/` | When producing video | Approved scripts, storyboards |
| `brands/{brand}/assets/` | When animating brand assets | Designer-produced visual assets |

## What to Write

| File | When to Write | Contains |
|------|--------------|----------|
| `brands/{brand}/videos/` | After every video production | Generated video assets |
| `brands/{brand}/campaigns/{campaign}/videos/` | Campaign video output | Campaign-specific videos |
| `daily/{date}.md` | After every task | Activity log entry |
| `brands/{brand}/videos/video-manifest.json` | Every production run | Machine-readable output metadata |

## Read Access

- `.pawbytes/creative-suites/index.md`
- `.pawbytes/creative-suites/brands/{brand}/guidelines.md`
- `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/brief.md`
- `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/`
- `.pawbytes/creative-suites/brands/{brand}/assets/` (Designer output for animation)
- `.pawbytes/creative-suites/brands/{brand}/research/`
- `.pawbytes/creative-suites/knowledge/`

## Write Access

- `.pawbytes/creative-suites/brands/{brand}/videos/`
- `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/videos/`
- `.pawbytes/creative-suites/daily/{date}.md`

## Deny Zones

- `.pawbytes/creative-suites/brands/{other-brand}/` -- Other brands not in scope
- Any files outside `.pawbytes/creative-suites/` without explicit permission

## Save Triggers

Always update memory after:

1. **Producing video assets** -- Log location, type, platform, campaign
2. **Discovering production preferences** -- Note in daily log (e.g., preferred subtitle style, voice selection)
3. **Completing a production run** -- Write video-manifest.json
4. **User preference discovered** -- Update brand notes if brand-specific

## Activity Log Format

```markdown
## {HH:MM} [VideoProducer]
**Task:** {capability type}
**For:** {brand}/{campaign}
**Output:** {file paths}
**Specs:** {resolution, duration, codec}
**Notes:** {any relevant notes}
```
