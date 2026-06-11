# Logging Correlation Execution Boundary Note

## Execution Mode

The Logging Correlation Lab validates event normalization, timeline reconstruction, and correlation rule evaluation using file-based operational logs.

This is the first execution boundary for log correlation before introducing OpenSearch-based indexing and query workflows.

## Upstream Context

This lab correlates runtime signals modeled from:

- 01-linux-observability-lab
- 03-ansible-automation-lab
- 04-container-runtime-lab
- 06-monitoring-stack-lab

## Correlation Boundary

This lab validates:

- Log dataset readability
- Event field normalization
- Service and severity counting
- Timeline reconstruction
- Correlation rule evaluation
- Local runtime summary generation

This lab does not validate:

- OpenSearch indexing
- Logstash or Fluent Bit pipelines
- Distributed log ingestion
- Long-term log retention
- SIEM-grade detection rules
- Production alert routing

## Evidence Policy

Generated runtime evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside repository commit history.

## Runtime Summary

Local runtime execution produces:

- evidence/generated/summary/logging-correlation-execution-summary.md

This summary is consumed by the local repository executive summary generator when present.