#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] monitoring stack validation started"

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/monitoring-validate.log"
SUMMARY="evidence/generated/summary/monitoring-stack-execution-summary.md"

PROM_URL="http://127.0.0.1:9090"
GRAFANA_URL="http://127.0.0.1:3000"

TARGET_01="192.168.8.129:9100"
TARGET_02="192.168.8.130:9100"

PROM_HEALTH="CHECK"
GRAFANA_HEALTH="CHECK"
TARGET_01_HEALTH="CHECK"
TARGET_02_HEALTH="CHECK"
DATASOURCE_FILE="CHECK"
DASHBOARD_PROVIDER_FILE="CHECK"
DASHBOARD_JSON_FILE="CHECK"
OVERALL_STATUS="CHECK"

exec > >(tee "$RAW_LOG") 2>&1

echo "# Monitoring Stack Validation"
echo
echo "## Container Status"
docker compose -f compose/docker-compose.yml ps || true
echo

echo "## Prometheus Health"
if curl -fsS "$PROM_URL/-/healthy"; then
  PROM_HEALTH="PASS"
else
  PROM_HEALTH="CHECK"
fi
echo

echo "## Grafana Health"
if curl -fsS "$GRAFANA_URL/api/health"; then
  GRAFANA_HEALTH="PASS"
else
  GRAFANA_HEALTH="CHECK"
fi
echo

echo "## Prometheus Targets"
TARGETS_JSON="$(curl -fsS "$PROM_URL/api/v1/targets" || true)"
echo "$TARGETS_JSON"
echo

if echo "$TARGETS_JSON" | grep -q "$TARGET_01" && echo "$TARGETS_JSON" | grep -A 30 "$TARGET_01" | grep -q '"health":"up"'; then
  TARGET_01_HEALTH="PASS"
fi

if echo "$TARGETS_JSON" | grep -q "$TARGET_02" && echo "$TARGETS_JSON" | grep -A 30 "$TARGET_02" | grep -q '"health":"up"'; then
  TARGET_02_HEALTH="PASS"
fi

echo "## Prometheus Query"
curl -fsS -G "$PROM_URL/api/v1/query" --data-urlencode 'query=up{job="linux-observability-vmware-targets"}' || true
echo
echo

echo "## Grafana Provisioning Files"
if [ -f "configs/grafana/provisioning/datasources/prometheus.yml" ]; then
  DATASOURCE_FILE="PASS"
fi

if [ -f "configs/grafana/provisioning/dashboards/linux-observability.yml" ]; then
  DASHBOARD_PROVIDER_FILE="PASS"
fi

if [ -f "configs/grafana/dashboards/linux-node-exporter-basic.json" ]; then
  DASHBOARD_JSON_FILE="PASS"
fi

echo "datasource_file=$DATASOURCE_FILE"
echo "dashboard_provider_file=$DASHBOARD_PROVIDER_FILE"
echo "dashboard_json_file=$DASHBOARD_JSON_FILE"
echo

if [ "$PROM_HEALTH" = "PASS" ] &&
   [ "$GRAFANA_HEALTH" = "PASS" ] &&
   [ "$TARGET_01_HEALTH" = "PASS" ] &&
   [ "$TARGET_02_HEALTH" = "PASS" ] &&
   [ "$DATASOURCE_FILE" = "PASS" ] &&
   [ "$DASHBOARD_PROVIDER_FILE" = "PASS" ] &&
   [ "$DASHBOARD_JSON_FILE" = "PASS" ]; then
  OVERALL_STATUS="PASS"
fi

cat > "$SUMMARY" <<EOF
# Monitoring Stack Execution Summary

Execution Mode: docker-compose
Evidence Policy: local-only
Overall Status: $OVERALL_STATUS

## Validation Signals

| Signal | Status |
|---|---|
| Prometheus health endpoint | $PROM_HEALTH |
| Grafana health endpoint | $GRAFANA_HEALTH |
| Prometheus target $TARGET_01 | $TARGET_01_HEALTH |
| Prometheus target $TARGET_02 | $TARGET_02_HEALTH |
| Grafana datasource provisioning file | $DATASOURCE_FILE |
| Grafana dashboard provider file | $DASHBOARD_PROVIDER_FILE |
| Grafana dashboard JSON file | $DASHBOARD_JSON_FILE |

## Expected Services

| Service | Port |
|---|---:|
| Prometheus | 9090 |
| Grafana | 3000 |
| node_exporter | 9100 |

## Boundary

This summary records local-only runtime validation for the Monitoring Stack Lab.
EOF

echo "[INFO] monitoring stack validation completed"
echo "[INFO] overall_status=$OVERALL_STATUS"