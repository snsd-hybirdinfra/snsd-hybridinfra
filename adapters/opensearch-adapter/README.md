# OpenSearch Adapter

## Integration Target

OpenSearch log and event query interface

## Adapter Purpose

Provides log and event search capability for correlation, investigation, evidence generation, and reviewer-facing incident context.

## Operational Boundary

This adapter queries log and event data. It does not determine final root cause or execute remediation.

## Inputs

- log index reference
- event query
- time window
- scenario investigation context

## Outputs

- event evidence
- log correlation context
- incident investigation reference
- validation support data

## Failure Mode

If log data is incomplete or unavailable, the adapter marks the evidence gap and avoids presenting partial logs as complete operational proof.

## Scenario Usage

Scenarios reference this adapter when the workflow requires integration with the target system. The adapter supports telemetry collection, execution context, visualization, evidence generation, or validation depending on the scenario lifecycle level.

<!-- ADAPTER_CONTRACT_START -->

## Integration Contract

### Responsibility

Provides log and event query access for investigation, correlation, and evidence generation.

### Non-Responsibility

Does not determine final root cause or execute remediation.

### Integration Target

OpenSearch indexes, log events, event queries, and investigation time windows.

### Input Contract

- index or data source reference
- query condition
- time window
- scenario investigation context

### Output Contract

- event evidence
- log correlation context
- incident investigation reference
- validation support data

### Failure Mode

If log data is incomplete, unavailable, or outside the time window, the evidence gap must be explicitly preserved.

### Scenario Usage

Used by correlation, security analysis, runtime investigation, and evidence-oriented scenarios.

<!-- ADAPTER_CONTRACT_END -->

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
