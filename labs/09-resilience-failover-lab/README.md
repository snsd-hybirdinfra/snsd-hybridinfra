# Resilience Failover Lab

## Lab Purpose

This lab defines the implementation boundary for:

09-resilience-failover-lab

## Lab Focus

Failure detection, failover decision, traffic shift validation, recovery validation, and resilience evidence.

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

- [Resilience Failover Execution Boundary Note](validation-reports/resilience-failover-execution-note.md)

## Phase 2 NGINX Failover Runtime

This lab includes an orchestrated local NGINX-based failover runtime.

Runtime model:

- NGINX failover entrypoint
- primary backend
- secondary backend
- primary failure simulation
- secondary traffic shift validation
- primary recovery validation

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/09-resilience-failover-lab"
    bash scripts/run.sh

Run and clean up automatically:

    bash scripts/run.sh --cleanup

### Manual Execution Flow

    bash scripts/setup.sh
    bash scripts/failover.sh
    bash scripts/validate.sh
    bash scripts/recover.sh
    bash scripts/cleanup.sh

### Expected Runtime Result

The end-to-end execution validates:

| Step | Expected Result |
|---|---|
| Initial response | primary backend |
| Primary failure | primary backend stopped |
| Failover response | secondary backend |
| Recovery response | primary backend |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/initial-primary-response.txt
- evidence/generated/raw/failover-response.txt
- evidence/generated/raw/recovery-response.txt
- evidence/generated/summary/resilience-failover-runtime-summary.md
