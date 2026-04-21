# Skill Specification

## Overview

This section defines the complete specification for Pawbytes Skill Suites skills. Every skill follows a consistent structure that enables discovery, routing, and execution.

## What is a Skill?

A skill is a single-purpose capability defined in a `SKILL.md` file with supporting reference documents, frameworks, and assets. Skills are the atomic units of functionality in the Pawbytes ecosystem.

## Skill Types

| Type | Description | Example |
|------|-------------|---------|
| **Agent** | Persistent persona with memory and identity | `paw-mkt-agent-agency`, `paw-cra-agent-designer` |
| **Workflow** | Deterministic pipeline with defined steps | `paw-cra-video-shortform`, `paw-mkt-sostac` |
| **Utility** | Single-purpose tool with minimal interaction | `paw-tools-release`, `paw-tools-presentation` |

## Documentation Index

| Document | Purpose |
|----------|---------|
| [Folder Structure](./folder-structure.md) | What goes in a skill folder |
| [SKILL.md Format](./skill-md-format.md) | Complete SKILL.md specification |
| [Frameworks](./frameworks.md) | Framework files and CSV index |
| [References](./references.md) | Reference documents pattern |
| [Assets](./assets.md) | Static assets, configs, scripts |

## Quick Reference

### Required Elements

Every skill must have:

1. **SKILL.md** - Main skill definition with YAML frontmatter
2. **name** in frontmatter - Following naming convention `{org}-{module}-{skillname}`
3. **description** in frontmatter - Including trigger phrases

### Common Patterns

```
skill-name/
├── SKILL.md                    # Required
├── references/                 # Knowledge files
│   ├── capability-*.md         # Capability documentation
│   ├── frameworks-index.csv    # Progressive disclosure index
│   └── frameworks/             # Domain-specific methodologies
└── assets/                     # Static resources
    └── module.yaml             # Setup skills only
```

### Naming Convention

Skills follow the pattern: `{org}-{module}-{skillname}`

| Part | Format | Examples |
|------|--------|----------|
| org | 3 letters | `paw` |
| module | 3 letters | `mkt`, `cra`, `tools` |
| skillname | kebab-case | `seo`, `agent-designer`, `video-shortform` |

**Valid examples:**
- `paw-mkt-seo`
- `paw-cra-agent-designer`
- `paw-tools-release`