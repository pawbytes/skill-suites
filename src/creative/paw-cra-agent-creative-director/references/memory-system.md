# Memory System

Aria maintains a shared memory structure at `{project-root}/.pawbytes/creative-suites/`. Other specialists read from and write to this same location.

## Core Principle

Memory enables continuity. A brand onboarded today should inform work next month. A campaign brief should be retrievable by any specialist. Memory persists across sessions.

## File Structure

```
.pawbytes/creative-suites/
├── index.md              # Entry point — active brand, current campaigns, tool status
├── brands/
│   └── {brand-name}/
│       ├── profile.md    # Brand identity
│       ├── assets/       # Logo files, templates
│       └── guidelines.md # Extended guidelines (optional)
├── campaigns/
│   └── {campaign-name}/
│       ├── brief.md
│       ├── plan.md
│       ├── status.md
│       └── assets/
├── briefs/
│   └── {brief-name}.md   # Standalone briefs (not yet campaigns)
└── daily/
    └── {YYYY-MM-DD}.md   # Daily logs
```

## Write Discipline

- **Always append, never overwrite** — preserve history
- **Use timestamps** — `## 2026-03-31 14:32` format for entries
- **Cross-reference** — link to related files when relevant
- **Keep index current** — update active brand and campaigns in `index.md`

## Index Format

```markdown
# Creative Suites Index

## Tool Status
- fal: available
- elevenlabs: unavailable
- pexels: available
- ffmpeg: available

## Active Brand
{brand-name}

## Active Campaigns
- {campaign-name}: in_progress
- {campaign-name}: blocked

## Recent Activity
- 2026-03-31: Onboarded brand "Acme Co"
- 2026-03-30: Completed campaign "Spring Launch"
```

## Memory Maintenance

- **Daily logs** — brief summary of what happened each session
- **Archive completed campaigns** — move to `campaigns/_archived/` after delivery
- **Prune old daily logs** — keep last 30 days, archive older

## Initialization

If memory doesn't exist, run `python3 ./scripts/init-memory.py` to create the structure. Then guide the user through brand onboarding.