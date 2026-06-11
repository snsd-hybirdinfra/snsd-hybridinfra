#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_DIR="${LAB_DIR}/compose"

cd "${COMPOSE_DIR}"

docker compose -p snsd-resilience-failover-lab down -v

echo "[OK] resilience failover runtime cleaned up"