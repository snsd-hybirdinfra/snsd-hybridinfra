# Operational Adapters

This directory contains repository-level integration boundaries for connecting scenarios and modules with external systems.

## Purpose

Adapters keep operational logic separate from external integration concerns such as telemetry collection, automation execution, dashboards, and evidence retrieval.

## Inventory

- [ansible-adapter](ansible-adapter/)
- [grafana-adapter](grafana-adapter/)
- [kubernetes-adapter](kubernetes-adapter/)
- [opensearch-adapter](opensearch-adapter/)
- [prometheus-adapter](prometheus-adapter/)
- [python-exporter-adapter](python-exporter-adapter/)

## Role in the repository

Adapters help the platform interact with observability, automation, and runtime systems without embedding that logic into scenarios themselves.
