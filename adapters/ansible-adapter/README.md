# Ansible Adapter

## Integration Target

Ansible automation execution boundary

## Adapter Purpose

Provides controlled automation execution support for recovery, remediation, provisioning, and validation workflows.

## Operational Boundary

This adapter invokes automation tasks when called by a module or workflow. It does not independently decide whether recovery should occur.

## Inputs

- playbook or task reference
- target inventory scope
- execution variables
- operator-approved workflow context

## Outputs

- task execution result
- changed or failed state
- automation log reference
- execution evidence

## Failure Mode

If execution fails, the adapter preserves task output and returns failure context to the recovery orchestration or validation workflow.

## Scenario Usage

Scenarios reference this adapter when the workflow requires integration with the target system. The adapter supports telemetry collection, execution context, visualization, evidence generation, or validation depending on the scenario lifecycle level.

<!-- ADAPTER_CONTRACT_START -->

## Integration Contract

### Responsibility

Provides an automation execution bridge for approved operational workflows.

### Non-Responsibility

Does not decide whether automation should run and does not define recovery policy.

### Integration Target

Ansible playbooks, inventories, task execution output, and automation control node context.

### Input Contract

- playbook or task reference
- target inventory scope
- execution variables
- approved workflow trigger

### Output Contract

- task execution result
- changed or failed state
- automation log reference
- execution evidence

### Failure Mode

Execution failure must be returned to the invoking module with task output and failure reason preserved.

### Scenario Usage

Used by recovery and automation scenarios that require controlled remediation or infrastructure task execution.

<!-- ADAPTER_CONTRACT_END -->

## Implementation Note

This adapter describes an integration boundary. It is intentionally separated from operational modules so that tool integration remains distinct from reusable operational capability logic.
