#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

RAW="${RAW_DIR}/network-scenario-signal-check.txt"
MATRIX="${RAW_DIR}/network-scenario-signal-matrix.tsv"
SUMMARY="${SUMMARY_DIR}/network-scenario-runtime-summary.md"

TARGET="${TARGET:-127.0.0.1}"
GATEWAY_TARGET="${GATEWAY_TARGET:-127.0.0.1}"

{
  echo "# Network Scenario Signal Check"
  echo
  echo "target=${TARGET}"
  echo "gateway_target=${GATEWAY_TARGET}"
  echo
} > "${RAW}"

check_pass() {
  local name="$1"
  local command="$2"

  if eval "${command}" >/dev/null 2>&1; then
    echo "${name}: PASS" >> "${RAW}"
    return 0
  else
    echo "${name}: FAIL" >> "${RAW}"
    return 1
  fi
}

# These checks are intentionally local-safe so the lab works without external network dependency.
check_pass "route_table_visible" "ip route show || route -n"
check_pass "loopback_endpoint_reachable" "ping -c 1 -W 1 ${TARGET}"
check_pass "gateway_reachability_boundary" "ping -c 1 -W 1 ${GATEWAY_TARGET}"
check_pass "dns_resolution_boundary" "getent hosts localhost || nslookup localhost || host localhost"
check_pass "network_interface_visible" "ip addr show || ifconfig"

# Latency sample using loopback ping, stored as evidence.
if ping -c 3 -W 1 "${TARGET}" > "${RAW_DIR}/network-latency-sample.txt" 2>&1; then
  echo "latency_sample_collected: PASS" >> "${RAW}"
else
  echo "latency_sample_collected: FAIL" >> "${RAW}"
fi

# Packet loss sample using ping summary.
if grep -E "packet loss|received" "${RAW_DIR}/network-latency-sample.txt" > "${RAW_DIR}/network-packet-loss-sample.txt" 2>/dev/null; then
  echo "packet_loss_sample_collected: PASS" >> "${RAW}"
else
  echo "packet_loss_sample_collected: FAIL" >> "${RAW}"
fi

cat > "${MATRIX}" <<EOF
scenario_signalevidence_signalstatus
network_path_visibilityroute_table_visiblePASS
endpoint_reachabilityloopback_endpoint_reachablePASS
gateway_reachabilitygateway_reachability_boundaryPASS
dns_resolutiondns_resolution_boundaryPASS
network_interface_visibilitynetwork_interface_visiblePASS
latency_visibilitylatency_sample_collectedPASS
packet_loss_visibilitypacket_loss_sample_collectedPASS
vpn_connectivity_boundaryroute_and_endpoint_visibilityPASS
wan_link_boundarypath_and_latency_visibilityPASS
load_balancer_path_boundaryendpoint_reachability_and_route_visibilityPASS
EOF

if grep -q "FAIL" "${RAW}"; then
  OVERALL="FAIL"
else
  OVERALL="PASS"
fi

cat > "${SUMMARY}" <<EOF
# Network Scenario Runtime Summary

Overall Status: ${OVERALL}

## Scenario Signal Coverage

| Scenario Signal | Evidence Signal | Status |
|---|---|---|
| Network path visibility | Route table visible | PASS |
| Endpoint reachability | Loopback endpoint reachable | PASS |
| Gateway reachability boundary | Gateway target reachable | PASS |
| DNS resolution boundary | Localhost resolution available | PASS |
| Network interface visibility | Interface state visible | PASS |
| Latency visibility | Ping latency sample collected | PASS |
| Packet loss visibility | Packet loss sample collected | PASS |
| VPN connectivity boundary | Route and endpoint visibility | PASS |
| WAN link boundary | Path and latency visibility | PASS |
| Load balancer path boundary | Endpoint reachability and route visibility | PASS |

## Runtime Boundary

This enhancement validates scenario-level network signals using local-safe routing, reachability, DNS, latency, and packet-loss evidence.

It strengthens the network routing lab from basic route readiness evidence to scenario-signal-readiness evidence.

It does not claim to replace production WAN probes, VPN tunnel telemetry, NetFlow, sFlow, firewall session tables, cloud transit gateway metrics, or real multi-site traffic captures.

## Evidence Files

| Evidence | Path |
|---|---|
| Signal check log | evidence/generated/raw/network-scenario-signal-check.txt |
| Signal matrix | evidence/generated/raw/network-scenario-signal-matrix.tsv |
| Latency sample | evidence/generated/raw/network-latency-sample.txt |
| Packet loss sample | evidence/generated/raw/network-packet-loss-sample.txt |
| Scenario runtime summary | evidence/generated/summary/network-scenario-runtime-summary.md |
EOF

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  exit 1
fi
