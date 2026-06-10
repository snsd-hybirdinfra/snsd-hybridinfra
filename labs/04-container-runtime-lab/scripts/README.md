# Container Runtime Lab Scripts

This directory contains lab-local execution entrypoints for the Container Runtime Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare Docker runtime validation targets and evidence directories |
| validate.sh | Execute Docker runtime, container health, log, recovery, and evidence validation checks |
| cleanup.sh | Clean temporary container validation outputs while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/04-container-runtime-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- Docker runtime availability checks
- validation container preparation
- container image validation
- container health validation
- container log collection
- restart and recovery workflow validation
- container evidence generation
