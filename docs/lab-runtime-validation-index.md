# Lab Runtime Validation Index

Generated At: 2026-06-30 11:44:47

This document indexes reviewer-facing runtime validation evidence generated for scenario packages.

## Executive Summary

- Total scenarios: 150
- OK: 150
- Missing evidence: 0
- Contains NOT_FOUND: 0

## Reviewer Interpretation

- `OK` means the scenario has generated reviewer-facing runtime validation evidence.
- `MISSING` means the scenario evidence file does not exist.
- `NOT_FOUND` means the evidence file exists but references missing local runtime evidence.

Reviewer-facing evidence is stored under each scenario directory:

    scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md

Local raw runtime evidence is generated under:

    labs/evidence/generated/

## Level Summary

| Level | Total | OK | Missing | NOT_FOUND |
|---|---:|---:|---:|---:|
| Level 1 - Visibility | 45 | 45 | 0 | 0 |
| Level 2 - Correlation | 41 | 41 | 0 | 0 |
| Level 3 - Recovery | 33 | 33 | 0 | 0 |
| Level 4 - Distributed Resilience | 0 | 0 | 0 | 0 |
| Level 5 - Enterprise Continuity | 0 | 0 | 0 | 0 |
| level-4-resilience | 21 | 21 | 0 | 0 |
| level-5-continuity | 10 | 10 | 0 | 0 |

## Review Path

Recommended review order:

1. Check the Executive Summary.
2. Confirm all levels show `Missing = 0` and `NOT_FOUND = 0`.
3. Open representative scenario evidence files from Level 1, Level 3, Level 4, and Level 5.
4. Review `docs/failure-injection-scenarios.md` for controlled failure validation.
5. Review `docs/runtime-validation-pipeline.md` for evidence generation workflow.

## Scenario Evidence Index

### Level 1 - Visibility

| Scenario | Status | Evidence |
|---|---|---|
| `api-gateway-health-monitoring` | OK | `scenarios/level-1-visibility/api-gateway-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `application-runtime-monitoring` | OK | `scenarios/level-1-visibility/application-runtime-monitoring/evidence/generated/lab-runtime-validation.md` |
| `audit-log-monitoring` | OK | `scenarios/level-1-visibility/audit-log-monitoring/evidence/generated/lab-runtime-validation.md` |
| `backup-job-monitoring` | OK | `scenarios/level-1-visibility/backup-job-monitoring/evidence/generated/lab-runtime-validation.md` |
| `bgp-neighbor-visibility` | OK | `scenarios/level-1-visibility/bgp-neighbor-visibility/evidence/generated/lab-runtime-validation.md` |
| `certificate-expiration-monitoring` | OK | `scenarios/level-1-visibility/certificate-expiration-monitoring/evidence/generated/lab-runtime-validation.md` |
| `cloud-instance-health-monitoring` | OK | `scenarios/level-1-visibility/cloud-instance-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `compute-resource-monitoring` | OK | `scenarios/level-1-visibility/compute-resource-monitoring/evidence/generated/lab-runtime-validation.md` |
| `configuration-drift-monitoring` | OK | `scenarios/level-1-visibility/configuration-drift-monitoring/evidence/generated/lab-runtime-validation.md` |
| `container-runtime-visibility` | OK | `scenarios/level-1-visibility/container-runtime-visibility/evidence/generated/lab-runtime-validation.md` |
| `control-plane-health-monitoring` | OK | `scenarios/level-1-visibility/control-plane-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `database-health-monitoring` | OK | `scenarios/level-1-visibility/database-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `database-replication-visibility` | OK | `scenarios/level-1-visibility/database-replication-visibility/evidence/generated/lab-runtime-validation.md` |
| `database-runtime-visibility` | OK | `scenarios/level-1-visibility/database-runtime-visibility/evidence/generated/lab-runtime-validation.md` |
| `dns-resolution-monitoring` | OK | `scenarios/level-1-visibility/dns-resolution-monitoring/evidence/generated/lab-runtime-validation.md` |
| `endpoint-reachability-monitoring` | OK | `scenarios/level-1-visibility/endpoint-reachability-monitoring/evidence/generated/lab-runtime-validation.md` |
| `endpoint-security-visibility` | OK | `scenarios/level-1-visibility/endpoint-security-visibility/evidence/generated/lab-runtime-validation.md` |
| `filesystem-health-visibility` | OK | `scenarios/level-1-visibility/filesystem-health-visibility/evidence/generated/lab-runtime-validation.md` |
| `hardware-health-monitoring` | OK | `scenarios/level-1-visibility/hardware-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `hypervisor-resource-monitoring` | OK | `scenarios/level-1-visibility/hypervisor-resource-monitoring/evidence/generated/lab-runtime-validation.md` |
| `identity-access-visibility` | OK | `scenarios/level-1-visibility/identity-access-visibility/evidence/generated/lab-runtime-validation.md` |
| `inter-region-connectivity-monitoring` | OK | `scenarios/level-1-visibility/inter-region-connectivity-monitoring/evidence/generated/lab-runtime-validation.md` |
| `kubernetes-cluster-health-monitoring` | OK | `scenarios/level-1-visibility/kubernetes-cluster-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `kubernetes-cluster-visibility` | OK | `scenarios/level-1-visibility/kubernetes-cluster-visibility/evidence/generated/lab-runtime-validation.md` |
| `load-balancer-health-monitoring` | OK | `scenarios/level-1-visibility/load-balancer-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `message-queue-monitoring` | OK | `scenarios/level-1-visibility/message-queue-monitoring/evidence/generated/lab-runtime-validation.md` |
| `microservice-health-monitoring` | OK | `scenarios/level-1-visibility/microservice-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `network-path-visibility` | OK | `scenarios/level-1-visibility/network-path-visibility/evidence/generated/lab-runtime-validation.md` |
| `network-traffic-visibility` | OK | `scenarios/level-1-visibility/network-traffic-visibility/evidence/generated/lab-runtime-validation.md` |
| `object-storage-health-monitoring` | OK | `scenarios/level-1-visibility/object-storage-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `privileged-session-monitoring` | OK | `scenarios/level-1-visibility/privileged-session-monitoring/evidence/generated/lab-runtime-validation.md` |
| `process-health-monitoring` | OK | `scenarios/level-1-visibility/process-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `security-event-monitoring` | OK | `scenarios/level-1-visibility/security-event-monitoring/evidence/generated/lab-runtime-validation.md` |
| `security-policy-visibility` | OK | `scenarios/level-1-visibility/security-policy-visibility/evidence/generated/lab-runtime-validation.md` |
| `security-telemetry-monitoring` | OK | `scenarios/level-1-visibility/security-telemetry-monitoring/evidence/generated/lab-runtime-validation.md` |
| `service-health-visibility` | OK | `scenarios/level-1-visibility/service-health-visibility/evidence/generated/lab-runtime-validation.md` |
| `service-mesh-traffic-visibility` | OK | `scenarios/level-1-visibility/service-mesh-traffic-visibility/evidence/generated/lab-runtime-validation.md` |
| `storage-capacity-monitoring` | OK | `scenarios/level-1-visibility/storage-capacity-monitoring/evidence/generated/lab-runtime-validation.md` |
| `storage-latency-monitoring` | OK | `scenarios/level-1-visibility/storage-latency-monitoring/evidence/generated/lab-runtime-validation.md` |
| `system-event-visibility` | OK | `scenarios/level-1-visibility/system-event-visibility/evidence/generated/lab-runtime-validation.md` |
| `virtual-machine-health-monitoring` | OK | `scenarios/level-1-visibility/virtual-machine-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `vpn-connectivity-monitoring` | OK | `scenarios/level-1-visibility/vpn-connectivity-monitoring/evidence/generated/lab-runtime-validation.md` |
| `vpn-latency-visibility` | OK | `scenarios/level-1-visibility/vpn-latency-visibility/evidence/generated/lab-runtime-validation.md` |
| `vpn-tunnel-health-monitoring` | OK | `scenarios/level-1-visibility/vpn-tunnel-health-monitoring/evidence/generated/lab-runtime-validation.md` |
| `wan-link-monitoring` | OK | `scenarios/level-1-visibility/wan-link-monitoring/evidence/generated/lab-runtime-validation.md` |

### Level 2 - Correlation

| Scenario | Status | Evidence |
|---|---|---|
| `api-latency-correlation` | OK | `scenarios/level-2-correlation/api-latency-correlation/evidence/generated/lab-runtime-validation.md` |
| `authentication-anomaly-analysis` | OK | `scenarios/level-2-correlation/authentication-anomaly-analysis/evidence/generated/lab-runtime-validation.md` |
| `backup-failure-correlation` | OK | `scenarios/level-2-correlation/backup-failure-correlation/evidence/generated/lab-runtime-validation.md` |
| `change-impact-correlation` | OK | `scenarios/level-2-correlation/change-impact-correlation/evidence/generated/lab-runtime-validation.md` |
| `cluster-resource-instability-analysis` | OK | `scenarios/level-2-correlation/cluster-resource-instability-analysis/evidence/generated/lab-runtime-validation.md` |
| `compute-resource-correlation` | OK | `scenarios/level-2-correlation/compute-resource-correlation/evidence/generated/lab-runtime-validation.md` |
| `configuration-drift-correlation` | OK | `scenarios/level-2-correlation/configuration-drift-correlation/evidence/generated/lab-runtime-validation.md` |
| `container-dependency-analysis` | OK | `scenarios/level-2-correlation/container-dependency-analysis/evidence/generated/lab-runtime-validation.md` |
| `control-plane-anomaly-correlation` | OK | `scenarios/level-2-correlation/control-plane-anomaly-correlation/evidence/generated/lab-runtime-validation.md` |
| `cross-domain-security-correlation` | OK | `scenarios/level-2-correlation/cross-domain-security-correlation/evidence/generated/lab-runtime-validation.md` |
| `cross-region-network-anomaly-correlation` | OK | `scenarios/level-2-correlation/cross-region-network-anomaly-correlation/evidence/generated/lab-runtime-validation.md` |
| `cross-server-failure-correlation` | OK | `scenarios/level-2-correlation/cross-server-failure-correlation/evidence/generated/lab-runtime-validation.md` |
| `cross-service-anomaly-correlation` | OK | `scenarios/level-2-correlation/cross-service-anomaly-correlation/evidence/generated/lab-runtime-validation.md` |
| `cross-service-database-dependency-analysis` | OK | `scenarios/level-2-correlation/cross-service-database-dependency-analysis/evidence/generated/lab-runtime-validation.md` |
| `cross-site-network-correlation` | OK | `scenarios/level-2-correlation/cross-site-network-correlation/evidence/generated/lab-runtime-validation.md` |
| `database-latency-correlation` | OK | `scenarios/level-2-correlation/database-latency-correlation/evidence/generated/lab-runtime-validation.md` |
| `filesystem-failure-correlation` | OK | `scenarios/level-2-correlation/filesystem-failure-correlation/evidence/generated/lab-runtime-validation.md` |
| `identity-risk-analysis` | OK | `scenarios/level-2-correlation/identity-risk-analysis/evidence/generated/lab-runtime-validation.md` |
| `infrastructure-anomaly-analysis` | OK | `scenarios/level-2-correlation/infrastructure-anomaly-analysis/evidence/generated/lab-runtime-validation.md` |
| `inter-region-dependency-correlation` | OK | `scenarios/level-2-correlation/inter-region-dependency-correlation/evidence/generated/lab-runtime-validation.md` |
| `multi-region-latency-correlation` | OK | `scenarios/level-2-correlation/multi-region-latency-correlation/evidence/generated/lab-runtime-validation.md` |
| `network-packet-loss-correlation` | OK | `scenarios/level-2-correlation/network-packet-loss-correlation/evidence/generated/lab-runtime-validation.md` |
| `network-path-dependency-analysis` | OK | `scenarios/level-2-correlation/network-path-dependency-analysis/evidence/generated/lab-runtime-validation.md` |
| `platform-dependency-correlation` | OK | `scenarios/level-2-correlation/platform-dependency-correlation/evidence/generated/lab-runtime-validation.md` |
| `pod-failure-correlation` | OK | `scenarios/level-2-correlation/pod-failure-correlation/evidence/generated/lab-runtime-validation.md` |
| `privilege-escalation-correlation` | OK | `scenarios/level-2-correlation/privilege-escalation-correlation/evidence/generated/lab-runtime-validation.md` |
| `query-lock-analysis` | OK | `scenarios/level-2-correlation/query-lock-analysis/evidence/generated/lab-runtime-validation.md` |
| `replication-failure-correlation` | OK | `scenarios/level-2-correlation/replication-failure-correlation/evidence/generated/lab-runtime-validation.md` |
| `resource-contention-correlation` | OK | `scenarios/level-2-correlation/resource-contention-correlation/evidence/generated/lab-runtime-validation.md` |
| `routing-instability-correlation` | OK | `scenarios/level-2-correlation/routing-instability-correlation/evidence/generated/lab-runtime-validation.md` |
| `runtime-instability-analysis` | OK | `scenarios/level-2-correlation/runtime-instability-analysis/evidence/generated/lab-runtime-validation.md` |
| `security-anomaly-correlation` | OK | `scenarios/level-2-correlation/security-anomaly-correlation/evidence/generated/lab-runtime-validation.md` |
| `security-policy-violation-analysis` | OK | `scenarios/level-2-correlation/security-policy-violation-analysis/evidence/generated/lab-runtime-validation.md` |
| `service-dependency-correlation` | OK | `scenarios/level-2-correlation/service-dependency-correlation/evidence/generated/lab-runtime-validation.md` |
| `service-mesh-latency-correlation` | OK | `scenarios/level-2-correlation/service-mesh-latency-correlation/evidence/generated/lab-runtime-validation.md` |
| `storage-io-instability-analysis` | OK | `scenarios/level-2-correlation/storage-io-instability-analysis/evidence/generated/lab-runtime-validation.md` |
| `threat-propagation-analysis` | OK | `scenarios/level-2-correlation/threat-propagation-analysis/evidence/generated/lab-runtime-validation.md` |
| `traffic-spike-correlation` | OK | `scenarios/level-2-correlation/traffic-spike-correlation/evidence/generated/lab-runtime-validation.md` |
| `virtualization-resource-correlation` | OK | `scenarios/level-2-correlation/virtualization-resource-correlation/evidence/generated/lab-runtime-validation.md` |
| `vpn-latency-correlation` | OK | `scenarios/level-2-correlation/vpn-latency-correlation/evidence/generated/lab-runtime-validation.md` |
| `vpn-tunnel-instability-analysis` | OK | `scenarios/level-2-correlation/vpn-tunnel-instability-analysis/evidence/generated/lab-runtime-validation.md` |

### Level 3 - Recovery

| Scenario | Status | Evidence |
|---|---|---|
| `api-service-recovery` | OK | `scenarios/level-3-recovery/api-service-recovery/evidence/generated/lab-runtime-validation.md` |
| `backup-restoration-automation` | OK | `scenarios/level-3-recovery/backup-restoration-automation/evidence/generated/lab-runtime-validation.md` |
| `certificate-renewal-automation` | OK | `scenarios/level-3-recovery/certificate-renewal-automation/evidence/generated/lab-runtime-validation.md` |
| `change-failure-rollback` | OK | `scenarios/level-3-recovery/change-failure-rollback/evidence/generated/lab-runtime-validation.md` |
| `cloud-instance-recovery-automation` | OK | `scenarios/level-3-recovery/cloud-instance-recovery-automation/evidence/generated/lab-runtime-validation.md` |
| `cluster-node-recovery-orchestration` | OK | `scenarios/level-3-recovery/cluster-node-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `compute-failover-orchestration` | OK | `scenarios/level-3-recovery/compute-failover-orchestration/evidence/generated/lab-runtime-validation.md` |
| `configuration-rollback-automation` | OK | `scenarios/level-3-recovery/configuration-rollback-automation/evidence/generated/lab-runtime-validation.md` |
| `container-failover-automation` | OK | `scenarios/level-3-recovery/container-failover-automation/evidence/generated/lab-runtime-validation.md` |
| `control-plane-recovery-orchestration` | OK | `scenarios/level-3-recovery/control-plane-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `data-recovery-orchestration` | OK | `scenarios/level-3-recovery/data-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `database-failover-automation` | OK | `scenarios/level-3-recovery/database-failover-automation/evidence/generated/lab-runtime-validation.md` |
| `database-recovery-orchestration` | OK | `scenarios/level-3-recovery/database-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `database-service-restoration` | OK | `scenarios/level-3-recovery/database-service-restoration/evidence/generated/lab-runtime-validation.md` |
| `dns-service-restoration` | OK | `scenarios/level-3-recovery/dns-service-restoration/evidence/generated/lab-runtime-validation.md` |
| `identity-access-remediation` | OK | `scenarios/level-3-recovery/identity-access-remediation/evidence/generated/lab-runtime-validation.md` |
| `infrastructure-recovery-orchestration` | OK | `scenarios/level-3-recovery/infrastructure-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `inter-region-routing-recovery` | OK | `scenarios/level-3-recovery/inter-region-routing-recovery/evidence/generated/lab-runtime-validation.md` |
| `kubernetes-control-plane-recovery` | OK | `scenarios/level-3-recovery/kubernetes-control-plane-recovery/evidence/generated/lab-runtime-validation.md` |
| `kubernetes-node-recovery` | OK | `scenarios/level-3-recovery/kubernetes-node-recovery/evidence/generated/lab-runtime-validation.md` |
| `kubernetes-service-recovery` | OK | `scenarios/level-3-recovery/kubernetes-service-recovery/evidence/generated/lab-runtime-validation.md` |
| `load-balancer-recovery` | OK | `scenarios/level-3-recovery/load-balancer-recovery/evidence/generated/lab-runtime-validation.md` |
| `network-failover-automation` | OK | `scenarios/level-3-recovery/network-failover-automation/evidence/generated/lab-runtime-validation.md` |
| `network-route-recovery-orchestration` | OK | `scenarios/level-3-recovery/network-route-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `platform-runtime-restoration` | OK | `scenarios/level-3-recovery/platform-runtime-restoration/evidence/generated/lab-runtime-validation.md` |
| `replication-recovery-orchestration` | OK | `scenarios/level-3-recovery/replication-recovery-orchestration/evidence/generated/lab-runtime-validation.md` |
| `resource-rebalancing-automation` | OK | `scenarios/level-3-recovery/resource-rebalancing-automation/evidence/generated/lab-runtime-validation.md` |
| `server-service-recovery` | OK | `scenarios/level-3-recovery/server-service-recovery/evidence/generated/lab-runtime-validation.md` |
| `service-mesh-traffic-restoration` | OK | `scenarios/level-3-recovery/service-mesh-traffic-restoration/evidence/generated/lab-runtime-validation.md` |
| `storage-volume-recovery-automation` | OK | `scenarios/level-3-recovery/storage-volume-recovery-automation/evidence/generated/lab-runtime-validation.md` |
| `traffic-restoration-workflow` | OK | `scenarios/level-3-recovery/traffic-restoration-workflow/evidence/generated/lab-runtime-validation.md` |
| `virtual-machine-restoration` | OK | `scenarios/level-3-recovery/virtual-machine-restoration/evidence/generated/lab-runtime-validation.md` |
| `vpn-tunnel-recovery-automation` | OK | `scenarios/level-3-recovery/vpn-tunnel-recovery-automation/evidence/generated/lab-runtime-validation.md` |

### level-4-resilience

| Scenario | Status | Evidence |
|---|---|---|
| `backup-resilience-validation` | OK | `scenarios/level-4-resilience/backup-resilience-validation/evidence/generated/lab-runtime-validation.md` |
| `change-resilience-coordination` | OK | `scenarios/level-4-resilience/change-resilience-coordination/evidence/generated/lab-runtime-validation.md` |
| `configuration-resilience-validation` | OK | `scenarios/level-4-resilience/configuration-resilience-validation/evidence/generated/lab-runtime-validation.md` |
| `control-plane-resilience` | OK | `scenarios/level-4-resilience/control-plane-resilience/evidence/generated/lab-runtime-validation.md` |
| `cross-region-data-survivability` | OK | `scenarios/level-4-resilience/cross-region-data-survivability/evidence/generated/lab-runtime-validation.md` |
| `cross-region-kubernetes-resilience` | OK | `scenarios/level-4-resilience/cross-region-kubernetes-resilience/evidence/generated/lab-runtime-validation.md` |
| `cross-region-network-resilience` | OK | `scenarios/level-4-resilience/cross-region-network-resilience/evidence/generated/lab-runtime-validation.md` |
| `distributed-connectivity-survivability` | OK | `scenarios/level-4-resilience/distributed-connectivity-survivability/evidence/generated/lab-runtime-validation.md` |
| `distributed-database-failover` | OK | `scenarios/level-4-resilience/distributed-database-failover/evidence/generated/lab-runtime-validation.md` |
| `distributed-platform-survivability` | OK | `scenarios/level-4-resilience/distributed-platform-survivability/evidence/generated/lab-runtime-validation.md` |
| `distributed-security-resilience` | OK | `scenarios/level-4-resilience/distributed-security-resilience/evidence/generated/lab-runtime-validation.md` |
| `identity-failover-resilience` | OK | `scenarios/level-4-resilience/identity-failover-resilience/evidence/generated/lab-runtime-validation.md` |
| `identity-resilience-coordination` | OK | `scenarios/level-4-resilience/identity-resilience-coordination/evidence/generated/lab-runtime-validation.md` |
| `inter-region-routing-resilience` | OK | `scenarios/level-4-resilience/inter-region-routing-resilience/evidence/generated/lab-runtime-validation.md` |
| `kubernetes-platform-resilience` | OK | `scenarios/level-4-resilience/kubernetes-platform-resilience/evidence/generated/lab-runtime-validation.md` |
| `multi-cluster-failover` | OK | `scenarios/level-4-resilience/multi-cluster-failover/evidence/generated/lab-runtime-validation.md` |
| `multi-cluster-failover-coordination` | OK | `scenarios/level-4-resilience/multi-cluster-failover-coordination/evidence/generated/lab-runtime-validation.md` |
| `multi-region-service-failover` | OK | `scenarios/level-4-resilience/multi-region-service-failover/evidence/generated/lab-runtime-validation.md` |
| `multi-region-service-failover-resilience` | OK | `scenarios/level-4-resilience/multi-region-service-failover-resilience/evidence/generated/lab-runtime-validation.md` |
| `multi-site-routing-failover` | OK | `scenarios/level-4-resilience/multi-site-routing-failover/evidence/generated/lab-runtime-validation.md` |
| `storage-replication-resilience` | OK | `scenarios/level-4-resilience/storage-replication-resilience/evidence/generated/lab-runtime-validation.md` |

### level-5-continuity

| Scenario | Status | Evidence |
|---|---|---|
| `enterprise-change-continuity` | OK | `scenarios/level-5-continuity/enterprise-change-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-cloud-continuity` | OK | `scenarios/level-5-continuity/enterprise-cloud-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-control-plane-continuity` | OK | `scenarios/level-5-continuity/enterprise-control-plane-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-data-protection-continuity` | OK | `scenarios/level-5-continuity/enterprise-data-protection-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-identity-continuity` | OK | `scenarios/level-5-continuity/enterprise-identity-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-network-continuity` | OK | `scenarios/level-5-continuity/enterprise-network-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-operational-continuity` | OK | `scenarios/level-5-continuity/enterprise-operational-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-platform-continuity` | OK | `scenarios/level-5-continuity/enterprise-platform-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-security-continuity` | OK | `scenarios/level-5-continuity/enterprise-security-continuity/evidence/generated/lab-runtime-validation.md` |
| `enterprise-service-continuity-coordination` | OK | `scenarios/level-5-continuity/enterprise-service-continuity-coordination/evidence/generated/lab-runtime-validation.md` |
