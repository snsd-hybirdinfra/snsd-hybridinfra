# Golden Tooling Flow

## Purpose

This document defines the authoritative operational flow of the repository toolchain.

## Golden Flow

taxonomy catalog
→ bulk scenario metadata generation
→ scenario package generation
→ topology rendering
→ governance validation
→ runtime observability
→ artifact lineage
→ execution graph

## Authoritative Execution Commands

### Bootstrap

    python .\tools\bootstrap-runtime\main.py

### Manifest Discovery

    python .\tools\shared-runtime\manifest-discovery\main.py

### Orchestration

    python .\tools\orchestration-runtime\main.py

### Runtime Registry Export

    python .\tools\orchestration-runtime\export_registry.py

## Freeze Decision

The current tooling flow is frozen as the MVP operational baseline.

Future changes must preserve:

- manifest-governed tool registration
- dependency-aware execution
- tool boundary validation
- runtime workspace isolation
- execution logging
- artifact tracking
- artifact lineage
- execution graph generation

## Deferred Enhancements

The following are deferred until the next phase:

- advanced README template refinement
- production diagram quality upgrade
- PNG export standardization
- parallel-safe execution
- dashboard UI
