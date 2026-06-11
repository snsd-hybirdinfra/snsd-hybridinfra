#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="01-linux-observability-lab"

echo "[INFO] cleanup started: ${LAB_NAME}"

ANSIBLE_CONFIG=./ansible.cfg ansible-playbook playbooks/cleanup.yml | tee runtime-workspace/logs/cleanup.log

echo "[OK] cleanup completed: ${LAB_NAME}"
