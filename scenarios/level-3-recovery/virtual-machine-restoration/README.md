# Virtual Machine Restoration

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | virtual-machine-restoration |
| Lifecycle Level | level-3-recovery |
| Scenario Path | scenarios/level-3-recovery/virtual-machine-restoration |
| Scenario Type | Recovery / Automation |
| Primary Domain | Virtual Machine |
| Status | draft |

---

## Overview

This scenario documents virtual machine restoration within the virtual machine operational domain.
It focuses on virtual machine, hypervisor, guest OS, compute host and demonstrates how
infrastructure operations teams can use domain-specific telemetry, lifecycle workflow design, and
evidence-backed validation to support execute controlled recovery, restoration, failover, or
mitigation workflow.

---

## Objectives

- Define the scenario-specific virtual machine signal represented by virtual-machine-restoration.
- Identify the affected virtual machine components and dependencies.
- Collect and interpret telemetry from virtual machine, hypervisor, guest OS, compute host.
- Use health status as an operational signal for detection or validation.
- Use availability signal as an operational signal for detection or validation.
- Use latency as an operational signal for detection or validation.
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

- Virtual Machine
- Hypervisor
- Guest Os
- Compute Host
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

health status; availability signal; latency; error indicator; event log; metric threshold

---

## Correlation and Analysis

Correlate virtual machine signals with related infrastructure state, dependencies, recent events,
and service impact.

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

Monitoring and visibility include health status; availability signal; latency; error indicator;
event log; metric threshold.

---

## Operational Components

| Component | Purpose |
|---|---|
| Virtual Machine | Provides context or signal source for Virtual Machine operations |
| Hypervisor | Provides context or signal source for Virtual Machine operations |
| Guest Os | Provides context or signal source for Virtual Machine operations |
| Compute Host | Provides context or signal source for Virtual Machine operations |
| Telemetry Source | Provides context or signal source for Virtual Machine operations |
| Detection Logic | Provides context or signal source for Virtual Machine operations |
| Evidence Output | Provides context or signal source for Virtual Machine operations |
| Correlation Logic | Connects related signals, dependencies, and impact context |
| Validation Method | Confirms stable state, restored condition, or visibility completeness |

---

<!-- L3_RECOVERY_CONTENT_START -->

## Recovery Scope

This scenario defines the recovery scope for **Virtual Machine Restoration**. It focuses on restoring the affected capability through controlled orchestration, automation execution, and validation.

- **Primary recovery target:** virtual machine, hypervisor, guest OS, compute host
- **Operational focus:** Execute controlled recovery, restoration, failover, or mitigation workflow

The recovery boundary includes confirmed failure detection, incident context, recovery trigger evaluation, automation execution, rollback handling, and post-recovery validation.

## Recovery Trigger Conditions

Recovery execution is required when one or more of the following conditions are observed:

- The affected capability is unavailable, unstable, or unable to serve its expected operational role.
- Correlation confirms that the issue is not limited to transient telemetry noise.
- Manual observation or automated analysis identifies a recoverable failure condition.
- The incident requires a repeatable recovery workflow rather than ad-hoc operator action.
- Validation evidence is required before the incident can be closed.

## Failure Signals

The following telemetry signals are used to determine recovery eligibility and execution priority:

- health status
- availability signal
- latency
- error indicator
- event log
- metric threshold

## Recovery Decision Criteria

The recovery workflow should only proceed when the affected resource, dependency context, and expected recovery action are clear.

Recovery should be executed when:

- The affected target matches the defined recovery scope.
- The failure condition is confirmed by telemetry or incident analysis.
- The recovery action has a known validation method.
- The automation path is available and safe to execute.
- Rollback or escalation is available if the recovery action fails.

## Recovery Orchestration Workflow

1. Confirm the affected resource and failure condition.
2. Correlate telemetry signals with the current incident context.
3. Select the recovery workflow that matches the failure scope.
4. Execute the recovery action through the assigned automation path.
5. Monitor execution status and collect recovery evidence.
6. Validate that the affected capability has returned to an acceptable operational state.
7. Escalate to resilience or continuity coordination if direct recovery fails.

## Operational Modules

- Recovery Orchestration Module
- Automation Execution Module
- Recovery Validation Module

## Integration Adapters

- Ansible Adapter
- Prometheus Adapter
- Grafana Adapter

## Automation Execution Boundary

This scenario assumes that recovery automation is controlled, observable, and reversible where possible. It does not assume blind execution of remediation commands.

Automation should be blocked or escalated when:

- The target resource cannot be confidently identified.
- Telemetry signals are contradictory or incomplete.
- The recovery action may increase blast radius.
- Required credentials, control plane access, or execution path is unavailable.
- Validation cannot confirm the recovery result.

## Recovery Validation

Recovery validation must prove that the affected capability has returned to a stable state. Validation includes:

- Resource health or reachability check
- Service or dependency availability check
- Error, latency, or failure signal reduction
- Automation execution status
- Evidence artifact generation

## Rollback and Escalation

If the recovery action fails or produces unstable results, the workflow must either roll back to the last known safe state or escalate to higher-level resilience coordination.

Escalation is required when:

- Recovery execution fails.
- The same failure repeats after recovery.
- Dependent services remain degraded.
- The affected capability requires failover, rerouting, or cross-domain coordination.
- Operator approval is required for further action.

## Acceptance Criteria

This scenario is considered complete when:

- The affected capability is restored or safely contained.
- Recovery execution evidence is available.
- Validation confirms operational stability.
- Any residual risk is documented.
- Incident status can be closed or escalated with clear evidence.

<!-- L3_RECOVERY_CONTENT_END -->

<!-- OPERATIONAL_INTERPRETATION_START -->

## Operational Interpretation

This scenario should be interpreted as an operational workflow for **hybrid infrastructure operations** within the **controlled recovery orchestration and validation** lifecycle. The goal is not to document a single tool action, but to show how operational signals, platform capabilities, and validation evidence are organized into a repeatable infrastructure operations pattern.

## Failure / Risk Context

The primary operational risk is **unvalidated automation, unsafe remediation, and incomplete service restoration**. In the context of **Virtual Machine Restoration**, this means the workflow must clearly separate observable symptoms, dependency context, response boundaries, and validation evidence.

## Operator Decision Points

Operators reviewing this scenario should be able to determine **whether recovery automation should execute, pause, roll back, or escalate based on validation evidence**. The scenario therefore emphasizes decision quality, evidence readiness, and operational traceability rather than isolated implementation steps.

## Reviewer Notes

This scenario demonstrates recovery automation boundaries, validation gates, and operational control.

<!-- OPERATIONAL_INTERPRETATION_END -->

<!-- OPERATIONAL_DECISION_MATRIX_START -->

## Operational Decision Matrix

### Recovery Decision Matrix

| State | Operational Condition | Operator Decision |
|---|---|---|
| Normal | Target service or infrastructure state is stable. | No recovery action required; retain readiness evidence. |
| Warning | Recovery condition is suspected but not fully qualified. | Pause automation and validate incident context. |
| Critical | Recovery condition is confirmed and action boundary is defined. | Execute approved recovery workflow or escalate if unsafe. |
| Validation | Post-recovery state and evidence are available. | Mark recovery workflow as validated or incomplete. |

### Decision Principle

The decision matrix defines how the scenario should be interpreted during review. It does not claim live production execution. It describes operational decision boundaries, escalation conditions, and validation expectations for the scenario lifecycle.

<!-- OPERATIONAL_DECISION_MATRIX_END -->

<!-- OPERATIONAL_REVIEW_NOTES_START -->

## Operational Review Notes

### Review Focus

This scenario should be reviewed for **controlled recovery workflow, automation boundary, rollback decision, and post-action validation**.

### Reviewer Questions

- Can the reviewer understand what condition triggers recovery?
- Is the automation boundary clearly defined?
- Does the workflow include validation after recovery?
- Are failure, pause, rollback, or escalation paths understandable?

### Review Boundary

The scenario should not present automation as safe without qualification, validation, or operator decision points.

### Acceptance Perspective

The scenario is acceptable when its operational intent, lifecycle boundary, decision points, evidence outputs, and reviewer-facing interpretation are clear without requiring direct access to a live production environment.

<!-- OPERATIONAL_REVIEW_NOTES_END -->



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

- [Traffic Restoration Workflow](/snsd-hybridinfra/scenarios/level-3-recovery/traffic-restoration-workflow/README.md)
- [Vpn Tunnel Recovery Automation](/snsd-hybridinfra/scenarios/level-3-recovery/vpn-tunnel-recovery-automation/README.md)
- [Security Anomaly Correlation](/snsd-hybridinfra/scenarios/level-2-correlation/security-anomaly-correlation/README.md)
- [Storage Replication Resilience](/snsd-hybridinfra/scenarios/level-4-resilience/storage-replication-resilience/README.md)

## Summary

This scenario contributes to the infrastructure operations portfolio by documenting virtual machine workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.
