#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_FILE="${LAB_DIR}/compose/docker-compose.yml"
PROJECT_NAME="snsd-container-runtime-lab"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"

echo "[INFO] container runtime cleanup started"

docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" down > "${RUNTIME_DIR}/logs/cleanup.log" 2>&1 || true

rm -rf "${RUNTIME_DIR}/logs"
mkdir -p "${RUNTIME_DIR}/logs"

echo "[INFO] container runtime cleanup completed"