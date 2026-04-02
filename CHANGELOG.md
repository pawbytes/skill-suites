# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-04-02

### Added
- Monorepo consolidation of agentic-marketing-suites, creative-agency-suites, and utility-skills into a single repo published as `pawbytes/skill-suites`
- 41 skills across 3 modules: 23 marketing (`paw-mkt-*`), 15 creative agency (`paw-cra-*`), 3 tools (`paw-tools-*`)
- `src/{module}/` folder structure for maintainability — `src/marketing/`, `src/creative/`, `src/tools/`
- Unified `.claude-plugin/marketplace.json` with category-based install via `npx skills add pawbytes/skill-suites`
- `_bmad/bmb/` and `_bmad/core/` builder tooling for developing new skills
- `src/marketing/docs/` and `src/marketing/evals/` migrated from agentic-marketing-suites
- SEO-optimized marketplace and README descriptions for all three module categories
