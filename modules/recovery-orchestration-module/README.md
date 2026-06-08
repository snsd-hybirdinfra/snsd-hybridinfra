# Recovery Orchestration Module

## Capability Purpose

Coordinates recovery workflows after incident qualification and before final recovery validation.

## Operational Boundary

This module controls recovery sequencing, execution handoff, rollback decision points, and validation gates. It does not collect raw telemetry directly.

## Inputs

- qualified incident context
- recovery candidate action
- target service or infrastructure scope
- pre-recovery validation state

## Outputs

- recovery workflow status
- automation execution handoff
- rollback or escalation decision
- post-recovery validation request

## Failure Handling Role

If recovery cannot be safely completed, the module pauses execution, preserves evidence, and escalates for operator review.

## Validation Evidence

Validation checks whether recovery action, post-state evidence, rollback criteria, and service restoration evidence are complete.

## Scenario Usage

This module is referenced by scenarios when the workflow requires this reusable operational capability. Scenario README files use module references to show how platform capabilities are composed into lifecycle-aligned operational workflows.

<!-- MODULE_CONTRACT_START -->

## Capability Contract

### Responsibility

Coordinates recovery sequence, automation handoff, rollback decision points, and post-recovery validation.

### Non-Responsibility

Does not collect raw telemetry directly or bypass validation gates.

### Input Contract

- qualified incident context
- recovery candidate action
- target service or infrastructure scope
- pre-recovery validation state

### Output Contract

- recovery workflow status
- automation handoff request
- rollback or escalation decision
- post-recovery validation request

### Lifecycle Contribution

Primarily contributes to Level 3 recovery and supports Level 4 resilience workflows.

### Failure Mode

Unsafe or incomplete recovery must pause and escalate rather than forcing completion.

### Example Scenario Usage

Used by vpn-tunnel-recovery-automation and database-recovery-orchestration scenarios.

<!-- MODULE_CONTRACT_END -->

## Implementation Note

This module describes a reusable capability boundary, not a single tool, product, or vendor-specific implementation.
