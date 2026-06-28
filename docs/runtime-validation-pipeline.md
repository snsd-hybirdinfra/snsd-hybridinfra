# Runtime Validation Pipeline

This repository includes a runtime validation pipeline for the local hybrid infrastructure lab.

The pipeline collects runtime evidence from the implemented VM lab, generates scenario-level validation evidence, builds an index document, and runs a smoke check against the active monitoring stack.

## Runtime Scope

- Ubuntu VM node inventory
- Node Exporter metrics
- Prometheus target health
- Grafana datasource/dashboard provisioning
- Loki and Promtail log pipeline
- Blackbox HTTP/TCP/ICMP probe checks
- HAProxy service continuity
- MariaDB and mysqld_exporter metrics
- Restic backup and restore validation metrics
- Alertmanager and Prometheus alert rule status

## Execution Environment

Run infrastructure and validation commands from WSL.

Run Git commands from PowerShell.

Recommended repository path in WSL:

```
/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra
```

Recommended repository path in PowerShell:

```
C:\Users\swfco\OneDrive\바탕 화면\github\snsd-hybridinfra
```

## Full Runtime Validation Pipeline

From WSL:

```
cd "/mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra"
tools/pipeline/run_runtime_validation_pipeline.sh
```

The pipeline runs the following steps:

1. Collect runtime evidence
2. Generate scenario-level lab runtime validation evidence
3. Generate lab runtime validation index
4. Run runtime smoke check

Expected final output:

```
[OK] runtime validation pipeline completed
```

## Generated Evidence

Raw runtime evidence is generated under:

```
labs/evidence/generated/
```

This directory is treated as local runtime evidence.

Reviewer-facing scenario evidence is generated under:

```
scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md
```

The runtime validation index is generated at:

```
docs/lab-runtime-validation-index.md
```

## Validation Targets

The smoke check verifies:

- Ansible connectivity
- systemd service state
- Prometheus health
- Grafana health
- Loki readiness
- Alertmanager health
- HAProxy frontend continuity
- Blackbox probe success
- Backup and restore metrics
- Scenario evidence count
- NOT_FOUND absence
- Runtime validation index existence

## Expected Coverage

Expected scenario evidence count:

```
150
```

Expected index summary:

```
Total scenarios: 150
OK: 150
Missing evidence: 0
Contains NOT_FOUND: 0
```

## Git Policy

Commit reviewer-facing generated evidence:

```
tools/evidence/
tools/validation/
tools/pipeline/
docs/lab-runtime-validation-index.md
scenarios/*/*/evidence/generated/lab-runtime-validation.md
```

Do not commit local raw runtime evidence unless explicitly needed:

```
labs/evidence/generated/
```

## Standard Workflow

From WSL:

```
tools/pipeline/run_runtime_validation_pipeline.sh
```

From PowerShell:

```
git status --short
git add tools/evidence/collect_runtime_evidence.sh
git add tools/evidence/generate_lab_runtime_validation.py
git add tools/evidence/generate_lab_runtime_validation_index.py
git add tools/validation/runtime_smoke_check.sh
git add tools/pipeline/run_runtime_validation_pipeline.sh
git add docs/runtime-validation-pipeline.md
git add docs/lab-runtime-validation-index.md
git add scenarios/*/*/evidence/generated/lab-runtime-validation.md
git commit -m "Document runtime validation pipeline"
git push
```
