# Technical Documentation

Welcome to the Pawbytes Skill Suites technical documentation. This section provides in-depth information for contributors, integrators, and architects who want to understand how the system works.

## Audience

| Audience | Documentation | Purpose |
|----------|---------------|---------|
| **Contributors** | Architecture, Contributing | Build new skills, follow patterns |
| **Integrators** | Skill Specification, Configuration | Use skills in projects |
| **Architects** | Architecture, Reference | Understand system design |

## Documentation Sections

### Contributing

Contributor standards, naming rules, validation guidance, and the reusable documentation improvement plan.

| Document | Description |
|----------|-------------|
| [Contributing Overview](./contributing/README.md) | Start here for contributor-facing guidance |
| [Documentation Quality Improvement Plan](./contributing/documentation-quality-improvement-plan.md) | Reusable phased plan for improving published docs |
| [Conventions](./contributing/conventions.md) | Standards and patterns for consistent authoring |
| [Validation Checklist](./contributing/validation-checklist.md) | Checklist for reviewing documentation quality |

### Architecture

System design and patterns that power Pawbytes Skill Suites.

| Document | Description |
|----------|-------------|
| [Architecture Overview](./architecture/README.md) | System diagram and key concepts |
| [Module System](./architecture/module-system.md) | How modules are structured and registered |
| [Skill Lifecycle](./architecture/skill-lifecycle.md) | Activation, execution, and completion flow |
| [Routing Patterns](./architecture/routing-patterns.md) | Coordinator to specialist routing |
| [Progressive Disclosure](./architecture/progressive-disclosure.md) | Framework loading pattern |

### Quick Links

- **SKILL.md Format** — See skill files in `src/marketing/paw-mkt-seo/SKILL.md` for examples
- **Module Registration** — See `.claude-plugin/marketplace.json`
- **Configuration** — See `src/marketing/paw-mkt-setup/assets/module.yaml`

## Key Concepts

### Modules

Collections of related skills sharing a namespace and output structure.

```
src/
├── marketing/    # paw-mkt-* (23 skills)
├── creative/     # paw-cra-* (15 skills)
└── tools/        # paw-tools-* (3 skills)
```

### Skills

Single-purpose capabilities defined in `SKILL.md` with:
- YAML frontmatter (name, description with triggers)
- Identity section (for agent skills)
- Capabilities table
- Response protocol
- Path resolution

### Frameworks

Domain knowledge loaded progressively:
- Indexed in `frameworks-index.csv`
- Loaded only when matched to user situation
- Keeps context window lean

### Configuration

Runtime settings loaded from:
- Module defaults (`module.yaml`)
- Project config (`config.yaml`)
- User overrides (`config.user.yaml`)

## Getting Started

1. **Understand Architecture** — Read [Architecture Overview](./architecture/README.md)
2. **Explore Skills** — Browse `src/marketing/paw-mkt-*` folders
3. **Study Patterns** — Review SKILL.md files and frameworks
4. **Build Skills** — Follow conventions documented here

## File Locations

| Purpose | Location |
|---------|----------|
| Skill definitions | `src/{module}/paw-{module}-{skill}/SKILL.md` |
| Reference files | `src/{module}/paw-{module}-{skill}/references/` |
| Framework index | `references/frameworks-index.csv` |
| Module config | `paw-{module}-setup/assets/module.yaml` |
| Marketplace | `.claude-plugin/marketplace.json` |