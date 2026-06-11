#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] logging correlation setup started"

python3 --version | tee runtime-workspace/logs/python-version.log

test -f datasets/sample-events.log
test -f configs/correlation-rules.yml
test -f scripts/correlate_logs.py

echo "[INFO] logging correlation setup completed"