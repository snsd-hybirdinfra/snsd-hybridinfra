#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] monitoring stack cleanup started"

cd "$(dirname "$0")/.."

docker compose -f compose/docker-compose.yml down

echo "[INFO] monitoring stack cleanup completed"