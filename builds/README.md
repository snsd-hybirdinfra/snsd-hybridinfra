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
| [Alb Based Web Service Routing](./alb-based-web-service-routing/README.md) | Builds application load balancing, listener routing, target health checks, and web service traffic distribution. |
| [Ansible Server Bootstrap](./ansible-server-bootstrap/README.md) | Automates baseline server initialization including users, packages, services, configuration, and validation checks. |
| [Backup Automation Foundation](./backup-automation-foundation/README.md) | Establishes backup job automation, repository target, retention boundary, and restore-readiness validation. |
| [Hybrid Vpc Foundation](./hybrid-vpc-foundation/README.md) | Designs and provisions baseline VPC, subnet, routing, gateway, and hybrid connectivity foundation. |
| [Log Pipeline Foundation](./log-pipeline-foundation/README.md) | Builds log collection, forwarding, indexing, retention, and review pipeline foundation for operational analysis. |
| [Nat Gateway Egress Architecture](./nat-gateway-egress-architecture/README.md) | Configures private subnet outbound access using NAT gateway routing and controlled internet egress. |
| [Observability Stack Deployment](./observability-stack-deployment/README.md) | Deploys monitoring exporters, metrics collection, dashboard visibility, and operational health signal foundation. |
| [Private Web Tier With Bastion](./private-web-tier-with-bastion/README.md) | Builds a private web tier that is administratively reachable only through a bastion-controlled access path. |
| [Recovery Validation Lab](./recovery-validation-lab/README.md) | Builds a controlled recovery validation environment for testing restoration, failover, evidence, and operational readiness. |
| [Security Boundary Baseline](./security-boundary-baseline/README.md) | Defines baseline security groups, access control boundaries, administrative access paths, and policy controls. |

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
