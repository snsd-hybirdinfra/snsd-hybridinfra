# Logging Correlation Lab Scripts

This directory contains lab-local execution entrypoints for the Logging Correlation Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare log source, search, correlation, and evidence boundaries |
| validate.sh | Execute log source, OpenSearch, search, normalization, correlation, timeline, and evidence validation checks |
| cleanup.sh | Clean temporary logging validation outputs while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/07-logging-correlation-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- log source availability checks
- log forwarding readiness checks
- OpenSearch availability checks
- index readiness validation
- log search validation
- event normalization validation
- correlation analysis validation
- incident timeline reconstruction
- logging evidence generation
