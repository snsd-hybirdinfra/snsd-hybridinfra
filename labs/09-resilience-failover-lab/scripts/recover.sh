#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_DIR="${LAB_DIR}/compose"

mkdir -p "${LAB_DIR}/evidence/generated/raw"

cd "${COMPOSE_DIR}"

docker compose start primary-backend

sleep 3

curl -fsS http://127.0.0.1:19090/ > "${LAB_DIR}/evidence/generated/raw/recovery-response.txt"

echo "[OK] primary backend restarted and recovery response captured"