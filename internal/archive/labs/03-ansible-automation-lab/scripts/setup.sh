#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace/ansible-runtime"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

mkdir -p "${RAW_DIR}" "${RUNTIME_DIR}" "${LOG_DIR}"

echo "[INFO] ansible automation setup started"

if ansible --version > "${RAW_DIR}/ansible-setup.log" 2>&1; then
  echo "[INFO] ansible CLI available"
else
  echo "[FAIL] ansible CLI is not available"
  cat "${RAW_DIR}/ansible-setup.log" || true
  exit 1
fi

cat > "${RUNTIME_DIR}/setup-boundary.txt" <<SETUP
SNSD_ANSIBLE_SETUP_BOUNDARY=ready
LAB=03-ansible-automation-lab
RUNTIME=local-ansible
SETUP

echo "[INFO] ansible automation setup completed"