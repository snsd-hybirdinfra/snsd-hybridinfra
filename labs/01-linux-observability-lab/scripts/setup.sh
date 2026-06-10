#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="01-linux-observability-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate management node dependencies"
echo "- validate Linux host reachability"
echo "- prepare node exporter installation path"
echo "- prepare Prometheus scrape target configuration"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
