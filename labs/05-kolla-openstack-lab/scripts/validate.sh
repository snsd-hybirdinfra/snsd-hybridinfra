#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/kolla-openstack-validate.log"
SUMMARY="evidence/generated/summary/kolla-openstack-execution-summary.md"

echo "[INFO] kolla openstack preflight validation started"

python3 scripts/kolla_preflight.py | tee "$RAW_LOG"

if [ ! -f "$SUMMARY" ]; then
  echo "[ERROR] summary not generated"
  exit 1
fi

cat "$SUMMARY"

if ! grep -q "Overall Status: PASS" "$SUMMARY"; then
  echo "[ERROR] kolla preflight summary is not PASS"
  exit 1
fi

echo "[INFO] kolla openstack preflight validation completed"