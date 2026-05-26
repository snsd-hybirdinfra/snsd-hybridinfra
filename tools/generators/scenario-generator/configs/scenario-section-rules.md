# Scenario Section Rules

## Purpose

This document defines section-level governance rules for operational scenario README files.

A scenario README must provide enough operational context for an operator or reviewer to understand, execute, validate, and govern the scenario workflow without requiring external explanation.

## Documentation Philosophy

Scenario documentation is not a feature description or implementation tutorial.

Each README must function as:

- an operational execution guide
- an operational reasoning artifact
- a validation evidence map
- a lifecycle continuity document

## Core Rule

Every section must contribute to operational decision-making visibility.

If a section only lists tools, components, or generic actions without explaining operational meaning, it is incomplete.

## Section Governance Rules

### Scenario Purpose

Required:

- define the operational risk being addressed
- explain why the scenario exists
- clarify lifecycle boundary
- explain downstream operational dependency

Forbidden:

- generic objective statements
- vendor/tool marketing language
- implementation-first wording

### Operational Relevance

Required:

- explain why the scenario matters operationally
- describe failure or visibility risk
- explain impact on downstream lifecycle workflows

Forbidden:

- abstract lifecycle explanation without scenario-specific risk
- generic importance claims

### Scenario Objectives

Required:

- describe measurable operational capabilities
- connect each objective to validation or evidence
- preserve lifecycle purity

Forbidden:

- vague goals
- feature lists
- objectives without validation meaning

### Scenario Architecture

Required:

- expose operational components and boundaries
- explain module responsibilities
- show dependency visibility
- connect architecture to lifecycle purpose

Forbidden:

- component inventory only
- diagram without operational explanation
- vendor-centric descriptions

### Detection Workflow

Required:

- explain telemetry anomaly interpretation
- define visibility escalation triggers
- identify operational risk indicators
- preserve lifecycle boundary

Forbidden:

- simple alert listing
- metric-only descriptions
- recovery discussion in L1 visibility scenarios

### Correlation & Analysis

Required:

- explain operational interpretation
- identify dependency reasoning where applicable
- describe false-positive elimination logic
- clarify analysis boundaries by lifecycle level

Forbidden:

- generic “analyze metrics” wording
- unsupported root-cause claims
- premature recovery decisions

### Recovery & Automation

Required:

- explain recovery decision criteria where lifecycle level allows recovery
- describe automation safety boundaries
- define validation requirements after action

Forbidden:

- recovery without validation
- automation without governance
- rollback/failover language in visibility-only scenarios

### Validation & Governance

Required:

- explain what each validation proves operationally
- connect validation to evidence outputs
- define reviewer PASS/FAIL basis
- preserve governance continuity

Forbidden:

- checklist-only validation
- success claims without evidence
- governance-free automation

### Evidence Outputs

Required:

- identify required evidence artifacts
- explain why evidence matters
- define evidence continuity across lifecycle stages

Forbidden:

- evidence folder references without purpose
- screenshots without validation meaning

### Related Scenarios

Required:

- show lifecycle continuity
- explain previous/next scenario relationship
- distinguish dependency, rollup, and convergence relationships

Forbidden:

- link lists without relationship meaning
- broken or relative ambiguous paths

## Operational Reasoning Density Rules

A section has acceptable reasoning density only when it explains:

- what operational signal is observed
- why the signal matters
- what decision it supports
- what evidence validates the decision
- how lifecycle boundaries are preserved

## Evidence Continuity Rules

Every scenario must make evidence continuity visible.

Evidence must support:

- telemetry visibility
- operational interpretation
- validation outcome
- governance review
- lifecycle progression

## Reviewer Readability Rules

A reviewer must be able to:

- understand the operational objective
- follow the execution flow
- identify decision points
- validate expected outcomes
- locate evidence outputs
- understand lifecycle progression

without verbal explanation from the author.

## Forbidden Anti-Patterns

The following patterns are not allowed:

- implementation tutorial style
- vendor marketing language
- feature listing without operational context
- alert-only workflows
- recovery without validation
- governance-free automation
- evidence omission
- isolated tooling descriptions
- lifecycle terms used outside their lifecycle boundary
- vague claims such as “improves reliability” without operational proof

## Scenario Completion Standard

A scenario README is complete only when an operator or reviewer can:

- understand why the scenario exists
- execute the operational workflow
- interpret telemetry and alerts
- identify operational decision points
- validate expected outcomes
- collect evidence
- understand related lifecycle progression

without requiring external explanation.
