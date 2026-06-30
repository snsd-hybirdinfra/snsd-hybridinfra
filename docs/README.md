# Documentation Guide

This directory contains reviewer-facing documentation for the SNSD Hybrid Infrastructure portfolio.

## Review Order

| Order | Document | Role |
|---:|---|---|
| 1 | `architecture.md` | Understand the runtime architecture and operational control points |
| 2 | `runtime-validation-pipeline.md` | Understand how runtime evidence is collected, generated, and validated |
| 3 | `failure-injection-scenarios.md` | Understand controlled failure injection and recovery validation |
| 4 | `lab-runtime-validation-index.md` | Review lifecycle scenario evidence coverage |

## Document Boundaries

### `architecture.md`

Architecture-level explanation.

Use this document to understand:

- Runtime architecture layers
- Service entrypoint model
- Observability components
- Incident coordination layer
- Runtime validation and failure injection control points

### `runtime-validation-pipeline.md`

Validation-flow explanation.

Use this document to understand:

- Runtime evidence collection
- Scenario-level evidence generation
- Validation index generation
- Runtime smoke checks
- Repository static checks
- Recommended validation order

### `failure-injection-scenarios.md`

Failure-and-recovery explanation.

Use this document to understand:

- Web backend failure
- Observability loss
- Database failure
- HAProxy service entrypoint failure
- Backup failure
- Recovery evidence model

### `lab-runtime-validation-index.md`

Evidence coverage index.

Use this document to review:

- Total scenario count
- Evidence status
- Missing evidence detection
- NOT_FOUND detection
- Scenario-to-evidence mapping

## Important Boundary

The 150 scenarios are not 150 separate infrastructure deployments.

They are lifecycle-aligned operational scenario packages connected to shared lab runtime evidence.
