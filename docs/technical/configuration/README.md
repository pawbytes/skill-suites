# Configuration System

## Overview

The configuration system provides runtime settings and user preferences for Pawbytes Skill Suites. It uses a hierarchical approach with sensible defaults and user overrides.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Module Defaults** | Base configuration defined in `module.yaml` |
| **Project Config** | Shared settings in `config.yaml` |
| **User Overrides** | Personal settings in `config.user.yaml` |
| **Variable Tokens** | Substitution tokens like `{project-root}` |

## Configuration Hierarchy

```
┌─────────────────────────────────┐
│     Module Defaults             │  Lowest priority
│   (module.yaml defaults)        │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     Project Config              │
│   (.pawbytes/config/config.yaml)│
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     User Overrides              │  Highest priority
│   (config.user.yaml)            │
└─────────────────────────────────┘
```

Loading order: defaults → project config → user overrides. Later values override earlier ones.

## Documentation

| Document | Purpose |
|----------|---------|
| [Config Files](./config-files.md) | config.yaml and config.user.yaml format |
| [Variables](./variables.md) | Available tokens and substitution |
| [Module YAML](./module-yaml.md) | Module metadata and configuration schema |

## Quick Reference

### Config File Locations

```
{project-root}/
└── .pawbytes/
    └── config/
        ├── config.yaml        # Shared configuration
        └── config.user.yaml   # User overrides (gitignored)
```

### Variable Substitution

Variables use curly brace syntax:

```yaml
output_folder: "{project-root}/.pawbytes/marketing-suites"
reports_folder: "{project-root}/.pawbytes/marketing-suites/reports"
```

The `{project-root}` token is a **literal token** that signals the value is relative to the project root. Skills resolve this at runtime.

### Common Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `user_name` | User's name for personalized output | `Jane` |
| `communication_language` | Language for skill interaction | `English` |
| `document_output_language` | Language for generated documents | `English` |
| `output_folder` | Base output directory | `{project-root}/.pawbytes/marketing-suites` |

## See Also

- [Skill Specification: SKILL.md Format](../skill-specification/skill-md-format.md)
- [Artifacts: .pawbytes Directory](../artifacts/pawbytes-directory.md)