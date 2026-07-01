# Monitoring Stack Lab

## Lab Purpose

This lab defines the implementation boundary for:

06-monitoring-stack-lab

## Lab Focus

Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence.

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

## Upstream Dependency

- [Upstream Linux Observability Dependency](architecture/upstream-linux-observability-dependency.md)
## Monitoring Stack Execution

- [Docker Compose Definition](compose/docker-compose.yml)
- [Monitoring Stack Scripts](scripts/README.md)
- [Prometheus VMware Config Example](configs/prometheus/prometheus.vmware.example.yml)
- [Grafana Prometheus Datasource](configs/grafana/provisioning/datasources/prometheus.yml)
- [Linux Node Exporter Basic Dashboard](configs/grafana/dashboards/linux-node-exporter-basic.json)

## Phase 2 Prometheus Alert Rule Runtime

This lab includes Prometheus alert rule loading validation as a Phase 2 runtime extension.

Runtime model:

- Prometheus runtime
- Grafana runtime
- Prometheus alert rule file
- Prometheus rule API validation
- local-only generated validation evidence

### Alert Rules

The lab validates the following alert rules:

| Alert | Purpose |
|---|---|
| SNSDTargetDown | Detects unavailable monitored targets |
| SNSDHighScrapeLatency | Detects elevated scrape latency |

### Runtime Validation

Run from WSL:

    cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/labs/06-monitoring-stack-lab"
    bash scripts/run.sh

Run and clean up automatically:

    bash scripts/run.sh --cleanup

Expected result:

| Signal | Expected Status |
|---|---|
| Prometheus health endpoint | PASS |
| Grafana health endpoint | PASS |
| Prometheus rule API reachable | PASS |
| SNSDTargetDown alert rule loaded | PASS |
| SNSDHighScrapeLatency alert rule loaded | PASS |

### Runtime Evidence

Generated runtime evidence is local-only and excluded from Git.

Local evidence paths:

- evidence/generated/raw/prometheus-health.txt
- evidence/generated/raw/grafana-health.json
- evidence/generated/raw/prometheus-rules.json
- evidence/generated/summary/monitoring-stack-runtime-summary.md

## Scenario Signal Validation

This lab includes scenario-level mock monitoring signals in addition to basic Prometheus and Grafana readiness checks.

Additional validation script:

- scripts/validate-scenario-signals.sh

Scenario signal coverage:

- service availability
- API latency
- certificate expiration
- storage capacity
- database health
- message queue backlog
- scrape latency

The generated runtime evidence remains local-only under evidence/generated.
