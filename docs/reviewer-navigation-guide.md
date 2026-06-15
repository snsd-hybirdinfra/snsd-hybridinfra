# Reviewer Navigation Guide

## 1. Purpose

This guide provides a reviewer-facing navigation path for the SNSD Hybrid Infrastructure repository.

The repository is structured as a scenario-driven infrastructure operations platform. It is not a simple collection of scripts or isolated scenarios.

Reviewers should use this guide to understand:

- what the repository represents
- which documents to review first
- how scenarios connect to implementation labs
- how runtime validation is structured
- where evidence and reports are located

## 2. Recommended Review Path

| Step | Review Target | Purpose |
|---|---|---|
| 1 | Root README | Understand repository identity and platform scope |
| 2 | Phase 2 Runtime Completion Report | Confirm all 10 labs expose runtime boundaries |
| 3 | Scenario-to-Lab Traceability | Confirm all 150 scenarios map to implementation labs |
| 4 | Labs README | Review implementation lab catalog |
| 5 | Scenarios README | Review operational scenario catalog |
| 6 | Lab README files | Inspect execution commands and validation boundaries |
| 7 | Validation reports | Confirm repository quality and reviewer-facing summaries |

## 3. Core Repository Positioning

SNSD Hybrid Infrastructure is an enterprise operational capability platform.

The repository demonstrates infrastructure operations capabilities through:

- lifecycle-aligned operational scenarios
- reusable implementation labs
- runtime validation boundaries
- generated evidence
- reviewer-readable validation reports
- governance and reporting outputs

## 4. Key Reviewer Documents

| Document | Path | Review Purpose |
|---|---|---|
| Root README | README.md | Repository overview and entry point |
| Labs README | labs/README.md | Implementation lab catalog |
| Scenarios README | scenarios/README.md | Scenario catalog and lifecycle inventory |
| Phase 2 Runtime Completion Report | validation-reports/phase-2-runtime-completion-report.md | Runtime standard completion |
| Scenario-to-Lab Traceability | docs/scenario-to-lab-traceability.md | Scenario-to-lab mapping |
| Phase 3 Traceability Report | validation-reports/phase-3-traceability-report.md | Traceability validation summary |
| Lab Coverage Matrix | docs/lab-coverage-matrix.md | Lab and scenario coverage overview |

## 5. Runtime Review Path

Reviewers who want to inspect execution boundaries should start with the lab catalog.

Each implementation lab follows the Phase 2 runtime standard:

| Runtime Component | Purpose |
|---|---|
| setup.sh | Prepare the lab-local runtime workspace |
| validate.sh | Execute runtime validation and generate evidence |
| cleanup.sh | Clean runtime workspace without removing generated evidence |
| run.sh | Provide one-command runtime orchestration |
| run.sh --cleanup | Execute validation and clean runtime state automatically |

Some labs include additional scripts such as preflight.sh, backup.sh, or restore.sh when the runtime boundary requires them.

## 6. Lab Review Order

| Order | Lab | Review Focus |
|---|---|---|
| 1 | 01-linux-observability-lab | Linux host observability |
| 2 | 02-network-routing-lab | Network path and reachability validation |
| 3 | 03-ansible-automation-lab | Idempotency and rollback automation |
| 4 | 04-container-runtime-lab | Container runtime validation |
| 5 | 05-kolla-openstack-lab | OpenStack readiness boundary |
| 6 | 06-monitoring-stack-lab | Prometheus and alert validation |
| 7 | 07-logging-correlation-lab | Log correlation and incident timeline |
| 8 | 08-backup-recovery-lab | Backup, restore, and integrity validation |
| 9 | 09-resilience-failover-lab | Failover and resilience validation |
| 10 | 10-governance-reporting-lab | Evidence aggregation and governance reporting |

## 7. Scenario Review Path

Reviewers who want to inspect operational design should start with the scenario catalog.

Scenarios are organized by lifecycle level:

| Lifecycle Level | Meaning |
|---|---|
| level-1-visibility | Detection and visibility |
| level-2-correlation | Correlation and analysis |
| level-3-recovery | Recovery and automation |
| level-4-resilience | Resilience and failover |
| level-5-continuity | Enterprise continuity and governance |

The scenario-to-lab traceability document maps all operational scenarios to implementation labs.

## 8. Evidence Policy

Runtime evidence is intentionally generated locally.

The repository commits:

- source scripts
- README documentation
- generated reviewer-facing reports
- validation summaries

The repository excludes:

- lab-local runtime workspace output
- local generated runtime evidence
- temporary execution artifacts
- local repository summary output

This keeps the repository reviewable while preserving reproducible execution boundaries.

## 9. Reviewer Interpretation

Expected review chain:

Operational scenario catalog -> implementation lab boundary -> runtime validation scripts -> generated local evidence -> repository-level validation reports

This structure demonstrates infrastructure operations capability design, not isolated command execution.

## 10. Final Navigation Statement

A reviewer should be able to enter from the root README, follow the Phase 2 and Phase 3 reports, inspect labs and scenarios, and understand how the repository validates operational capabilities through implementation labs.