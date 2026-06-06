# Operational Scenarios

This directory contains lifecycle-based infrastructure operations scenarios.

Scenarios are organized by operational maturity level, from visibility and detection through correlation, recovery, resilience, and continuity governance.

---

## Scenario Lifecycle

| Level | Purpose |
|---|---|
| Level 1 - Visibility | Monitoring, telemetry, health visibility, and detection evidence |
| Level 2 - Correlation | Dependency analysis, signal correlation, and impact reasoning |
| Level 3 - Recovery | Recovery workflow, automation, restoration, and validation |
| Level 4 - Resilience | Distributed failover, survivability, and multi-site resilience |
| Level 5 - Continuity | Enterprise continuity, governance, and executive reporting |

---

## Level 1 - Visibility

Scenario count: **42**

| Scenario | Domain | Type | Target Resource |
|---|---|---|---|
| [Api Gateway Health Monitoring](level-1-visibility/api-gateway-health-monitoring/) | API / Gateway | Visibility / Monitoring | API gateway, route, upstream service, client request path |
| [Application Runtime Monitoring](level-1-visibility/application-runtime-monitoring/) | Application Runtime | Visibility / Monitoring | application process, runtime endpoint, container or VM-hosted service |
| [Audit Log Monitoring](level-1-visibility/audit-log-monitoring/) | Audit / Logging | Visibility / Monitoring | audit log source, event stream, policy record, evidence trail |
| [Backup Job Monitoring](level-1-visibility/backup-job-monitoring/) | Backup / Recovery | Visibility / Monitoring | backup job, backup scheduler, protected workload, backup repository, recovery point |
| [Bgp Neighbor Visibility](level-1-visibility/bgp-neighbor-visibility/) | Network / Routing | Visibility / Monitoring | BGP neighbor, router, route table, WAN path |
| [Certificate Expiration Monitoring](level-1-visibility/certificate-expiration-monitoring/) | TLS / Certificate | Visibility / Monitoring | TLS certificate, domain endpoint, certificate chain, renewal process |
| [Cloud Instance Health Monitoring](level-1-visibility/cloud-instance-health-monitoring/) | Cloud Instance | Visibility / Monitoring | cloud instance, VM, host resource, instance status check |
| [Compute Resource Monitoring](level-1-visibility/compute-resource-monitoring/) | Compute / Resource | Visibility / Monitoring | compute node, instance, CPU, memory, disk, runtime host |
| [Container Runtime Visibility](level-1-visibility/container-runtime-visibility/) | Container / Runtime | Visibility / Monitoring | container runtime, pod, workload, node, image runtime |
| [Database Health Monitoring](level-1-visibility/database-health-monitoring/) | Database | Visibility / Monitoring | database instance, query workload, replication channel, storage backend |
| [Database Replication Visibility](level-1-visibility/database-replication-visibility/) | Database | Visibility / Monitoring | database instance, query workload, replication channel, storage backend |
| [Database Runtime Visibility](level-1-visibility/database-runtime-visibility/) | Database | Visibility / Monitoring | database instance, query workload, replication channel, storage backend |
| [Dns Resolution Monitoring](level-1-visibility/dns-resolution-monitoring/) | DNS / Name Resolution | Visibility / Monitoring | DNS resolver, DNS record, query path, client resolution flow |
| [Endpoint Reachability Monitoring](level-1-visibility/endpoint-reachability-monitoring/) | Endpoint | Visibility / Monitoring | endpoint host, reachability path, agent signal, service access point |
| [Endpoint Security Visibility](level-1-visibility/endpoint-security-visibility/) | Security / Telemetry | Visibility / Monitoring | security event, policy control, endpoint signal, audit source |
| [Filesystem Health Visibility](level-1-visibility/filesystem-health-visibility/) | Filesystem | Visibility / Monitoring | filesystem, mount point, volume, inode, disk path |
| [Hardware Health Monitoring](level-1-visibility/hardware-health-monitoring/) | Hardware | Visibility / Monitoring | physical host, hardware sensor, disk, power, fan, health controller |
| [Hypervisor Resource Monitoring](level-1-visibility/hypervisor-resource-monitoring/) | Virtualization | Visibility / Monitoring | hypervisor, VM host, resource pool, guest workload |
| [Identity Access Visibility](level-1-visibility/identity-access-visibility/) | Identity / Access | Visibility / Monitoring | identity provider, access policy, authentication flow, account state |
| [Kubernetes Cluster Health Monitoring](level-1-visibility/kubernetes-cluster-health-monitoring/) | Kubernetes / Cluster | Visibility / Monitoring | Kubernetes cluster, node, pod, control plane, service object |
| [Kubernetes Cluster Visibility](level-1-visibility/kubernetes-cluster-visibility/) | Kubernetes / Cluster | Visibility / Monitoring | Kubernetes cluster, node, pod, control plane, service object |
| [Load Balancer Health Monitoring](level-1-visibility/load-balancer-health-monitoring/) | Load Balancing | Visibility / Monitoring | load balancer, listener, target group, backend service |
| [Message Queue Monitoring](level-1-visibility/message-queue-monitoring/) | Message Queue | Visibility / Monitoring | message broker, queue depth, consumer group, producer flow |
| [Microservice Health Monitoring](level-1-visibility/microservice-health-monitoring/) | Microservice | Visibility / Monitoring | microservice, service endpoint, dependency call path, runtime signal |
| [Network Path Visibility](level-1-visibility/network-path-visibility/) | Network / Routing | Visibility / Monitoring | network path, route, interface, traffic flow |
| [Network Traffic Visibility](level-1-visibility/network-traffic-visibility/) | Network / Routing | Visibility / Monitoring | network path, route, interface, traffic flow |
| [Object Storage Health Monitoring](level-1-visibility/object-storage-health-monitoring/) | Storage | Visibility / Monitoring | storage volume, storage backend, object store, I/O path |
| [Privileged Session Monitoring](level-1-visibility/privileged-session-monitoring/) | Privileged Access | Visibility / Monitoring | privileged session, admin account, access control, audit source |
| [Process Health Monitoring](level-1-visibility/process-health-monitoring/) | Process / Service | Visibility / Monitoring | process, service runtime, OS host, health signal |
| [Security Event Monitoring](level-1-visibility/security-event-monitoring/) | Security / Telemetry | Visibility / Monitoring | security event, policy control, endpoint signal, audit source |
| [Security Policy Visibility](level-1-visibility/security-policy-visibility/) | Security / Telemetry | Visibility / Monitoring | security event, policy control, endpoint signal, audit source |
| [Security Telemetry Monitoring](level-1-visibility/security-telemetry-monitoring/) | Security / Telemetry | Visibility / Monitoring | security event, policy control, endpoint signal, audit source |
| [Service Health Visibility](level-1-visibility/service-health-visibility/) | General Infrastructure | Visibility / Monitoring | infrastructure component, telemetry source, operational dependency |
| [Service Mesh Traffic Visibility](level-1-visibility/service-mesh-traffic-visibility/) | Service Mesh | Visibility / Monitoring | service mesh route, sidecar proxy, service dependency, traffic policy |
| [Storage Capacity Monitoring](level-1-visibility/storage-capacity-monitoring/) | Storage | Visibility / Monitoring | storage volume, storage backend, object store, I/O path |
| [Storage Latency Monitoring](level-1-visibility/storage-latency-monitoring/) | Storage | Visibility / Monitoring | storage volume, storage backend, object store, I/O path |
| [System Event Visibility](level-1-visibility/system-event-visibility/) | System Event | Visibility / Monitoring | system event log, OS runtime, service state, host signal |
| [Virtual Machine Health Monitoring](level-1-visibility/virtual-machine-health-monitoring/) | Virtual Machine | Visibility / Monitoring | virtual machine, hypervisor, guest OS, compute host |
| [Vpn Connectivity Monitoring](level-1-visibility/vpn-connectivity-monitoring/) | Network / VPN | Visibility / Monitoring | VPN tunnel, VPN gateway, remote endpoint, routing path |
| [Vpn Latency Visibility](level-1-visibility/vpn-latency-visibility/) | Network / VPN | Visibility / Monitoring | VPN tunnel, VPN gateway, remote endpoint, routing path |
| [Vpn Tunnel Health Monitoring](level-1-visibility/vpn-tunnel-health-monitoring/) | Network / VPN | Visibility / Monitoring | VPN tunnel, VPN gateway, remote endpoint, routing path |
| [Wan Link Monitoring](level-1-visibility/wan-link-monitoring/) | Network / WAN | Visibility / Monitoring | WAN link, edge router, remote site, network path |

---

## Level 2 - Correlation

Scenario count: **37**

| Scenario | Domain | Type | Target Resource |
|---|---|---|---|
| [Api Latency Correlation](level-2-correlation/api-latency-correlation/) | API / Service | Correlation / Analysis | API endpoint, upstream service, request path, runtime dependency |
| [Authentication Anomaly Analysis](level-2-correlation/authentication-anomaly-analysis/) | Identity / Authentication | Correlation / Analysis | authentication flow, identity provider, login event, risk signal |
| [Backup Failure Correlation](level-2-correlation/backup-failure-correlation/) | Backup / Recovery | Correlation / Analysis | backup job, backup scheduler, protected workload, backup repository, recovery point |
| [Cluster Resource Instability Analysis](level-2-correlation/cluster-resource-instability-analysis/) | Cluster / Platform | Correlation / Analysis | cluster node, workload, control plane, resource pool |
| [Compute Resource Correlation](level-2-correlation/compute-resource-correlation/) | Compute / Resource | Correlation / Analysis | compute node, instance, CPU, memory, disk, runtime host |
| [Container Dependency Analysis](level-2-correlation/container-dependency-analysis/) | Container / Runtime | Correlation / Analysis | container runtime, pod, workload, node, image runtime |
| [Cross Domain Security Correlation](level-2-correlation/cross-domain-security-correlation/) | Security / Telemetry | Correlation / Analysis | security event, policy control, endpoint signal, audit source |
| [Cross Region Network Anomaly Correlation](level-2-correlation/cross-region-network-anomaly-correlation/) | Network / Routing | Correlation / Analysis | network path, route, interface, traffic flow |
| [Cross Server Failure Correlation](level-2-correlation/cross-server-failure-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Cross Service Anomaly Correlation](level-2-correlation/cross-service-anomaly-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Cross Service Database Dependency Analysis](level-2-correlation/cross-service-database-dependency-analysis/) | Database | Correlation / Analysis | database instance, query workload, replication channel, storage backend |
| [Cross Site Network Correlation](level-2-correlation/cross-site-network-correlation/) | Network / Routing | Correlation / Analysis | network path, route, interface, traffic flow |
| [Database Latency Correlation](level-2-correlation/database-latency-correlation/) | Database | Correlation / Analysis | database instance, query workload, replication channel, storage backend |
| [Filesystem Failure Correlation](level-2-correlation/filesystem-failure-correlation/) | Filesystem | Correlation / Analysis | filesystem, mount point, volume, inode, disk path |
| [Identity Risk Analysis](level-2-correlation/identity-risk-analysis/) | Identity / Access | Correlation / Analysis | identity provider, access policy, authentication flow, account state |
| [Infrastructure Anomaly Analysis](level-2-correlation/infrastructure-anomaly-analysis/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Multi Region Latency Correlation](level-2-correlation/multi-region-latency-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Network Packet Loss Correlation](level-2-correlation/network-packet-loss-correlation/) | Network / Routing | Correlation / Analysis | network path, route, interface, traffic flow |
| [Network Path Dependency Analysis](level-2-correlation/network-path-dependency-analysis/) | Network / Routing | Correlation / Analysis | network path, route, interface, traffic flow |
| [Platform Dependency Correlation](level-2-correlation/platform-dependency-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Pod Failure Correlation](level-2-correlation/pod-failure-correlation/) | Container / Pod | Correlation / Analysis | pod, container, node, workload, service endpoint |
| [Privilege Escalation Correlation](level-2-correlation/privilege-escalation-correlation/) | Privileged Access | Correlation / Analysis | privileged session, admin account, access control, audit source |
| [Query Lock Analysis](level-2-correlation/query-lock-analysis/) | Database / Query | Correlation / Analysis | query workload, lock state, connection pool, database runtime |
| [Replication Failure Correlation](level-2-correlation/replication-failure-correlation/) | Database / Replication | Correlation / Analysis | replication channel, source database, replica database, lag signal |
| [Resource Contention Correlation](level-2-correlation/resource-contention-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Routing Instability Correlation](level-2-correlation/routing-instability-correlation/) | Network / Routing | Correlation / Analysis | route table, routing path, router, service path |
| [Runtime Instability Analysis](level-2-correlation/runtime-instability-analysis/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Security Anomaly Correlation](level-2-correlation/security-anomaly-correlation/) | Security / Telemetry | Correlation / Analysis | security event, policy control, endpoint signal, audit source |
| [Security Policy Violation Analysis](level-2-correlation/security-policy-violation-analysis/) | Security / Telemetry | Correlation / Analysis | security event, policy control, endpoint signal, audit source |
| [Service Dependency Correlation](level-2-correlation/service-dependency-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Service Mesh Latency Correlation](level-2-correlation/service-mesh-latency-correlation/) | Service Mesh | Correlation / Analysis | service mesh route, sidecar proxy, service dependency, traffic policy |
| [Storage Io Instability Analysis](level-2-correlation/storage-io-instability-analysis/) | Storage | Correlation / Analysis | storage volume, storage backend, object store, I/O path |
| [Threat Propagation Analysis](level-2-correlation/threat-propagation-analysis/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Traffic Spike Correlation](level-2-correlation/traffic-spike-correlation/) | Traffic / Flow | Correlation / Analysis | traffic flow, interface, request volume, network path |
| [Virtualization Resource Correlation](level-2-correlation/virtualization-resource-correlation/) | General Infrastructure | Correlation / Analysis | infrastructure component, telemetry source, operational dependency |
| [Vpn Latency Correlation](level-2-correlation/vpn-latency-correlation/) | Network / VPN | Correlation / Analysis | VPN tunnel, VPN gateway, remote endpoint, routing path |
| [Vpn Tunnel Instability Analysis](level-2-correlation/vpn-tunnel-instability-analysis/) | Network / VPN | Correlation / Analysis | VPN tunnel, VPN gateway, remote endpoint, routing path |

---

## Level 3 - Recovery

Scenario count: **25**

| Scenario | Domain | Type | Target Resource |
|---|---|---|---|
| [Api Service Recovery](level-3-recovery/api-service-recovery/) | API / Service | Recovery / Automation | API endpoint, upstream service, request path, runtime dependency |
| [Backup Restoration Automation](level-3-recovery/backup-restoration-automation/) | Backup / Recovery | Recovery / Automation | backup job, backup scheduler, protected workload, backup repository, recovery point |
| [Cloud Instance Recovery Automation](level-3-recovery/cloud-instance-recovery-automation/) | Cloud Instance | Recovery / Automation | cloud instance, VM, host resource, instance status check |
| [Cluster Node Recovery Orchestration](level-3-recovery/cluster-node-recovery-orchestration/) | Cluster / Platform | Recovery / Automation | cluster node, workload, control plane, resource pool |
| [Compute Failover Orchestration](level-3-recovery/compute-failover-orchestration/) | Compute / Resource | Recovery / Automation | compute node, instance, CPU, memory, disk, runtime host |
| [Container Failover Automation](level-3-recovery/container-failover-automation/) | Container / Runtime | Recovery / Automation | container runtime, pod, workload, node, image runtime |
| [Data Recovery Orchestration](level-3-recovery/data-recovery-orchestration/) | General Infrastructure | Recovery / Automation | infrastructure component, telemetry source, operational dependency |
| [Database Failover Automation](level-3-recovery/database-failover-automation/) | Database | Recovery / Automation | database instance, query workload, replication channel, storage backend |
| [Database Recovery Orchestration](level-3-recovery/database-recovery-orchestration/) | Database | Recovery / Automation | database instance, query workload, replication channel, storage backend |
| [Database Service Restoration](level-3-recovery/database-service-restoration/) | Database | Recovery / Automation | database instance, query workload, replication channel, storage backend |
| [Dns Service Restoration](level-3-recovery/dns-service-restoration/) | DNS / Name Resolution | Recovery / Automation | DNS resolver, DNS record, query path, client resolution flow |
| [Infrastructure Recovery Orchestration](level-3-recovery/infrastructure-recovery-orchestration/) | General Infrastructure | Recovery / Automation | infrastructure component, telemetry source, operational dependency |
| [Kubernetes Node Recovery](level-3-recovery/kubernetes-node-recovery/) | Kubernetes / Cluster | Recovery / Automation | Kubernetes cluster, node, pod, control plane, service object |
| [Kubernetes Service Recovery](level-3-recovery/kubernetes-service-recovery/) | Kubernetes / Cluster | Recovery / Automation | Kubernetes cluster, node, pod, control plane, service object |
| [Load Balancer Recovery](level-3-recovery/load-balancer-recovery/) | Load Balancing | Recovery / Automation | load balancer, listener, target group, backend service |
| [Network Failover Automation](level-3-recovery/network-failover-automation/) | Network / Routing | Recovery / Automation | network path, route, interface, traffic flow |
| [Network Route Recovery Orchestration](level-3-recovery/network-route-recovery-orchestration/) | Network / Routing | Recovery / Automation | network path, route, interface, traffic flow |
| [Platform Runtime Restoration](level-3-recovery/platform-runtime-restoration/) | General Infrastructure | Recovery / Automation | infrastructure component, telemetry source, operational dependency |
| [Replication Recovery Orchestration](level-3-recovery/replication-recovery-orchestration/) | Database / Replication | Recovery / Automation | replication channel, source database, replica database, lag signal |
| [Resource Rebalancing Automation](level-3-recovery/resource-rebalancing-automation/) | General Infrastructure | Recovery / Automation | infrastructure component, telemetry source, operational dependency |
| [Server Service Recovery](level-3-recovery/server-service-recovery/) | General Infrastructure | Recovery / Automation | infrastructure component, telemetry source, operational dependency |
| [Service Mesh Traffic Restoration](level-3-recovery/service-mesh-traffic-restoration/) | Service Mesh | Recovery / Automation | service mesh route, sidecar proxy, service dependency, traffic policy |
| [Traffic Restoration Workflow](level-3-recovery/traffic-restoration-workflow/) | Traffic / Flow | Recovery / Automation | traffic flow, interface, request volume, network path |
| [Virtual Machine Restoration](level-3-recovery/virtual-machine-restoration/) | Virtual Machine | Recovery / Automation | virtual machine, hypervisor, guest OS, compute host |
| [Vpn Tunnel Recovery Automation](level-3-recovery/vpn-tunnel-recovery-automation/) | Network / VPN | Recovery / Automation | VPN tunnel, VPN gateway, remote endpoint, routing path |

---

## Level 4 - Resilience

Scenario count: **13**

| Scenario | Domain | Type | Target Resource |
|---|---|---|---|
| [Cross Region Data Survivability](level-4-resilience/cross-region-data-survivability/) | General Infrastructure | Resilience / Failover | infrastructure component, telemetry source, operational dependency |
| [Cross Region Kubernetes Resilience](level-4-resilience/cross-region-kubernetes-resilience/) | Kubernetes / Cluster | Resilience / Failover | Kubernetes cluster, node, pod, control plane, service object |
| [Cross Region Network Resilience](level-4-resilience/cross-region-network-resilience/) | Network / Routing | Resilience / Failover | network path, route, interface, traffic flow |
| [Distributed Connectivity Survivability](level-4-resilience/distributed-connectivity-survivability/) | General Infrastructure | Resilience / Failover | infrastructure component, telemetry source, operational dependency |
| [Distributed Database Failover](level-4-resilience/distributed-database-failover/) | Database | Resilience / Failover | database instance, query workload, replication channel, storage backend |
| [Distributed Platform Survivability](level-4-resilience/distributed-platform-survivability/) | General Infrastructure | Resilience / Failover | infrastructure component, telemetry source, operational dependency |
| [Distributed Security Resilience](level-4-resilience/distributed-security-resilience/) | Security / Telemetry | Resilience / Failover | security event, policy control, endpoint signal, audit source |
| [Identity Resilience Coordination](level-4-resilience/identity-resilience-coordination/) | Identity / Access | Resilience / Failover | identity provider, access policy, authentication flow, account state |
| [Multi Cluster Failover](level-4-resilience/multi-cluster-failover/) | Cluster / Platform | Resilience / Failover | cluster node, workload, control plane, resource pool |
| [Multi Cluster Failover Coordination](level-4-resilience/multi-cluster-failover-coordination/) | Cluster / Platform | Resilience / Failover | cluster node, workload, control plane, resource pool |
| [Multi Region Service Failover](level-4-resilience/multi-region-service-failover/) | General Infrastructure | Resilience / Failover | infrastructure component, telemetry source, operational dependency |
| [Multi Region Service Failover Resilience](level-4-resilience/multi-region-service-failover-resilience/) | General Infrastructure | Resilience / Failover | infrastructure component, telemetry source, operational dependency |
| [Multi Site Routing Failover](level-4-resilience/multi-site-routing-failover/) | Network / Routing | Resilience / Failover | route table, routing path, router, service path |

---

## Level 5 - Continuity

Scenario count: **6**

| Scenario | Domain | Type | Target Resource |
|---|---|---|---|
| [Enterprise Cloud Continuity](level-5-continuity/enterprise-cloud-continuity/) | General Infrastructure | Continuity / Governance | infrastructure component, telemetry source, operational dependency |
| [Enterprise Network Continuity](level-5-continuity/enterprise-network-continuity/) | Network / Routing | Continuity / Governance | network path, route, interface, traffic flow |
| [Enterprise Operational Continuity](level-5-continuity/enterprise-operational-continuity/) | General Infrastructure | Continuity / Governance | infrastructure component, telemetry source, operational dependency |
| [Enterprise Platform Continuity](level-5-continuity/enterprise-platform-continuity/) | General Infrastructure | Continuity / Governance | infrastructure component, telemetry source, operational dependency |
| [Enterprise Security Continuity](level-5-continuity/enterprise-security-continuity/) | Security / Telemetry | Continuity / Governance | security event, policy control, endpoint signal, audit source |
| [Enterprise Service Continuity Coordination](level-5-continuity/enterprise-service-continuity-coordination/) | General Infrastructure | Continuity / Governance | infrastructure component, telemetry source, operational dependency |

---

## Summary

This scenario catalog provides a reviewer-readable index of the operational scenarios in the portfolio.

Each scenario README documents scenario metadata, operational context, used modules, infrastructure components, lifecycle workflow, validation criteria, and evidence references.
