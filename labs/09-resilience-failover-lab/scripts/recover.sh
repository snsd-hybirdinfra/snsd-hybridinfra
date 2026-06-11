#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_DIR="${LAB_DIR}/compose"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/resilience-failover-runtime-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

cd "${COMPOSE_DIR}"

docker compose -p snsd-resilience-failover-lab start primary-backend

sleep 5

curl -fsS http://127.0.0.1:19090/ > "${RAW_DIR}/recovery-response.txt"

if grep -q "SNSD_FAILOVER_BACKEND=primary" "${RAW_DIR}/recovery-response.txt"; then
  RECOVERY_STATUS="PASS"
else
  RECOVERY_STATUS="CHECK"
fi

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## Recovery Event

| Signal | Value |
|---|---|
| Primary backend restarted | yes |
| Recovery response captured | yes |
| Expected backend after recovery | primary |
| Primary backend response detected | ${RECOVERY_STATUS} |

SUMMARY_APPEND

if [ "${RECOVERY_STATUS}" != "PASS" ]; then
  echo "[CHECK] primary backend restarted, but response did not return to primary"
  exit 1
fi

echo "[OK] primary backend restarted and recovery response returned to primary"