# Container Runtime Lab

## Lab Purpose

This lab defines the implementation boundary for:

04-container-runtime-lab

## Lab Focus

Docker runtime visibility, container health, logs, restart recovery, and container evidence.

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

- [Container Runtime Execution Boundary Note](validation-reports/container-runtime-execution-note.md)

## Phase 2 Container Runtime

This lab includes deterministic local Docker Compose runtime validation as a Phase 2 runtime extension.

Runtime model:

- container runtime workspace setup
- Docker CLI availability validation
- Docker Compose availability validation
- Docker Compose service startup
- container running-state validation
- HTTP endpoint response validation
- local-only generated validation evidence

### Container Runtime Model

The runtime starts a local NGINX container through Docker Compose.

Validated runtime inputs:

| Input | Purpose |
|---|---|
| compose/docker-compose.yml | Docker Compose runtime definition |
| configs/index.html | Static web response used for endpoint validation |
| scripts/run.sh | One-command runtime orchestration entrypoint |

Runtime endpoint:

    http://localhost:18080

Compose project name:

    snsd-container-runtime-lab

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/04-container-runtime-lab"
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
| Docker CLI available | PASS |
| Docker Compose available | PASS |
| Compose file present | PASS |
| Web index file present | PASS |
| Container started | PASS |
| Container running | PASS |
| HTTP endpoint responded | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/container-runtime-status.tsv
- evidence/generated/raw/container-compose-ps.log
- evidence/generated/raw/container-web.log
- evidence/generated/raw/container-web-endpoint.html
- evidence/generated/raw/container-runtime-validate.log
- evidence/generated/summary/container-runtime-summary.md
- evidence/generated/summary/container-runtime-execution-summary.md

## Scenario Container Runtime Validation

This lab includes scenario-level container runtime validation in addition to basic runtime readiness checks.

Additional validation script:

- scripts/validate-container-runtime-signals.sh

Scenario signal coverage:

- container runtime visibility
- Kubernetes cluster visibility
- Kubernetes cluster health monitoring
- pod failure correlation
- container dependency analysis
- container failover automation
- cluster node recovery orchestration
- Kubernetes node recovery
- Kubernetes service recovery
- service mesh traffic visibility
- service mesh latency correlation
- cross-region Kubernetes resilience

Generated container runtime artifacts:

- mock container workload spec
- runtime boundary log
- container health signal log
- restart/failover boundary log
- service dependency boundary log
- scenario signal matrix
- container runtime summary

The generated runtime evidence remains local-only under evidence/generated and runtime/.
