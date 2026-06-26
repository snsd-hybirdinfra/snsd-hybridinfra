#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${REPO_ROOT}"

echo
echo "============================================================"
echo "SNSD Runtime Validation Pipeline"
echo "============================================================"
echo "repo=${REPO_ROOT}"
echo "started_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

echo
echo "============================================================"
echo "Step 1. Collect runtime evidence"
echo "============================================================"
tools/evidence/collect_runtime_evidence.sh

echo
echo "============================================================"
echo "Step 2. Generate scenario-level lab runtime validation evidence"
echo "============================================================"
python3 tools/evidence/generate_lab_runtime_validation.py

echo
echo "============================================================"
echo "Step 3. Generate lab runtime validation index"
echo "============================================================"
python3 tools/evidence/generate_lab_runtime_validation_index.py

echo
echo "============================================================"
echo "Step 4. Run runtime smoke check"
echo "============================================================"
tools/validation/runtime_smoke_check.sh

echo
echo "============================================================"
echo "Pipeline Summary"
echo "============================================================"

echo "scenario_evidence_count=$(find scenarios -path '*/evidence/generated/lab-runtime-validation.md' | wc -l)"
echo "not_found_count=$(grep -R 'NOT_FOUND:' scenarios/*/*/evidence/generated/lab-runtime-validation.md 2>/dev/null | wc -l)"
echo "index=docs/lab-runtime-validation-index.md"
echo "finished_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

echo
echo "[OK] runtime validation pipeline completed"
