#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${REPO_ROOT}"

failures=0

section() {
  echo
  echo "============================================================"
  echo "$1"
  echo "============================================================"
}

pass() {
  echo "[PASS] $1"
}

fail() {
  echo "[FAIL] $1"
  failures=$((failures + 1))
}

check_equals() {
  local name="$1"
  local actual="$2"
  local expected="$3"

  if [ "${actual}" = "${expected}" ]; then
    pass "${name}: ${actual}"
  else
    fail "${name}: actual=${actual}, expected=${expected}"
  fi
}

section "SNSD Repository Static Check"
echo "repo=${REPO_ROOT}"
echo "checked_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

section "Scenario Count"
scenario_count="$(find scenarios -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')"
check_equals "scenario directory count" "${scenario_count}" "150"

section "Scenario Runtime Evidence"
runtime_evidence_count="$(find scenarios -path '*/evidence/generated/lab-runtime-validation.md' | wc -l | tr -d ' ')"
check_equals "lab-runtime-validation evidence count" "${runtime_evidence_count}" "150"

if grep -R "NOT_FOUND:" scenarios/*/*/evidence/generated/lab-runtime-validation.md >/dev/null 2>&1; then
  fail "NOT_FOUND remains in scenario runtime evidence"
  grep -R "NOT_FOUND:" scenarios/*/*/evidence/generated/lab-runtime-validation.md | head -20
else
  pass "no NOT_FOUND in scenario runtime evidence"
fi

section "Runtime Validation Documents"
if [ -f docs/runtime-validation-pipeline.md ]; then
  pass "docs/runtime-validation-pipeline.md exists"
else
  fail "docs/runtime-validation-pipeline.md missing"
fi

if [ -f docs/lab-runtime-validation-index.md ]; then
  pass "docs/lab-runtime-validation-index.md exists"
else
  fail "docs/lab-runtime-validation-index.md missing"
fi

if [ -f docs/lab-runtime-validation-index.md ]; then
  index_total="$(grep -E 'Total scenarios:' docs/lab-runtime-validation-index.md | head -1 | sed 's/[^0-9]//g')"
  index_ok="$(grep -E 'OK:' docs/lab-runtime-validation-index.md | head -1 | sed 's/[^0-9]//g')"
  index_missing="$(grep -E 'Missing evidence:' docs/lab-runtime-validation-index.md | head -1 | sed 's/[^0-9]//g')"
  index_not_found="$(grep -E 'Contains NOT_FOUND:' docs/lab-runtime-validation-index.md | head -1 | sed 's/[^0-9]//g')"

  check_equals "index total scenarios" "${index_total:-missing}" "150"
  check_equals "index ok scenarios" "${index_ok:-missing}" "150"
  check_equals "index missing evidence" "${index_missing:-missing}" "0"
  check_equals "index NOT_FOUND count" "${index_not_found:-missing}" "0"
fi

section "README Check"
if [ -f README.md ]; then
  if grep -q "docs/runtime-validation-pipeline.md" README.md; then
    pass "README links runtime validation pipeline doc"
  else
    fail "README missing runtime validation pipeline link"
  fi

  if grep -q "docs/lab-runtime-validation-index.md" README.md; then
    pass "README links runtime validation index doc"
  else
    fail "README missing lab runtime validation index link"
  fi
else
  fail "README.md missing"
fi

section "Deprecated Files"
if [ -f ansible/playbooks/15-collect-runtime-evidence.yml ]; then
  fail "deprecated ansible/playbooks/15-collect-runtime-evidence.yml still exists"
else
  pass "deprecated 15-collect-runtime-evidence.yml removed"
fi

section "Git Policy Check"
if git status --short | grep -E '^A  labs/evidence/generated|^M  labs/evidence/generated|^\?\? labs/evidence/generated' >/dev/null 2>&1; then
  fail "labs/evidence/generated appears in git visible changes"
  git status --short | grep "labs/evidence/generated" || true
else
  pass "labs/evidence/generated not staged as reviewer evidence"
fi

section "Tool Files"
for file in \
  tools/evidence/collect_runtime_evidence.sh \
  tools/evidence/generate_lab_runtime_validation.py \
  tools/evidence/generate_lab_runtime_validation_index.py \
  tools/validation/runtime_smoke_check.sh \
  tools/validation/repository_static_check.sh \
  tools/pipeline/run_runtime_validation_pipeline.sh
do
  if [ -f "${file}" ]; then
    pass "${file} exists"
  else
    fail "${file} missing"
  fi
done

section "Summary"
if [ "${failures}" -eq 0 ]; then
  echo "[OK] repository static check passed"
  exit 0
else
  echo "[FAIL] repository static check failed: ${failures} issue(s)"
  exit 1
fi
