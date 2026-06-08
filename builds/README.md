# Build Foundations

This directory contains build-level foundations that support the SNSD Hybrid Infrastructure operational capability platform.

Build foundations represent reusable setup, automation, or enablement layers that support scenarios, modules, adapters, and shared runtime workflows.

---

## Build Design Principles

- Build foundations should support repeatable infrastructure operations.
- Build content should avoid scenario-only assumptions.
- Build outputs should support operational validation, automation, or evidence generation.
- Build foundations may support multiple lifecycle levels and infrastructure domains.

---

## Build Inventory

Total build foundations: 10

| Build Foundation | Purpose |
|---|---|
| [Alb Based Web Service Routing](./alb-based-web-service-routing/README.md) | Defines application load balancing and service entry routing for web-facing workloads. |
| [Ansible Server Bootstrap](./ansible-server-bootstrap/README.md) | Defines automation control node preparation for infrastructure operations workflows. |
| [Backup Automation Foundation](./backup-automation-foundation/README.md) | Defines backup automation patterns used to support recovery and continuity scenarios. |
| [Hybrid Vpc Foundation](./hybrid-vpc-foundation/README.md) | Defines baseline network segmentation and cloud connectivity structure for scenario support environments. |
| [Log Pipeline Foundation](./log-pipeline-foundation/README.md) | Defines log collection and search pipeline foundations for operational investigation and evidence generation. |
| [Nat Gateway Egress Architecture](./nat-gateway-egress-architecture/README.md) | Defines controlled outbound access for private infrastructure components. |
| [Observability Stack Deployment](./observability-stack-deployment/README.md) | Defines baseline observability stack deployment for telemetry, dashboarding, and operational visibility. |
| [Private Web Tier With Bastion](./private-web-tier-with-bastion/README.md) | Defines a private application tier access model where administrative access is mediated through a bastion host. |
| [Recovery Validation Lab](./recovery-validation-lab/README.md) | Defines a controlled lab structure for validating recovery workflows and post-recovery evidence. |
| [Security Boundary Baseline](./security-boundary-baseline/README.md) | Defines baseline security segmentation and access control context for operational scenarios. |

---

## Platform Role

Build foundations support the repository by providing reusable implementation groundwork for:

- automation preparation
- infrastructure setup
- validation workflows
- recovery readiness
- operational evidence generation

---

## Summary

The builds layer provides reusable foundation assets that support the operational capability platform without replacing scenario-level workflows.
