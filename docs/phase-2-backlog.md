# Phase 2 Backlog

## Purpose

This document defines the Phase 2 extension backlog for SNSD Hybrid Infrastructure.

Phase 1 established the repository baseline:

- 150 lifecycle-aligned scenarios
- 10 implementation lab boundaries
- generated reviewer-facing documentation
- repository validation reports
- runtime evidence policy
- local-only lab evidence model

Phase 2 should extend selected lab implementations without breaking the repository governance model.

## Phase 2 Direction

Phase 2 focuses on deeper runtime implementation, stronger validation fidelity, and improved reviewer-facing evidence.

It should not expand the repository by adding random scenarios or unnecessary tools.

## Priority Model

| Priority | Meaning |
|---|---|
| P1 | High-value extension aligned with current lab boundary |
| P2 | Useful enhancement after P1 stabilization |
| P3 | Optional improvement, defer unless needed |

## Lab Extension Backlog

| Lab | Phase 2 Candidate | Priority |
|---|---|---|
| 01-linux-observability-lab | Add richer node exporter validation and host health dashboard examples | P2 |
| 02-network-routing-lab | Add traceroute/path comparison and route failure simulation | P1 |
| 03-ansible-automation-lab | Add rollback playbook and idempotency validation report | P1 |
| 04-container-runtime-lab | Add container failure injection and recovery timing measurement | P1 |
| 05-kolla-openstack-lab | Strengthen Kolla-Ansible preflight and optional dry-run validation | P1 |
| 06-monitoring-stack-lab | Add Prometheus alert rules and alert validation examples | P1 |
| 07-logging-correlation-lab | Extend from file-based correlation to OpenSearch-backed query examples | P1 |
| 08-backup-recovery-lab | Add scheduled backup simulation and restore point comparison | P2 |
| 09-resilience-failover-lab | Add HAProxy or NGINX-based traffic failover runtime simulation | P1 |
| 10-governance-reporting-lab | Add dashboard-style governance summary generation | P2 |

## Documentation Backlog

| Document | Candidate Improvement | Priority |
|---|---|---|
| README.md | Keep generated from repository state | P1 |
| labs/README.md | Keep generated from lab state | P1 |
| scenarios/README.md | Keep generated from scenario state | P1 |
| docs/lab-coverage-matrix.md | Improve scenario-to-lab mapping rules if taxonomy changes | P2 |
| validation-reports/lab-runtime-implementation-summary.md | Improve status extraction from local runtime summaries | P2 |
| validation-reports/lab-readiness-summary.md | Extend readiness checks if new lab boundary assets are added | P2 |

## CI / GitHub Actions Backlog

GitHub Actions is not required for Phase 1.

If added in Phase 2, CI should remain lightweight.

Allowed CI scope:

- Python syntax validation
- generated documentation drift check
- markdown link validation
- repository structure validation
- forbidden language validation

Disallowed CI scope:

- VMware target access
- SSH target validation
- Docker Compose runtime lab execution
- Kolla deployment
- local runtime evidence generation
- private key usage

## Evidence Policy Backlog

The Phase 1 evidence policy remains authoritative.

| Evidence Area | Policy |
|---|---|
| scenarios/*/evidence/generated/ | committed reviewer-readable placeholder evidence |
| labs/*/evidence/generated/ | local-only runtime evidence |
| labs/*/runtime-workspace/ | local-only runtime workspace |
| a.txt | local-only repository summary |
| *.pem / *.key / id_* | ignored sensitive local material |

Phase 2 must not weaken this policy.

## Out of Scope for Phase 2

The following are intentionally out of scope unless the repository direction changes:

- adding another 100+ scenarios without taxonomy need
- replacing local lab validation with GitHub-hosted mock execution
- claiming full production OpenStack deployment without actual deployment evidence
- committing raw runtime output
- committing private keys or machine-specific execution artifacts
- turning every scenario into a separate standalone lab

## Recommended Phase 2 Start

Recommended first Phase 2 work item:

| Order | Work Item |
|---:|---|
| 1 | Improve 09-resilience-failover-lab with HAProxy or NGINX traffic failover simulation |
| 2 | Add Prometheus alert rules to 06-monitoring-stack-lab |
| 3 | Add rollback/idempotency checks to 03-ansible-automation-lab |
| 4 | Extend 07-logging-correlation-lab toward OpenSearch-backed examples |
| 5 | Strengthen 05-kolla-openstack-lab preflight checks |

## Governance Rule

Phase 2 changes must preserve:

- lifecycle alignment
- lab boundary clarity
- generated documentation model
- local-only evidence policy
- repository validation PASS target
- reviewer readability