# Scenario Quality Model

## Purpose

This document defines the quality model used to evaluate operational scenario README files and generated scenario artifacts.

A scenario is considered high quality only when it demonstrates operational realism, lifecycle purity, execution readiness, validation evidence, and reviewer readability.

## Quality Dimensions

| Dimension | Purpose |
|---|---|
| Operational Realism | Validate that the scenario reflects realistic operational conditions |
| Lifecycle Purity | Ensure the scenario stays within its assigned lifecycle level |
| Execution Readiness | Confirm the README can guide scenario execution without external explanation |
| Reasoning Density | Ensure operational decisions are explained, not merely listed |
| Evidence Continuity | Ensure evidence supports validation and governance review |
| Dependency Visibility | Confirm upstream/downstream operational relationships are visible |
| Reviewer Readability | Ensure a reviewer can evaluate the scenario quickly and accurately |
| Artificial Complexity Avoidance | Prevent unnecessary complexity or inflated scenario scope |

---

# 1. Operational Realism

## PASS Criteria

- telemetry signals are realistic
- operational risks are explicit
- workflow reflects real operational escalation or visibility flow
- validation proves an operationally meaningful outcome

## FAIL Criteria

- generic monitoring descriptions
- unrealistic recovery or automation claims
- missing operational risk context
- tool-focused explanation without operational meaning

---

# 2. Lifecycle Purity

## PASS Criteria

- lifecycle level is clearly preserved
- excluded lifecycle behaviors are explicitly stated
- terminology matches assigned lifecycle scope
- adjacent lifecycle relationships are clear

## FAIL Criteria

- L1 scenarios include recovery or failover execution
- L2 scenarios imply recovery automation
- L3 scenarios imply distributed resilience ownership
- L4 scenarios imply enterprise continuity governance ownership
- L5 scenarios omit governance or continuity coordination

---

# 3. Execution Readiness

## PASS Criteria

- README explains the full execution flow
- operator can understand what to observe, validate, and record
- evidence locations or expected outputs are defined
- workflow can be followed without external explanation

## FAIL Criteria

- README only describes the scenario conceptually
- missing detection, analysis, validation, or evidence flow
- no operational decision points
- no PASS/FAIL validation basis

---

# 4. Reasoning Density

## PASS Criteria

Each major section explains:

- what signal or condition is observed
- why it matters operationally
- what decision it supports
- what evidence validates the outcome
- how lifecycle boundaries are preserved

## FAIL Criteria

- feature listing
- component inventory
- generic alert descriptions
- vendor/tool tutorial language
- operational decisions without reasoning

---

# 5. Evidence Continuity

## PASS Criteria

- telemetry evidence is defined
- dashboard or visualization evidence is defined where applicable
- alert timeline or incident evidence is defined where applicable
- validation evidence supports review
- evidence connects to lifecycle progression

## FAIL Criteria

- success stated without evidence
- evidence folder exists but purpose is unclear
- screenshots or logs listed without validation meaning
- governance review lacks evidence input

---

# 6. Dependency Visibility

## PASS Criteria

- related scenarios use absolute repository paths
- previous/next lifecycle relationship is visible
- rollup or convergence relationships are explained
- module and adapter responsibilities are operationally meaningful

## FAIL Criteria

- broken links
- generic related scenario lists
- missing dependency meaning
- module names without responsibility explanation

---

# 7. Reviewer Readability

## PASS Criteria

A reviewer can quickly identify:

- scenario purpose
- operational risk
- lifecycle level
- workflow flow
- validation method
- evidence output
- related scenario progression

## FAIL Criteria

- dense prose without operational structure
- missing tables where structured comparison is needed
- unclear section headings
- hidden validation assumptions
- README requires verbal explanation

---

# 8. Artificial Complexity Avoidance

## PASS Criteria

- complexity matches lifecycle level
- no unnecessary components
- no premature recovery, resilience, or continuity logic
- operational scope remains justified

## FAIL Criteria

- inflated enterprise language in simple visibility scenarios
- unnecessary automation
- resilience terminology in non-resilience scenarios
- governance claims without actual governance workflow

---

# Quality Rating

| Rating | Meaning |
|---|---|
| Gold Reference | Can serve as canonical baseline for generated scenarios |
| Production Ready | Suitable for repository use with minor refinement |
| Needs Normalization | Structurally usable but requires quality improvement |
| Reject | Violates lifecycle, evidence, or execution readiness standards |

## Gold Reference Requirements

A Gold Reference scenario must pass all dimensions and demonstrate:

- strong operational reasoning
- strict lifecycle purity
- execution-ready workflow
- evidence continuity
- reviewer-readable structure
- reusable template value

## Completion Standard

A scenario is complete only when an operator or reviewer can understand, execute, validate, and govern the workflow using the README and scenario package without external explanation.
