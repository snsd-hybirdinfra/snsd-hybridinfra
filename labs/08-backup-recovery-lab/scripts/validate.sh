#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"

DATA_DIR="${LAB_DIR}/runtime-workspace/data"
BACKUP_DIR="${LAB_DIR}/runtime-workspace/backup"
RESTORE_DIR="${LAB_DIR}/runtime-workspace/restore"

BACKUP_ARCHIVE="${BACKUP_DIR}/snsd-backup-recovery-lab.tar.gz"

SOURCE_DIGEST="${RAW_DIR}/source-digest.sha256"
RESTORE_DIGEST="${RAW_DIR}/restore-digest.sha256"
VALIDATE_LOG="${RAW_DIR}/backup-recovery-validate.log"
MARKER_LOG="${RAW_DIR}/restore-marker-check.log"

SUMMARY="${SUMMARY_DIR}/backup-recovery-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/backup-recovery-execution-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

SOURCE_DATASET="FAIL"
BACKUP_ARTIFACT="FAIL"
RESTORE_COMPLETED="FAIL"
CHECKSUM_INTEGRITY="FAIL"
MARKER_VALIDATION="FAIL"

echo "[INFO] backup recovery validation started"

SOURCE_COUNT="$(find "${DATA_DIR}" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"
RESTORE_COUNT="$(find "${RESTORE_DIR}" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"

if [ "${SOURCE_COUNT}" -gt 0 ]; then
  SOURCE_DATASET="PASS"
fi

if [ -f "${BACKUP_ARCHIVE}" ] && [ -s "${BACKUP_ARCHIVE}" ]; then
  BACKUP_ARTIFACT="PASS"
fi

if [ "${RESTORE_COUNT}" -gt 0 ]; then
  RESTORE_COMPLETED="PASS"
fi

(
  cd "${DATA_DIR}"
  find . -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum | sed 's#  ./#  #'
) > "${SOURCE_DIGEST}"

(
  cd "${RESTORE_DIR}"
  find . -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum | sed 's#  ./#  #'
) > "${RESTORE_DIGEST}"

if cmp -s "${SOURCE_DIGEST}" "${RESTORE_DIGEST}"; then
  CHECKSUM_INTEGRITY="PASS"
fi

if grep -R "SNSD_BACKUP_RECOVERY_VALIDATION_MARKER" "${RESTORE_DIR}" > "${MARKER_LOG}" 2>/dev/null; then
  MARKER_VALIDATION="PASS"
fi

cat > "${VALIDATE_LOG}" <<LOG
# Backup Recovery Validation Raw Evidence

source_dir=${DATA_DIR}
backup_archive=${BACKUP_ARCHIVE}
restore_dir=${RESTORE_DIR}

source_file_count=${SOURCE_COUNT}
restore_file_count=${RESTORE_COUNT}

source_dataset=${SOURCE_DATASET}
backup_artifact=${BACKUP_ARTIFACT}
restore_completed=${RESTORE_COMPLETED}
checksum_integrity=${CHECKSUM_INTEGRITY}
marker_validation=${MARKER_VALIDATION}

## Source Digest

$(cat "${SOURCE_DIGEST}")

## Restore Digest

$(cat "${RESTORE_DIGEST}")

## Marker Check

$(cat "${MARKER_LOG}" 2>/dev/null || true)
LOG

if [ "${SOURCE_DATASET}" = "PASS" ] && \
   [ "${BACKUP_ARTIFACT}" = "PASS" ] && \
   [ "${RESTORE_COMPLETED}" = "PASS" ] && \
   [ "${CHECKSUM_INTEGRITY}" = "PASS" ] && \
   [ "${MARKER_VALIDATION}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Backup Recovery Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Source dataset created | ${SOURCE_DATASET} |
| Backup artifact created | ${BACKUP_ARTIFACT} |
| Restore workflow completed | ${RESTORE_COMPLETED} |
| Checksum integrity verified | ${CHECKSUM_INTEGRITY} |
| Restore marker validated | ${MARKER_VALIDATION} |

## Runtime Boundary

This lab validates local backup artifact creation, restore workflow execution, and checksum-based recovery integrity.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| Source digest | evidence/generated/raw/source-digest.sha256 |
| Restore digest | evidence/generated/raw/restore-digest.sha256 |
| Marker check | evidence/generated/raw/restore-marker-check.log |
| Validation log | evidence/generated/raw/backup-recovery-validate.log |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] backup recovery validation did not reach PASS"
  cat "${VALIDATE_LOG}" || true
  exit 1
fi

echo "[INFO] backup recovery validation completed"