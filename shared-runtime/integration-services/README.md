# Integration Services

## Runtime Purpose

Defines shared integration boundaries between modules, adapters, telemetry sources, automation systems, and reporting outputs.

## Runtime Boundary

This runtime layer coordinates integration patterns. It does not own the semantics of individual modules or adapters.

## Inputs

- adapter request
- module context
- target system reference
- scenario integration requirement

## Outputs

- integration result
- adapter handoff context
- integration evidence
- failure or retry context

## Operational Role

Integration services keep external tool interaction separate from reusable operational capability logic.

## Failure / Consistency Handling

If an integration fails, the failure should be isolated, recorded, and handed back to the scenario workflow.

## Scenario Usage

Scenarios use this shared runtime structure to keep operational workflows consistent across lifecycle levels. The runtime layer supports repeatable orchestration, telemetry handling, evidence generation, and integration behavior without turning each scenario into a one-off implementation note.

<!-- RUNTIME_CONTRACT_START -->

## Runtime Contract

### Responsibility

Defines shared integration behavior between modules, adapters, telemetry sources, automation systems, and reports.

### Non-Responsibility

Does not own module capability semantics or adapter-specific implementation details.

### Runtime Scope

Adapter invocation, module-to-adapter handoff, integration result capture, retry context, and failure isolation.

### Input Contract

- adapter request
- module context
- target system reference
- scenario integration requirement
- execution or query parameters

### Output Contract

- integration result
- adapter handoff context
- integration evidence
- failure or retry context
- downstream workflow signal

### Consistency Rule

Integration behavior must keep tool-specific boundaries separate from reusable operational capability logic.

### Failure Mode

Integration failures must be isolated, recorded, and returned to the scenario workflow without hiding the failure.

<!-- RUNTIME_CONTRACT_END -->

## Implementation Note

This directory describes reusable platform mechanics. It is intentionally separated from scenario README files, operational modules, and external adapters.
