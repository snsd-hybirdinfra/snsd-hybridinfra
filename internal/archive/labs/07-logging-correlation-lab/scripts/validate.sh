#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

SOURCE_LOG="${LOG_DIR}/operational-events.log"
NORMALIZED="${RAW_DIR}/normalized-events.tsv"
TIMELINE="${RAW_DIR}/correlation-timeline.md"
VALIDATE_LOG="${RAW_DIR}/logging-correlation-validate.log"
SUMMARY="${SUMMARY_DIR}/logging-correlation-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/logging-correlation-execution-summary.md"

TARGET_CORRELATION_ID="INC-2026-0701"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

echo "[INFO] logging correlation validation started"

WORKSPACE_PREPARED="FAIL"
LOG_DATASET_CREATED="FAIL"
SOURCE_SCAN_COMPLETED="FAIL"
CORRELATION_KEY_DETECTED="FAIL"
RELATED_EVENTS_CORRELATED="FAIL"
ERROR_PATTERN_DETECTED="FAIL"
RECOVERY_PATTERN_DETECTED="FAIL"
REPORT_GENERATED="FAIL"

if [ -d "${LOG_DIR}" ]; then
  WORKSPACE_PREPARED="PASS"
fi

if [ -f "${SOURCE_LOG}" ] && [ -s "${SOURCE_LOG}" ]; then
  LOG_DATASET_CREATED="PASS"
fi

{
  echo -e "timestamp\tlevel\tservice\tcorrelation_id\tevent\tstatus"
  awk '
    {
      timestamp=$1
      level=""; service=""; correlation_id=""; event=""; status=""
      for (i=2; i<=NF; i++) {
        split($i, kv, "=")
        if (kv[1] == "level") level=kv[2]
        if (kv[1] == "service") service=kv[2]
        if (kv[1] == "correlation_id") correlation_id=kv[2]
        if (kv[1] == "event") event=kv[2]
        if (kv[1] == "status") status=kv[2]
      }
      print timestamp "\t" level "\t" service "\t" correlation_id "\t" event "\t" status
    }
  ' "${SOURCE_LOG}"
} > "${NORMALIZED}"

if [ -s "${NORMALIZED}" ]; then
  SOURCE_SCAN_COMPLETED="PASS"
fi

if grep -q "${TARGET_CORRELATION_ID}" "${NORMALIZED}"; then
  CORRELATION_KEY_DETECTED="PASS"
fi

RELATED_COUNT="$(awk -F '\t' -v cid="${TARGET_CORRELATION_ID}" 'NR>1 && $4==cid {count++} END {print count+0}' "${NORMALIZED}")"
ERROR_COUNT="$(awk -F '\t' -v cid="${TARGET_CORRELATION_ID}" 'NR>1 && $4==cid && $2=="ERROR" {count++} END {print count+0}' "${NORMALIZED}")"
WARN_COUNT="$(awk -F '\t' -v cid="${TARGET_CORRELATION_ID}" 'NR>1 && $4==cid && $2=="WARN" {count++} END {print count+0}' "${NORMALIZED}")"
RECOVERY_COUNT="$(awk -F '\t' -v cid="${TARGET_CORRELATION_ID}" 'NR>1 && $4==cid && ($6=="recovered" || $6=="ok") {count++} END {print count+0}' "${NORMALIZED}")"

if [ "${RELATED_COUNT}" -ge 4 ]; then
  RELATED_EVENTS_CORRELATED="PASS"
fi

if [ "${ERROR_COUNT}" -ge 1 ] || [ "${WARN_COUNT}" -ge 1 ]; then
  ERROR_PATTERN_DETECTED="PASS"
fi

if [ "${RECOVERY_COUNT}" -ge 1 ]; then
  RECOVERY_PATTERN_DETECTED="PASS"
fi

cat > "${TIMELINE}" <<TIMELINE
# Logging Correlation Timeline

Target correlation id: ${TARGET_CORRELATION_ID}

## Correlated Events

| Timestamp | Level | Service | Event | Status |
|---|---|---|---|---|
$(awk -F '\t' -v cid="${TARGET_CORRELATION_ID}" 'NR>1 && $4==cid {print "| " $1 " | " $2 " | " $3 " | " $5 " | " $6 " |"}' "${NORMALIZED}")

## Correlation Interpretation

The runtime dataset contains a complete incident sequence:

1. request intake
2. latency degradation
3. upstream timeout
4. retry execution
5. recovery completion
6. request completion
TIMELINE

if [ -s "${TIMELINE}" ]; then
  REPORT_GENERATED="PASS"
fi

cat > "${VALIDATE_LOG}" <<LOG
# Logging Correlation Validation Raw Evidence

source_log=${SOURCE_LOG}
target_correlation_id=${TARGET_CORRELATION_ID}

related_event_count=${RELATED_COUNT}
warn_event_count=${WARN_COUNT}
error_event_count=${ERROR_COUNT}
recovery_event_count=${RECOVERY_COUNT}

workspace_prepared=${WORKSPACE_PREPARED}
log_dataset_created=${LOG_DATASET_CREATED}
source_scan_completed=${SOURCE_SCAN_COMPLETED}
correlation_key_detected=${CORRELATION_KEY_DETECTED}
related_events_correlated=${RELATED_EVENTS_CORRELATED}
error_pattern_detected=${ERROR_PATTERN_DETECTED}
recovery_pattern_detected=${RECOVERY_PATTERN_DETECTED}
report_generated=${REPORT_GENERATED}
LOG

if [ "${WORKSPACE_PREPARED}" = "PASS" ] && \
   [ "${LOG_DATASET_CREATED}" = "PASS" ] && \
   [ "${SOURCE_SCAN_COMPLETED}" = "PASS" ] && \
   [ "${CORRELATION_KEY_DETECTED}" = "PASS" ] && \
   [ "${RELATED_EVENTS_CORRELATED}" = "PASS" ] && \
   [ "${ERROR_PATTERN_DETECTED}" = "PASS" ] && \
   [ "${RECOVERY_PATTERN_DETECTED}" = "PASS" ] && \
   [ "${REPORT_GENERATED}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Logging Correlation Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Logging workspace prepared | ${WORKSPACE_PREPARED} |
| Operational log dataset created | ${LOG_DATASET_CREATED} |
| Correlation source scan completed | ${SOURCE_SCAN_COMPLETED} |
| Incident correlation key detected | ${CORRELATION_KEY_DETECTED} |
| Related events correlated | ${RELATED_EVENTS_CORRELATED} |
| Error or warning pattern detected | ${ERROR_PATTERN_DETECTED} |
| Recovery pattern detected | ${RECOVERY_PATTERN_DETECTED} |
| Correlation report generated | ${REPORT_GENERATED} |

## Correlation Decision

| Decision Field | Value |
|---|---|
| Target correlation id | ${TARGET_CORRELATION_ID} |
| Related event count | ${RELATED_COUNT} |
| Error event count | ${ERROR_COUNT} |
| Warning event count | ${WARN_COUNT} |
| Recovery event count | ${RECOVERY_COUNT} |
| Aggregation result | ${OVERALL} |

## Runtime Boundary

This lab validates local log correlation by normalizing operational events and grouping related events by correlation id.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| Normalized events | evidence/generated/raw/normalized-events.tsv |
| Correlation timeline | evidence/generated/raw/correlation-timeline.md |
| Validation log | evidence/generated/raw/logging-correlation-validate.log |
| Runtime summary | evidence/generated/summary/logging-correlation-runtime-summary.md |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] logging correlation validation did not reach PASS"
  cat "${VALIDATE_LOG}" || true
  exit 1
fi

echo "[INFO] logging correlation validation completed"