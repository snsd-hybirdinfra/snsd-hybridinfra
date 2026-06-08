# Evidence Standard

This document defines the generated evidence standard for operational scenarios.

## Purpose

Generated evidence provides reviewer-facing validation documentation for each scenario.

Evidence files represent scenario-based operational validation structure. They should not be interpreted as live production execution proof unless explicitly connected to a real execution environment.

## Evidence Package

Each scenario evidence package should include:

- summary.md
- validation-evidence.md
- execution-evidence.md
- artifact-manifest.json
- artifact-checksums.json

## Evidence Content

Evidence should explain:

- observed signal
- decision context
- operational action context
- validation focus
- reviewer interpretation
- artifact role
- evidence limitation

## Evidence Principle

Evidence should make the operational workflow traceable, reviewable, and aligned with the scenario lifecycle.

It must avoid overstating generated documentation as live execution logs.
