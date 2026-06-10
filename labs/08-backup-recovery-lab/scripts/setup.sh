#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="08-backup-recovery-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate backup source boundary"
echo "- prepare backup repository boundary"
echo "- prepare restore target boundary"
echo "- prepare integrity validation boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
