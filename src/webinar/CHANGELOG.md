# Changelog

All notable changes to the Webinar Creator Suite module will be documented in this file.

## [Unreleased]

### Changed
- Output moved from `.pawbytes/webinar-suites/` to `paw-suites/webinars/`, with a generated `README.md` index and a README dashboard per item. Each webinar sits directly under the root (no `webinars/` layer) with a README dashboard; memory moves to `_memory/`.
- Old trees keep working: each skill detects them through the bundled `scripts/paw-paths.py` and maps paths, and the setup skill offers a dry-run-first migration that never overwrites and leaves `MOVED.md` behind.

## [0.1.0] - 2026-04-03

### Added
- **paw-wbc-setup**: Setup skill for Webinar module configuration
- **paw-wbc-agent-discovery**: Discovery agent for webinar research and hook generation
- **paw-wbc-agent-producer**: Production agent for script and slide deck creation
- **paw-wbc-webinar-creation**: Workflow for end-to-end webinar creation

---

## Release Summary

| Version | Date | Skills Count | Key Changes |
|---------|------|--------------|-------------|
| 0.1.0 | 2026-04-03 | 4 | Initial release with webinar discovery and production suite |