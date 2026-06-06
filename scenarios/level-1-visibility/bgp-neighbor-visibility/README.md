# Bgp Neighbor Visibility

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | bgp-neighbor-visibility |
| Lifecycle Level | level-1-visibility |
| Scenario Path | scenarios/level-1-visibility/bgp-neighbor-visibility |
| Scenario Type | Visibility / Monitoring |
| Primary Domain | Network / Routing |
| Status | draft |

---

## Overview

This scenario documents bgp neighbor visibility within the network / routing operational domain. It
focuses on BGP neighbor, router, route table, WAN path and demonstrates how infrastructure
operations teams can use domain-specific telemetry, lifecycle workflow design, and evidence-backed
validation to support detect and expose operational health signals before incident escalation.

---

## Objectives

- Define the scenario-specific network / routing signal represented by bgp-neighbor-visibility.
- Identify the affected network / routing components and dependencies.
- Collect and interpret telemetry from BGP neighbor, router, route table, WAN path.
- Use link status as an operational signal for detection or validation.
- Use route change as an operational signal for detection or validation.
- Use BGP state as an operational signal for detection or validation.
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

- Bgp Neighbor
- Router
- Route Table
- Wan Path
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

link status; route change; BGP state; packet loss; latency; interface utilization; traffic volume

---

## Correlation and Analysis

Correlate network / routing signals with related infrastructure state, dependencies, recent events,
and service impact.

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

Monitoring and visibility include link status; route change; BGP state; packet loss; latency;
interface utilization; traffic volume.

---

## Operational Components

| Component | Purpose |
|---|---|
| Bgp Neighbor | Provides context or signal source for Network / Routing operations |
| Router | Provides context or signal source for Network / Routing operations |
| Route Table | Provides context or signal source for Network / Routing operations |
| Wan Path | Provides context or signal source for Network / Routing operations |
| Telemetry Source | Provides context or signal source for Network / Routing operations |
| Detection Logic | Provides context or signal source for Network / Routing operations |
| Evidence Output | Provides context or signal source for Network / Routing operations |
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

- /snsd-hybridinfra/scenarios/level-1-visibility/network-path-visibility
- /snsd-hybridinfra/scenarios/level-1-visibility/network-traffic-visibility

### Downstream Scenarios

- /snsd-hybridinfra/scenarios/level-2-correlation/cross-region-network-anomaly-correlation

### Cross-Domain Scenarios

None currently defined.

---

## Summary

This scenario contributes to the infrastructure operations portfolio by documenting network / routing workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.
