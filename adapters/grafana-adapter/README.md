# Grafana Adapter

## Integration Target

Grafana dashboards and visualization references

## Adapter Purpose

Provides dashboard visibility and reviewer-facing operational visualization context for scenario workflows.

## Operational Boundary

This adapter represents dashboard and visualization integration. It does not collect raw telemetry or execute operational actions.

## Inputs

- dashboard references
- panel definitions
- metric visualization requirements
- scenario visibility context

## Outputs

- dashboard reference
- visual operational context
- reviewer-facing visibility evidence
- monitoring view alignment

## Failure Mode

If dashboard references are unavailable, the scenario should still preserve telemetry evidence and mark visualization as incomplete.

## Scenario Usage

Scenarios reference this adapter when the workflow requires integration with the target system. The adapter supports telemetry collection, execution context, visualization, evidence generation, or validation depending on the scenario lifecycle level.

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
