#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"
DATA_DIR="${RUNTIME_DIR}/data"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}" "${DATA_DIR}"

echo "[INFO] network routing setup started"

{
  printf "destination\tgateway\tinterface\tmetric\tstate\n"
  printf "10.10.10.0/24\t192.168.10.1\teth0\t100\tactive\n"
  printf "10.10.20.0/24\t192.168.20.1\teth1\t100\tactive\n"
  printf "10.10.30.0/24\t192.168.30.1\teth2\t200\tstandby\n"
  printf "0.0.0.0/0\t192.168.10.254\teth0\t500\tdefault\n"
} > "${DATA_DIR}/route-table.tsv"

{
  printf "subnet\trole\texpected_gateway\texpected_interface\n"
  printf "10.10.10.0/24\tapp-segment\t192.168.10.1\teth0\n"
  printf "10.10.20.0/24\tdata-segment\t192.168.20.1\teth1\n"
  printf "10.10.30.0/24\trecovery-segment\t192.168.30.1\teth2\n"
} > "${DATA_DIR}/subnet-boundary.tsv"

{
  printf "target_ip\texpected_subnet\texpected_gateway\texpected_result\n"
  printf "10.10.10.25\t10.10.10.0/24\t192.168.10.1\treachable\n"
  printf "10.10.20.25\t10.10.20.0/24\t192.168.20.1\treachable\n"
  printf "10.10.30.25\t10.10.30.0/24\t192.168.30.1\treachable\n"
} > "${DATA_DIR}/reachability-targets.tsv"

cat > "${LOG_DIR}/setup.log" <<SETUP
SNSD_NETWORK_ROUTING_SETUP=ready
LAB=02-network-routing-lab
RUNTIME=local-routing-readiness-validation
ROUTE_TABLE=${DATA_DIR}/route-table.tsv
SUBNET_BOUNDARY=${DATA_DIR}/subnet-boundary.tsv
REACHABILITY_TARGETS=${DATA_DIR}/reachability-targets.tsv
SETUP

cp "${LOG_DIR}/setup.log" "${RAW_DIR}/network-routing-setup.log"

echo "[INFO] network routing setup completed"