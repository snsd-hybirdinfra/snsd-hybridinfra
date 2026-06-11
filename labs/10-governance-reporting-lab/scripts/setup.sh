#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] governance reporting setup started"

python3 --version | tee runtime-workspace/logs/python-version.log

test -f configs/governance-reporting-policy.env
test -f scripts/collect_governance_report.py

echo "[INFO] governance reporting setup completed"