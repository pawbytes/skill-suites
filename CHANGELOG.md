# Changelog

All notable changes to this project will be documented in this file.

## [1.1.2] - 2026-04-02

### Bug Fixes
- **paw-mkt-agency:** Use Glob pattern for brand discovery instead of directory scan to reliably find brands across platforms

## [1.1.1] - 2026-04-02

### Documentation
- Harden marketing skill templates for consistency and reliability
- Normalize marketing and creative module references across documentation
- Reorganize modules and standardize documentation quality
- Add documentation quality improvement plan

## [1.1.0] - 2026-04-02

### Features
- **paw-mkt-dashboard:** Add feature gap detection for existing dashboards — identifies missing visualization capabilities and recommends enhancements

### Chores
- Ignore `_bmad` directory in .gitignore
- Remove bmad mention from changelog

## [1.0.0] - 2026-04-02

### Added
- Monorepo consolidation of agentic-marketing-suites, creative-agency-suites, and utility-skills into a single repo published as `pawbytes/skill-suites`
- 41 skills across 3 modules: 23 marketing (`paw-mkt-*`), 15 creative agency (`paw-cra-*`), 3 tools (`paw-tools-*`)
- `src/{module}/` folder structure for maintainability — `src/marketing/`, `src/creative/`, `src/tools/`
- Unified `.claude-plugin/marketplace.json` with category-based install via `npx skills add pawbytes/skill-suites`
- `src/marketing/docs/` and `src/marketing/evals/` migrated from agentic-marketing-suites
- SEO-optimized marketplace and README descriptions for all three module categories
