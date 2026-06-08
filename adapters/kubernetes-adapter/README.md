# Kubernetes Adapter

## Integration Target

Kubernetes cluster API and workload state

## Adapter Purpose

Provides cluster, node, pod, service, and control-plane state context for platform operations scenarios.

## Operational Boundary

This adapter exposes Kubernetes operational state. It does not define application architecture or independently perform failover decisions.

## Inputs

- cluster health state
- node and pod status
- service and deployment state
- control-plane availability signals

## Outputs

- cluster operational context
- workload health evidence
- platform dependency signals
- recovery or resilience validation references

## Failure Mode

If Kubernetes API access is unavailable, the adapter reports control-plane visibility loss and prevents unsafe assumptions about workload state.

## Scenario Usage

Scenarios reference this adapter when the workflow requires integration with the target system. The adapter supports telemetry collection, execution context, visualization, evidence generation, or validation depending on the scenario lifecycle level.

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
