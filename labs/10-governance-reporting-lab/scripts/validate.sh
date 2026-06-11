#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/governance-reporting-validate.log"
SUMMARY="evidence/generated/summary/governance-reporting-execution-summary.md"

set -a
source configs/governance-reporting-policy.env
set +a

echo "[INFO] governance reporting validation started"

python3 scripts/collect_governance_report.py | tee "$RAW_LOG"

if [ ! -f "$SUMMARY" ]; then
  echo "[ERROR] governance summary not generated"
  exit 1
fi

cat "$SUMMARY"

if ! grep -q "Overall Status: PASS" "$SUMMARY"; then
  echo "[ERROR] governance reporting summary is not PASS"
  exit 1
fi

echo "[INFO] governance reporting validation completed"