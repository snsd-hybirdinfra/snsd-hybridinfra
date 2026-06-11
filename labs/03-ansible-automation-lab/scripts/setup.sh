#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] ansible automation setup started"

ansible --version | tee runtime-workspace/logs/ansible-version.log

ansible -m ping ansible_automation_targets \
  | tee runtime-workspace/logs/ansible-ping.log

ansible-playbook playbooks/setup.yml \
  | tee runtime-workspace/logs/setup.log

cp runtime-workspace/logs/setup.log evidence/generated/raw/ansible-setup.log

echo "[INFO] ansible automation setup completed"