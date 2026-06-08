# SNSD Hybrid Infrastructure

## Enterprise Operational Capability Platform

SNSD Hybrid Infrastructure is a scenario-driven infrastructure operations portfolio designed to demonstrate reusable enterprise operational capabilities across hybrid infrastructure environments.

This repository is not a simple scenario collection.

It is structured as an operational capability platform where reusable modules, adapters, evidence artifacts, dashboards, and scenario workflows are organized around production-oriented infrastructure operations.

---

## Platform Positioning

This repository represents the following engineering capability areas:

- Cloud Infrastructure Engineering
- Hybrid Infrastructure Operations
- Platform Engineering
- Observability Engineering
- Recovery Automation
- Resilience Engineering
- Operational Governance
- AIOps-oriented Operations

The repository demonstrates how infrastructure operations can be modeled, validated, and documented through reusable operational capabilities and scenario-based validation workflows.

Each scenario includes an operational interpretation section that explains the risk context, operator decision points, and reviewer-facing operational value of the workflow.

---

## Operational Lifecycle

The repository follows a consistent operational lifecycle:

    Detection
    -> Correlation & Analysis
    -> Incident Coordination
    -> Recovery & Automation
    -> Recovery Validation
    -> Governance & Reporting

Each scenario is mapped to a lifecycle maturity level and validates one or more operational capabilities.

---

## Repository Structure

    snsd-hybridinfra/
    |-- scenarios/
    |   |-- level-1-visibility/
    |   |-- level-2-correlation/
    |   |-- level-3-recovery/
    |   |-- level-4-resilience/
    |   `-- level-5-continuity/
    |-- modules/
    |-- adapters/
    |-- shared-runtime/
    |-- tools/
    |-- reports/
    |-- builds/
    `-- docs/

---

## Scenario Maturity Model

| Level | Lifecycle Area | Operational Meaning |
|---|---|---|
| Level 1 | Visibility | Detect and expose infrastructure health, telemetry, and operational signals. |
| Level 2 | Correlation | Analyze dependencies, symptoms, and operational impact across infrastructure components. |
| Level 3 | Recovery | Execute controlled recovery workflows and validate restored state. |
| Level 4 | Resilience | Coordinate distributed resilience across regions, sites, clusters, or failure domains. |
| Level 5 | Continuity | Govern enterprise continuity, operational readiness, and cross-domain recovery posture. |

---

## Scenario Inventory

The repository currently contains:

    Total scenarios: 150
    Level 1 Visibility scenarios: 45
    Level 2 Correlation scenarios: 41
    Level 3 Recovery scenarios: 33
    Level 4 Resilience scenarios: 21
    Level 5 Continuity scenarios: 10

Scenario index:

- [Scenario Inventory](./scenarios/README.md)

Detailed scenario relationships are maintained inside each scenario README through strict `related_scenarios` metadata.

---

## Lifecycle Coverage

The scenario set is organized to demonstrate operational maturity across the full infrastructure operations lifecycle.

| Lifecycle Level | Focus | Example Capability Areas |
|---|---|---|
| Level 1 Visibility | Signal collection and health visibility | VPN, network path, compute, database, storage, Kubernetes, security telemetry |
| Level 2 Correlation | Dependency and impact analysis | latency correlation, packet loss analysis, database dependency analysis, security anomaly correlation |
| Level 3 Recovery | Controlled recovery execution | service recovery, failover automation, restoration workflows, recovery validation |
| Level 4 Resilience | Distributed failure-domain coordination | multi-region failover, cluster resilience, routing resilience, distributed platform survivability |
| Level 5 Continuity | Enterprise continuity governance | cloud continuity, platform continuity, network continuity, security continuity, service continuity |

The repository is intended to show operational breadth across infrastructure domains rather than a single linear incident chain.

---

## Operational Capabilities

The repository uses reusable capability modules and operational adapters to support scenario workflows.

Representative capability areas include:

- Telemetry aggregation
- Health signal collection
- Dependency correlation
- Incident coordination
- Recovery orchestration
- Automation execution
- Recovery validation
- Visibility reporting
- Governance reporting

Platform indexes:

- [Operational Modules](./modules/README.md)
- [Operational Adapters](./adapters/README.md)
- [Shared Runtime](./shared-runtime/README.md)
- [Build Foundations](./builds/README.md)
- [Reports](./reports/README.md)
- [Tools](./tools/README.md)
- [Documentation](./docs/README.md)

---

## Generated Artifacts

Each scenario is designed to include:

    metadata.yaml
    README.md
    diagrams/operational-poster.svg
    diagrams/operational-poster.png
    evidence/generated/summary.md
    evidence/generated/execution-evidence.md
    evidence/generated/validation-evidence.md
    evidence/generated/artifact-manifest.json
    evidence/generated/artifact-checksums.json

These artifacts provide reviewer-readable operational documentation, visual architecture summaries, and validation evidence.

---

## Quality Status

Repository quality validation has been executed across all scenarios.

Current validation status:

    scenario_directories: 150
    metadata_files: 150
    poster_svg_files: 150
    poster_png_files: 150
    missing_required_artifacts: 0
    small_png_files: 0
    bad_phrase_hits: 0
    readmes_with_empty_related_notice: 0

Quality reports:

- [Portfolio Health Summary](./reports/portfolio-health-summary.md)
- [Repository Quality Check](./reports/repository-quality-check.md)
- [Markdown Link Check](./reports/markdown-link-check.md)
- [Top-Level Structure Check](./reports/top-level-structure-check.md)
- [Root README Alignment Check](./reports/root-readme-alignment-check.md)
- [Repository Language Check](./reports/repository-language-check.md)
- [Related Scenarios Generation Report](./reports/related-scenarios-generation-report.md)

---

## Tooling

Repository automation is handled through internal tooling under `tools/`.

Current tooling includes:

- metadata generation
- README generation
- operational poster rendering
- related scenario generation
- repository quality checking
- markdown link validation
- top-level structure validation
- portfolio health summary generation
- temporary file cleanup
- repository validation workflow execution

Relevant tools:

    tools/content-generator/
    tools/diagram-renderer/

Primary validation command:

    python tools/content-generator/run_repository_validation.py

---

## Portfolio Value

This repository demonstrates the ability to:

- structure infrastructure operations as reusable platform capabilities
- design lifecycle-based operational scenarios
- generate consistent documentation and visual artifacts
- validate infrastructure operations through evidence-driven workflows
- model recovery, resilience, and continuity in a production-oriented way
- maintain repository-wide governance, consistency, and quality checks

---

## Summary

SNSD Hybrid Infrastructure is an enterprise infrastructure operations portfolio focused on operational capability design, scenario-based validation, and production-oriented documentation.

It presents infrastructure operations as a reusable, governed, and evidence-backed platform rather than isolated troubleshooting examples.
