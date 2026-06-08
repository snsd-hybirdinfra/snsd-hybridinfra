# Prometheus Adapter

## Integration Target

Prometheus-compatible metric collection and query interface

## Adapter Purpose

Provides metric-based telemetry input for visibility, correlation, recovery validation, and operational evidence workflows.

## Operational Boundary

This adapter collects and exposes metric signals. It does not decide incident severity, execute remediation, or define recovery policy.

## Inputs

- Prometheus scrape targets
- metric queries
- health and availability metrics
- threshold or baseline references

## Outputs

- scenario-ready metric signals
- time-series evidence
- alert candidate context
- validation metric references

## Failure Mode

If metrics are missing, stale, or inconsistent, the adapter should expose telemetry gaps rather than allowing unsupported downstream conclusions.

## Scenario Usage

Scenarios reference this adapter when the workflow requires integration with the target system. The adapter supports telemetry collection, execution context, visualization, evidence generation, or validation depending on the scenario lifecycle level.

<!-- ADAPTER_CONTRACT_START -->

## Integration Contract

### Responsibility

Provides metric-based telemetry input for visibility, correlation, alert readiness, and validation workflows.

### Non-Responsibility

Does not decide incident severity, execute remediation, or define operational policy.

### Integration Target

Prometheus metrics, scrape targets, alert candidate signals, and time-series query results.

### Input Contract

- metric query
- scrape target reference
- time window
- threshold or baseline context

### Output Contract

- scenario-ready metric signal
- time-series evidence
- health or availability context
- validation metric reference

### Failure Mode

Missing, stale, or inconsistent metrics must be surfaced as telemetry gaps before downstream analysis proceeds.

### Scenario Usage

Used by monitoring, visibility, correlation, recovery validation, and resilience validation scenarios.

<!-- ADAPTER_CONTRACT_END -->

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
