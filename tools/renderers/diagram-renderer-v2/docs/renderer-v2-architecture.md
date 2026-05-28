# Diagram Renderer V2 Architecture

## Objectives

Diagram Renderer V2 is responsible for generating presentation-grade operational architecture diagrams from scenario metadata, lifecycle level, topology specification, and semantic rendering rules.

The renderer must not behave as a simple node-and-edge drawing tool. It must operate as a scenario-intent-aware operational visualization engine.

## Rendering Philosophy

The primary goal is reviewer readability.

A generated diagram must communicate:

- what operational domain is involved
- what lifecycle stage the scenario belongs to
- what signals, decisions, workflows, and outcomes exist
- how operational responsibility moves across the scenario
- what capability is being demonstrated

Visual quality is important, but semantic clarity is mandatory.

## Semantic Visualization Model

Renderer V2 uses four semantic inputs:

1. scenario metadata
2. lifecycle level
3. topology nodes and edges
4. visual section taxonomy

Each node must belong to a semantic group such as:

- connectivity
- observability
- analysis
- recovery
- resilience
- governance
- service
- platform
- data
- security

## Lifecycle-specific Layout Strategy

### L1 Visibility Layout

Focus:

- source system
- telemetry collection
- monitoring pipeline
- dashboard
- validation evidence

Reading flow:

Observed Resource → Telemetry → Monitoring → Visibility Output

### L2 Correlation Layout

Focus:

- multiple signal sources
- correlation engine
- dependency analysis
- anomaly explanation
- incident context

Reading flow:

Signals → Correlation → Dependency Mapping → Operational Insight

### L3 Recovery Layout

Focus:

- detection trigger
- recovery decision
- automation controller
- recovery workflow
- post-recovery validation

Reading flow:

Detection → Recovery Decision → Automation → Validation

### L4 Resilience Layout

Focus:

- distributed failure domain
- failover coordination
- survivability control
- cross-site validation
- resilience outcome

Reading flow:

Failure Domain → Coordination → Failover → Survivability Validation

### L5 Continuity & Governance Layout

Focus:

- enterprise service continuity
- governance control
- executive visibility
- compliance evidence
- continuity posture

Reading flow:

Enterprise Impact → Continuity Control → Governance Evidence → Reporting

## Rendering Pipeline

Scenario Metadata
→ Semantic Topology
→ Lifecycle Mutation
→ Layout Profile Selection
→ Section Placement
→ Node Rendering
→ Edge Rendering
→ Annotation Rendering
→ Legend Rendering
→ SVG Export
→ PNG Export

## Icon Registry Architecture

Icon registry maps node types and groups to visual symbols.

Examples:

- network → router/switch icon
- database → cylinder
- telemetry → signal collector
- analysis → decision/brain/graph
- automation → gear/workflow
- governance → document/shield
- dashboard → monitor

## Section-based Layout Engine

Renderer V2 should render diagrams using semantic sections.

Example sections:

- Source Systems
- Telemetry Pipeline
- Analysis Layer
- Recovery Workflow
- Governance Layer
- Validation Evidence
- Operational Outcome

## Workflow Lane System

Workflow-oriented diagrams should support side lanes:

- Detection
- Correlation
- Decision
- Recovery
- Validation
- Governance

## Dashboard Rendering System

Operational dashboards may be rendered as summary panels containing:

- alert status
- scenario status
- validation result
- affected domain
- operational outcome

## Legend & Annotation System

Every generated diagram should include:

- node type legend
- edge meaning legend
- lifecycle label
- scenario name
- operational scope

## Theme System

Renderer V2 must support dark and light themes.

Theme choice is secondary to semantic consistency.

## Export Pipeline

SVG is the authoritative artifact.

PNG is a derived artifact and may be regenerated in batch.

## Future Roadmap

1. lifecycle-aware templates
2. icon registry
3. semantic grouping
4. workflow lane rendering
5. dashboard panels
6. auto-generated legends
7. PNG export normalization
8. reviewer-quality visual polish
