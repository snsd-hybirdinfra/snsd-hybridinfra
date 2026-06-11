#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/failover-policy.env

mkdir -p runtime-workspace/state
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw

echo "[INFO] resilience failover simulation started"

# Simulate primary failure.
echo "unhealthy" > "$PRIMARY_HEALTH_FILE"

PRIMARY_HEALTH="$(cat "$PRIMARY_HEALTH_FILE")"
SECONDARY_HEALTH="$(cat "$SECONDARY_HEALTH_FILE")"
CURRENT_ACTIVE="$(cat "$ACTIVE_ENDPOINT_FILE")"

FAILOVER_DECISION="hold"

if [ "$CURRENT_ACTIVE" = "$PRIMARY_ENDPOINT" ] &&
   [ "$PRIMARY_HEALTH" = "unhealthy" ] &&
   [ "$SECONDARY_HEALTH" = "healthy" ]; then
  FAILOVER_DECISION="shift_to_secondary"
  echo "$SECONDARY_ENDPOINT" > "$ACTIVE_ENDPOINT_FILE"
fi

NEW_ACTIVE="$(cat "$ACTIVE_ENDPOINT_FILE")"

cat > "$FAILOVER_DECISION_LOG" <<EOF
timestamp=2026-06-11T10:05:00Z
current_active=$CURRENT_ACTIVE
primary_health=$PRIMARY_HEALTH
secondary_health=$SECONDARY_HEALTH
decision=$FAILOVER_DECISION
new_active=$NEW_ACTIVE
marker=$VALIDATION_MARKER
EOF

cat >> "$TRAFFIC_LOG" <<EOF
2026-06-11T10:05:00Z,primary_failure_detected,$PRIMARY_ENDPOINT,unhealthy,$VALIDATION_MARKER
2026-06-11T10:05:05Z,failover_decision,$NEW_ACTIVE,$FAILOVER_DECISION,$VALIDATION_MARKER
2026-06-11T10:05:10Z,traffic_shifted,$NEW_ACTIVE,active,$VALIDATION_MARKER
EOF

{
  echo "# Resilience Failover Simulation"
  echo
  cat "$FAILOVER_DECISION_LOG"
  echo
  echo "## Traffic Log"
  cat "$TRAFFIC_LOG"
} | tee runtime-workspace/logs/failover.log

cp runtime-workspace/logs/failover.log evidence/generated/raw/resilience-failover-job.log
cp "$FAILOVER_DECISION_LOG" evidence/generated/raw/failover-decision.log
cp "$TRAFFIC_LOG" evidence/generated/raw/traffic-shift.log

echo "[INFO] resilience failover simulation completed"