#!/usr/bin/env bash
set -uo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
SUMMARY="${SUMMARY_DIR}/ansible-automation-runtime-summary.md"
MARKER="${LAB_DIR}/runtime-workspace/ansible-runtime/phase2-idempotency-marker.txt"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LAB_DIR}/runtime-workspace/logs"

ANSIBLE_CLI="FAIL"
FIRST_APPLY="FAIL"
SECOND_APPLY="FAIL"
IDEMPOTENCY_CHECK="FAIL"
ROLLBACK_EXECUTION="FAIL"
ROLLBACK_VALIDATION="FAIL"

echo "[INFO] ansible automation validation started"

if ansible --version > "${RAW_DIR}/ansible-version.txt" 2>&1; then
  ANSIBLE_CLI="PASS"
fi

ansible-playbook "${LAB_DIR}/playbooks/phase2-idempotency.yml" \
  > "${RAW_DIR}/phase2-idempotency-first.log" 2>&1
FIRST_RC=$?

if [ "${FIRST_RC}" -eq 0 ] && [ -f "${MARKER}" ]; then
  FIRST_APPLY="PASS"
fi

ansible-playbook "${LAB_DIR}/playbooks/phase2-idempotency.yml" \
  > "${RAW_DIR}/phase2-idempotency-second.log" 2>&1
SECOND_RC=$?

if [ "${SECOND_RC}" -eq 0 ]; then
  SECOND_APPLY="PASS"
fi

if grep -q "changed=0" "${RAW_DIR}/phase2-idempotency-second.log"; then
  IDEMPOTENCY_CHECK="PASS"
fi

ansible-playbook "${LAB_DIR}/playbooks/phase2-rollback.yml" \
  > "${RAW_DIR}/phase2-rollback.log" 2>&1
ROLLBACK_RC=$?

if [ "${ROLLBACK_RC}" -eq 0 ]; then
  ROLLBACK_EXECUTION="PASS"
fi

if [ ! -f "${MARKER}" ]; then
  ROLLBACK_VALIDATION="PASS"
fi

if [ "${ANSIBLE_CLI}" = "PASS" ] && \
   [ "${FIRST_APPLY}" = "PASS" ] && \
   [ "${SECOND_APPLY}" = "PASS" ] && \
   [ "${IDEMPOTENCY_CHECK}" = "PASS" ] && \
   [ "${ROLLBACK_EXECUTION}" = "PASS" ] && \
   [ "${ROLLBACK_VALIDATION}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Ansible Automation Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Ansible CLI available | ${ANSIBLE_CLI} |
| First automation apply completed | ${FIRST_APPLY} |
| Second automation apply completed | ${SECOND_APPLY} |
| Idempotency confirmed on second run | ${IDEMPOTENCY_CHECK} |
| Rollback playbook completed | ${ROLLBACK_EXECUTION} |
| Rollback removed runtime marker | ${ROLLBACK_VALIDATION} |

## Runtime Boundary

This lab validates local Ansible automation execution quality.

Phase 2 extends the runtime with deterministic idempotency and rollback validation.

Generated runtime evidence remains local-only.

SUMMARY

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] Ansible automation runtime validation did not reach PASS"
  echo "[DEBUG] first apply log:"
  tail -80 "${RAW_DIR}/phase2-idempotency-first.log" 2>/dev/null || true
  echo "[DEBUG] second apply log:"
  tail -80 "${RAW_DIR}/phase2-idempotency-second.log" 2>/dev/null || true
  echo "[DEBUG] rollback log:"
  tail -80 "${RAW_DIR}/phase2-rollback.log" 2>/dev/null || true
  exit 1
fi

echo "[OK] ansible automation validation completed"