# Linux Observability Monitoring Handoff Note

## Purpose

This note defines the handoff boundary between the Linux Observability Lab and the Monitoring Stack Lab.

The Linux Observability Lab validates Linux target readiness, Ansible execution, and host-level observability preparation.

The Monitoring Stack Lab consumes those prepared Linux targets as scrape and dashboard candidates.

## Handoff Source

Source lab:

- 01-linux-observability-lab

Validated source capabilities:

- Linux target reachability
- SSH key-based Ansible execution
- Become privilege readiness
- Two-node inventory execution
- Basic system validation workflow
- Local-only evidence parsing

## Handoff Target

Target lab:

- 06-monitoring-stack-lab

Expected downstream capabilities:

- Prometheus scrape configuration
- Node exporter target validation
- Grafana dashboard readiness
- Alert readiness validation
- Monitoring evidence generation

## Handoff Boundary

This handoff does not mean the Monitoring Stack Lab is fully implemented.

It means the Linux target layer is ready to be consumed by a monitoring stack implementation.

## Expected Target Model

| Target | Role |
|---|---|
| linux-node-01 | Linux observability target |
| linux-node-02 | Linux observability target |
| monitoring-node | Future Prometheus and Grafana host |

## Next Implementation Step

The next implementation step is to add node exporter installation and validation to the Linux Observability Lab, then consume those endpoints from the Monitoring Stack Lab.