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
| [Automation Execution Module](./automation-execution-module/README.md) | ﻿# Automation Execution Module |
| [Compute Foundation Module](./compute-foundation-module/README.md) | ﻿# Compute Foundation Module |
| [Continuity Governance Module](./continuity-governance-module/README.md) | ﻿# Continuity Governance Module |
| [Dependency Correlation Module](./dependency-correlation-module/README.md) | ﻿# Dependency Correlation Module |
| [Infrastructure Provisioning Module](./infrastructure-provisioning-module/README.md) | ﻿# Infrastructure Provisioning Module |
| [Network Foundation Module](./network-foundation-module/README.md) | ﻿# Network Foundation Module |
| [Observability Foundation Module](./observability-foundation-module/README.md) | ﻿# Observability Foundation Module |
| [Recovery Orchestration Module](./recovery-orchestration-module/README.md) | ﻿# Recovery Orchestration Module |
| [Security Baseline Module](./security-baseline-module/README.md) | ﻿# Security Baseline Module |
| [Telemetry Aggregation Module](./telemetry-aggregation-module/README.md) | ﻿# Telemetry Aggregation Module |
| [Validation Reporting Module](./validation-reporting-module/README.md) | ﻿# Validation Reporting Module |

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
