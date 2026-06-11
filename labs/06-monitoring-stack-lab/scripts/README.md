# Monitoring Stack Scripts

## Purpose

These scripts define the execution boundary for the Monitoring Stack Lab.

## Scripts

| Script | Purpose |
|---|---|
| setup.sh | Start Prometheus and Grafana through Docker Compose |
| validate.sh | Validate container status, Prometheus health, Prometheus targets, and Grafana health |
| cleanup.sh | Stop and remove the monitoring stack containers |

## Execution Flow

    bash scripts/setup.sh
    bash scripts/validate.sh
    bash scripts/cleanup.sh

## Evidence Policy

Generated runtime evidence under evidence/generated/ is local-only and intentionally ignored by Git.