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

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
