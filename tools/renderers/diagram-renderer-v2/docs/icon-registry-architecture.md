# Icon Registry Architecture

## Purpose

The icon registry defines how semantic operational entities are visually represented in Diagram Renderer V2.

Icons are semantic identifiers.

They must improve reviewer comprehension and operational readability.

## Core Principle

Icons must communicate operational meaning immediately.

Renderer V2 should avoid decorative icon usage without semantic value.

## Registry Structure

node_type -> semantic_group -> icon_identifier -> rendering_style

## Primary Semantic Domains

### Connectivity

Represents network communication and connectivity infrastructure.

Node Types:

- network
- vpn
- routing
- gateway
- firewall
- load-balancer

Suggested Visuals:

- router
- network switch
- directional flow
- tunnel

### Observability

Represents telemetry and monitoring systems.

Node Types:

- telemetry
- monitoring
- metrics
- logging
- dashboard

Suggested Visuals:

- signal
- pulse
- monitoring screen
- chart
- event stream

### Analysis

Represents operational reasoning systems.

Node Types:

- analysis
- correlation
- anomaly
- intelligence

Suggested Visuals:

- graph
- decision node
- analysis hub
- magnifier

### Recovery

Represents operational remediation workflows.

Node Types:

- automation
- orchestration
- remediation
- recovery

Suggested Visuals:

- gear
- workflow
- automation pipeline
- restart arrow

### Resilience

Represents survivability coordination systems.

Node Types:

- resilience
- failover
- coordination
- survivability

Suggested Visuals:

- distributed topology
- redundancy
- failover arrows
- regional synchronization

### Governance

Represents continuity and governance control systems.

Node Types:

- governance
- continuity
- reporting
- compliance

Suggested Visuals:

- shield
- document
- audit record
- reporting dashboard

### Validation

Represents verification and operational evidence systems.

Node Types:

- validation
- evidence
- verification
- status

Suggested Visuals:

- checklist
- validation badge
- status indicator
- operational report

## Rendering Rules

- icons must remain visually consistent
- icon size must remain normalized
- icon meaning must remain stable across scenarios
- icon color must follow semantic grouping
- operational readability overrides stylistic preference

## Registry Expansion Rules

New icon mappings must define:

- semantic meaning
- rendering context
- lifecycle compatibility
- accessibility visibility
- dark/light theme compatibility

## Future Roadmap

- SVG icon packs
- animated operational states
- lifecycle-aware icon variants
- status overlays
- evidence indicators
- operational severity coloring
