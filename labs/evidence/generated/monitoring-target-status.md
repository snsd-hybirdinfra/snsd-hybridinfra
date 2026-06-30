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
