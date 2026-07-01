# Python Resilience Parser Adapter

## Adapter Purpose

Parses failover output, health checks, traffic shift state, and evidence summaries.

## Lab Boundary

This is a lab-local adapter for:

labs/09-resilience-failover-lab/

## Integration Role

The adapter provides the integration boundary between resilience validation workflows and Ansible automation, load balancing, routing, monitoring, or Python evidence parsing.

## Expected Outputs

- Primary availability result
- Secondary readiness result
- Failure detection result
- Traffic shift validation result
- Routing or load balancer validation result
- Post-failover health result
- Failback readiness result
- Evidence input data

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
