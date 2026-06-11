#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="01-linux-observability-lab"

echo "[INFO] setup started: ${LAB_NAME}"

mkdir -p evidence/generated/raw
mkdir -p evidence/generated/processed
mkdir -p evidence/generated/summary
mkdir -p runtime-workspace/logs
mkdir -p runtime-workspace/tmp

ANSIBLE_CONFIG=./ansible.cfg ansible-playbook playbooks/setup.yml | tee runtime-workspace/logs/setup.log

echo "[OK] setup completed: ${LAB_NAME}"
