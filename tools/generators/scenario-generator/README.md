# Scenario Generator

## Purpose

Generates operational scenario packages from structured metadata.

## Responsibilities

- scenario package generation
- README rendering
- lifecycle-aware defaults
- diagram profile orchestration
- diagram renderer invocation
- operational structure generation

## Pipeline

scenario metadata
-> metadata validation
-> lifecycle profile mapping
-> README rendering
-> scenario structure generation
-> diagram renderer invocation
-> PNG distribution

## Generated Structure

- README.md
- architecture/
- implementation/
- evidence/
- artifacts/
- diagrams/

## Lifecycle Awareness

Supports lifecycle-aware defaults:

- level-1-visibility
- level-2-correlation
- level-3-recovery
- level-4-resilience
- level-5-continuity

## Execution

.\venv\Scripts\python.exe .\main.py
