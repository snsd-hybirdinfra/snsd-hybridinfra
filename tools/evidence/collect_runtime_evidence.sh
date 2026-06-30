#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
EVIDENCE_DIR="${REPO_ROOT}/labs/evidence/generated"
ALERTING_VALIDATION_SUMMARY="${EVIDENCE_DIR}/alerting-validation-summary.md"
INVENTORY="${REPO_ROOT}/inventory/lab/hosts.ini"

mkdir -p "${EVIDENCE_DIR}"
: > "${ALERTING_VALIDATION_SUMMARY}"

GENERATED_AT="$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

echo "[INFO] repo=${REPO_ROOT}"
echo "[INFO] evidence_dir=${EVIDENCE_DIR}"

{
  echo "# Runtime Service Inventory"
  echo
  echo "Generated At: ${GENERATED_AT}"
  echo
  echo "Source: ansible ubuntu_nodes service and port collection"
  echo
  echo "----- BEGIN RUNTIME INVENTORY -----"
  ansible -i "${INVENTORY}" ubuntu_nodes -b -m shell -a '
echo "## Host"
hostname
echo
echo "## Time"
date "+%Y-%m-%d %H:%M:%S %Z %z"
echo
echo "## IP Address"
hostname -I
echo
echo "## Active Services"
for svc in docker node_exporter promtail haproxy prometheus grafana-server loki blackbox_exporter mariadb mysqld_exporter alertmanager chrony; do
  if systemctl list-unit-files "${svc}.service" >/dev/null 2>&1; then
    echo "${svc}: $(systemctl is-active ${svc} 2>/dev/null || true)"
  fi
done
echo
echo "## Listening Ports"
ss -lntp || true
' || true
  echo "----- END RUNTIME INVENTORY -----"
} > "${EVIDENCE_DIR}/runtime-service-inventory.md"

{
  echo "# Monitoring Target Status"
  echo
  echo "Generated At: ${GENERATED_AT}"
  echo
  echo "Source: Prometheus API /api/v1/targets"
  echo
  echo "----- BEGIN PROMETHEUS TARGETS JSON -----"
  curl -s http://192.168.1.40:9090/api/v1/targets | jq '
{
  activeTargets: [
    .data.activeTargets[] |
    {
      job: .labels.job,
      instance: .labels.instance,
      health: .health,
      scrapeUrl: .scrapeUrl,
      lastError: .lastError
    }
  ]
}' || echo "PROMETHEUS_TARGET_COLLECTION_FAILED"
  echo "----- END PROMETHEUS TARGETS JSON -----"
} > "${EVIDENCE_DIR}/monitoring-target-status.md"

{
  echo "# Alerting Validation Summary"
  echo
  echo "Generated At: ${GENERATED_AT}"
  echo
  echo "## Prometheus Alerts"
  echo
  echo "----- BEGIN PROMETHEUS ALERTS JSON -----"
  curl -s http://192.168.1.40:9090/api/v1/alerts | jq '
{
  alerts: [
    .data.alerts[] |
    {
      state: .state,
      alertname: .labels.alertname,
      severity: .labels.severity,
      lifecycle: .labels.lifecycle,
      job: .labels.job,
      instance: .labels.instance,
      activeAt: .activeAt,
      value: .value
    }
  ]
}' || echo "PROMETHEUS_ALERT_COLLECTION_FAILED"
  echo "----- END PROMETHEUS ALERTS JSON -----"
  echo
  echo "## Alertmanager Status"
  echo
  echo "----- BEGIN ALERTMANAGER STATUS JSON -----"
  curl -s http://192.168.1.40:9093/api/v2/status | jq || echo "ALERTMANAGER_STATUS_COLLECTION_FAILED"
  echo "----- END ALERTMANAGER STATUS JSON -----"
} > "${EVIDENCE_DIR}/alerting-validation-summary.md"

{
  echo "# Recovery Validation Summary"
  echo
  echo "Generated At: ${GENERATED_AT}"
  echo
  echo "## Backup / Restore Metrics"
  echo
  echo "----- BEGIN BACKUP RESTORE METRICS -----"
  curl -s http://192.168.1.40:9100/metrics | grep -E "snsd_backup|snsd_restore|node_textfile" || true
  echo "----- END BACKUP RESTORE METRICS -----"
  echo
  echo "## HAProxy / Probe Continuity"
  echo
  echo "----- BEGIN HAPROXY PROBE CONTINUITY -----"
  echo "## HAProxy Frontend"
  curl -k -s https://192.168.1.20 | grep -E "hostname|status" || true
  echo
  echo "## Backend Direct Checks"
  curl -s http://192.168.1.31 | grep -E "hostname|status" || true
  echo
  curl -s http://192.168.1.32 | grep -E "hostname|status" || true
  echo
  echo "## Blackbox Probe Success"
  curl -s "http://192.168.1.40:9115/probe?target=https://192.168.1.20&module=http_2xx" | grep probe_success || true
  curl -s "http://192.168.1.40:9115/probe?target=192.168.1.20&module=icmp" | grep probe_success || true
  echo "----- END HAPROXY PROBE CONTINUITY -----"
} > "${EVIDENCE_DIR}/recovery-validation-summary.md"

echo "[OK] generated runtime evidence files"
find "${EVIDENCE_DIR}" -maxdepth 1 -type f -name "*.md" -print

{
  echo
  echo "## Alert Webhook Receiver"
  echo
  echo "### Health"
  curl -s http://192.168.1.40:5001/health || true
  echo
  echo
  echo "### Recent Alert Webhook Payloads"
  curl -s http://192.168.1.40:5001/alerts || true
  echo
} >> "${ALERTING_VALIDATION_SUMMARY}"

