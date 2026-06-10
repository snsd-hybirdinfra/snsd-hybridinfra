# SNSD Hybrid Infrastructure

SNSD Hybrid Infrastructure is a scenario-driven infrastructure operations portfolio.

The repository models enterprise operational capabilities through lifecycle-aligned scenarios and implementation-oriented labs.

---

## Repository Positioning

This repository is positioned as an:

**Enterprise Operational Capability Platform**

It is not a simple scenario collection.

Scenarios define operational validation cases.

Labs define implementation boundaries for validating those scenarios.

Modules, adapters, and shared runtime directories define reusable capability catalogs and lab-local execution boundaries.

---

## Operational Lifecycle

The repository follows this operational lifecycle:

Detection → Correlation & Analysis → Incident Coordination → Recovery & Automation → Recovery Validation → Governance & Reporting

---

## Repository Scope

| Area | Count |
|---|---:|
| Lifecycle-aligned scenarios | 150 |
| Implementation labs | 10 |
| Scenario levels | 5 |
| Operational lifecycle stages | 6 |

---

## Implementation Labs

| Lab | Focus |
|---|---|
| [01-linux-observability-lab](./labs/01-linux-observability-lab/README.md) | Linux host visibility, process health, filesystem state, service monitoring, and system events |
| [02-network-routing-lab](./labs/02-network-routing-lab/README.md) | Routing, VPN, WAN, DNS, reachability, latency, packet loss, and route recovery validation |
| [03-ansible-automation-lab](./labs/03-ansible-automation-lab/README.md) | Inventory, SSH access, playbook execution, rollback, recovery, validation, and automation evidence |
| [04-container-runtime-lab](./labs/04-container-runtime-lab/README.md) | Docker runtime visibility, container health, logs, restart recovery, and container evidence |
| [05-kolla-openstack-lab](./labs/05-kolla-openstack-lab/README.md) | Kolla-Ansible based OpenStack control plane, compute, network, service recovery, and evidence |
| [06-monitoring-stack-lab](./labs/06-monitoring-stack-lab/README.md) | Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence |
| [07-logging-correlation-lab](./labs/07-logging-correlation-lab/README.md) | Log collection, event normalization, OpenSearch query readiness, correlation, timeline reconstruction, and evidence |
| [08-backup-recovery-lab](./labs/08-backup-recovery-lab/README.md) | Backup job readiness, artifact validation, restore workflows, integrity checks, and recovery evidence |
| [09-resilience-failover-lab](./labs/09-resilience-failover-lab/README.md) | Failure detection, failover decision, traffic shift validation, recovery validation, and resilience evidence |
| [10-governance-reporting-lab](./labs/10-governance-reporting-lab/README.md) | Repository validation, coverage reporting, quality gates, documentation consistency, and governance reporting |

---

## Reviewer Entry Points

| Document | Purpose |
|---|---|
| [Lab Readiness Summary](./validation-reports/lab-readiness-summary.md) | Summarizes 10 lab documentation readiness |
| [Lab Coverage Matrix](./docs/lab-coverage-matrix.md) | Maps scenarios to implementation labs |
| [Repository Tree](./docs/repository-tree.md) | Shows reviewer-facing repository structure |
| [Report Layer Guide](./docs/report-layer-guide.md) | Explains docs, reports, and validation-reports roles |
| [Scenario Index](./scenarios/README.md) | Lists lifecycle-aligned operational scenarios |
| [Modules Index](./modules/README.md) | Lists repository-level capability module catalog |
| [Adapters Index](./adapters/README.md) | Lists repository-level adapter catalog |

---

## Current Baseline

| Area | Status |
|---|---|
| Scenario baseline | 150 scenarios |
| Lab baseline | 10 implementation labs |
| Lab readiness | documentation-ready |
| Implementation status | planned |
| Execution status | not yet executed |
| Evidence status | placeholder until lab execution |
| Repository validation | PASS |

---

## Report Layers

| Directory | Role |
|---|---|
| [reports/](./reports/) | Generated detailed checker outputs |
| [validation-reports/](./validation-reports/) | Reviewer-facing validation summaries |
| [docs/](./docs/) | Reviewer-facing repository documentation |
| [labs/](./labs/) | Implementation-oriented lab boundaries |
| [scenarios/](./scenarios/) | Lifecycle-aligned operational validation scenarios |

---

## Implementation Note

The current repository state defines documentation-ready lab boundaries.

Actual runtime execution, automation scripts, deployment artifacts, and evidence outputs are planned for the implementation phase.

