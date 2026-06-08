# Scenario README Standard

This document defines the README documentation standard for operational scenarios in the SNSD Hybrid Infrastructure repository.

## Purpose

Scenario README files explain lifecycle-based operational workflows. They are not isolated troubleshooting notes or implementation tutorials.

Each scenario README should describe:

- scenario metadata
- operational overview
- objectives
- scenario architecture
- used modules
- used adapters
- infrastructure components
- operational workflow
- detection context
- correlation and analysis context
- incident or alert workflow
- recovery and automation workflow
- recovery validation
- monitoring and visibility
- operational components
- generated evidence
- validation checklist
- related scenario policy
- operational interpretation

## Documentation Principle

Scenario documentation should show how reusable platform capabilities are composed into operational workflows.

The README should explain what the operator observes, how the workflow is interpreted, which modules and adapters are involved, what evidence is produced, and how the scenario is validated.

## Relationship Policy

Scenario relationships are maintained conservatively through lifecycle-aware mapping. Only clearly related operational workflows are linked. Uncertain relationships remain pending by design.
