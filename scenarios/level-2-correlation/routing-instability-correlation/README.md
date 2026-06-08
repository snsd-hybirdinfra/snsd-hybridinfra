# Routing Instability Correlation

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | routing-instability-correlation |
| Lifecycle Level | level-2-correlation |
| Scenario Path | scenarios/level-2-correlation/routing-instability-correlation |
| Scenario Type | Correlation / Analysis |
| Primary Domain | Network / Routing |
| Status | draft |

---

## Overview

This scenario documents routing instability correlation within the network / routing operational
domain. It focuses on route table, routing path, router, service path and demonstrates how
infrastructure operations teams can use domain-specific telemetry, lifecycle workflow design, and
evidence-backed validation to support correlate related symptoms, dependencies, and impact paths.

---

## Objectives

- Define the scenario-specific network / routing signal represented by routing-instability-correlation.
- Identify the affected network / routing components and dependencies.
- Collect and interpret telemetry from route table, routing path, router, service path.
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
- Dependency Correlation Module
- Impact Analysis Module

---

## Used Adapters

- Prometheus Adapter
- Grafana Adapter
- OpenSearch Adapter

---

## Infrastructure Components

- Route Table
- Routing Path
- Router
- Service Path
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

Monitoring and visibility include link status; route change; BGP state; packet loss; latency;
interface utilization; traffic volume.

---

## Operational Components

| Component | Purpose |
|---|---|
| Route Table | Provides context or signal source for Network / Routing operations |
| Routing Path | Provides context or signal source for Network / Routing operations |
| Router | Provides context or signal source for Network / Routing operations |
| Service Path | Provides context or signal source for Network / Routing operations |
| Telemetry Source | Provides context or signal source for Network / Routing operations |
| Detection Logic | Provides context or signal source for Network / Routing operations |
| Evidence Output | Provides context or signal source for Network / Routing operations |
| Correlation Logic | Connects related signals, dependencies, and impact context |
| Validation Method | Confirms stable state, restored condition, or visibility completeness |

---

<!-- L2_CORRELATION_CONTENT_START -->

## Correlation Scope

This scenario defines the correlation scope for **Routing Instability Correlation**. It focuses on connecting telemetry symptoms, dependency context, and operational impact before recovery or escalation decisions are made.

- **Primary correlation target:** route table, routing path, router, service path
- **Operational focus:** Correlate related symptoms, dependencies, and impact paths

The correlation boundary includes telemetry normalization, dependency mapping, anomaly grouping, impact analysis, and incident handoff preparation.

## Correlation Trigger Conditions

Correlation is required when one or more observed signals are insufficient to explain the operational condition by themselves.

This scenario should enter correlation workflow when:

- Multiple telemetry signals appear related.
- A service symptom may be caused by an upstream infrastructure, platform, network, security, or data dependency.
- The affected component is unclear from a single alert.
- The issue may require recovery action but needs evidence before execution.
- Incident coordination requires a concise impact summary.

## Correlated Signals

The following telemetry signals are used as correlation input:

- link status
- route change
- BGP state
- packet loss
- latency
- interface utilization
- traffic volume

## Dependency Context

Correlation analysis evaluates how the affected target relates to upstream and downstream operational dependencies. This includes:

- Infrastructure dependency
- Platform or runtime dependency
- Network or routing dependency
- Service or application dependency
- Security, identity, or policy dependency
- Storage, database, or data path dependency

The objective is to determine whether the observed symptom is local, dependent, cascading, or cross-domain.

## Analysis Workflow

1. Collect telemetry from the affected resource and related dependencies.
2. Normalize signal timestamps, severity, and source context.
3. Group symptoms that occur within the same operational window.
4. Compare correlated signals against known dependency relationships.
5. Identify the most likely affected domain and impact boundary.
6. Produce an incident-ready correlation summary.
7. Recommend whether the next step is monitoring, incident coordination, recovery, or resilience escalation.

## Operational Modules

- Telemetry Aggregation Module
- Dependency Correlation Module
- Impact Analysis Module

## Integration Adapters

- Prometheus Adapter
- Grafana Adapter
- OpenSearch Adapter

## Incident Handoff Criteria

The scenario should hand off to incident coordination when correlation identifies a credible operational impact.

Handoff is required when:

- Affected service or infrastructure scope is identified.
- The issue is persistent or recurring.
- The correlated signals indicate user-facing, service-facing, or control-plane impact.
- Recovery action requires operator approval or automation execution.
- Evidence is sufficient to support an incident record.

## Recovery Readiness

L2 correlation does not execute recovery directly. It prepares the operational context needed for L3 recovery workflows.

Recovery readiness is established when:

- The affected target is identified.
- The likely failure domain is known.
- Related dependencies are documented.
- Recovery candidates are clear.
- Validation signals are available for post-recovery confirmation.

## Correlation Evidence

Evidence should demonstrate why the signals are considered related and how the impact boundary was determined.

Required evidence includes:

- Correlated telemetry summary
- Dependency impact notes
- Timeline of related signals
- Candidate root-cause or failure-domain statement
- Recommended next action

## Acceptance Criteria

This scenario is considered complete when:

- Related signals are grouped and explained.
- Affected dependency scope is identified.
- Incident handoff context is ready.
- Recovery readiness is either confirmed or explicitly not required.
- Evidence is available for operational review.

<!-- L2_CORRELATION_CONTENT_END -->

<!-- OPERATIONAL_INTERPRETATION_START -->

## Operational Interpretation

This scenario should be interpreted as an operational workflow for **network routing** within the **cross-signal correlation and dependency analysis** lifecycle. The goal is not to document a single tool action, but to show how operational signals, platform capabilities, and validation evidence are organized into a repeatable infrastructure operations pattern.

## Failure / Risk Context

The primary operational risk is **misdiagnosis, isolated symptom handling, and delayed incident qualification**. In the context of **Routing Instability Correlation**, this means the workflow must clearly separate observable symptoms, dependency context, response boundaries, and validation evidence.

## Operator Decision Points

Operators reviewing this scenario should be able to determine **whether multiple signals indicate a shared dependency, cascading condition, or localized anomaly**. The scenario therefore emphasizes decision quality, evidence readiness, and operational traceability rather than isolated implementation steps.

## Reviewer Notes

This scenario demonstrates operational reasoning across telemetry sources, dependencies, and incident handoff criteria.

<!-- OPERATIONAL_INTERPRETATION_END -->

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

- [Resource Contention Correlation](/snsd-hybridinfra/scenarios/level-2-correlation/resource-contention-correlation/README.md)
- [Runtime Instability Analysis](/snsd-hybridinfra/scenarios/level-2-correlation/runtime-instability-analysis/README.md)
- [Object Storage Health Monitoring](/snsd-hybridinfra/scenarios/level-1-visibility/object-storage-health-monitoring/README.md)
- [Storage Volume Recovery Automation](/snsd-hybridinfra/scenarios/level-3-recovery/storage-volume-recovery-automation/README.md)

## Summary

This scenario contributes to the infrastructure operations portfolio by documenting network / routing workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.
