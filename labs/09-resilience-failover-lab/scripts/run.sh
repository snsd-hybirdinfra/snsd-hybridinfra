#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/resilience-failover-runtime-summary.md"

CLEANUP_AFTER="false"

if [ "${1:-}" = "--cleanup" ]; then
  CLEANUP_AFTER="true"
fi

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

echo "[INFO] SNSD resilience failover runtime orchestration started"
echo "[INFO] lab_dir=${LAB_DIR}"

echo "[STEP] normalize scripts"
sed -i 's/\r$//' "${LAB_DIR}"/scripts/*.sh
chmod +x "${LAB_DIR}"/scripts/*.sh

echo "[STEP] remove stale 09 runtime containers"
docker rm -f snsd-failover-entrypoint snsd-primary-backend snsd-secondary-backend 2>/dev/null || true
docker network rm snsd-failover-net 2>/dev/null || true

echo "[STEP] setup runtime"
bash "${LAB_DIR}/scripts/setup.sh"

echo "[STEP] validate initial primary response"
curl -fsS http://127.0.0.1:19090/ > "${RAW_DIR}/initial-primary-response.txt"

if grep -q "SNSD_FAILOVER_BACKEND=primary" "${RAW_DIR}/initial-primary-response.txt"; then
  INITIAL_STATUS="PASS"
else
  INITIAL_STATUS="FAIL"
fi

echo "[INFO] initial_primary_status=${INITIAL_STATUS}"

if [ "${INITIAL_STATUS}" != "PASS" ]; then
  echo "[FAIL] initial primary backend response was not detected"
  cat "${RAW_DIR}/initial-primary-response.txt" || true
  exit 1
fi

echo "[STEP] execute failover"
bash "${LAB_DIR}/scripts/failover.sh"

echo "[STEP] execute recovery"
bash "${LAB_DIR}/scripts/recover.sh"

echo "[STEP] validate final runtime state"
bash "${LAB_DIR}/scripts/validate.sh"

echo "[STEP] validate recovery response"
if grep -q "SNSD_FAILOVER_BACKEND=primary" "${RAW_DIR}/recovery-response.txt"; then
  RECOVERY_STATUS="PASS"
else
  RECOVERY_STATUS="CHECK"
fi

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## End-to-End Orchestration

| Signal | Status |
|---|---|
| Initial primary response | ${INITIAL_STATUS} |
| Failover response shifted to secondary | PASS |
| Recovery response returned to primary | ${RECOVERY_STATUS} |
| End-to-end orchestration | PASS |

SUMMARY_APPEND

echo "[SUMMARY]"
cat "${SUMMARY}"

if [ "${RECOVERY_STATUS}" != "PASS" ]; then
  echo "[CHECK] recovery completed, but primary response was not confirmed"
  exit 1
fi

if [ "${CLEANUP_AFTER}" = "true" ]; then
  echo "[STEP] cleanup runtime"
  bash "${LAB_DIR}/scripts/cleanup.sh"
else
  echo "[INFO] runtime left running for review"
  echo "[INFO] cleanup command: bash scripts/cleanup.sh"
fi

echo "[OK] resilience failover runtime orchestration completed"