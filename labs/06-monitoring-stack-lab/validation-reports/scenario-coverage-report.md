# Monitoring Stack Lab Scenario Coverage Report

This report summarizes repository scenarios mapped to the Monitoring Stack Lab.

## Lab

- Lab: 06-monitoring-stack-lab
- Focus: Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence generation.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |

## Coverage Summary

Mapped scenarios: 7

## Mapped Scenarios

| Scenario | Level | Domain | Lab |
|---|---|---|---|
| [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) | 6 |
| [Api Gateway Health Monitoring](../scenarios/level-1-visibility/api-gateway-health-monitoring/) | level-1-visibility | API / Gateway | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Application Runtime Monitoring](../scenarios/level-1-visibility/application-runtime-monitoring/) | level-1-visibility | Application Runtime | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Message Queue Monitoring](../scenarios/level-1-visibility/message-queue-monitoring/) | level-1-visibility | Message Queue | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Microservice Health Monitoring](../scenarios/level-1-visibility/microservice-health-monitoring/) | level-1-visibility | Microservice | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Api Latency Correlation](../scenarios/level-2-correlation/api-latency-correlation/) | level-2-correlation | API / Service | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |
| [Api Service Recovery](../scenarios/level-3-recovery/api-service-recovery/) | level-3-recovery | API / Service | [06-monitoring-stack-lab](../labs/06-monitoring-stack-lab/) |

## Validation Interpretation

This lab validates monitoring-oriented visibility and validation scenarios by preparing Prometheus, Grafana, exporter targets, metric queries, dashboard readiness checks, alert readiness checks, and evidence outputs for mapped scenarios.

## Evidence Relationship

Expected evidence is produced under:

- evidence/raw/
- evidence/processed/
- evidence/summary/
- validation-reports/lab-validation-report.md
