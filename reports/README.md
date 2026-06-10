# Reports

This directory contains generated detailed validation outputs.

Reports in this directory are produced by repository validation tools and are intended for internal quality inspection.

## Report Role

reports/ is the detailed generated output layer.

Reviewer-facing summaries are maintained under:

validation-reports/

## Generated Reports

Typical generated reports include:

- markdown-link-check.md
- portfolio-health-summary.md
- related-scenarios-generation-report.md
- repository-language-check.md
- repository-quality-check.md
- repository-summary-report.txt
- root-readme-alignment-check.md
- top-level-structure-check.md

## Validation Workflow

Run the repository validation workflow with:

python tools/content-generator/run_repository_validation.py
