# Resilience Failover Lab Scripts

This directory contains lab-local execution entrypoints for the Resilience Failover Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare primary service, secondary service, traffic shift, and evidence boundaries |
| validate.sh | Execute availability, failure detection, failover, traffic shift, recovery, failback readiness, and evidence validation checks |
| cleanup.sh | Clean temporary resilience validation outputs while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/09-resilience-failover-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- primary service availability checks
- secondary service readiness checks
- failure detection validation
- failover decision validation
- traffic shift validation
- post-failover health validation
- failback readiness validation
- resilience evidence generation
