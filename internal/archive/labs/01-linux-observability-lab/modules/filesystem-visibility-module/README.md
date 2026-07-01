# Filesystem Visibility Module

## Module Purpose

Checks filesystem usage, mount availability, and capacity risk.

## Lab Boundary

This is a lab-local implementation module for:

labs/01-linux-observability-lab/

## Inputs

- Linux host state
- Process and service status
- Filesystem state
- System event data
- Prometheus node exporter metrics

## Outputs

- Raw evidence
- Processed validation output
- Scenario evidence summaries
- Lab validation report inputs

## Related Lab Runtime

- shared-runtime/runners/
- shared-runtime/validators/
- shared-runtime/parsers/
