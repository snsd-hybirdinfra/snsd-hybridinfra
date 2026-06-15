# Kolla OpenStack Lab

## Lab Purpose

This lab defines the implementation boundary for:

05-kolla-openstack-lab

## Lab Focus

Kolla-Ansible based OpenStack control plane, compute, network, service recovery, and evidence.

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

## Phase 2 Kolla OpenStack Readiness Runtime

This lab includes deterministic local OpenStack deployment readiness validation as a Phase 2 runtime extension.

Runtime model:

- OpenStack readiness workspace setup
- Kolla inventory boundary validation
- Kolla globals configuration validation
- control, compute, and network group validation
- deployment boundary decision generation
- local-only generated validation evidence

### Deployment Readiness Model

This lab does not perform a full OpenStack deployment.

Instead, it validates the deployment input boundary required before running Kolla-Ansible deployment workflows.

Validated inputs:

| Input | Purpose |
|---|---|
| inventory/multinode.ini | Kolla-Ansible inventory boundary |
| configs/globals.yml | Kolla global deployment configuration |
| configs/kolla-lab-policy.env | Lab-local deployment policy reference |

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/05-kolla-openstack-lab"
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
| OpenStack readiness workspace prepared | PASS |
| Kolla inventory present | PASS |
| Kolla globals present | PASS |
| Lab policy present | PASS |
| Control group present | PASS |
| Compute group present | PASS |
| Network group present | PASS |
| Required globals present | PASS |
| Deployment boundary defined | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/kolla-deployment-boundary-matrix.tsv
- evidence/generated/raw/kolla-preflight-raw.txt
- evidence/generated/raw/kolla-openstack-validate.log
- evidence/generated/summary/kolla-openstack-runtime-summary.md
- evidence/generated/summary/kolla-openstack-execution-summary.md
