# Pawbytes Skill Suites Documentation

Welcome to the Pawbytes Skill Suites documentation. This monorepo contains 42 skills across three modules: Marketing, Creative, and Tools.

## Quick Navigation

| I want to... | Go to |
|--------------|-------|
| Plan marketing strategy | [Marketing: SOSTAC Planning](./marketing/workflows/sostac-planning.md) |
| Create content & campaigns | [Marketing: Content & Social](./marketing/user-guide/part-3-chapters-7-8.md) |
| Design visuals & videos | [Creative Suite](./creative/README.md) |
| Build presentations | [Tools: Presentation Builder](./tools/skills/paw-tools-presentation.md) |
| Automate releases | [Tools: Release Automation](./tools/skills/paw-tools-release.md) |

## Documentation by Module

### Marketing Suite (paw-mkt-*)
**24 skills** covering the full marketing stack.

- Strategic planning with SOSTAC methodology
- Channel execution: content, email, SEO, social, video, ads, PR
- Conversion optimization and revenue growth
- Analytics and dashboard generation

**Start here:** [Marketing Module](./marketing/README.md)

### Creative Suite (paw-cra-*)
**15 skills** for visual and video production.

- Agent-based creative team (Creative Director, Designer, Video Producer, Strategist)
- Design workflows: social posts, carousels, logos, brand assets
- Video workflows: short-form, long-form, clips
- Campaign orchestration and multi-platform export

**Start here:** [Creative Module](./creative/README.md)

### Tools Suite (paw-tools-*)
**3 skills** for productivity and automation.

- Presentation Builder: McKinsey-style HTML presentations
- Release Automation: Version bump to GitHub release
- Setup: Module installation and configuration

**Start here:** [Tools Module](./tools/README.md)

## Getting Started

New to the suites? Read the [Getting Started Guide](./getting-started.md) for:

- How to install each module
- Which module to start with
- First project checklist

## Install

```bash
# Install all skills
npx skills add pawbytes/skill-suites

# Install globally
npx skills add pawbytes/skill-suites --global

# Install one skill only
npx skills add pawbytes/skill-suites --skill paw-mkt-sostac
npx skills add pawbytes/skill-suites --skill paw-cra-agent-creative-director
npx skills add pawbytes/skill-suites --skill paw-tools-presentation
```

## Repository Structure

```
src/
├── marketing/   # paw-mkt-* skills (24 skills)
├── creative/    # paw-cra-* skills (15 skills)
└── tools/       # paw-tools-* skills (3 skills)
```

## Additional Resources

- [SOSTAC Gap Analysis](./sostac-gap-analysis.md) -- Framework coverage analysis