#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw

echo "[INFO] ansible automation cleanup started"

ansible-playbook playbooks/cleanup.yml \
  | tee runtime-workspace/logs/cleanup.log

cp runtime-workspace/logs/cleanup.log evidence/generated/raw/ansible-cleanup.log

echo "[INFO] ansible automation cleanup completed"