# Diagram Renderer

## Purpose

Generates lifecycle-aware operational diagrams for scenario documentation.

## Pipeline

diagram metadata
-> governance validation
-> template routing
-> SVG rendering
-> PNG export
-> scenario distribution

## Artifact Policy

SVG = renderer source artifact
PNG = README presentation artifact

## Outputs

- outputs/svg/
- outputs/png/
- sources/
- scenarios/<level>/<scenario>/diagrams/

## Current MVP Support

- level-1-visibility
- architecture-overview
- workflow-lifecycle

## Execution

Run from tools/renderers/diagram-renderer:

.\venv\Scripts\python.exe .\main.py
