# Lab Runtime Validation Evidence

Generated At: 2026-06-29 09:49:00

Scenario: `change-resilience-coordination`  
Level: `level-4-resilience`

## Validation Position

This evidence links the scenario to the current hybrid infrastructure lab runtime.

The validation scope is not a full production certification. It records observable runtime signals from the implemented lab environment and maps those signals to the scenario's operational intent.

## Related Runtime Labs

- `10-governance-reporting-lab`
- `09-resilience-failover-lab`
- `08-backup-recovery-lab`

## Runtime Evidence Sources

- `labs/evidence/generated/runtime-service-inventory.md`
- `labs/evidence/generated/monitoring-target-status.md`
- `labs/evidence/generated/alerting-validation-summary.md`
- `labs/evidence/generated/recovery-validation-summary.md`

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

Generated At: 2026-06-29 09:48:56 KST +0900

Source: Prometheus API /api/v1/targets

----- BEGIN PROMETHEUS TARGETS JSON -----
{
  "activeTargets": [
    {
      "job": "blackbox_http",
      "instance": "http://192.168.1.20",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=http_2xx&target=http%3A%2F%2F192.168.1.20",
      "lastError": ""
    },
    {
      "job": "blackbox_http",
      "instance": "http://192.168.1.31",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=http_2xx&target=http%3A%2F%2F192.168.1.31",
      "lastError": ""
    },
    {
      "job": "blackbox_http",
      "instance": "http://192.168.1.32",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=http_2xx&target=http%3A%2F%2F192.168.1.32",
      "lastError": ""
    },
    {
      "job": "blackbox_icmp",
      "instance": "192.168.1.32",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=icmp&target=192.168.1.32",
      "lastError": ""
    },
    {
      "job": "blackbox_icmp",
      "instance": "192.168.1.40",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=icmp&target=192.168.1.40",
      "lastError": ""
    },
    {
      "job": "blackbox_icmp",
      "instance": "192.168.1.10",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=icmp&target=192.168.1.10",
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
      "job": "blackbox_icmp",
      "instance": "192.168.1.31",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=icmp&target=192.168.1.31",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.31:9100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.31%3A9100",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.32:9100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.32%3A9100",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.40:9100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.40%3A9100",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.40:3000",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.40%3A3000",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.40:3100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.40%3A3100",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.10:9100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.10%3A9100",
      "lastError": ""
    },
    {
      "job": "blackbox_tcp",
      "instance": "192.168.1.20:9100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.20%3A9100",
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
      "job": "mysqld_exporter",
      "instance": "192.168.1.40:9104",
      "health": "up",
      "scrapeUrl": "http://192.168.1.40:9104/metrics",
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

Generated At: 2026-06-29 09:48:56 KST +0900

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
    "name": "01KW1CT7ZPBKBBNBMPAEBWWFQR",
    "peers": [
      {
        "address": "192.168.8.135:9094",
        "name": "01KW1CT7ZPBKBBNBMPAEBWWFQR"
      }
    ],
    "status": "ready"
  },
  "config": {
    "original": "global:\n  resolve_timeout: 5m\n  http_config:\n    follow_redirects: true\n    enable_http2: true\n  smtp_hello: localhost\n  smtp_require_tls: true\n  pagerduty_url: https://events.pagerduty.com/v2/enqueue\n  opsgenie_api_url: https://api.opsgenie.com/\n  wechat_api_url: https://qyapi.weixin.qq.com/cgi-bin/\n  victorops_api_url: https://alert.victorops.com/integrations/generic/20131114/alert/\n  telegram_api_url: https://api.telegram.org\n  webex_api_url: https://webexapis.com/v1/messages\nroute:\n  receiver: snsd-local-receiver\n  group_by:\n  - alertname\n  - severity\n  continue: false\n  group_wait: 10s\n  group_interval: 1m\n  repeat_interval: 30m\nreceivers:\n- name: snsd-local-receiver\ntemplates: []\n"
  },
  "uptime": "2026-06-26T16:20:25.335+09:00",
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
```

### Recovery Validation Summary

```text
# Recovery Validation Summary

Generated At: 2026-06-29 09:48:56 KST +0900

## Backup / Restore Metrics

----- BEGIN BACKUP RESTORE METRICS -----
# HELP node_textfile_mtime_seconds Unixtime mtime of textfiles successfully read.
# TYPE node_textfile_mtime_seconds gauge
node_textfile_mtime_seconds{file="/var/lib/node_exporter/textfile_collector/snsd_backup.prom"} 1.782693995e+09
node_textfile_mtime_seconds{file="/var/lib/node_exporter/textfile_collector/snsd_restore.prom"} 1.782455809e+09
# HELP node_textfile_scrape_error 1 if there was an error opening or reading a file, 0 otherwise
# TYPE node_textfile_scrape_error gauge
node_textfile_scrape_error 0
# HELP snsd_backup_last_duration_seconds Backup duration in seconds.
# TYPE snsd_backup_last_duration_seconds gauge
snsd_backup_last_duration_seconds 3
# HELP snsd_backup_last_run_timestamp_seconds Last backup run timestamp.
# TYPE snsd_backup_last_run_timestamp_seconds gauge
snsd_backup_last_run_timestamp_seconds 1.782693995e+09
# HELP snsd_backup_last_success Backup success status. 1 means success, 0 means failure.
# TYPE snsd_backup_last_success gauge
snsd_backup_last_success 1
# HELP snsd_backup_snapshot_count Restic snapshot count.
# TYPE snsd_backup_snapshot_count gauge
snsd_backup_snapshot_count 26
# HELP snsd_restore_validation_duration_seconds Restore validation duration in seconds.
# TYPE snsd_restore_validation_duration_seconds gauge
snsd_restore_validation_duration_seconds 1
# HELP snsd_restore_validation_last_run_timestamp_seconds Last restore validation timestamp.
# TYPE snsd_restore_validation_last_run_timestamp_seconds gauge
snsd_restore_validation_last_run_timestamp_seconds 1.782455809e+09
# HELP snsd_restore_validation_success Restore validation success status. 1 means success, 0 means failure.
# TYPE snsd_restore_validation_success gauge
snsd_restore_validation_success 1
----- END BACKUP RESTORE METRICS -----

## HAProxy / Probe Continuity

----- BEGIN HAPROXY PROBE CONTINUITY -----
## HAProxy Frontend
  <p>hostname: app-node-01</p>
  <p>status: healthy</p>

## Backend Direct Checks
  <p>hostname: app-node-01</p>
  <p>status: healthy</p>

  <p>hostname: app-node-02</p>
  <p>status: healthy</p>

## Blackbox Probe Success
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
----- END HAPROXY PROBE CONTINUITY -----
```

## Reviewer Note

This file is generated from the active lab runtime evidence. The authoritative raw runtime evidence remains under `labs/evidence/generated/`, while this scenario-level file provides reviewer-facing linkage between scenario intent and observed lab signals.
