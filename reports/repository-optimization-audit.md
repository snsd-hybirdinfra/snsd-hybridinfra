# Repository Optimization Audit

## 1. Purpose

This report identifies optimization and deduplication candidates before any destructive cleanup is performed.

## 2. Summary

| Signal | Value |
|---|---:|
| Files scanned | 2675 |
| Duplicate hash groups | 5 |
| Large files over 512 KiB | 0 |
| README quality anomalies | 4 |
| Status language anomalies | 1 |
| Domain fragmentation groups | 2 |

## 3. Scenario Evidence Artifact Counts

| Artifact | Count | Expected | Status |
|---|---:|---:|---|
| scenario-test-evidence.md | 150 | 150 | PASS |
| scenario-evidence-matrix.tsv | 150 | 150 | PASS |
| scenario-validation-result.md | 150 | 150 | PASS |

## 4. README Quality Findings

- CHECK: README.md quality status row for root_readme_missing_links is malformed
- CHECK: README.md quality status row for root_readme_missing_terms is malformed
- CHECK: README.md does not expose Phase 5 Scenario Evidence Report in reviewer quick start
- CHECK: README.md does not expose Scenario Test Evidence Index in reviewer quick start

## 5. Status Language Findings

- CHECK: labs/README.md still emphasizes documentation-ready status while root README reports runtime PASS

## 6. Domain Fragmentation Candidates

- REVIEW: Database: Database, Database / Replication, Database / Query
- REVIEW: Network: Network / Routing, Network / VPN, Network / WAN

## 7. Duplicate Hash Groups

### 3cc4914ebeb97d1b1a0aaa02ccc358244d37a9dc8acc1a3f940a6ba902e44d8e

- labs/09-resilience-failover-lab/evidence/generated/raw/initial-primary-response.txt (100 bytes)
- labs/09-resilience-failover-lab/evidence/generated/raw/recovery-response.txt (100 bytes)

### 4fbe7ac339f25cf929ac39a599b15a33dfea62d9284bac94b4938d2d4bc8de9c

- labs/04-container-runtime-lab/configs/index.html (223 bytes)
- labs/04-container-runtime-lab/evidence/generated/raw/container-web-endpoint.html (223 bytes)

### 62e72a95b3a5b3ba5bb9057f24f10447a7bbb31ae4125e6f57956c2760a42fe1

- labs/08-backup-recovery-lab/evidence/generated/raw/restore-digest.sha256 (254 bytes)
- labs/08-backup-recovery-lab/evidence/generated/raw/source-digest.sha256 (254 bytes)

### 94db4cd26578beb18ee24edc6910c9d139daeae16d35b802465f211941ad66ca

- labs/03-ansible-automation-lab/evidence/generated/raw/ansible-setup.log (849 bytes)
- labs/03-ansible-automation-lab/evidence/generated/raw/ansible-version.txt (849 bytes)

### e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

- internal/rebuild-roadmap.md (0 bytes)
- labs/04-container-runtime-lab/evidence/generated/raw/container-runtime-cleanup.log (0 bytes)


## 8. Large Files

- PASS: no large files over threshold detected

## 9. Generated Duplicate Candidates

- PASS: no generated duplicate candidates detected

## 10. Cleanup Policy

Do not delete scenario evidence artifacts automatically.
Do not delete lab evidence boundary notes automatically.
Only remove duplicates after confirming they are not reviewer-facing evidence, generated indexes, or validation summaries.
