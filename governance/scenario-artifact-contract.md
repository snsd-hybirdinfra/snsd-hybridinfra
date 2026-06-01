# Scenario Artifact Contract

## Purpose

This document defines the required artifact contract for each scenario in this repository.

A scenario is considered portfolio-ready only when its required documentation, diagram, evidence, and metadata artifacts are present and aligned with the repository visibility policy.

---

## Scenario Scope

Each scenario represents one infrastructure operations situation.

A scenario must document:

- operational context
- affected infrastructure components
- detection workflow
- correlation and analysis workflow
- incident coordination workflow
- recovery, resilience, or continuity workflow
- validation checklist
- used operational modules
- used integration adapters
- generated evidence summary
- operational poster diagram

---

## Required Scenario Directory Structure

Each scenario must follow this structure:

    scenarios/<level>/<scenario-name>/
    ├─ metadata.yaml
    ├─ README.md
    ├─ architecture/
    ├─ artifacts/
    ├─ diagrams/
    │  ├─ operational-poster.svg
    │  └─ operational-poster.png
    ├─ evidence/
    │  └─ generated/
    │     ├─ summary.md
    │     ├─ execution-evidence.md
    │     ├─ validation-evidence.md
    │     ├─ artifact-manifest.json
    │     └─ artifact-checksums.json
    └─ implementation/

---

## Required Public Artifacts

| Artifact | Required | Purpose |
|---|---:|---|
| metadata.yaml | Yes | Scenario metadata and lifecycle classification |
| README.md | Yes | Main scenario documentation |
| diagrams/operational-poster.svg | Yes | Source operational poster diagram |
| diagrams/operational-poster.png | Yes | Public visual diagram for README and reviews |
| evidence/generated/summary.md | Yes | Human-readable evidence summary |
| evidence/generated/execution-evidence.md | Yes | Generated execution evidence |
| evidence/generated/validation-evidence.md | Yes | Validation evidence summary |
| evidence/generated/artifact-manifest.json | Yes | Scenario artifact inventory |
| evidence/generated/artifact-checksums.json | Yes | File checksum record |

---

## README Diagram Rule

Each scenario README must reference only the operational poster as the primary visual artifact.

Required reference:

    ![Operational Poster](diagrams/operational-poster.png)

The following legacy diagram references must not be used:

    ![Architecture Overview](diagrams/architecture-overview.png)
    ![Relationship Overview](diagrams/relationship-overview.png)
    ![Workflow Overview](diagrams/workflow-overview.png)

---

## Deprecated Diagram Artifacts

The following legacy diagram artifacts are deprecated and must not be regenerated:

    architecture-overview.*
    relationship-overview.*
    workflow-overview.*

These artifacts should be removed from scenario folders once the operational poster workflow is fully adopted.

---

## Metadata Contract

Each metadata.yaml must include enough information to identify and classify the scenario.

Minimum required metadata fields:

    scenario_name: <scenario-name>
    lifecycle_level: <level-name>
    domain: <operations-domain>
    summary: <short-summary>
    used_modules:
      - <module-name>
    used_adapters:
      - <adapter-name>
    related_scenarios:
      upstream: []
      same_level: []
      downstream: []
      cross_domain: []

---

## Module Reference Rule

All module references must use the module naming convention:

    <operational-capability>-module

Examples:

    telemetry-aggregation-module
    latency-analysis-module
    dependency-correlation-module
    recovery-orchestration-module
    validation-reporting-module

---

## Adapter Reference Rule

All adapter references must use the adapter naming convention:

    <integration-target>-adapter

Examples:

    prometheus-adapter
    grafana-adapter
    ansible-adapter
    kubernetes-adapter
    opensearch-adapter
    python-exporter-adapter

---

## Evidence Contract

Generated evidence must be clean and public-safe.

Generated evidence may include:

- generated artifact list
- validation summary
- artifact status
- checksum records
- diagram existence proof
- README reference validation
- metadata validation summary

Generated evidence must not include:

- raw runtime logs
- local machine paths
- environment variables
- secrets
- credentials
- failed debug traces
- sensitive screenshots
- internal-only notes

---

## Internal Evidence Rule

Raw logs, command outputs, failed runs, debug traces, and local test results must remain internal-only unless cleaned and summarized.

Internal evidence may be stored locally but should not be committed to the public repository.

---

## Scenario Completion Criteria

A scenario is considered complete when all of the following checks pass:

    metadata.yaml exists
    README.md exists
    diagrams/operational-poster.svg exists
    diagrams/operational-poster.png exists
    README references diagrams/operational-poster.png
    README does not reference deprecated diagrams
    evidence/generated/summary.md exists
    evidence/generated/execution-evidence.md exists
    evidence/generated/validation-evidence.md exists
    evidence/generated/artifact-manifest.json exists
    evidence/generated/artifact-checksums.json exists
    scenario name matches folder name
    lifecycle level matches parent level directory
    module references follow module naming convention
    adapter references follow adapter naming convention

---

## Final Principle

A scenario is portfolio-ready only when it is readable, visually supported, evidence-backed, and aligned with the repository's scenario-driven infrastructure operations portfolio positioning.
