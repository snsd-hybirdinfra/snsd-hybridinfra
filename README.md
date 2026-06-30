## Reviewer Quick Start

SNSD Hybrid Infrastructure is a scenario-driven hybrid infrastructure operations portfolio.

It demonstrates how infrastructure operations capabilities can be validated through lifecycle-aligned scenarios, runtime labs, observability, automation, recovery validation, and controlled failure injection.

### What is validated

- 150 lifecycle-aligned infrastructure operations scenarios
- 10 reusable runtime lab domains
- Ansible-based deployment and validation workflows
- Prometheus, Grafana, Loki, Promtail, Blackbox Exporter, Alertmanager, HAProxy, MariaDB, and backup/restore runtime checks
- Controlled failure injection for web, observability, database, proxy, and backup failure paths
- HAProxy HTTPS service entrypoint with HTTP redirect, TLS termination, stats page, and Blackbox HTTPS probing
- Scenario-level generated evidence under each scenario directory

### Recommended review path

1. `docs/architecture.md`
2. `docs/runtime-validation-pipeline.md`
3. `docs/failure-injection-scenarios.md`
4. `docs/lab-runtime-validation-index.md`
5. `ansible/README.md`
6. `scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md`

### Runtime validation commands

Run from WSL at the repository root.

    tools/pipeline/run_runtime_validation_pipeline.sh
    tools/failure/run_resilience_failure_suite.sh --precheck-only

Full failure injection suite:

    tools/failure/run_resilience_failure_suite.sh

### Evidence boundary

Local raw runtime evidence is generated under:

    labs/evidence/generated/

Reviewer-facing scenario evidence is generated under:

    scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md

Raw runtime evidence is local-only. Scenario-level generated evidence is intended for review.

﻿# SNSD Hybrid Infrastructure

SNSD Hybrid Infrastructure is a scenario-driven hybrid infrastructure operations portfolio.

It validates reusable operational capabilities across observability, correlation, automation, recovery, resilience, and governance scenarios.

## Positioning

- Repository type: Hybrid Infrastructure Operations Portfolio
- Operating model: Scenario-driven infrastructure operations
- Validation model: Lab-backed runtime evidence and scenario-level evidence
- Scope: Linux, networking, automation, containers, monitoring, logging, backup, recovery, resilience, and governance

## Operational Lifecycle

1. Detection
2. Correlation and Analysis
3. Incident Coordination
4. Recovery and Automation
5. Recovery Validation
6. Governance and Reporting

## Scenario Levels

| Level | Focus |
|---|---|
| Level 1 | Visibility |
| Level 2 | Correlation |
| Level 3 | Recovery and Automation |
| Level 4 | Distributed Resilience |
| Level 5 | Enterprise Continuity |

## Runtime Labs

| Lab | Purpose |
|---|---|
| 01-linux-observability-lab | Linux host and system visibility |
| 02-network-routing-lab | Network reachability and routing validation |
| 03-ansible-automation-lab | Automation and configuration workflow |
| 04-container-runtime-lab | Container runtime validation |
| 05-kolla-openstack-lab | OpenStack readiness and cloud control plane scope |
| 06-monitoring-stack-lab | Prometheus, Grafana, exporters, and alert signals |
| 07-logging-correlation-lab | Loki, Promtail, and log correlation flow |
| 08-backup-recovery-lab | Restic backup and restore validation |
| 09-resilience-failover-lab | HAProxy continuity and failover validation |
| 10-governance-reporting-lab | Governance and reporting evidence |

## Runtime Validation Pipeline

The repository includes a runtime validation pipeline for the local VM-based hybrid infrastructure lab.

From WSL:

```
tools/pipeline/run_runtime_validation_pipeline.sh
```

The pipeline performs:

- Runtime evidence collection
- Scenario-level validation evidence generation
- Runtime validation index generation
- Smoke check execution

Primary documents:

- docs/runtime-validation-pipeline.md
- docs/lab-runtime-validation-index.md
- docs/failure-injection-scenarios.md

## Evidence Model

| Evidence Type | Path | Commit Policy |
|---|---|---|
| Raw runtime evidence | labs/evidence/generated/ | Local runtime evidence |
| Scenario validation evidence | scenarios/<level>/<scenario>/evidence/generated/ | Reviewer-facing evidence |
| Runtime validation index | docs/lab-runtime-validation-index.md | Reviewer-facing document |

## Key Documentation

- docs/architecture.md
- docs/governance.md
- docs/portfolio-map.md
- docs/scenario-selection-criteria.md
- docs/scenario-package-standard.md
- docs/scenario-quality-checklist.md
- docs/runtime-validation-pipeline.md
- docs/lab-runtime-validation-index.md
- docs/failure-injection-scenarios.md

## Standard Workflow

Run validation from WSL:

```
cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra"
tools/pipeline/run_runtime_validation_pipeline.sh
```

Run Git from PowerShell:

```
cd "C:\Users\swfco\OneDrive\바탕 화면\github\snsd-hybridinfra"
git status --short
git add -A
git commit -m "Update runtime validation evidence"
git push
```

## Boundary

This repository is not a simple scenario collection.

It is structured as an implementation-oriented infrastructure operations portfolio, where scenarios, labs, runtime evidence, and governance documents are connected.
