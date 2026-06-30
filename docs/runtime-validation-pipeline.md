# Runtime Validation Pipeline

This document describes the runtime validation pipeline used by the SNSD Hybrid Infrastructure portfolio.

The pipeline connects local runtime lab state with reviewer-facing scenario evidence.

## Purpose

The runtime validation pipeline proves that this repository is not only a static scenario catalog.

It validates that scenario packages are connected to executable runtime evidence, including:

- Infrastructure service health
- Monitoring target health
- HTTP and blackbox probe status
- Alerting readiness
- Backup and restore validation metrics
- Scenario-level generated evidence
- Repository structure consistency

## Pipeline Entry Point

Run from WSL at the repository root.

    tools/pipeline/run_runtime_validation_pipeline.sh

The expected final result is:

    [OK] runtime validation pipeline completed

## Pipeline Flow

The pipeline executes the following flow:

    Runtime Evidence Collection
      -> Scenario-level Evidence Generation
      -> Runtime Validation Index Generation
      -> Runtime Smoke Check
      -> Repository Static Check

## Pipeline Steps

| Step | Tool | Purpose |
|---:|---|---|
| 1 | `tools/evidence/collect_runtime_evidence.sh` | Collects local runtime service, monitoring, alerting, and recovery evidence |
| 2 | `tools/evidence/generate_lab_runtime_validation.py` | Generates scenario-level reviewer-facing runtime validation evidence |
| 3 | `tools/evidence/generate_lab_runtime_validation_index.py` | Generates the scenario evidence index |
| 4 | `tools/validation/runtime_smoke_check.sh` | Validates runtime services, APIs, probes, targets, backup metrics, and evidence count |
| 5 | `tools/validation/repository_static_check.sh` | Validates repository structure, required documents, tools, and failure playbooks |

## Runtime Smoke Check Coverage

The runtime smoke check validates:

| Area | Validation |
|---|---|
| Ansible connectivity | `ubuntu_nodes` ping |
| Core services | node_exporter, Docker, Prometheus, Grafana, Loki, Promtail, Blackbox Exporter, HAProxy, HAProxy Exporter, MariaDB, mysqld_exporter, Alertmanager |
| HTTP/API health | Prometheus, Grafana, Loki, Alertmanager, HAProxy HTTP redirect, HAProxy HTTPS frontend, HAProxy stats, and app-node health endpoints |
| Prometheus targets | All active targets are UP, including node_exporter, cAdvisor, mysqld_exporter, Blackbox, and HAProxy exporter |
| Blackbox probes | HTTPS service entrypoint probe and ICMP probe success |
| Backup and restore | `snsd_backup_last_success` and `snsd_restore_validation_success` |
| Scenario evidence | 150 scenario evidence files and no `NOT_FOUND` markers |
| Runtime index | `docs/lab-runtime-validation-index.md` exists |

## Repository Static Check Coverage

The repository static check validates:

- Scenario count
- Scenario-level runtime evidence count
- Absence of `NOT_FOUND` markers
- Required runtime validation documents
- Required evidence tools
- Required validation tools
- Required pipeline tools
- Required failure injection playbooks
- Resilience failure suite wrapper
- Local raw runtime evidence is not staged accidentally

## Evidence Outputs

### Local Raw Runtime Evidence

Generated under:

    labs/evidence/generated/

Typical files:

    runtime-service-inventory.md
    monitoring-target-status.md
    alerting-validation-summary.md
    recovery-validation-summary.md
    resilience-failure-suite-summary.md

These files represent local runtime output and are not intended to be committed by default.

### Reviewer-facing Scenario Evidence

Generated under each scenario package:

    scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md

This evidence is intended for reviewer inspection.

### Runtime Validation Index

Generated at:

    docs/lab-runtime-validation-index.md

This index summarizes all scenario-level runtime evidence files.

Expected summary:

    Total scenarios: 150
    OK: 150
    Missing evidence: 0
    Contains NOT_FOUND: 0

## Service Entrypoint Observability

The service entrypoint is monitored through two complementary paths.

| Signal | Source | Purpose |
|---|---|---|
| External HTTPS availability | Blackbox Exporter | Validates the user-facing HTTPS endpoint |
| HAProxy backend/server state | HAProxy Exporter | Validates internal HAProxy backend and server visibility |
| HAProxy stats page | HAProxy built-in stats | Provides browser-readable operational status |
| App health endpoints | app-node `18080/health` | Validates backend application health |
| Container telemetry | cAdvisor on `8080` | Keeps container observability separate from app traffic |

This separates user-facing availability from internal service entrypoint telemetry.


## Current Service Validation Endpoints

The runtime smoke check validates the current service entrypoint model.

| Component | Endpoint | Expected |
|---|---|---|
| HAProxy HTTP | `http://192.168.1.20` | 301 redirect |
| HAProxy HTTPS | `https://192.168.1.20` | 200 OK |
| HAProxy stats | `http://192.168.1.20:8404/stats` | 200 OK |
| app-node-01 health | `http://192.168.1.31:18080/health` | 200 OK |
| app-node-02 health | `http://192.168.1.32:18080/health` | 200 OK |
| cAdvisor app-node-01 | `http://192.168.1.31:8080` | Prometheus target UP |
| cAdvisor app-node-02 | `http://192.168.1.32:8080` | Prometheus target UP |
| Blackbox HTTPS | `https://192.168.1.20` | `probe_success = 1` |

## Failure Injection Relationship

Failure injection is intentionally excluded from the default bootstrap path.

Controlled failure validation is documented at:

    docs/failure-injection-scenarios.md

The resilience failure suite can be checked without injecting failures:

    tools/failure/run_resilience_failure_suite.sh --precheck-only

The full failure suite can be executed after a healthy baseline is confirmed:

    tools/failure/run_resilience_failure_suite.sh

The suite validates:

- Web backend failure and recovery
- Observability loss and recovery
- Database failure and recovery
- Proxy entrypoint failure and recovery
- Backup failure and recovery validation

After the suite completes, runtime validation evidence is refreshed through the standard pipeline.

The suite writes a local runtime summary to:

    labs/evidence/generated/resilience-failure-suite-summary.md

## Recommended Validation Order

For a full local validation session, run:

    tools/failure/run_resilience_failure_suite.sh --precheck-only
    tools/pipeline/run_runtime_validation_pipeline.sh

For full resilience validation, run:

    tools/failure/run_resilience_failure_suite.sh

Then verify:

    tools/validation/runtime_smoke_check.sh
    tools/validation/repository_static_check.sh

## Failure Handling

If validation fails, use the failure area to isolate the cause.

| Failure Area | First Check |
|---|---|
| Ansible connectivity | `ansible -i inventory/lab/hosts.ini ubuntu_nodes -m ping` |
| Prometheus target failure | Prometheus targets API or `/targets` UI |
| Blackbox failure | `http://192.168.1.40:9115/probe?target=https://192.168.1.20&module=http_2xx` |
| Backup metric failure | node_exporter metrics on `192.168.1.40:9100` |
| Scenario evidence failure | `docs/lab-runtime-validation-index.md` and generated scenario evidence |
| Static check failure | Missing required file or accidentally staged local runtime evidence |

## Boundary

This pipeline is designed for local hybrid infrastructure validation.

It does not claim production-grade chaos engineering coverage.

It demonstrates a controlled operations validation loop:

    Deploy
      -> Observe
      -> Validate
      -> Inject Failure
      -> Recover
      -> Regenerate Evidence
      -> Review
