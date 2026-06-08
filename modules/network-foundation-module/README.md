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

## Implementation Note

This module describes a reusable capability boundary, not a single tool, product, or vendor-specific implementation.
