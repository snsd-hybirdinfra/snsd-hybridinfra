# Runtime Evidence Policy

## Purpose

This document defines how generated evidence is handled in SNSD Hybrid Infrastructure.

The repository separates reviewer-readable scenario evidence from local-only lab runtime evidence.

## Evidence Classification

| Evidence Area | Git Policy | Purpose |
|---|---|---|
| scenarios/*/evidence/generated/ | committed | Reviewer-readable placeholder evidence and stable scenario links |
| labs/*/evidence/generated/ | ignored | Local runtime execution evidence |
| labs/*/runtime-workspace/ | ignored | Temporary runtime workspace |
| a.txt | ignored | Local repository summary report |
| *.pem / *.key / id_* | ignored | Sensitive local execution material |

## Scenario Evidence

Scenario evidence is committed intentionally.

It provides stable reviewer-facing links for:

- scenario summaries
- execution evidence placeholders
- validation evidence placeholders
- artifact manifests
- artifact checksums

Scenario evidence does not represent live runtime execution.

## Lab Runtime Evidence

Lab runtime evidence is generated locally and excluded from Git.

It may include:

- raw command output
- generated runtime summaries
- runtime workspaces
- local IP addresses
- environment-specific paths
- temporary validation artifacts

This keeps the repository reviewer-readable and avoids committing environment-specific or sensitive data.

## Boundary

The repository commits implementation scripts, validation scripts, configuration examples, execution notes, and reviewer-facing summaries.

The repository does not commit raw local runtime output from lab execution.