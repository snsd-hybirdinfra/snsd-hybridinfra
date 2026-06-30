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
