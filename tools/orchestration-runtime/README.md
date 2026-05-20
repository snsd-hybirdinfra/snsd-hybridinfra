# Orchestration Runtime

## Purpose

Coordinates the repository toolchain execution order and artifact handoff flow.

## Responsibilities

- define tool execution order
- coordinate metadata handoff
- coordinate relationship graph handoff
- coordinate scenario generation
- coordinate diagram rendering
- coordinate taxonomy validation
- coordinate governance validation

## Toolchain Order

1. metadata-parser
2. relationship-mapper
3. scenario-generator
4. diagram-renderer
5. taxonomy-validator
6. governance-checker

## Artifact Flow

metadata
-> normalized metadata
-> relationship graph
-> scenario package
-> diagram artifacts
-> taxonomy report
-> governance report

## Execution

Run from repository root:

python tools/orchestration-runtime/main.py
