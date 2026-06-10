#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="05-kolla-openstack-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate Kolla-Ansible configuration boundary"
echo "- prepare OpenStack service validation boundary"
echo "- prepare API endpoint validation boundary"
echo "- prepare compute and network validation boundary"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
