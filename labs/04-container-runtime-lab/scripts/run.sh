#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUMMARY="${LAB_DIR}/evidence/generated/summary/container-runtime-summary.md"

CLEANUP_AFTER="false"

if [ "${1:-}" = "--cleanup" ]; then
  CLEANUP_AFTER="true"
fi

echo "[INFO] SNSD container runtime orchestration started"
echo "[INFO] lab_dir=${LAB_DIR}"

echo "[STEP] normalize scripts"
sed -i 's/\r$//' "${LAB_DIR}"/scripts/*.sh
chmod +x "${LAB_DIR}"/scripts/*.sh

echo "[STEP] setup container runtime workspace"
bash "${LAB_DIR}/scripts/setup.sh"

echo "[STEP] validate container runtime"
bash "${LAB_DIR}/scripts/validate.sh"

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## End-to-End Orchestration

| Signal | Status |
|---|---|
| Container runtime setup | PASS |
| Container runtime validation | PASS |
| Runtime report generation | PASS |
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

echo "[OK] container runtime orchestration completed"