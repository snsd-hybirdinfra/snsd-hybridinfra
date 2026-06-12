#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/ansible-automation-runtime-summary.md"

CLEANUP_AFTER="false"

if [ "${1:-}" = "--cleanup" ]; then
  CLEANUP_AFTER="true"
fi

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LAB_DIR}/runtime-workspace/logs"

echo "[INFO] SNSD Ansible automation runtime orchestration started"
echo "[INFO] lab_dir=${LAB_DIR}"

echo "[STEP] normalize scripts"
sed -i 's/\r$//' "${LAB_DIR}"/scripts/*.sh
chmod +x "${LAB_DIR}"/scripts/*.sh

echo "[STEP] remove stale Phase 2 runtime marker"
rm -f "${LAB_DIR}/runtime-workspace/ansible-runtime/phase2-idempotency-marker.txt"

echo "[STEP] setup Ansible runtime"
bash "${LAB_DIR}/scripts/setup.sh"

echo "[STEP] validate idempotency and rollback"
bash "${LAB_DIR}/scripts/validate.sh"

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## End-to-End Orchestration

| Signal | Status |
|---|---|
| Ansible runtime setup | PASS |
| Idempotency validation | PASS |
| Rollback validation | PASS |
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

echo "[OK] Ansible automation runtime orchestration completed"