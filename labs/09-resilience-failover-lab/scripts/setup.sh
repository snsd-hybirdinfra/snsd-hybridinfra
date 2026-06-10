#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="09-resilience-failover-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate primary service boundary"
echo "- validate secondary service boundary"
echo "- prepare traffic shift validation boundary"
echo "- prepare failover decision boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
