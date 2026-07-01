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

## Phase 2 Linux Observability Runtime

This lab includes deterministic local Linux observability validation as a Phase 2 runtime extension.

Runtime model:

- Linux observability preflight validation
- runtime workspace setup
- OS release signal collection
- CPU signal collection
- memory signal collection
- disk usage signal collection
- process snapshot collection
- service-like signal collection
- local-only generated validation evidence

### Observability Validation Model

This lab validates local Linux host observability signals without requiring privileged host changes.

Validated signal groups:

| Signal Group | Evidence Purpose |
|---|---|
| OS release | Host identity and platform visibility |
| CPU | Processor visibility baseline |
| Memory | Host memory visibility baseline |
| Disk usage | Filesystem visibility baseline |
| Process snapshot | Process visibility baseline |
| Service-like signals | Runtime service/process visibility baseline |

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/01-linux-observability-lab"
    bash scripts/run.sh

Run and clean up automatically:

    bash scripts/run.sh --cleanup

### Manual Execution Flow

    bash scripts/preflight.sh
    bash scripts/setup.sh
    bash scripts/validate.sh
    bash scripts/cleanup.sh

### Expected Runtime Result

| Signal | Expected Status |
|---|---|
| Linux observability preflight | PASS |
| Linux observability workspace prepared | PASS |
| OS release signal collected | PASS |
| CPU signal collected | PASS |
| Memory signal collected | PASS |
| Disk usage signal collected | PASS |
| Process snapshot collected | PASS |
| Service-like signal collected | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/linux-observability-preflight.log
- evidence/generated/raw/linux-observability-setup.log
- evidence/generated/raw/linux-os-release.log
- evidence/generated/raw/linux-cpuinfo.log
- evidence/generated/raw/linux-meminfo.log
- evidence/generated/raw/linux-disk-usage.log
- evidence/generated/raw/linux-process-snapshot.log
- evidence/generated/raw/linux-service-like-signals.log
- evidence/generated/raw/linux-observability-validate.log
- evidence/generated/processed/linux-observability-processed-summary.md
- evidence/generated/summary/linux-observability-runtime-summary.md
- evidence/generated/summary/linux-observability-execution-summary.md

## Scenario Observability Validation

This lab includes scenario-level Linux observability validation in addition to basic host readiness checks.

Additional validation script:

- scripts/validate-linux-observability-signals.sh

Scenario signal coverage:

- compute resource monitoring
- filesystem health visibility
- process health monitoring
- hardware health monitoring boundary
- server service recovery visibility
- compute resource correlation
- filesystem failure correlation
- Linux operational visibility
- system event visibility

Generated observability artifacts:

- system identity sample
- CPU sample
- memory sample
- disk sample
- filesystem sample
- process sample
- system event boundary
- scenario signal matrix
- Linux observability runtime summary

The generated runtime evidence remains local-only under evidence/generated.
