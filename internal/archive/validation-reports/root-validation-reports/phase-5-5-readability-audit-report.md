# Phase 5.5 Repository Readability and Redundancy Audit

## Audit Objective

This audit reviews repository readability, document layering, reviewer navigation, and redundancy risk before the final portfolio release pack.

The objective is not to add more content, but to reduce reviewer friction and clarify the authoritative reading path.

## Current Repository State

- 150 lifecycle-aligned operational scenarios
- 10 primary implementation labs
- 10 lab runtime boundaries
- 150 scenario-level evidence manifests
- 150 scenario evidence matrices
- 150 scenario validation result files
- Repository validation target: PASS

## Primary Finding

The repository is structurally complete, but the documentation layer has accumulated overlapping summary, validation, and generated report files.

The main risk is reviewer navigation friction, not missing technical content.

## Keep

### Root

- README.md

### docs/

- docs/README.md
- docs/reviewer-navigation-guide.md
- docs/scenario-to-lab-traceability.md
- docs/scenario-test-evidence-index.md
- docs/lab-coverage-matrix.md
- docs/runtime-evidence-policy.md
- docs/report-layer-guide.md
- docs/repository-tree.md
- docs/scenario-quality-checklist.md
- docs/validation-workflow.md

### validation-reports/

- validation-reports/README.md
- validation-reports/repository-validation-summary.md
- validation-reports/phase-1-baseline-summary.md
- validation-reports/phase-2-runtime-completion-report.md
- validation-reports/phase-3-traceability-report.md
- validation-reports/phase-4-reviewer-navigation-report.md
- validation-reports/phase-5-scenario-evidence-report.md

### reports/

- reports/README.md
- reports/portfolio-health-summary.md
- reports/markdown-link-check.md
- reports/top-level-structure-check.md
- reports/root-readme-alignment-check.md
- reports/repository-language-check.md

## Hide From Root README

The following files may remain in the repository but should not be emphasized in the root README:

- reports/lab-readiness-alignment-check.md
- reports/related-scenarios-generation-report.md
- reports/repository-quality-check.md
- reports/repository-simplification-candidates.md
- reports/repository-summary-report.txt
- validation-reports/lab-readiness-summary.md
- validation-reports/lab-runtime-implementation-summary.md
- validation-reports/lab-validation-summary.md
- validation-reports/scenario-validation-summary.md

## Merge Candidates

### Reviewer Entry Point Documents

- docs/scenario-review-entry-points.md
- docs/reviewer-navigation-guide.md

Recommendation:

Use docs/reviewer-navigation-guide.md as the authoritative reviewer navigation document.

### Lab Validation Summaries

- validation-reports/lab-readiness-summary.md
- validation-reports/lab-runtime-implementation-summary.md
- validation-reports/lab-validation-summary.md

Recommendation:

Use validation-reports/phase-2-runtime-completion-report.md as the authoritative runtime completion summary.

## Structural Risk

### internal/lab-evidence

The internal/lab-evidence directory can be mistaken for an implementation lab.

Recommendation:

Move or rename it in a later cleanup phase, preferably:

- internal/lab-evidence

If it remains under labs/, generators and README text must explicitly exclude it from the primary lab inventory.

## Root README Recommendation

The root README should emphasize this reading path:

1. Executive Overview
2. Reviewer Quick Start
3. Current Baseline
4. Scenario and Lab Coverage
5. Runtime Evidence Policy
6. Quality Status
7. Report Layers

The reviewer should not need to understand every generated report to evaluate the repository.

## Final Recommendation

Proceed with a readability cleanup before the final release pack.

Priority order:

1. Reduce root README links.
2. Make reviewer-navigation-guide.md authoritative.
3. Hide maintainer-only generated reports from the primary reviewer path.
4. Clarify or relocate internal/lab-evidence.
5. Regenerate repository validation and executive summary.

