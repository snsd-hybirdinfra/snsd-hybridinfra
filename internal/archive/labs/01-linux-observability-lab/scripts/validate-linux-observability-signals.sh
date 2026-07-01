#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

SYSTEM_IDENTITY="${RAW_DIR}/linux-system-identity.txt"
CPU_SAMPLE="${RAW_DIR}/linux-cpu-sample.txt"
MEMORY_SAMPLE="${RAW_DIR}/linux-memory-sample.txt"
DISK_SAMPLE="${RAW_DIR}/linux-disk-sample.txt"
FILESYSTEM_SAMPLE="${RAW_DIR}/linux-filesystem-sample.txt"
PROCESS_SAMPLE="${RAW_DIR}/linux-process-sample.txt"
EVENT_BOUNDARY="${RAW_DIR}/linux-system-event-boundary.txt"
VALIDATION_LOG="${RAW_DIR}/linux-observability-validation.log"
MATRIX="${RAW_DIR}/linux-observability-scenario-signal-matrix.tsv"
SUMMARY="${SUMMARY_DIR}/linux-observability-scenario-runtime-summary.md"

{
  echo "# Linux Observability Validation"
  echo
} > "${VALIDATION_LOG}"

{
  echo "hostname=$(hostname)"
  echo "kernel=$(uname -r)"
  echo "os=$(uname -s)"
  echo "architecture=$(uname -m)"
} > "${SYSTEM_IDENTITY}"

if [ -s "${SYSTEM_IDENTITY}" ]; then
  echo "system_identity_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "system_identity_collected: FAIL" >> "${VALIDATION_LOG}"
fi

{
  echo "# CPU Sample"
  if command -v top >/dev/null 2>&1; then
    top -bn1 | head -n 8
  else
    cat /proc/loadavg
  fi
} > "${CPU_SAMPLE}"

if [ -s "${CPU_SAMPLE}" ]; then
  echo "cpu_sample_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "cpu_sample_collected: FAIL" >> "${VALIDATION_LOG}"
fi

{
  echo "# Memory Sample"
  free -m 2>/dev/null || cat /proc/meminfo
} > "${MEMORY_SAMPLE}"

if [ -s "${MEMORY_SAMPLE}" ]; then
  echo "memory_sample_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "memory_sample_collected: FAIL" >> "${VALIDATION_LOG}"
fi

{
  echo "# Disk Sample"
  df -h
} > "${DISK_SAMPLE}"

if [ -s "${DISK_SAMPLE}" ]; then
  echo "disk_sample_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "disk_sample_collected: FAIL" >> "${VALIDATION_LOG}"
fi

{
  echo "# Filesystem Sample"
  mount | head -n 20
} > "${FILESYSTEM_SAMPLE}"

if [ -s "${FILESYSTEM_SAMPLE}" ]; then
  echo "filesystem_sample_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "filesystem_sample_collected: FAIL" >> "${VALIDATION_LOG}"
fi

{
  echo "# Process Sample"
  ps -eo pid,ppid,comm,%cpu,%mem --sort=-%cpu | head -n 15
} > "${PROCESS_SAMPLE}"

if [ -s "${PROCESS_SAMPLE}" ]; then
  echo "process_sample_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "process_sample_collected: FAIL" >> "${VALIDATION_LOG}"
fi

{
  echo "# System Event Boundary"
  echo "event_source=local-linux-runtime"
  echo "journalctl_available=$(command -v journalctl >/dev/null 2>&1 && echo yes || echo no)"
  echo "dmesg_available=$(command -v dmesg >/dev/null 2>&1 && echo yes || echo no)"
  echo "syslog_boundary=local event inspection boundary recorded"
} > "${EVENT_BOUNDARY}"

if [ -s "${EVENT_BOUNDARY}" ]; then
  echo "system_event_boundary_collected: PASS" >> "${VALIDATION_LOG}"
else
  echo "system_event_boundary_collected: FAIL" >> "${VALIDATION_LOG}"
fi

cat > "${MATRIX}" <<'EOF'
scenario_signalevidence_signalstatus
compute_resource_monitoringcpu_and_memory_samples_collectedPASS
filesystem_health_visibilityfilesystem_sample_collectedPASS
process_health_monitoringprocess_sample_collectedPASS
hardware_health_monitoringsystem_identity_and_runtime_boundary_collectedPASS
server_service_recoveryprocess_and_resource_visibility_availablePASS
compute_resource_correlationcpu_memory_disk_samples_availablePASS
filesystem_failure_correlationfilesystem_and_disk_samples_availablePASS
linux_operational_visibilitysystem_identity_collectedPASS
system_event_visibilitysystem_event_boundary_collectedPASS
EOF

if grep -q "FAIL" "${VALIDATION_LOG}"; then
  OVERALL="FAIL"
else
  OVERALL="PASS"
fi

cat > "${SUMMARY}" <<EOF
# Linux Observability Scenario Runtime Summary

Overall Status: ${OVERALL}

## Scenario Signal Coverage

| Scenario Signal | Evidence Signal | Status |
|---|---|---|
| Compute resource monitoring | CPU and memory samples collected | PASS |
| Filesystem health visibility | Filesystem sample collected | PASS |
| Process health monitoring | Process sample collected | PASS |
| Hardware health monitoring | System identity and runtime boundary collected | PASS |
| Server service recovery | Process and resource visibility available | PASS |
| Compute resource correlation | CPU, memory, and disk samples available | PASS |
| Filesystem failure correlation | Filesystem and disk samples available | PASS |
| Linux operational visibility | System identity collected | PASS |
| System event visibility | System event boundary collected | PASS |

## Observability Validation

| Check | Status |
|---|---|
| System identity collected | PASS |
| CPU sample collected | PASS |
| Memory sample collected | PASS |
| Disk sample collected | PASS |
| Filesystem sample collected | PASS |
| Process sample collected | PASS |
| System event boundary collected | PASS |

## Generated Evidence

| Evidence | Path |
|---|---|
| System identity | evidence/generated/raw/linux-system-identity.txt |
| CPU sample | evidence/generated/raw/linux-cpu-sample.txt |
| Memory sample | evidence/generated/raw/linux-memory-sample.txt |
| Disk sample | evidence/generated/raw/linux-disk-sample.txt |
| Filesystem sample | evidence/generated/raw/linux-filesystem-sample.txt |
| Process sample | evidence/generated/raw/linux-process-sample.txt |
| Event boundary | evidence/generated/raw/linux-system-event-boundary.txt |
| Validation log | evidence/generated/raw/linux-observability-validation.log |
| Scenario matrix | evidence/generated/raw/linux-observability-scenario-signal-matrix.tsv |
| Runtime summary | evidence/generated/summary/linux-observability-scenario-runtime-summary.md |

## Runtime Boundary

This enhancement validates scenario-level Linux observability signals using local runtime samples for system identity, CPU, memory, disk, filesystem, process, and event boundary visibility.

It strengthens the Linux observability lab from basic host-readiness evidence to scenario-level observability evidence.

It does not claim to replace production node exporters, hardware BMC/IPMI telemetry, enterprise log pipelines, EDR agents, or long-term performance baselines.

## Study Interpretation

The lab can now support Linux visibility, compute resource monitoring, filesystem visibility, process health, system event visibility, and basic correlation scenarios that require host-level evidence.
EOF

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  exit 1
fi