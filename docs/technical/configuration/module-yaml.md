# Module Metadata (module.yaml)

## Purpose

The `module.yaml` file defines configuration schema for setup skills. It specifies:

- Module identity and version
- Configuration variables to collect
- Default values and prompts
- Directory structure to create

---

## Location

```
src/{module}/paw-{module}-setup/
└── assets/
    └── module.yaml
```

Example locations:
- `src/marketing/paw-mkt-setup/assets/module.yaml`
- `src/creative/paw-cra-setup/assets/module.yaml`
- `src/tools/paw-tools-setup/assets/module.yaml`

---

## File Structure

### Minimal Format

```yaml
code: mkt
name: Marketing Suite
description: Marketing skills module.
module_version: 1.0.0
default_selected: false
module_greeting: Welcome to Marketing Suite!
```

### Complete Format

```yaml
# Module Identity
code: mkt
name: Agentic Marketing Suite
description: 21 specialized AI marketing agents.
module_version: 0.3.7
default_selected: false
module_greeting: |
  Marketing Suite activated.

  Quick Start:
  - `paw-mkt-agent-agency` — Multi-channel coordination
  - `paw-mkt-sostac` — Build marketing plans

# Configuration Paths
config_path: .pawbytes/config
user_config_path: .pawbytes/config/config.user.yaml
memory_path: .pawbytes/marketing-suites

# Configuration Variables
output_folder:
  prompt: "Where should output be saved?"
  default: "{project-root}/.pawbytes/marketing-suites"
  result: "{value}"
  directories: true
  user_setting: false

api_key:
  prompt: "Enter your API key"
  default: ""
  result: "{value}"
  user_setting: true
  sensitive: true
  required: false

# Directories to create
directories:
  - "{output_folder}"
  - "{output_folder}/brands"
  - "{output_folder}/reports"

# Post-install message
post_install_notes: |
  Setup complete! Run `paw-mkt-agent-agency` to get started.
```

---

## Module Identity Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `code` | string | Yes | 3-letter module code (e.g., `mkt`, `cra`, `paw`) |
| `name` | string | Yes | Display name |
| `description` | string | Yes | Module description |
| `module_version` | string | Yes | Semantic version |
| `default_selected` | boolean | No | Pre-selected in installer (default: `false`) |
| `module_greeting` | string | No | Shown after activation |
| `greeting` | string | No | Alternative to `module_greeting` |

---

## Configuration Path Fields

| Field | Type | Description |
|-------|------|-------------|
| `config_path` | path | Config directory location |
| `user_config_path` | path | User config file location |
| `memory_path` | path | Memory/output root for module |

---

## Variable Definition Fields

Variables can be defined in two formats:

### Dictionary Format (Marketing Style)

```yaml
brands_folder:
  prompt: "Where should brand contexts be stored?"
  default: "{project-root}/.pawbytes/marketing-suites/brands"
  result: "{value}"
  directories: true
  user_setting: false
```

### List Format (Creative/Tools Style)

```yaml
questions:
  - key: fal_key
    prompt: "fal.ai API key (required)"
    default: ""
    user_setting: true
    required: true
```

### Field Reference

| Field | Type | Purpose |
|-------|------|---------|
| `key` | string | Variable name (list format) |
| `prompt` | string | Question shown during setup |
| `default` | any | Default value (can contain tokens) |
| `result` | string | Storage format (usually `{value}`) |
| `result_template` | string | Template for computed values |
| `directories` | boolean | Create directories at this path |
| `user_setting` | boolean | Save to `config.user.yaml` |
| `sensitive` | boolean | Don't log value (for secrets) |
| `required` | boolean | Value must be provided |

---

## Directory Creation

The `directories` field specifies paths to create during setup:

```yaml
directories:
  - "{output_directory}"
  - "{output_directory}/brands"
  - "{output_directory}/knowledge"
```

Variables in paths are resolved before creation.

---

## Examples

### Marketing Module (Dictionary Format)

```yaml
code: mkt
name: Agentic Marketing Suite
description: 21 specialized AI marketing agents covering strategy, content, SEO, paid ads, social, email, CRO, PR, pricing, retention, and more.
module_version: 0.3.7
default_selected: false
module_greeting: |
  Agentic Marketing Suite activated. You now have 21 specialized marketing agents.

  Quick Start:
  - `paw-mkt-agent-agency` — Multi-channel coordination

# Configuration Variables
brands_folder:
  prompt: "Where should brand contexts be stored?"
  default: "{project-root}/.pawbytes/marketing-suites/brands"
  result: "{value}"
  directories: true

reports_folder:
  prompt: "Where should reports be saved?"
  default: "{project-root}/.pawbytes/marketing-suites/reports"
  result: "{value}"
  directories: true

default_brand:
  prompt: "Default brand slug (leave empty to always specify)?"
  default: ""
  user_setting: true

communication_language:
  prompt: "Language for agent responses?"
  default: "English"
  user_setting: true
```

### Creative Module (List Format)

```yaml
name: Pawbytes Creative Suites
code: cra
version: 0.3.7
description: AI creative agency for visual, video, and content production.
greeting: Pawbytes Creative Suites is ready. Run `paw-cra-agent-creative-director` to meet Aria.

config_path: .pawbytes/config
user_config_path: .pawbytes/config/config.user.yaml
memory_path: .pawbytes/creative-suites

questions:
  - key: fal_key
    prompt: "fal.ai API key (required for image/video generation)"
    default: ""
    user_setting: true
    required: true

  - key: user_name
    prompt: "Your name (for personalized greetings)"
    default: ""
    user_setting: true
    required: false

  - key: output_directory
    prompt: "Output directory for creative assets"
    default: ".pawbytes/creative-suites"
    user_setting: false
    required: false
    result_template: "{project-root}/{value}"

directories:
  - "{output_directory}"
  - "{output_directory}/brands"
  - "{output_directory}/knowledge"

post_install_notes: |
  Pawbytes Creative Suites installed successfully!

  Next steps:
  1. Run `paw-cra-agent-creative-director` to meet Aria
```

### Tools Module (Config Section)

```yaml
name: Pawbytes Tools
code: paw
version: 0.1.0
description: Productivity utility tools for the Pawbytes ecosystem.
greeting: "Pawbytes Tools is ready!"

config_path: .pawbytes/config

config:
  - key: presentation_output_folder
    prompt: "Where should presentations be saved?"
    default: "{project-root}/.pawbytes/tools-output/presentations"

  - key: release_default_branch
    prompt: "Default branch for releases"
    default: "main"

  - key: pexels_api_key
    prompt: "Pexels API key for stock images (optional)"
    default: ""
    required: false
    user_setting: true

  - key: fal_api_key
    prompt: "fal.ai API key for AI-generated images (optional)"
    default: ""
    required: false
    user_setting: true
```

---

## Setup Skill Integration

Setup skills read `module.yaml` to:

1. **Display module info** — Show name and description
2. **Collect configuration** — Prompt for each variable
3. **Write config files** — Save to `config.yaml` and `config.user.yaml`
4. **Create directories** — Make configured paths
5. **Show greeting** — Display `module_greeting` or `greeting`

### Setup Skill Workflow

```markdown
## On Activation

1. Read `./assets/module.yaml` for module metadata
2. Check if config exists — inform user if this is an update
3. Collect values for each variable with a `prompt` field
4. Write to `{project-root}/.pawbytes/config/config.yaml`
5. Write user settings to `config.user.yaml`
6. Create directories listed in `directories`
7. Display the greeting
```

---

## Best Practices

1. **Include a helpful greeting** — Guide users to key skills
2. **Use token defaults** — `{project-root}` for portable paths
3. **Separate user settings** — API keys go to `config.user.yaml`
4. **Mark sensitive fields** — Use `sensitive: true` for secrets
5. **Provide sensible defaults** — Users can accept and go
6. **Document required vs optional** — Clear about what's needed

---

## See Also

- [Config Files](./config-files.md)
- [Variables Reference](./variables.md)
- [Skill Specification: Folder Structure](../skill-specification/folder-structure.md)