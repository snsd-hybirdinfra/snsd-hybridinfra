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
| [Ansible Adapter](./ansible-adapter/README.md) | This adapter is a repository-level integration boundary definition. |
| [Grafana Adapter](./grafana-adapter/README.md) | This adapter is a repository-level integration boundary definition. |
| [Kubernetes Adapter](./kubernetes-adapter/README.md) | This adapter is a repository-level integration boundary definition. |
| [Opensearch Adapter](./opensearch-adapter/README.md) | This adapter is a repository-level integration boundary definition. |
| [Prometheus Adapter](./prometheus-adapter/README.md) | This adapter is a repository-level integration boundary definition. |
| [Python Exporter Adapter](./python-exporter-adapter/README.md) | This adapter is a repository-level integration boundary definition. |

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
