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
| [Automation Execution Module](./automation-execution-module/README.md) | Executes controlled automation actions after operational conditions, approvals, or validation gates are satisfied. |
| [Compute Foundation Module](./compute-foundation-module/README.md) | Defines compute resource context used by visibility, correlation, recovery, and resilience scenarios. |
| [Continuity Governance Module](./continuity-governance-module/README.md) | Supports enterprise continuity decisions, ownership tracking, governance reporting, and executive-level recovery assurance. |
| [Dependency Correlation Module](./dependency-correlation-module/README.md) | Correlates signals across services, infrastructure components, and platform dependencies to distinguish root conditions from symptoms. |
| [Infrastructure Provisioning Module](./infrastructure-provisioning-module/README.md) | Defines infrastructure build and provisioning context used to support operational scenarios and validation environments. |
| [Network Foundation Module](./network-foundation-module/README.md) | Provides network topology, routing, connectivity, and path context for operational scenarios. |
| [Observability Foundation Module](./observability-foundation-module/README.md) | Provides the monitoring and visibility foundation used by scenarios to collect, structure, and expose operational signals. |
| [Recovery Orchestration Module](./recovery-orchestration-module/README.md) | Coordinates recovery workflows after incident qualification and before final recovery validation. |
| [Security Baseline Module](./security-baseline-module/README.md) | Defines security posture, policy visibility, and baseline control context for operational scenarios. |
| [Telemetry Aggregation Module](./telemetry-aggregation-module/README.md) | Collects, normalizes, and prepares operational telemetry for visibility, correlation, and validation workflows. |
| [Validation Reporting Module](./validation-reporting-module/README.md) | Produces validation summaries, artifact manifests, evidence outputs, and reviewer-readable operational reports. |

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
