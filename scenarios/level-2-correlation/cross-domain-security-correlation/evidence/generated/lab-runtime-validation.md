# Lab Runtime Validation Evidence

Generated At: 2026-06-30 11:44:43

Scenario: `cross-domain-security-correlation`  
Level: `level-2-correlation`

## Validation Position

This evidence links the scenario to the current hybrid infrastructure lab runtime.

The validation scope is not a full production certification. It records observable runtime signals from the implemented lab environment and maps those signals to the scenario's operational intent.

## Related Runtime Labs

- `10-governance-reporting-lab`
- `07-logging-correlation-lab`
- `06-monitoring-stack-lab`

## Runtime Evidence Sources

- `labs/evidence/generated/runtime-service-inventory.md`
- `labs/evidence/generated/monitoring-target-status.md`
- `labs/evidence/generated/alerting-validation-summary.md`
- `labs/evidence/generated/recovery-validation-summary.md`
- `labs/evidence/generated/resilience-failure-suite-summary.md`

## Validation Summary

| Validation Area | Runtime Basis | Result |
|---|---|---|
| Node / service visibility | systemd service inventory and listening ports | collected |
| Monitoring target status | Prometheus `/api/v1/targets` | collected |
| Alerting state | Prometheus alerts and Alertmanager status | collected |
| Recovery validation | HAProxy continuity, backup/restore metrics, probe results | collected |

## Runtime Evidence Excerpts

### Monitoring Target Status

```json
# Monitoring Target Status

Generated At: 2026-06-30 11:44:42 KST +0900

Source: Prometheus API /api/v1/targets

----- BEGIN PROMETHEUS TARGETS JSON -----
{
  "activeTargets": [
    {
      "job": "blackbox_http",
      "instance": "https://192.168.1.20",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=http_2xx&target=https%3A%2F%2F192.168.1.20",
      "lastError": ""
    },
    {
      "job": "blackbox_icmp",
      "instance": "192.168.1.20",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=icmp&target=192.168.1.20",
      "lastError": ""
    },
    {
      "job": "cadvisor",
      "instance": "192.168.1.31:8080",
      "health": "up",
      "scrapeUrl": "http://192.168.1.31:8080/metrics",
      "lastError": ""
    },
    {
      "job": "cadvisor",
      "instance": "192.168.1.32:8080",
      "health": "up",
      "scrapeUrl": "http://192.168.1.32:8080/metrics",
      "lastError": ""
    },
    {
      "job": "haproxy_exporter",
      "instance": "192.168.1.20:9101",
      "health": "up",
      "scrapeUrl": "http://192.168.1.20:9101/metrics",
      "lastError": ""
    },
    {
      "job": "mysqld_exporter",
      "instance": "192.168.1.40:9104",
      "health": "up",
      "scrapeUrl": "http://192.168.1.40:9104/metrics",
      "lastError": ""
    },
    {
      "job": "node_exporter",
      "instance": "192.168.1.31:9100",
      "health": "up",
      "scrapeUrl": "http://192.168.1.31:9100/metrics",
      "lastError": ""
    },
    {
      "job": "node_exporter",
      "instance": "192.168.1.32:9100",
      "health": "up",
      "scrapeUrl": "http://192.168.1.32:9100/metrics",
      "lastError": ""
    },
    {
      "job": "node_exporter",
      "instance": "192.168.1.40:9100",
      "health": "up",
      "scrapeUrl": "http://192.168.1.40:9100/metrics",
      "lastError": ""
    },
    {
      "job": "node_exporter",
      "instance": "192.168.1.10:9100",
      "health": "up",
      "scrapeUrl": "http://192.168.1.10:9100/metrics",
      "lastError": ""
    },
    {
      "job": "node_exporter",
      "instance": "192.168.1.20:9100",
      "health": "up",
      "scrapeUrl": "http://192.168.1.20:9100/metrics",
      "lastError": ""
    },
    {
      "job": "prometheus",
      "instance": "127.0.0.1:9090",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9090/metrics",
      "lastError": ""
    }
  ]
}
----- END PROMETHEUS TARGETS JSON -----
```

### Alerting Validation Summary

```json
# Alerting Validation Summary

Generated At: 2026-06-30 11:44:42 KST +0900

## Prometheus Alerts

----- BEGIN PROMETHEUS ALERTS JSON -----
{
  "alerts": []
}
----- END PROMETHEUS ALERTS JSON -----

## Alertmanager Status

----- BEGIN ALERTMANAGER STATUS JSON -----
{
  "cluster": {
    "name": "01KWB2NMH08DR664KD8RK0ZVK8",
    "peers": [
      {
        "address": "192.168.8.135:9094",
        "name": "01KWB2NMH08DR664KD8RK0ZVK8"
      }
    ],
    "status": "ready"
  },
  "config": {
    "original": "global:\n  resolve_timeout: 5m\n  http_config:\n    follow_redirects: true\n    enable_http2: true\n  smtp_hello: localhost\n  smtp_require_tls: true\n  pagerduty_url: https://events.pagerduty.com/v2/enqueue\n  opsgenie_api_url: https://api.opsgenie.com/\n  wechat_api_url: https://qyapi.weixin.qq.com/cgi-bin/\n  victorops_api_url: https://alert.victorops.com/integrations/generic/20131114/alert/\n  telegram_api_url: https://api.telegram.org\n  webex_api_url: https://webexapis.com/v1/messages\nroute:\n  receiver: snsd-webhook\n  group_by:\n  - alertname\n  - instance\n  continue: false\n  group_wait: 10s\n  group_interval: 30s\n  repeat_interval: 5m\nreceivers:\n- name: snsd-webhook\n  webhook_configs:\n  - send_resolved: true\n    http_config:\n      follow_redirects: true\n      enable_http2: true\n    url: <secret>\n    url_file: \"\"\n    max_alerts: 0\ntemplates: []\n"
  },
  "uptime": "2026-06-30T10:35:32.900+09:00",
  "versionInfo": {
    "branch": "HEAD",
    "buildDate": "20240228-11:51:20",
    "buildUser": "root@22cd11f671e9",
    "goVersion": "go1.21.7",
    "revision": "0aa3c2aad14cff039931923ab16b26b7481783b5",
    "version": "0.27.0"
  }
}
----- END ALERTMANAGER STATUS JSON -----

## Alert Webhook Receiver

### Health
{"status": "ok", "service": "snsd-alert-webhook"}

### Recent Alert Webhook Payloads
{"alerts": [{"received_at": "2026-06-30T01:35:33.659197+00:00", "path": "/alertmanager", "payload": {"receiver": "snsd-webhook", "status": "firing", "alerts": [{"status": "firing", "labels": {"alertname": "SNSDWebhookReceiverTest", "severity": "info"}, "annotations": {"summary": "SNSD webhook receiver test"}}]}}]}
```

### Recovery Validation Summary

```text
# Recovery Validation Summary

Generated At: 2026-06-30 11:44:42 KST +0900

## Backup / Restore Metrics

----- BEGIN BACKUP RESTORE METRICS -----
# HELP node_textfile_mtime_seconds Unixtime mtime of textfiles successfully read.
# TYPE node_textfile_mtime_seconds gauge
node_textfile_mtime_seconds{file="/var/lib/node_exporter/textfile_collector/snsd_backup.prom"} 1.782787438e+09
node_textfile_mtime_seconds{file="/var/lib/node_exporter/textfile_collector/snsd_restore.prom"} 1.782706783e+09
# HELP node_textfile_scrape_error 1 if there was an error opening or reading a file, 0 otherwise
# TYPE node_textfile_scrape_error gauge
node_textfile_scrape_error 0
# HELP snsd_backup_last_duration_seconds Backup duration in seconds.
# TYPE snsd_backup_last_duration_seconds gauge
snsd_backup_last_duration_seconds 1
# HELP snsd_backup_last_run_timestamp_seconds Last backup run timestamp.
# TYPE snsd_backup_last_run_timestamp_seconds gauge
snsd_backup_last_run_timestamp_seconds 1.782787438e+09
# HELP snsd_backup_last_success Backup success status. 1 means success, 0 means failure.
# TYPE snsd_backup_last_success gauge
snsd_backup_last_success 1
# HELP snsd_backup_snapshot_count Restic snapshot count.
# TYPE snsd_backup_snapshot_count gauge
snsd_backup_snapshot_count 76
# HELP snsd_restore_validation_duration_seconds Restore validation duration in seconds.
# TYPE snsd_restore_validation_duration_seconds gauge
snsd_restore_validation_duration_seconds 1
# HELP snsd_restore_validation_last_run_timestamp_seconds Last restore validation timestamp.
# TYPE snsd_restore_validation_last_run_timestamp_seconds gauge
snsd_restore_validation_last_run_timestamp_seconds 1.782706783e+09
# HELP snsd_restore_validation_success Restore validation success status. 1 means success, 0 means failure.
# TYPE snsd_restore_validation_success gauge
snsd_restore_validation_success 1
----- END BACKUP RESTORE METRICS -----

## HAProxy / Probe Continuity

----- BEGIN HAPROXY PROBE CONTINUITY -----
## HAProxy Frontend
  <p>hostname=app-node-01</p>
  <p>status=ok</p>

## Backend Direct Checks


## Blackbox Probe Success
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
----- END HAPROXY PROBE CONTINUITY -----
```

### Resilience Failure Suite Summary

```text
# Resilience Failure Suite Summary

Generated At: 2026-06-29 13:08:59 KST +0900

Repository: /mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra
Inventory: /mnt/c/Users/swfco/OneDrive/바탕 화면/github/snsd-hybridinfra/inventory/lab/hosts.ini

## Suite Scope

- Web backend failure and recovery
- Observability loss and recovery
- Database failure and recovery
- Proxy entrypoint failure and recovery
- Backup failure and recovery validation

## Execution Log


### Web backend failure and recovery

- Playbook: ansible/playbooks/14-failure-injection-web-recovery.yml
- Result: PASS
- Finished At: 2026-06-29 13:10:55 KST +0900

### Observability loss and recovery

- Playbook: ansible/playbooks/15-failure-injection-observability-loss.yml
- Result: PASS
- Finished At: 2026-06-29 13:13:15 KST +0900

### Database failure and recovery

- Playbook: ansible/playbooks/16-failure-injection-database-recovery.yml
- Result: PASS
- Finished At: 2026-06-29 13:15:39 KST +0900

### Proxy entrypoint failure and recovery

- Playbook: ansible/playbooks/17-failure-injection-proxy-recovery.yml
- Result: PASS
- Finished At: 2026-06-29 13:18:04 KST +0900

### Backup failure and recovery validation

- Playbook: ansible/playbooks/18-failure-injection-backup-recovery.yml
- Result: PASS
- Finished At: 2026-06-29 13:20:30 KST +0900

## Final Result

- Result: PASS
- Finished At: 2026-06-29 13:21:31 KST +0900
- Runtime Evidence Refreshed: yes
```

## Reviewer Note

This file is generated from the active lab runtime evidence. The authoritative raw runtime evidence remains under `labs/evidence/generated/`, while this scenario-level file provides reviewer-facing linkage between scenario intent and observed lab signals.
