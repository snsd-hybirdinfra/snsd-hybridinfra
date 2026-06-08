# Repository Reports

This directory contains generated repository reports for the SNSD Hybrid Infrastructure platform.

Reports provide reviewer-facing evidence of repository structure, scenario coverage, artifact completeness, validation status, and portfolio health.

## Report Role

The reports layer supports repository review by making validation results visible and repeatable.

It helps answer:

- How many scenarios exist?
- Are required artifacts present?
- Are markdown links valid?
- Is the top-level repository structure clean?
- Does the root README align with repository inventory?
- Are repository language policies respected?
- Is the portfolio baseline currently passing?

## Primary Reports

### repository-summary-report.txt

Summarizes repository positioning, scenario inventory, artifact coverage, validation status, platform layers, and current baseline state.

### portfolio-health-summary.md

Provides a reviewer-readable health summary of the portfolio, including quality status and validation interpretation.

### scenario-index.md

Provides a generated index of lifecycle-based operational scenarios.

### module-index.md

Provides a generated index of reusable operational capability modules.

### adapter-index.md

Provides a generated index of tool and platform integration adapters.

### build-index.md

Provides a generated index of build foundation documentation.

### related-scenarios-generation-report.md

Documents conservative lifecycle-aware scenario relationship generation and pending relationship counts.

## Validation Baseline

The expected validation baseline is:

- Markdown Broken Links: 0
- Top-Level Extra Directories: 0
- Top-Level Missing Directories: 0
- Root README Missing Links: 0
- Root README Missing Terms: 0
- Repository Language Hits: 0
- Missing Required Artifacts: 0
- Portfolio Baseline Status: PASS

## Relationship to Tools

Reports are generated or refreshed by tools under:

- tools/content-generator/

The main validation workflow is:

- tools/content-generator/run_repository_validation.py

## Review Boundary

Reports represent repository quality and documentation validation state.

They do not claim live production infrastructure execution. They provide audit-style evidence that the portfolio structure, generated artifacts, and documentation baseline are consistent and reviewable.
