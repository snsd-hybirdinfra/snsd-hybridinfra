#!/usr/bin/env bash
set -euo pipefail

LAB_NAME="01-linux-observability-lab"

echo "[INFO] preflight started: ${LAB_NAME}"

check_file() {
  local path="$1"
  if [ -f "$path" ]; then
    echo "[OK] file exists: $path"
  else
    echo "[FAIL] missing file: $path"
    exit 1
  fi
}

check_dir() {
  local path="$1"
  if [ -d "$path" ]; then
    echo "[OK] directory exists: $path"
  else
    echo "[FAIL] missing directory: $path"
    exit 1
  fi
}

check_command() {
  local cmd="$1"
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[OK] command exists: $cmd"
  else
    echo "[FAIL] command not found: $cmd"
    exit 1
  fi
}

check_command ansible
check_command ansible-playbook

check_file ansible.cfg
check_file inventory/hosts.ini
check_file inventory/group_vars/linux_observability_targets.yml

check_file playbooks/setup.yml
check_file playbooks/validate.yml
check_file playbooks/cleanup.yml

check_dir evidence/generated/raw
check_dir evidence/generated/processed
check_dir evidence/generated/summary
check_dir runtime-workspace/logs
check_dir runtime-workspace/tmp

echo "[INFO] ansible version"
ansible --version | head -n 5

echo "[INFO] inventory graph"
ANSIBLE_CONFIG=./ansible.cfg ansible-inventory --graph

echo "[INFO] playbook syntax checks"
ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --syntax-check playbooks/setup.yml
ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --syntax-check playbooks/validate.yml
ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --syntax-check playbooks/cleanup.yml

echo "[OK] preflight completed: ${LAB_NAME}"
