# OpenStack Private Cloud Lab Host Requirements

## Purpose

This document defines host requirements for the OpenStack Private Cloud Lab.

The requirements are intended for portfolio validation, operational workflow testing, monitoring integration, automation testing, and evidence generation.

This lab is not sized as a production OpenStack deployment.

## Deployment Profiles

| Profile | Use Case |
|---|---|
| Minimal | API and basic OpenStack workflow validation |
| Recommended | Stable single-node private cloud lab with observability |
| Expanded | Multi-node or heavier operational testing |

## Minimal Profile

The minimal profile is suitable for basic OpenStack API testing, instance lifecycle validation, and documentation-level workflow verification.

| Resource | Requirement |
|---|---|
| CPU | 4 cores with virtualization support |
| Memory | 16 GB RAM |
| Disk | 100 GB available storage |
| Network | 1 NIC |
| OS | Ubuntu Server LTS or compatible Linux distribution |
| Use Case | DevStack or lightweight single-node testing |

## Recommended Profile

The recommended profile is suitable for Kolla-Ansible based lab deployment, OpenStack service validation, monitoring, dashboards, and automation testing.

| Resource | Requirement |
|---|---|
| CPU | 8 cores or more with virtualization support |
| Memory | 32 GB RAM or more |
| Disk | 200 GB or more SSD-backed storage |
| Network | 1 to 2 NICs |
| OS | Ubuntu Server LTS or compatible Linux distribution |
| Use Case | Single-node OpenStack lab with observability and automation |

## Expanded Profile

The expanded profile is suitable for multi-node testing, compute separation, network path validation, and resilience-oriented workflows.

| Resource | Requirement |
|---|---|
| CPU | 12 cores or more across nodes |
| Memory | 64 GB RAM or more across nodes |
| Disk | 500 GB or more SSD-backed storage |
| Network | 2 NICs or more per host preferred |
| OS | Ubuntu Server LTS or compatible Linux distribution |
| Use Case | Multi-node OpenStack lab, resilience validation, and failover-oriented testing |

## CPU Requirements

The host should support hardware virtualization.

Check virtualization support on Linux:

- Intel: vmx flag
- AMD: svm flag

Example validation command:

- lscpu
- grep -E 'vmx|svm' /proc/cpuinfo

## Memory Guidance

OpenStack services, containers, databases, message queues, monitoring tools, and test instances all consume memory.

Memory pressure can cause misleading operational failures. For stable portfolio validation, 32 GB RAM is strongly preferred.

## Disk Guidance

SSD-backed storage is strongly recommended.

Disk should support:

- OpenStack service containers
- VM images
- instance disks
- logs
- Prometheus time-series data
- OpenSearch data if enabled
- generated evidence artifacts

For early testing, keep OpenSearch optional if disk or memory is limited.

## Network Guidance

A single NIC can be used for a simple lab, but a two-NIC design is cleaner.

| Network Role | Purpose |
|---|---|
| Management Network | Host access, OpenStack APIs, internal services |
| Provider or External Network | Floating IP, router external access, test workload reachability |

If only one NIC is available, VLANs or Linux bridges can be used, but this increases configuration complexity.

## Recommended Network Plan

| Network | Example CIDR | Purpose |
|---|---|
| Management | 192.168.56.0/24 | Host, OpenStack APIs, SSH, monitoring access |
| Provider / External | 192.168.100.0/24 | Floating IP and test workload access |
| Tenant Network | 10.10.0.0/24 | Internal VM network |
| Storage / Optional | 192.168.57.0/24 | Future storage or backend traffic |

These CIDRs are examples and should be adjusted to avoid conflict with the local environment.

## Base OS Requirements

The host should have:

- static IP address
- working DNS resolution
- working package repository access
- synchronized time
- SSH access
- sudo-capable administrative user
- Python available
- Git installed
- enough disk space under the selected deployment directory

## Recommended Base Packages

- git
- curl
- wget
- vim
- python3
- python3-pip
- python3-venv
- net-tools
- iproute2
- bridge-utils
- tcpdump
- jq
- chrony or systemd-timesyncd

## Firewall and Security Notes

For a lab environment, firewall rules may need to be adjusted depending on the deployment method.

Do not blindly disable host security controls in a shared or exposed network.

If firewall changes are required, document:

- what was changed
- why it was changed
- which OpenStack or monitoring service required it
- how access is restricted

## Virtualization Options

The lab can run on:

- bare metal host
- nested virtualization environment
- local hypervisor such as VMware Workstation, VirtualBox, Hyper-V, or Proxmox

Nested virtualization may work but can introduce performance and networking issues.

## Tooling Requirements

The host should support the following tooling:

- Git
- Python virtual environments
- Ansible
- Docker or container runtime required by the deployment method
- OpenStack CLI
- Prometheus and exporters
- Grafana
- OpenSearch if log visibility is enabled

## Risk and Constraint Notes

| Risk | Impact | Mitigation |
|---|---|---|
| Low memory | OpenStack services fail or become unstable | Start with minimal services or increase RAM |
| Weak disk performance | Slow image, instance, and database operations | Use SSD-backed storage |
| Network conflict | Floating IP or external network fails | Pre-plan CIDRs and avoid overlap |
| No virtualization support | Instance boot may fail | Enable virtualization in BIOS or use another host |
| Too many tools at once | Lab becomes hard to troubleshoot | Add observability and logs after OpenStack baseline is stable |

## Readiness Checklist

- CPU virtualization support confirmed
- Static IP configured
- DNS working
- Time sync working
- Git installed
- Python installed
- Ansible available or installable
- Sufficient RAM confirmed
- Sufficient disk confirmed
- Network CIDRs planned
- Deployment method selected
- Rollback or rebuild approach documented

## Recommended Starting Point

Start with the Recommended Profile when possible:

- 8 CPU cores
- 32 GB RAM
- 200 GB SSD
- Ubuntu Server LTS
- 1 or 2 NICs
- Kolla-Ansible deployment path
- Prometheus and Grafana after OpenStack baseline
- OpenSearch added only after the core lab is stable

## Validation Boundary

These requirements are for a lab-grade private cloud environment used to validate operational workflows.

They should not be treated as production OpenStack sizing guidance.
