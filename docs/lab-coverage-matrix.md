# Lab Coverage Matrix

This document maps repository scenarios to implementation-oriented infrastructure operations labs.

Scenarios remain under /scenarios as lifecycle-aligned validation cases. Labs define implementation boundaries used to validate groups of scenarios through reusable modules, adapters, runtime utilities, and evidence workflows.

---

## Coverage Summary

Total mapped scenarios: 150

| Lab | Scenario Count |
|---|---:|
| [01-linux-observability-lab](../labs/01-linux-observability-lab/) | 8 |
| [02-network-routing-lab](../labs/02-network-routing-lab/) | 26 |
| [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) | 3 |
| [04-container-runtime-lab](../labs/04-container-runtime-lab/) | 12 |
| [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) | 6 |
| [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) | 6 |
| [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) | 16 |
| [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) | 9 |
| [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) | 9 |
| [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) | 55 |

---

## Scenario to Lab Mapping

| Scenario | Level | Domain | Lab |
|---|---|---|---|
| [Api Gateway Health Monitoring](../scenarios/level-1-visibility/api-gateway-health-monitoring/) | level-1-visibility | API / Gateway | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Application Runtime Monitoring](../scenarios/level-1-visibility/application-runtime-monitoring/) | level-1-visibility | Application Runtime | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Audit Log Monitoring](../scenarios/level-1-visibility/audit-log-monitoring/) | level-1-visibility | Audit / Logging | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Backup Job Monitoring](../scenarios/level-1-visibility/backup-job-monitoring/) | level-1-visibility | Backup / Recovery | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Bgp Neighbor Visibility](../scenarios/level-1-visibility/bgp-neighbor-visibility/) | level-1-visibility | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Certificate Expiration Monitoring](../scenarios/level-1-visibility/certificate-expiration-monitoring/) | level-1-visibility | TLS / Certificate | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cloud Instance Health Monitoring](../scenarios/level-1-visibility/cloud-instance-health-monitoring/) | level-1-visibility | Cloud Instance | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Compute Resource Monitoring](../scenarios/level-1-visibility/compute-resource-monitoring/) | level-1-visibility | Compute / Resource | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) |
| [Configuration Drift Monitoring](../scenarios/level-1-visibility/configuration-drift-monitoring/) | level-1-visibility | Configuration Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Container Runtime Visibility](../scenarios/level-1-visibility/container-runtime-visibility/) | level-1-visibility | Container / Runtime | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Control Plane Health Monitoring](../scenarios/level-1-visibility/control-plane-health-monitoring/) | level-1-visibility | Platform Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Database Health Monitoring](../scenarios/level-1-visibility/database-health-monitoring/) | level-1-visibility | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Database Replication Visibility](../scenarios/level-1-visibility/database-replication-visibility/) | level-1-visibility | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Database Runtime Visibility](../scenarios/level-1-visibility/database-runtime-visibility/) | level-1-visibility | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Dns Resolution Monitoring](../scenarios/level-1-visibility/dns-resolution-monitoring/) | level-1-visibility | DNS / Name Resolution | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Endpoint Reachability Monitoring](../scenarios/level-1-visibility/endpoint-reachability-monitoring/) | level-1-visibility | Endpoint | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Endpoint Security Visibility](../scenarios/level-1-visibility/endpoint-security-visibility/) | level-1-visibility | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Filesystem Health Visibility](../scenarios/level-1-visibility/filesystem-health-visibility/) | level-1-visibility | Filesystem | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Hardware Health Monitoring](../scenarios/level-1-visibility/hardware-health-monitoring/) | level-1-visibility | Hardware | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Hypervisor Resource Monitoring](../scenarios/level-1-visibility/hypervisor-resource-monitoring/) | level-1-visibility | Virtualization | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Identity Access Visibility](../scenarios/level-1-visibility/identity-access-visibility/) | level-1-visibility | Identity / Access | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Inter Region Connectivity Monitoring](../scenarios/level-1-visibility/inter-region-connectivity-monitoring/) | level-1-visibility | Network Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Kubernetes Cluster Health Monitoring](../scenarios/level-1-visibility/kubernetes-cluster-health-monitoring/) | level-1-visibility | Kubernetes / Cluster | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Kubernetes Cluster Visibility](../scenarios/level-1-visibility/kubernetes-cluster-visibility/) | level-1-visibility | Kubernetes / Cluster | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Load Balancer Health Monitoring](../scenarios/level-1-visibility/load-balancer-health-monitoring/) | level-1-visibility | Load Balancing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Message Queue Monitoring](../scenarios/level-1-visibility/message-queue-monitoring/) | level-1-visibility | Message Queue | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Microservice Health Monitoring](../scenarios/level-1-visibility/microservice-health-monitoring/) | level-1-visibility | Microservice | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Network Path Visibility](../scenarios/level-1-visibility/network-path-visibility/) | level-1-visibility | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Network Traffic Visibility](../scenarios/level-1-visibility/network-traffic-visibility/) | level-1-visibility | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Object Storage Health Monitoring](../scenarios/level-1-visibility/object-storage-health-monitoring/) | level-1-visibility | Storage | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Privileged Session Monitoring](../scenarios/level-1-visibility/privileged-session-monitoring/) | level-1-visibility | Privileged Access | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Process Health Monitoring](../scenarios/level-1-visibility/process-health-monitoring/) | level-1-visibility | Process / Service | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Security Event Monitoring](../scenarios/level-1-visibility/security-event-monitoring/) | level-1-visibility | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Security Policy Visibility](../scenarios/level-1-visibility/security-policy-visibility/) | level-1-visibility | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Security Telemetry Monitoring](../scenarios/level-1-visibility/security-telemetry-monitoring/) | level-1-visibility | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Service Health Visibility](../scenarios/level-1-visibility/service-health-visibility/) | level-1-visibility | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Service Mesh Traffic Visibility](../scenarios/level-1-visibility/service-mesh-traffic-visibility/) | level-1-visibility | Service Mesh | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Storage Capacity Monitoring](../scenarios/level-1-visibility/storage-capacity-monitoring/) | level-1-visibility | Storage | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Storage Latency Monitoring](../scenarios/level-1-visibility/storage-latency-monitoring/) | level-1-visibility | Storage | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [System Event Visibility](../scenarios/level-1-visibility/system-event-visibility/) | level-1-visibility | System Event | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Virtual Machine Health Monitoring](../scenarios/level-1-visibility/virtual-machine-health-monitoring/) | level-1-visibility | Virtual Machine | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Vpn Connectivity Monitoring](../scenarios/level-1-visibility/vpn-connectivity-monitoring/) | level-1-visibility | Network / VPN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Vpn Latency Visibility](../scenarios/level-1-visibility/vpn-latency-visibility/) | level-1-visibility | Network / VPN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Vpn Tunnel Health Monitoring](../scenarios/level-1-visibility/vpn-tunnel-health-monitoring/) | level-1-visibility | Network / VPN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Wan Link Monitoring](../scenarios/level-1-visibility/wan-link-monitoring/) | level-1-visibility | Network / WAN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Api Latency Correlation](../scenarios/level-2-correlation/api-latency-correlation/) | level-2-correlation | API / Service | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Authentication Anomaly Analysis](../scenarios/level-2-correlation/authentication-anomaly-analysis/) | level-2-correlation | Identity / Authentication | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Backup Failure Correlation](../scenarios/level-2-correlation/backup-failure-correlation/) | level-2-correlation | Backup / Recovery | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Change Impact Correlation](../scenarios/level-2-correlation/change-impact-correlation/) | level-2-correlation | Change Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cluster Resource Instability Analysis](../scenarios/level-2-correlation/cluster-resource-instability-analysis/) | level-2-correlation | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Compute Resource Correlation](../scenarios/level-2-correlation/compute-resource-correlation/) | level-2-correlation | Compute / Resource | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) |
| [Configuration Drift Correlation](../scenarios/level-2-correlation/configuration-drift-correlation/) | level-2-correlation | Configuration Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Container Dependency Analysis](../scenarios/level-2-correlation/container-dependency-analysis/) | level-2-correlation | Container / Runtime | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Control Plane Anomaly Correlation](../scenarios/level-2-correlation/control-plane-anomaly-correlation/) | level-2-correlation | Platform Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cross Domain Security Correlation](../scenarios/level-2-correlation/cross-domain-security-correlation/) | level-2-correlation | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Cross Region Network Anomaly Correlation](../scenarios/level-2-correlation/cross-region-network-anomaly-correlation/) | level-2-correlation | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Cross Server Failure Correlation](../scenarios/level-2-correlation/cross-server-failure-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cross Service Anomaly Correlation](../scenarios/level-2-correlation/cross-service-anomaly-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cross Service Database Dependency Analysis](../scenarios/level-2-correlation/cross-service-database-dependency-analysis/) | level-2-correlation | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Cross Site Network Correlation](../scenarios/level-2-correlation/cross-site-network-correlation/) | level-2-correlation | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Database Latency Correlation](../scenarios/level-2-correlation/database-latency-correlation/) | level-2-correlation | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Filesystem Failure Correlation](../scenarios/level-2-correlation/filesystem-failure-correlation/) | level-2-correlation | Filesystem | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Identity Risk Analysis](../scenarios/level-2-correlation/identity-risk-analysis/) | level-2-correlation | Identity / Access | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Infrastructure Anomaly Analysis](../scenarios/level-2-correlation/infrastructure-anomaly-analysis/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Inter Region Dependency Correlation](../scenarios/level-2-correlation/inter-region-dependency-correlation/) | level-2-correlation | Network Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Multi Region Latency Correlation](../scenarios/level-2-correlation/multi-region-latency-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Network Packet Loss Correlation](../scenarios/level-2-correlation/network-packet-loss-correlation/) | level-2-correlation | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Network Path Dependency Analysis](../scenarios/level-2-correlation/network-path-dependency-analysis/) | level-2-correlation | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Platform Dependency Correlation](../scenarios/level-2-correlation/platform-dependency-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Pod Failure Correlation](../scenarios/level-2-correlation/pod-failure-correlation/) | level-2-correlation | Container / Pod | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Privilege Escalation Correlation](../scenarios/level-2-correlation/privilege-escalation-correlation/) | level-2-correlation | Privileged Access | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Query Lock Analysis](../scenarios/level-2-correlation/query-lock-analysis/) | level-2-correlation | Database / Query | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Replication Failure Correlation](../scenarios/level-2-correlation/replication-failure-correlation/) | level-2-correlation | Database / Replication | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Resource Contention Correlation](../scenarios/level-2-correlation/resource-contention-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Routing Instability Correlation](../scenarios/level-2-correlation/routing-instability-correlation/) | level-2-correlation | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Runtime Instability Analysis](../scenarios/level-2-correlation/runtime-instability-analysis/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Security Anomaly Correlation](../scenarios/level-2-correlation/security-anomaly-correlation/) | level-2-correlation | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Security Policy Violation Analysis](../scenarios/level-2-correlation/security-policy-violation-analysis/) | level-2-correlation | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Service Dependency Correlation](../scenarios/level-2-correlation/service-dependency-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Service Mesh Latency Correlation](../scenarios/level-2-correlation/service-mesh-latency-correlation/) | level-2-correlation | Service Mesh | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Storage Io Instability Analysis](../scenarios/level-2-correlation/storage-io-instability-analysis/) | level-2-correlation | Storage | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Threat Propagation Analysis](../scenarios/level-2-correlation/threat-propagation-analysis/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Traffic Spike Correlation](../scenarios/level-2-correlation/traffic-spike-correlation/) | level-2-correlation | Traffic / Flow | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Virtualization Resource Correlation](../scenarios/level-2-correlation/virtualization-resource-correlation/) | level-2-correlation | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Vpn Latency Correlation](../scenarios/level-2-correlation/vpn-latency-correlation/) | level-2-correlation | Network / VPN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Vpn Tunnel Instability Analysis](../scenarios/level-2-correlation/vpn-tunnel-instability-analysis/) | level-2-correlation | Network / VPN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Api Service Recovery](../scenarios/level-3-recovery/api-service-recovery/) | level-3-recovery | API / Service | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Backup Restoration Automation](../scenarios/level-3-recovery/backup-restoration-automation/) | level-3-recovery | Backup / Recovery | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Certificate Renewal Automation](../scenarios/level-3-recovery/certificate-renewal-automation/) | level-3-recovery | Security Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Change Failure Rollback](../scenarios/level-3-recovery/change-failure-rollback/) | level-3-recovery | Change Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cloud Instance Recovery Automation](../scenarios/level-3-recovery/cloud-instance-recovery-automation/) | level-3-recovery | Cloud Instance | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Cluster Node Recovery Orchestration](../scenarios/level-3-recovery/cluster-node-recovery-orchestration/) | level-3-recovery | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Compute Failover Orchestration](../scenarios/level-3-recovery/compute-failover-orchestration/) | level-3-recovery | Compute / Resource | [03-ansible-automation-lab](../labs/03-ansible-automation-lab/) |
| [Configuration Rollback Automation](../scenarios/level-3-recovery/configuration-rollback-automation/) | level-3-recovery | Configuration Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Container Failover Automation](../scenarios/level-3-recovery/container-failover-automation/) | level-3-recovery | Container / Runtime | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Control Plane Recovery Orchestration](../scenarios/level-3-recovery/control-plane-recovery-orchestration/) | level-3-recovery | Platform Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Database Failover Automation](../scenarios/level-3-recovery/database-failover-automation/) | level-3-recovery | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Database Recovery Orchestration](../scenarios/level-3-recovery/database-recovery-orchestration/) | level-3-recovery | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Database Service Restoration](../scenarios/level-3-recovery/database-service-restoration/) | level-3-recovery | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Data Recovery Orchestration](../scenarios/level-3-recovery/data-recovery-orchestration/) | level-3-recovery | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Dns Service Restoration](../scenarios/level-3-recovery/dns-service-restoration/) | level-3-recovery | DNS / Name Resolution | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Identity Access Remediation](../scenarios/level-3-recovery/identity-access-remediation/) | level-3-recovery | Identity Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Infrastructure Recovery Orchestration](../scenarios/level-3-recovery/infrastructure-recovery-orchestration/) | level-3-recovery | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Inter Region Routing Recovery](../scenarios/level-3-recovery/inter-region-routing-recovery/) | level-3-recovery | Network Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Kubernetes Control Plane Recovery](../scenarios/level-3-recovery/kubernetes-control-plane-recovery/) | level-3-recovery | Kubernetes Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Kubernetes Node Recovery](../scenarios/level-3-recovery/kubernetes-node-recovery/) | level-3-recovery | Kubernetes / Cluster | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Kubernetes Service Recovery](../scenarios/level-3-recovery/kubernetes-service-recovery/) | level-3-recovery | Kubernetes / Cluster | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Load Balancer Recovery](../scenarios/level-3-recovery/load-balancer-recovery/) | level-3-recovery | Load Balancing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Network Failover Automation](../scenarios/level-3-recovery/network-failover-automation/) | level-3-recovery | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Network Route Recovery Orchestration](../scenarios/level-3-recovery/network-route-recovery-orchestration/) | level-3-recovery | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Platform Runtime Restoration](../scenarios/level-3-recovery/platform-runtime-restoration/) | level-3-recovery | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Replication Recovery Orchestration](../scenarios/level-3-recovery/replication-recovery-orchestration/) | level-3-recovery | Database / Replication | [08-backup-recovery-lab](../labs/08-backup-recovery-lab/) |
| [Resource Rebalancing Automation](../scenarios/level-3-recovery/resource-rebalancing-automation/) | level-3-recovery | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Server Service Recovery](../scenarios/level-3-recovery/server-service-recovery/) | level-3-recovery | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Service Mesh Traffic Restoration](../scenarios/level-3-recovery/service-mesh-traffic-restoration/) | level-3-recovery | Service Mesh | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Storage Volume Recovery Automation](../scenarios/level-3-recovery/storage-volume-recovery-automation/) | level-3-recovery | Storage Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Traffic Restoration Workflow](../scenarios/level-3-recovery/traffic-restoration-workflow/) | level-3-recovery | Traffic / Flow | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Virtual Machine Restoration](../scenarios/level-3-recovery/virtual-machine-restoration/) | level-3-recovery | Virtual Machine | [01-linux-observability-lab](../labs/01-linux-observability-lab/) |
| [Vpn Tunnel Recovery Automation](../scenarios/level-3-recovery/vpn-tunnel-recovery-automation/) | level-3-recovery | Network / VPN | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Backup Resilience Validation](../scenarios/level-4-resilience/backup-resilience-validation/) | level-4-resilience | Backup Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Change Resilience Coordination](../scenarios/level-4-resilience/change-resilience-coordination/) | level-4-resilience | Change Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Configuration Resilience Validation](../scenarios/level-4-resilience/configuration-resilience-validation/) | level-4-resilience | Configuration Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Control Plane Resilience](../scenarios/level-4-resilience/control-plane-resilience/) | level-4-resilience | Platform Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cross Region Data Survivability](../scenarios/level-4-resilience/cross-region-data-survivability/) | level-4-resilience | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Cross Region Kubernetes Resilience](../scenarios/level-4-resilience/cross-region-kubernetes-resilience/) | level-4-resilience | Kubernetes / Cluster | [04-container-runtime-lab](../labs/04-container-runtime-lab/) |
| [Cross Region Network Resilience](../scenarios/level-4-resilience/cross-region-network-resilience/) | level-4-resilience | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Distributed Connectivity Survivability](../scenarios/level-4-resilience/distributed-connectivity-survivability/) | level-4-resilience | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Distributed Database Failover](../scenarios/level-4-resilience/distributed-database-failover/) | level-4-resilience | Database | [09-resilience-failover-lab](../labs/09-resilience-failover-lab/) |
| [Distributed Platform Survivability](../scenarios/level-4-resilience/distributed-platform-survivability/) | level-4-resilience | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Distributed Security Resilience](../scenarios/level-4-resilience/distributed-security-resilience/) | level-4-resilience | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Identity Failover Resilience](../scenarios/level-4-resilience/identity-failover-resilience/) | level-4-resilience | Identity Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Identity Resilience Coordination](../scenarios/level-4-resilience/identity-resilience-coordination/) | level-4-resilience | Identity / Access | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Inter Region Routing Resilience](../scenarios/level-4-resilience/inter-region-routing-resilience/) | level-4-resilience | Network Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Kubernetes Platform Resilience](../scenarios/level-4-resilience/kubernetes-platform-resilience/) | level-4-resilience | Kubernetes Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Multi Cluster Failover](../scenarios/level-4-resilience/multi-cluster-failover/) | level-4-resilience | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Multi Cluster Failover Coordination](../scenarios/level-4-resilience/multi-cluster-failover-coordination/) | level-4-resilience | Cluster / Platform | [05-kolla-openstack-lab](../labs/05-kolla-openstack-lab/) |
| [Multi Region Service Failover](../scenarios/level-4-resilience/multi-region-service-failover/) | level-4-resilience | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Multi Region Service Failover Resilience](../scenarios/level-4-resilience/multi-region-service-failover-resilience/) | level-4-resilience | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Multi Site Routing Failover](../scenarios/level-4-resilience/multi-site-routing-failover/) | level-4-resilience | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Storage Replication Resilience](../scenarios/level-4-resilience/storage-replication-resilience/) | level-4-resilience | Storage Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Change Continuity](../scenarios/level-5-continuity/enterprise-change-continuity/) | level-5-continuity | Continuity Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Cloud Continuity](../scenarios/level-5-continuity/enterprise-cloud-continuity/) | level-5-continuity | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Control Plane Continuity](../scenarios/level-5-continuity/enterprise-control-plane-continuity/) | level-5-continuity | Continuity Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Data Protection Continuity](../scenarios/level-5-continuity/enterprise-data-protection-continuity/) | level-5-continuity | Continuity Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Identity Continuity](../scenarios/level-5-continuity/enterprise-identity-continuity/) | level-5-continuity | Continuity Operations | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Network Continuity](../scenarios/level-5-continuity/enterprise-network-continuity/) | level-5-continuity | Network / Routing | [02-network-routing-lab](../labs/02-network-routing-lab/) |
| [Enterprise Operational Continuity](../scenarios/level-5-continuity/enterprise-operational-continuity/) | level-5-continuity | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Platform Continuity](../scenarios/level-5-continuity/enterprise-platform-continuity/) | level-5-continuity | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
| [Enterprise Security Continuity](../scenarios/level-5-continuity/enterprise-security-continuity/) | level-5-continuity | Security / Telemetry | [07-logging-correlation-lab](../labs/07-logging-correlation-lab/) |
| [Enterprise Service Continuity Coordination](../scenarios/level-5-continuity/enterprise-service-continuity-coordination/) | level-5-continuity | General Infrastructure | [10-governance-reporting-lab](../labs/10-governance-reporting-lab/) |
