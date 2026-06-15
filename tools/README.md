# Repository Tooling

This directory contains the generation, validation, repair, indexing, and diagram rendering tools used by the SNSD Hybrid Infrastructure repository.

The tooling layer exists to keep the repository repeatable, reviewable, and structurally consistent as the operational scenario catalog grows.

## Tooling Role

The tools support the repository as an Enterprise Operational Capability Platform by providing:

- scenario metadata generation
- scenario README generation support
- generated evidence maintenance
- poster seed and rendering support
- repository inventory generation
- markdown link validation
- root README alignment checks
- top-level structure validation
- repository language validation
- portfolio health summary generation
- full validation workflow execution

## Tool Groups

### content-generator

The content-generator tools maintain repository documentation, scenario inventory files, generated evidence, reports, indexes, and validation status.

Typical responsibilities include:

- generating scenario indexes
- generating module, adapter, and build indexes
- repairing missing scenario artifacts
- generating related scenario mappings
- updating root README inventory data
- generating repository summary reports
- validating markdown links
- validating repository structure
- validating operational language policy

### diagram-renderer

The diagram-renderer tools generate operational poster artifacts from poster YAML data.

Typical responsibilities include:

- seeding scenario poster YAML files
- rendering operational-poster.svg
- rendering operational-poster.png
- enforcing compact visual data for lifecycle-aligned diagrams

## Validation Workflow

The primary validation entrypoint is:

- tools/content-generator/run_repository_validation.py

This workflow coordinates repository cleanup, artifact repair, index generation, poster integrity checks, quality checks, README alignment checks, language validation, health summary generation, and repository summary report generation.

## Tooling Boundary

The tooling layer does not replace scenario documentation, module contracts, adapter contracts, or shared runtime contracts.

Tools provide repeatability, consistency, and validation support. Operational meaning remains documented in the scenario, module, adapter, shared-runtime, evidence, and docs layers.

## Review Value

The tooling layer demonstrates that the portfolio is not manually assembled only. It includes repeatable validation and generation workflows that help maintain consistency across 150 lifecycle-based operational scenarios.
