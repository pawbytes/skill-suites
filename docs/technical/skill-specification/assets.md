# Assets

## Purpose

Assets are static resources that support skill execution. Unlike references (which are knowledge), assets are files used directly by the skill or user.

## Directory Structure

```
assets/
├── module.yaml             # Setup skills: configuration schema
├── module-help.csv         # Setup skills: CLI help entries
├── scripts/                # Executable scripts
│   ├── tool-discovery.sh
│   └── tool-discovery.bat
└── templates/              # Reusable templates
    └── presentation/
        ├── code.html
        └── screen.png
```

## Asset Types

### module.yaml

Configuration schema for setup skills. Defines what configuration to collect during module installation.

#### Location

Only in setup skills: `paw-{module}-setup/assets/module.yaml`

#### Structure

```yaml
# Module metadata
code: mkt                              # Short code (3 letters)
name: Agentic Marketing Suite          # Display name
description: Multi-line description    # Module description
version: 1.0.0                         # Version
default_selected: false                # Pre-selected in installer?

# Paths
config_path: .pawbytes/config/config.yaml
user_config_path: .pawbytes/config/config.user.yaml
memory_path: .pawbytes/marketing-suites

# Configuration questions
questions:
  - key: user_name
    prompt: "Your name (for personalized greetings)"
    default: ""
    user_setting: true
    required: false

  - key: communication_language
    prompt: "Communication language"
    default: "English"
    user_setting: true
    required: false

  - key: fal_key
    prompt: "fal.ai API key (required for image generation)"
    default: ""
    user_setting: true
    required: true

# Directories to create
directories:
  - "{memory_path}"
  - "{memory_path}/brands"
  - "{memory_path}/reports"

# Post-install message
post_install_notes: |
  Module installed successfully!
  
  **Next steps:**
  1. Run `paw-mkt-agency` to start
  2. Configure API keys in config.user.yaml
```

#### Question Fields

| Field | Purpose |
|-------|---------|
| `key` | Variable name for the configuration value |
| `prompt` | Question shown to user during setup |
| `default` | Default value if user doesn't specify |
| `user_setting` | If true, saves to config.user.yaml (gitignored) |
| `required` | If true, setup won't complete without value |

#### Variable Resolution

Variables in paths are resolved at runtime:

| Variable | Resolves To |
|----------|-------------|
| `{project-root}` | Project root directory |
| `{value}` | User's input value |
| `{memory_path}` | Module's memory path |

### module-help.csv

CLI help entries for the module.

#### Format

```csv
command,description,usage
paw-mkt-agency,Multi-channel marketing coordination,paw-mkt-agency [--headless]
paw-mkt-seo,SEO specialist for audits and optimization,paw-mkt-seo [url]
paw-mkt-content,Content strategy and editorial planning,paw-mkt-content
```

### Scripts

Executable scripts for tool discovery, setup, and maintenance.

#### Location

```
assets/scripts/
├── tool-discovery.sh    # Unix/Linux/macOS
├── tool-discovery.bat   # Windows
├── chrome-profiles.sh   # Unix/Linux/macOS
└── chrome-profiles.bat  # Windows
```

#### Purpose

| Script | Purpose |
|--------|---------|
| `tool-discovery.sh/bat` | Detect available tools and APIs |
| `chrome-profiles.sh/bat` | Manage Chrome profiles for automation |
| `merge-config.py` | Merge configuration files |
| `cleanup-legacy.py` | Clean up old directory structures |

#### Example: tool-discovery.sh

```bash
#!/bin/bash

echo "Checking available tools..."

# Check for ffmpeg
if command -v ffmpeg &> /dev/null; then
    echo "✓ ffmpeg available"
else
    echo "✗ ffmpeg not found"
fi

# Check for Puppeteer
if [ -d "node_modules/puppeteer" ]; then
    echo "✓ Puppeteer installed"
else
    echo "✗ Puppeteer not installed"
fi
```

### Templates

Reusable templates for generated outputs.

#### Location

```
assets/templates/
└── presentation/
    ├── title_slide_template/
    │   ├── code.html
    │   └── screen.png
    └── agenda_template/
        ├── code.html
        └── screen.png
```

#### Template Structure

Each template has:
- `code.html` — HTML/CSS template
- `screen.png` — Preview screenshot

#### Example Template

```html
<!-- title_slide_template/code.html -->
<!DOCTYPE html>
<html>
<head>
  <style>
    .slide {
      width: 1920px;
      height: 1080px;
      background: #1a1a2e;
      font-family: 'McKinsey Sans', sans-serif;
    }
    .title {
      font-size: 64px;
      color: white;
      text-align: center;
      padding-top: 400px;
    }
    .subtitle {
      font-size: 32px;
      color: #8b8b8b;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="slide">
    <div class="title">{{title}}</div>
    <div class="subtitle">{{subtitle}}</div>
  </div>
</body>
</html>
```

## Setup Skill Assets

Setup skills have a special asset structure:

```
paw-{module}-setup/
├── SKILL.md
└── assets/
    ├── module.yaml         # Required: Configuration schema
    ├── module-help.csv     # Optional: CLI help
    └── scripts/            # Optional: Setup scripts
```

### Required Assets for Setup Skills

| Asset | Required | Purpose |
|-------|----------|---------|
| `module.yaml` | Yes | Defines configuration to collect |
| `module-help.csv` | No | CLI help entries |
| `scripts/` | No | Setup and maintenance scripts |

## Asset vs Reference

| Aspect | Asset | Reference |
|--------|-------|-----------|
| Content | Static files, configs, scripts | Knowledge, methodologies |
| Loading | Used directly or copied | Read and processed |
| Modification | May be user-modified | Skill-owned |
| Purpose | Support execution | Guide execution |

## Best Practices

### module.yaml

1. **Group related questions** — API keys together, settings together
2. **Mark sensitive fields** — `user_setting: true` for secrets
3. **Provide helpful prompts** — Guide users on what to enter
4. **Set sensible defaults** — Minimize required input

### Scripts

1. **Cross-platform support** — Provide both `.sh` and `.bat`
2. **Clear output** — Use ✓/✗ for pass/fail indicators
3. **Exit codes** — Return non-zero on failure
4. **No side effects** — Check without modifying unless explicit

### Templates

1. **Include preview** — Provide `screen.png` for visual reference
2. **Use variables** — Template should accept substitution
3. **Document requirements** — Note any dependencies
4. **Test rendering** — Verify output quality

## Real-World Examples

### Marketing Setup Assets

```
paw-mkt-setup/
└── assets/
    ├── module.yaml
    ├── module-help.csv
    └── scripts/
        ├── tool-discovery.sh
        ├── tool-discovery.bat
        ├── chrome-profiles.sh
        └── chrome-profiles.bat
```

### Creative Setup Assets

```
paw-cra-setup/
└── assets/
    ├── module.yaml
    └── module-help.csv
```

### Tools Presentation Assets

```
paw-tools-presentation/
└── assets/
    ├── title_slide_template/
    │   ├── code.html
    │   └── screen.png
    ├── agenda_template/
    │   ├── code.html
    │   └── screen.png
    ├── 2x2_matrix_template/
    │   ├── code.html
    │   └── screen.png
    └── kinetic_insight_colour_template/
        └── DESIGN.md
```