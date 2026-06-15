# Scenario to Lab Traceability

## 1. Purpose

This document maps operational scenarios to implementation labs so reviewers can trace each scenario to a concrete runtime validation boundary.

## 2. Traceability Model

| Layer | Meaning |
|---|---|
| Scenario | Operational capability validation workflow |
| Lab | Implementation and runtime validation boundary |
| Evidence | Local generated runtime validation output |
| Report | Reviewer-readable validation or governance summary |

## 3. Coverage Summary

| Metric | Count |
|---|---:|
| Total scenarios | 150 |
| Total labs | 10 |
| Mapped scenarios | 150 |

## 4. Lifecycle Coverage

| Lifecycle | Scenario Count |
|---|---:|
| level-1-visibility | 45 |
| level-2-correlation | 41 |
| level-3-recovery | 33 |
| level-4-resilience | 21 |
| level-5-continuity | 10 |

## 5. Lab Coverage

| Lab | Runtime Boundary | Scenario Count |
|---|---|---:|
| 01-linux-observability-lab | Linux Observability Lab | 9 |
| 02-network-routing-lab | Network Routing Lab | 28 |
| 03-ansible-automation-lab | Ansible Automation Lab | 9 |
| 04-container-runtime-lab | Container Runtime Lab | 12 |
| 05-kolla-openstack-lab | Kolla OpenStack Lab | 10 |
| 06-monitoring-stack-lab | Monitoring Stack Lab | 17 |
| 07-logging-correlation-lab | Logging Correlation Lab | 21 |
| 08-backup-recovery-lab | Backup Recovery Lab | 13 |
| 09-resilience-failover-lab | Resilience Failover Lab | 21 |
| 10-governance-reporting-lab | Governance Reporting Lab | 10 |

## 6. Scenario Mapping

| Lifecycle | Scenario | Primary Domain | Mapped Lab | Mapping Reason |
|---|---|---|---|---|
| level-1-visibility | [api-gateway-health-monitoring](../scenarios/level-1-visibility/api-gateway-health-monitoring) | API / Gateway | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [application-runtime-monitoring](../scenarios/level-1-visibility/application-runtime-monitoring) | Application Runtime | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [audit-log-monitoring](../scenarios/level-1-visibility/audit-log-monitoring) | Audit / Logging | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [backup-job-monitoring](../scenarios/level-1-visibility/backup-job-monitoring) | Backup / Recovery | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-1-visibility | [bgp-neighbor-visibility](../scenarios/level-1-visibility/bgp-neighbor-visibility) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [certificate-expiration-monitoring](../scenarios/level-1-visibility/certificate-expiration-monitoring) | TLS / Certificate | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [cloud-instance-health-monitoring](../scenarios/level-1-visibility/cloud-instance-health-monitoring) | Cloud Instance | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-1-visibility | [compute-resource-monitoring](../scenarios/level-1-visibility/compute-resource-monitoring) | Compute / Resource | 01-linux-observability-lab | Domain priority: linux host observability |
| level-1-visibility | [configuration-drift-monitoring](../scenarios/level-1-visibility/configuration-drift-monitoring) | Configuration Operations | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [container-runtime-visibility](../scenarios/level-1-visibility/container-runtime-visibility) | Container / Runtime | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-1-visibility | [control-plane-health-monitoring](../scenarios/level-1-visibility/control-plane-health-monitoring) | Platform Operations | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-1-visibility | [database-health-monitoring](../scenarios/level-1-visibility/database-health-monitoring) | Database | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [database-replication-visibility](../scenarios/level-1-visibility/database-replication-visibility) | Database | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-1-visibility | [database-runtime-visibility](../scenarios/level-1-visibility/database-runtime-visibility) | Database | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [dns-resolution-monitoring](../scenarios/level-1-visibility/dns-resolution-monitoring) | DNS / Name Resolution | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [endpoint-reachability-monitoring](../scenarios/level-1-visibility/endpoint-reachability-monitoring) | Endpoint | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [endpoint-security-visibility](../scenarios/level-1-visibility/endpoint-security-visibility) | Security / Telemetry | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [filesystem-health-visibility](../scenarios/level-1-visibility/filesystem-health-visibility) | Filesystem | 01-linux-observability-lab | Domain priority: linux host observability |
| level-1-visibility | [hardware-health-monitoring](../scenarios/level-1-visibility/hardware-health-monitoring) | Hardware | 01-linux-observability-lab | Domain priority: linux host observability |
| level-1-visibility | [hypervisor-resource-monitoring](../scenarios/level-1-visibility/hypervisor-resource-monitoring) | Virtualization | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-1-visibility | [identity-access-visibility](../scenarios/level-1-visibility/identity-access-visibility) | Identity / Access | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [inter-region-connectivity-monitoring](../scenarios/level-1-visibility/inter-region-connectivity-monitoring) | Network Operations | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [kubernetes-cluster-health-monitoring](../scenarios/level-1-visibility/kubernetes-cluster-health-monitoring) | Kubernetes / Cluster | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-1-visibility | [kubernetes-cluster-visibility](../scenarios/level-1-visibility/kubernetes-cluster-visibility) | Kubernetes / Cluster | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-1-visibility | [load-balancer-health-monitoring](../scenarios/level-1-visibility/load-balancer-health-monitoring) | Load Balancing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [message-queue-monitoring](../scenarios/level-1-visibility/message-queue-monitoring) | Message Queue | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [microservice-health-monitoring](../scenarios/level-1-visibility/microservice-health-monitoring) | Microservice | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [network-path-visibility](../scenarios/level-1-visibility/network-path-visibility) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [network-traffic-visibility](../scenarios/level-1-visibility/network-traffic-visibility) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [object-storage-health-monitoring](../scenarios/level-1-visibility/object-storage-health-monitoring) | Storage | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-1-visibility | [privileged-session-monitoring](../scenarios/level-1-visibility/privileged-session-monitoring) | Privileged Access | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [process-health-monitoring](../scenarios/level-1-visibility/process-health-monitoring) | Process / Service | 01-linux-observability-lab | Domain priority: linux host observability |
| level-1-visibility | [security-event-monitoring](../scenarios/level-1-visibility/security-event-monitoring) | Security / Telemetry | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [security-policy-visibility](../scenarios/level-1-visibility/security-policy-visibility) | Security / Telemetry | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [security-telemetry-monitoring](../scenarios/level-1-visibility/security-telemetry-monitoring) | Security / Telemetry | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [service-health-visibility](../scenarios/level-1-visibility/service-health-visibility) | General Infrastructure | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [service-mesh-traffic-visibility](../scenarios/level-1-visibility/service-mesh-traffic-visibility) | Service Mesh | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-1-visibility | [storage-capacity-monitoring](../scenarios/level-1-visibility/storage-capacity-monitoring) | Storage | 06-monitoring-stack-lab | Lifecycle priority: level-1-visibility monitoring |
| level-1-visibility | [storage-latency-monitoring](../scenarios/level-1-visibility/storage-latency-monitoring) | Storage | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [system-event-visibility](../scenarios/level-1-visibility/system-event-visibility) | System Event | 01-linux-observability-lab | Domain priority: linux host observability |
| level-1-visibility | [virtual-machine-health-monitoring](../scenarios/level-1-visibility/virtual-machine-health-monitoring) | Virtual Machine | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-1-visibility | [vpn-connectivity-monitoring](../scenarios/level-1-visibility/vpn-connectivity-monitoring) | Network / VPN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [vpn-latency-visibility](../scenarios/level-1-visibility/vpn-latency-visibility) | Network / VPN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [vpn-tunnel-health-monitoring](../scenarios/level-1-visibility/vpn-tunnel-health-monitoring) | Network / VPN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-1-visibility | [wan-link-monitoring](../scenarios/level-1-visibility/wan-link-monitoring) | Network / WAN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [api-latency-correlation](../scenarios/level-2-correlation/api-latency-correlation) | API / Service | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [authentication-anomaly-analysis](../scenarios/level-2-correlation/authentication-anomaly-analysis) | Identity / Authentication | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [backup-failure-correlation](../scenarios/level-2-correlation/backup-failure-correlation) | Backup / Recovery | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-2-correlation | [change-impact-correlation](../scenarios/level-2-correlation/change-impact-correlation) | Change Operations | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [cluster-resource-instability-analysis](../scenarios/level-2-correlation/cluster-resource-instability-analysis) | Cluster / Platform | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-2-correlation | [compute-resource-correlation](../scenarios/level-2-correlation/compute-resource-correlation) | Compute / Resource | 01-linux-observability-lab | Domain priority: linux host observability |
| level-2-correlation | [configuration-drift-correlation](../scenarios/level-2-correlation/configuration-drift-correlation) | Configuration Operations | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [container-dependency-analysis](../scenarios/level-2-correlation/container-dependency-analysis) | Container / Runtime | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-2-correlation | [control-plane-anomaly-correlation](../scenarios/level-2-correlation/control-plane-anomaly-correlation) | Platform Operations | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-2-correlation | [cross-domain-security-correlation](../scenarios/level-2-correlation/cross-domain-security-correlation) | Security / Telemetry | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [cross-region-network-anomaly-correlation](../scenarios/level-2-correlation/cross-region-network-anomaly-correlation) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [cross-server-failure-correlation](../scenarios/level-2-correlation/cross-server-failure-correlation) | General Infrastructure | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [cross-service-anomaly-correlation](../scenarios/level-2-correlation/cross-service-anomaly-correlation) | General Infrastructure | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [cross-service-database-dependency-analysis](../scenarios/level-2-correlation/cross-service-database-dependency-analysis) | Database | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [cross-site-network-correlation](../scenarios/level-2-correlation/cross-site-network-correlation) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [database-latency-correlation](../scenarios/level-2-correlation/database-latency-correlation) | Database | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [filesystem-failure-correlation](../scenarios/level-2-correlation/filesystem-failure-correlation) | Filesystem | 01-linux-observability-lab | Domain priority: linux host observability |
| level-2-correlation | [identity-risk-analysis](../scenarios/level-2-correlation/identity-risk-analysis) | Identity / Access | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [infrastructure-anomaly-analysis](../scenarios/level-2-correlation/infrastructure-anomaly-analysis) | General Infrastructure | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [inter-region-dependency-correlation](../scenarios/level-2-correlation/inter-region-dependency-correlation) | Network Operations | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [multi-region-latency-correlation](../scenarios/level-2-correlation/multi-region-latency-correlation) | General Infrastructure | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [network-packet-loss-correlation](../scenarios/level-2-correlation/network-packet-loss-correlation) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [network-path-dependency-analysis](../scenarios/level-2-correlation/network-path-dependency-analysis) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [platform-dependency-correlation](../scenarios/level-2-correlation/platform-dependency-correlation) | General Infrastructure | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [pod-failure-correlation](../scenarios/level-2-correlation/pod-failure-correlation) | Container / Pod | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-2-correlation | [privilege-escalation-correlation](../scenarios/level-2-correlation/privilege-escalation-correlation) | Privileged Access | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [query-lock-analysis](../scenarios/level-2-correlation/query-lock-analysis) | Database / Query | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [replication-failure-correlation](../scenarios/level-2-correlation/replication-failure-correlation) | Database / Replication | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-2-correlation | [resource-contention-correlation](../scenarios/level-2-correlation/resource-contention-correlation) | General Infrastructure | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [routing-instability-correlation](../scenarios/level-2-correlation/routing-instability-correlation) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [runtime-instability-analysis](../scenarios/level-2-correlation/runtime-instability-analysis) | General Infrastructure | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [security-anomaly-correlation](../scenarios/level-2-correlation/security-anomaly-correlation) | Security / Telemetry | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [security-policy-violation-analysis](../scenarios/level-2-correlation/security-policy-violation-analysis) | Security / Telemetry | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [service-dependency-correlation](../scenarios/level-2-correlation/service-dependency-correlation) | General Infrastructure | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [service-mesh-latency-correlation](../scenarios/level-2-correlation/service-mesh-latency-correlation) | Service Mesh | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-2-correlation | [storage-io-instability-analysis](../scenarios/level-2-correlation/storage-io-instability-analysis) | Storage | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [threat-propagation-analysis](../scenarios/level-2-correlation/threat-propagation-analysis) | General Infrastructure | 07-logging-correlation-lab | Lifecycle/domain priority: correlation logging/security |
| level-2-correlation | [traffic-spike-correlation](../scenarios/level-2-correlation/traffic-spike-correlation) | Traffic / Flow | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [virtualization-resource-correlation](../scenarios/level-2-correlation/virtualization-resource-correlation) | General Infrastructure | 07-logging-correlation-lab | Lifecycle priority: level-2-correlation |
| level-2-correlation | [vpn-latency-correlation](../scenarios/level-2-correlation/vpn-latency-correlation) | Network / VPN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-2-correlation | [vpn-tunnel-instability-analysis](../scenarios/level-2-correlation/vpn-tunnel-instability-analysis) | Network / VPN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-3-recovery | [api-service-recovery](../scenarios/level-3-recovery/api-service-recovery) | API / Service | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [backup-restoration-automation](../scenarios/level-3-recovery/backup-restoration-automation) | Backup / Recovery | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [certificate-renewal-automation](../scenarios/level-3-recovery/certificate-renewal-automation) | Security Operations | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [change-failure-rollback](../scenarios/level-3-recovery/change-failure-rollback) | Change Operations | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [cloud-instance-recovery-automation](../scenarios/level-3-recovery/cloud-instance-recovery-automation) | Cloud Instance | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-3-recovery | [cluster-node-recovery-orchestration](../scenarios/level-3-recovery/cluster-node-recovery-orchestration) | Cluster / Platform | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-3-recovery | [compute-failover-orchestration](../scenarios/level-3-recovery/compute-failover-orchestration) | Compute / Resource | 01-linux-observability-lab | Domain priority: linux host observability |
| level-3-recovery | [configuration-rollback-automation](../scenarios/level-3-recovery/configuration-rollback-automation) | Configuration Operations | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [container-failover-automation](../scenarios/level-3-recovery/container-failover-automation) | Container / Runtime | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-3-recovery | [control-plane-recovery-orchestration](../scenarios/level-3-recovery/control-plane-recovery-orchestration) | Platform Operations | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-3-recovery | [data-recovery-orchestration](../scenarios/level-3-recovery/data-recovery-orchestration) | General Infrastructure | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [database-failover-automation](../scenarios/level-3-recovery/database-failover-automation) | Database | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [database-recovery-orchestration](../scenarios/level-3-recovery/database-recovery-orchestration) | Database | 08-backup-recovery-lab | Lifecycle/domain priority: recovery data protection |
| level-3-recovery | [database-service-restoration](../scenarios/level-3-recovery/database-service-restoration) | Database | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [dns-service-restoration](../scenarios/level-3-recovery/dns-service-restoration) | DNS / Name Resolution | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [identity-access-remediation](../scenarios/level-3-recovery/identity-access-remediation) | Identity Operations | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [infrastructure-recovery-orchestration](../scenarios/level-3-recovery/infrastructure-recovery-orchestration) | General Infrastructure | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [inter-region-routing-recovery](../scenarios/level-3-recovery/inter-region-routing-recovery) | Network Operations | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-3-recovery | [kubernetes-control-plane-recovery](../scenarios/level-3-recovery/kubernetes-control-plane-recovery) | Kubernetes Operations | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-3-recovery | [kubernetes-node-recovery](../scenarios/level-3-recovery/kubernetes-node-recovery) | Kubernetes / Cluster | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-3-recovery | [kubernetes-service-recovery](../scenarios/level-3-recovery/kubernetes-service-recovery) | Kubernetes / Cluster | 04-container-runtime-lab | Domain priority: container/kubernetes/runtime |
| level-3-recovery | [load-balancer-recovery](../scenarios/level-3-recovery/load-balancer-recovery) | Load Balancing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-3-recovery | [network-failover-automation](../scenarios/level-3-recovery/network-failover-automation) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-3-recovery | [network-route-recovery-orchestration](../scenarios/level-3-recovery/network-route-recovery-orchestration) | Network / Routing | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-3-recovery | [platform-runtime-restoration](../scenarios/level-3-recovery/platform-runtime-restoration) | General Infrastructure | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [replication-recovery-orchestration](../scenarios/level-3-recovery/replication-recovery-orchestration) | Database / Replication | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [resource-rebalancing-automation](../scenarios/level-3-recovery/resource-rebalancing-automation) | General Infrastructure | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [server-service-recovery](../scenarios/level-3-recovery/server-service-recovery) | General Infrastructure | 01-linux-observability-lab | Domain priority: linux host observability |
| level-3-recovery | [service-mesh-traffic-restoration](../scenarios/level-3-recovery/service-mesh-traffic-restoration) | Service Mesh | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [storage-volume-recovery-automation](../scenarios/level-3-recovery/storage-volume-recovery-automation) | Storage Operations | 03-ansible-automation-lab | Lifecycle priority: level-3-recovery automation |
| level-3-recovery | [traffic-restoration-workflow](../scenarios/level-3-recovery/traffic-restoration-workflow) | Traffic / Flow | 08-backup-recovery-lab | Domain priority: backup/recovery |
| level-3-recovery | [virtual-machine-restoration](../scenarios/level-3-recovery/virtual-machine-restoration) | Virtual Machine | 05-kolla-openstack-lab | Domain priority: cloud/openstack/control-plane |
| level-3-recovery | [vpn-tunnel-recovery-automation](../scenarios/level-3-recovery/vpn-tunnel-recovery-automation) | Network / VPN | 02-network-routing-lab | Domain priority: network/routing/connectivity |
| level-4-resilience | [backup-resilience-validation](../scenarios/level-4-resilience/backup-resilience-validation) | Backup Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [change-resilience-coordination](../scenarios/level-4-resilience/change-resilience-coordination) | Change Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [configuration-resilience-validation](../scenarios/level-4-resilience/configuration-resilience-validation) | Configuration Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [control-plane-resilience](../scenarios/level-4-resilience/control-plane-resilience) | Platform Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [cross-region-data-survivability](../scenarios/level-4-resilience/cross-region-data-survivability) | General Infrastructure | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [cross-region-kubernetes-resilience](../scenarios/level-4-resilience/cross-region-kubernetes-resilience) | Kubernetes / Cluster | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [cross-region-network-resilience](../scenarios/level-4-resilience/cross-region-network-resilience) | Network / Routing | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [distributed-connectivity-survivability](../scenarios/level-4-resilience/distributed-connectivity-survivability) | General Infrastructure | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [distributed-database-failover](../scenarios/level-4-resilience/distributed-database-failover) | Database | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [distributed-platform-survivability](../scenarios/level-4-resilience/distributed-platform-survivability) | General Infrastructure | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [distributed-security-resilience](../scenarios/level-4-resilience/distributed-security-resilience) | Security / Telemetry | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [identity-failover-resilience](../scenarios/level-4-resilience/identity-failover-resilience) | Identity Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [identity-resilience-coordination](../scenarios/level-4-resilience/identity-resilience-coordination) | Identity / Access | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [inter-region-routing-resilience](../scenarios/level-4-resilience/inter-region-routing-resilience) | Network Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [kubernetes-platform-resilience](../scenarios/level-4-resilience/kubernetes-platform-resilience) | Kubernetes Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [multi-cluster-failover](../scenarios/level-4-resilience/multi-cluster-failover) | Cluster / Platform | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [multi-cluster-failover-coordination](../scenarios/level-4-resilience/multi-cluster-failover-coordination) | Cluster / Platform | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [multi-region-service-failover](../scenarios/level-4-resilience/multi-region-service-failover) | General Infrastructure | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [multi-region-service-failover-resilience](../scenarios/level-4-resilience/multi-region-service-failover-resilience) | General Infrastructure | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [multi-site-routing-failover](../scenarios/level-4-resilience/multi-site-routing-failover) | Network / Routing | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-4-resilience | [storage-replication-resilience](../scenarios/level-4-resilience/storage-replication-resilience) | Storage Operations | 09-resilience-failover-lab | Lifecycle priority: level-4-resilience |
| level-5-continuity | [enterprise-change-continuity](../scenarios/level-5-continuity/enterprise-change-continuity) | Continuity Operations | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-cloud-continuity](../scenarios/level-5-continuity/enterprise-cloud-continuity) | General Infrastructure | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-control-plane-continuity](../scenarios/level-5-continuity/enterprise-control-plane-continuity) | Continuity Operations | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-data-protection-continuity](../scenarios/level-5-continuity/enterprise-data-protection-continuity) | Continuity Operations | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-identity-continuity](../scenarios/level-5-continuity/enterprise-identity-continuity) | Continuity Operations | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-network-continuity](../scenarios/level-5-continuity/enterprise-network-continuity) | Network / Routing | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-operational-continuity](../scenarios/level-5-continuity/enterprise-operational-continuity) | General Infrastructure | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-platform-continuity](../scenarios/level-5-continuity/enterprise-platform-continuity) | General Infrastructure | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-security-continuity](../scenarios/level-5-continuity/enterprise-security-continuity) | Security / Telemetry | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |
| level-5-continuity | [enterprise-service-continuity-coordination](../scenarios/level-5-continuity/enterprise-service-continuity-coordination) | General Infrastructure | 10-governance-reporting-lab | Lifecycle priority: level-5-continuity |

## 7. Reviewer Interpretation

The mapping is intentionally implementation-oriented. A scenario may describe an operational capability at a higher level, while the mapped lab provides the concrete runtime boundary used to validate a representative implementation path.
