# SNSD Hybrid Infrastructure

Scenario-driven Infrastructure Operations Platform

## Executive Overview

SNSD Hybrid Infrastructure is an Enterprise Operational Capability Platform for scenario-driven infrastructure operations.

This repository is not a simple scenario collection.

It models reusable enterprise operational capabilities through lifecycle-aligned scenarios and validates them through implementation-oriented labs.

The repository is organized around:

- lifecycle-aligned operational scenarios
- implementation labs
- reusable module and adapter catalogs
- shared runtime boundaries
- reviewer-facing validation reports
- local-only runtime evidence

## Repository Positioning

This repository is positioned as an:

**Enterprise Operational Capability Platform**

Scenarios define operational validation cases.

Labs define implementation boundaries for validating those scenarios.

Modules, adapters, and shared runtime directories define reusable capability catalogs and lab-local execution boundaries.

## Operational Lifecycle

Detection → Correlation & Analysis → Incident Coordination → Recovery & Automation → Recovery Validation → Governance & Reporting

## Current Baseline

| Area | Count / Status |
|---|---:|
| Lifecycle-aligned scenarios | 150 |
| Implementation labs | 10 |
| Execution boundary notes | 10 |
| Scenario levels | 5 |
| Operational lifecycle stages | 6 |
| Scenario poster SVG artifacts | 150 |
| Scenario poster PNG artifacts | 150 |
| Repository validation target | PASS |

## Runtime Implementation Baseline

The current implementation baseline provides execution boundaries for implementation labs.

| Lab | Runtime Boundary | Runtime Status |
|---|---|---|
| [01-linux-observability-lab](./labs/01-linux-observability-lab/README.md) | Linux host visibility and node exporter preparation | PASS |
| [02-network-routing-lab](./labs/02-network-routing-lab/README.md) | Route, DNS, latency, reachability, and service path validation | PASS |
| [03-ansible-automation-lab](./labs/03-ansible-automation-lab/README.md) | SSH, sudo, package, service, and playbook validation | PASS |
| [04-container-runtime-lab](./labs/04-container-runtime-lab/README.md) | Docker runtime, container health, endpoint, log, and restart validation | PASS |
| [05-kolla-openstack-lab](./labs/05-kolla-openstack-lab/README.md) | Kolla-Ansible preflight, inventory, globals, and command validation | PASS |
| [06-monitoring-stack-lab](./labs/06-monitoring-stack-lab/README.md) | Prometheus, Grafana, target scrape, and dashboard provisioning validation | PASS |
| [07-logging-correlation-lab](./labs/07-logging-correlation-lab/README.md) | Log normalization, timeline reconstruction, and correlation validation | PASS |
| [08-backup-recovery-lab](./labs/08-backup-recovery-lab/README.md) | Backup, restore, checksum, and integrity validation | PASS |
| [09-resilience-failover-lab](./labs/09-resilience-failover-lab/README.md) | Failure detection, failover decision, traffic shift, and recovery validation | PASS |
| [10-governance-reporting-lab](./labs/10-governance-reporting-lab/README.md) | Runtime summary aggregation and governance matrix validation | PASS |

## Reviewer Quick Start

Recommended review order:

1. [Lab Runtime Implementation Summary](./validation-reports/lab-runtime-implementation-summary.md)
2. [Lab Readiness Summary](./validation-reports/lab-readiness-summary.md)
3. [Lab Coverage Matrix](./docs/lab-coverage-matrix.md)
4. [Scenario Index](./scenarios/README.md)
5. [Implementation Labs](./labs/README.md)
6. [Report Layer Guide](./docs/report-layer-guide.md)
7. [Repository Tree](./docs/repository-tree.md)
8. [Runtime Evidence Policy](./docs/runtime-evidence-policy.md)
9. [Phase 2 Backlog](./docs/phase-2-backlog.md)

## Runtime Evidence Policy

Runtime evidence is generated locally and intentionally excluded from Git.

See [Runtime Evidence Policy](./docs/runtime-evidence-policy.md) for the scenario evidence and lab runtime evidence boundary.

Committed content includes:

- lab execution scripts
- validation scripts
- configuration examples
- execution boundary notes
- reviewer-facing validation reports
- repository quality reports

Local-only content includes:

- raw command output
- generated runtime summaries
- temporary runtime workspaces
- sensitive local execution artifacts

## Scenario Inventory

<!-- SCENARIO_INVENTORY_START -->
| Lifecycle Level | Scenario Count |
|---|---:|
| Level 1 Visibility | 45 |
| Level 2 Correlation | 41 |
| Level 3 Recovery | 33 |
| Level 4 Resilience | 21 |
| Level 5 Continuity | 10 |
| Total | 150 |
<!-- SCENARIO_INVENTORY_END -->

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

## Report Layers

| Directory | Role |
|---|---|
| [reports/](./reports/) | Generated detailed checker outputs |
| [validation-reports/](./validation-reports/) | Reviewer-facing validation summaries |
| [docs/](./docs/) | Reviewer-facing repository documentation |
| [labs/](./labs/) | Implementation-oriented lab boundaries |
| [scenarios/](./scenarios/) | Lifecycle-aligned operational validation scenarios |
| [modules/](./modules/) | Repository-level capability module catalog |
| [adapters/](./adapters/) | Repository-level adapter catalog |
| [shared-runtime/](./shared-runtime/) | Shared runtime and integration boundary catalog |

## Repository Support Areas

- [Tools](./tools/) - repository generation, validation, and content automation utilities
- [Builds](./builds/) - generated build and portfolio artifact index area
- [Diagrams](./diagrams/) - repository-level visualization and diagram artifact area
- [Internal](./internal/) - internal quality models, governance references, and repository control documents

## Quality Status

<!-- QUALITY_STATUS_START -->
| Quality Signal | Current Value |
|---|---|
| missing_required_artifacts | not reported |
| small_png_count | not reported |
| markdown_broken_links | 0 |
| top_level_extra_directories | not reported |
| top_level_missing_directories | not reported |
| root_readme_missing_links | | root_readme_missing_links | 0 | |
| root_readme_missing_terms | | root_readme_missing_terms | 0 | |
| repository_language_hits | not reported |
<!-- QUALITY_STATUS_END -->

## Important Boundary

This repository does not claim production deployment of every technology stack.

It validates reusable operational capability boundaries through controlled, reviewer-readable lab implementations and lifecycle-aligned scenarios.

Generated by tools/content-generator/generate_root_readme.py

## Phase 2 Runtime Completion

- [Phase 2 Runtime Completion Report](validation-reports/phase-2-runtime-completion-report.md)
