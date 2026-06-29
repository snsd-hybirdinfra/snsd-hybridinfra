#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INVENTORY="${REPO_ROOT}/inventory/lab/hosts.ini"

cd "${REPO_ROOT}"

run_playbook() {
  local playbook="$1"

  echo
  echo "============================================================"
  echo "[RUN] ${playbook}"
  echo "============================================================"

  ansible-playbook -i "${INVENTORY}" "ansible/playbooks/${playbook}"

  echo
  echo "[OK] ${playbook}"
}

echo
echo "============================================================"
echo "SNSD Ansible Lab Bootstrap"
echo "============================================================"
echo "repo=${REPO_ROOT}"
echo "inventory=${INVENTORY}"
echo "started_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

echo
echo "============================================================"
echo "Precheck: Ansible connectivity"
echo "============================================================"
ansible -i "${INVENTORY}" ubuntu_nodes -m ping

run_playbook "01-common-base.yml"
run_playbook "02-configure-time-sync.yml"
run_playbook "03-install-docker.yml"
run_playbook "04-install-node-exporter.yml"
run_playbook "05-install-prometheus-grafana.yml"
run_playbook "06-configure-grafana-provisioning.yml"
run_playbook "07-install-loki-promtail.yml"
run_playbook "08-install-blackbox-exporter.yml"
run_playbook "09-deploy-sample-web-haproxy.yml"
run_playbook "10-install-cadvisor.yml"
run_playbook "11-install-mariadb-exporter.yml"
run_playbook "12-configure-restic-backup.yml"
run_playbook "13-configure-alertmanager-rules.yml"

echo
echo "============================================================"
echo "Postcheck: repository static check"
echo "============================================================"
tools/validation/repository_static_check.sh

echo
echo "============================================================"
echo "Postcheck: runtime smoke check"
echo "============================================================"
tools/validation/runtime_smoke_check.sh

echo
echo "============================================================"
echo "Bootstrap Summary"
echo "============================================================"
echo "finished_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"
echo "[OK] ansible lab bootstrap completed"
echo
echo "Failure injection is intentionally excluded from bootstrap."
echo "Run manually when needed:"
echo "ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/14-failure-injection-web-recovery.yml"
