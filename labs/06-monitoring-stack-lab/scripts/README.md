# Monitoring Stack Lab Scripts

This directory contains lab-local execution entrypoints for the Monitoring Stack Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare monitoring stack prerequisites and evidence directories |
| validate.sh | Execute Prometheus, Grafana, exporter, metric, alert, and evidence validation checks |
| cleanup.sh | Clean temporary monitoring validation outputs while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/06-monitoring-stack-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- Prometheus service preparation
- Grafana service preparation
- node exporter validation
- scrape target validation
- metric query validation
- dashboard readiness validation
- alert rule readiness validation
- monitoring evidence generation
