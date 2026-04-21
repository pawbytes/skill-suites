# Architecture Overview

This document provides a high-level view of the Pawbytes Skill Suites architecture, explaining how skills, modules, and frameworks work together.

## System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                           User Request                           │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Coordinator Skill                           │
│              (paw-mkt-agent-agency, paw-cra-agent-creative-director)   │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Load Config │──│ Read Memory │──│ Route to    │             │
│  │             │  │             │  │ Specialist  │             │
│  └─────────────┘  └─────────────┘  └──────┬──────┘             │
└───────────────────────────────────────────┼─────────────────────┘
                                            │
                                 ┌──────────┴──────────┐
                                 ▼                     ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │   Specialist    │    │   Specialist    │
                    │  (paw-mkt-seo)  │    │ (paw-mkt-content)│
                    └────────┬────────┘    └────────┬────────┘
                             │                      │
                             ▼                      ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │ frameworks-     │    │ frameworks-     │
                    │ index.csv (24r) │    │ index.csv       │
                    └────────┬────────┘    └────────┬────────┘
                             │                      │
                    Match to best_for        Match to best_for
                             │                      │
                             ▼                      ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │ framework/*.md  │    │ framework/*.md  │
                    │ (loaded only    │    │ (loaded only    │
                    │  when matched)  │    │  when matched)  │
                    └────────┬────────┘    └────────┬────────┘
                             │                      │
                             └──────────┬───────────┘
                                        ▼
                         ┌─────────────────────────────┐
                         │     Output Artifacts        │
                         │  .pawbytes/{module}/brands/ │
                         └─────────────────────────────┘
```

## Key Concepts

### Modules

Modules are collections of related skills that share:
- **Namespace prefix** — `paw-mkt-`, `paw-cra-`, `paw-tools-`
- **Output directory** — `.pawbytes/marketing-suites/`, etc.
- **Configuration** — Loaded from module.yaml

Each module has a setup skill that initializes configuration and a coordinator skill that routes requests.

### Skills

Skills are single-purpose capabilities defined in `SKILL.md`:

| Type | Characteristics | Examples |
|------|-----------------|----------|
| **Agent** | Persistent persona, memory, coordinates others | paw-mkt-agent-agency, paw-cra-agent-creative-director |
| **Workflow** | Deterministic pipeline, defined steps | paw-cra-video-shortform, paw-mkt-sostac |
| **Utility** | Single-purpose, minimal interaction | paw-tools-release, paw-tools-presentation |

### Frameworks

Domain knowledge stored in `references/frameworks/`:
- **Indexed** — `frameworks-index.csv` provides lightweight lookup
- **Progressive** — Only matched files are loaded
- **Tagged** — Enables discovery via keywords

### Configuration

Three-level hierarchy:

```
1. Module defaults    → module.yaml (in setup skill)
2. Project config     → .pawbytes/config/config.yaml
3. User overrides     → .pawbytes/config/config.user.yaml
```

Variables like `{user_name}` and `{project-root}` are resolved at runtime.

### Artifacts

All outputs go to `.pawbytes/`:

```
.pawbytes/
├── config/                    # Configuration files
├── marketing-suites/          # Marketing outputs
│   └── brands/{brand-slug}/   # Brand workspaces
├── creative-suites/           # Creative outputs
│   └── brands/{brand-slug}/   # Brand workspaces
└── tools-output/              # Tool outputs
```

## Documentation Index

| Document | Purpose |
|----------|---------|
| [Module System](./module-system.md) | How modules are structured and registered |
| [Skill Lifecycle](./skill-lifecycle.md) | Activation through completion phases |
| [Routing Patterns](./routing-patterns.md) | Coordinator to specialist routing |
| [Progressive Disclosure](./progressive-disclosure.md) | Framework loading optimization |

## Design Principles

### 1. Read Before Acting

Skills always read existing context before generating content:
- Brand context (`brand-context.md`)
- Strategy files (`sostac/`)
- Campaign briefs (`campaigns/{campaign}/brief.md`)

### 2. File System as Truth

All state lives in files:
- Progress tracked in `status.md`
- Memory in `index.md`
- Plans in their respective directories

### 3. Progressive Loading

Load only what's needed:
- Framework index first (~20 rows)
- Match to user situation
- Load specific framework file

### 4. User Is the Client

Present options, explain reasoning, let user decide:
- Advise, don't mandate
- Show what exists vs what needs creation
- Use numbered choices for selection

## Module Overview

### Marketing (paw-mkt-*)

23 skills covering the full marketing stack:

```
paw-mkt-agent-agency          → Coordinator (routes all requests)
paw-mkt-sostac          → SOSTAC planning framework
paw-mkt-seo             → Technical and content SEO
paw-mkt-content         → Content marketing
paw-mkt-email           → Email sequences
paw-mkt-social          → Social media
paw-mkt-paid-ads        → Paid advertising
... (18 more specialists)
```

### Creative (paw-cra-*)

15 skills for design and video production:

```
paw-cra-agent-creative-director  → Aria (coordinator)
paw-cra-agent-designer           → Visual production
paw-cra-agent-video-producer     → Video production
paw-cra-agent-strategist         → Research (on-demand)
paw-cra-video-shortform          → TikTok/Reels/Shorts
paw-cra-video-longform           → YouTube/web video
paw-cra-design-social            → Social posts/carousels
... (8 more workflows)
```

### Tools (paw-tools-*)

3 utility skills:

```
paw-tools-presentation  → McKinsey-style HTML decks
paw-tools-release       → Automated releases
paw-tools-setup         → Module configuration
```