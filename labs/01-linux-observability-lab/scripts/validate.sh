#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="01-linux-observability-lab"

echo "[INFO] validation started: ${LAB_NAME}"

mkdir -p evidence/generated/raw
mkdir -p evidence/generated/processed
mkdir -p evidence/generated/summary
mkdir -p runtime-workspace/logs

ANSIBLE_CONFIG=./ansible.cfg ansible-playbook playbooks/validate.yml | tee runtime-workspace/logs/validate.log

cp runtime-workspace/logs/validate.log evidence/generated/raw/ansible-validate.log

python3 scripts/parse_evidence.py

echo "[OK] validation completed: ${LAB_NAME}"
