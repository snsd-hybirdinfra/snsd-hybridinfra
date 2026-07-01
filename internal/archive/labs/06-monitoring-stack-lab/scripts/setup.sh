#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] monitoring stack setup started"

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs

docker compose -p snsd-monitoring-stack-lab -f compose/docker-compose.yml up -d | tee runtime-workspace/logs/setup.log

echo "[INFO] monitoring stack setup completed"