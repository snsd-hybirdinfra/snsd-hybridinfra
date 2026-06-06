# Operational Modules

This directory contains reusable operational capability modules used by scenario workflows across the SNSD Hybrid Infrastructure portfolio.

Modules represent platform-level operational capabilities, not one-off scenario logic. They are intended to be reused across visibility, correlation, recovery, resilience, and continuity scenarios.

---

## Module Design Principles

- Each module represents a reusable operational capability.
- Modules should avoid vendor-specific or implementation-only naming.
- Modules support scenario orchestration, evidence generation, validation, or reporting.
- Scenario READMEs reference modules as capability dependencies.
- Module boundaries should remain lifecycle-aware and operationally meaningful.

---

## Module Inventory

Total modules: 11

| Module | Purpose |
|---|---|
| [Automation Execution Module](./automation-execution-module/README.md) | Supports controlled execution of scripts, runbooks, configuration tasks, and automation workflows. |
| [Compute Foundation Module](./compute-foundation-module/README.md) | Supports virtual machines, cloud instances, nodes, runtime hosts, and compute baseline configuration. |
| [Continuity Governance Module](./continuity-governance-module/README.md) | Supports enterprise continuity decisions, governance reporting, ownership tracking, and executive evidence. |
| [Dependency Correlation Module](./dependency-correlation-module/README.md) | Correlates related signals, dependencies, symptoms, and operational impact paths. |
| [Infrastructure Provisioning Module](./infrastructure-provisioning-module/README.md) | Supports baseline infrastructure creation, provisioning workflow design, and deployment readiness. |
| [Network Foundation Module](./network-foundation-module/README.md) | Supports VPC, subnet, routing, gateway, VPN, WAN, and network path foundation design. |
| [Observability Foundation Module](./observability-foundation-module/README.md) | Supports metrics, logs, exporters, dashboards, health checks, and visibility foundation setup. |
| [Recovery Orchestration Module](./recovery-orchestration-module/README.md) | Coordinates recovery, failover, restoration, restart, rebalancing, and mitigation workflows. |
| [Security Baseline Module](./security-baseline-module/README.md) | Supports security groups, network access rules, identity boundaries, policy controls, and secure baseline configuration. |
| [Telemetry Aggregation Module](./telemetry-aggregation-module/README.md) | Collects, normalizes, and prepares operational telemetry for visibility and analysis scenarios. |
| [Validation Reporting Module](./validation-reporting-module/README.md) | Produces recovery validation summaries, artifact manifests, evidence outputs, and reviewer-readable reports. |

---

## Capability Role

Operational modules provide reusable building blocks for:

- telemetry collection
- health signal normalization
- dependency correlation
- incident context preparation
- recovery orchestration
- automation execution
- recovery validation
- dashboard and evidence reporting

---

## Summary

The module layer supports the repository's platform-oriented structure by separating reusable operational capabilities from scenario-specific workflows.
