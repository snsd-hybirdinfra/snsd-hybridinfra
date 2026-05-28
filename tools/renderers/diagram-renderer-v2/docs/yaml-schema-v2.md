# YAML Schema V2

## Purpose

Schema V2 defines the semantic operational visualization model used by Diagram Renderer V2.

The schema is lifecycle-aware and section-aware.

It is designed for operational readability rather than generic graph rendering.

---

# Top-level Structure

- diagram
- lifecycle
- layout
- sections
- nodes
- edges
- annotations
- dashboards
- legends

---

# Diagram Metadata

## diagram

Defines diagram identity and rendering profile.

Fields:

- id
- title
- scenario
- lifecycle
- theme
- layout_profile

Example:

- id: architecture-overview
- title: VPN Recovery Architecture
- scenario: vpn-tunnel-recovery-automation
- lifecycle: level-3-recovery
- theme: dark
- layout_profile: recovery-workflow

---

# Layout Definition

## layout

Defines rendering behavior.

Fields:

- direction
- spacing
- section_gap
- node_gap
- workflow_lanes
- auto_grouping

---

# Semantic Sections

## sections

Defines operational semantic zones.

Fields:

- id
- label
- type
- position
- emphasis

Example section types:

- source
- telemetry
- analysis
- recovery
- resilience
- governance
- validation

---

# Nodes

## nodes

Represents operational entities.

Fields:

- id
- label
- type
- group
- section
- criticality
- icon
- status
- metadata

---

# Edges

## edges

Represents operational relationships.

Fields:

- from
- to
- type
- direction
- label
- severity
- animated

Example edge types:

- telemetry-flow
- dependency
- failover
- orchestration
- validation
- governance-reporting

---

# Workflow Lanes

## workflow_lanes

Represents lifecycle progression lanes.

Examples:

- Detection
- Correlation
- Decision
- Recovery
- Validation
- Governance

---

# Dashboards

## dashboards

Represents operational summary panels.

Fields:

- id
- title
- metrics
- alerts
- validation_status
- operational_summary

---

# Annotations

## annotations

Represents reviewer guidance and operational context.

Fields:

- text
- target
- severity
- annotation_type

---

# Legends

## legends

Represents generated visual meaning references.

Fields:

- node_types
- edge_types
- lifecycle_labels
- status_meanings

---

# Rendering Rules

- every node requires section assignment
- every node requires semantic grouping
- lifecycle layout must remain visible
- validation outcome must remain visible
- governance visibility required for L5

---

# Future Extensions

- operational timelines
- animated SVG states
- incident overlays
- live telemetry overlays
- evidence attachments
- interactive reviewer mode
