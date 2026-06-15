#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
PROCESSED_DIR="${LAB_DIR}/evidence/generated/processed"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

OS_RELEASE_RAW="${RAW_DIR}/linux-os-release.log"
CPU_RAW="${RAW_DIR}/linux-cpuinfo.log"
MEM_RAW="${RAW_DIR}/linux-meminfo.log"
DISK_RAW="${RAW_DIR}/linux-disk-usage.log"
PROCESS_RAW="${RAW_DIR}/linux-process-snapshot.log"
SERVICE_RAW="${RAW_DIR}/linux-service-like-signals.log"
VALIDATE_LOG="${RAW_DIR}/linux-observability-validate.log"

PROCESSED_SUMMARY="${PROCESSED_DIR}/linux-observability-processed-summary.md"
SUMMARY="${SUMMARY_DIR}/linux-observability-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/linux-observability-execution-summary.md"

mkdir -p "${RAW_DIR}" "${PROCESSED_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] linux observability validation started"

WORKSPACE_PREPARED="FAIL"
OS_SIGNAL_COLLECTED="FAIL"
CPU_SIGNAL_COLLECTED="FAIL"
MEMORY_SIGNAL_COLLECTED="FAIL"
DISK_SIGNAL_COLLECTED="FAIL"
PROCESS_SIGNAL_COLLECTED="FAIL"
SERVICE_SIGNAL_COLLECTED="FAIL"
REPORT_GENERATED="FAIL"

if [ -d "${RAW_DIR}" ] && [ -d "${SUMMARY_DIR}" ] && [ -d "${LOG_DIR}" ]; then
  WORKSPACE_PREPARED="PASS"
fi

if [ -f /etc/os-release ]; then
  cat /etc/os-release > "${OS_RELEASE_RAW}"
  OS_SIGNAL_COLLECTED="PASS"
else
  echo "os_release=unavailable" > "${OS_RELEASE_RAW}"
fi

if [ -f /proc/cpuinfo ]; then
  head -n 80 /proc/cpuinfo > "${CPU_RAW}"
  CPU_SIGNAL_COLLECTED="PASS"
else
  echo "cpuinfo=unavailable" > "${CPU_RAW}"
fi

if [ -f /proc/meminfo ]; then
  head -n 40 /proc/meminfo > "${MEM_RAW}"
  MEMORY_SIGNAL_COLLECTED="PASS"
else
  echo "meminfo=unavailable" > "${MEM_RAW}"
fi

if df -h > "${DISK_RAW}" 2>&1; then
  DISK_SIGNAL_COLLECTED="PASS"
fi

if ps -eo pid,ppid,comm,%cpu,%mem --sort=-%cpu | head -n 25 > "${PROCESS_RAW}" 2>&1; then
  PROCESS_SIGNAL_COLLECTED="PASS"
fi

{
  echo "service_like_signalstatus"
  if command -v systemctl >/dev/null 2>&1; then
    echo "systemctl_availablePASS"
    systemctl list-units --type=service --no-pager --no-legend 2>/dev/null | head -n 20 || true
  else
    echo "systemctl_availableCHECK"
  fi

  if pgrep -f "init|systemd|bash|sh" >/dev/null 2>&1; then
    echo "baseline_process_signalPASS"
  else
    echo "baseline_process_signalCHECK"
  fi
} > "${SERVICE_RAW}"

if [ -s "${SERVICE_RAW}" ]; then
  SERVICE_SIGNAL_COLLECTED="PASS"
fi

CPU_MODEL="$(awk -F ': ' '/model name/ {print $2; exit}' "${CPU_RAW}" 2>/dev/null || true)"
CPU_COUNT="$(grep -c '^processor' "${CPU_RAW}" 2>/dev/null || echo 0)"
MEM_TOTAL="$(awk '/MemTotal/ {print $2 " " $3; exit}' "${MEM_RAW}" 2>/dev/null || true)"
ROOT_USAGE="$(awk '$6=="/" {print $5; exit}' "${DISK_RAW}" 2>/dev/null || true)"
TOP_PROCESS="$(awk 'NR==2 {print $3; exit}' "${PROCESS_RAW}" 2>/dev/null || true)"

[ -z "${CPU_MODEL}" ] && CPU_MODEL="unknown"
[ -z "${MEM_TOTAL}" ] && MEM_TOTAL="unknown"
[ -z "${ROOT_USAGE}" ] && ROOT_USAGE="unknown"
[ -z "${TOP_PROCESS}" ] && TOP_PROCESS="unknown"

cat > "${PROCESSED_SUMMARY}" <<PROCESSED
# Linux Observability Processed Summary

| Field | Value |
|---|---|
| CPU model | ${CPU_MODEL} |
| CPU processor entries | ${CPU_COUNT} |
| Memory total | ${MEM_TOTAL} |
| Root filesystem usage | ${ROOT_USAGE} |
| Top observed process | ${TOP_PROCESS} |
PROCESSED

cat > "${VALIDATE_LOG}" <<LOG
# Linux Observability Validation Log

workspace_prepared=${WORKSPACE_PREPARED}
os_signal_collected=${OS_SIGNAL_COLLECTED}
cpu_signal_collected=${CPU_SIGNAL_COLLECTED}
memory_signal_collected=${MEMORY_SIGNAL_COLLECTED}
disk_signal_collected=${DISK_SIGNAL_COLLECTED}
process_signal_collected=${PROCESS_SIGNAL_COLLECTED}
service_signal_collected=${SERVICE_SIGNAL_COLLECTED}

cpu_model=${CPU_MODEL}
cpu_count=${CPU_COUNT}
memory_total=${MEM_TOTAL}
root_usage=${ROOT_USAGE}
top_process=${TOP_PROCESS}
LOG

if [ "${WORKSPACE_PREPARED}" = "PASS" ] && \
   [ "${OS_SIGNAL_COLLECTED}" = "PASS" ] && \
   [ "${CPU_SIGNAL_COLLECTED}" = "PASS" ] && \
   [ "${MEMORY_SIGNAL_COLLECTED}" = "PASS" ] && \
   [ "${DISK_SIGNAL_COLLECTED}" = "PASS" ] && \
   [ "${PROCESS_SIGNAL_COLLECTED}" = "PASS" ] && \
   [ "${SERVICE_SIGNAL_COLLECTED}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Linux Observability Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Linux observability workspace prepared | ${WORKSPACE_PREPARED} |
| OS release signal collected | ${OS_SIGNAL_COLLECTED} |
| CPU signal collected | ${CPU_SIGNAL_COLLECTED} |
| Memory signal collected | ${MEMORY_SIGNAL_COLLECTED} |
| Disk usage signal collected | ${DISK_SIGNAL_COLLECTED} |
| Process snapshot collected | ${PROCESS_SIGNAL_COLLECTED} |
| Service-like signal collected | ${SERVICE_SIGNAL_COLLECTED} |

## Observability Decision

| Decision Field | Value |
|---|---|
| CPU model | ${CPU_MODEL} |
| CPU processor entries | ${CPU_COUNT} |
| Memory total | ${MEM_TOTAL} |
| Root filesystem usage | ${ROOT_USAGE} |
| Top observed process | ${TOP_PROCESS} |
| Runtime validation result | ${OVERALL} |

## Runtime Boundary

This lab validates local Linux host observability signals without requiring privileged host changes.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| OS release raw signal | evidence/generated/raw/linux-os-release.log |
| CPU raw signal | evidence/generated/raw/linux-cpuinfo.log |
| Memory raw signal | evidence/generated/raw/linux-meminfo.log |
| Disk usage raw signal | evidence/generated/raw/linux-disk-usage.log |
| Process snapshot | evidence/generated/raw/linux-process-snapshot.log |
| Service-like signals | evidence/generated/raw/linux-service-like-signals.log |
| Validation log | evidence/generated/raw/linux-observability-validate.log |
| Processed summary | evidence/generated/processed/linux-observability-processed-summary.md |
| Runtime summary | evidence/generated/summary/linux-observability-runtime-summary.md |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

REPORT_GENERATED="PASS"

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] linux observability validation did not reach PASS"
  cat "${VALIDATE_LOG}" || true
  exit 1
fi

echo "[INFO] linux observability validation completed"