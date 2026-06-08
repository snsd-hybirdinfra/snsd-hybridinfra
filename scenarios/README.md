# Scenario Inventory

This directory contains lifecycle-aligned infrastructure operations scenarios for the SNSD Hybrid Infrastructure portfolio.

The scenario set is designed to demonstrate operational breadth across visibility, correlation, recovery, resilience, and continuity workflows. Scenarios are organized by lifecycle maturity level rather than by a single representative incident chain.

---

## Inventory Summary

- Total scenarios: 150
- Level 1 - Visibility: 45
- Level 2 - Correlation: 41
- Level 3 - Recovery: 33
- Level 4 - Resilience: 21
- Level 5 - Continuity: 10

---

## Lifecycle Coverage

| Level | Scenario Count | Operational Focus |
|---|---:|---|
| Level 1 - Visibility | 45 | Signal collection, health visibility, and operational state exposure. |
| Level 2 - Correlation | 41 | Dependency analysis, symptom correlation, and impact reasoning. |
| Level 3 - Recovery | 33 | Controlled recovery execution, automation workflow, and restoration validation. |
| Level 4 - Resilience | 21 | Distributed failure-domain coordination and survivability validation. |
| Level 5 - Continuity | 10 | Enterprise continuity governance, readiness validation, and operational reporting. |

---

## Domain Coverage

| Domain | Scenario Count |
|---|---:|
| General Infrastructure | 25 |
| Network / Routing | 16 |
| Database | 9 |
| Security / Telemetry | 9 |
| Configuration / Change | 8 |
| Kubernetes / Cluster | 7 |
| Identity / Access | 6 |
| Network / VPN | 6 |
| Control Plane | 5 |
| Storage | 5 |
| Backup / Recovery | 4 |
| Cluster / Platform | 4 |
| Compute / Resource | 3 |
| Container / Runtime | 3 |
| Database / Replication | 3 |
| Service Mesh | 3 |
| API / Service | 2 |
| Cloud Instance | 2 |
| DNS / Name Resolution | 2 |
| Filesystem | 2 |
| Load Balancing | 2 |
| Privileged Access | 2 |
| TLS / Certificate | 2 |
| Traffic / Flow | 2 |
| Virtual Machine | 2 |
| API / Gateway | 1 |
| Application Runtime | 1 |
| Audit / Logging | 1 |
| Container / Pod | 1 |
| Data Protection | 1 |
| Database / Query | 1 |
| Endpoint | 1 |
| Hardware | 1 |
| Identity / Authentication | 1 |
| Message Queue | 1 |
| Microservice | 1 |
| Multi-Region Operations | 1 |
| Network / WAN | 1 |
| Process / Service | 1 |
| System Event | 1 |
| Virtualization | 1 |

---

## Scenario Index

### Level 1 - Visibility

Signal collection, health visibility, and operational state exposure.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Api Gateway Health Monitoring](./level-1-visibility/api-gateway-health-monitoring/README.md) | API / Gateway | draft | 0 |
| [Application Runtime Monitoring](./level-1-visibility/application-runtime-monitoring/README.md) | Application Runtime | draft | 0 |
| [Audit Log Monitoring](./level-1-visibility/audit-log-monitoring/README.md) | Audit / Logging | draft | 0 |
| [Backup Job Monitoring](./level-1-visibility/backup-job-monitoring/README.md) | Backup / Recovery | draft | 1 |
| [Bgp Neighbor Visibility](./level-1-visibility/bgp-neighbor-visibility/README.md) | Network / Routing | draft | 3 |
| [Certificate Expiration Monitoring](./level-1-visibility/certificate-expiration-monitoring/README.md) | TLS / Certificate | draft | 0 |
| [Cloud Instance Health Monitoring](./level-1-visibility/cloud-instance-health-monitoring/README.md) | Cloud Instance | draft | 0 |
| [Compute Resource Monitoring](./level-1-visibility/compute-resource-monitoring/README.md) | Compute / Resource | draft | 1 |
| [Configuration Drift Monitoring](./level-1-visibility/configuration-drift-monitoring/README.md) | Configuration / Change | draft | 3 |
| [Container Runtime Visibility](./level-1-visibility/container-runtime-visibility/README.md) | Container / Runtime | draft | 1 |
| [Control Plane Health Monitoring](./level-1-visibility/control-plane-health-monitoring/README.md) | Control Plane | draft | 3 |
| [Database Health Monitoring](./level-1-visibility/database-health-monitoring/README.md) | Database | draft | 3 |
| [Database Replication Visibility](./level-1-visibility/database-replication-visibility/README.md) | Database | draft | 3 |
| [Database Runtime Visibility](./level-1-visibility/database-runtime-visibility/README.md) | Database | draft | 3 |
| [Dns Resolution Monitoring](./level-1-visibility/dns-resolution-monitoring/README.md) | DNS / Name Resolution | draft | 0 |
| [Endpoint Reachability Monitoring](./level-1-visibility/endpoint-reachability-monitoring/README.md) | Endpoint | draft | 0 |
| [Endpoint Security Visibility](./level-1-visibility/endpoint-security-visibility/README.md) | Security / Telemetry | draft | 4 |
| [Filesystem Health Visibility](./level-1-visibility/filesystem-health-visibility/README.md) | Filesystem | draft | 1 |
| [Hardware Health Monitoring](./level-1-visibility/hardware-health-monitoring/README.md) | Hardware | draft | 0 |
| [Hypervisor Resource Monitoring](./level-1-visibility/hypervisor-resource-monitoring/README.md) | Virtualization | draft | 0 |
| [Identity Access Visibility](./level-1-visibility/identity-access-visibility/README.md) | Identity / Access | draft | 1 |
| [Inter Region Connectivity Monitoring](./level-1-visibility/inter-region-connectivity-monitoring/README.md) | Network / Routing | draft | 3 |
| [Kubernetes Cluster Health Monitoring](./level-1-visibility/kubernetes-cluster-health-monitoring/README.md) | Kubernetes / Cluster | draft | 1 |
| [Kubernetes Cluster Visibility](./level-1-visibility/kubernetes-cluster-visibility/README.md) | Kubernetes / Cluster | draft | 1 |
| [Load Balancer Health Monitoring](./level-1-visibility/load-balancer-health-monitoring/README.md) | Load Balancing | draft | 0 |
| [Message Queue Monitoring](./level-1-visibility/message-queue-monitoring/README.md) | Message Queue | draft | 0 |
| [Microservice Health Monitoring](./level-1-visibility/microservice-health-monitoring/README.md) | Microservice | draft | 0 |
| [Network Path Visibility](./level-1-visibility/network-path-visibility/README.md) | Network / Routing | draft | 3 |
| [Network Traffic Visibility](./level-1-visibility/network-traffic-visibility/README.md) | Network / Routing | draft | 3 |
| [Object Storage Health Monitoring](./level-1-visibility/object-storage-health-monitoring/README.md) | Storage | draft | 3 |
| [Privileged Session Monitoring](./level-1-visibility/privileged-session-monitoring/README.md) | Privileged Access | draft | 1 |
| [Process Health Monitoring](./level-1-visibility/process-health-monitoring/README.md) | Process / Service | draft | 0 |
| [Security Event Monitoring](./level-1-visibility/security-event-monitoring/README.md) | Security / Telemetry | draft | 4 |
| [Security Policy Visibility](./level-1-visibility/security-policy-visibility/README.md) | Security / Telemetry | draft | 4 |
| [Security Telemetry Monitoring](./level-1-visibility/security-telemetry-monitoring/README.md) | Security / Telemetry | draft | 4 |
| [Service Health Visibility](./level-1-visibility/service-health-visibility/README.md) | General Infrastructure | draft | 1 |
| [Service Mesh Traffic Visibility](./level-1-visibility/service-mesh-traffic-visibility/README.md) | Service Mesh | draft | 1 |
| [Storage Capacity Monitoring](./level-1-visibility/storage-capacity-monitoring/README.md) | Storage | draft | 3 |
| [Storage Latency Monitoring](./level-1-visibility/storage-latency-monitoring/README.md) | Storage | draft | 3 |
| [System Event Visibility](./level-1-visibility/system-event-visibility/README.md) | System Event | draft | 0 |
| [Virtual Machine Health Monitoring](./level-1-visibility/virtual-machine-health-monitoring/README.md) | Virtual Machine | draft | 0 |
| [Vpn Connectivity Monitoring](./level-1-visibility/vpn-connectivity-monitoring/README.md) | Network / VPN | draft | 3 |
| [Vpn Latency Visibility](./level-1-visibility/vpn-latency-visibility/README.md) | Network / VPN | draft | 3 |
| [Vpn Tunnel Health Monitoring](./level-1-visibility/vpn-tunnel-health-monitoring/README.md) | Network / VPN | draft | 3 |
| [Wan Link Monitoring](./level-1-visibility/wan-link-monitoring/README.md) | Network / WAN | draft | 0 |

### Level 2 - Correlation

Dependency analysis, symptom correlation, and impact reasoning.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Api Latency Correlation](./level-2-correlation/api-latency-correlation/README.md) | API / Service | draft | 1 |
| [Authentication Anomaly Analysis](./level-2-correlation/authentication-anomaly-analysis/README.md) | Identity / Authentication | draft | 0 |
| [Backup Failure Correlation](./level-2-correlation/backup-failure-correlation/README.md) | Backup / Recovery | draft | 2 |
| [Change Impact Correlation](./level-2-correlation/change-impact-correlation/README.md) | Configuration / Change | draft | 5 |
| [Cluster Resource Instability Analysis](./level-2-correlation/cluster-resource-instability-analysis/README.md) | Cluster / Platform | draft | 1 |
| [Compute Resource Correlation](./level-2-correlation/compute-resource-correlation/README.md) | Compute / Resource | draft | 2 |
| [Configuration Drift Correlation](./level-2-correlation/configuration-drift-correlation/README.md) | Configuration / Change | draft | 5 |
| [Container Dependency Analysis](./level-2-correlation/container-dependency-analysis/README.md) | Container / Runtime | draft | 2 |
| [Control Plane Anomaly Correlation](./level-2-correlation/control-plane-anomaly-correlation/README.md) | Control Plane | draft | 5 |
| [Cross Domain Security Correlation](./level-2-correlation/cross-domain-security-correlation/README.md) | Security / Telemetry | draft | 3 |
| [Cross Region Network Anomaly Correlation](./level-2-correlation/cross-region-network-anomaly-correlation/README.md) | Network / Routing | draft | 5 |
| [Cross Server Failure Correlation](./level-2-correlation/cross-server-failure-correlation/README.md) | General Infrastructure | draft | 5 |
| [Cross Service Anomaly Correlation](./level-2-correlation/cross-service-anomaly-correlation/README.md) | General Infrastructure | draft | 5 |
| [Cross Service Database Dependency Analysis](./level-2-correlation/cross-service-database-dependency-analysis/README.md) | Database | draft | 3 |
| [Cross Site Network Correlation](./level-2-correlation/cross-site-network-correlation/README.md) | Network / Routing | draft | 5 |
| [Database Latency Correlation](./level-2-correlation/database-latency-correlation/README.md) | Database | draft | 3 |
| [Filesystem Failure Correlation](./level-2-correlation/filesystem-failure-correlation/README.md) | Filesystem | draft | 1 |
| [Identity Risk Analysis](./level-2-correlation/identity-risk-analysis/README.md) | Identity / Access | draft | 1 |
| [Infrastructure Anomaly Analysis](./level-2-correlation/infrastructure-anomaly-analysis/README.md) | General Infrastructure | draft | 5 |
| [Inter Region Dependency Correlation](./level-2-correlation/inter-region-dependency-correlation/README.md) | Multi-Region Operations | draft | 5 |
| [Multi Region Latency Correlation](./level-2-correlation/multi-region-latency-correlation/README.md) | General Infrastructure | draft | 5 |
| [Network Packet Loss Correlation](./level-2-correlation/network-packet-loss-correlation/README.md) | Network / Routing | draft | 5 |
| [Network Path Dependency Analysis](./level-2-correlation/network-path-dependency-analysis/README.md) | Network / Routing | draft | 5 |
| [Platform Dependency Correlation](./level-2-correlation/platform-dependency-correlation/README.md) | General Infrastructure | draft | 5 |
| [Pod Failure Correlation](./level-2-correlation/pod-failure-correlation/README.md) | Container / Pod | draft | 0 |
| [Privilege Escalation Correlation](./level-2-correlation/privilege-escalation-correlation/README.md) | Privileged Access | draft | 1 |
| [Query Lock Analysis](./level-2-correlation/query-lock-analysis/README.md) | Database / Query | draft | 0 |
| [Replication Failure Correlation](./level-2-correlation/replication-failure-correlation/README.md) | Database / Replication | draft | 1 |
| [Resource Contention Correlation](./level-2-correlation/resource-contention-correlation/README.md) | General Infrastructure | draft | 5 |
| [Routing Instability Correlation](./level-2-correlation/routing-instability-correlation/README.md) | Network / Routing | draft | 5 |
| [Runtime Instability Analysis](./level-2-correlation/runtime-instability-analysis/README.md) | General Infrastructure | draft | 5 |
| [Security Anomaly Correlation](./level-2-correlation/security-anomaly-correlation/README.md) | Security / Telemetry | draft | 3 |
| [Security Policy Violation Analysis](./level-2-correlation/security-policy-violation-analysis/README.md) | Security / Telemetry | draft | 3 |
| [Service Dependency Correlation](./level-2-correlation/service-dependency-correlation/README.md) | General Infrastructure | draft | 5 |
| [Service Mesh Latency Correlation](./level-2-correlation/service-mesh-latency-correlation/README.md) | Service Mesh | draft | 2 |
| [Storage Io Instability Analysis](./level-2-correlation/storage-io-instability-analysis/README.md) | Storage | draft | 1 |
| [Threat Propagation Analysis](./level-2-correlation/threat-propagation-analysis/README.md) | General Infrastructure | draft | 5 |
| [Traffic Spike Correlation](./level-2-correlation/traffic-spike-correlation/README.md) | Traffic / Flow | draft | 1 |
| [Virtualization Resource Correlation](./level-2-correlation/virtualization-resource-correlation/README.md) | General Infrastructure | draft | 5 |
| [Vpn Latency Correlation](./level-2-correlation/vpn-latency-correlation/README.md) | Network / VPN | draft | 3 |
| [Vpn Tunnel Instability Analysis](./level-2-correlation/vpn-tunnel-instability-analysis/README.md) | Network / VPN | draft | 3 |

### Level 3 - Recovery

Controlled recovery execution, automation workflow, and restoration validation.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Api Service Recovery](./level-3-recovery/api-service-recovery/README.md) | API / Service | draft | 1 |
| [Backup Restoration Automation](./level-3-recovery/backup-restoration-automation/README.md) | Backup / Recovery | draft | 1 |
| [Certificate Renewal Automation](./level-3-recovery/certificate-renewal-automation/README.md) | TLS / Certificate | draft | 5 |
| [Change Failure Rollback](./level-3-recovery/change-failure-rollback/README.md) | Configuration / Change | draft | 5 |
| [Cloud Instance Recovery Automation](./level-3-recovery/cloud-instance-recovery-automation/README.md) | Cloud Instance | draft | 0 |
| [Cluster Node Recovery Orchestration](./level-3-recovery/cluster-node-recovery-orchestration/README.md) | Cluster / Platform | draft | 2 |
| [Compute Failover Orchestration](./level-3-recovery/compute-failover-orchestration/README.md) | Compute / Resource | draft | 1 |
| [Configuration Rollback Automation](./level-3-recovery/configuration-rollback-automation/README.md) | Configuration / Change | draft | 5 |
| [Container Failover Automation](./level-3-recovery/container-failover-automation/README.md) | Container / Runtime | draft | 1 |
| [Control Plane Recovery Orchestration](./level-3-recovery/control-plane-recovery-orchestration/README.md) | Control Plane | draft | 5 |
| [Data Recovery Orchestration](./level-3-recovery/data-recovery-orchestration/README.md) | General Infrastructure | draft | 5 |
| [Database Failover Automation](./level-3-recovery/database-failover-automation/README.md) | Database | draft | 4 |
| [Database Recovery Orchestration](./level-3-recovery/database-recovery-orchestration/README.md) | Database | draft | 4 |
| [Database Service Restoration](./level-3-recovery/database-service-restoration/README.md) | Database | draft | 4 |
| [Dns Service Restoration](./level-3-recovery/dns-service-restoration/README.md) | DNS / Name Resolution | draft | 0 |
| [Identity Access Remediation](./level-3-recovery/identity-access-remediation/README.md) | Identity / Access | draft | 5 |
| [Infrastructure Recovery Orchestration](./level-3-recovery/infrastructure-recovery-orchestration/README.md) | General Infrastructure | draft | 5 |
| [Inter Region Routing Recovery](./level-3-recovery/inter-region-routing-recovery/README.md) | Network / Routing | draft | 5 |
| [Kubernetes Control Plane Recovery](./level-3-recovery/kubernetes-control-plane-recovery/README.md) | Kubernetes / Cluster | draft | 5 |
| [Kubernetes Node Recovery](./level-3-recovery/kubernetes-node-recovery/README.md) | Kubernetes / Cluster | draft | 2 |
| [Kubernetes Service Recovery](./level-3-recovery/kubernetes-service-recovery/README.md) | Kubernetes / Cluster | draft | 2 |
| [Load Balancer Recovery](./level-3-recovery/load-balancer-recovery/README.md) | Load Balancing | draft | 0 |
| [Network Failover Automation](./level-3-recovery/network-failover-automation/README.md) | Network / Routing | draft | 3 |
| [Network Route Recovery Orchestration](./level-3-recovery/network-route-recovery-orchestration/README.md) | Network / Routing | draft | 3 |
| [Platform Runtime Restoration](./level-3-recovery/platform-runtime-restoration/README.md) | General Infrastructure | draft | 5 |
| [Replication Recovery Orchestration](./level-3-recovery/replication-recovery-orchestration/README.md) | Database / Replication | draft | 1 |
| [Resource Rebalancing Automation](./level-3-recovery/resource-rebalancing-automation/README.md) | General Infrastructure | draft | 5 |
| [Server Service Recovery](./level-3-recovery/server-service-recovery/README.md) | General Infrastructure | draft | 5 |
| [Service Mesh Traffic Restoration](./level-3-recovery/service-mesh-traffic-restoration/README.md) | Service Mesh | draft | 1 |
| [Storage Volume Recovery Automation](./level-3-recovery/storage-volume-recovery-automation/README.md) | Storage | draft | 5 |
| [Traffic Restoration Workflow](./level-3-recovery/traffic-restoration-workflow/README.md) | Traffic / Flow | draft | 1 |
| [Virtual Machine Restoration](./level-3-recovery/virtual-machine-restoration/README.md) | Virtual Machine | draft | 0 |
| [Vpn Tunnel Recovery Automation](./level-3-recovery/vpn-tunnel-recovery-automation/README.md) | Network / VPN | draft | 1 |

### Level 4 - Resilience

Distributed failure-domain coordination and survivability validation.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Backup Resilience Validation](./level-4-resilience/backup-resilience-validation/README.md) | Backup / Recovery | draft | 5 |
| [Change Resilience Coordination](./level-4-resilience/change-resilience-coordination/README.md) | Configuration / Change | draft | 5 |
| [Configuration Resilience Validation](./level-4-resilience/configuration-resilience-validation/README.md) | Configuration / Change | draft | 5 |
| [Control Plane Resilience](./level-4-resilience/control-plane-resilience/README.md) | Control Plane | draft | 5 |
| [Cross Region Data Survivability](./level-4-resilience/cross-region-data-survivability/README.md) | General Infrastructure | draft | 5 |
| [Cross Region Kubernetes Resilience](./level-4-resilience/cross-region-kubernetes-resilience/README.md) | Kubernetes / Cluster | draft | 1 |
| [Cross Region Network Resilience](./level-4-resilience/cross-region-network-resilience/README.md) | Network / Routing | draft | 3 |
| [Distributed Connectivity Survivability](./level-4-resilience/distributed-connectivity-survivability/README.md) | General Infrastructure | draft | 5 |
| [Distributed Database Failover](./level-4-resilience/distributed-database-failover/README.md) | Database | draft | 1 |
| [Distributed Platform Survivability](./level-4-resilience/distributed-platform-survivability/README.md) | General Infrastructure | draft | 5 |
| [Distributed Security Resilience](./level-4-resilience/distributed-security-resilience/README.md) | Security / Telemetry | draft | 1 |
| [Identity Failover Resilience](./level-4-resilience/identity-failover-resilience/README.md) | Identity / Access | draft | 5 |
| [Identity Resilience Coordination](./level-4-resilience/identity-resilience-coordination/README.md) | Identity / Access | draft | 0 |
| [Inter Region Routing Resilience](./level-4-resilience/inter-region-routing-resilience/README.md) | Network / Routing | draft | 5 |
| [Kubernetes Platform Resilience](./level-4-resilience/kubernetes-platform-resilience/README.md) | Kubernetes / Cluster | draft | 5 |
| [Multi Cluster Failover](./level-4-resilience/multi-cluster-failover/README.md) | Cluster / Platform | draft | 2 |
| [Multi Cluster Failover Coordination](./level-4-resilience/multi-cluster-failover-coordination/README.md) | Cluster / Platform | draft | 2 |
| [Multi Region Service Failover](./level-4-resilience/multi-region-service-failover/README.md) | General Infrastructure | draft | 5 |
| [Multi Region Service Failover Resilience](./level-4-resilience/multi-region-service-failover-resilience/README.md) | General Infrastructure | draft | 5 |
| [Multi Site Routing Failover](./level-4-resilience/multi-site-routing-failover/README.md) | Network / Routing | draft | 3 |
| [Storage Replication Resilience](./level-4-resilience/storage-replication-resilience/README.md) | Database / Replication | draft | 5 |

### Level 5 - Continuity

Enterprise continuity governance, readiness validation, and operational reporting.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Enterprise Change Continuity](./level-5-continuity/enterprise-change-continuity/README.md) | Configuration / Change | draft | 4 |
| [Enterprise Cloud Continuity](./level-5-continuity/enterprise-cloud-continuity/README.md) | General Infrastructure | draft | 4 |
| [Enterprise Control Plane Continuity](./level-5-continuity/enterprise-control-plane-continuity/README.md) | Control Plane | draft | 4 |
| [Enterprise Data Protection Continuity](./level-5-continuity/enterprise-data-protection-continuity/README.md) | Data Protection | draft | 4 |
| [Enterprise Identity Continuity](./level-5-continuity/enterprise-identity-continuity/README.md) | Identity / Access | draft | 4 |
| [Enterprise Network Continuity](./level-5-continuity/enterprise-network-continuity/README.md) | Network / Routing | draft | 1 |
| [Enterprise Operational Continuity](./level-5-continuity/enterprise-operational-continuity/README.md) | General Infrastructure | draft | 4 |
| [Enterprise Platform Continuity](./level-5-continuity/enterprise-platform-continuity/README.md) | General Infrastructure | draft | 4 |
| [Enterprise Security Continuity](./level-5-continuity/enterprise-security-continuity/README.md) | Security / Telemetry | draft | 1 |
| [Enterprise Service Continuity Coordination](./level-5-continuity/enterprise-service-continuity-coordination/README.md) | General Infrastructure | draft | 4 |

---

## Scenario Artifact Standard

Each scenario is expected to include the following reviewer-readable artifacts:

    metadata.yaml
    README.md
    diagrams/operational-poster.svg
    diagrams/operational-poster.png
    evidence/generated/summary.md
    evidence/generated/execution-evidence.md
    evidence/generated/validation-evidence.md
    evidence/generated/artifact-manifest.json
    evidence/generated/artifact-checksums.json

---

## Validation Reports

- [Repository Quality Check](../reports/repository-quality-check.md)
- [Related Scenarios Generation Report](../reports/related-scenarios-generation-report.md)

---

## Summary

The scenario inventory provides lifecycle-based operational coverage across infrastructure domains. It supports portfolio review by showing scenario distribution, operational focus, domain coverage, and artifact consistency from one index page.
