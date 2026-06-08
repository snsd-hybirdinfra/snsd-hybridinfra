# Repository Validation Workflow

## Purpose

This document defines the repository validation workflow for the SNSD Hybrid Infrastructure platform.

The validation workflow ensures that repository structure, generated artifacts, documentation links, root README alignment, language policy, reports, and portfolio health remain consistent.

## Primary Execution Entrypoint

The executable validation workflow is maintained at:

- ../tools/content-generator/run_repository_validation.py

This script coordinates the main repository validation sequence.

## Validation Scope

The workflow validates:

- scenario artifact coverage
- generated poster artifacts
- generated evidence artifacts
- markdown links
- top-level repository structure
- root README alignment
- repository language policy
- related scenario mapping status
- generated portfolio health reports
- repository summary report output

## Expected Baseline

The expected repository baseline is:

- Markdown Broken Links: 0
- Top-Level Extra Directories: 0
- Top-Level Missing Directories: 0
- Root README Missing Links: 0
- Root README Missing Terms: 0
- Repository Language Hits: 0
- Missing Required Artifacts: 0
- Small PNG Files: 0
- Portfolio Baseline Status: PASS

## Execution Order

The validation workflow performs cleanup, artifact repair, index generation, report generation, link validation, structure validation, language validation, and summary report generation.

The workflow is designed to keep the portfolio repeatable and reviewer-readable.

## Review Interpretation

A passing validation result means that the repository structure, documentation links, generated artifacts, reports, and platform positioning are consistent.

It does not mean every scenario represents live production execution. Scenario evidence is portfolio documentation evidence unless explicitly connected to a lab or production execution result.

## Operational Boundary

The validation workflow checks repository quality and documentation consistency.

It does not replace infrastructure testing, OpenStack lab execution, monitoring validation, recovery automation testing, or production readiness assessment.
