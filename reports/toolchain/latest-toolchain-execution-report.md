# Toolchain Execution Report

Generated At: 2026-05-28T05:16:07.457158Z

## Summary

| Status | Count |
|---|---:|
| COMPLETED | 11 |
| WARNING | 1 |
| FAILED | 1 |
| BLOCKED | 3 |
| SKIPPED | 0 |

## Tool Results

| Tool | Status | Duration Seconds | Notes |
|---|---|---:|---|
| metadata-parser | COMPLETED | 0.697 | execution completed |
| relationship-mapper | COMPLETED | 2.167 | execution completed |
| scenario-generator | COMPLETED | 0.577 | execution completed |
| diagram-renderer | FAILED | 302.246 | diagram-renderer timeout exceeded. |
| scenario-relationship-validator | COMPLETED | 1.489 | execution completed |
| taxonomy-validator | COMPLETED | 1.558 | execution completed |
| topology-validator | COMPLETED | 1.572 | execution completed |
| capability-validator | COMPLETED | 1.434 | execution completed |
| tool-boundary-validator | COMPLETED | 2.108 | execution completed |
| tool-dependency-validator | COMPLETED | 1.409 | execution completed |
| lifecycle-semantic-validator | WARNING | 1.451 | execution completed with warnings |
| artifact-existence-validator | BLOCKED | 0 | blocked by failed dependencies: diagram-renderer |
| diagram-consistency-validator | BLOCKED | 0 | blocked by failed dependencies: diagram-renderer |
| governance-checker | COMPLETED | 1.544 | execution completed |
| lifecycle-chain-validator | COMPLETED | 1.438 | execution completed |
| scenario-governance-validator | BLOCKED | 0 | blocked by failed dependencies: diagram-consistency-validator, artifact-existence-validator |