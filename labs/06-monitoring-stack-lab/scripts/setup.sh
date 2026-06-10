#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="06-monitoring-stack-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate monitoring node prerequisites"
echo "- prepare Prometheus configuration boundary"
echo "- prepare Grafana dashboard boundary"
echo "- prepare exporter target boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
