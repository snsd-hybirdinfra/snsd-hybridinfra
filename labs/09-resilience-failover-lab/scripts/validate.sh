#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/resilience-failover-runtime-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

ENTRYPOINT_STATUS="FAIL"
PRIMARY_STATUS="FAIL"
SECONDARY_STATUS="FAIL"
FAILOVER_STATUS="FAIL"

if curl -fsS http://127.0.0.1:19090/health | grep -q "failover-entrypoint-ok"; then
  ENTRYPOINT_STATUS="PASS"
fi

docker ps --format '{{.Names}}' | grep -q "snsd-primary-backend" && PRIMARY_STATUS="PASS" || true
docker ps --format '{{.Names}}' | grep -q "snsd-secondary-backend" && SECONDARY_STATUS="PASS" || true

if [ -f "${RAW_DIR}/failover-response.txt" ] && grep -q "SNSD_FAILOVER_BACKEND=secondary" "${RAW_DIR}/failover-response.txt"; then
  FAILOVER_STATUS="PASS"
fi

if [ "${ENTRYPOINT_STATUS}" = "PASS" ] && [ "${SECONDARY_STATUS}" = "PASS" ] && [ "${FAILOVER_STATUS}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Resilience Failover Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| NGINX failover entrypoint health | ${ENTRYPOINT_STATUS} |
| Primary backend container running | ${PRIMARY_STATUS} |
| Secondary backend container running | ${SECONDARY_STATUS} |
| Traffic shifted to secondary after primary failure | ${FAILOVER_STATUS} |

## Runtime Boundary

This lab validates a local traffic failover runtime boundary using NGINX upstream failover behavior.

Generated runtime evidence remains local-only.

SUMMARY

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  exit 1
fi