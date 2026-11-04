# Memory System for Video Producer

**Shared agency tree:** `{suite-root}/` (memory in `_memory/`, deliverables under `brands/`)

## Core Principle

The Video Producer shares memory with all agents in the Aria Creative Suite. This ensures brand consistency across all creative outputs -- when the Strategist defines brand voice, the Video Producer uses exactly that voice. When the Designer creates visual assets, the Video Producer can animate them.

## Shared Memory Structure

```
{suite-root}/
├── _memory/
│   ├── index.md                # Agency roster, active campaigns, status
│   ├── knowledge/index.md      # Research index (platform specs, guides)
│   └── daily/{YYYY-MM-DD}.md   # Activity log
└── brands/
    └── {brand-name}/
        ├── README.md           # Brand dashboard (Status:, Next:, links)
        ├── guidelines.md       # Colors, fonts, logo, visual identity
        ├── research/           # Strategist research reports
        ├── brand-assets/       # Logos, video/ intros, outros, watermarks
        ├── designs/            # Designer output (non-campaign)
        ├── campaigns/
        │   └── {YYYY-MM-campaign}/
        │       ├── brief.md    # Approved creative brief
        │       ├── scripts/    # Approved scripts, copy
        │       ├── designs/    # Visual assets (Designer output)
        │       └── videos/     # Same scheme as below
        └── videos/             # Non-campaign video
            ├── short-form/     # MP4s + video-manifest.json
            ├── long-form/{slug}/
            ├── series/{name}/
            ├── clips/{session}/
            ├── motion-graphics/
            ├── audio/
            └── .work/          # Temporary working files
```

## What to Read

| File | When to Read | Contains |
|------|-------------|----------|
| `_memory/index.md` | Every activation | Active brand, current campaigns |
| `brands/{brand}/guidelines.md` | Before every video task | Colors, typography, visual style |
| `brands/{brand}/campaigns/{campaign}/brief.md` | When working on campaign | Requirements, deliverables |
| `brands/{brand}/campaigns/{campaign}/scripts/` | When producing video | Approved scripts, storyboards |
| `brands/{brand}/designs/`, `brands/{brand}/brand-assets/` | When animating brand assets | Designer-produced visual assets |

## What to Write

| File | When to Write | Contains |
|------|--------------|----------|
| `brands/{brand}/videos/{short-form,long-form,...}/` | After every video production | Generated video assets |
| `brands/{brand}/campaigns/{campaign}/videos/` | Campaign video output | Campaign-specific videos |
| `_memory/daily/{date}.md` | After every task | Activity log entry |
| `video-manifest.json` beside the output | Every production run | Machine-readable output metadata |

## Read Access

- `{suite-root}/_memory/index.md`
- `{suite-root}/brands/{brand}/guidelines.md`
- `{suite-root}/brands/{brand}/campaigns/{campaign}/brief.md`
- `{suite-root}/brands/{brand}/campaigns/{campaign}/scripts/`
- `{suite-root}/brands/{brand}/designs/`, `brand-assets/` (Designer output for animation)
- `{suite-root}/brands/{brand}/research/`
- `{suite-root}/_memory/knowledge/`

## Write Access

- `{suite-root}/brands/{brand}/videos/`
- `{suite-root}/brands/{brand}/campaigns/{campaign}/videos/`
- `{suite-root}/_memory/daily/{date}.md`

## Deny Zones

- `{suite-root}/brands/{other-brand}/` -- Other brands not in scope
- Any files outside `{suite-root}/` without explicit permission

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
