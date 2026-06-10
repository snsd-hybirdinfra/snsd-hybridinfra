# Linux Observability Lab Scenario Coverage Report

This report summarizes repository scenarios mapped to the Linux Observability Lab.

## Lab

- Lab: 01-linux-observability-lab
- Focus: Linux host visibility, process health, filesystem state, system events, and host-level telemetry.

## Coverage Summary

Mapped scenarios: 9

## Mapped Scenarios

| Scenario | Level | Domain | Lab |
|---|---|---|---|
| [01-linux-observability-lab](../labs/01-linux-observability-lab/) | 8 |
| [Filesystem Health Visibility](../scenarios/level-1-visibility/filesystem-health-visibility/) | level-1-visibility | Filesystem | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Hardware Health Monitoring](../scenarios/level-1-visibility/hardware-health-monitoring/) | level-1-visibility | Hardware | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Hypervisor Resource Monitoring](../scenarios/level-1-visibility/hypervisor-resource-monitoring/) | level-1-visibility | Virtualization | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Process Health Monitoring](../scenarios/level-1-visibility/process-health-monitoring/) | level-1-visibility | Process / Service | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [System Event Visibility](../scenarios/level-1-visibility/system-event-visibility/) | level-1-visibility | System Event | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Virtual Machine Health Monitoring](../scenarios/level-1-visibility/virtual-machine-health-monitoring/) | level-1-visibility | Virtual Machine | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Filesystem Failure Correlation](../scenarios/level-2-correlation/filesystem-failure-correlation/) | level-2-correlation | Filesystem | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Virtual Machine Restoration](../scenarios/level-3-recovery/virtual-machine-restoration/) | level-3-recovery | Virtual Machine | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |

## Validation Interpretation

This lab validates Linux-oriented visibility scenarios by preparing Linux hosts, collecting host telemetry, validating process and filesystem state, and generating evidence outputs for mapped scenarios.

## Evidence Relationship

Expected evidence is produced under:

- evidence/raw/
- evidence/processed/
- evidence/summary/
- validation-reports/lab-validation-report.md
