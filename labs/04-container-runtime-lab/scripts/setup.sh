#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="04-container-runtime-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate Docker runtime prerequisite boundary"
echo "- prepare validation container boundary"
echo "- prepare image, volume, and network validation boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
