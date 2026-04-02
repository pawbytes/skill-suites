# Changelog

All notable changes to the Agentic Marketing Suite will be documented in this file.

## [0.6.0] - 2026-04-02

### Features
- **paw-mkt-dashboard:** Add feature gap detection for existing dashboards — identifies missing visualization capabilities and recommends enhancements during discovery phase

## [0.5.0] - 2026-04-02

### Features
- **Dashboard Documents Route**: `paw-mkt-dashboard` now collects all `.md` files from brand workspaces during discovery and renders them as read-only formatted HTML in a `/documents` route — index page grouped by category with individual document detail views using server-side markdown rendering via `marked`

## [0.4.0] - 2026-04-02

### Added
- **Marketing Dashboard Skill**: New `paw-mkt-dashboard` skill (22nd specialist) for generating interactive standalone HTML dashboards — campaign tracking, analytics visualization, and SOSTAC progress monitoring
- **Dashboard Escalation Routes**: All 15 channel specialist skills now route to `paw-mkt-dashboard` for visualization needs
- **SOSTAC Escalation Routes**: Added escalation routes section to SOSTAC skill for post-planning handoff
- **Setup Test Scripts**: Added Python test scripts for cleanup-legacy, merge-config, and merge-help-csv

### Fixed
- **Video Deliverables Path**: Fixed relative path in video deliverables reference doc

### Chores
- Added `*.pyc` to `.gitignore`

## [0.3.7] - 2026-04-01

### Added
- **Deterministic Workflows**: Response protocols and output contracts across all skills for consistent agent behavior
- **Full Changelog History**: Comprehensive CHANGELOG.md documenting all releases

### Changed
- **Module Code Migration**: Changed module code from 'ams' to 'mkt' across all skills
- **Shared Config Structure**: Migrated to PawBytes ecosystem config structure
- **SKILL.md Standardization**: Standardized SKILL.md structure across all 22 marketing skills

### Fixed
- **Module Help**: Fixed corrupted text in module-help.csv from batch replace operation

## [0.3.6] - 2026-04-01

### Added
- **SOSTAC Plan Editing**: Explicit plan editing capability for flexible marketing plan management
- **Tool Discovery**: Chrome profile utilities and tool discovery for enhanced agent capabilities
- **HITL Review Gates**: Human-in-the-Loop review gates to SOSTAC agent for safer AI-assisted planning

### Changed
- Quality improvements across marketing suite agents
- Changed default user_name from BMad to Pawbytes in setup skill
- Updated documentation for new repository and skill naming conventions

## [0.3.5] - 2026-03-31

### Changed
- Repository migrated to `pawbytes/agentic-marketing-suites`
- Updated skill naming convention (e.g., `marketing-sostac` → `paw-mkt-sostac`)
- Updated marketplace.json for new repository structure

---

## Previous Releases (gnoviawan/agentic-marketing)

## [0.3.0] - 2026-03-08

### Added
- Marketplace.json for bulk skill installation via `npx skills add`

### Changed
- Normalized skill context routing across all 21 marketing skills
- Standardized around blank-page, codebase, and URL-first entry points
- Strategy-led skills no longer block on missing brand workspace files

## [0.2.0] - 2026-03-07

### Added
- **7 New Specialist Skills**: CRO, Launch, Pricing, Psychology, Retention, Sales, Product Marketing Context
- Programmatic SEO framework to marketing-seo skill
- Agent-browser auto-install fallback to all skills
- Ethical frameworks to CRO, Email, Pricing skills (dark patterns to avoid)
- AI/GEO (Generative Engine Optimization) coverage to Content, PR, Social skills
- Bidirectional escalation signals between Analytics, Retention, Email, Content

### Changed
- Enforced skill standards across all 21 skills (all under 500-line limit)
- Moved inline templates, benchmarks, frameworks to reference files
- Added bridging citations from every SKILL.md to reference files

### Fixed
- Duplicate section numbering in content, email, and paid-ads skills

## [0.1.0] - 2026-03-06

### Added
- **Initial Release** with 14 marketing specialist skills:
  - marketing-agency: Coordinator skill for multi-agent workflows
  - marketing-analytics: Measurement and attribution
  - marketing-community: Community building and engagement
  - marketing-content: Content strategy and creation
  - marketing-email: Email marketing campaigns
  - marketing-guerrilla: Unconventional marketing tactics
  - marketing-influencer: Influencer partnership strategy
  - marketing-paid-ads: Paid advertising across platforms
  - marketing-pr: Public relations and media outreach
  - marketing-referral: Referral program design
  - marketing-seo: Search engine optimization
  - marketing-social: Social media strategy
  - marketing-sostac: SOSTAC marketing planning framework
  - marketing-video: Video marketing strategy
- SOSTAC documentation with all 6 phases
- Brand workspace structure
- Project README with skills index

---

## Release Summary

| Version | Date | Skills Count | Key Changes |
|---------|------|--------------|-------------|
| 0.5.0 | 2026-04-02 | 22 | Dashboard documents route with markdown rendering |
| 0.4.0 | 2026-04-02 | 22 | Dashboard skill, escalation routes |
| 0.3.6 | 2026-04-01 | 21 | SOSTAC editing, HITL gates, tool discovery |
| 0.3.5 | 2026-03-31 | 21 | Repository migration, skill renaming |
| 0.3.0 | 2026-03-08 | 21 | Marketplace installation, normalized routing |
| 0.2.0 | 2026-03-07 | 21 | 7 new skills, ethical frameworks, GEO coverage |
| 0.1.0 | 2026-03-06 | 14 | Initial release with core marketing skills |

---

**Previous Repository**: https://github.com/gnoviawan/agentic-marketing
**Current Repository**: https://github.com/pawbytes/agentic-marketing-suites