# Resilience Failover Lab Shared Runtime

This shared runtime provides lab-local execution helpers for resilience and failover validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute failure simulation, failover validation, post-failover checks, failback readiness, evidence, and cleanup workflows |
| validators/ | Check service availability, primary and secondary readiness, traffic shift state, recovery state, failback readiness, and evidence outputs |
| parsers/ | Convert health checks, routing output, load balancer state, monitoring signals, and failover results into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/09-resilience-failover-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
