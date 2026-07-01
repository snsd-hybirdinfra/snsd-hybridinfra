# Resilience Failover Execution Boundary Note

## Execution Mode

The Resilience Failover Lab validates a state-file-based failover simulation.

This lab demonstrates failure detection, failover decision generation, traffic shift validation, recovery recording, and resilience validation.

## Resilience Boundary

This lab validates:

- Active endpoint tracking
- Primary failure detection
- Secondary endpoint health validation
- Failover decision generation
- Traffic shift simulation
- Recovery event recording
- Validation marker preservation
- Local runtime summary generation

This lab does not validate:

- Production load balancer control planes
- BGP or DNS failover
- Multi-region data replication
- Stateful service consistency
- Real traffic steering
- Production disaster recovery orchestration

## Evidence Policy

Generated runtime evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside repository commit history.

## Runtime Summary

Local runtime execution produces:

- evidence/generated/summary/resilience-failover-execution-summary.md

This summary is consumed by the local repository executive summary generator when present.