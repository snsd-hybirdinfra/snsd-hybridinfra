# Governance Reporting Lab Shared Runtime

This shared runtime provides lab-local execution helpers for governance validation and reporting workflows.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute cleanup, validation, coverage generation, report generation, evidence, and summary workflows |
| validators/ | Check artifact coverage, lab readiness, markdown links, structure, README alignment, repository language, and report outputs |
| parsers/ | Convert validation outputs, checker reports, coverage matrices, inventory data, and generated reports into governance summaries |

## Runtime Boundary

This runtime belongs only to:

labs/10-governance-reporting-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
