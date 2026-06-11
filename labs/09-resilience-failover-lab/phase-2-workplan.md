# Phase 2 Workplan - Resilience Failover Runtime

## Target Lab

09-resilience-failover-lab

## Objective

Extend the Phase 1 state-file failover simulation into a more realistic local traffic failover runtime boundary.

## Planned Scope

Phase 2 will add:

- active/standby service endpoint model
- local traffic routing validation
- primary failure simulation
- secondary endpoint promotion validation
- recovery-after-failover validation
- generated failover runtime summary

## Candidate Runtime Model

The preferred runtime model is:

- NGINX or HAProxy as traffic entrypoint
- primary backend service
- secondary backend service
- scripted failure injection
- scripted validation of active backend response

## Out of Scope

This phase does not require:

- cloud load balancer integration
- Kubernetes deployment
- production HA architecture
- external DNS failover
- GitHub Actions runtime execution

## Evidence Policy

Generated runtime evidence remains local-only.

Committed files should include:

- scripts
- configs
- compose files if used
- validation notes
- reviewer-readable summary documents

Generated runtime output must remain excluded from Git.