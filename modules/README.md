# Operational Capability Modules

This directory contains reusable operational and infrastructure capability modules.

Modules are not individual scenarios.  
They represent reusable capabilities that can support build scenarios, visibility scenarios, correlation workflows, recovery workflows, validation workflows, and continuity governance.

## Module Categories

| Module | Purpose |
|---|---|
| Infrastructure Provisioning Module | Supports baseline infrastructure creation and provisioning workflows |
| Network Foundation Module | Supports VPC, subnet, routing, gateway, VPN, and network path design |
| Compute Foundation Module | Supports VM, instance, node, and runtime foundation workflows |
| Security Baseline Module | Supports security group, access control, policy, and boundary configuration |
| Observability Foundation Module | Supports metrics, logs, dashboards, exporters, and visibility setup |
| Automation Execution Module | Supports scripted or orchestrated execution workflows |
| Telemetry Aggregation Module | Collects and normalizes operational telemetry |
| Dependency Correlation Module | Connects related symptoms, dependencies, and impact paths |
| Recovery Orchestration Module | Coordinates recovery, failover, restart, and restoration actions |
| Validation Reporting Module | Produces validation evidence and reviewer-readable summaries |
| Continuity Governance Module | Supports continuity decision, governance reporting, and executive evidence |

## Usage

Modules are referenced by both build scenarios and operational scenarios.

Build scenarios demonstrate how infrastructure foundations are created.  
Operational scenarios demonstrate how those foundations are monitored, analyzed, recovered, validated, and governed.
