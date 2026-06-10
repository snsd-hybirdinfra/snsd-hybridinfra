# Linux Observability Lab Scripts

This directory contains lab-local execution entrypoints.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare Linux observability lab prerequisites |
| validate.sh | Execute lab validation checks |
| cleanup.sh | Clean temporary lab execution outputs |

## Execution Boundary

These scripts belong only to:

labs/01-linux-observability-lab/

They are intended to coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- Ansible inventory validation
- node exporter deployment checks
- Prometheus scrape validation
- filesystem checks
- process and service checks
- system event collection
- evidence generation
