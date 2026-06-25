# Scenario Test Evidence Index

This document indexes scenario-level test evidence and mapped lab relationships across the SNSD Hybrid Infrastructure repository.

The index is generated from each scenario evidence file under:

scenarios/<level>/<scenario>/evidence/generated/scenario-test-evidence.md

Lab-based study validation files are checked under:

scenarios/<level>/<scenario>/evidence/generated/lab-based-study-validation.md

## Summary

| Metric | Value |
|---|---|
| Total scenarios | 150 |
| Scenarios with lab-based study evidence | 150 |
| Labs referenced | 10 |

## Scenario Count by Level

| Level | Scenario Count |
|---|---:|
| Level 1 Visibility | 45 |
| Level 2 Correlation | 41 |
| Level 3 Recovery | 33 |
| Level 4 Resilience | 21 |
| Level 5 Continuity | 10 |

## Scenario Count by Mapped Lab

| Mapped Lab | Scenario Count |
|---|---:|
| 01-linux-observability-lab | 7 |
| 02-network-routing-lab | 28 |
| 03-ansible-automation-lab | 10 |
| 04-container-runtime-lab | 12 |
| 05-kolla-openstack-lab | 10 |
| 06-monitoring-stack-lab | 12 |
| 07-logging-correlation-lab | 25 |
| 08-backup-recovery-lab | 13 |
| 09-resilience-failover-lab | 23 |
| 10-governance-reporting-lab | 10 |

## Evidence Status Summary

| Status | Count |
|---|---:|
| STUDY_VALIDATED | 150 |

## Level 1 Visibility

| Scenario | Mapped Lab | Study Evidence | Status | Evidence Path |
|---|---|---|---|---|
| api-gateway-health-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/api-gateway-health-monitoring/evidence/generated/scenario-test-evidence.md |
| application-runtime-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/application-runtime-monitoring/evidence/generated/scenario-test-evidence.md |
| audit-log-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/audit-log-monitoring/evidence/generated/scenario-test-evidence.md |
| backup-job-monitoring | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/backup-job-monitoring/evidence/generated/scenario-test-evidence.md |
| bgp-neighbor-visibility | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/bgp-neighbor-visibility/evidence/generated/scenario-test-evidence.md |
| certificate-expiration-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/certificate-expiration-monitoring/evidence/generated/scenario-test-evidence.md |
| cloud-instance-health-monitoring | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/cloud-instance-health-monitoring/evidence/generated/scenario-test-evidence.md |
| compute-resource-monitoring | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/compute-resource-monitoring/evidence/generated/scenario-test-evidence.md |
| configuration-drift-monitoring | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/configuration-drift-monitoring/evidence/generated/scenario-test-evidence.md |
| container-runtime-visibility | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/container-runtime-visibility/evidence/generated/scenario-test-evidence.md |
| control-plane-health-monitoring | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/control-plane-health-monitoring/evidence/generated/scenario-test-evidence.md |
| database-health-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/database-health-monitoring/evidence/generated/scenario-test-evidence.md |
| database-replication-visibility | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/database-replication-visibility/evidence/generated/scenario-test-evidence.md |
| database-runtime-visibility | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/database-runtime-visibility/evidence/generated/scenario-test-evidence.md |
| dns-resolution-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/dns-resolution-monitoring/evidence/generated/scenario-test-evidence.md |
| endpoint-reachability-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/endpoint-reachability-monitoring/evidence/generated/scenario-test-evidence.md |
| endpoint-security-visibility | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/endpoint-security-visibility/evidence/generated/scenario-test-evidence.md |
| filesystem-health-visibility | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/filesystem-health-visibility/evidence/generated/scenario-test-evidence.md |
| hardware-health-monitoring | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/hardware-health-monitoring/evidence/generated/scenario-test-evidence.md |
| hypervisor-resource-monitoring | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/hypervisor-resource-monitoring/evidence/generated/scenario-test-evidence.md |
| identity-access-visibility | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/identity-access-visibility/evidence/generated/scenario-test-evidence.md |
| inter-region-connectivity-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/inter-region-connectivity-monitoring/evidence/generated/scenario-test-evidence.md |
| kubernetes-cluster-health-monitoring | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/kubernetes-cluster-health-monitoring/evidence/generated/scenario-test-evidence.md |
| kubernetes-cluster-visibility | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/kubernetes-cluster-visibility/evidence/generated/scenario-test-evidence.md |
| load-balancer-health-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/load-balancer-health-monitoring/evidence/generated/scenario-test-evidence.md |
| message-queue-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/message-queue-monitoring/evidence/generated/scenario-test-evidence.md |
| microservice-health-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/microservice-health-monitoring/evidence/generated/scenario-test-evidence.md |
| network-path-visibility | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/network-path-visibility/evidence/generated/scenario-test-evidence.md |
| network-traffic-visibility | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/network-traffic-visibility/evidence/generated/scenario-test-evidence.md |
| object-storage-health-monitoring | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/object-storage-health-monitoring/evidence/generated/scenario-test-evidence.md |
| privileged-session-monitoring | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/privileged-session-monitoring/evidence/generated/scenario-test-evidence.md |
| process-health-monitoring | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/process-health-monitoring/evidence/generated/scenario-test-evidence.md |
| security-event-monitoring | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/security-event-monitoring/evidence/generated/scenario-test-evidence.md |
| security-policy-visibility | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/security-policy-visibility/evidence/generated/scenario-test-evidence.md |
| security-telemetry-monitoring | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/security-telemetry-monitoring/evidence/generated/scenario-test-evidence.md |
| service-health-visibility | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/service-health-visibility/evidence/generated/scenario-test-evidence.md |
| service-mesh-traffic-visibility | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/service-mesh-traffic-visibility/evidence/generated/scenario-test-evidence.md |
| storage-capacity-monitoring | 06-monitoring-stack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/storage-capacity-monitoring/evidence/generated/scenario-test-evidence.md |
| storage-latency-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/storage-latency-monitoring/evidence/generated/scenario-test-evidence.md |
| system-event-visibility | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/system-event-visibility/evidence/generated/scenario-test-evidence.md |
| virtual-machine-health-monitoring | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/virtual-machine-health-monitoring/evidence/generated/scenario-test-evidence.md |
| vpn-connectivity-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/vpn-connectivity-monitoring/evidence/generated/scenario-test-evidence.md |
| vpn-latency-visibility | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/vpn-latency-visibility/evidence/generated/scenario-test-evidence.md |
| vpn-tunnel-health-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/vpn-tunnel-health-monitoring/evidence/generated/scenario-test-evidence.md |
| wan-link-monitoring | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-1-visibility/wan-link-monitoring/evidence/generated/scenario-test-evidence.md |

## Level 2 Correlation

| Scenario | Mapped Lab | Study Evidence | Status | Evidence Path |
|---|---|---|---|---|
| api-latency-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/api-latency-correlation/evidence/generated/scenario-test-evidence.md |
| authentication-anomaly-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/authentication-anomaly-analysis/evidence/generated/scenario-test-evidence.md |
| backup-failure-correlation | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/backup-failure-correlation/evidence/generated/scenario-test-evidence.md |
| change-impact-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/change-impact-correlation/evidence/generated/scenario-test-evidence.md |
| cluster-resource-instability-analysis | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cluster-resource-instability-analysis/evidence/generated/scenario-test-evidence.md |
| compute-resource-correlation | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/compute-resource-correlation/evidence/generated/scenario-test-evidence.md |
| configuration-drift-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/configuration-drift-correlation/evidence/generated/scenario-test-evidence.md |
| container-dependency-analysis | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/container-dependency-analysis/evidence/generated/scenario-test-evidence.md |
| control-plane-anomaly-correlation | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/control-plane-anomaly-correlation/evidence/generated/scenario-test-evidence.md |
| cross-domain-security-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cross-domain-security-correlation/evidence/generated/scenario-test-evidence.md |
| cross-region-network-anomaly-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cross-region-network-anomaly-correlation/evidence/generated/scenario-test-evidence.md |
| cross-server-failure-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cross-server-failure-correlation/evidence/generated/scenario-test-evidence.md |
| cross-service-anomaly-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cross-service-anomaly-correlation/evidence/generated/scenario-test-evidence.md |
| cross-service-database-dependency-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cross-service-database-dependency-analysis/evidence/generated/scenario-test-evidence.md |
| cross-site-network-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/cross-site-network-correlation/evidence/generated/scenario-test-evidence.md |
| database-latency-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/database-latency-correlation/evidence/generated/scenario-test-evidence.md |
| filesystem-failure-correlation | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/filesystem-failure-correlation/evidence/generated/scenario-test-evidence.md |
| identity-risk-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/identity-risk-analysis/evidence/generated/scenario-test-evidence.md |
| infrastructure-anomaly-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/infrastructure-anomaly-analysis/evidence/generated/scenario-test-evidence.md |
| inter-region-dependency-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/inter-region-dependency-correlation/evidence/generated/scenario-test-evidence.md |
| multi-region-latency-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/multi-region-latency-correlation/evidence/generated/scenario-test-evidence.md |
| network-packet-loss-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/network-packet-loss-correlation/evidence/generated/scenario-test-evidence.md |
| network-path-dependency-analysis | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/network-path-dependency-analysis/evidence/generated/scenario-test-evidence.md |
| platform-dependency-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/platform-dependency-correlation/evidence/generated/scenario-test-evidence.md |
| pod-failure-correlation | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/pod-failure-correlation/evidence/generated/scenario-test-evidence.md |
| privilege-escalation-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/privilege-escalation-correlation/evidence/generated/scenario-test-evidence.md |
| query-lock-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/query-lock-analysis/evidence/generated/scenario-test-evidence.md |
| replication-failure-correlation | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/replication-failure-correlation/evidence/generated/scenario-test-evidence.md |
| resource-contention-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/resource-contention-correlation/evidence/generated/scenario-test-evidence.md |
| routing-instability-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/routing-instability-correlation/evidence/generated/scenario-test-evidence.md |
| runtime-instability-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/runtime-instability-analysis/evidence/generated/scenario-test-evidence.md |
| security-anomaly-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/security-anomaly-correlation/evidence/generated/scenario-test-evidence.md |
| security-policy-violation-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/security-policy-violation-analysis/evidence/generated/scenario-test-evidence.md |
| service-dependency-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/service-dependency-correlation/evidence/generated/scenario-test-evidence.md |
| service-mesh-latency-correlation | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/service-mesh-latency-correlation/evidence/generated/scenario-test-evidence.md |
| storage-io-instability-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/storage-io-instability-analysis/evidence/generated/scenario-test-evidence.md |
| threat-propagation-analysis | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/threat-propagation-analysis/evidence/generated/scenario-test-evidence.md |
| traffic-spike-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/traffic-spike-correlation/evidence/generated/scenario-test-evidence.md |
| virtualization-resource-correlation | 07-logging-correlation-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/virtualization-resource-correlation/evidence/generated/scenario-test-evidence.md |
| vpn-latency-correlation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/vpn-latency-correlation/evidence/generated/scenario-test-evidence.md |
| vpn-tunnel-instability-analysis | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-2-correlation/vpn-tunnel-instability-analysis/evidence/generated/scenario-test-evidence.md |

## Level 3 Recovery

| Scenario | Mapped Lab | Study Evidence | Status | Evidence Path |
|---|---|---|---|---|
| api-service-recovery | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/api-service-recovery/evidence/generated/scenario-test-evidence.md |
| backup-restoration-automation | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/backup-restoration-automation/evidence/generated/scenario-test-evidence.md |
| certificate-renewal-automation | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/certificate-renewal-automation/evidence/generated/scenario-test-evidence.md |
| change-failure-rollback | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/change-failure-rollback/evidence/generated/scenario-test-evidence.md |
| cloud-instance-recovery-automation | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/cloud-instance-recovery-automation/evidence/generated/scenario-test-evidence.md |
| cluster-node-recovery-orchestration | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/cluster-node-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| compute-failover-orchestration | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/compute-failover-orchestration/evidence/generated/scenario-test-evidence.md |
| configuration-rollback-automation | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/configuration-rollback-automation/evidence/generated/scenario-test-evidence.md |
| container-failover-automation | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/container-failover-automation/evidence/generated/scenario-test-evidence.md |
| control-plane-recovery-orchestration | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/control-plane-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| data-recovery-orchestration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/data-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| database-failover-automation | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/database-failover-automation/evidence/generated/scenario-test-evidence.md |
| database-recovery-orchestration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/database-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| database-service-restoration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/database-service-restoration/evidence/generated/scenario-test-evidence.md |
| dns-service-restoration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/dns-service-restoration/evidence/generated/scenario-test-evidence.md |
| identity-access-remediation | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/identity-access-remediation/evidence/generated/scenario-test-evidence.md |
| infrastructure-recovery-orchestration | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/infrastructure-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| inter-region-routing-recovery | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/inter-region-routing-recovery/evidence/generated/scenario-test-evidence.md |
| kubernetes-control-plane-recovery | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/kubernetes-control-plane-recovery/evidence/generated/scenario-test-evidence.md |
| kubernetes-node-recovery | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/kubernetes-node-recovery/evidence/generated/scenario-test-evidence.md |
| kubernetes-service-recovery | 04-container-runtime-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/kubernetes-service-recovery/evidence/generated/scenario-test-evidence.md |
| load-balancer-recovery | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/load-balancer-recovery/evidence/generated/scenario-test-evidence.md |
| network-failover-automation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/network-failover-automation/evidence/generated/scenario-test-evidence.md |
| network-route-recovery-orchestration | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/network-route-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| platform-runtime-restoration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/platform-runtime-restoration/evidence/generated/scenario-test-evidence.md |
| replication-recovery-orchestration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/replication-recovery-orchestration/evidence/generated/scenario-test-evidence.md |
| resource-rebalancing-automation | 03-ansible-automation-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/resource-rebalancing-automation/evidence/generated/scenario-test-evidence.md |
| server-service-recovery | 01-linux-observability-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/server-service-recovery/evidence/generated/scenario-test-evidence.md |
| service-mesh-traffic-restoration | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/service-mesh-traffic-restoration/evidence/generated/scenario-test-evidence.md |
| storage-volume-recovery-automation | 08-backup-recovery-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/storage-volume-recovery-automation/evidence/generated/scenario-test-evidence.md |
| traffic-restoration-workflow | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/traffic-restoration-workflow/evidence/generated/scenario-test-evidence.md |
| virtual-machine-restoration | 05-kolla-openstack-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/virtual-machine-restoration/evidence/generated/scenario-test-evidence.md |
| vpn-tunnel-recovery-automation | 02-network-routing-lab | YES | STUDY_VALIDATED | scenarios/level-3-recovery/vpn-tunnel-recovery-automation/evidence/generated/scenario-test-evidence.md |

## Level 4 Resilience

| Scenario | Mapped Lab | Study Evidence | Status | Evidence Path |
|---|---|---|---|---|
| backup-resilience-validation | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/backup-resilience-validation/evidence/generated/scenario-test-evidence.md |
| change-resilience-coordination | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/change-resilience-coordination/evidence/generated/scenario-test-evidence.md |
| configuration-resilience-validation | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/configuration-resilience-validation/evidence/generated/scenario-test-evidence.md |
| control-plane-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/control-plane-resilience/evidence/generated/scenario-test-evidence.md |
| cross-region-data-survivability | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/cross-region-data-survivability/evidence/generated/scenario-test-evidence.md |
| cross-region-kubernetes-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/cross-region-kubernetes-resilience/evidence/generated/scenario-test-evidence.md |
| cross-region-network-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/cross-region-network-resilience/evidence/generated/scenario-test-evidence.md |
| distributed-connectivity-survivability | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/distributed-connectivity-survivability/evidence/generated/scenario-test-evidence.md |
| distributed-database-failover | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/distributed-database-failover/evidence/generated/scenario-test-evidence.md |
| distributed-platform-survivability | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/distributed-platform-survivability/evidence/generated/scenario-test-evidence.md |
| distributed-security-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/distributed-security-resilience/evidence/generated/scenario-test-evidence.md |
| identity-failover-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/identity-failover-resilience/evidence/generated/scenario-test-evidence.md |
| identity-resilience-coordination | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/identity-resilience-coordination/evidence/generated/scenario-test-evidence.md |
| inter-region-routing-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/inter-region-routing-resilience/evidence/generated/scenario-test-evidence.md |
| kubernetes-platform-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/kubernetes-platform-resilience/evidence/generated/scenario-test-evidence.md |
| multi-cluster-failover | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/multi-cluster-failover/evidence/generated/scenario-test-evidence.md |
| multi-cluster-failover-coordination | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/multi-cluster-failover-coordination/evidence/generated/scenario-test-evidence.md |
| multi-region-service-failover | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/multi-region-service-failover/evidence/generated/scenario-test-evidence.md |
| multi-region-service-failover-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/multi-region-service-failover-resilience/evidence/generated/scenario-test-evidence.md |
| multi-site-routing-failover | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/multi-site-routing-failover/evidence/generated/scenario-test-evidence.md |
| storage-replication-resilience | 09-resilience-failover-lab | YES | STUDY_VALIDATED | scenarios/level-4-resilience/storage-replication-resilience/evidence/generated/scenario-test-evidence.md |

## Level 5 Continuity

| Scenario | Mapped Lab | Study Evidence | Status | Evidence Path |
|---|---|---|---|---|
| enterprise-change-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-change-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-cloud-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-cloud-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-control-plane-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-control-plane-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-data-protection-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-data-protection-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-identity-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-identity-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-network-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-network-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-operational-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-operational-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-platform-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-platform-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-security-continuity | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-security-continuity/evidence/generated/scenario-test-evidence.md |
| enterprise-service-continuity-coordination | 10-governance-reporting-lab | YES | STUDY_VALIDATED | scenarios/level-5-continuity/enterprise-service-continuity-coordination/evidence/generated/scenario-test-evidence.md |

## Notes

- Mapped Lab is extracted from scenario-test-evidence.md.
- Study Evidence indicates whether lab-based-study-validation.md exists for the scenario.
- STUDY_VALIDATED means the scenario has baseline generated evidence and lab-based study evidence.
- EVIDENCE_READY means baseline scenario evidence exists but lab-based study evidence has not been generated yet.
- PARTIAL_EVIDENCE means at least one expected baseline evidence file is missing.
- MISSING_MAPPING means no mapped lab could be extracted.
