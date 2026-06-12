#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] governance reporting setup started"

python3 --version > "${LOG_DIR}/python-version.log" 2>&1 || true

cat > "${RAW_DIR}/governance-reporting-setup.log" <<SETUP
SNSD_GOVERNANCE_REPORTING_SETUP=ready
LAB=10-governance-reporting-lab
RUNTIME=local-governance-evidence-aggregation
SETUP

echo "[INFO] governance reporting setup completed"