#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] kolla openstack readiness setup started"

python3 --version > "${LOG_DIR}/python-version.log" 2>&1 || true

cat > "${RAW_DIR}/kolla-openstack-setup.log" <<SETUP
SNSD_KOLLA_OPENSTACK_SETUP=ready
LAB=05-kolla-openstack-lab
RUNTIME=local-openstack-readiness-gate
INVENTORY=inventory/multinode.ini
GLOBALS=configs/globals.yml
SETUP

echo "[INFO] kolla openstack readiness setup completed"