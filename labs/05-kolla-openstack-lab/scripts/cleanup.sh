#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[INFO] kolla openstack cleanup started"

rm -rf evidence/generated/raw
rm -rf evidence/generated/summary
rm -rf runtime-workspace/logs

mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary
mkdir -p runtime-workspace/logs

echo "[INFO] kolla openstack cleanup completed"