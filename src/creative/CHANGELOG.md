# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Output moved from `.pawbytes/creative-suites/` to `paw-suites/creative/`, with a generated `README.md` index and a README dashboard per item. Brands hold dated `campaigns/YYYY-MM-<name>/`, standalone `designs/` and one `videos/` scheme (short-form, long-form, clips, motion-graphics, series); brand-less work lands in `brands/unassigned/`; memory moves to `_memory/`; `.auth/` stays hidden in `.pawbytes/creative/`. Removed the BMad naming note and the `_bmad` config check.
- Old trees keep working: each skill detects them through the bundled `scripts/paw-paths.py` and maps paths, and the setup skill offers a dry-run-first migration that never overwrites and leaves `MOVED.md` behind.

## [0.2.0] - 2026-04-01

### Added

- Paw-cra-setup module installer for Pawbytes Creative Suites — enables easy installation and setup of the creative agency module
- Visual/video production-first workflow architecture — routes visual/video deliverables directly to production agents (Designer, Video Producer) bypassing strategist gate
- Trigger field to Designer skill frontmatter — enables skill activation via triggers
- Quality improvements to Aria Creative Suite agents — enhanced agent capabilities and reliability

### Fixed

- 10 skill analysis findings across Aria Creative Suite — resolved structural and content issues identified in quality analysis
- Designer skill description for skills CLI compatibility — fixed formatting to ensure proper CLI parsing

### Changed

- Updated marketplace.json to v0.2.0 with full skill list — complete listing of all 14 skills in the suite
- Removed trigger field (consolidated) — cleaned up duplicate trigger definitions
- Updated SKILL.md documentation — improved skill documentation clarity
- Removed duplicate skills marketplace.json — consolidated to single source of truth at root

### Project Structure

- Initial commit establishing Pawbytes Creative Agency Suites — 4 specialist agents (Creative Director, Designer, Strategist, Video Producer) and 10 production workflows

---

**Note:** This project uses conventional commits for changelog generation. Using prefixes like `feat:`, `fix:`, `docs:`, `chore:` in commit messages helps automate changelog categorization.

[0.2.0]: https://github.com/pawbytes/creative-agency-suites/releases/tag/v0.2.0