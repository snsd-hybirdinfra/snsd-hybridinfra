#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INVENTORY="${REPO_ROOT}/inventory/lab/hosts.ini"

cd "${REPO_ROOT}"

failures=0

section() {
  echo
  echo "============================================================"
  echo "$1"
  echo "============================================================"
}

check_cmd() {
  local name="$1"
  shift

  echo
  echo "[CHECK] ${name}"

  if "$@"; then
    echo "[PASS] ${name}"
  else
    echo "[FAIL] ${name}"
    failures=$((failures + 1))
  fi
}

section "SNSD Runtime Smoke Check"
echo "repo=${REPO_ROOT}"
echo "generated_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

section "Ansible Connectivity"
check_cmd "ansible ping ubuntu_nodes" \
  ansible -i "${INVENTORY}" ubuntu_nodes -m ping

section "Core Service Status"
check_cmd "node_exporter active on ubuntu_nodes" \
  ansible -i "${INVENTORY}" ubuntu_nodes -b -m shell -a "systemctl is-active node_exporter"

check_cmd "docker active on ubuntu_nodes" \
  ansible -i "${INVENTORY}" ubuntu_nodes -b -m shell -a "systemctl is-active docker"

check_cmd "prometheus active" \
  ansible -i "${INVENTORY}" monitoring -b -m shell -a "systemctl is-active prometheus"

check_cmd "grafana active" \
  ansible -i "${INVENTORY}" monitoring -b -m shell -a "systemctl is-active grafana-server"

check_cmd "loki active" \
  ansible -i "${INVENTORY}" monitoring -b -m shell -a "systemctl is-active loki"

check_cmd "promtail active on ubuntu_nodes" \
  ansible -i "${INVENTORY}" ubuntu_nodes -b -m shell -a "systemctl is-active promtail"

check_cmd "blackbox_exporter active" \
  ansible -i "${INVENTORY}" monitoring -b -m shell -a "systemctl is-active blackbox_exporter"

check_cmd "haproxy active" \
  ansible -i "${INVENTORY}" proxy -b -m shell -a "systemctl is-active haproxy"

check_cmd "mariadb active" \
  ansible -i "${INVENTORY}" data_ops -b -m shell -a "systemctl is-active mariadb"

check_cmd "mysqld_exporter active" \
  ansible -i "${INVENTORY}" data_ops -b -m shell -a "systemctl is-active mysqld_exporter"

check_cmd "alertmanager active" \
  ansible -i "${INVENTORY}" monitoring -b -m shell -a "systemctl is-active alertmanager"

section "HTTP/API Health"
check_cmd "Prometheus healthy" \
  bash -c "curl -fsS http://192.168.1.40:9090/-/healthy >/dev/null"

check_cmd "Grafana healthy" \
  bash -c "curl -fsS http://192.168.1.40:3000/api/health >/dev/null"

check_cmd "Loki ready" \
  bash -c "curl -fsS http://192.168.1.40:3100/ready >/dev/null"

check_cmd "Alertmanager healthy" \
  bash -c "curl -fsS http://192.168.1.40:9093/-/healthy >/dev/null"

check_cmd "HAProxy HTTP redirects to HTTPS" \
  bash -c 'code=$(curl -s -o /dev/null -w "%{http_code}" http://192.168.1.20); [ "$code" = "301" ]'

check_cmd "app-node-01 sample web health HTTP 200" \
  bash -c "curl -fsS http://192.168.1.31:18080/health >/dev/null"

check_cmd "app-node-02 sample web health HTTP 200" \
  bash -c "curl -fsS http://192.168.1.32:18080/health >/dev/null"

section "Prometheus Target Health"
check_cmd "all Prometheus active targets are up" \
  bash -c 'curl -fsS http://192.168.1.40:9090/api/v1/targets | jq -e "[.data.activeTargets[] | select(.health != \"up\")] | length == 0" >/dev/null'

section "Blackbox Probe"
check_cmd "blackbox HTTP proxy probe success" \
  bash -c 'curl -fsS "http://192.168.1.40:9115/probe?target=https://192.168.1.20&module=http_2xx" | grep -q "probe_success 1"'

check_cmd "blackbox ICMP proxy probe success" \
  bash -c 'curl -fsS "http://192.168.1.40:9115/probe?target=192.168.1.20&module=icmp" | grep -q "probe_success 1"'

section "Backup / Restore Metrics"
check_cmd "backup success metric exists" \
  bash -c 'curl -fsS http://192.168.1.40:9100/metrics | grep -q "snsd_backup_last_success 1"'

check_cmd "restore validation success metric exists" \
  bash -c 'curl -fsS http://192.168.1.40:9100/metrics | grep -q "snsd_restore_validation_success 1"'

section "Scenario Evidence"
check_cmd "scenario lab-runtime-validation count is 150" \
  bash -c '[ "$(find scenarios -path "*/evidence/generated/lab-runtime-validation.md" | wc -l)" -eq 150 ]'

check_cmd "scenario lab-runtime-validation has no NOT_FOUND" \
  bash -c '! grep -R "NOT_FOUND:" scenarios/*/*/evidence/generated/lab-runtime-validation.md >/dev/null 2>&1'

check_cmd "runtime validation index exists" \
  bash -c 'test -f docs/lab-runtime-validation-index.md'

section "Summary"
if [ "${failures}" -eq 0 ]; then
  echo "[OK] runtime smoke check passed"
  exit 0
else
  echo "[FAIL] runtime smoke check failed: ${failures} checks failed"
  exit 1
fi
