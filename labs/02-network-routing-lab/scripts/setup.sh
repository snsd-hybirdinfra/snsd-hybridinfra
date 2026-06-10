#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="02-network-routing-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate management node dependencies"
echo "- validate routing node reachability"
echo "- prepare interface and route validation paths"
echo "- prepare FRR or Linux routing configuration boundary"
echo "- prepare DNS and reachability validation tools"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
