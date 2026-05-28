# Layout Taxonomy

## Purpose

Layout taxonomy defines how operational scenarios are visually organized based on lifecycle intent.

Renderer V2 must not use a single generic layout strategy.

Different operational lifecycles require different reviewer reading flows.

---

# L1 Visibility Layout

## Objective

Represent telemetry visibility and operational monitoring flow.

## Primary Reading Direction

Left → Right

## Preferred Sections

- Observed Resource
- Telemetry
- Monitoring
- Dashboard
- Validation

## Visual Characteristics

- linear visibility chain
- telemetry emphasis
- dashboard emphasis
- minimal branching

---

# L2 Correlation Layout

## Objective

Represent multi-signal analysis and dependency reasoning.

## Primary Reading Direction

Multi-source → Correlation Center

## Preferred Sections

- Signal Sources
- Correlation Layer
- Dependency Analysis
- Incident Context
- Operational Insight

## Visual Characteristics

- fan-in topology
- dependency edges
- analysis-centered layout
- anomaly grouping

---

# L3 Recovery Layout

## Objective

Represent operational recovery workflow orchestration.

## Primary Reading Direction

Detection → Recovery → Validation

## Preferred Sections

- Detection
- Decision
- Recovery Controller
- Recovery Workflow
- Validation Outcome

## Visual Characteristics

- workflow lane structure
- orchestration emphasis
- automation highlighting
- validation closure

---

# L4 Resilience Layout

## Objective

Represent distributed survivability coordination.

## Primary Reading Direction

Failure Domain → Coordination → Failover → Survivability

## Preferred Sections

- Failure Domain
- Coordination Layer
- Failover Systems
- Recovery Validation
- Resilience Outcome

## Visual Characteristics

- multi-domain layout
- distributed grouping
- coordination hub
- cross-site relationships

---

# L5 Continuity Layout

## Objective

Represent enterprise continuity governance.

## Primary Reading Direction

Enterprise Impact → Governance → Reporting

## Preferred Sections

- Enterprise Scope
- Continuity Control
- Governance Layer
- Compliance Evidence
- Executive Reporting

## Visual Characteristics

- governance-heavy layout
- reporting panels
- operational summary zones
- continuity status emphasis

---

# Shared Layout Rules

## Rules

- semantic grouping required
- reviewer readability prioritized
- operational flow must remain visible
- edge crossing minimized
- validation outcome visible
- lifecycle identity visually explicit

---

# Future Layout Features

- adaptive layout engine
- edge routing engine
- workflow swimlanes
- dashboard overlays
- evidence rendering
- operational timeline rendering
