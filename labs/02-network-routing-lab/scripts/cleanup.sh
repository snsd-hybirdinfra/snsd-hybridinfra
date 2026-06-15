#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"

echo "[INFO] network routing cleanup started"

rm -rf "${RUNTIME_DIR}/data" "${RUNTIME_DIR}/logs"
mkdir -p "${RUNTIME_DIR}/data" "${RUNTIME_DIR}/logs"

echo "[INFO] network routing cleanup completed"