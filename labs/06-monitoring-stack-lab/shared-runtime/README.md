# Monitoring Stack Lab Shared Runtime

This shared runtime provides lab-local execution helpers for monitoring stack validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute Prometheus, Grafana, exporter, alert, and evidence workflows |
| validators/ | Check scrape targets, metric queries, dashboards, alert rules, and exporter readiness |
| parsers/ | Convert Prometheus API responses, Grafana metadata, and validation output into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/06-monitoring-stack-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
