# Pawbytes Tools Suite

Three automation tools that handle technical workflows so you can focus on your work.

## What's Inside

| Tool | What It Does | Who Should Use It |
|------|--------------|-------------------|
| [Presentation Builder](./skills/paw-tools-presentation.md) | Transform marketing plans into McKinsey-style HTML presentations | Marketing teams presenting strategies to stakeholders |
| [Release Automation](./skills/paw-tools-release.md) | Automate software releases from version bump to GitHub release | Developers releasing new versions |
| [Tools Setup](./skills/paw-tools-setup.md) | Configure Pawbytes Tools for your project | Anyone setting up Pawbytes for the first time |

## Quick Navigation

### I want to...

- **Present a marketing strategy** → [Presentation Builder](./skills/paw-tools-presentation.md)
- **Release a new version of my software** → [Release Automation](./skills/paw-tools-release.md)
- **Set up Pawbytes Tools in my project** → [Tools Setup](./skills/paw-tools-setup.md)

### I'm coming from...

- **Marketing Suite** → Use [Presentation Builder](./skills/paw-tools-presentation.md) to turn your SOSTAC plans into executive-ready decks
- **Creative Suite** → Use [Presentation Builder](./skills/paw-tools-presentation.md) when campaign strategy or results need to be presented, or [Tools Setup](./skills/paw-tools-setup.md) when configuring utility workflows
- **New project** → Start with [Tools Setup](./skills/paw-tools-setup.md)

## Workflows

| Workflow | Description | Time |
|----------|-------------|------|
| [Presentation from Marketing Plan](./workflows/presentation-from-marketing-plan.md) | End-to-end: SOSTAC plan to polished presentation | 10-15 min |

## Prerequisites

### For Presentation Builder
- A marketing plan, strategy document, or content to present
- (Optional) Brand configuration from `paw-mkt-setup`

### For Release Automation
- A Git repository
- GitHub CLI (`gh`) installed and authenticated
- Conventional commit messages (`feat:`, `fix:`, `breaking:`)

### For Tools Setup
- A project directory where you want to use Pawbytes Tools

## Installation

Pawbytes Tools are included in the Pawbytes Skill Suites:

```bash
npx skills add pawbytes/skill-suites
```

Individual tools activate based on your request — no separate installation needed.

## Configuration

Tools share configuration stored in:

```
{project-root}/.pawbytes/config/
├── config.yaml           # Shared settings
└── config.user.yaml      # Personal settings (API keys, gitignored)
```

Run **Tools Setup** to configure these settings interactively.