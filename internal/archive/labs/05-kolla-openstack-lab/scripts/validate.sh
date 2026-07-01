#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

INVENTORY="${LAB_DIR}/inventory/multinode.ini"
GLOBALS="${LAB_DIR}/configs/globals.yml"
POLICY="${LAB_DIR}/configs/kolla-lab-policy.env"

RAW_PREFLIGHT="${RAW_DIR}/kolla-preflight-raw.txt"
VALIDATE_LOG="${RAW_DIR}/kolla-openstack-validate.log"
BOUNDARY_MATRIX="${RAW_DIR}/kolla-deployment-boundary-matrix.tsv"
SUMMARY="${SUMMARY_DIR}/kolla-openstack-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/kolla-openstack-execution-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] kolla openstack readiness validation started"

WORKSPACE_PREPARED="FAIL"
INVENTORY_PRESENT="FAIL"
GLOBALS_PRESENT="FAIL"
POLICY_PRESENT="FAIL"
CONTROL_GROUP_PRESENT="FAIL"
COMPUTE_GROUP_PRESENT="FAIL"
NETWORK_GROUP_PRESENT="FAIL"
REQUIRED_GLOBALS_PRESENT="FAIL"
DEPLOYMENT_BOUNDARY_DEFINED="FAIL"
REPORT_GENERATED="FAIL"

if [ -d "${LOG_DIR}" ]; then
  WORKSPACE_PREPARED="PASS"
fi

if [ -f "${INVENTORY}" ] && [ -s "${INVENTORY}" ]; then
  INVENTORY_PRESENT="PASS"
fi

if [ -f "${GLOBALS}" ] && [ -s "${GLOBALS}" ]; then
  GLOBALS_PRESENT="PASS"
fi

if [ -f "${POLICY}" ] && [ -s "${POLICY}" ]; then
  POLICY_PRESENT="PASS"
fi

if grep -Eq "^\[control\]" "${INVENTORY}"; then
  CONTROL_GROUP_PRESENT="PASS"
fi

if grep -Eq "^\[compute\]" "${INVENTORY}"; then
  COMPUTE_GROUP_PRESENT="PASS"
fi

if grep -Eq "^\[network\]" "${INVENTORY}"; then
  NETWORK_GROUP_PRESENT="PASS"
fi

GLOBALS_REQUIRED_COUNT=0

for key in kolla_base_distro kolla_install_type openstack_release network_interface neutron_external_interface; do
  if grep -Eq "^${key}:" "${GLOBALS}"; then
    GLOBALS_REQUIRED_COUNT=$((GLOBALS_REQUIRED_COUNT + 1))
  fi
done

if [ "${GLOBALS_REQUIRED_COUNT}" -ge 4 ]; then
  REQUIRED_GLOBALS_PRESENT="PASS"
fi

if [ "${INVENTORY_PRESENT}" = "PASS" ] && \
   [ "${GLOBALS_PRESENT}" = "PASS" ] && \
   [ "${CONTROL_GROUP_PRESENT}" = "PASS" ] && \
   [ "${COMPUTE_GROUP_PRESENT}" = "PASS" ] && \
   [ "${NETWORK_GROUP_PRESENT}" = "PASS" ]; then
  DEPLOYMENT_BOUNDARY_DEFINED="PASS"
fi

cat > "${BOUNDARY_MATRIX}" <<MATRIX
signalstatus
workspace_prepared${WORKSPACE_PREPARED}
inventory_present${INVENTORY_PRESENT}
globals_present${GLOBALS_PRESENT}
policy_present${POLICY_PRESENT}
control_group_present${CONTROL_GROUP_PRESENT}
compute_group_present${COMPUTE_GROUP_PRESENT}
network_group_present${NETWORK_GROUP_PRESENT}
required_globals_present${REQUIRED_GLOBALS_PRESENT}
deployment_boundary_defined${DEPLOYMENT_BOUNDARY_DEFINED}
MATRIX

cat > "${RAW_PREFLIGHT}" <<RAW
# Kolla OpenStack Readiness Raw Evidence

inventory=${INVENTORY}
globals=${GLOBALS}
policy=${POLICY}

## Inventory Groups

$(grep -E "^\[[^]]+\]" "${INVENTORY}" || true)

## Required Globals

required_keys_checked:
- kolla_base_distro
- kolla_install_type
- openstack_release
- network_interface
- neutron_external_interface

required_globals_detected=${GLOBALS_REQUIRED_COUNT}
RAW

cat > "${VALIDATE_LOG}" <<LOG
# Kolla OpenStack Validation Log

workspace_prepared=${WORKSPACE_PREPARED}
inventory_present=${INVENTORY_PRESENT}
globals_present=${GLOBALS_PRESENT}
policy_present=${POLICY_PRESENT}
control_group_present=${CONTROL_GROUP_PRESENT}
compute_group_present=${COMPUTE_GROUP_PRESENT}
network_group_present=${NETWORK_GROUP_PRESENT}
required_globals_present=${REQUIRED_GLOBALS_PRESENT}
deployment_boundary_defined=${DEPLOYMENT_BOUNDARY_DEFINED}
LOG

if [ "${WORKSPACE_PREPARED}" = "PASS" ] && \
   [ "${INVENTORY_PRESENT}" = "PASS" ] && \
   [ "${GLOBALS_PRESENT}" = "PASS" ] && \
   [ "${POLICY_PRESENT}" = "PASS" ] && \
   [ "${CONTROL_GROUP_PRESENT}" = "PASS" ] && \
   [ "${COMPUTE_GROUP_PRESENT}" = "PASS" ] && \
   [ "${NETWORK_GROUP_PRESENT}" = "PASS" ] && \
   [ "${REQUIRED_GLOBALS_PRESENT}" = "PASS" ] && \
   [ "${DEPLOYMENT_BOUNDARY_DEFINED}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Kolla OpenStack Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| OpenStack readiness workspace prepared | ${WORKSPACE_PREPARED} |
| Kolla inventory present | ${INVENTORY_PRESENT} |
| Kolla globals present | ${GLOBALS_PRESENT} |
| Lab policy present | ${POLICY_PRESENT} |
| Control group present | ${CONTROL_GROUP_PRESENT} |
| Compute group present | ${COMPUTE_GROUP_PRESENT} |
| Network group present | ${NETWORK_GROUP_PRESENT} |
| Required globals present | ${REQUIRED_GLOBALS_PRESENT} |
| Deployment boundary defined | ${DEPLOYMENT_BOUNDARY_DEFINED} |

## Deployment Readiness Decision

| Decision Field | Value |
|---|---|
| Inventory file | inventory/multinode.ini |
| Globals file | configs/globals.yml |
| Required globals detected | ${GLOBALS_REQUIRED_COUNT} |
| Deployment gate result | ${OVERALL} |

## Runtime Boundary

This lab validates OpenStack deployment readiness inputs for a Kolla-Ansible based lab boundary.

It does not perform a full OpenStack deployment. The purpose is to produce reviewer-readable readiness evidence before deployment execution.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| Boundary matrix | evidence/generated/raw/kolla-deployment-boundary-matrix.tsv |
| Preflight raw evidence | evidence/generated/raw/kolla-preflight-raw.txt |
| Validation log | evidence/generated/raw/kolla-openstack-validate.log |
| Runtime summary | evidence/generated/summary/kolla-openstack-runtime-summary.md |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] kolla openstack readiness validation did not reach PASS"
  cat "${BOUNDARY_MATRIX}" || true
  exit 1
fi

echo "[INFO] kolla openstack readiness validation completed"