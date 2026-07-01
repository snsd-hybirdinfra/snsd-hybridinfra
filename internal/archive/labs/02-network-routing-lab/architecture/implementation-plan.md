# Network Routing Lab Implementation Plan

## Lab Purpose

This lab validates network routing, VPN visibility, WAN path monitoring, DNS reachability, load-balancer visibility, and route recovery scenarios.

The lab is designed as the routing and network-path validation environment for lifecycle Level 1 visibility, Level 2 correlation, and selected Level 3 recovery scenarios.

---

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |

---

## Implementation Scope

This lab focuses on:

- Linux routing visibility
- Static route and dynamic route validation
- VPN tunnel state inspection
- WAN link monitoring
- DNS resolution checks
- Load-balancer health visibility
- Packet loss and latency correlation
- Route recovery validation

---

## Target Environment

| Component | Purpose |
|---|---|
| Router Node 1 | Primary routing node |
| Router Node 2 | Secondary routing node |
| Client Node | Traffic generation and reachability validation |
| Server Node | Destination service endpoint |
| Management Node | Ansible control and validation runner |
| FRR or Linux routing stack | Routing protocol and route table validation |
| Prometheus | Network and host telemetry collection |
| Grafana | Network visibility dashboard |
| Python scripts | Route, reachability, DNS, and latency validation |

---

## Lab Architecture

Management Node
- Runs Ansible playbooks
- Executes routing validation scripts
- Collects evidence outputs

Routing Nodes
- Provide routing table, interface, VPN, and path state
- Support static route or FRR-based dynamic routing validation

Client and Server Nodes
- Generate reachability, latency, and path validation signals
- Provide endpoint evidence for traffic path checks

Monitoring Stack
- Collects node and network telemetry
- Provides dashboard-level visibility

Evidence Layer
- Stores command output
- Stores route validation summaries
- Stores scenario evidence mappings

---

## Lab Modules

| Module | Role |
|---|---|
| Network Path Visibility Module | Validates reachability and path state |
| Routing State Collection Module | Collects route table and next-hop data |
| VPN Visibility Module | Validates VPN tunnel status and tunnel health |
| DNS Resolution Validation Module | Validates DNS resolution and name service behavior |
| Network Evidence Generation Module | Converts routing and reachability checks into evidence |

---

## Lab Adapters

| Adapter | Role |
|---|---|
| Ansible Network Adapter | Executes routing setup and validation tasks |
| Linux Routing Adapter | Reads route table, interface, and path state |
| FRR Adapter | Supports dynamic routing validation when FRR is used |
| Prometheus Network Adapter | Collects network telemetry |
| Python Network Check Adapter | Runs reachability, latency, DNS, and path checks |

---

## Shared Runtime

| Runtime Area | Purpose |
|---|---|
| runners/ | Executes routing validation workflows |
| validators/ | Checks route, reachability, DNS, VPN, and latency conditions |
| parsers/ | Converts ip route, ping, traceroute, dig, and telemetry outputs into summaries |

---

## Scenario Coverage

Primary scenario groups:

- network-path-visibility
- endpoint-reachability-monitoring
- dns-resolution-monitoring
- load-balancer-health-monitoring
- wan-link-monitoring
- bgp-neighbor-visibility
- vpn-connectivity-monitoring
- vpn-tunnel-health-monitoring
- routing-instability-correlation
- network-packet-loss-correlation
- network-route-recovery-orchestration
- inter-region-routing-recovery

---

## Validation Workflow

1. Prepare routing nodes
2. Validate interface and IP configuration
3. Validate route table state
4. Validate endpoint reachability
5. Validate DNS resolution
6. Validate VPN or tunnel status when configured
7. Validate latency and packet loss signals
8. Validate route failure or recovery behavior
9. Generate raw evidence
10. Generate processed summaries
11. Produce lab validation report
12. Confirm scenario coverage

---

## Evidence Outputs

Expected evidence paths:

- evidence/raw/
- evidence/processed/
- evidence/summary/
- validation-reports/lab-validation-report.md
- validation-reports/scenario-coverage-report.md

---

## Completion Criteria

The lab is considered documentation-ready when:

- Lab architecture is documented
- Network modules are defined
- Network adapters are defined
- Shared runtime areas are documented
- Scenario coverage is mapped
- Lab validation report exists

The lab becomes implementation-ready when:

- Routing nodes are configured
- Route validation scripts exist
- Ansible setup and validation playbooks exist
- Reachability evidence is generated
- DNS evidence is generated
- Routing failure and recovery evidence is generated
