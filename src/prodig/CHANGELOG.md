# Changelog

All notable changes to the Prodig Suites module will be documented in this file.

## [Unreleased]

### Changed
- Output moved from `.pawbytes/prodig-suites/` to `paw-suites/products/`, with a generated `README.md` index and a README dashboard per item. Each product lives in one folder (`plan/`, `build/`, `package/`, `research/`, `audience/`); the sidecar memory becomes `_memory/`, standards move to `_standards/`. Config keys `output_folder` → `products_folder`, `sidecar_folder` → `memory_folder`. Removed `cleanup-legacy.py` and all `_bmad` references.
- Old trees keep working: each skill detects them through the bundled `scripts/paw-paths.py` and maps paths, and the setup skill offers a dry-run-first migration that never overwrites and leaves `MOVED.md` behind.

## [0.1.1] - 2026-04-07

### Fixed
- Add module-help.csv for capability registration (#3)
- Add missing scripts folder for module registration (#4)

## [0.1.0] - 2026-04-03

### Added
- **paw-ps-setup**: Setup skill for Prodig module configuration
- **paw-ps-agent-product-builder**: Coordinator skill for product creation workflows
- **paw-ps-audience**: Audience discovery and persona construction
- **paw-ps-discovery**: Concept comparison and opportunity framing
- **paw-ps-research**: Demand signals, competitor analysis, and gap identification
- **paw-ps-research-to-brief**: Research synthesis and brief creation
- **paw-ps-strategist**: Product shaping and execution handoff
- **paw-ps-concept-to-product-plan**: Plan creation from validated concepts
- **paw-ps-software-executor**: Software product execution (MVP, PRD, features)
- **paw-ps-knowledge-executor**: Knowledge product execution (courses, ebooks, memberships)
- **paw-ps-service-executor**: Service product execution (offers, pricing, onboarding)
- **paw-ps-template-executor**: Template and digital kit creation
- **paw-ps-product-package-assembler**: Artifact gathering and bundle organization
- **paw-ps-publish-ready-check**: Quality assessment and readiness verification

---

## Release Summary

| Version | Date | Skills Count | Key Changes |
|---------|------|--------------|-------------|
| 0.1.1 | 2026-04-07 | 14 | Module registration fixes |
| 0.1.0 | 2026-04-03 | 14 | Initial release with full product creation suite |