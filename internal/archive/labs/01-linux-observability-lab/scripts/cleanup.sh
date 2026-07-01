#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"

echo "[INFO] linux observability cleanup started"

rm -rf "${RUNTIME_DIR}/logs" "${RUNTIME_DIR}/tmp"
mkdir -p "${RUNTIME_DIR}/logs" "${RUNTIME_DIR}/tmp"

echo "[INFO] linux observability cleanup completed"