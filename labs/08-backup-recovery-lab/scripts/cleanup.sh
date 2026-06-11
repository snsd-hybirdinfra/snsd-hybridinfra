#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[INFO] backup recovery cleanup started"

rm -rf runtime-workspace
rm -rf evidence/generated/raw
rm -rf evidence/generated/summary

mkdir -p runtime-workspace/data
mkdir -p runtime-workspace/backup
mkdir -p runtime-workspace/restore
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] backup recovery cleanup completed"