#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/monitoring-stack-runtime-summary.md"

CLEANUP_AFTER="false"

if [ "${1:-}" = "--cleanup" ]; then
  CLEANUP_AFTER="true"
fi

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

echo "[INFO] SNSD monitoring stack runtime orchestration started"
echo "[INFO] lab_dir=${LAB_DIR}"

echo "[STEP] normalize scripts"
sed -i 's/\r$//' "${LAB_DIR}"/scripts/*.sh
chmod +x "${LAB_DIR}"/scripts/*.sh

echo "[STEP] remove stale 06 runtime containers"
docker rm -f snsd-prometheus snsd-grafana 2>/dev/null || true
docker network rm snsd-monitoring-stack-lab_default snsd-monitoring-net 2>/dev/null || true

echo "[STEP] setup monitoring runtime"
bash "${LAB_DIR}/scripts/setup.sh"

echo "[STEP] wait for runtime readiness"
sleep 15

echo "[STEP] validate monitoring runtime"
bash "${LAB_DIR}/scripts/validate.sh"

cat >> "${SUMMARY}" <<SUMMARY_APPEND

## End-to-End Orchestration

| Signal | Status |
|---|---|
| Monitoring stack setup | PASS |
| Prometheus alert rule validation | PASS |
| End-to-end orchestration | PASS |

SUMMARY_APPEND

echo "[SUMMARY]"
cat "${SUMMARY}"

if [ "${CLEANUP_AFTER}" = "true" ]; then
  echo "[STEP] cleanup runtime"
  bash "${LAB_DIR}/scripts/cleanup.sh"
else
  echo "[INFO] runtime left running for review"
  echo "[INFO] cleanup command: bash scripts/cleanup.sh"
fi

echo "[OK] monitoring stack runtime orchestration completed"
echo "[INFO] running scenario signal validation"
bash "${SCRIPT_DIR}/validate-scenario-signals.sh"

echo "[OK] scenario signal validation completed"

