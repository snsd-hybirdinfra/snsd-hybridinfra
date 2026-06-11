#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[INFO] resilience failover cleanup started"

rm -rf runtime-workspace
rm -rf evidence/generated/raw
rm -rf evidence/generated/summary

mkdir -p runtime-workspace/state
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] resilience failover cleanup completed"