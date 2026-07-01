#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] monitoring stack cleanup started"

cd "$(dirname "$0")/.."

docker compose -p snsd-monitoring-stack-lab -f compose/docker-compose.yml down

echo "[INFO] monitoring stack cleanup completed"