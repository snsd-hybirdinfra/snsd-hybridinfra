# Legend & Annotation Architecture

## Purpose

Legend and annotation systems provide semantic interpretation support for Diagram Renderer V2.

Operational diagrams must remain understandable without external explanation.

Legends and annotations exist to accelerate reviewer operational comprehension.

---

# Core Principle

Operational meaning must remain visible.

The renderer should explain:

- what node types represent
- what edge types represent
- what lifecycle stage is active
- what operational outcome occurred
- what validation succeeded or failed

---

# Legend System

## Purpose

Legends define visual meaning references.

Legends reduce reviewer ambiguity.

---

# Legend Categories

## Node Type Legend

Represents semantic node meaning.

Examples:

- network
- telemetry
- analysis
- recovery
- governance
- validation

---

## Edge Type Legend

Represents operational relationship meaning.

Examples:

- telemetry-flow
- dependency
- orchestration
- failover
- governance-reporting
- validation

---

## Severity Legend

Represents operational severity interpretation.

Examples:

- INFO
- WARNING
- DEGRADED
- CRITICAL
- RECOVERED
- VALIDATED

---

## Lifecycle Legend

Represents lifecycle classification.

Examples:

- L1 Visibility
- L2 Correlation
- L3 Recovery
- L4 Resilience
- L5 Continuity

---

# Annotation System

## Purpose

Annotations provide operational reasoning guidance.

Annotations explain:

- operational transitions
- recovery triggers
- validation outcomes
- governance reporting
- resilience coordination

---

# Annotation Types

## Operational Annotation

Explains operational behavior.

Examples:

- traffic rerouted
- failover initiated
- dependency degraded
- validation completed

---

## Governance Annotation

Explains governance visibility.

Examples:

- compliance evidence generated
- executive reporting updated
- continuity status confirmed

---

## Validation Annotation

Explains operational verification.

Examples:

- service restored
- dependency verified
- telemetry normalized

---

## Incident Annotation

Explains incident context.

Examples:

- anomaly detected
- blast radius expanded
- escalation initiated

---

# Placement Strategy

## Inline Annotation

Placed near nodes or edges.

Purpose:

Immediate operational context.

---

## Side Annotation Panel

Placed beside workflow sections.

Purpose:

Reviewer guidance.

---

## Validation Summary Section

Placed near validation dashboards.

Purpose:

Operational closure visibility.

---

# Rendering Rules

## Rules

- annotations must remain concise
- legends must remain visually stable
- operational meaning prioritized
- governance visibility explicit
- validation outcome visible

---

# Visual Strategy

Legends and annotations may use:

- bordered containers
- semantic color grouping
- lifecycle indicators
- operational badges
- validation highlights

---

# Future Roadmap

- interactive annotations
- hover explanations
- operational replay guidance
- reviewer walkthrough mode
- timeline-linked annotations
- evidence-linked annotations
