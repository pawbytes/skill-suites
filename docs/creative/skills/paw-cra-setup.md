# paw-cra-setup

## Overview

Installs and configures the Pawbytes Creative Suites module in a project. Collects user preferences and API keys, creates output directories, and registers module capabilities with the help system.

## What It Does

| Step | Purpose |
|------|---------|
| Module Load | Read module metadata from `./assets/module.yaml` |
| Config Check | Check for existing config or legacy BMad format |
| Collect Values | Gather user preferences and API keys |
| Write Config | Write to `config.yaml` and `config.user.yaml` |
| Create Directories | Create output folders for brands, knowledge, logs |
| Register Help | Add capabilities to `module-help.csv` |

## When to Use It

- First-time setup of Creative Suites in a project
- Updating existing Creative Suites configuration
- Adding API keys after initial setup
- Migrating from legacy BMad config format

## Trigger Phrases

- "Install creative suites"
- "Configure creative suites"
- "Setup creative suites"
- "paw-cra setup"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Shared config | `.pawbytes/config/config.yaml` |
| User settings | `.pawbytes/config/config.user.yaml` (gitignored) |
| Help registry | `.pawbytes/config/module-help.csv` |
| Output directories | `.pawbytes/creative-suites/` |

## Configuration Values

### Core Config (written to both files)

| Key | Description | Default |
|-----|-------------|---------|
| `user_name` | How to address the user | `user` |
| `communication_language` | Language for interactions | `English` |
| `document_output_language` | Language for generated content | `English` |

### Module Config

| Key | Description | Required |
|-----|-------------|----------|
| `fal_key` | fal.ai API key for image/video generation | **Yes** |
| `elevenlabs_api_key` | ElevenLabs API key for AI voiceover | Optional |
| `pexels_api_key` | Pexels API key for stock media research | Optional |
| `default_brand` | Default brand name | null |
| `output_directory` | Where assets are saved | `.pawbytes/creative-suites` |

## Quick Example

**Input**: "Setup creative suites, my name is Alex, fal key is abc123"

**Output**: Configuration written with user_name=Alex, fal_key=abc123 (stored in config.user.yaml). Directories created at `.pawbytes/creative-suites/`. Greeting message displayed from module.yaml. Ready to use Aria Creative Suite.

## File Structure After Setup

```
{project-root}/
  .pawbytes/
    config/
      config.yaml           # Shared config (committed)
      config.user.yaml      # User settings (gitignored)
      module-help.csv       # Capability registry
    creative-suites/
      index.md              # Agency memory index
      brands/               # Brand guidelines and assets
      knowledge/            # Research and references
      daily/                # Activity logs
```

## Arguments

| Arg | Description |
|-----|-------------|
| `accept all defaults` | Skip prompting, use default values |
| `--headless` | Non-interactive setup with defaults |
| Inline values | e.g., "user name is Alice, fal key is abc123" |

## Anti-Zombie Pattern

Existing entries for this module are removed before writing fresh ones, so stale values never persist. This ensures clean updates on reconfiguration.

## Related Skills

- [paw-cra-agent-creative-director](./paw-cra-agent-creative-director.md) -- Start here after setup
- All other Creative Suite skills require this setup to be completed first