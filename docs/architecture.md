# SNSD Hybrid Infrastructure Architecture

SNSD Hybrid Infrastructure is a scenario-driven hybrid infrastructure operations portfolio.

The repository connects infrastructure operations scenarios, reusable runtime labs, automation workflows, observability, recovery validation, and controlled failure injection into a reviewer-readable portfolio structure.

## Architecture Positioning

This repository is not a simple scenario collection.

It is organized as an operations capability validation platform where scenario packages are mapped to runtime lab domains and validated through executable tooling.

## Core Architecture Layers

| Layer | Role |
|---|---|
| Scenario Layer | Defines lifecycle-aligned infrastructure operations scenarios |
| Runtime Lab Layer | Provides reusable local runtime validation domains |
| Automation Layer | Uses Ansible and scripts to deploy, validate, and recover lab components |
| Observability Layer | Uses Prometheus, Grafana, Loki, Promtail, Blackbox Exporter, and Alertmanager |
| Recovery Layer | Validates backup, restore, service recovery, and failure response paths |
| Evidence Layer | Generates reviewer-facing scenario-level runtime validation evidence |

## Operational Lifecycle

The portfolio follows the operational lifecycle below.

1. Detection
2. Correlation and Analysis
3. Incident Coordination
4. Recovery and Automation
5. Recovery Validation
6. Governance and Reporting

## Runtime Lab Domains

| Lab | Purpose |
|---|---|
| 01 Linux Observability Lab | Base host metrics and operating system visibility |
| 02 Network Routing Lab | Network path, reachability, and proxy validation |
| 03 Ansible Automation Lab | Configuration and recovery automation |
| 04 Container Runtime Lab | Containerized service runtime validation |
| 05 Kolla OpenStack Lab | Cloud infrastructure deployment domain |
| 06 Monitoring Stack Lab | Metrics, dashboards, probes, and alerting |
| 07 Logging Correlation Lab | Log collection and correlation workflow |
| 08 Backup Recovery Lab | Backup, restore, and recovery validation |
| 09 Resilience Failover Lab | Failure injection and recovery behavior |
| 10 Governance Reporting Lab | Evidence, index, and reviewer-facing reporting |

## Service Entrypoint Layer

The service entrypoint is implemented with HAProxy.

HAProxy provides:

- HTTP to HTTPS redirection on port 80
- TLS termination on port 443
- Round-robin backend routing to application nodes
- Layer 7 health checks against `/health`
- HAProxy statistics on port 8404
- External availability validation through Blackbox HTTPS probing
- Backend and server visibility through HAProxy Exporter

Current service path:

    Client
      -> HAProxy HTTP 80
      -> HTTPS redirect
      -> HAProxy HTTPS 443
      -> app-node-01/app-node-02:18080

Container telemetry remains separated from application traffic:

    cAdvisor
      -> app-node-01/app-node-02:8080

This separation avoids port collision between application runtime traffic and container observability.

### Service Entrypoint Observability Model

The HAProxy service entrypoint is validated from both outside and inside.

| Perspective | Tool | Validation |
|---|---|---|
| External user perspective | Blackbox Exporter | HTTPS endpoint availability |
| Proxy internal perspective | HAProxy Exporter | HAProxy backend and server metrics |
| Operator perspective | HAProxy stats page | Browser-readable HAProxy status |
| Backend perspective | App `/health` endpoint | Application node health |
| Container perspective | cAdvisor | Container runtime telemetry |

This model prevents the service entrypoint from being treated as a simple reverse proxy and instead positions it as an observable operational control point.

## Incident Coordination Layer

The architecture includes a local Alertmanager webhook receiver mock to validate alert delivery.

This layer connects detection and alerting to incident coordination evidence.

    Prometheus
      -> Alertmanager
      -> SNSD Alert Webhook Receiver
      -> /var/log/snsd-alert-webhook/alerts.jsonl
      -> Runtime Evidence

The webhook receiver is intentionally simple. Its purpose is not to replace an incident management platform, but to prove that alert payloads can leave Alertmanager and become auditable evidence.

## Runtime Validation and Failure Injection Layer

The architecture includes a dedicated runtime validation layer that connects scenario documentation with executable lab evidence.

This layer proves that the repository is not only a static scenario catalog, but an executable operations validation portfolio.

### Validation Flow

    Scenario Definition
      -> Runtime Lab Mapping
      -> Ansible Deployment
      -> Observability and Service Health Checks
      -> Failure Injection
      -> Recovery Validation
      -> Scenario-level Evidence Generation

### Runtime Validation Components

| Component | Role |
|---|---|
| `tools/pipeline/run_runtime_validation_pipeline.sh` | Runs the end-to-end runtime evidence refresh pipeline |
| `tools/validation/runtime_smoke_check.sh` | Validates service health, monitoring targets, probes, backup metrics, and scenario evidence |
| `tools/validation/repository_static_check.sh` | Validates repository structure, required documents, generated evidence, and failure playbook presence |
| `tools/failure/run_resilience_failure_suite.sh` | Executes controlled failure injection scenarios as a resilience validation suite |
| `tools/evidence/generate_lab_runtime_validation.py` | Generates scenario-level reviewer-facing runtime evidence |

### Failure Injection Position

Failure injection is placed after the runtime lab reaches a healthy baseline.

The failure injection layer validates:

- Detection behavior
- Monitoring target state changes
- Alerting paths
- Recovery execution
- Recovery validation evidence

Current controlled failure domains:

| Domain | Failure Path |
|---|---|
| Web backend | Application backend container failure and recovery |
| Observability | `node_exporter` loss and recovery |
| Database | MariaDB service failure and recovery |
| Proxy entrypoint | HAProxy service failure and recovery |
| Backup validation | Restic backup failure and recovery-validation success |

### Evidence Boundary

Raw runtime evidence is generated locally under:

    labs/evidence/generated/

Reviewer-facing scenario evidence is generated under:

    scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md

This separation keeps local runtime output out of the Git history while preserving reviewer-readable evidence inside each scenario package.

