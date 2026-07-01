#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUMMARY="${LAB_DIR}/evidence/generated/summary/kolla-openstack-runtime-summary.md"

CLEANUP_AFTER="false"

if [ "${1:-}" = "--cleanup" ]; then
  CLEANUP_AFTER="true"
fi

echo "[INFO] SNSD kolla openstack readiness runtime orchestration started"
echo "[INFO] lab_dir=${LAB_DIR}"

echo "[STEP] normalize scripts"
sed -i 's/\r$//' "${LAB_DIR}"/scripts/*.sh
chmod +x "${LAB_DIR}"/scripts/*.sh

echo "[STEP] setup openstack readiness workspace"
bash "${LAB_DIR}/scripts/setup.sh"

echo "[STEP] validate kolla deployment readiness"
bash "${LAB_DIR}/scripts/validate.sh"

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## End-to-End Orchestration

| Signal | Status |
|---|---|
| Kolla readiness setup | PASS |
| Deployment readiness validation | PASS |
| Readiness report generation | PASS |
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

echo "[OK] kolla openstack readiness runtime orchestration completed"
echo "[INFO] running openstack readiness scenario signal validation"
bash "${SCRIPT_DIR}/validate-openstack-readiness-signals.sh"

echo "[OK] openstack readiness scenario signal validation completed"
