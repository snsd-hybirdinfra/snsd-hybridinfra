# Prometheus Target Model

## Purpose

This document defines how the Monitoring Stack Lab consumes Linux observability targets prepared by the Linux Observability Lab.

## Upstream Source

Source lab:

- 01-linux-observability-lab

Prepared targets:

| Target | Exporter | Port |
|---|---|---:|
| linux-node-01 | node_exporter | 9100 |
| linux-node-02 | node_exporter | 9100 |

## Monitoring Responsibility

The Monitoring Stack Lab is responsible for validating:

- Prometheus scrape configuration
- Target availability
- Exporter endpoint health
- Metrics ingestion readiness
- Dashboard readiness
- Alert readiness

## Boundary

This lab does not own Linux host preparation.

Linux host preparation belongs to the Linux Observability Lab.

This lab owns telemetry collection and visualization readiness.