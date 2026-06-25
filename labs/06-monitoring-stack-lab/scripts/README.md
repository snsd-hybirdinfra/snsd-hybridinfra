# Monitoring Stack Lab Scripts

This directory contains lab-local execution scripts for the Monitoring Stack Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepares runtime workspace, configuration, fixtures, and evidence boundaries |
| validate.sh | Validates runtime results and writes validation evidence |
| cleanup.sh | Cleans runtime workspace outputs |
| run.sh | Orchestrates the full lab runtime workflow |

## Execution

Recommended entrypoint from the lab root:

bash scripts/run.sh

Optional cleanup execution:

bash scripts/run.sh --cleanup

## Runtime Boundary

This lab validates a local Prometheus and Grafana monitoring runtime boundary.

The runtime boundary is intentionally scoped to lab-local execution and reviewer-readable validation evidence.

## Evidence Boundary

Generated evidence is written under evidence/generated/.

Generated runtime evidence remains local-only unless explicitly promoted to reviewer-facing evidence.

## Scenario Study Usage

This lab can be used to study monitoring readiness, service health, application health, API gateway health, certificate visibility, alert readiness, and dashboard visibility scenarios.
