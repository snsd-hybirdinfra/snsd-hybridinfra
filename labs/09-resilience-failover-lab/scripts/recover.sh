#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/failover-policy.env

mkdir -p runtime-workspace/state
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw

echo "[INFO] primary recovery simulation started"

echo "healthy" > "$PRIMARY_HEALTH_FILE"

ACTIVE_ENDPOINT="$(cat "$ACTIVE_ENDPOINT_FILE")"
PRIMARY_HEALTH="$(cat "$PRIMARY_HEALTH_FILE")"
SECONDARY_HEALTH="$(cat "$SECONDARY_HEALTH_FILE")"

cat >> "$TRAFFIC_LOG" <<EOF
2026-06-11T10:10:00Z,primary_recovered,$PRIMARY_ENDPOINT,healthy,$VALIDATION_MARKER
2026-06-11T10:10:05Z,active_endpoint_confirmed,$ACTIVE_ENDPOINT,active,$VALIDATION_MARKER
EOF

{
  echo "# Primary Recovery Simulation"
  echo
  echo "active_endpoint=$ACTIVE_ENDPOINT"
  echo "primary_health=$PRIMARY_HEALTH"
  echo "secondary_health=$SECONDARY_HEALTH"
  echo
  echo "## Traffic Log"
  cat "$TRAFFIC_LOG"
} | tee runtime-workspace/logs/recover.log

cp runtime-workspace/logs/recover.log evidence/generated/raw/resilience-recover-job.log
cp "$TRAFFIC_LOG" evidence/generated/raw/traffic-shift.log

echo "[INFO] primary recovery simulation completed"