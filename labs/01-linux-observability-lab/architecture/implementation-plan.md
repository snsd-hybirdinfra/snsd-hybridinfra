# Linux Observability Lab Implementation Plan

## Lab Purpose

This lab validates Linux host visibility scenarios through system-level telemetry collection, process health checks, filesystem monitoring, service state inspection, and event visibility.

The lab is designed as the base infrastructure observability environment for lifecycle Level 1 visibility scenarios and selected Level 2 correlation scenarios.

---

## Implementation Scope

This lab focuses on:

- Linux host health visibility
- Process and service monitoring
- Filesystem capacity and availability checks
- System event collection
- Hardware and virtual machine visibility
- Basic telemetry export
- Evidence generation for scenario validation

---

## Target Environment

| Component | Purpose |
|---|---|
| Linux VM 1 | Primary monitored host |
| Linux VM 2 | Secondary monitored host |
| Management Node | Ansible control and validation runner |
| Prometheus Node Exporter | Host telemetry source |
| Prometheus | Metric collection |
| Grafana | Dashboard visibility |
| Python scripts | Lightweight validation and evidence generation |
| Ansible | Setup, validation, and cleanup automation |

---

## Lab Architecture

Management Node
- Runs Ansible playbooks
- Executes validation scripts
- Collects evidence outputs

Linux Hosts
- Expose system metrics through node exporter
- Provide process, filesystem, service, and event data

Monitoring Stack
- Prometheus scrapes Linux host telemetry
- Grafana visualizes host-level visibility signals

Evidence Layer
- Stores raw command outputs
- Stores processed validation summaries
- Stores scenario evidence mappings

---

## Lab Modules

| Module | Role |
|---|---|
| Linux Health Collection Module | Collects host health signals |
| Process Visibility Module | Validates process and service status |
| Filesystem Visibility Module | Validates filesystem usage and availability |
| System Event Visibility Module | Collects and summarizes system events |
| Evidence Generation Module | Converts validation output into reviewer-readable evidence |

---

## Lab Adapters

| Adapter | Role |
|---|---|
| Ansible Adapter | Executes setup, validation, and cleanup workflows |
| Prometheus Adapter | Collects Linux host metrics |
| Grafana Adapter | Provides dashboard visibility |
| Python Exporter Adapter | Supports lightweight custom checks |

---

## Shared Runtime

| Runtime Area | Purpose |
|---|---|
| runners/ | Executes lab validation workflows |
| validators/ | Checks telemetry and scenario evidence requirements |
| parsers/ | Converts command output and metrics into summaries |

---

## Scenario Coverage

Primary scenario groups:

- filesystem-health-visibility
- process-health-monitoring
- system-event-visibility
- hardware-health-monitoring
- virtual-machine-health-monitoring
- compute-resource-monitoring
- service-health-visibility

---

## Validation Workflow

1. Provision or prepare Linux hosts
2. Install required packages
3. Deploy node exporter
4. Configure Prometheus scrape targets
5. Validate metric availability
6. Execute process, service, filesystem, and event checks
7. Generate raw evidence
8. Generate processed summaries
9. Produce lab validation report
10. Confirm scenario coverage

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

The lab is considered ready when:

- Linux hosts are reachable
- node exporter metrics are available
- Prometheus scrape status is healthy
- Grafana dashboard is reachable
- filesystem checks produce evidence
- process checks produce evidence
- system event checks produce evidence
- lab validation report is generated
- mapped scenario coverage is documented
