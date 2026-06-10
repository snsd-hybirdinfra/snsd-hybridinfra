#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="07-logging-correlation-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate log source boundary"
echo "- prepare log forwarding boundary"
echo "- prepare OpenSearch search boundary"
echo "- prepare correlation validation boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
