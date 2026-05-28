# Diagram Renderer V2

Diagram Renderer V2 is the next-generation operational visualization engine for the repository.

It is designed to generate presentation-grade operational architecture diagrams from lifecycle-aware semantic topology specifications.

## Positioning

Renderer V2 is not a generic diagram drawing tool.

It is a scenario-intent-aware operational visualization engine.

## Current Scope

Renderer V2 focuses on:

- lifecycle-aware layout profiles
- semantic section rendering
- workflow lane visualization
- icon registry integration
- dashboard panel rendering
- legend and annotation generation
- SVG-first artifact generation
- PNG regeneration as a derived export step

## Authoritative Artifact Strategy

SVG is the authoritative diagram artifact.

PNG is a derived artifact and may be regenerated later.

## Lifecycle Rendering Profiles

- L1 Visibility
- L2 Correlation
- L3 Recovery
- L4 Resilience
- L5 Continuity & Governance

## Documentation

See:

- docs/renderer-v2-architecture.md
- docs/layout-taxonomy.md
- docs/semantic-section-taxonomy.md
- docs/icon-registry-architecture.md
- docs/yaml-schema-v2.md
- docs/layout-engine-architecture.md
- docs/workflow-lane-architecture.md
- docs/dashboard-rendering-architecture.md
- docs/legend-annotation-architecture.md
- docs/theme-system-architecture.md

## Examples

See:

- examples/l1-visibility-example.yaml
- examples/l2-correlation-example.yaml
- examples/l3-recovery-example.yaml
- examples/l4-resilience-example.yaml
- examples/l5-governance-example.yaml
