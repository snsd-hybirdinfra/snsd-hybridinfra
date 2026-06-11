#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_DIR="${LAB_DIR}/compose"

mkdir -p "${LAB_DIR}/evidence/generated/raw"
mkdir -p "${LAB_DIR}/evidence/generated/summary"

cd "${COMPOSE_DIR}"

docker compose up -d

sleep 3

docker compose ps > "${LAB_DIR}/evidence/generated/raw/failover-compose-ps.txt"

cat > "${LAB_DIR}/evidence/generated/summary/resilience-failover-runtime-summary.md" <<'SUMMARY'
# Resilience Failover Runtime Summary

Setup Status: PASS

Runtime Model:

- NGINX failover entrypoint
- primary backend
- secondary backend
- local traffic validation boundary

SUMMARY

echo "[OK] resilience failover runtime started"