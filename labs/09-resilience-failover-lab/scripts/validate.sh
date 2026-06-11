#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/resilience-failover-runtime-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

ENTRYPOINT_STATUS="FAIL"
PRIMARY_CONTAINER_STATE="stopped"
SECONDARY_STATUS="FAIL"
FAILOVER_STATUS="FAIL"
RECOVERY_STATUS="not-run"

if curl -fsS http://127.0.0.1:19090/health | grep -q "failover-entrypoint-ok"; then
  ENTRYPOINT_STATUS="PASS"
fi

if docker ps --format '{{.Names}}' | grep -q "snsd-primary-backend"; then
  PRIMARY_CONTAINER_STATE="running"
fi

if docker ps --format '{{.Names}}' | grep -q "snsd-secondary-backend"; then
  SECONDARY_STATUS="PASS"
fi

if [ -f "${RAW_DIR}/failover-response.txt" ] && grep -q "SNSD_FAILOVER_BACKEND=secondary" "${RAW_DIR}/failover-response.txt"; then
  FAILOVER_STATUS="PASS"
fi

if [ -f "${RAW_DIR}/recovery-response.txt" ]; then
  if grep -q "SNSD_FAILOVER_BACKEND=primary" "${RAW_DIR}/recovery-response.txt"; then
    RECOVERY_STATUS="PASS"
  else
    RECOVERY_STATUS="CHECK"
  fi
fi

if [ "${ENTRYPOINT_STATUS}" = "PASS" ] && \
   [ "${SECONDARY_STATUS}" = "PASS" ] && \
   [ "${FAILOVER_STATUS}" = "PASS" ] && \
   { [ "${RECOVERY_STATUS}" = "PASS" ] || [ "${RECOVERY_STATUS}" = "not-run" ]; }; then
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
| Primary backend container state | ${PRIMARY_CONTAINER_STATE} |
| Secondary backend container running | ${SECONDARY_STATUS} |
| Traffic shifted to secondary after primary failure | ${FAILOVER_STATUS} |
| Traffic returned to primary after recovery | ${RECOVERY_STATUS} |

## Runtime Boundary

This lab validates a local traffic failover runtime boundary using NGINX upstream failover behavior.

Generated runtime evidence remains local-only.

## Interpretation

During failover validation, the primary backend is intentionally stopped.

A stopped primary backend during the failover phase is expected behavior, not a runtime failure.

SUMMARY

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  exit 1
fi