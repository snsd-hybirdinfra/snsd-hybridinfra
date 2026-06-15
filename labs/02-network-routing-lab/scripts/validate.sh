#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
DATA_DIR="${LAB_DIR}/runtime-workspace/data"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

TARGETS_ENV="${LAB_DIR}/configs/network-targets.env"
ROUTE_TABLE="${DATA_DIR}/route-table.tsv"
SUBNET_BOUNDARY="${DATA_DIR}/subnet-boundary.tsv"
REACHABILITY_TARGETS="${DATA_DIR}/reachability-targets.tsv"

LOCAL_ROUTE_LOG="${RAW_DIR}/local-route-table.log"
ROUTE_MATRIX="${RAW_DIR}/network-route-validation-matrix.tsv"
REACHABILITY_MATRIX="${RAW_DIR}/network-reachability-matrix.tsv"
VALIDATE_LOG="${RAW_DIR}/network-routing-validate.log"
SUMMARY="${SUMMARY_DIR}/network-routing-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/network-routing-execution-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] network routing validation started"

WORKSPACE_PREPARED="FAIL"
CONFIG_PRESENT="FAIL"
ROUTE_TABLE_PRESENT="FAIL"
SUBNET_BOUNDARY_PRESENT="FAIL"
REACHABILITY_TARGETS_PRESENT="FAIL"
DEFAULT_ROUTE_PRESENT="FAIL"
APP_ROUTE_PRESENT="FAIL"
DATA_ROUTE_PRESENT="FAIL"
RECOVERY_ROUTE_PRESENT="FAIL"
GATEWAY_MAPPING_VALID="FAIL"
REACHABILITY_DECISION_GENERATED="FAIL"

if [ -d "${DATA_DIR}" ] && [ -d "${LOG_DIR}" ]; then
  WORKSPACE_PREPARED="PASS"
fi

if [ -f "${TARGETS_ENV}" ] && [ -s "${TARGETS_ENV}" ]; then
  CONFIG_PRESENT="PASS"
fi

if [ -f "${ROUTE_TABLE}" ] && [ -s "${ROUTE_TABLE}" ]; then
  ROUTE_TABLE_PRESENT="PASS"
fi

if [ -f "${SUBNET_BOUNDARY}" ] && [ -s "${SUBNET_BOUNDARY}" ]; then
  SUBNET_BOUNDARY_PRESENT="PASS"
fi

if [ -f "${REACHABILITY_TARGETS}" ] && [ -s "${REACHABILITY_TARGETS}" ]; then
  REACHABILITY_TARGETS_PRESENT="PASS"
fi

cp "${ROUTE_TABLE}" "${LOCAL_ROUTE_LOG}"

if awk 'NR>1 && $1=="0.0.0.0/0" && $5=="default" {found=1} END {exit found ? 0 : 1}' "${ROUTE_TABLE}"; then
  DEFAULT_ROUTE_PRESENT="PASS"
fi

if awk 'NR>1 && $1=="10.10.10.0/24" && $2=="192.168.10.1" && $3=="eth0" {found=1} END {exit found ? 0 : 1}' "${ROUTE_TABLE}"; then
  APP_ROUTE_PRESENT="PASS"
fi

if awk 'NR>1 && $1=="10.10.20.0/24" && $2=="192.168.20.1" && $3=="eth1" {found=1} END {exit found ? 0 : 1}' "${ROUTE_TABLE}"; then
  DATA_ROUTE_PRESENT="PASS"
fi

if awk 'NR>1 && $1=="10.10.30.0/24" && $2=="192.168.30.1" && $3=="eth2" {found=1} END {exit found ? 0 : 1}' "${ROUTE_TABLE}"; then
  RECOVERY_ROUTE_PRESENT="PASS"
fi

GATEWAY_MATCH_COUNT="$(awk '
  NR==FNR && NR>1 {
    gateway[$1]=$3
    iface[$1]=$4
    next
  }
  NR>1 {
    subnet=$1
    if (gateway[subnet] == $2 && iface[subnet] == $3) {
      count++
    }
  }
  END {print count+0}
' "${SUBNET_BOUNDARY}" "${ROUTE_TABLE}")"

if [ "${GATEWAY_MATCH_COUNT}" -ge 3 ]; then
  GATEWAY_MAPPING_VALID="PASS"
fi

{
  printf "target_ip\texpected_subnet\texpected_gateway\texpected_result\tdecision\n"
  awk '
    NR==FNR && NR>1 {
      route_gateway[$1]=$2
      next
    }
    NR>1 {
      target=$1
      subnet=$2
      gateway=$3
      expected=$4
      decision="blocked"
      if (route_gateway[subnet] == gateway && expected == "reachable") {
        decision="reachable"
      }
      printf "%s\t%s\t%s\t%s\t%s\n", target, subnet, gateway, expected, decision
    }
  ' "${ROUTE_TABLE}" "${REACHABILITY_TARGETS}"
} > "${REACHABILITY_MATRIX}"

REACHABLE_COUNT="$(awk 'NR>1 && $5=="reachable" {count++} END {print count+0}' "${REACHABILITY_MATRIX}")"

if [ "${REACHABLE_COUNT}" -ge 3 ]; then
  REACHABILITY_DECISION_GENERATED="PASS"
fi

{
  printf "signal\tstatus\n"
  printf "workspace_prepared\t%s\n" "${WORKSPACE_PREPARED}"
  printf "config_present\t%s\n" "${CONFIG_PRESENT}"
  printf "route_table_present\t%s\n" "${ROUTE_TABLE_PRESENT}"
  printf "subnet_boundary_present\t%s\n" "${SUBNET_BOUNDARY_PRESENT}"
  printf "reachability_targets_present\t%s\n" "${REACHABILITY_TARGETS_PRESENT}"
  printf "default_route_present\t%s\n" "${DEFAULT_ROUTE_PRESENT}"
  printf "app_route_present\t%s\n" "${APP_ROUTE_PRESENT}"
  printf "data_route_present\t%s\n" "${DATA_ROUTE_PRESENT}"
  printf "recovery_route_present\t%s\n" "${RECOVERY_ROUTE_PRESENT}"
  printf "gateway_mapping_valid\t%s\n" "${GATEWAY_MAPPING_VALID}"
  printf "reachability_decision_generated\t%s\n" "${REACHABILITY_DECISION_GENERATED}"
} > "${ROUTE_MATRIX}"

cat > "${VALIDATE_LOG}" <<LOG
# Network Routing Validation Log

targets_env=${TARGETS_ENV}
route_table=${ROUTE_TABLE}
subnet_boundary=${SUBNET_BOUNDARY}
reachability_targets=${REACHABILITY_TARGETS}

gateway_match_count=${GATEWAY_MATCH_COUNT}
reachable_count=${REACHABLE_COUNT}

$(cat "${ROUTE_MATRIX}")
LOG

if [ "${WORKSPACE_PREPARED}" = "PASS" ] && \
   [ "${CONFIG_PRESENT}" = "PASS" ] && \
   [ "${ROUTE_TABLE_PRESENT}" = "PASS" ] && \
   [ "${SUBNET_BOUNDARY_PRESENT}" = "PASS" ] && \
   [ "${REACHABILITY_TARGETS_PRESENT}" = "PASS" ] && \
   [ "${DEFAULT_ROUTE_PRESENT}" = "PASS" ] && \
   [ "${APP_ROUTE_PRESENT}" = "PASS" ] && \
   [ "${DATA_ROUTE_PRESENT}" = "PASS" ] && \
   [ "${RECOVERY_ROUTE_PRESENT}" = "PASS" ] && \
   [ "${GATEWAY_MAPPING_VALID}" = "PASS" ] && \
   [ "${REACHABILITY_DECISION_GENERATED}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Network Routing Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Network routing workspace prepared | ${WORKSPACE_PREPARED} |
| Network target config present | ${CONFIG_PRESENT} |
| Route table present | ${ROUTE_TABLE_PRESENT} |
| Subnet boundary present | ${SUBNET_BOUNDARY_PRESENT} |
| Reachability targets present | ${REACHABILITY_TARGETS_PRESENT} |
| Default route present | ${DEFAULT_ROUTE_PRESENT} |
| App segment route present | ${APP_ROUTE_PRESENT} |
| Data segment route present | ${DATA_ROUTE_PRESENT} |
| Recovery segment route present | ${RECOVERY_ROUTE_PRESENT} |
| Gateway mapping valid | ${GATEWAY_MAPPING_VALID} |
| Reachability decision generated | ${REACHABILITY_DECISION_GENERATED} |

## Routing Decision

| Decision Field | Value |
|---|---|
| App segment | 10.10.10.0/24 via 192.168.10.1 |
| Data segment | 10.10.20.0/24 via 192.168.20.1 |
| Recovery segment | 10.10.30.0/24 via 192.168.30.1 |
| Default route | 0.0.0.0/0 via 192.168.10.254 |
| Reachable target count | ${REACHABLE_COUNT} |
| Runtime validation result | ${OVERALL} |

## Runtime Boundary

This lab validates deterministic routing-state and reachability evidence without creating privileged network namespaces.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| Local route table | evidence/generated/raw/local-route-table.log |
| Route validation matrix | evidence/generated/raw/network-route-validation-matrix.tsv |
| Reachability matrix | evidence/generated/raw/network-reachability-matrix.tsv |
| Validation log | evidence/generated/raw/network-routing-validate.log |
| Runtime summary | evidence/generated/summary/network-routing-runtime-summary.md |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] network routing validation did not reach PASS"
  cat "${ROUTE_MATRIX}" || true
  exit 1
fi

echo "[INFO] network routing validation completed"