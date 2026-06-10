# Repository Report Layer Guide

This document defines the role of repository documentation and report layers.

---

## Layer Model

| Directory | Role | Audience |
|---|---|---|
| docs/ | Reviewer-facing repository documentation and coverage references | Reviewer |
| reports/ | Generated detailed checker outputs | Maintainer |
| validation-reports/ | Reviewer-facing validation summaries | Reviewer |

---

## docs/

The docs directory contains stable repository documentation.

Expected contents include:

- lab coverage matrix
- repository tree
- reviewer-facing reference documents

The docs directory should not be used for raw checker output.

---

## reports/

The reports directory contains generated checker outputs.

Expected contents include:

- markdown link check results
- top-level structure check results
- repository language check results
- lab readiness alignment check results
- simplification candidate reports
- detailed validation diagnostics

The reports directory is useful for maintainers and repository quality control.

---

## validation-reports/

The validation-reports directory contains reviewer-facing summaries.

Expected contents include:

- lab readiness summary
- portfolio health summary
- repository validation summary
- final readiness summaries

The validation-reports directory should be concise and easy to review.

---

## Local-Only Output

The local file a.txt is used as an executive repository summary during local validation.

It is intentionally local-only and should not be committed.

---

## Policy

- Detailed diagnostics belong in reports/
- Reviewer-facing validation summaries belong in validation-reports/
- Stable repository references belong in docs/
- Local-only working summaries remain ignored
