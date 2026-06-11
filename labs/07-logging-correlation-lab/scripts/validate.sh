#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/logging-correlation-validate.log"
SUMMARY="evidence/generated/summary/logging-correlation-execution-summary.md"

echo "[INFO] logging correlation validation started"

python3 scripts/correlate_logs.py | tee "$RAW_LOG"

if [ ! -f "$SUMMARY" ]; then
  echo "[ERROR] summary not generated"
  exit 1
fi

cat "$SUMMARY"

echo "[INFO] logging correlation validation completed"