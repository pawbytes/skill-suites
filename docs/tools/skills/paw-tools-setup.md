# Tools Setup

## Overview

Installs and configures Pawbytes Tools module in your project. Collects your preferences and writes them to configuration files that other tools use automatically.

## When to Use It

- You're setting up Pawbytes Tools for the first time in a project
- You want to change your tools configuration
- You need to add API keys for presentation images
- You're updating from a previous version

## Trigger Phrases

- "Install paw tools"
- "Configure Pawbytes Tools"
- "Setup utility tools"
- "Set up tools module"
- "Update tools config"

## What Gets Configured

### Shared Configuration
`{project-root}/.pawbytes/config/config.yaml`

| Setting | Purpose | Default |
|---------|---------|---------|
| `communication_language` | Language for tool interactions | English |
| `document_output_language` | Language for generated documents | English |
| `presentation_output_folder` | Where presentations are saved | `.pawbytes/tools-output/presentations/` |
| `release_default_branch` | Branch for releases | main |

### User Configuration (Private)
`{project-root}/.pawbytes/config/config.user.yaml`

| Setting | Purpose | Note |
|---------|---------|------|
| `pexels_api_key` | Stock photos for presentations | gitignored |
| `fal_api_key` | AI-generated images for presentations | gitignored |

## Step-by-Step Workflow

| Step | What Happens | Your Role |
|------|--------------|-----------|
| 1 | Check existing config | Tool detects if this is a fresh install or update |
| 2 | Ask for preferences | Provide values (or accept defaults) |
| 3 | Write config files | Tool creates configuration |
| 4 | Create output directories | Tool creates necessary folders |

## What You Get

```
{project-root}/.pawbytes/
├── config/
│   ├── config.yaml           # Shared settings
│   └── config.user.yaml      # API keys (gitignored)
└── tools-output/
    ├── presentations/        # Presentation Builder output
    └── releases/             # Release Automation reports
```

## End-to-End Example

**User**: "Install paw tools"

**Tools Setup**:
```
Setting up Pawbytes Tools...

This appears to be a fresh installation.

Please provide values for the following:
[Defaults shown in brackets]

1. Communication language [English]:
2. Document output language [English]:
3. Presentation output folder [.pawbytes/tools-output/presentations/]:
4. Release default branch [main]:
5. Pexels API key (for stock photos) [optional]:
6. fal.ai API key (for AI images) [optional]:
```

**User**: "All defaults are fine, but add my Pexels key: abc123xyz"

**Tools Setup**:
- Creates `.pawbytes/config/config.yaml` with your settings
- Creates `.pawbytes/config/config.user.yaml` with your Pexels key
- Creates output directories

**Output**:
```
Configuration saved!

Settings:
- Language: English
- Presentations saved to: .pawbytes/tools-output/presentations/
- Release branch: main
- Pexels API: configured

Next steps:
- Use "Create a presentation" to build decks from your content
- Use "Create a release" to automate version releases
```

## Headless Mode

Skip interactive prompts by providing values upfront:

```bash
"Install paw tools accept all defaults"
"Install paw tools --headless"
"Setup tools with language=Spanish, branch=master"
```

## Updating Configuration

Run Tools Setup again to update your configuration. Existing values are shown as defaults, so you only need to provide what you want to change.

**User**: "Update tools config"

**Tools Setup**:
```
Updating Pawbytes Tools configuration...

Current values shown in brackets:

1. Communication language [English]:
2. Document output language [English]:
...
```

## Configuration Priority

When multiple sources exist, priority is (highest to lowest):

1. Values you provide during setup
2. Existing configuration values
3. Default values from module definition

## Related Skills

- [Presentation Builder](./paw-tools-presentation.md) — Uses your config for output paths and API keys
- [Release Automation](./paw-tools-release.md) — Uses your config for default branch