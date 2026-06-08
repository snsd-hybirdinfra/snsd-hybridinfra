# Poster YAML Standard

This document defines the role of poster YAML files in the SNSD Hybrid Infrastructure repository.

## Purpose

Poster YAML files provide compact, visual-ready data for operational poster rendering.

They are intentionally separate from scenario metadata. Scenario metadata may contain long operational descriptions, while poster YAML should remain short enough for reliable visual rendering.

## Poster Data Principle

Poster YAML should contain concise values for:

- poster title
- lifecycle level
- operational domain
- visual sections
- workflow steps
- dashboard references
- evidence summary
- legend entries

## Rendering Boundary

Poster YAML is used by the diagram renderer to generate operational-poster.svg and operational-poster.png.

The poster is a visual summary of the scenario. It should not attempt to contain the full scenario explanation.

## Stability Rule

Long metadata fields should not be pushed directly into poster cards or visual panels. Poster content must remain compact, readable, and lifecycle-aligned.
