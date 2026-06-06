# Service Mesh Traffic Restoration

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | service-mesh-traffic-restoration |
| Lifecycle Level | level-3-recovery |
| Scenario Path | scenarios/level-3-recovery/service-mesh-traffic-restoration |
| Scenario Type | Recovery / Automation |
| Primary Domain | Service Mesh |
| Status | draft |

---

## Overview

This scenario documents service mesh traffic restoration within the service mesh operational domain.
It focuses on service mesh route, sidecar proxy, service dependency, traffic policy and demonstrates
how infrastructure operations teams can use domain-specific telemetry, lifecycle workflow design,
and evidence-backed validation to support execute controlled recovery, restoration, failover, or
mitigation workflow.

---

## Objectives

- Define the scenario-specific service mesh signal represented by service-mesh-traffic-restoration.
- Identify the affected service mesh components and dependencies.
- Collect and interpret telemetry from service mesh route, sidecar proxy, service dependency, traffic policy.
- Use service health as an operational signal for detection or validation.
- Use request latency as an operational signal for detection or validation.
- Use error rate as an operational signal for detection or validation.
- Document the lifecycle workflow from detection through validation.
- Produce reviewer-readable evidence artifacts for portfolio assessment.

---

## Scenario Architecture

![Operational Poster](diagrams/operational-poster.png)

---

## Used Modules

- Recovery Orchestration Module
- Automation Execution Module
- Recovery Validation Module

---

## Used Adapters

- Ansible Adapter
- Prometheus Adapter
- Grafana Adapter

---

## Infrastructure Components

- Service Mesh Route
- Sidecar Proxy
- Service Dependency
- Traffic Policy
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

service health; request latency; error rate; dependency call failure; mesh traffic; endpoint
availability

---

## Correlation and Analysis

Correlate service mesh signals with related infrastructure state, dependencies, recent events, and
service impact.

---

## Alert and Incident Workflow

Execute controlled recovery, restoration, failover, or mitigation workflow

---

## Recovery and Automation Workflow

Execute controlled recovery, restoration, failover, or mitigation workflow

---

## Recovery Validation

Validate stable state, evidence completeness, and operational readiness after detection, analysis,
response, or recovery.

---

## Monitoring and Visibility

Monitoring and visibility include service health; request latency; error rate; dependency call
failure; mesh traffic; endpoint availability.

---

## Operational Components

| Component | Purpose |
|---|---|
| Service Mesh Route | Provides context or signal source for Service Mesh operations |
| Sidecar Proxy | Provides context or signal source for Service Mesh operations |
| Service Dependency | Provides context or signal source for Service Mesh operations |
| Traffic Policy | Provides context or signal source for Service Mesh operations |
| Telemetry Source | Provides context or signal source for Service Mesh operations |
| Detection Logic | Provides context or signal source for Service Mesh operations |
| Evidence Output | Provides context or signal source for Service Mesh operations |
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

- /snsd-hybridinfra/scenarios/level-2-correlation/service-mesh-latency-correlation

### Same-Level Scenarios

None currently defined.

### Downstream Scenarios

None currently defined.

### Cross-Domain Scenarios

None currently defined.

---

## Summary

This scenario contributes to the infrastructure operations portfolio by documenting service mesh workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.
