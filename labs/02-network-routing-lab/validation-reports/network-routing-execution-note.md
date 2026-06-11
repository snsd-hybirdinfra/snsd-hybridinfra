# Network Routing Execution Boundary Note

## Execution Mode

The Network Routing Lab validates local network path behavior from the execution host toward Linux infrastructure targets.

This lab focuses on reachability, route visibility, latency measurement, DNS resolution, and service path validation.

## Upstream Context

This lab uses target nodes prepared through:

- 01-linux-observability-lab

It validates network paths toward node exporter endpoints already used by:

- 06-monitoring-stack-lab

## Network Validation Boundary

This lab validates:

- Local route table availability
- DNS resolution
- ICMP reachability
- Average latency measurement
- Service port reachability
- node_exporter metrics path validation
- Local runtime summary generation

This lab does not validate:

- Enterprise WAN routing
- BGP convergence
- VPN tunnel lifecycle
- Firewall policy governance
- Multi-region routing
- Production packet capture retention

## Evidence Policy

Generated runtime evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside repository commit history.

## Runtime Summary

Local runtime execution produces:

- evidence/generated/summary/network-routing-execution-summary.md

This summary is consumed by the local repository executive summary generator when present.