#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] kolla openstack setup started"

test -f configs/kolla-lab-policy.env
test -f configs/globals.yml
test -f inventory/multinode.ini
test -f scripts/kolla_preflight.py

python3 --version | tee runtime-workspace/logs/python-version.log

echo "[INFO] kolla openstack setup completed"