#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/monitoring-stack-runtime-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

PROMETHEUS_URL="http://127.0.0.1:9090"
GRAFANA_URL="http://127.0.0.1:3000"

PROMETHEUS_HEALTH="FAIL"
GRAFANA_HEALTH="FAIL"
RULE_API_STATUS="FAIL"
TARGET_DOWN_RULE="FAIL"
SCRAPE_LATENCY_RULE="FAIL"

retry_curl() {
  local url="$1"
  local output="$2"
  local attempts="${3:-20}"
  local delay="${4:-3}"

  for i in $(seq 1 "${attempts}"); do
    if curl -fsS "${url}" > "${output}"; then
      return 0
    fi
    sleep "${delay}"
  done

  return 1
}

if retry_curl "${PROMETHEUS_URL}/-/healthy" "${RAW_DIR}/prometheus-health.txt" 20 3; then
  PROMETHEUS_HEALTH="PASS"
fi

if retry_curl "${GRAFANA_URL}/api/health" "${RAW_DIR}/grafana-health.json" 30 3; then
  GRAFANA_HEALTH="PASS"
fi

if retry_curl "${PROMETHEUS_URL}/api/v1/rules" "${RAW_DIR}/prometheus-rules.json" 20 3; then
  RULE_API_STATUS="PASS"
fi

if grep -q "SNSDTargetDown" "${RAW_DIR}/prometheus-rules.json" 2>/dev/null; then
  TARGET_DOWN_RULE="PASS"
fi

if grep -q "SNSDHighScrapeLatency" "${RAW_DIR}/prometheus-rules.json" 2>/dev/null; then
  SCRAPE_LATENCY_RULE="PASS"
fi

if [ "${PROMETHEUS_HEALTH}" = "PASS" ] && \
   [ "${GRAFANA_HEALTH}" = "PASS" ] && \
   [ "${RULE_API_STATUS}" = "PASS" ] && \
   [ "${TARGET_DOWN_RULE}" = "PASS" ] && \
   [ "${SCRAPE_LATENCY_RULE}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Monitoring Stack Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Prometheus health endpoint | ${PROMETHEUS_HEALTH} |
| Grafana health endpoint | ${GRAFANA_HEALTH} |
| Prometheus rule API reachable | ${RULE_API_STATUS} |
| SNSDTargetDown alert rule loaded | ${TARGET_DOWN_RULE} |
| SNSDHighScrapeLatency alert rule loaded | ${SCRAPE_LATENCY_RULE} |

## Runtime Boundary

This lab validates a local monitoring stack runtime boundary using Prometheus and Grafana.

Phase 2 extends the runtime with Prometheus alert rule loading validation.

Generated runtime evidence remains local-only.

SUMMARY

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] monitoring stack validation did not reach PASS"
  echo "[DEBUG] docker containers:"
  docker ps
  echo "[DEBUG] prometheus rules sample:"
  head -c 2000 "${RAW_DIR}/prometheus-rules.json" 2>/dev/null || true
  echo
  exit 1
fi