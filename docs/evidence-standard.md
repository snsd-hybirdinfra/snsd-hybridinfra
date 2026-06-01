# Evidence Standard

## Purpose

This document defines the evidence structure used by scenario documents in this repository.

Evidence artifacts exist to show that each scenario has generated outputs, validation results, artifact manifests, and public-safe proof of completion.

This repository is a scenario-driven infrastructure operations portfolio. Evidence should support portfolio credibility without exposing raw logs, local machine details, credentials, failed debug traces, or internal-only production notes.

---

## Evidence Scope

Each scenario may contain evidence artifacts under its evidence directory.

Required structure:

    scenarios/<level>/<scenario-name>/evidence/
    ├─ generated/
    │  ├─ summary.md
    │  ├─ execution-evidence.md
    │  ├─ validation-evidence.md
    │  ├─ artifact-manifest.json
    │  └─ artifact-checksums.json
    └─ internal/
       ├─ raw-execution-log.txt
       ├─ validator-raw-result.json
       └─ debug-notes.md

The generated directory is public-safe.

The internal directory is local-only and must not be committed to the public repository.

---

## Public Evidence

Public evidence must be clean, summarized, and safe for external review.

Public evidence may include:

- scenario name
- scenario path
- generated artifact list
- operational poster existence status
- README existence status
- metadata existence status
- validation summary
- artifact manifest
- checksum records
- evidence generation timestamp
- public-safe completion status

Public evidence must not include:

- local absolute paths
- credentials
- secrets
- environment variables
- raw stack traces
- failed debug logs
- private notes
- sensitive screenshots
- internal-only command output

---

## Internal Evidence

Internal evidence is used for local debugging, production tracking, and raw execution inspection.

Internal evidence may include:

- raw execution logs
- raw validator output
- failed generation details
- command output
- local paths
- debug notes
- temporary troubleshooting records

Internal evidence must remain on the local PC unless explicitly cleaned and converted into a public-safe summary.

---

## Required Generated Evidence Files

Each scenario should include the following generated evidence files.

| File | Purpose | Public |
|---|---|---:|
| evidence/generated/summary.md | Human-readable evidence overview | Yes |
| evidence/generated/execution-evidence.md | Tool or generation execution summary | Yes |
| evidence/generated/validation-evidence.md | Validation result summary | Yes |
| evidence/generated/artifact-manifest.json | List of generated scenario artifacts | Yes |
| evidence/generated/artifact-checksums.json | Hash record for scenario artifacts | Yes |

---

## Evidence Summary

The summary.md file should provide a short human-readable overview.

Required content:

- scenario name
- lifecycle level
- evidence status
- generated artifacts
- validation status
- poster status
- README status
- metadata status

Example fields:

    Scenario: vpn-connectivity-monitoring
    Level: level-1-visibility
    Evidence Status: READY
    README: PRESENT
    Metadata: PRESENT
    Operational Poster: PRESENT
    Validation Evidence: PRESENT

---

## Execution Evidence

The execution-evidence.md file should summarize generated artifacts and execution status.

Recommended content:

- scenario path
- generated artifact list
- generation status
- timestamp
- notes about missing optional artifacts

Execution evidence must not include raw runtime logs.

---

## Validation Evidence

The validation-evidence.md file should summarize validation checks.

Recommended checks:

- metadata.yaml exists
- README.md exists
- operational-poster.svg exists
- operational-poster.png exists
- README references operational-poster.png
- README does not reference deprecated diagram artifacts
- generated evidence files exist
- module references follow naming convention
- adapter references follow naming convention
- lifecycle level matches parent directory

Validation evidence should be reviewer-readable.

---

## Artifact Manifest

The artifact-manifest.json file should list the scenario artifacts.

Required fields:

    scenario_name
    scenario_path
    lifecycle_level
    generated_at
    artifacts
    missing_artifacts
    status

Artifacts should use repository-relative paths.

---

## Artifact Checksums

The artifact-checksums.json file should record checksums for public scenario artifacts.

Recommended algorithm:

    SHA-256

Recommended checksum targets:

- metadata.yaml
- README.md
- diagrams/operational-poster.svg
- diagrams/operational-poster.png
- evidence/generated/summary.md
- evidence/generated/execution-evidence.md
- evidence/generated/validation-evidence.md
- evidence/generated/artifact-manifest.json

---

## Implementation Evidence

Implementation evidence may be added only when real lab work, screenshots, logs, or command outputs are available.

Implementation evidence should be separated from generated evidence.

Recommended local structure:

    evidence/implementation/
    ├─ screenshots/
    ├─ logs/
    ├─ command-output/
    └─ test-results/

Before committing implementation evidence, it must be reviewed for sensitive information.

---

## Evidence Completion Criteria

A scenario evidence set is considered complete when:

    evidence/generated/summary.md exists
    evidence/generated/execution-evidence.md exists
    evidence/generated/validation-evidence.md exists
    evidence/generated/artifact-manifest.json exists
    evidence/generated/artifact-checksums.json exists
    public evidence contains no local absolute paths
    public evidence contains no secrets or credentials
    public evidence references only repository-relative paths

---

## Final Principle

Evidence should make the portfolio more credible without exposing internal production tools, raw logs, debug traces, credentials, or local machine details.
