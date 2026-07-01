#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] container runtime setup started"

docker --version > "${LOG_DIR}/docker-version.log" 2>&1 || true
docker compose version > "${LOG_DIR}/docker-compose-version.log" 2>&1 || true

cat > "${LOG_DIR}/setup.log" <<SETUP
SNSD_CONTAINER_RUNTIME_SETUP=ready
LAB=04-container-runtime-lab
RUNTIME=local-docker-compose-nginx
COMPOSE_FILE=compose/docker-compose.yml
ENDPOINT=http://localhost:18080
SETUP

cat > "${RAW_DIR}/container-runtime-setup.log" <<SETUP_RAW
SNSD_CONTAINER_RUNTIME_SETUP=ready
LAB=04-container-runtime-lab
RUNTIME=local-docker-compose-nginx
SETUP_RAW

echo "[INFO] container runtime setup completed"