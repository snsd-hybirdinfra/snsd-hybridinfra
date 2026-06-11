# Logging Correlation Lab Shared Runtime

This shared runtime provides lab-local execution helpers for logging and correlation validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute log collection, search validation, correlation, evidence, and cleanup workflows |
| validators/ | Check log source availability, OpenSearch readiness, query output, correlation readiness, and evidence outputs |
| parsers/ | Convert raw logs, OpenSearch results, normalized events, and correlation output into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/07-logging-correlation-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
