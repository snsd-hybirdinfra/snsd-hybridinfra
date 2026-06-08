# Network Foundation Module

## Capability Purpose

Provides network topology, routing, connectivity, and path context for operational scenarios.

## Operational Boundary

This module represents network foundation context. It does not independently execute failover unless invoked by a recovery or resilience workflow.

## Inputs

- network path state
- routing or tunnel status
- connectivity signals
- gateway or link health

## Outputs

- network dependency context
- connectivity evidence
- routing or path visibility
- scenario-ready network state

## Failure Handling Role

Network foundation degradation is escalated when reachability, routing, or path health affects dependent services.

## Validation Evidence

Validation confirms path reachability, routing state, link health, and dependency impact evidence.

## Scenario Usage

This module is referenced by scenarios when the workflow requires this reusable operational capability. Scenario README files use module references to show how platform capabilities are composed into lifecycle-aligned operational workflows.

<!-- MODULE_CONTRACT_START -->

## Capability Contract

### Responsibility

Provides network topology, routing, connectivity, and path health context.

### Non-Responsibility

Does not independently perform failover unless invoked by a recovery or resilience workflow.

### Input Contract

- path reachability state
- routing status
- gateway or tunnel health
- link availability indicators

### Output Contract

- network health context
- connectivity evidence
- routing dependency signal
- network impact context

### Lifecycle Contribution

Supports visibility, correlation, recovery, and resilience workflows involving network operations.

### Failure Mode

If network reachability cannot be confirmed, dependent workflows must treat path state as unresolved.

### Example Scenario Usage

Used by vpn-connectivity-monitoring, network-path-visibility, and multi-site-routing-failover scenarios.

<!-- MODULE_CONTRACT_END -->

## Implementation Note

This module describes a reusable capability boundary, not a single tool, product, or vendor-specific implementation.
