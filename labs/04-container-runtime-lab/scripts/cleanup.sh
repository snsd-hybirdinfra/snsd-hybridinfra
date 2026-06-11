#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw

echo "[INFO] container runtime cleanup started"

docker compose -f compose/docker-compose.yml down -v \
  | tee runtime-workspace/logs/cleanup.log

cp runtime-workspace/logs/cleanup.log evidence/generated/raw/container-runtime-cleanup.log

echo "[INFO] container runtime cleanup completed"