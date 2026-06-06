# Tools

This directory contains repository automation tools for generating, rendering, validating, and maintaining the SNSD Hybrid Infrastructure portfolio.

Tools are used to keep scenario documentation, metadata, diagrams, reports, and repository quality checks consistent across the platform.

---

## Tool Areas

| Tool Area | Purpose |
|---|---|
| content-generator | Generates scenario metadata, README files, repository indexes, relationship reports, and quality reports. |
| diagram-renderer | Renders operational poster diagrams for scenario-level visual documentation. |

---

## Current Tooling

### Content Generator

The `content-generator` toolset supports repository documentation and governance automation.

Current responsibilities include:

- scenario README generation
- scenario inventory index generation
- module index generation
- adapter index generation
- related scenario generation
- repository quality checking
- temporary file cleanup

### Diagram Renderer

The `diagram-renderer` toolset supports scenario poster rendering.

Current responsibilities include:

- scenario poster SVG generation
- scenario poster PNG generation
- lifecycle-aware workflow visualization
- operational evidence visual summary generation

---

## Standard Workflow

Repository maintenance should follow this workflow:

    generate
    validate
    cleanup
    review diff
    commit
    push

Recommended validation command sequence:

    python .\tools\content-generator\check_repository_quality.py
    python .\tools\content-generator\cleanup_temporary_files.py

---

## Governance Role

Tools support repository governance by reducing manual drift across:

- scenario metadata
- generated README files
- diagram artifacts
- relationship metadata
- quality reports
- temporary file hygiene

---

## Summary

The tools layer provides repeatable automation for maintaining the repository as a consistent operational capability platform rather than a manually edited scenario collection.
