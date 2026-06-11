#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_DIR="${LAB_DIR}/compose"

mkdir -p "${LAB_DIR}/evidence/generated/raw"
mkdir -p "${LAB_DIR}/evidence/generated/summary"

cd "${COMPOSE_DIR}"

docker compose stop primary-backend

sleep 5

curl -fsS http://127.0.0.1:19090/ > "${LAB_DIR}/evidence/generated/raw/failover-response.txt"

if grep -q "SNSD_FAILOVER_BACKEND=secondary" "${LAB_DIR}/evidence/generated/raw/failover-response.txt"; then
  STATUS="PASS"
else
  STATUS="FAIL"
fi

cat > "${LAB_DIR}/evidence/generated/summary/resilience-failover-runtime-summary.md" <<SUMMARY
# Resilience Failover Runtime Summary

Overall Status: ${STATUS}

## Failover Event

| Signal | Value |
|---|---|
| Primary backend stopped | yes |
| Traffic response captured | yes |
| Expected active backend after failure | secondary |
| Secondary backend response detected | ${STATUS} |

## Validation Marker

Expected marker:

SNSD_RESILIENCE_FAILOVER_SECONDARY

SUMMARY

if [ "${STATUS}" != "PASS" ]; then
  echo "[FAIL] failover validation failed"
  exit 1
fi

echo "[OK] failover shifted traffic to secondary backend"