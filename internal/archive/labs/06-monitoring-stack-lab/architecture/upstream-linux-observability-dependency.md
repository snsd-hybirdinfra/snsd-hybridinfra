# Upstream Linux Observability Dependency

## Purpose

This document defines the dependency from the Monitoring Stack Lab to the Linux Observability Lab.

The Monitoring Stack Lab should not begin from abstract monitoring configuration alone. It should consume validated Linux targets from the Linux Observability Lab.

## Upstream Lab

- 01-linux-observability-lab

## Required Upstream Conditions

| Condition | Required State |
|---|---|
| Linux target inventory | available |
| SSH access | validated |
| Become privilege | validated |
| Multi-node execution | validated |
| Local execution evidence parser | available |
| Monitoring handoff note | available |

## Downstream Responsibility

The Monitoring Stack Lab is responsible for:

- Prometheus installation boundary
- Grafana installation boundary
- Node exporter scrape configuration
- Target health validation
- Dashboard readiness validation
- Monitoring evidence generation

## Boundary Statement

The Linux Observability Lab prepares the monitored targets.

The Monitoring Stack Lab validates the telemetry collection and visualization layer.