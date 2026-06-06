# Operational Capability Modules

This directory contains reusable infrastructure and operational capability modules.

Modules are not individual scenarios. They define reusable capability boundaries used by build scenarios and lifecycle-based operational scenarios.

---

## Module Catalog

| Module | Purpose |
|---|---|
| [Automation Execution Module](automation-execution-module/) | Controlled script, runbook, configuration, and automation execution capability |
| [Compute Foundation Module](compute-foundation-module/) | Virtual machine, cloud instance, node, and runtime host foundation capability |
| [Continuity Governance Module](continuity-governance-module/) | Continuity decision, governance reporting, ownership, and executive evidence capability |
| [Dependency Correlation Module](dependency-correlation-module/) | Signal, dependency, symptom, and impact path correlation capability |
| [Infrastructure Provisioning Module](infrastructure-provisioning-module/) | Baseline infrastructure creation and provisioning workflow capability |
| [Network Foundation Module](network-foundation-module/) | VPC, subnet, routing, gateway, VPN, WAN, and network path foundation capability |
| [Observability Foundation Module](observability-foundation-module/) | Metrics, logs, exporters, dashboards, and visibility foundation capability |
| [Recovery Orchestration Module](recovery-orchestration-module/) | Recovery, failover, restart, restoration, and mitigation orchestration capability |
| [Security Baseline Module](security-baseline-module/) | Security group, access boundary, policy, and control baseline capability |
| [Telemetry Aggregation Module](telemetry-aggregation-module/) | Operational telemetry collection, normalization, and preparation capability |
| [Validation Reporting Module](validation-reporting-module/) | Validation summary, evidence, manifest, and reporting capability |

---

## Usage Model

Build scenarios use modules to describe infrastructure construction and baseline configuration capabilities.

Operational scenarios use modules to describe monitoring, correlation, recovery, validation, and continuity capabilities.

---

## Summary

This module catalog provides reusable capability references for the infrastructure operations portfolio.
