#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] setup started: 01-linux-observability-lab"

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/processed
mkdir -p evidence/generated/summary

ANSIBLE_ARGS=()

if [[ "${ANSIBLE_ASK_PASS:-false}" == "true" ]]; then
  ANSIBLE_ARGS+=("--ask-pass")
fi

if [[ "${ANSIBLE_ASK_BECOME_PASS:-false}" == "true" ]]; then
  ANSIBLE_ARGS+=("--ask-become-pass")
fi

ANSIBLE_CONFIG=./ansible.cfg ansible-playbook playbooks/setup.yml "${ANSIBLE_ARGS[@]}" | tee runtime-workspace/logs/setup.log

echo "[INFO] setup completed: 01-linux-observability-lab"