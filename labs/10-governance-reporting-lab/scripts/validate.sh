#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_DIR="$(cd "${LAB_DIR}/../.." && pwd)"

RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"

MATRIX="${RAW_DIR}/phase2-runtime-evidence-matrix.tsv"
STATUS_TSV="${RAW_DIR}/governance-runtime-status.tsv"
VALIDATE_LOG="${RAW_DIR}/governance-reporting-validate.log"
SUMMARY="${SUMMARY_DIR}/governance-reporting-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/governance-reporting-execution-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] governance reporting validation started"

declare -A LAB_SUMMARIES
LAB_SUMMARIES["03-ansible-automation-lab"]="${REPO_DIR}/labs/03-ansible-automation-lab/evidence/generated/summary/ansible-automation-runtime-summary.md"
LAB_SUMMARIES["06-monitoring-stack-lab"]="${REPO_DIR}/labs/06-monitoring-stack-lab/evidence/generated/summary/monitoring-stack-runtime-summary.md"
LAB_SUMMARIES["08-backup-recovery-lab"]="${REPO_DIR}/labs/08-backup-recovery-lab/evidence/generated/summary/backup-recovery-runtime-summary.md"
LAB_SUMMARIES["09-resilience-failover-lab"]="${REPO_DIR}/labs/09-resilience-failover-lab/evidence/generated/summary/resilience-failover-runtime-summary.md"

WORKSPACE_STATUS="PASS"
SCAN_STATUS="PASS"
REPORT_STATUS="FAIL"

ANSIBLE_STATUS="FAIL"
MONITORING_STATUS="FAIL"
BACKUP_STATUS="FAIL"
FAILOVER_STATUS="FAIL"

{
  echo -e "lab\tsummary_path\tfile_present\toverall_status"
} > "${MATRIX}"

for lab in "03-ansible-automation-lab" "06-monitoring-stack-lab" "08-backup-recovery-lab" "09-resilience-failover-lab"; do
  summary="${LAB_SUMMARIES[$lab]}"
  present="no"
  status="MISSING"

  if [ -f "${summary}" ]; then
    present="yes"
    if grep -q "Overall Status: PASS" "${summary}"; then
      status="PASS"
    else
      status="CHECK"
    fi
  fi

  echo -e "${lab}\t${summary}\t${present}\t${status}" >> "${MATRIX}"

  case "${lab}" in
    "03-ansible-automation-lab")
      [ "${status}" = "PASS" ] && ANSIBLE_STATUS="PASS" || ANSIBLE_STATUS="CHECK"
      ;;
    "06-monitoring-stack-lab")
      [ "${status}" = "PASS" ] && MONITORING_STATUS="PASS" || MONITORING_STATUS="CHECK"
      ;;
    "08-backup-recovery-lab")
      [ "${status}" = "PASS" ] && BACKUP_STATUS="PASS" || BACKUP_STATUS="CHECK"
      ;;
    "09-resilience-failover-lab")
      [ "${status}" = "PASS" ] && FAILOVER_STATUS="PASS" || FAILOVER_STATUS="CHECK"
      ;;
  esac
done

if [ "${ANSIBLE_STATUS}" = "PASS" ] && \
   [ "${MONITORING_STATUS}" = "PASS" ] && \
   [ "${BACKUP_STATUS}" = "PASS" ] && \
   [ "${FAILOVER_STATUS}" = "PASS" ]; then
  GOVERNANCE_DECISION="PASS"
  REPORT_STATUS="PASS"
else
  GOVERNANCE_DECISION="CHECK"
  REPORT_STATUS="PASS"
fi

cat > "${STATUS_TSV}" <<STATUS
signalstatus
governance_workspace_prepared${WORKSPACE_STATUS}
runtime_evidence_source_scan_completed${SCAN_STATUS}
ansible_runtime_evidence_evaluated${ANSIBLE_STATUS}
monitoring_runtime_evidence_evaluated${MONITORING_STATUS}
backup_recovery_runtime_evidence_evaluated${BACKUP_STATUS}
resilience_failover_runtime_evidence_evaluated${FAILOVER_STATUS}
governance_report_generated${REPORT_STATUS}
governance_decision${GOVERNANCE_DECISION}
STATUS

cat > "${VALIDATE_LOG}" <<LOG
# Governance Reporting Validation Raw Evidence

repo_dir=${REPO_DIR}
lab_dir=${LAB_DIR}

## Runtime Evidence Matrix

$(cat "${MATRIX}")

## Governance Runtime Status

$(cat "${STATUS_TSV}")
LOG

cat > "${SUMMARY}" <<SUMMARY
# Governance Reporting Runtime Summary

Overall Status: ${GOVERNANCE_DECISION}

## Validation Matrix

| Signal | Status |
|---|---|
| Governance workspace prepared | ${WORKSPACE_STATUS} |
| Runtime evidence source scan completed | ${SCAN_STATUS} |
| Ansible runtime evidence evaluated | ${ANSIBLE_STATUS} |
| Monitoring runtime evidence evaluated | ${MONITORING_STATUS} |
| Backup recovery runtime evidence evaluated | ${BACKUP_STATUS} |
| Resilience failover runtime evidence evaluated | ${FAILOVER_STATUS} |
| Governance report generated | ${REPORT_STATUS} |

## Governance Decision

| Decision Field | Value |
|---|---|
| Runtime evidence coverage | 03 / 06 / 08 / 09 |
| Aggregation result | ${GOVERNANCE_DECISION} |
| Reviewer interpretation | Phase 2 runtime evidence is suitable for governance-level reporting when all source labs report PASS. |

## Runtime Boundary

This lab validates local governance reporting by aggregating runtime evidence summaries from Phase 2 labs.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| Runtime evidence matrix | evidence/generated/raw/phase2-runtime-evidence-matrix.tsv |
| Governance status table | evidence/generated/raw/governance-runtime-status.tsv |
| Validation log | evidence/generated/raw/governance-reporting-validate.log |
| Runtime summary | evidence/generated/summary/governance-reporting-runtime-summary.md |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

cat "${SUMMARY}"

if [ "${GOVERNANCE_DECISION}" != "PASS" ]; then
  echo "[CHECK] governance reporting did not reach PASS"
  echo "[DEBUG] phase2 runtime evidence matrix:"
  cat "${MATRIX}" || true
  exit 1
fi

echo "[INFO] governance reporting validation completed"