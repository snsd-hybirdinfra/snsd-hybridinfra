# Document Visibility Policy

## Purpose

This policy defines which repository assets are intended for public GitHub visibility and which assets must remain internal-only on the local PC.

This repository is positioned as a scenario-driven infrastructure operations portfolio. The public repository should contain final portfolio artifacts only. Internal production tools, drafts, raw logs, temporary outputs, and debugging materials must remain outside the public repository.

---

## Public GitHub Assets

The following assets are allowed to be included in the public GitHub repository.

### Repository Entry Documents

- `README.md`
- `docs/**`
- `reviews/**`

### Portfolio Artifacts

- `modules/**/README.md`
- `adapters/**/README.md`
- `scenarios/**/README.md`
- `scenarios/**/metadata.yaml`
- `scenarios/**/diagrams/operational-poster.svg`
- `scenarios/**/diagrams/operational-poster.png`

### Public Evidence Summaries

- `scenarios/**/evidence/generated/summary.md`
- `scenarios/**/evidence/generated/execution-evidence.md`
- `scenarios/**/evidence/generated/validation-evidence.md`
- `scenarios/**/evidence/generated/artifact-manifest.json`
- `scenarios/**/evidence/generated/artifact-checksums.json`

### Public Summary Reports

- `reports/toolchain/*.md`
- `reports/toolchain/*summary*.json`
- `reports/validators/*.md`

---

## Internal PC-only Assets

The following assets must remain internal-only and should not be committed to the public GitHub repository.

### Internal Planning Documents

- `internal/**`
- `../internal/**`

### Internal Production Tools

- `tools/**`

### Runtime and Temporary Workspaces

- `runtime-workspace/**`
- `**/runtime-workspace/**`
- `**/tmp/**`
- `**/temp/**`
- `**/debug/**`
- `**/outputs/**`

### Raw Logs and Debug Artifacts

- `*.log`
- `raw-execution-log.txt`
- `validator-raw-result.json`
- `debug-notes.md`
- `reports/raw/**`
- `reports/validators/findings/**`

### Local Python Environments and Cache

- `**/venv/**`
- `**/.venv/**`
- `**/__pycache__/**`
- `*.pyc`
- `*.pyo`
- `*.pyd`

### Local Environment Files

- `.env`
- `.env.*`
- `*.local`

---

## Evidence Visibility Rule

Evidence artifacts are divided into public summaries and internal raw evidence.

### Public Evidence

Public evidence must be cleaned, summarized, and safe for external review.

Examples:

- generated artifact manifest
- validation summary
- generated evidence summary
- poster existence proof
- scenario artifact checklist

### Internal Evidence

Internal evidence may contain raw logs, debugging details, failed runs, local paths, command outputs, screenshots, or sensitive environment details.

Internal evidence must not be committed without review.

---

## Tooling Visibility Rule

Automation tools are treated as internal production utilities.

The public repository may mention that internal automation was used to maintain consistency, but tool source code, temporary outputs, runtime workspaces, virtual environments, and debugging artifacts should remain local unless explicitly selected for public release later.

---

## Final Principle

The public GitHub repository should present the final scenario-driven infrastructure operations portfolio.

The local PC workspace may contain production tools, drafts, raw evidence, intermediate files, and experimental materials.
