# Evidence Runtime

## Runtime Purpose

Defines shared evidence generation, artifact tracking, and validation reporting patterns.

## Runtime Boundary

This runtime layer produces evidence outputs. It does not decide operational severity or perform remediation.

## Inputs

- workflow result
- validation criteria
- artifact references
- scenario execution context

## Outputs

- evidence summary
- artifact manifest
- validation report
- reviewer-readable operational record

## Operational Role

The evidence runtime makes scenario outcomes traceable and reviewable.

## Failure / Consistency Handling

If evidence is incomplete, the workflow should mark the scenario as not fully validated instead of reporting false success.

## Scenario Usage

Scenarios use this shared runtime structure to keep operational workflows consistent across lifecycle levels. The runtime layer supports repeatable orchestration, telemetry handling, evidence generation, and integration behavior without turning each scenario into a one-off implementation note.

<!-- RUNTIME_CONTRACT_START -->

## Runtime Contract

### Responsibility

Produces and organizes generated evidence, artifact manifests, checksums, and validation reports.

### Non-Responsibility

Does not claim live production execution unless connected to an actual execution environment.

### Runtime Scope

Evidence summaries, validation evidence, execution evidence, artifact manifests, and checksum records.

### Input Contract

- scenario metadata
- workflow result
- validation criteria
- artifact references
- scenario execution context

### Output Contract

- summary.md
- validation-evidence.md
- execution-evidence.md
- artifact-manifest.json
- artifact-checksums.json

### Consistency Rule

Generated evidence must be reviewer-readable and must clearly state its documentation-evidence boundary.

### Failure Mode

If evidence is incomplete, validation must remain incomplete rather than reporting false success.

<!-- RUNTIME_CONTRACT_END -->

## Implementation Note

This directory describes reusable platform mechanics. It is intentionally separated from scenario README files, operational modules, and external adapters.
