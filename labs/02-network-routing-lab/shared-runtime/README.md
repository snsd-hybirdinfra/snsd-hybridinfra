# Network Routing Lab Shared Runtime

This shared runtime provides lab-local execution helpers for network routing validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute route, reachability, DNS, VPN, and evidence workflows |
| validators/ | Check network path, route table, tunnel, latency, and DNS conditions |
| parsers/ | Convert command output and telemetry responses into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/02-network-routing-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
