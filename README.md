## Reviewer Quick Start

## Evaluator Summary

SNSD Hybrid Infrastructure is a scenario-driven hybrid infrastructure operations portfolio.

It demonstrates how a shared lab runtime can support observability, alerting, incident coordination, backup and restore validation, and controlled recovery scenarios.

This repository is not just a collection of scenario documents. It connects lifecycle-aligned scenario packages with executable Ansible playbooks, runtime validation scripts, and generated evidence.

## Evaluator Quick Path

| Order | Document | Purpose |
|---:|---|---|
| 1 | `docs/architecture.md` | Runtime architecture and operational control points |
| 2 | `docs/runtime-validation-pipeline.md` | Evidence generation and validation flow |
| 3 | `docs/failure-injection-scenarios.md` | Controlled failure injection and recovery scenarios |
| 4 | `docs/lab-runtime-validation-index.md` | Scenario-level runtime evidence coverage |
| 5 | `ansible/README.md` | Playbook order and execution boundary |

## Implemented Runtime Capabilities

| Area | Implementation |
|---|---|
| Service entrypoint | HAProxy HTTPS, HTTP redirect, stats page |
| External availability | Blackbox HTTPS probe |
| Proxy observability | HAProxy Exporter |
| Node observability | node_exporter |
| Container observability | cAdvisor |
| Database observability | mysqld_exporter |
| Alerting | Prometheus rules and Alertmanager |
| Incident coordination | Alertmanager webhook receiver |
| Backup and restore | Restic backup and restore validation |
| Failure injection | Web, observability, database, proxy, and backup recovery scenarios |

## Execution Boundary

Normal operating baseline:

    ansible/playbooks/01-*.yml through ansible/playbooks/15-*.yml

Controlled failure injection:

    ansible/playbooks/21-*.yml through ansible/playbooks/25-*.yml

Bootstrap:

    tools/bootstrap/run_ansible_lab_bootstrap.sh

Failure suite:

    tools/failure/run_resilience_failure_suite.sh

Runtime validation pipeline:

    tools/pipeline/run_runtime_validation_pipeline.sh

## Scenario Catalog Boundary

The `scenarios/` directory contains lifecycle-aligned scenario packages.

The 150 scenarios are not 150 separate infrastructure deployments. They are a reviewer-readable operational scenario catalog connected to shared lab runtime evidence.

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
