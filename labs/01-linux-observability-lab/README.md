# Linux Observability Lab

## Lab Purpose

This lab defines the implementation boundary for:

01-linux-observability-lab

## Lab Focus

Linux host visibility, process health, filesystem state, service monitoring, and system events.

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

---

## Execution Structure

| Document | Link |
|---|---|
| Execution Structure | [architecture/execution-structure.md](./architecture/execution-structure.md) |

---

## Execution Guide

| Document | Link |
|---|---|
| Execution Guide | [architecture/execution-guide.md](./architecture/execution-guide.md) |

---

## Execution Entrypoints

| Script | Link |
|---|---|
| Preflight | [scripts/preflight.sh](./scripts/preflight.sh) |
| Setup | [scripts/setup.sh](./scripts/setup.sh) |
| Validate | [scripts/validate.sh](./scripts/validate.sh) |
| Cleanup | [scripts/cleanup.sh](./scripts/cleanup.sh) |

---

## Evidence Parser

| Script | Link |
|---|---|
| Evidence Parser | [scripts/parse_evidence.py](./scripts/parse_evidence.py) |


## Local Execution Note

- [Local Execution Note](validation-reports/local-execution-note.md)
## Execution Boundary Status

| Execution Mode | Status |
|---|---|
| local-node | validated |
| remote-password | supported |
| remote-key-single-node | validated |
| remote-key-two-node | validated |
| generated runtime evidence | local-only |

## Monitoring Handoff

- [Monitoring Handoff Note](validation-reports/monitoring-handoff-note.md)
