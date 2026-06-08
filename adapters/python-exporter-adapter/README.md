# Python Exporter Adapter

## Integration Target

Python-based custom telemetry exporters

## Adapter Purpose

Provides custom signal collection for scenarios where standard telemetry sources do not fully capture the required operational condition.

## Operational Boundary

This adapter exposes custom telemetry signals. It does not replace centralized monitoring, correlation, or recovery orchestration modules.

## Inputs

- custom collection script
- target endpoint or resource
- exporter configuration
- scenario-specific signal definition

## Outputs

- custom metric or signal
- exporter execution evidence
- scenario-specific visibility data
- telemetry enrichment context

## Failure Mode

If custom collection fails, the adapter reports exporter failure separately from the infrastructure condition being observed.

## Scenario Usage

Scenarios reference this adapter when the workflow requires integration with the target system. The adapter supports telemetry collection, execution context, visualization, evidence generation, or validation depending on the scenario lifecycle level.

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
