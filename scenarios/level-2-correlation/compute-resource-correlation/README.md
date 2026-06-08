# Compute Resource Correlation

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | compute-resource-correlation |
| Lifecycle Level | level-2-correlation |
| Scenario Path | scenarios/level-2-correlation/compute-resource-correlation |
| Scenario Type | Correlation / Analysis |
| Primary Domain | Compute / Resource |
| Status | draft |

---

## Overview

This scenario documents compute resource correlation within the compute / resource operational
domain. It focuses on compute node, instance, CPU, memory, disk, runtime host and demonstrates how
infrastructure operations teams can use domain-specific telemetry, lifecycle workflow design, and
evidence-backed validation to support correlate related symptoms, dependencies, and impact paths.

---

## Objectives

- Define the scenario-specific compute / resource signal represented by compute-resource-correlation.
- Identify the affected compute / resource components and dependencies.
- Collect and interpret telemetry from compute node, instance, CPU, memory, disk, runtime host.
- Use CPU usage as an operational signal for detection or validation.
- Use memory usage as an operational signal for detection or validation.
- Use disk pressure as an operational signal for detection or validation.
- Document the lifecycle workflow from detection through validation.
- Produce reviewer-readable evidence artifacts for portfolio assessment.

---

## Scenario Architecture

![Operational Poster](diagrams/operational-poster.png)

---

## Used Modules

- Telemetry Aggregation Module
- Dependency Correlation Module
- Impact Analysis Module

---

## Used Adapters

- Prometheus Adapter
- Grafana Adapter
- OpenSearch Adapter

---

## Infrastructure Components

- Compute Node
- Instance
- Cpu
- Memory
- Disk
- Runtime Host
- Telemetry Source
- Detection Logic
- Evidence Output

---

## Operational Workflow

The scenario follows the infrastructure operations lifecycle:

1. Detection
2. Correlation and Analysis
3. Incident Coordination
4. Recovery and Automation
5. Recovery Validation
6. Governance and Reporting

---

## Detection Workflow

CPU usage; memory usage; disk pressure; instance status; host health; reboot event; availability
state

---

## Correlation and Analysis

Correlate compute / resource signals with related infrastructure state, dependencies, recent events,
and service impact.

---

## Alert and Incident Workflow

Correlate related symptoms, dependencies, and impact paths

---

## Recovery and Automation Workflow

Correlate related symptoms, dependencies, and impact paths

---

## Recovery Validation

Validate stable state, evidence completeness, and operational readiness after detection, analysis,
response, or recovery.

---

## Monitoring and Visibility

Monitoring and visibility include CPU usage; memory usage; disk pressure; instance status; host
health; reboot event; availability state.

---

## Operational Components

| Component | Purpose |
|---|---|
| Compute Node | Provides context or signal source for Compute / Resource operations |
| Instance | Provides context or signal source for Compute / Resource operations |
| Cpu | Provides context or signal source for Compute / Resource operations |
| Memory | Provides context or signal source for Compute / Resource operations |
| Disk | Provides context or signal source for Compute / Resource operations |
| Runtime Host | Provides context or signal source for Compute / Resource operations |
| Telemetry Source | Provides context or signal source for Compute / Resource operations |
| Detection Logic | Provides context or signal source for Compute / Resource operations |
| Evidence Output | Provides context or signal source for Compute / Resource operations |
| Correlation Logic | Connects related signals, dependencies, and impact context |
| Validation Method | Confirms stable state, restored condition, or visibility completeness |

---

## Evidence

- [Evidence Summary](evidence/generated/summary.md)
- [Execution Evidence](evidence/generated/execution-evidence.md)
- [Validation Evidence](evidence/generated/validation-evidence.md)
- [Artifact Manifest](evidence/generated/artifact-manifest.json)
- [Artifact Checksums](evidence/generated/artifact-checksums.json)

---

## Expected Outcomes

- The scenario has domain-specific operational context.
- Telemetry signals are identified and mapped to the scenario purpose.
- Infrastructure components and dependencies are documented.
- Lifecycle workflow sections are populated with scenario-specific content.
- Validation and evidence outputs are defined for portfolio review.

---

## Validation Checklist

- [ ] Scenario metadata is present.
- [ ] Operational poster reference is preserved.
- [ ] Used modules are listed.
- [ ] Used adapters are listed.
- [ ] Detection workflow is scenario-specific.
- [ ] Correlation and analysis workflow is scenario-specific.
- [ ] Response or recovery workflow is described.
- [ ] Recovery validation is described.
- [ ] Evidence links are present.
- [ ] Deprecated diagram references are not used.

---

## Related Scenarios

### Upstream Scenarios

None currently defined.

### Same-Level Scenarios

None currently defined.

### Downstream Scenarios

None currently defined.

### Cross-Domain Scenarios

None currently defined.

---

## Summary

This scenario contributes to the infrastructure operations portfolio by documenting compute / resource workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.

