# Governance Reporting Lab Scripts

This directory contains lab-local execution entrypoints for the Governance Reporting Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare repository validation, reporting, governance evidence, and summary boundaries |
| validate.sh | Execute quality, coverage, structure, markdown, README, language, report, and evidence validation checks |
| cleanup.sh | Clean temporary governance reporting outputs while preserving reports and evidence |

## Execution Boundary

These scripts belong only to:

labs/10-governance-reporting-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, validation reports, governance summaries, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- repository validation execution
- artifact coverage validation
- lab structure validation
- markdown link validation
- README alignment validation
- repository language validation
- coverage report validation
- governance summary generation
- reviewer-facing report generation
