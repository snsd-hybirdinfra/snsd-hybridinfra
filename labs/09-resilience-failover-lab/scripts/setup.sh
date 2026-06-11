#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/failover-policy.env

mkdir -p runtime-workspace/state
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] resilience failover setup started"

echo "$PRIMARY_ENDPOINT" > "$ACTIVE_ENDPOINT_FILE"
echo "healthy" > "$PRIMARY_HEALTH_FILE"
echo "healthy" > "$SECONDARY_HEALTH_FILE"

cat > "$TRAFFIC_LOG" <<EOF
timestamp,event,endpoint,status,marker
2026-06-11T10:00:00Z,traffic_initialized,$PRIMARY_ENDPOINT,active,$VALIDATION_MARKER
EOF

{
  echo "# Resilience Failover Setup"
  echo
  echo "primary_endpoint=$PRIMARY_ENDPOINT"
  echo "secondary_endpoint=$SECONDARY_ENDPOINT"
  echo "active_endpoint=$(cat "$ACTIVE_ENDPOINT_FILE")"
  echo "primary_health=$(cat "$PRIMARY_HEALTH_FILE")"
  echo "secondary_health=$(cat "$SECONDARY_HEALTH_FILE")"
} | tee runtime-workspace/logs/setup.log

cp runtime-workspace/logs/setup.log evidence/generated/raw/resilience-failover-setup.log

echo "[INFO] resilience failover setup completed"