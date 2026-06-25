# Network Routing Lab

## Lab Purpose

This lab defines the implementation boundary for:

02-network-routing-lab

## Lab Focus

Routing, VPN, WAN, DNS, reachability, latency, packet loss, and route recovery validation.

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

- [Network Routing Execution Boundary Note](validation-reports/network-routing-execution-note.md)

## Phase 2 Network Routing Runtime

This lab includes deterministic local network routing validation as a Phase 2 runtime extension.

Runtime model:

- network routing workspace setup
- deterministic route table generation
- subnet boundary validation
- gateway mapping validation
- reachability decision generation
- local-only generated validation evidence

### Routing Validation Model

This lab does not create privileged Linux network namespaces.

Instead, it validates a deterministic routing-state dataset that represents operational network path validation.

Validated routing segments:

| Segment | Route | Gateway | Interface |
|---|---|---|---|
| App segment | 10.10.10.0/24 | 192.168.10.1 | eth0 |
| Data segment | 10.10.20.0/24 | 192.168.20.1 | eth1 |
| Recovery segment | 10.10.30.0/24 | 192.168.30.1 | eth2 |
| Default route | 0.0.0.0/0 | 192.168.10.254 | eth0 |

### One-command Execution

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/02-network-routing-lab"
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
| Network routing workspace prepared | PASS |
| Network target config present | PASS |
| Route table present | PASS |
| Subnet boundary present | PASS |
| Reachability targets present | PASS |
| Default route present | PASS |
| App segment route present | PASS |
| Data segment route present | PASS |
| Recovery segment route present | PASS |
| Gateway mapping valid | PASS |
| Reachability decision generated | PASS |
| End-to-end orchestration | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/local-route-table.log
- evidence/generated/raw/network-route-validation-matrix.tsv
- evidence/generated/raw/network-reachability-matrix.tsv
- evidence/generated/raw/network-routing-validate.log
- evidence/generated/summary/network-routing-runtime-summary.md
- evidence/generated/summary/network-routing-execution-summary.md

## Scenario Signal Validation

This lab includes scenario-level network signal validation in addition to basic routing readiness checks.

Additional validation script:

- scripts/validate-network-scenario-signals.sh

Scenario signal coverage:

- network path visibility
- endpoint reachability
- gateway reachability boundary
- DNS resolution boundary
- network interface visibility
- latency visibility
- packet loss visibility
- VPN connectivity boundary
- WAN link boundary
- load balancer path boundary

The generated runtime evidence remains local-only under evidence/generated.
