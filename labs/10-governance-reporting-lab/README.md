# Governance Reporting Lab

## Lab Purpose

This lab defines the implementation boundary for:

10-governance-reporting-lab

## Lab Focus

Repository validation, coverage reporting, quality gates, documentation consistency, and governance reporting.

---

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |

---

## Lab Boundary

This lab is a documentation-ready implementation boundary.

It does not claim completed runtime execution until actual deployment, automation execution, validation, and evidence collection are performed.

---

## Core Documents

| Document | Link |
|---|---|
| Implementation Plan | [architecture/implementation-plan.md](./architecture/implementation-plan.md) |
| Scenario Coverage Report | [validation-reports/scenario-coverage-report.md](./validation-reports/scenario-coverage-report.md) |
| Lab Validation Report | [validation-reports/lab-validation-report.md](./validation-reports/lab-validation-report.md) |
| Evidence Boundary | [evidence/README.md](./evidence/README.md) |
| Scripts Boundary | [scripts/README.md](./scripts/README.md) |
| Shared Runtime | [shared-runtime/README.md](./shared-runtime/README.md) |

---

## Lab Components

| Component | Path |
|---|---|
| Modules | [modules/](./modules/) |
| Adapters | [adapters/](./adapters/) |
| Shared Runtime Runners | [shared-runtime/runners/README.md](./shared-runtime/runners/README.md) |
| Shared Runtime Validators | [shared-runtime/validators/README.md](./shared-runtime/validators/README.md) |
| Shared Runtime Parsers | [shared-runtime/parsers/README.md](./shared-runtime/parsers/README.md) |
| Raw Evidence | [evidence/raw/README.md](./evidence/raw/README.md) |
| Processed Evidence | [evidence/processed/README.md](./evidence/processed/README.md) |
| Evidence Summary | [evidence/summary/README.md](./evidence/summary/README.md) |

---

## Implementation Note

Runtime scripts, deployment artifacts, generated evidence, and execution outputs are planned for the implementation phase.

## Execution Boundary Note

- [Governance Reporting Execution Boundary Note](validation-reports/governance-reporting-execution-note.md)

## Phase 2 Governance Reporting Runtime

This lab includes governance-level runtime evidence aggregation as a Phase 2 runtime extension.

Runtime model:

- governance reporting workspace setup
- Phase 2 runtime evidence source scan
- runtime summary evaluation from upstream labs
- governance decision report generation
- local-only generated validation evidence

### Evidence Sources

The governance report aggregates local runtime summaries from:

| Lab | Runtime Evidence |
|---|---|
| 03 Ansible Automation | idempotency and rollback runtime summary |
| 06 Monitoring Stack | Prometheus alert rule runtime summary |
| 08 Backup Recovery | backup and restore integrity runtime summary |
| 09 Resilience Failover | NGINX failover runtime summary |

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/10-governance-reporting-lab"
    bash scripts/run.sh

Run and clean up automatically:

    bash scripts/run.sh --cleanup

### Manual Execution Flow

    bash scripts/setup.sh
    bash scripts/validate.sh
    bash scripts/cleanup.sh

### Expected Runtime Result

| Signal | Expected Status |
|---|---|
| Governance workspace prepared | PASS |
| Runtime evidence source scan completed | PASS |
| Ansible runtime evidence evaluated | PASS |
| Monitoring runtime evidence evaluated | PASS |
| Backup recovery runtime evidence evaluated | PASS |
| Resilience failover runtime evidence evaluated | PASS |
| Governance report generated | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/phase2-runtime-evidence-matrix.tsv
- evidence/generated/raw/governance-runtime-status.tsv
- evidence/generated/raw/governance-reporting-validate.log
- evidence/generated/summary/governance-reporting-runtime-summary.md
- evidence/generated/summary/governance-reporting-execution-summary.md

## Scenario Governance Reporting Validation

This lab includes scenario-level governance and reporting validation in addition to basic reporting readiness checks.

Additional validation script:

- scripts/validate-governance-reporting-signals.sh

Scenario signal coverage:

- enterprise change continuity
- enterprise cloud continuity
- enterprise control plane continuity
- enterprise data protection continuity
- enterprise identity continuity
- enterprise network continuity
- enterprise operational continuity
- enterprise platform continuity
- enterprise security continuity
- enterprise service continuity coordination
- governance reporting
- risk boundary management

Generated governance artifacts:

- enterprise scenario coverage summary
- continuity governance decision log
- governance risk register
- executive continuity report
- scenario signal matrix
- governance reporting runtime summary

The generated runtime evidence remains local-only under evidence/generated.
