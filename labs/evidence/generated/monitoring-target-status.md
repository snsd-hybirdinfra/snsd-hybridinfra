# Monitoring Target Status

Generated At: 2026-06-26 17:10:55 KST +0900

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
      "job": "blackbox_tcp",
      "instance": "192.168.1.20:9100",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9115/probe?module=tcp_connect&target=192.168.1.20%3A9100",
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
      "job": "prometheus",
      "instance": "127.0.0.1:9090",
      "health": "up",
      "scrapeUrl": "http://127.0.0.1:9090/metrics",
      "lastError": ""
    }
  ]
}
----- END PROMETHEUS TARGETS JSON -----
