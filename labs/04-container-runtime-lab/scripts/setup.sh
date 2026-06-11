#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] container runtime setup started"

docker --version | tee runtime-workspace/logs/docker-version.log
docker compose version | tee runtime-workspace/logs/docker-compose-version.log

docker compose -f compose/docker-compose.yml up -d | tee runtime-workspace/logs/setup.log

docker compose -f compose/docker-compose.yml ps | tee evidence/generated/raw/container-setup-ps.log

echo "[INFO] container runtime setup completed"