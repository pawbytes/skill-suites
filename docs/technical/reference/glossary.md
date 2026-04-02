# Technical Glossary

Definitions of technical terms used throughout Pawbytes Skill Suites. Terms are organized by category for easy navigation.

## General

### Skill
A single-purpose capability defined in a SKILL.md file. Skills are the fundamental building blocks of Pawbytes Skill Suites, providing specialized functionality for specific tasks. Each skill has a unique name following the naming convention `{org}-{module}-{skillname}`.

### Module
A collection of related skills that share a configuration namespace, output directory structure, and naming convention (prefix). Modules organize skills into logical groups such as Marketing (`paw-mkt-`), Creative (`paw-cra-`), and Tools (`paw-tools-`).

### Framework
A domain-specific methodology file loaded progressively during skill execution. Frameworks contain structured knowledge (processes, checklists, examples) and are indexed in `frameworks-index.csv` for selective loading. See also: Progressive Disclosure.

### Reference
A documentation file loaded during skill execution. References include capabilities, best practices, and supporting documentation. Unlike frameworks, references are loaded directly without indexing.

### Capability
A specific function or service a skill provides. Capabilities are mapped to reference files in the SKILL.md capabilities table, enabling the skill to load relevant documentation on demand.

### Trigger Phrase
Natural language patterns included in a skill's description frontmatter that enable skill discovery. When a user's request matches a trigger phrase, the skill may be activated.

### Progressive Disclosure
A loading pattern where skills read only the knowledge they need, when they need it. Skills first read `frameworks-index.csv`, match the user's situation to the `best_for` column, then load only matched framework files. This conserves context and improves response relevance.

## Architecture

### Coordinator
A skill that orchestrates other skills. Coordinators assess user requests, load brand context, and route work to appropriate specialists. Examples: `paw-mkt-agency` (Marketing), `paw-cra-agent-creative-director` (Creative).

### Specialist
A focused skill that executes one discipline well. Specialists receive routed requests from coordinators and produce specific deliverables. Examples: `paw-mkt-seo`, `paw-cra-agent-designer`.

### Agent Skill
A persistent persona with memory and identity. Agent skills have an Identity section in SKILL.md, use the memory system, maintain conversation context, and may coordinate other skills. See also: Workflow Skill.

### Workflow Skill
A deterministic pipeline with defined steps. Workflow skills follow step-by-step processes with clear inputs and outputs, may support `--headless` mode, and have no persistent persona. See also: Agent Skill.

### Utility Skill
A single-purpose tool with minimal interaction. Utility skills perform quick, focused tasks, often support `--headless` mode, and may have CLI integration. Examples: `paw-tools-release`, `paw-tools-presentation`.

### Escalation Route
A defined pathway from one skill to another. Skills declare escalation routes to recommend follow-up skills based on signals detected during execution.

### Routing Pattern
The pattern by which a coordinator skill determines which specialist to invoke. Routing is typically based on request type, brand context, or explicit user direction.

### HITL (Human-in-the-Loop)
Review gates that require explicit user approval before proceeding. HITL gates prevent auto-advancement through multi-step processes without user confirmation.

## Artifacts

### Brand Workspace
A local folder under `brands/{brand-slug}/` that stores strategy, campaign work, content, and analytics for one brand. The brand workspace is the primary organizational unit for marketing and creative work.

### Brand Context
A lightweight onboarding document saved as `brand-context.md`. Contains essential brand information: what the company does, target audience, stage, USP, current marketing status, and competitors.

### Product Marketing Context
A deeper positioning document saved as `product-marketing-context.md`. Focuses on personas, differentiation, objections, customer language, and proof points.

### Campaign
A coordinated marketing or creative initiative with defined objectives, timeline, and deliverables. Campaigns are stored in `campaigns/{type}-{slug}/` within a brand workspace.

### SOSTAC
A six-phase marketing planning model used as the primary strategic framework in Marketing Suite:
- **S**ituation — Current state analysis
- **O**bjectives — Goals and KPIs
- **S**trategy — High-level approach
- **T**actics — Specific actions
- **A**ction — Implementation timeline
- **C**ontrol — Measurement and review

### .pawbytes Directory
The primary output location for all skill artifacts. Should be added to `.gitignore`. Contains configuration, brand workspaces, and generated content.

### Output Contract
The structured output a skill commits to delivering. Output contracts typically include: deliverable type, key findings, recommendations, files saved, and next steps.

### Video Manifest
A `video-manifest.json` file produced by video workflows containing metadata about generated videos: duration, resolution, codec, scenes, and platform specifications.

## Configuration

### Variable
A named value that can be referenced in skill execution. Variables are defined in `module.yaml` and resolved at runtime. Standard variables include `{user_name}`, `{communication_language}`, `{project-root}`.

### Config File
A YAML file storing configuration values. Configuration exists at three levels:
1. **Module defaults** — `assets/module.yaml` in setup skill
2. **Project config** — `.pawbytes/config/config.yaml`
3. **User overrides** — `.pawbytes/config/config.user.yaml`

### module.yaml
A YAML file in a setup skill's `assets/` folder that defines module metadata and configuration variables. Includes: code, name, description, version, greeting, and variable definitions.

### Config Hierarchy
The priority order for configuration values: user overrides > project config > module defaults. Higher-priority values override lower-priority ones.

### Sensitive Variable
A configuration variable marked `sensitive: true` in module.yaml. Sensitive values (API keys, tokens) are not logged and should be written to `config.user.yaml`.

### User Setting
A configuration variable marked `user_setting: true` in module.yaml. User settings are saved to `config.user.yaml` rather than shared `config.yaml`.

### Project Root Token
The literal string `{project-root}` used in config values to indicate a path relative to the project root. Should not be substituted with actual paths in config files.

## Memory and State

### Memory System
A persistent storage mechanism for agent skills to maintain context across sessions. Memory is stored in `.pawbytes/{module}/index.md` and brand-specific files.

### On Activation
A section in SKILL.md defining steps executed when a skill activates. Typically includes loading configuration, checking for existing context, and initializing state.

### Sidecar Memory
Memory stored alongside project files in `.pawbytes/`. Provides context for agent skills without requiring explicit project files.

### Campaign Status
A tracking file (`status.md`) within a brand workspace showing SOSTAC phase completion, active campaigns, and next steps.

## Skill Development

### Frontmatter
YAML metadata at the top of SKILL.md containing `name` and `description` fields. The description should include trigger phrases for skill discovery.

### Identity Section
A section in agent skill SKILL.md defining how the skill presents itself: name, role, personality traits, and communication style.

### Principles
Core guidelines that direct a skill's behavior. Principles are listed in SKILL.md and influence all skill decisions.

### Response Protocol
A step-by-step workflow defined in SKILL.md for handling user requests. Ensures consistent, thorough execution.

### Path Resolution
The mapping of output locations in SKILL.md. Defines where deliverables, brand context, campaigns, and reports are saved.

### Best For Column
A column in `frameworks-index.csv` describing when to use a particular framework. Skills match user situations to `best_for` values for progressive disclosure.

---

## Cross-Reference Index

| Term | Related Terms |
|------|---------------|
| Skill | Module, Capability, Trigger Phrase |
| Module | Skill, Configuration, Naming Convention |
| Framework | Progressive Disclosure, Reference, Capability |
| Coordinator | Specialist, Routing Pattern, Agent Skill |
| Brand Workspace | Brand Context, Campaign, .pawbytes Directory |
| Configuration | Variable, module.yaml, Config Hierarchy |
| Agent Skill | Workflow Skill, Identity Section, Memory System |
| SOSTAC | Campaign, Brand Workspace |