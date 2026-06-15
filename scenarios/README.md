# Scenario Inventory

This directory contains lifecycle-aligned infrastructure operations scenarios for the SNSD Hybrid Infrastructure portfolio.

## How to use this catalog

- Start with the lifecycle summary to understand the progression from visibility to continuity.
- Browse by level to inspect scenarios by maturity and operational purpose.
- Open each scenario README for its intent, validation focus, and related lab.

## Inventory summary

- Total scenarios: 150
- Level 1 — Visibility: 45
- Level 2 — Correlation: 41
- Level 3 — Recovery: 33
- Level 4 — Resilience: 21
- Level 5 — Continuity: 10

## Lifecycle coverage

| Level | Focus |
|---|---|
| Level 1 — Visibility | Detection, health visibility, and state exposure |
| Level 2 — Correlation | Dependency analysis and impact reasoning |
| Level 3 — Recovery | Controlled recovery execution and rollback workflows |
| Level 4 — Resilience | Failover and survivability validation |
| Level 5 — Continuity | Governance, continuity readiness, and reporting |

## Browse by level

- [level-1-visibility](level-1-visibility/)
- [level-2-correlation](level-2-correlation/)
- [level-3-recovery](level-3-recovery/)
- [level-4-resilience](level-4-resilience/)
- [level-5-continuity](level-5-continuity/)

## Related documents

- [docs/lab-coverage-matrix.md](../docs/lab-coverage-matrix.md)
- [docs/scenario-to-lab-traceability.md](../docs/scenario-to-lab-traceability.md)
- [validation-reports/scenario-validation-summary.md](../validation-reports/scenario-validation-summary.md)
| [Kubernetes Node Recovery](./level-3-recovery/kubernetes-node-recovery/README.md) | Kubernetes / Cluster | content-filled | 0 |
| [Kubernetes Service Recovery](./level-3-recovery/kubernetes-service-recovery/README.md) | Kubernetes / Cluster | content-filled | 0 |
| [Load Balancer Recovery](./level-3-recovery/load-balancer-recovery/README.md) | Load Balancing | content-filled | 0 |
| [Network Failover Automation](./level-3-recovery/network-failover-automation/README.md) | Network / Routing | content-filled | 0 |
| [Network Route Recovery Orchestration](./level-3-recovery/network-route-recovery-orchestration/README.md) | Network / Routing | content-filled | 0 |
| [Platform Runtime Restoration](./level-3-recovery/platform-runtime-restoration/README.md) | General Infrastructure | content-filled | 0 |
| [Replication Recovery Orchestration](./level-3-recovery/replication-recovery-orchestration/README.md) | Database / Replication | content-filled | 0 |
| [Resource Rebalancing Automation](./level-3-recovery/resource-rebalancing-automation/README.md) | General Infrastructure | content-filled | 0 |
| [Server Service Recovery](./level-3-recovery/server-service-recovery/README.md) | General Infrastructure | content-filled | 0 |
| [Service Mesh Traffic Restoration](./level-3-recovery/service-mesh-traffic-restoration/README.md) | Service Mesh | content-filled | 0 |
| [Storage Volume Recovery Automation](./level-3-recovery/storage-volume-recovery-automation/README.md) | Storage Operations | content-filled | 0 |
| [Traffic Restoration Workflow](./level-3-recovery/traffic-restoration-workflow/README.md) | Traffic / Flow | content-filled | 0 |
| [Virtual Machine Restoration](./level-3-recovery/virtual-machine-restoration/README.md) | Virtual Machine | content-filled | 0 |
| [Vpn Tunnel Recovery Automation](./level-3-recovery/vpn-tunnel-recovery-automation/README.md) | Network / VPN | content-filled | 0 |

### Level 4 - Resilience

This level focuses on survivability under disruption. Scenarios in this group validate failover coordination, redundancy, and resilience across distributed infrastructure.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Backup Resilience Validation](./level-4-resilience/backup-resilience-validation/README.md) | Backup Operations | content-filled | 0 |
| [Change Resilience Coordination](./level-4-resilience/change-resilience-coordination/README.md) | Change Operations | content-filled | 0 |
| [Configuration Resilience Validation](./level-4-resilience/configuration-resilience-validation/README.md) | Configuration Operations | content-filled | 0 |
| [Control Plane Resilience](./level-4-resilience/control-plane-resilience/README.md) | Platform Operations | content-filled | 0 |
| [Cross Region Data Survivability](./level-4-resilience/cross-region-data-survivability/README.md) | General Infrastructure | content-filled | 0 |
| [Cross Region Kubernetes Resilience](./level-4-resilience/cross-region-kubernetes-resilience/README.md) | Kubernetes / Cluster | content-filled | 0 |
| [Cross Region Network Resilience](./level-4-resilience/cross-region-network-resilience/README.md) | Network / Routing | content-filled | 0 |
| [Distributed Connectivity Survivability](./level-4-resilience/distributed-connectivity-survivability/README.md) | General Infrastructure | content-filled | 0 |
| [Distributed Database Failover](./level-4-resilience/distributed-database-failover/README.md) | Database | content-filled | 0 |
| [Distributed Platform Survivability](./level-4-resilience/distributed-platform-survivability/README.md) | General Infrastructure | content-filled | 0 |
| [Distributed Security Resilience](./level-4-resilience/distributed-security-resilience/README.md) | Security / Telemetry | content-filled | 0 |
| [Identity Failover Resilience](./level-4-resilience/identity-failover-resilience/README.md) | Identity Operations | content-filled | 0 |
| [Identity Resilience Coordination](./level-4-resilience/identity-resilience-coordination/README.md) | Identity / Access | content-filled | 0 |
| [Inter Region Routing Resilience](./level-4-resilience/inter-region-routing-resilience/README.md) | Network Operations | content-filled | 0 |
| [Kubernetes Platform Resilience](./level-4-resilience/kubernetes-platform-resilience/README.md) | Kubernetes Operations | content-filled | 0 |
| [Multi Cluster Failover](./level-4-resilience/multi-cluster-failover/README.md) | Cluster / Platform | content-filled | 0 |
| [Multi Cluster Failover Coordination](./level-4-resilience/multi-cluster-failover-coordination/README.md) | Cluster / Platform | content-filled | 0 |
| [Multi Region Service Failover](./level-4-resilience/multi-region-service-failover/README.md) | General Infrastructure | content-filled | 0 |
| [Multi Region Service Failover Resilience](./level-4-resilience/multi-region-service-failover-resilience/README.md) | General Infrastructure | content-filled | 0 |
| [Multi Site Routing Failover](./level-4-resilience/multi-site-routing-failover/README.md) | Network / Routing | content-filled | 0 |
| [Storage Replication Resilience](./level-4-resilience/storage-replication-resilience/README.md) | Storage Operations | content-filled | 0 |

### Level 5 - Continuity

This level focuses on enterprise continuity. Scenarios in this group address governance, readiness, reporting, and long-term operational assurance.

| Scenario | Domain | Status | Related Links |
|---|---|---|---:|
| [Enterprise Change Continuity](./level-5-continuity/enterprise-change-continuity/README.md) | Continuity Operations | content-filled | 0 |
| [Enterprise Cloud Continuity](./level-5-continuity/enterprise-cloud-continuity/README.md) | General Infrastructure | content-filled | 0 |
| [Enterprise Control Plane Continuity](./level-5-continuity/enterprise-control-plane-continuity/README.md) | Continuity Operations | content-filled | 0 |
| [Enterprise Data Protection Continuity](./level-5-continuity/enterprise-data-protection-continuity/README.md) | Continuity Operations | content-filled | 0 |
| [Enterprise Identity Continuity](./level-5-continuity/enterprise-identity-continuity/README.md) | Continuity Operations | content-filled | 0 |
| [Enterprise Network Continuity](./level-5-continuity/enterprise-network-continuity/README.md) | Network / Routing | content-filled | 0 |
| [Enterprise Operational Continuity](./level-5-continuity/enterprise-operational-continuity/README.md) | General Infrastructure | content-filled | 0 |
| [Enterprise Platform Continuity](./level-5-continuity/enterprise-platform-continuity/README.md) | General Infrastructure | content-filled | 0 |
| [Enterprise Security Continuity](./level-5-continuity/enterprise-security-continuity/README.md) | Security / Telemetry | content-filled | 0 |
| [Enterprise Service Continuity Coordination](./level-5-continuity/enterprise-service-continuity-coordination/README.md) | General Infrastructure | content-filled | 0 |

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
