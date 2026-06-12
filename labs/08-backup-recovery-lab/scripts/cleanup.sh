#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"

echo "[INFO] backup recovery cleanup started"

rm -rf "${RUNTIME_DIR}/data" \
       "${RUNTIME_DIR}/backup" \
       "${RUNTIME_DIR}/restore" \
       "${RUNTIME_DIR}/logs"

mkdir -p "${RUNTIME_DIR}/data" \
         "${RUNTIME_DIR}/backup" \
         "${RUNTIME_DIR}/restore" \
         "${RUNTIME_DIR}/logs"

echo "[INFO] backup recovery cleanup completed"