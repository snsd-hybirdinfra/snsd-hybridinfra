#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace/ansible-runtime"

echo "[INFO] ansible automation cleanup started"

rm -f "${RUNTIME_DIR}/phase2-idempotency-marker.txt"
rm -f "${RUNTIME_DIR}/setup-boundary.txt"

echo "[INFO] ansible automation cleanup completed"