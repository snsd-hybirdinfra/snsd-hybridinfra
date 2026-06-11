# Linux Observability Lab Execution Structure

## Purpose

This document defines the executable structure for the Linux Observability Lab.

The lab moves from documentation-ready boundaries into implementation-ready execution layout.

---

## Execution Scope

This lab execution structure covers:

- Ansible inventory
- Linux host validation playbooks
- Node exporter configuration boundary
- Prometheus scrape configuration boundary
- Grafana dashboard configuration boundary
- Validation scripts
- Runtime workspace
- Generated evidence outputs

---

## Directory Model

| Path | Purpose |
|---|---|
| inventory/ | Ansible inventory and host grouping |
| inventory/group_vars/ | Group-level variables |
| inventory/host_vars/ | Host-level variables |
| playbooks/ | Ansible playbooks |
| playbooks/tasks/ | Reusable task files |
| playbooks/handlers/ | Handler definitions |
| configs/ | Lab configuration files |
| configs/prometheus/ | Prometheus scrape configuration boundary |
| configs/grafana/ | Grafana dashboard configuration boundary |
| configs/node-exporter/ | Node exporter configuration boundary |
| scripts/lib/ | Reusable shell helper functions |
| runtime-workspace/ | Local runtime working area, ignored from Git |
| evidence/generated/ | Generated execution evidence boundary |

---

## Execution Boundary

The execution structure prepares the lab for implementation.

Runtime results should be written under:

- runtime-workspace/
- evidence/generated/

Only reviewer-safe summaries should be promoted into stable evidence or validation reports.

---

## Implementation Status

| Area | Status |
|---|---|
| Execution Structure | prepared |
| Inventory | planned |
| Playbooks | planned |
| Configs | planned |
| Runtime Execution | not yet executed |
| Generated Evidence | not yet produced |
