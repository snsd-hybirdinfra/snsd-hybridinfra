# Diagram Renderer Tools

This directory contains tools used to seed and render operational poster artifacts for scenario documentation.

## Purpose

The diagram-renderer layer converts compact poster YAML data into visual operational artifacts.

Each scenario should have:

- diagrams/operational-poster.svg
- diagrams/operational-poster.png

## Poster Data Boundary

Poster YAML is intentionally compact.

Scenario metadata can contain detailed operational descriptions, but poster YAML should contain visual-ready values that fit into lifecycle-aligned diagram sections.

Long metadata fields should not be inserted directly into poster cards or panels because they can break poster readability.

## Rendering Workflow

The rendering workflow uses scenario poster YAML data to produce SVG and PNG artifacts.

The renderer should preserve:

- lifecycle-specific layout
- readable visual hierarchy
- compact operational wording
- consistent poster dimensions
- reviewer-friendly visual summaries

## Relationship to Scenario README

The poster is a visual summary. It does not replace the scenario README, evidence files, module contracts, adapter contracts, or shared runtime contracts.

The README provides operational explanation. The poster provides quick visual orientation.

## Review Value

Operational posters help reviewers understand scenario purpose, lifecycle placement, workflow shape, dashboard context, and evidence outputs without reading every file first.
