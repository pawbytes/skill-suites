# Reference Documentation

Quick reference documentation for Pawbytes Skill Suites contributors. Each document provides focused information on specific topics.

## Quick Reference Table

| Document | Purpose | When to Use |
|----------|---------|-------------|
| [Glossary](./glossary.md) | Technical term definitions | Encountering unfamiliar terminology |
| Path Resolutions | Output path patterns | Determining where files should be saved |
| Trigger Phrases | Skill activation patterns | Understanding how skills are discovered |

## What Each Reference Provides

### Glossary

The [glossary](./glossary.md) defines technical terms used throughout Pawbytes Skill Suites. Terms are organized by category:

- **General** — Core concepts like Skill, Module, Framework
- **Architecture** — System design terms like Coordinator, Specialist
- **Artifacts** — Output structures like Brand workspace, Campaign
- **Configuration** — Settings and variables

Use the glossary when you encounter unfamiliar terms in skill definitions or documentation.

### Path Resolutions

Path resolution documentation explains how output paths are constructed:

```
.pawbytes/{module}/{type}/{slug}/
```

This covers:
- Module-specific output directories
- Brand workspace paths
- Campaign and deliverable locations
- Variable substitution in paths

### Trigger Phrases

Trigger phrase documentation explains how skills are discovered:

- How description frontmatter enables skill discovery
- Pattern matching for user requests
- Best practices for writing trigger phrases
- Examples from existing skills

## Using Reference Documentation

Reference documentation is designed for quick lookup:

1. **Scan the table** to find the relevant document
2. **Open the document** for detailed information
3. **Return to your task** with the information you need

For comprehensive guides on skill development, see:
- [Skill Specification](../skill-specification/) — Complete SKILL.md format
- [Contributing](../contributing/) — Conventions and best practices
- [Architecture](../architecture/) — System design patterns

## Related Documentation

| Topic | Location |
|-------|----------|
| SKILL.md format | [Skill Specification](../skill-specification/skill-md-format.md) |
| Folder structure | [Skill Specification](../skill-specification/folder-structure.md) |
| Naming conventions | [Contributing](../contributing/naming-conventions.md) |
| Configuration system | [Configuration](../configuration/) |