# Logging Correlation Lab

## Lab Purpose

This lab defines the implementation boundary for:

07-logging-correlation-lab

## Lab Focus

Log collection, event normalization, OpenSearch query readiness, correlation, timeline reconstruction, and evidence.

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

- [Logging Correlation Execution Boundary Note](validation-reports/logging-correlation-execution-note.md)

## Phase 2 Logging Correlation Runtime

This lab includes deterministic local log correlation validation as a Phase 2 runtime extension.

Runtime model:

- logging correlation workspace setup
- deterministic operational log dataset generation
- event normalization into tabular evidence
- correlation-id based event grouping
- error, warning, and recovery pattern validation
- local-only generated validation evidence

### Correlation Model

The runtime validates an incident sequence using a deterministic correlation id:

    INC-2026-0701

The correlated event flow represents:

1. request intake
2. latency degradation
3. upstream timeout
4. retry execution
5. recovery completion
6. request completion

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/07-logging-correlation-lab"
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
| Logging workspace prepared | PASS |
| Operational log dataset created | PASS |
| Correlation source scan completed | PASS |
| Incident correlation key detected | PASS |
| Related events correlated | PASS |
| Error or warning pattern detected | PASS |
| Recovery pattern detected | PASS |
| Correlation report generated | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/normalized-events.tsv
- evidence/generated/raw/correlation-timeline.md
- evidence/generated/raw/logging-correlation-validate.log
- evidence/generated/summary/logging-correlation-runtime-summary.md
- evidence/generated/summary/logging-correlation-execution-summary.md

## Scenario Correlation Validation

This lab includes scenario-level logging and correlation validation in addition to basic logging readiness checks.

Additional validation script:

- scripts/validate-correlation-signals.sh

Scenario signal coverage:

- authentication anomaly analysis
- privilege escalation correlation
- change impact correlation
- cross-service anomaly correlation
- security policy violation analysis
- query lock analysis
- service dependency correlation
- traffic spike correlation

Generated correlation artifacts:

- raw mock events
- normalized events
- event timeline
- correlation findings
- root-cause hints

The generated runtime evidence remains local-only under evidence/generated.
