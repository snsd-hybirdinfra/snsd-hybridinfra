# Lab Coverage Matrix

Generated At: 2026-06-15T00:02:29.884702Z

## Purpose

This document maps lifecycle-aligned operational scenarios to implementation lab boundaries.

Scenarios define operational validation cases.

Labs define reusable implementation boundaries that validate groups of scenarios.

This matrix is generated from repository state and scenario naming taxonomy.

## Coverage Summary

| Signal | Value |
|---|---:|
| Total scenarios | 150 |
| Covered scenarios | 150 |
| Uncovered scenarios | 0 |
| Implementation labs | 10 |

## Lifecycle Scenario Count

| Lifecycle Level | Scenario Count |
|---|---:|
| [Level 1 Visibility](../scenarios/level-1-visibility/README.md) | 45 |
| [Level 2 Correlation](../scenarios/level-2-correlation/README.md) | 41 |
| [Level 3 Recovery](../scenarios/level-3-recovery/README.md) | 33 |
| [Level 4 Resilience](../scenarios/level-4-resilience/README.md) | 21 |
| [Level 5 Continuity](../scenarios/level-5-continuity/README.md) | 10 |

## Lab Coverage Count

| Lab | Scope | Covered Scenarios |
|---|---|---:|
| [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) | Linux observability and host visibility | 25 |
| [02-network-routing-lab](../labs/02-network-routing-lab/README.md) | Network routing, reachability, DNS, and latency validation | 15 |
| [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) | Automation execution, recovery workflow, and validation | 13 |
| [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) | Container runtime visibility and restart recovery | 7 |
| [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/README.md) | OpenStack/Kolla-Ansible preflight and control plane readiness | 2 |
| [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/README.md) | Prometheus/Grafana monitoring, scrape, and dashboard readiness | 0 |
| [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) | Log normalization, timeline reconstruction, and correlation analysis | 36 |
| [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) | Backup, restore, checksum, and integrity validation | 16 |
| [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) | Failover decision, traffic shift, and resilience validation | 34 |
| [10-governance-reporting-lab](../labs/10-governance-reporting-lab/README.md) | Repository validation, governance reporting, and quality gates | 2 |

## Scenario-to-Lab Matrix

| Lifecycle Level | Scenario | Implementation Lab |
|---|---|---|
| Level 1 Visibility | [api-gateway-health-monitoring](../scenarios/level-1-visibility/api-gateway-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [application-runtime-monitoring](../scenarios/level-1-visibility/application-runtime-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [audit-log-monitoring](../scenarios/level-1-visibility/audit-log-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [backup-job-monitoring](../scenarios/level-1-visibility/backup-job-monitoring/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 1 Visibility | [bgp-neighbor-visibility](../scenarios/level-1-visibility/bgp-neighbor-visibility/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [certificate-expiration-monitoring](../scenarios/level-1-visibility/certificate-expiration-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [cloud-instance-health-monitoring](../scenarios/level-1-visibility/cloud-instance-health-monitoring/README.md) | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/README.md) |
| Level 1 Visibility | [compute-resource-monitoring](../scenarios/level-1-visibility/compute-resource-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [configuration-drift-monitoring](../scenarios/level-1-visibility/configuration-drift-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [container-runtime-visibility](../scenarios/level-1-visibility/container-runtime-visibility/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 1 Visibility | [control-plane-health-monitoring](../scenarios/level-1-visibility/control-plane-health-monitoring/README.md) | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/README.md) |
| Level 1 Visibility | [database-health-monitoring](../scenarios/level-1-visibility/database-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [database-replication-visibility](../scenarios/level-1-visibility/database-replication-visibility/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 1 Visibility | [database-runtime-visibility](../scenarios/level-1-visibility/database-runtime-visibility/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [dns-resolution-monitoring](../scenarios/level-1-visibility/dns-resolution-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [endpoint-reachability-monitoring](../scenarios/level-1-visibility/endpoint-reachability-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [endpoint-security-visibility](../scenarios/level-1-visibility/endpoint-security-visibility/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [filesystem-health-visibility](../scenarios/level-1-visibility/filesystem-health-visibility/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [hardware-health-monitoring](../scenarios/level-1-visibility/hardware-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [hypervisor-resource-monitoring](../scenarios/level-1-visibility/hypervisor-resource-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [identity-access-visibility](../scenarios/level-1-visibility/identity-access-visibility/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [inter-region-connectivity-monitoring](../scenarios/level-1-visibility/inter-region-connectivity-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [kubernetes-cluster-health-monitoring](../scenarios/level-1-visibility/kubernetes-cluster-health-monitoring/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 1 Visibility | [kubernetes-cluster-visibility](../scenarios/level-1-visibility/kubernetes-cluster-visibility/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 1 Visibility | [load-balancer-health-monitoring](../scenarios/level-1-visibility/load-balancer-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [message-queue-monitoring](../scenarios/level-1-visibility/message-queue-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [microservice-health-monitoring](../scenarios/level-1-visibility/microservice-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [network-path-visibility](../scenarios/level-1-visibility/network-path-visibility/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [network-traffic-visibility](../scenarios/level-1-visibility/network-traffic-visibility/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [object-storage-health-monitoring](../scenarios/level-1-visibility/object-storage-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [privileged-session-monitoring](../scenarios/level-1-visibility/privileged-session-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [process-health-monitoring](../scenarios/level-1-visibility/process-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [security-event-monitoring](../scenarios/level-1-visibility/security-event-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [security-policy-visibility](../scenarios/level-1-visibility/security-policy-visibility/README.md) | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/README.md) |
| Level 1 Visibility | [security-telemetry-monitoring](../scenarios/level-1-visibility/security-telemetry-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [service-health-visibility](../scenarios/level-1-visibility/service-health-visibility/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [service-mesh-traffic-visibility](../scenarios/level-1-visibility/service-mesh-traffic-visibility/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 1 Visibility | [storage-capacity-monitoring](../scenarios/level-1-visibility/storage-capacity-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [storage-latency-monitoring](../scenarios/level-1-visibility/storage-latency-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [system-event-visibility](../scenarios/level-1-visibility/system-event-visibility/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [virtual-machine-health-monitoring](../scenarios/level-1-visibility/virtual-machine-health-monitoring/README.md) | [01-linux-observability-lab](../labs/01-linux-observability-lab/README.md) |
| Level 1 Visibility | [vpn-connectivity-monitoring](../scenarios/level-1-visibility/vpn-connectivity-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [vpn-latency-visibility](../scenarios/level-1-visibility/vpn-latency-visibility/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [vpn-tunnel-health-monitoring](../scenarios/level-1-visibility/vpn-tunnel-health-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 1 Visibility | [wan-link-monitoring](../scenarios/level-1-visibility/wan-link-monitoring/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 2 Correlation | [api-latency-correlation](../scenarios/level-2-correlation/api-latency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [authentication-anomaly-analysis](../scenarios/level-2-correlation/authentication-anomaly-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [backup-failure-correlation](../scenarios/level-2-correlation/backup-failure-correlation/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 2 Correlation | [change-impact-correlation](../scenarios/level-2-correlation/change-impact-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [cluster-resource-instability-analysis](../scenarios/level-2-correlation/cluster-resource-instability-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [compute-resource-correlation](../scenarios/level-2-correlation/compute-resource-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [configuration-drift-correlation](../scenarios/level-2-correlation/configuration-drift-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [container-dependency-analysis](../scenarios/level-2-correlation/container-dependency-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [control-plane-anomaly-correlation](../scenarios/level-2-correlation/control-plane-anomaly-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [cross-domain-security-correlation](../scenarios/level-2-correlation/cross-domain-security-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [cross-region-network-anomaly-correlation](../scenarios/level-2-correlation/cross-region-network-anomaly-correlation/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 2 Correlation | [cross-server-failure-correlation](../scenarios/level-2-correlation/cross-server-failure-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [cross-service-anomaly-correlation](../scenarios/level-2-correlation/cross-service-anomaly-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [cross-service-database-dependency-analysis](../scenarios/level-2-correlation/cross-service-database-dependency-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [cross-site-network-correlation](../scenarios/level-2-correlation/cross-site-network-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [database-latency-correlation](../scenarios/level-2-correlation/database-latency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [filesystem-failure-correlation](../scenarios/level-2-correlation/filesystem-failure-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [identity-risk-analysis](../scenarios/level-2-correlation/identity-risk-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [infrastructure-anomaly-analysis](../scenarios/level-2-correlation/infrastructure-anomaly-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [inter-region-dependency-correlation](../scenarios/level-2-correlation/inter-region-dependency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [multi-region-latency-correlation](../scenarios/level-2-correlation/multi-region-latency-correlation/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 2 Correlation | [network-packet-loss-correlation](../scenarios/level-2-correlation/network-packet-loss-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [network-path-dependency-analysis](../scenarios/level-2-correlation/network-path-dependency-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [platform-dependency-correlation](../scenarios/level-2-correlation/platform-dependency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [pod-failure-correlation](../scenarios/level-2-correlation/pod-failure-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [privilege-escalation-correlation](../scenarios/level-2-correlation/privilege-escalation-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [query-lock-analysis](../scenarios/level-2-correlation/query-lock-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [replication-failure-correlation](../scenarios/level-2-correlation/replication-failure-correlation/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 2 Correlation | [resource-contention-correlation](../scenarios/level-2-correlation/resource-contention-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [routing-instability-correlation](../scenarios/level-2-correlation/routing-instability-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [runtime-instability-analysis](../scenarios/level-2-correlation/runtime-instability-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [security-anomaly-correlation](../scenarios/level-2-correlation/security-anomaly-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [security-policy-violation-analysis](../scenarios/level-2-correlation/security-policy-violation-analysis/README.md) | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/README.md) |
| Level 2 Correlation | [service-dependency-correlation](../scenarios/level-2-correlation/service-dependency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [service-mesh-latency-correlation](../scenarios/level-2-correlation/service-mesh-latency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [storage-io-instability-analysis](../scenarios/level-2-correlation/storage-io-instability-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [threat-propagation-analysis](../scenarios/level-2-correlation/threat-propagation-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [traffic-spike-correlation](../scenarios/level-2-correlation/traffic-spike-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [virtualization-resource-correlation](../scenarios/level-2-correlation/virtualization-resource-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [vpn-latency-correlation](../scenarios/level-2-correlation/vpn-latency-correlation/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 2 Correlation | [vpn-tunnel-instability-analysis](../scenarios/level-2-correlation/vpn-tunnel-instability-analysis/README.md) | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/README.md) |
| Level 3 Recovery | [api-service-recovery](../scenarios/level-3-recovery/api-service-recovery/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [backup-restoration-automation](../scenarios/level-3-recovery/backup-restoration-automation/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [certificate-renewal-automation](../scenarios/level-3-recovery/certificate-renewal-automation/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [change-failure-rollback](../scenarios/level-3-recovery/change-failure-rollback/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [cloud-instance-recovery-automation](../scenarios/level-3-recovery/cloud-instance-recovery-automation/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [cluster-node-recovery-orchestration](../scenarios/level-3-recovery/cluster-node-recovery-orchestration/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [compute-failover-orchestration](../scenarios/level-3-recovery/compute-failover-orchestration/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 3 Recovery | [configuration-rollback-automation](../scenarios/level-3-recovery/configuration-rollback-automation/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [container-failover-automation](../scenarios/level-3-recovery/container-failover-automation/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 3 Recovery | [control-plane-recovery-orchestration](../scenarios/level-3-recovery/control-plane-recovery-orchestration/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [data-recovery-orchestration](../scenarios/level-3-recovery/data-recovery-orchestration/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [database-failover-automation](../scenarios/level-3-recovery/database-failover-automation/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 3 Recovery | [database-recovery-orchestration](../scenarios/level-3-recovery/database-recovery-orchestration/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [database-service-restoration](../scenarios/level-3-recovery/database-service-restoration/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [dns-service-restoration](../scenarios/level-3-recovery/dns-service-restoration/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [identity-access-remediation](../scenarios/level-3-recovery/identity-access-remediation/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [infrastructure-recovery-orchestration](../scenarios/level-3-recovery/infrastructure-recovery-orchestration/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [inter-region-routing-recovery](../scenarios/level-3-recovery/inter-region-routing-recovery/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 3 Recovery | [kubernetes-control-plane-recovery](../scenarios/level-3-recovery/kubernetes-control-plane-recovery/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 3 Recovery | [kubernetes-node-recovery](../scenarios/level-3-recovery/kubernetes-node-recovery/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 3 Recovery | [kubernetes-service-recovery](../scenarios/level-3-recovery/kubernetes-service-recovery/README.md) | [04-container-runtime-lab](../labs/04-container-runtime-lab/README.md) |
| Level 3 Recovery | [load-balancer-recovery](../scenarios/level-3-recovery/load-balancer-recovery/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 3 Recovery | [network-failover-automation](../scenarios/level-3-recovery/network-failover-automation/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 3 Recovery | [network-route-recovery-orchestration](../scenarios/level-3-recovery/network-route-recovery-orchestration/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 3 Recovery | [platform-runtime-restoration](../scenarios/level-3-recovery/platform-runtime-restoration/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [replication-recovery-orchestration](../scenarios/level-3-recovery/replication-recovery-orchestration/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [resource-rebalancing-automation](../scenarios/level-3-recovery/resource-rebalancing-automation/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [server-service-recovery](../scenarios/level-3-recovery/server-service-recovery/README.md) | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/README.md) |
| Level 3 Recovery | [service-mesh-traffic-restoration](../scenarios/level-3-recovery/service-mesh-traffic-restoration/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [storage-volume-recovery-automation](../scenarios/level-3-recovery/storage-volume-recovery-automation/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [traffic-restoration-workflow](../scenarios/level-3-recovery/traffic-restoration-workflow/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [virtual-machine-restoration](../scenarios/level-3-recovery/virtual-machine-restoration/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 3 Recovery | [vpn-tunnel-recovery-automation](../scenarios/level-3-recovery/vpn-tunnel-recovery-automation/README.md) | [02-network-routing-lab](../labs/02-network-routing-lab/README.md) |
| Level 4 Resilience | [backup-resilience-validation](../scenarios/level-4-resilience/backup-resilience-validation/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 4 Resilience | [change-resilience-coordination](../scenarios/level-4-resilience/change-resilience-coordination/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [configuration-resilience-validation](../scenarios/level-4-resilience/configuration-resilience-validation/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [control-plane-resilience](../scenarios/level-4-resilience/control-plane-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [cross-region-data-survivability](../scenarios/level-4-resilience/cross-region-data-survivability/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [cross-region-kubernetes-resilience](../scenarios/level-4-resilience/cross-region-kubernetes-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [cross-region-network-resilience](../scenarios/level-4-resilience/cross-region-network-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [distributed-connectivity-survivability](../scenarios/level-4-resilience/distributed-connectivity-survivability/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [distributed-database-failover](../scenarios/level-4-resilience/distributed-database-failover/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [distributed-platform-survivability](../scenarios/level-4-resilience/distributed-platform-survivability/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [distributed-security-resilience](../scenarios/level-4-resilience/distributed-security-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [identity-failover-resilience](../scenarios/level-4-resilience/identity-failover-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [identity-resilience-coordination](../scenarios/level-4-resilience/identity-resilience-coordination/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [inter-region-routing-resilience](../scenarios/level-4-resilience/inter-region-routing-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [kubernetes-platform-resilience](../scenarios/level-4-resilience/kubernetes-platform-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [multi-cluster-failover](../scenarios/level-4-resilience/multi-cluster-failover/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [multi-cluster-failover-coordination](../scenarios/level-4-resilience/multi-cluster-failover-coordination/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [multi-region-service-failover](../scenarios/level-4-resilience/multi-region-service-failover/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [multi-region-service-failover-resilience](../scenarios/level-4-resilience/multi-region-service-failover-resilience/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [multi-site-routing-failover](../scenarios/level-4-resilience/multi-site-routing-failover/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 4 Resilience | [storage-replication-resilience](../scenarios/level-4-resilience/storage-replication-resilience/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 5 Continuity | [enterprise-change-continuity](../scenarios/level-5-continuity/enterprise-change-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-cloud-continuity](../scenarios/level-5-continuity/enterprise-cloud-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-control-plane-continuity](../scenarios/level-5-continuity/enterprise-control-plane-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-data-protection-continuity](../scenarios/level-5-continuity/enterprise-data-protection-continuity/README.md) | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/README.md) |
| Level 5 Continuity | [enterprise-identity-continuity](../scenarios/level-5-continuity/enterprise-identity-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-network-continuity](../scenarios/level-5-continuity/enterprise-network-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-operational-continuity](../scenarios/level-5-continuity/enterprise-operational-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-platform-continuity](../scenarios/level-5-continuity/enterprise-platform-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-security-continuity](../scenarios/level-5-continuity/enterprise-security-continuity/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |
| Level 5 Continuity | [enterprise-service-continuity-coordination](../scenarios/level-5-continuity/enterprise-service-continuity-coordination/README.md) | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/README.md) |

## Mapping Policy

The matrix maps scenarios to labs based on operational domain and scenario naming taxonomy.

A scenario does not require a dedicated standalone lab.

Multiple scenarios may be validated through the same reusable implementation boundary.

This keeps the repository scalable while preserving reviewer-readable operational coverage.

## Important Boundary

This matrix represents implementation coverage at the lab boundary level.

It does not claim that every scenario has a separate runtime deployment.

Generated by tools/content-generator/generate_lab_coverage_matrix.py
