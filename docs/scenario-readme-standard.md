# Scenario README Standard

## Purpose

This document defines the standard README structure for all scenario documents in this repository.

Each scenario README must present the scenario as part of a scenario-driven infrastructure operations portfolio. The README should be readable for technical reviewers, infrastructure engineers, and interviewers.

---

## Scenario README Principles

Each scenario README must be:

- scenario-centered
- infrastructure operations focused
- lifecycle aligned
- visually supported by one operational poster
- evidence-backed
- readable without internal tooling context

The README must not present the scenario as part of a commercial platform, AIOps product, or production runtime system.

---

## Required README Section Order

Each scenario README must follow this section order:

1. Scenario Metadata
2. Overview
3. Objectives
4. Scenario Architecture
5. Used Modules
6. Infrastructure Components
7. Operational Workflow
8. Detection Workflow
9. Correlation and Analysis
10. Alert and Incident Workflow
11. Recovery and Automation Workflow
12. Recovery Validation
13. Monitoring and Visibility
14. Operational Components
15. Evidence
16. Expected Outcomes
17. Validation Checklist
18. Related Scenarios
19. Summary

---

## Required Heading Structure

Each scenario README must use a single H1 title.

Example:

    # VPN Connectivity Monitoring

Major sections must use H2 headings.

Example:

    ## Scenario Metadata
    ## Overview
    ## Scenario Architecture
    ## Evidence
    ## Summary

Subsections may use H3 headings only when needed.

---

## Scenario Metadata Section

The Scenario Metadata section must summarize the scenario identity.

Required metadata table fields:

| Field | Description |
|---|---|
| Scenario Name | Human-readable scenario name |
| Scenario ID | Folder-based scenario identifier |
| Level | Operational maturity level |
| Focus Area | Main infrastructure operations focus |
| Primary Lifecycle Phase | Main lifecycle phase |
| Related Modules | Referenced operational modules |
| Related Adapters | Referenced integration adapters |

---

## Overview Section

The Overview section must explain the operational situation represented by the scenario.

It should answer:

- What operational problem does this scenario represent?
- Why does this scenario matter?
- What infrastructure area is affected?
- What operational capability does this scenario demonstrate?

---

## Objectives Section

The Objectives section must list the operational goals of the scenario.

Objectives should be practical and infrastructure-focused.

Examples:

- detect service degradation
- correlate dependency impact
- coordinate recovery workflow
- validate restored state
- document evidence-backed operational outcome

---

## Scenario Architecture Section

The Scenario Architecture section must include only one primary visual diagram.

Required diagram reference:

    ![Operational Poster](diagrams/operational-poster.png)

The scenario README must not reference the deprecated diagram set.

Prohibited references:

    diagrams/architecture-overview.png
    diagrams/relationship-overview.png
    diagrams/workflow-overview.png

---

## Used Modules Section

The Used Modules section must list operational capability modules used by the scenario.

Module names must follow this convention:

    <operational-capability>-module

Examples:

- telemetry-aggregation-module
- latency-analysis-module
- dependency-correlation-module
- recovery-orchestration-module
- validation-reporting-module

The section must explain how each module contributes to the scenario.

---

## Infrastructure Components Section

The Infrastructure Components section must describe the affected infrastructure areas.

Possible components include:

- network path
- VPN tunnel
- load balancer
- compute instance
- Kubernetes node
- database service
- storage system
- monitoring pipeline
- identity system
- security telemetry source

The section should describe operational relevance, not low-level implementation steps.

---

## Operational Workflow Section

The Operational Workflow section must summarize the scenario flow from detection to validation.

Required lifecycle flow:

    Detection
    Correlation and Analysis
    Incident Coordination
    Recovery and Automation
    Recovery Validation
    Governance and Reporting

The exact emphasis may differ by level, but the lifecycle order must remain clear.

---

## Detection Workflow Section

The Detection Workflow section must describe how the issue becomes visible.

It may include:

- telemetry signals
- health checks
- status indicators
- metric deviation
- log symptoms
- alert conditions

---

## Correlation and Analysis Section

The Correlation and Analysis section must describe how the scenario connects symptoms, dependencies, and possible causes.

It should explain:

- what signals are compared
- what dependencies are evaluated
- what impact path is analyzed
- what operational conclusion is reached

---

## Alert and Incident Workflow Section

The Alert and Incident Workflow section must describe how the situation becomes an operational incident.

It may include:

- alert qualification
- severity assignment
- escalation target
- incident owner
- coordination flow
- communication point

---

## Recovery and Automation Workflow Section

The Recovery and Automation Workflow section must describe the intended recovery or mitigation path.

For lower-level scenarios, this may be limited to manual validation or recommended operator action.

For higher-level scenarios, this may include recovery orchestration, failover, rebalancing, or continuity workflow.

---

## Recovery Validation Section

The Recovery Validation section must explain how the restored or stabilized state is confirmed.

Validation may include:

- metric normalization
- connectivity restoration
- service health confirmation
- dependency recovery
- user impact reduction
- repeated health checks

---

## Monitoring and Visibility Section

The Monitoring and Visibility section must describe the observability signals used by the scenario.

Examples:

- metrics
- logs
- traces
- status checks
- synthetic checks
- event streams
- dashboard indicators

---

## Operational Components Section

The Operational Components section must summarize the operational building blocks used in the scenario.

This section may include:

- telemetry source
- correlation logic
- alerting path
- recovery action
- validation method
- evidence output

---

## Evidence Section

The Evidence section must link to public-safe generated evidence artifacts.

Required links:

- evidence/generated/summary.md
- evidence/generated/execution-evidence.md
- evidence/generated/validation-evidence.md
- evidence/generated/artifact-manifest.json
- evidence/generated/artifact-checksums.json

Example:

    - [Evidence Summary](evidence/generated/summary.md)
    - [Execution Evidence](evidence/generated/execution-evidence.md)
    - [Validation Evidence](evidence/generated/validation-evidence.md)
    - [Artifact Manifest](evidence/generated/artifact-manifest.json)
    - [Artifact Checksums](evidence/generated/artifact-checksums.json)

---

## Expected Outcomes Section

The Expected Outcomes section must describe what successful handling of the scenario demonstrates.

Examples:

- issue visibility is established
- dependency impact is understood
- recovery path is documented
- validation criteria are clear
- evidence artifacts are available

---

## Validation Checklist Section

The Validation Checklist section must provide reviewer-readable pass criteria.

Example:

    - [ ] Scenario metadata is present
    - [ ] Operational poster is present
    - [ ] Used modules are listed
    - [ ] Used adapters are listed
    - [ ] Detection workflow is described
    - [ ] Validation workflow is described
    - [ ] Evidence links are present

---

## Related Scenarios Section

The Related Scenarios section must show how the scenario connects to other scenarios.

Required relationship groups:

- Upstream Scenarios
- Same-Level Scenarios
- Downstream Scenarios
- Cross-Domain Scenarios

If no relationship exists, use:

    None currently defined.

---

## Summary Section

The Summary section must close the scenario with a concise operational interpretation.

It should explain what capability the scenario demonstrates and why it matters in infrastructure operations.

---

## Final Principle

A scenario README is complete when it clearly explains the operational situation, shows the operational poster, references modules and adapters, documents the lifecycle workflow, and links to public-safe generated evidence.
