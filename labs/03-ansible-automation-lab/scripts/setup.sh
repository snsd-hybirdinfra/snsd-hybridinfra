#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="03-ansible-automation-lab"

echo "[INFO] setup started: ${LAB_NAME}"
echo "[INFO] planned setup tasks:"
echo "- validate Ansible control node dependencies"
echo "- validate inventory path"
echo "- validate SSH key and managed node access boundary"
echo "- prepare playbook execution directories"
echo "- prepare evidence directories"

mkdir -p ../evidence/raw
mkdir -p ../evidence/processed
mkdir -p ../evidence/summary

echo "[OK] setup stub completed: ${LAB_NAME}"
