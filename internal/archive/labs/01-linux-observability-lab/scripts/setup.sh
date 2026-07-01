#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
PROCESSED_DIR="${LAB_DIR}/evidence/generated/processed"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"
TMP_DIR="${RUNTIME_DIR}/tmp"

mkdir -p "${RAW_DIR}" "${PROCESSED_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}" "${TMP_DIR}"

echo "[INFO] linux observability setup started"

cat > "${LOG_DIR}/setup.log" <<SETUP
SNSD_LINUX_OBSERVABILITY_SETUP=ready
LAB=01-linux-observability-lab
RUNTIME=local-linux-observability-baseline
RAW_DIR=${RAW_DIR}
PROCESSED_DIR=${PROCESSED_DIR}
SUMMARY_DIR=${SUMMARY_DIR}
SETUP

cp "${LOG_DIR}/setup.log" "${RAW_DIR}/linux-observability-setup.log"

echo "[INFO] linux observability setup completed"