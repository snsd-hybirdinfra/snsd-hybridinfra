# Compute Foundation Module

## Capability Purpose

Defines compute resource context used by visibility, correlation, recovery, and resilience scenarios.

## Operational Boundary

This module represents compute capacity, instance health, resource allocation, and host-level operational context. It does not perform recovery execution by itself.

## Inputs

- instance or node health state
- CPU, memory, and runtime metrics
- compute placement or availability context
- resource pressure indicators

## Outputs

- compute health context
- resource pressure evidence
- capacity-related operational signal
- scenario-ready compute dependency context

## Failure Handling Role

Compute degradation is escalated to correlation or recovery modules when resource exhaustion, instance failure, or host instability affects service operation.

## Validation Evidence

Validation checks whether compute state, resource metrics, and recovery evidence align with expected operational health.

## Scenario Usage

This module is referenced by scenarios when the workflow requires this reusable operational capability. Scenario README files use module references to show how platform capabilities are composed into lifecycle-aligned operational workflows.

## Implementation Note

This module describes a reusable capability boundary, not a single tool, product, or vendor-specific implementation.
