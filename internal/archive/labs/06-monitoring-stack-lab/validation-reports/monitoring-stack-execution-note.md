# Monitoring Stack Execution Boundary Note

## Execution Mode

The Monitoring Stack Lab uses Docker Compose to run Prometheus and Grafana.

This execution mode validates the monitoring stack boundary after Linux observability targets have been prepared by the Linux Observability Lab.

## Upstream Dependency

Upstream lab:

- 01-linux-observability-lab

Required upstream state:

- Linux targets reachable
- node_exporter running on target hosts
- Metrics endpoint available on port 9100
- Two-node Linux observability target model available

## Monitoring Stack Components

| Component | Role | Port |
|---|---|---:|
| Prometheus | Metrics collection and target scraping | 9090 |
| Grafana | Dashboard visualization | 3000 |
| node_exporter | Linux host metrics source | 9100 |

## Validated Boundary

This validates:

- Docker Compose execution boundary
- Prometheus container startup
- Grafana container startup
- Prometheus health endpoint
- Grafana health endpoint
- Prometheus scrape target configuration
- Linux node exporter target visibility

This does not validate:

- Production monitoring retention
- Alertmanager integration
- Long-term dashboard governance
- Authentication hardening
- TLS-enabled monitoring access
- External persistent storage

## Evidence Policy

Generated runtime evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside the repository commit history.

## Next Execution Target

The next implementation step is to formalize Prometheus target validation and dashboard readiness checks into repeatable validation scripts.
## Runtime Validation Signals

The monitoring stack validation script records the following local-only runtime signals:

| Signal | Expected Result |
|---|---|
| Prometheus health endpoint | PASS |
| Grafana health endpoint | PASS |
| Prometheus target linux-node-01 node_exporter | PASS |
| Prometheus target linux-node-02 node_exporter | PASS |
| Grafana datasource provisioning file | PASS |
| Grafana dashboard provider file | PASS |
| Grafana dashboard JSON file | PASS |

These signals are generated under evidence/generated/ and are intentionally not committed.
