#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

source configs/network-targets.env

RAW_LOG="evidence/generated/raw/network-routing-validate.log"
SUMMARY="evidence/generated/summary/network-routing-execution-summary.md"
PING_01_RAW="evidence/generated/raw/ping-${TARGET_01_NAME}.log"
PING_02_RAW="evidence/generated/raw/ping-${TARGET_02_NAME}.log"
ROUTE_RAW="evidence/generated/raw/local-route-table.log"
DNS_RAW="evidence/generated/raw/dns-resolution.log"
SERVICE_01_RAW="evidence/generated/raw/service-${TARGET_01_NAME}.log"
SERVICE_02_RAW="evidence/generated/raw/service-${TARGET_02_NAME}.log"

TARGET_01_REACHABILITY="CHECK"
TARGET_02_REACHABILITY="CHECK"
TARGET_01_SERVICE="CHECK"
TARGET_02_SERVICE="CHECK"
DNS_STATUS="CHECK"
ROUTE_STATUS="CHECK"
LATENCY_STATUS="CHECK"
OVERALL_STATUS="CHECK"

TARGET_01_AVG_LATENCY="unknown"
TARGET_02_AVG_LATENCY="unknown"

: > "$RAW_LOG"

echo "[INFO] network routing validation started"

{
  echo "# Network Routing Validation"
  echo
  echo "## Local Route Table"
} | tee -a "$RAW_LOG"

if ip route | tee "$ROUTE_RAW" | tee -a "$RAW_LOG" | grep -q "default"; then
  ROUTE_STATUS="PASS"
fi

{
  echo
  echo "## DNS Resolution"
} | tee -a "$RAW_LOG"

if getent hosts "$DNS_TEST_NAME" | tee "$DNS_RAW" | tee -a "$RAW_LOG"; then
  DNS_STATUS="PASS"
fi

{
  echo
  echo "## ICMP Reachability - $TARGET_01_NAME"
} | tee -a "$RAW_LOG"

if ping -c "$PING_COUNT" "$TARGET_01_IP" | tee "$PING_01_RAW" | tee -a "$RAW_LOG"; then
  TARGET_01_REACHABILITY="PASS"
fi

{
  echo
  echo "## ICMP Reachability - $TARGET_02_NAME"
} | tee -a "$RAW_LOG"

if ping -c "$PING_COUNT" "$TARGET_02_IP" | tee "$PING_02_RAW" | tee -a "$RAW_LOG"; then
  TARGET_02_REACHABILITY="PASS"
fi

TARGET_01_AVG_LATENCY="$(awk -F'/' '/rtt min\/avg\/max/ {print $5}' "$PING_01_RAW" 2>/dev/null || echo unknown)"
TARGET_02_AVG_LATENCY="$(awk -F'/' '/rtt min\/avg\/max/ {print $5}' "$PING_02_RAW" 2>/dev/null || echo unknown)"

if python3 - "$TARGET_01_AVG_LATENCY" "$TARGET_02_AVG_LATENCY" "$LATENCY_THRESHOLD_MS" <<'PY'
import sys

values = sys.argv[1:3]
threshold = float(sys.argv[3])

try:
    parsed = [float(v) for v in values if v != "unknown" and v != ""]
    if len(parsed) == 2 and all(v <= threshold for v in parsed):
        sys.exit(0)
except Exception:
    pass

sys.exit(1)
PY
then
  LATENCY_STATUS="PASS"
fi

{
  echo
  echo "## Service Port Reachability - $TARGET_01_NAME"
} | tee -a "$RAW_LOG"

if curl -fsS "http://$TARGET_01_IP:$TARGET_SERVICE_PORT/metrics" -o "$SERVICE_01_RAW"; then
  if grep -q "node_cpu_seconds_total" "$SERVICE_01_RAW"; then
    TARGET_01_SERVICE="PASS"
  fi
fi

echo "service_${TARGET_01_NAME}=$TARGET_01_SERVICE" | tee -a "$RAW_LOG"

{
  echo
  echo "## Service Port Reachability - $TARGET_02_NAME"
} | tee -a "$RAW_LOG"

if curl -fsS "http://$TARGET_02_IP:$TARGET_SERVICE_PORT/metrics" -o "$SERVICE_02_RAW"; then
  if grep -q "node_cpu_seconds_total" "$SERVICE_02_RAW"; then
    TARGET_02_SERVICE="PASS"
  fi
fi

echo "service_${TARGET_02_NAME}=$TARGET_02_SERVICE" | tee -a "$RAW_LOG"

{
  echo
  echo "## Latency Summary"
  echo "target_01_avg_latency_ms=$TARGET_01_AVG_LATENCY"
  echo "target_02_avg_latency_ms=$TARGET_02_AVG_LATENCY"
  echo "latency_threshold_ms=$LATENCY_THRESHOLD_MS"
  echo "latency_status=$LATENCY_STATUS"
} | tee -a "$RAW_LOG"

if [ "$TARGET_01_REACHABILITY" = "PASS" ] &&
   [ "$TARGET_02_REACHABILITY" = "PASS" ] &&
   [ "$TARGET_01_SERVICE" = "PASS" ] &&
   [ "$TARGET_02_SERVICE" = "PASS" ] &&
   [ "$DNS_STATUS" = "PASS" ] &&
   [ "$ROUTE_STATUS" = "PASS" ] &&
   [ "$LATENCY_STATUS" = "PASS" ]; then
  OVERALL_STATUS="PASS"
fi

cat > "$SUMMARY" <<EOF
# Network Routing Execution Summary

Execution Mode: local-network-path-validation
Evidence Policy: local-only
Overall Status: $OVERALL_STATUS

## Validation Signals

| Signal | Status |
|---|---|
| Local route table available | $ROUTE_STATUS |
| DNS resolution available | $DNS_STATUS |
| $TARGET_01_NAME ICMP reachability | $TARGET_01_REACHABILITY |
| $TARGET_02_NAME ICMP reachability | $TARGET_02_REACHABILITY |
| $TARGET_01_NAME node_exporter service path | $TARGET_01_SERVICE |
| $TARGET_02_NAME node_exporter service path | $TARGET_02_SERVICE |
| Latency threshold validation | $LATENCY_STATUS |

## Latency Measurements

| Target | Average Latency ms | Threshold ms |
|---|---:|---:|
| $TARGET_01_NAME | $TARGET_01_AVG_LATENCY | $LATENCY_THRESHOLD_MS |
| $TARGET_02_NAME | $TARGET_02_AVG_LATENCY | $LATENCY_THRESHOLD_MS |

## Target Model

| Target | Address | Service Port |
|---|---|---:|
| $TARGET_01_NAME | $TARGET_01_IP | $TARGET_SERVICE_PORT |
| $TARGET_02_NAME | $TARGET_02_IP | $TARGET_SERVICE_PORT |

## Boundary

This summary records local-only runtime validation for the Network Routing Lab.
EOF

echo "[INFO] network routing validation completed"
echo "[INFO] overall_status=$OVERALL_STATUS"