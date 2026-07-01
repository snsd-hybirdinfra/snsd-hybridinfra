# Ansible Automation Lab Scenario Coverage Report

This report summarizes repository scenarios mapped to the Ansible Automation Lab.

## Lab

- Lab: 03-ansible-automation-lab
- Focus: Ansible-based setup, recovery execution, rollback workflows, validation checks, and evidence generation.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |

## Coverage Summary

Mapped scenarios: 4

## Mapped Scenarios

| Scenario | Level | Domain | Lab |
|---|---|---|---|
| [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) | 3 |
| [Compute Resource Monitoring](../scenarios/level-1-visibility/compute-resource-monitoring/) | level-1-visibility | Compute / Resource | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) |
| [Compute Resource Correlation](../scenarios/level-2-correlation/compute-resource-correlation/) | level-2-correlation | Compute / Resource | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) |
| [Compute Failover Orchestration](../scenarios/level-3-recovery/compute-failover-orchestration/) | level-3-recovery | Compute / Resource | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) |

## Validation Interpretation

This lab validates automation-oriented recovery and rollback scenarios by preparing Ansible control workflows, validating inventory and SSH access, executing planned playbook workflows, checking post-execution state, and generating evidence outputs for mapped scenarios.

## Evidence Relationship

Expected evidence is produced under:

- evidence/raw/
- evidence/processed/
- evidence/summary/
- validation-reports/lab-validation-report.md
