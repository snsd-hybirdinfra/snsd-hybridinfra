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
    ├── scenarios/
    │   ├── level-1-visibility/
    │   ├── level-2-correlation/
    │   ├── level-3-recovery/
    │   ├── level-4-resilience/
    │   └── level-5-continuity/
    ├── modules/
    ├── adapters/
    ├── shared-runtime/
    ├── tools/
    ├── reports/
    ├── builds/
    └── docs/

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

    Total scenarios: 123
    Level 1 Visibility scenarios: 42
    Level 2 Correlation scenarios: 37
    Level 3 Recovery scenarios: 25
    Level 4 Resilience scenarios: 13
    Level 5 Continuity scenarios: 6

Scenario index:

- [Scenario Inventory](./scenarios/README.md)

---

## Flagship Operational Chain

The flagship scenario chain demonstrates lifecycle progression from visibility to enterprise continuity:

    vpn-connectivity-monitoring
    -> vpn-latency-correlation
    -> vpn-tunnel-recovery-automation
    -> multi-site-routing-failover
    -> enterprise-operational-continuity

| Level | Scenario | Purpose |
|---|---|---|
| L1 | [VPN Connectivity Monitoring](./scenarios/level-1-visibility/vpn-connectivity-monitoring/README.md) | VPN health visibility and signal collection |
| L2 | [VPN Latency Correlation](./scenarios/level-2-correlation/vpn-latency-correlation/README.md) | VPN latency and dependency correlation |
| L3 | [VPN Tunnel Recovery Automation](./scenarios/level-3-recovery/vpn-tunnel-recovery-automation/README.md) | Controlled tunnel recovery workflow |
| L4 | [Multi Site Routing Failover](./scenarios/level-4-resilience/multi-site-routing-failover/README.md) | Distributed routing resilience coordination |
| L5 | [Enterprise Operational Continuity](./scenarios/level-5-continuity/enterprise-operational-continuity/README.md) | Enterprise continuity governance and reporting |

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

Module index:

- [Operational Modules](./modules/README.md)

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

    scenario_directories: 123
    metadata_files: 123
    poster_svg_files: 123
    poster_png_files: 123
    missing_required_artifacts: 0
    small_png_files: 0
    bad_phrase_hits: 0
    readmes_with_empty_related_notice: 0

Quality report:

- [Repository Quality Check](./reports/repository-quality-check.md)
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

Relevant tools:

    tools/content-generator/
    tools/diagram-renderer/

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
