#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] network routing setup started"

test -f configs/network-targets.env

source configs/network-targets.env

{
  echo "# Network Routing Setup"
  echo
  echo "target_01=$TARGET_01_NAME $TARGET_01_IP"
  echo "target_02=$TARGET_02_NAME $TARGET_02_IP"
  echo "target_service_port=$TARGET_SERVICE_PORT"
  echo
  echo "## Local Route Table"
  ip route || true
  echo
  echo "## Local Address"
  ip addr || true
} | tee runtime-workspace/logs/setup.log

cp runtime-workspace/logs/setup.log evidence/generated/raw/network-routing-setup.log

echo "[INFO] network routing setup completed"