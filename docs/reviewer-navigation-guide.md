# Reviewer Navigation Guide

Use this guide to review the repository in a clear, consistent order.

## Recommended review order

| Step | Review target | Why it matters |
|---|---|---|
| 1 | [README.md](../README.md) | Understand the repository purpose and scope |
| 2 | [docs/repository-orientation.md](repository-orientation.md) | Get a concise map of the structure |
| 3 | [labs/README.md](../labs/README.md) | Review the implementation lab catalog |
| 4 | [scenarios/README.md](../scenarios/README.md) | Review the scenario catalog by lifecycle level |
| 5 | [validation-reports/README.md](../validation-reports/README.md) | Inspect reviewer-facing summaries |

## What to review next

- [docs/lab-coverage-matrix.md](lab-coverage-matrix.md) for scenario-to-lab coverage
- [docs/scenario-to-lab-traceability.md](scenario-to-lab-traceability.md) for traceability details
- [docs/runtime-evidence-policy.md](runtime-evidence-policy.md) for evidence boundaries

## Lab review order

1. 01-linux-observability-lab
2. 02-network-routing-lab
3. 03-ansible-automation-lab
4. 04-container-runtime-lab
5. 05-kolla-openstack-lab
6. 06-monitoring-stack-lab
7. 07-logging-correlation-lab
8. 08-backup-recovery-lab
9. 09-resilience-failover-lab
10. 10-governance-reporting-lab

## Scenario review path

Scenarios are organized by lifecycle maturity:

- Level 1 — visibility and detection
- Level 2 — correlation and analysis
- Level 3 — recovery and automation
- Level 4 — resilience and failover
- Level 5 — continuity and governance

## Evidence policy

Runtime evidence is generated locally and intentionally excluded from Git. The repository keeps committed content reviewer-friendly while preserving execution boundaries.
