# Resilience Failover Lab Scripts

This directory contains lab-local execution scripts for the Resilience Failover Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepares runtime workspace, configuration, fixtures, and evidence boundaries |
| failover.sh | Executes failover transition logic |
| recover.sh | Executes recovery workflow logic |
| validate.sh | Validates runtime results and writes validation evidence |
| cleanup.sh | Cleans runtime workspace outputs |
| run.sh | Orchestrates the full lab runtime workflow |

## Execution

Recommended entrypoint from the lab root:

bash scripts/run.sh

Optional cleanup execution:

bash scripts/run.sh --cleanup

## Runtime Boundary

This lab validates a local resilience and failover runtime boundary.

The runtime boundary is intentionally scoped to lab-local execution and reviewer-readable validation evidence.

## Evidence Boundary

Generated evidence is written under evidence/generated/.

Generated runtime evidence remains local-only unless explicitly promoted to reviewer-facing evidence.

## Scenario Study Usage

This lab can be used to study failover visibility, resilience validation, service continuity, traffic shift validation, and recovery confirmation scenarios.
