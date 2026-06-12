#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/backup-recovery-runtime-summary.md"

CLEANUP_AFTER="false"

if [ "${1:-}" = "--cleanup" ]; then
  CLEANUP_AFTER="true"
fi

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LAB_DIR}/runtime-workspace/logs"

echo "[INFO] SNSD backup recovery runtime orchestration started"
echo "[INFO] lab_dir=${LAB_DIR}"

echo "[STEP] normalize scripts"
sed -i 's/\r$//' "${LAB_DIR}"/scripts/*.sh
chmod +x "${LAB_DIR}"/scripts/*.sh

echo "[STEP] reset runtime workspace"
rm -rf "${LAB_DIR}/runtime-workspace/data" \
       "${LAB_DIR}/runtime-workspace/backup" \
       "${LAB_DIR}/runtime-workspace/restore"

mkdir -p "${LAB_DIR}/runtime-workspace/data" \
         "${LAB_DIR}/runtime-workspace/backup" \
         "${LAB_DIR}/runtime-workspace/restore" \
         "${LAB_DIR}/runtime-workspace/logs"

echo "[STEP] setup backup recovery dataset"
bash "${LAB_DIR}/scripts/setup.sh"

echo "[STEP] create backup artifact"
bash "${LAB_DIR}/scripts/backup.sh"

echo "[STEP] execute restore workflow"
bash "${LAB_DIR}/scripts/restore.sh"

echo "[STEP] validate backup recovery integrity"
bash "${LAB_DIR}/scripts/validate.sh"

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## End-to-End Orchestration

| Signal | Status |
|---|---|
| Backup recovery setup | PASS |
| Backup artifact creation | PASS |
| Restore workflow execution | PASS |
| Integrity validation | PASS |
| End-to-end orchestration | PASS |

SUMMARY_APPEND

echo "[SUMMARY]"
cat "${SUMMARY}"

if [ "${CLEANUP_AFTER}" = "true" ]; then
  echo "[STEP] cleanup runtime"
  bash "${LAB_DIR}/scripts/cleanup.sh"
else
  echo "[INFO] runtime left available for review"
  echo "[INFO] cleanup command: bash scripts/cleanup.sh"
fi

echo "[OK] backup recovery runtime orchestration completed"