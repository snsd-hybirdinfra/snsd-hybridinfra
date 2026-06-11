# Implementation Labs

Generated At: 2026-06-11T20:20:50.086300Z

## Purpose

This directory contains implementation-oriented lab boundaries for validating lifecycle-aligned infrastructure operations scenarios.

Labs are not isolated tutorials.

They are reusable execution boundaries that support scenario validation across observability, automation, recovery, resilience, and governance workflows.

## Lab Baseline

| Signal | Value |
|---|---:|
| Total implementation labs | 10 |
| Documentation-ready labs | 10 |
| Labs needing attention | 0 |

## Lab Index

| Lab | Scope | Focus | Status |
|---|---|---|---|
| [01-linux-observability-lab](./01-linux-observability-lab/README.md) | Observability | Linux host visibility, process health, filesystem state, service monitoring, and system events | documentation-ready |
| [02-network-routing-lab](./02-network-routing-lab/README.md) | Network | Routing, VPN, WAN, DNS, reachability, latency, packet loss, and route recovery validation | documentation-ready |
| [03-ansible-automation-lab](./03-ansible-automation-lab/README.md) | Automation | Inventory, SSH access, playbook execution, rollback, recovery, validation, and automation evidence | documentation-ready |
| [04-container-runtime-lab](./04-container-runtime-lab/README.md) | Container Runtime | Docker runtime visibility, container health, logs, restart recovery, and container evidence | documentation-ready |
| [05-kolla-openstack-lab](./05-kolla-openstack-lab/README.md) | OpenStack Preflight | Kolla-Ansible based OpenStack control plane readiness, network model, service preflight, and validation evidence | documentation-ready |
| [06-monitoring-stack-lab](./06-monitoring-stack-lab/README.md) | Monitoring | Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence | documentation-ready |
| [07-logging-correlation-lab](./07-logging-correlation-lab/README.md) | Logging & Correlation | Log collection, event normalization, correlation, timeline reconstruction, and evidence | documentation-ready |
| [08-backup-recovery-lab](./08-backup-recovery-lab/README.md) | Backup & Recovery | Backup job readiness, artifact validation, restore workflows, integrity checks, and recovery evidence | documentation-ready |
| [09-resilience-failover-lab](./09-resilience-failover-lab/README.md) | Resilience | Failure detection, failover decision, traffic shift validation, recovery validation, and resilience evidence | documentation-ready |
| [10-governance-reporting-lab](./10-governance-reporting-lab/README.md) | Governance | Repository validation, coverage reporting, quality gates, documentation consistency, and governance reporting | documentation-ready |

## Readiness Matrix

| Lab | README | Scripts | Execution Note | Runtime Boundary Assets | Status |
|---|---|---|---|---|---|
| [01-linux-observability-lab](./01-linux-observability-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [02-network-routing-lab](./02-network-routing-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [03-ansible-automation-lab](./03-ansible-automation-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [04-container-runtime-lab](./04-container-runtime-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [05-kolla-openstack-lab](./05-kolla-openstack-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [06-monitoring-stack-lab](./06-monitoring-stack-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [07-logging-correlation-lab](./07-logging-correlation-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [08-backup-recovery-lab](./08-backup-recovery-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [09-resilience-failover-lab](./09-resilience-failover-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |
| [10-governance-reporting-lab](./10-governance-reporting-lab/README.md) | PASS | PASS | PASS | PASS | documentation-ready |

## Execution Boundary Model

Each lab provides a controlled implementation boundary for one or more operational capabilities.

A lab boundary may include:

- setup scripts
- validation scripts
- cleanup scripts
- configuration examples
- compose definitions
- Ansible playbooks
- datasets
- architecture notes
- execution boundary notes

## Runtime Evidence Policy

Generated lab runtime evidence is local-only and intentionally excluded from Git.

See [Runtime Evidence Policy](../docs/runtime-evidence-policy.md) for the committed scenario evidence and local-only lab runtime evidence boundary.

Committed lab content should remain reviewer-readable and environment-neutral.

Local-only runtime content includes:

- raw command output
- generated runtime summaries
- temporary runtime workspaces
- sensitive local execution artifacts

## Related Repository Documents

- [Lab Runtime Implementation Summary](../validation-reports/lab-runtime-implementation-summary.md)
- [Lab Readiness Summary](../validation-reports/lab-readiness-summary.md)
- [Lab Coverage Matrix](../docs/lab-coverage-matrix.md)
- [Repository README](../README.md)
- [Runtime Evidence Policy](../docs/runtime-evidence-policy.md)

Generated by tools/content-generator/generate_labs_readme.py
