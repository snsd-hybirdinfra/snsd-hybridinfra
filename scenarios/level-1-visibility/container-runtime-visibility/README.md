# Container Runtime Visibility

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | container-runtime-visibility |
| Lifecycle Level | level-1-visibility |
| Scenario Path | scenarios/level-1-visibility/container-runtime-visibility |
| Scenario Type | Visibility / Monitoring |
| Primary Domain | Container / Runtime |
| Status | draft |

---

## Overview

This scenario documents container runtime visibility within the container / runtime operational
domain. It focuses on container runtime, pod, workload, node, image runtime and demonstrates how
infrastructure operations teams can use domain-specific telemetry, lifecycle workflow design, and
evidence-backed validation to support detect and expose operational health signals before incident
escalation.

---

## Objectives

- Define the scenario-specific container / runtime signal represented by container-runtime-visibility.
- Identify the affected container / runtime components and dependencies.
- Collect and interpret telemetry from container runtime, pod, workload, node, image runtime.
- Use pod phase as an operational signal for detection or validation.
- Use restart count as an operational signal for detection or validation.
- Use container exit code as an operational signal for detection or validation.
- Document the lifecycle workflow from detection through validation.
- Produce reviewer-readable evidence artifacts for portfolio assessment.

---

## Scenario Architecture

![Operational Poster](diagrams/operational-poster.png)

---

## Used Modules

- Telemetry Aggregation Module
- Health Signal Collection Module
- Visibility Reporting Module

---

## Used Adapters

- Prometheus Adapter
- Grafana Adapter

---

## Infrastructure Components

- Container Runtime
- Pod
- Workload
- Node
- Image Runtime
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

pod phase; restart count; container exit code; readiness status; liveness status; CPU usage; memory
pressure

---

## Correlation and Analysis

Correlate container / runtime signals with related infrastructure state, dependencies, recent
events, and service impact.

---

## Alert and Incident Workflow

Detect and expose operational health signals before incident escalation

---

## Recovery and Automation Workflow

Detect and expose operational health signals before incident escalation

---

## Recovery Validation

Validate stable state, evidence completeness, and operational readiness after detection, analysis,
response, or recovery.

---

## Monitoring and Visibility

Monitoring and visibility include pod phase; restart count; container exit code; readiness status;
liveness status; CPU usage; memory pressure.

---

## Operational Components

| Component | Purpose |
|---|---|
| Container Runtime | Provides context or signal source for Container / Runtime operations |
| Pod | Provides context or signal source for Container / Runtime operations |
| Workload | Provides context or signal source for Container / Runtime operations |
| Node | Provides context or signal source for Container / Runtime operations |
| Image Runtime | Provides context or signal source for Container / Runtime operations |
| Telemetry Source | Provides context or signal source for Container / Runtime operations |
| Detection Logic | Provides context or signal source for Container / Runtime operations |
| Evidence Output | Provides context or signal source for Container / Runtime operations |
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

This scenario contributes to the infrastructure operations portfolio by documenting container / runtime workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.
