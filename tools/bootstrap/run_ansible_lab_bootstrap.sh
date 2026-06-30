#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

INVENTORY="${INVENTORY:-inventory/lab/hosts.ini}"

PLAYBOOKS=(
  ansible/playbooks/01-common-base.yml
  ansible/playbooks/02-configure-time-sync.yml
  ansible/playbooks/03-install-docker.yml
  ansible/playbooks/04-install-node-exporter.yml
  ansible/playbooks/05-install-prometheus-grafana.yml
  ansible/playbooks/06-configure-grafana-provisioning.yml
  ansible/playbooks/07-install-loki-promtail.yml
  ansible/playbooks/08-install-blackbox-exporter.yml
  ansible/playbooks/09-deploy-sample-web-haproxy.yml
  ansible/playbooks/10-install-cadvisor.yml
  ansible/playbooks/11-install-mariadb-exporter.yml
  ansible/playbooks/12-configure-restic-backup.yml
  ansible/playbooks/13-install-haproxy-exporter.yml
  ansible/playbooks/14-install-alert-webhook-receiver.yml
  ansible/playbooks/15-configure-alertmanager-rules.yml
)

echo "[INFO] SNSD Ansible lab bootstrap started"
echo "[INFO] root=${ROOT_DIR}"
echo "[INFO] inventory=${INVENTORY}"
echo

for playbook in "${PLAYBOOKS[@]}"; do
  if [[ ! -f "${playbook}" ]]; then
    echo "[FAIL] missing playbook: ${playbook}"
    exit 1
  fi

  echo
  echo "======================================================================"
  echo "[RUN] ${playbook}"
  echo "======================================================================"
  ansible-playbook -i "${INVENTORY}" "${playbook}"
done

echo
echo "======================================================================"
echo "[CHECK] runtime smoke check"
echo "======================================================================"
tools/validation/runtime_smoke_check.sh

echo
echo "======================================================================"
echo "[CHECK] repository static check"
echo "======================================================================"
tools/validation/repository_static_check.sh

echo
echo "[OK] SNSD Ansible lab bootstrap completed"
echo
echo "Failure injection playbooks 21-25 are intentionally excluded from bootstrap."
echo "Run manually when needed:"
echo "  tools/failure/run_resilience_failure_suite.sh"
