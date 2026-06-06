# Operational Adapters

This directory contains adapter components used to connect operational scenarios and platform modules with external infrastructure, observability, automation, and reporting systems.

Adapters are not scenario logic. They represent integration boundaries that allow reusable operational modules to interact with telemetry sources, automation engines, dashboards, and runtime platforms.

---

## Adapter Design Principles

- Adapters provide external system integration boundaries.
- Adapters should remain reusable across multiple scenarios.
- Adapters should avoid embedding scenario-specific workflow logic.
- Adapters support telemetry ingestion, automation execution, dashboard integration, or evidence retrieval.
- Operational modules consume adapter capabilities through platform workflows.

---

## Adapter Inventory

Total adapters: 6

| Adapter | Integration Role |
|---|---|
| [Ansible Adapter](./ansible-adapter/README.md) | Provides automation execution integration for recovery, remediation, and operational workflow execution. |
| [Grafana Adapter](./grafana-adapter/README.md) | Provides dashboard visualization and operational reporting integration for scenario evidence and infrastructure visibility. |
| [Kubernetes Adapter](./kubernetes-adapter/README.md) | Provides Kubernetes cluster integration for container platform telemetry, service state, and recovery workflow coordination. |
| [Opensearch Adapter](./opensearch-adapter/README.md) | Provides log, event, and operational evidence indexing integration for analysis, correlation, and reporting workflows. |
| [Prometheus Adapter](./prometheus-adapter/README.md) | Provides metric collection and telemetry integration for infrastructure visibility, alerting, and operational signal workflows. |
| [Python Exporter Adapter](./python-exporter-adapter/README.md) | Provides custom telemetry export and integration logic for scenario-specific infrastructure signals. |

---

## Integration Role

Adapters support operational workflows by connecting platform capabilities to:

- metric collection systems
- log and event platforms
- dashboard and visualization tools
- automation execution engines
- Kubernetes and container platforms
- validation and evidence sources

---

## Summary

The adapter layer keeps external integration concerns separate from reusable operational modules and scenario orchestration logic.
