# Linux Observability Lab Shared Runtime

This shared runtime provides lab-local execution helpers for Linux observability validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute setup, validation, and evidence workflows |
| validators/ | Check Linux host, process, filesystem, and telemetry conditions |
| parsers/ | Convert command output and metric responses into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/01-linux-observability-lab/

Repository-level shared-runtime remains a catalog layer.
