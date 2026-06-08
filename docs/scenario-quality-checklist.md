# Scenario Quality Checklist

This document defines quality criteria for operational scenarios in the SNSD Hybrid Infrastructure repository.

## Quality Criteria

Each scenario should satisfy the following criteria:

- The scenario has a clear lifecycle level.
- The operational scope is understandable.
- The scenario uses reusable modules where appropriate.
- The scenario references adapters only as integration boundaries.
- The workflow avoids artificial complexity.
- The scenario separates detection, analysis, response, validation, and reporting.
- Generated evidence is present.
- Operational poster artifacts are present.
- The README includes reviewer-readable interpretation.
- Related scenarios are linked only when the relationship is meaningful.

## Lifecycle Quality

Level 1 scenarios focus on visibility and signal readiness.

Level 2 scenarios focus on correlation, dependency analysis, and incident qualification.

Level 3 scenarios focus on controlled recovery and automation validation.

Level 4 scenarios focus on distributed resilience and degraded-state coordination.

Level 5 scenarios focus on enterprise continuity, governance visibility, and recovery assurance.

## Review Principle

A scenario should be understandable as an operational workflow even when the reviewer does not execute the environment directly.
