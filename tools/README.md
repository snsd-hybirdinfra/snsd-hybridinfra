# Repository Tooling

This directory contains the tooling used to generate, validate, and maintain the SNSD Hybrid Infrastructure repository.

The tooling layer supports scenario documentation generation, operational poster rendering, repository validation, report generation, and portfolio baseline checks.

## Tool Groups

### content-generator/

Generates and validates repository content, including:

- scenario metadata
- scenario README files
- related scenario mappings
- scenario indexes
- module and adapter indexes
- repository summary reports
- portfolio health summaries
- markdown link validation
- root README alignment checks
- top-level structure checks
- repository language checks

### diagram-renderer/

Generates visual operational posters for scenario workflows.

The renderer uses lifecycle-specific poster templates and scenario poster data to produce:

- operational-poster.svg
- operational-poster.png

## Validation Workflow

The primary validation entrypoint is:

```text
tools/content-generator/run_repository_validation.py
@'
# Repository Tooling

This directory contains the tooling used to generate, validate, and maintain the SNSD Hybrid Infrastructure repository.

The tooling layer supports scenario documentation generation, operational poster rendering, repository validation, report generation, and portfolio baseline checks.

## Tool Groups

### content-generator/

Generates and validates repository content, including:

- scenario metadata
- scenario README files
- related scenario mappings
- scenario indexes
- module and adapter indexes
- repository summary reports
- portfolio health summaries
- markdown link validation
- root README alignment checks
- top-level structure checks
- repository language checks

### diagram-renderer/

Generates visual operational posters for scenario workflows.

The renderer uses lifecycle-specific poster templates and scenario poster data to produce:

- operational-poster.svg
- operational-poster.png

## Validation Workflow

Primary validation entrypoint:

- tools/content-generator/run_repository_validation.py

This workflow verifies that the repository remains structurally consistent, reviewer-readable, and portfolio-ready.

## Role in the Platform

The tooling layer keeps the repository repeatable. It prevents the scenario catalog from becoming manually maintained documentation by enforcing generation, validation, and reporting workflows.
