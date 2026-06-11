#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] validation started: 01-linux-observability-lab"

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

ANSIBLE_CONFIG=./ansible.cfg ansible-playbook playbooks/validate.yml "${ANSIBLE_ARGS[@]}" | tee runtime-workspace/logs/validate.log

cp runtime-workspace/logs/validate.log evidence/generated/raw/ansible-validate.log

python3 scripts/parse_evidence.py

echo "[INFO] validation completed: 01-linux-observability-lab"