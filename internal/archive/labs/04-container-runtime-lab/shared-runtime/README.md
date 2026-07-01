# Container Runtime Lab Shared Runtime

This shared runtime provides lab-local execution helpers for container runtime validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute container setup, validation, recovery, log collection, evidence, and cleanup workflows |
| validators/ | Check Docker runtime, container state, health checks, images, volumes, restart results, and evidence outputs |
| parsers/ | Convert Docker command output, container logs, health output, and validation results into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/04-container-runtime-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
