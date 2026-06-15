# Shared Runtime

This directory is the repository-level shared runtime catalog.

Shared runtime entries describe common execution, telemetry, evidence, orchestration, and integration concepts used across the platform.

## Repository Role

Top-level shared-runtime is not the primary executable runtime location.

It defines shared runtime capability boundaries and common operational patterns.

## Implementation Boundary

Actual lab-specific runners, validators, parsers, and execution utilities belong under:

labs/<lab-name>/shared-runtime/

## Runtime Catalog

Shared runtime concepts include orchestration runtime, telemetry pipeline, evidence runtime, and integration services.
