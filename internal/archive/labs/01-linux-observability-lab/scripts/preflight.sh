#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

mkdir -p "${RAW_DIR}" "${LOG_DIR}"

echo "[INFO] linux observability preflight started"

OS_RELEASE_STATUS="FAIL"
PROC_CPUINFO_STATUS="FAIL"
PROC_MEMINFO_STATUS="FAIL"
DF_STATUS="FAIL"
PS_STATUS="FAIL"

[ -f /etc/os-release ] && OS_RELEASE_STATUS="PASS"
[ -f /proc/cpuinfo ] && PROC_CPUINFO_STATUS="PASS"
[ -f /proc/meminfo ] && PROC_MEMINFO_STATUS="PASS"

if df -h >/dev/null 2>&1; then
  DF_STATUS="PASS"
fi

if ps -eo pid,comm >/dev/null 2>&1; then
  PS_STATUS="PASS"
fi

cat > "${RAW_DIR}/linux-observability-preflight.log" <<PREFLIGHT
os_release_available=${OS_RELEASE_STATUS}
proc_cpuinfo_available=${PROC_CPUINFO_STATUS}
proc_meminfo_available=${PROC_MEMINFO_STATUS}
df_available=${DF_STATUS}
ps_available=${PS_STATUS}
PREFLIGHT

cat "${RAW_DIR}/linux-observability-preflight.log"

if [ "${OS_RELEASE_STATUS}" != "PASS" ] || \
   [ "${PROC_CPUINFO_STATUS}" != "PASS" ] || \
   [ "${PROC_MEMINFO_STATUS}" != "PASS" ] || \
   [ "${DF_STATUS}" != "PASS" ] || \
   [ "${PS_STATUS}" != "PASS" ]; then
  echo "[CHECK] linux observability preflight has missing signals"
  exit 1
fi

echo "[INFO] linux observability preflight completed"