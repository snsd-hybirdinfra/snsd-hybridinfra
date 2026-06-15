# Repository Report Layer Guide

This document defines how the repository separates stable documentation, generated diagnostics, and reviewer-facing summaries.

## Layer model

| Directory | Purpose |
|---|---|
| docs/ | Stable reviewer documentation and reference material |
| reports/ | Detailed generated validation diagnostics for maintainers |
| validation-reports/ | Concise review summaries for reviewers |

## Policy

- Keep stable references in docs/
- Keep detailed checker output in reports/
- Keep reviewer-facing summaries in validation-reports/
- Keep local-only runtime summaries such as a.txt out of Git
