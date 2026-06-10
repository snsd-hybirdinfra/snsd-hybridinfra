#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="10-governance-reporting-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate repository workspace boundary"
echo "- prepare governance reporting boundary"
echo "- prepare validation report boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
