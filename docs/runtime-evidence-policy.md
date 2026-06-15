# Runtime Evidence Policy

This document defines how evidence is handled in the repository.

## Policy summary

- Scenario evidence is committed when it is reviewer-readable and stable.
- Lab runtime evidence is generated locally and intentionally excluded from Git.
- Sensitive or environment-specific artifacts are not committed.

## Evidence boundary

| Area | Git policy | Purpose |
|---|---|---|
| scenarios/*/evidence/generated/ | committed | Stable reviewer-facing evidence placeholders |
| labs/*/evidence/generated/ | ignored | Local runtime execution evidence |
| labs/*/runtime-workspace/ | ignored | Temporary runtime workspace |
| a.txt | ignored | Local repository summary output |
| *.pem, *.key, id_* | ignored | Sensitive local execution material |

## Why this matters

This keeps the repository reviewable while preserving local execution flexibility and avoiding the commit of environment-specific data.