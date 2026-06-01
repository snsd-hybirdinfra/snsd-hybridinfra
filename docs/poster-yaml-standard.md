# Poster YAML Standard

poster.yaml is the dedicated visualization source for scenario operational posters.

## Purpose

metadata.yaml is used for scenario documentation, README generation, evidence generation, and portfolio consistency.

poster.yaml is used only for visual poster rendering.

## Resolution Rule

The diagram renderer must resolve poster input in this order:

1. Use poster.yaml when it exists in the scenario directory.
2. Fallback to metadata.yaml when poster.yaml does not exist.
3. Output files must always be written to diagrams/operational-poster.svg and diagrams/operational-poster.png.

## Scenario Structure

scenarios/<level>/<scenario>/
  metadata.yaml
  poster.yaml
  README.md
  diagrams/
    operational-poster.svg
    operational-poster.png
  evidence/
    generated/

## Required Poster YAML Shape

poster:
  title: Example Scenario
  subtitle: Scenario-driven Infrastructure Operations Portfolio
  scenario: example-scenario
  lifecycle: level-3-recovery
  level: Recovery and Automation
  scope: Infrastructure Operations
  environment: Hybrid Infrastructure
  width: 2600
  height: 1900

sections:
  - id: incident-trigger
    title: Incident Trigger
    summary: TRIGGERED
    description: Operational condition requires recovery response.
    cards:
      - title: Trigger Signal
        subtitle: Incident or recovery trigger detected
        type: alert
        status: Detected
        icon: alert

workflow:
  title: Operational Workflow
  steps:
    - title: Step 1
      description: Qualify incident trigger
      status: Ready

summary:
  title: Recovery Summary
  items:
    - Recovery trigger qualified
    - Recovery workflow selected

dashboards:
  - title: Recovery State
    widgets:
      - label: Recovery
        value: READY
        status: healthy

legend:
  - label: Incident Trigger
    color: red
  - label: Recovery Control
    color: purple
  - label: Automation Execution
    color: cyan
  - label: Recovery Validation
    color: green

## Governance

poster.yaml should be used for flagship or showcase scenarios.

Generic scenarios may omit poster.yaml and rely on metadata-based fallback rendering.
