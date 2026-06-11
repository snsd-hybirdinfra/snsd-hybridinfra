#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/container-runtime-validate.log"
SUMMARY="evidence/generated/summary/container-runtime-execution-summary.md"
ENDPOINT_BODY="evidence/generated/raw/container-web-endpoint.html"

WEB_CONTAINER="snsd-runtime-web"
WORKER_CONTAINER="snsd-runtime-worker"
WEB_URL="http://127.0.0.1:18080"

DOCKER_STATUS="CHECK"
COMPOSE_STATUS="CHECK"
WEB_RUNNING_STATUS="CHECK"
WORKER_RUNNING_STATUS="CHECK"
WEB_HEALTH_STATUS="CHECK"
WEB_ENDPOINT_STATUS="CHECK"
LOG_STATUS="CHECK"
RESTART_STATUS="CHECK"
FAILED_COUNT="0"
OVERALL_STATUS="CHECK"

: > "$RAW_LOG"

echo "[INFO] container runtime validation started"

{
  echo "# Container Runtime Validation"
  echo
  echo "## Docker Runtime"
} | tee -a "$RAW_LOG"

if docker info > /dev/null 2>&1; then
  DOCKER_STATUS="PASS"
  echo "docker_runtime=PASS" | tee -a "$RAW_LOG"
else
  echo "docker_runtime=CHECK" | tee -a "$RAW_LOG"
fi

{
  echo
  echo "## Compose Status"
} | tee -a "$RAW_LOG"

if docker compose -p snsd-container-runtime-lab -f compose/docker-compose.yml ps | tee -a "$RAW_LOG"; then
  COMPOSE_STATUS="PASS"
fi

if docker inspect -f '{{.State.Running}}' "$WEB_CONTAINER" 2>/dev/null | grep -q "true"; then
  WEB_RUNNING_STATUS="PASS"
fi

if docker inspect -f '{{.State.Running}}' "$WORKER_CONTAINER" 2>/dev/null | grep -q "true"; then
  WORKER_RUNNING_STATUS="PASS"
fi

{
  echo
  echo "## Web Healthcheck Wait"
} | tee -a "$RAW_LOG"

for i in $(seq 1 12); do
  WEB_HEALTH="$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$WEB_CONTAINER" 2>/dev/null || true)"
  echo "health_attempt=$i web_health=$WEB_HEALTH" | tee -a "$RAW_LOG"

  if [ "$WEB_HEALTH" = "healthy" ]; then
    WEB_HEALTH_STATUS="PASS"
    break
  fi

  sleep 5
done

{
  echo
  echo "## Endpoint Check"
} | tee -a "$RAW_LOG"

if curl -fsS "$WEB_URL" -o "$ENDPOINT_BODY"; then
  cat "$ENDPOINT_BODY" >> "$RAW_LOG"
  echo >> "$RAW_LOG"

  if grep -q "SNSD Container Runtime Lab" "$ENDPOINT_BODY"; then
    WEB_ENDPOINT_STATUS="PASS"
  fi
fi

{
  echo
  echo "## Container Logs"
} | tee -a "$RAW_LOG"

docker logs "$WORKER_CONTAINER" --tail 20 | tee -a "$RAW_LOG" > evidence/generated/raw/container-worker.log

if grep -q "runtime-worker-alive" evidence/generated/raw/container-worker.log; then
  LOG_STATUS="PASS"
fi

{
  echo
  echo "## Restart Recovery Check"
} | tee -a "$RAW_LOG"

docker restart "$WEB_CONTAINER" | tee -a "$RAW_LOG"

for i in $(seq 1 12); do
  WEB_RUNNING_AFTER_RESTART="$(docker inspect -f '{{.State.Running}}' "$WEB_CONTAINER" 2>/dev/null || true)"
  WEB_HEALTH_AFTER_RESTART="$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$WEB_CONTAINER" 2>/dev/null || true)"

  echo "restart_attempt=$i running=$WEB_RUNNING_AFTER_RESTART health=$WEB_HEALTH_AFTER_RESTART" | tee -a "$RAW_LOG"

  if [ "$WEB_RUNNING_AFTER_RESTART" = "true" ]; then
    RESTART_STATUS="PASS"
  fi

  if [ "$WEB_HEALTH_AFTER_RESTART" = "healthy" ]; then
    break
  fi

  sleep 5
done

FAILED_COUNT="$(grep -Ec "ERROR|FAILED|Cannot connect to the Docker daemon" "$RAW_LOG" || true)"

if [ "$DOCKER_STATUS" = "PASS" ] &&
   [ "$COMPOSE_STATUS" = "PASS" ] &&
   [ "$WEB_RUNNING_STATUS" = "PASS" ] &&
   [ "$WORKER_RUNNING_STATUS" = "PASS" ] &&
   [ "$WEB_HEALTH_STATUS" = "PASS" ] &&
   [ "$WEB_ENDPOINT_STATUS" = "PASS" ] &&
   [ "$LOG_STATUS" = "PASS" ] &&
   [ "$RESTART_STATUS" = "PASS" ]; then
  OVERALL_STATUS="PASS"
fi

cat > "$SUMMARY" <<EOF
# Container Runtime Execution Summary

Execution Mode: docker-compose
Evidence Policy: local-only
Overall Status: $OVERALL_STATUS

## Validation Signals

| Signal | Status |
|---|---|
| Docker runtime available | $DOCKER_STATUS |
| docker compose -p snsd-container-runtime-lab status available | $COMPOSE_STATUS |
| Web container running | $WEB_RUNNING_STATUS |
| Worker container running | $WORKER_RUNNING_STATUS |
| Web container healthcheck | $WEB_HEALTH_STATUS |
| Web endpoint content check | $WEB_ENDPOINT_STATUS |
| Worker container log check | $LOG_STATUS |
| Restart recovery check | $RESTART_STATUS |
| Failure pattern count | $FAILED_COUNT |

## Runtime Components

| Component | Role | Port |
|---|---|---:|
| snsd-runtime-web | HTTP service container | 18080 |
| snsd-runtime-worker | Background worker container | n/a |

## Boundary

This summary records local-only runtime validation for the Container Runtime Lab.
EOF

echo "[INFO] container runtime validation completed"
echo "[INFO] overall_status=$OVERALL_STATUS"
echo "[INFO] web_health_status=$WEB_HEALTH_STATUS"
echo "[INFO] web_endpoint_status=$WEB_ENDPOINT_STATUS"