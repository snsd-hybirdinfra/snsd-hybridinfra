#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"

echo "[INFO] kolla openstack cleanup started"

rm -rf "${RUNTIME_DIR}/logs"
mkdir -p "${RUNTIME_DIR}/logs"

echo "[INFO] kolla openstack cleanup completed"