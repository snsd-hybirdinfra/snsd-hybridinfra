# Linux Observability Lab Scripts

This directory contains lab-local execution scripts for the Linux Observability Lab.

## Script Roles

| Script | Purpose |
|---|---|
| preflight.sh | Checks local runtime prerequisites before setup and validation |
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

This lab validates a local Linux host observability runtime boundary.

The runtime boundary is intentionally scoped to lab-local execution and reviewer-readable validation evidence.

## Evidence Boundary

Generated evidence is written under evidence/generated/.

Generated runtime evidence remains local-only unless explicitly promoted to reviewer-facing evidence.

## Scenario Study Usage

This lab can be used to study Linux host visibility, process health, filesystem health, service state, and system event visibility scenarios.
