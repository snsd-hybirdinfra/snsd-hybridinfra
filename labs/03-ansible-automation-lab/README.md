# Ansible Automation Lab

## Lab Purpose

This lab defines the implementation boundary for:

03-ansible-automation-lab

## Lab Focus

Inventory, SSH access, playbook execution, rollback, recovery, validation, and automation evidence.

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

- [Ansible Automation Execution Boundary Note](validation-reports/ansible-automation-execution-note.md)

## Phase 2 Ansible Idempotency and Rollback Runtime

This lab includes deterministic local Ansible automation validation as a Phase 2 runtime extension.

Runtime model:

- local Ansible CLI validation
- deterministic automation marker creation
- repeated playbook execution
- idempotency validation on the second run
- rollback playbook execution
- rollback result validation
- local-only generated validation evidence

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/03-ansible-automation-lab"
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
| Ansible CLI available | PASS |
| First automation apply completed | PASS |
| Second automation apply completed | PASS |
| Idempotency confirmed on second run | PASS |
| Rollback playbook completed | PASS |
| Rollback removed runtime marker | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/ansible-version.txt
- evidence/generated/raw/phase2-idempotency-first.log
- evidence/generated/raw/phase2-idempotency-second.log
- evidence/generated/raw/phase2-rollback.log
- evidence/generated/summary/ansible-automation-runtime-summary.md
