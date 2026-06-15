# SNSD Hybrid Infrastructure

Scenario-driven infrastructure operations platform for validating reusable operational capability boundaries.

## What this repository is

This repository combines three layers:

- operational scenarios for lifecycle-aligned validation cases
- implementation labs that define runnable boundaries for those scenarios
- reviewer-facing reports and evidence for quality, coverage, and readiness

## Start here

1. [docs/repository-orientation.md](docs/repository-orientation.md) — repository map and reading path
2. [labs/README.md](labs/README.md) — implementation lab catalog
3. [scenarios/README.md](scenarios/README.md) — scenario catalog by lifecycle level
4. [validation-reports/README.md](validation-reports/README.md) — concise review summaries

## Repository map

| Area | Purpose |
|---|---|
| [docs/](docs/) | Stable reviewer-facing documentation |
| [labs/](labs/) | Implementation-oriented lab boundaries |
| [scenarios/](scenarios/) | Lifecycle-aligned operational scenarios |
| [modules/](modules/) | Reusable module catalog |
| [adapters/](adapters/) | Adapter catalog |
| [shared-runtime/](shared-runtime/) | Shared runtime and integration boundary |
| [validation-reports/](validation-reports/) | Reviewer-facing validation summaries |
| [reports/](reports/) | Detailed generated diagnostics |

## Review flow

1. Read the repository overview and orientation.
2. Inspect the lab catalog and scenario catalog.
3. Open a lab README to review runtime boundaries and validation intent.
4. Use the validation reports to confirm readiness and evidence status.

## Current baseline

- 150 lifecycle-aligned scenarios
- 10 implementation labs
- 5 scenario maturity levels
- 6 operational lifecycle stages
- 10 runtime boundary notes

## Evidence boundary

Committed content includes scripts, documentation, and reviewer-facing summaries.

Local-only content includes raw execution output, temporary runtime workspaces, and generated evidence that is intentionally excluded from Git.

## Operational lifecycle

Detection → Correlation and analysis → Incident coordination → Recovery and automation → Recovery validation → Governance and reporting
