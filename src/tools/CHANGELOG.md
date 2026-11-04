# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Output moved from `.pawbytes/tools-output/` to `paw-suites/tools/`, with a generated `README.md` index and a README dashboard per item. New presentations are dated `YYYY-MM-DD-<slug>.html`; folder keys live in the `tools` config section; presentations read brand info from the marketing suite's `brand-context.md`.
- Old trees keep working: each skill detects them through the bundled `scripts/paw-paths.py` and maps paths, and the setup skill offers a dry-run-first migration that never overwrites and leaves `MOVED.md` behind.

## [0.1.0] - 2026-04-01

### Features
- **paw-tools-release:** Automated software release workflow with version bumping, changelog generation, git tagging, and GitHub release creation
- **paw-tools-presentation:** Modular slide templates for McKinsey-style HTML presentation generation
- **paw-tools-setup:** Pawbytes Tools module setup with `.claude-plugin` convention

### Bug Fixes
- **marketplace.json:** Update to plugins format for "All" selection support

### Other Changes
- Initial commit