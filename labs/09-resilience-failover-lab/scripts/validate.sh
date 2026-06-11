#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/failover-policy.env

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/resilience-failover-validate.log"
SUMMARY="evidence/generated/summary/resilience-failover-execution-summary.md"

ACTIVE_STATUS="CHECK"
PRIMARY_FAILURE_STATUS="CHECK"
SECONDARY_HEALTH_STATUS="CHECK"
DECISION_STATUS="CHECK"
TRAFFIC_SHIFT_STATUS="CHECK"
RECOVERY_STATUS="CHECK"
MARKER_STATUS="CHECK"
OVERALL_STATUS="CHECK"

ACTIVE_ENDPOINT="$(cat "$ACTIVE_ENDPOINT_FILE" 2>/dev/null || echo unknown)"
PRIMARY_HEALTH="$(cat "$PRIMARY_HEALTH_FILE" 2>/dev/null || echo unknown)"
SECONDARY_HEALTH="$(cat "$SECONDARY_HEALTH_FILE" 2>/dev/null || echo unknown)"

: > "$RAW_LOG"

echo "[INFO] resilience failover validation started"

{
  echo "# Resilience Failover Validation"
  echo
  echo "active_endpoint=$ACTIVE_ENDPOINT"
  echo "primary_health=$PRIMARY_HEALTH"
  echo "secondary_health=$SECONDARY_HEALTH"
  echo
  echo "## Failover Decision Log"
  cat "$FAILOVER_DECISION_LOG"
  echo
  echo "## Traffic Shift Log"
  cat "$TRAFFIC_LOG"
} | tee -a "$RAW_LOG"

if [ "$ACTIVE_ENDPOINT" = "$SECONDARY_ENDPOINT" ]; then
  ACTIVE_STATUS="PASS"
fi

if grep -q "primary_failure_detected" "$TRAFFIC_LOG" && grep -q "$PRIMARY_ENDPOINT,unhealthy" "$TRAFFIC_LOG"; then
  PRIMARY_FAILURE_STATUS="PASS"
fi

if [ "$SECONDARY_HEALTH" = "healthy" ]; then
  SECONDARY_HEALTH_STATUS="PASS"
fi

if grep -q "decision=shift_to_secondary" "$FAILOVER_DECISION_LOG"; then
  DECISION_STATUS="PASS"
fi

if grep -q "traffic_shifted,$SECONDARY_ENDPOINT,active" "$TRAFFIC_LOG"; then
  TRAFFIC_SHIFT_STATUS="PASS"
fi

if grep -q "primary_recovered,$PRIMARY_ENDPOINT,healthy" "$TRAFFIC_LOG"; then
  RECOVERY_STATUS="PASS"
fi

if grep -R "$VALIDATION_MARKER" runtime-workspace > evidence/generated/raw/resilience-marker-check.log; then
  MARKER_STATUS="PASS"
fi

if [ "$ACTIVE_STATUS" = "PASS" ] &&
   [ "$PRIMARY_FAILURE_STATUS" = "PASS" ] &&
   [ "$SECONDARY_HEALTH_STATUS" = "PASS" ] &&
   [ "$DECISION_STATUS" = "PASS" ] &&
   [ "$TRAFFIC_SHIFT_STATUS" = "PASS" ] &&
   [ "$RECOVERY_STATUS" = "PASS" ] &&
   [ "$MARKER_STATUS" = "PASS" ]; then
  OVERALL_STATUS="PASS"
fi

cat > "$SUMMARY" <<EOF
# Resilience Failover Execution Summary

Execution Mode: state-file-failover-simulation
Evidence Policy: local-only
Overall Status: $OVERALL_STATUS

## Validation Signals

| Signal | Status |
|---|---|
| Active endpoint shifted to secondary | $ACTIVE_STATUS |
| Primary failure detected | $PRIMARY_FAILURE_STATUS |
| Secondary endpoint healthy | $SECONDARY_HEALTH_STATUS |
| Failover decision generated | $DECISION_STATUS |
| Traffic shift validated | $TRAFFIC_SHIFT_STATUS |
| Primary recovery recorded | $RECOVERY_STATUS |
| Validation marker present | $MARKER_STATUS |

## Runtime State

| State | Value |
|---|---|
| Active endpoint | $ACTIVE_ENDPOINT |
| Primary health | $PRIMARY_HEALTH |
| Secondary health | $SECONDARY_HEALTH |

## Boundary

This summary records local-only runtime validation for the Resilience Failover Lab.
EOF

echo "[INFO] resilience failover validation completed"
echo "[INFO] overall_status=$OVERALL_STATUS"