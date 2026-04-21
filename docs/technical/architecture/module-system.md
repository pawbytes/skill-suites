# Module System

Modules are the primary organizational unit in Pawbytes Skill Suites. This document explains how modules are structured, registered, and configured.

## What is a Module?

A module is a collection of related skills that share:
- **Namespace prefix** — All skills start with the same prefix (e.g., `paw-mkt-`)
- **Output directory** — Artifacts go to a shared location (e.g., `.pawbytes/marketing-suites/`)
- **Configuration schema** — Variables defined in `module.yaml`

## Module Types

| Type | Prefix | Skills | Purpose |
|------|--------|--------|---------|
| **Marketing** | `paw-mkt-` | 23 | Marketing strategy and execution |
| **Creative** | `paw-cra-` | 15 | Design and video production |
| **Tools** | `paw-tools-` | 3 | Developer utilities |

## Module Structure

```
src/{module}/
├── CHANGELOG.md
│
├── paw-{module}-setup/              # Setup skill (required)
│   ├── SKILL.md
│   └── assets/
│       └── module.yaml              # Configuration schema
│
├── paw-{module}-{coordinator}/      # Coordinator skill
│   ├── SKILL.md
│   └── references/
│       └── *.md
│
├── paw-{module}-{specialist-1}/     # Specialist skills
│   ├── SKILL.md
│   └── references/
│       ├── frameworks-index.csv
│       └── frameworks/
│
└── paw-{module}-{specialist-n}/
    ├── SKILL.md
    └── references/
```

### Directory Breakdown

| Directory | Purpose |
|-----------|---------|
| `paw-{module}-setup/` | Initializes module configuration |
| `paw-{module}-{skill}/` | Individual skill folder |
| `SKILL.md` | Main skill definition (required) |
| `references/` | Knowledge files loaded during execution |
| `assets/` | Static resources (configs, scripts) |

## Module Registration

Modules are registered in `.claude-plugin/marketplace.json`:

```json
{
  "name": "skill-suites",
  "plugins": [
    {
      "name": "marketing-suites",
      "description": "AI marketing agent with 23 specialist skills...",
      "source": "./",
      "skills": [
        "./src/marketing/paw-mkt-setup",
        "./src/marketing/paw-mkt-agent-agency",
        "./src/marketing/paw-mkt-sostac",
        "./src/marketing/paw-mkt-seo",
        // ... more skills
      ]
    },
    {
      "name": "creative-agency-suites",
      "description": "AI creative agency with 15 skills...",
      "source": "./",
      "skills": [
        "./src/creative/paw-cra-setup",
        // ... more skills
      ]
    }
  ]
}
```

### Registration Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Plugin identifier (used in output paths) |
| `description` | Yes | Plugin description for marketplace |
| `source` | Yes | Source location (usually `./`) |
| `skills` | Yes | Array of skill folder paths |
| `strict` | No | Enable strict mode (default: false) |

## Module Configuration

Each module defines its configuration schema in `module.yaml`:

```yaml
code: mkt                                    # Short code (3 letters)
name: Agentic Marketing Suite                # Display name
description: |                               # Module description
  Multi-line description of what the module provides.
module_version: 1.0.0                        # Version
default_selected: false                      # Pre-selected in installer?
module_greeting: |                           # Shown on activation
  Welcome to Agentic Marketing!

# Configuration Variables
output_folder:
  prompt: "Where should output be saved?"
  default: "{project-root}/.pawbytes/marketing-suites"
  result: "{value}"
  directories: true                          # Create directories?
  user_setting: true                         # Save to config.user.yaml?

user_name:
  prompt: "What should I call you?"
  default: ""
  result: "{value}"
  user_setting: true

api_key:
  prompt: "Enter your API key (optional)"
  default: ""
  result: "{value}"
  user_setting: true
  sensitive: true                            # Don't log value
```

### Configuration Variable Fields

| Field | Purpose |
|-------|---------|
| `prompt` | Question shown to user during setup |
| `default` | Default value if user doesn't specify |
| `result` | How value is stored (`{value}` = user input) |
| `directories` | Create directories if true |
| `user_setting` | Save to `config.user.yaml` (gitignored) |
| `sensitive` | Don't log the value |

## Configuration Loading

Skills load configuration in their `On Activation` section:

```markdown
## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml`
and `{project-root}/.pawbytes/config/config.user.yaml` if present.
Resolve and apply throughout the session.
```

### Loading Order

```
1. Module defaults    → module.yaml
2. Project config     → .pawbytes/config/config.yaml
3. User overrides     → .pawbytes/config/config.user.yaml
```

Later values override earlier ones.

### Variable Resolution

Variables are referenced with curly braces:

| Variable | Resolves To |
|----------|-------------|
| `{project-root}` | Project root directory |
| `{user_name}` | User's name from config |
| `{output_folder}` | Output directory path |
| `{communication_language}` | Language for responses |
| `{document_output_language}` | Language for documents |

## Output Directory Structure

Each module writes to its own directory under `.pawbytes/`:

```
.pawbytes/
├── config/
│   ├── config.yaml              # Project-level config
│   └── config.user.yaml         # User overrides (gitignored)
│
├── marketing-suites/            # paw-mkt-* outputs
│   ├── brands/{brand-slug}/
│   └── reports/
│
├── creative-suites/             # paw-cra-* outputs
│   ├── index.md                 # Memory entry point
│   ├── brands/{brand-slug}/
│   └── output/
│
└── tools-output/                # paw-tools-* outputs
    ├── presentations/
    └── releases/
```

## Naming Conventions

### Skill Names

Format: `{org}-{module}-{skillname}`

| Part | Format | Example |
|------|--------|---------|
| `org` | 3 letters | `paw` |
| `module` | 3 letters | `mkt`, `cra`, `tools` |
| `skillname` | kebab-case | `seo`, `agent-designer` |

**Examples:**
- `paw-mkt-seo` — Marketing module, SEO skill
- `paw-cra-agent-designer` — Creative module, Designer agent
- `paw-tools-release` — Tools module, Release utility

### Folder Names

Match skill name exactly:
- `src/marketing/paw-mkt-seo/`
- `src/creative/paw-cra-agent-designer/`
- `src/tools/paw-tools-release/`

## Example: Marketing Module

```
src/marketing/
├── CHANGELOG.md
│
├── paw-mkt-setup/
│   ├── SKILL.md
│   └── assets/
│       └── module.yaml
│
├── paw-mkt-agent-agency/              # Coordinator
│   ├── SKILL.md
│   └── references/
│       ├── context-router.md
│       ├── brand-onboarding.md
│       └── team-spawning.md
│
├── paw-mkt-seo/                 # Specialist
│   ├── SKILL.md
│   └── references/
│       ├── frameworks-index.csv
│       ├── capability-technical-seo.md
│       └── frameworks/
│           ├── technical-audit.md
│           └── schema-markup.md
│
└── ... (21 more specialists)
```

## Adding a New Module

1. Create directory: `src/{module}/`
2. Create setup skill: `paw-{module}-setup/`
3. Define `module.yaml` with configuration schema
4. Create coordinator skill (if needed)
5. Create specialist skills
6. Register in `marketplace.json`

## Module Independence

Modules are designed to work independently:
- Each has its own configuration
- Each has its own output directory
- Each can be installed separately
- No cross-module dependencies required