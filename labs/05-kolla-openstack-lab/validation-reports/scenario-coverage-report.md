# Kolla OpenStack Lab Scenario Coverage Report

This report summarizes repository scenarios mapped to the Kolla OpenStack Lab.

## Lab

- Lab: 05-kolla-openstack-lab
- Focus: Kolla-Ansible based OpenStack control plane validation, compute visibility, network validation, service recovery boundaries, and OpenStack evidence generation.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |

## Coverage Summary

Mapped scenarios: 7

## Mapped Scenarios

| Scenario | Level | Domain | Lab |
|---|---|---|---|
| [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) | 6 |
| [Cloud Instance Health Monitoring](../scenarios/level-1-visibility/cloud-instance-health-monitoring/) | level-1-visibility | Cloud Instance | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Cluster Resource Instability Analysis](../scenarios/level-2-correlation/cluster-resource-instability-analysis/) | level-2-correlation | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Cloud Instance Recovery Automation](../scenarios/level-3-recovery/cloud-instance-recovery-automation/) | level-3-recovery | Cloud Instance | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Cluster Node Recovery Orchestration](../scenarios/level-3-recovery/cluster-node-recovery-orchestration/) | level-3-recovery | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Multi Cluster Failover](../scenarios/level-4-resilience/multi-cluster-failover/) | level-4-resilience | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Multi Cluster Failover Coordination](../scenarios/level-4-resilience/multi-cluster-failover-coordination/) | level-4-resilience | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |

## Validation Interpretation

This lab validates private cloud infrastructure operations scenarios by preparing Kolla-Ansible deployment boundaries, OpenStack service validation, API endpoint checks, compute and network visibility, service recovery workflow boundaries, and evidence outputs for mapped scenarios.

## Evidence Relationship

Expected evidence is produced under:

- evidence/raw/
- evidence/processed/
- evidence/summary/
- validation-reports/lab-validation-report.md
