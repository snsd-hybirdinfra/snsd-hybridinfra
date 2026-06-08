# Scenario Review Entry Points

## Purpose

This document defines practical review entry points for the SNSD Hybrid Infrastructure scenario catalog.

The repository contains lifecycle-based operational scenarios across visibility, correlation, recovery, resilience, and continuity. These entries provide a reviewer-friendly starting point for understanding the lifecycle model without requiring the reviewer to inspect every scenario first.

## Review Entry Points

| Lifecycle Level | Scenario | Review Purpose |
|---|---|---|
| Level 1 Visibility | [VPN Connectivity Monitoring](../scenarios/level-1-visibility/vpn-connectivity-monitoring/README.md) | Review signal visibility, monitoring readiness, and baseline operational evidence |
| Level 2 Correlation | [VPN Latency Correlation](../scenarios/level-2-correlation/vpn-latency-correlation/README.md) | Review dependency correlation, latency interpretation, and incident qualification |
| Level 3 Recovery | [VPN Tunnel Recovery Automation](../scenarios/level-3-recovery/vpn-tunnel-recovery-automation/README.md) | Review controlled recovery workflow, automation boundary, and post-action validation |
| Level 4 Resilience | [Multi Site Routing Failover](../scenarios/level-4-resilience/multi-site-routing-failover/README.md) | Review distributed resilience coordination, routing failover, and survivability validation |
| Level 5 Continuity | [Enterprise Network Continuity](../scenarios/level-5-continuity/enterprise-network-continuity/README.md) | Review enterprise continuity posture, governance-facing evidence, and recovery assurance |

## Review Boundary

These entries are review starting points.

They are not a golden path, mandatory scenario chain, or exclusive validation route. The full catalog remains organized under the lifecycle-based scenario inventory.

## How to Review

A reviewer should use these entries to inspect:

- scenario README structure
- operational interpretation
- operational decision matrix
- operational review notes
- used modules
- used adapters
- generated evidence
- operational poster artifacts
- validation checklist
- related scenario policy

## Interpretation

The review entry points demonstrate how the repository models infrastructure operations across the lifecycle.

They help the reviewer understand the operational progression from visibility to correlation, recovery, resilience, and continuity without implying that every scenario must be connected linearly.
