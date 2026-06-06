# Hybrid VPC Foundation

## Overview

Designs and provisions baseline VPC, subnet, routing, gateway, and hybrid connectivity foundation.

This build scenario documents infrastructure creation and baseline configuration work that supports downstream operational scenarios.

## Build Objectives

- Define the infrastructure foundation represented by this build.
- Identify required components, access paths, and configuration boundaries.
- Establish the baseline build workflow.
- Connect the build output to monitoring, recovery, and validation scenarios.
- Produce reviewer-readable implementation and validation evidence.

## Build Scope

This scenario focuses on infrastructure build, configuration, and readiness preparation.

## Used Modules

- Infrastructure Provisioning Module
- Network Foundation Module
- Security Baseline Module

## Build Workflow

1. Define target architecture.
2. Provision or configure required infrastructure components.
3. Apply baseline access, routing, security, or runtime configuration.
4. Validate the created infrastructure state.
5. Connect the build output to operational monitoring or recovery scenarios.
6. Document implementation evidence.

## Expected Outputs

- Build architecture summary
- Configuration boundary
- Validation checklist
- Operational handoff notes
- Related operational scenario references

## Related Operational Scenarios

- `/scenarios/**/vpn-connectivity-monitoring`
- `/scenarios/**/network-path-visibility`
- `/scenarios/**/multi-site-routing-failover`

## Summary

This build scenario supports the portfolio by showing how infrastructure foundations are created before they are monitored, analyzed, recovered, and governed through operational scenarios.
