#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone

METRICS = """# HELP snsd_service_up Mock service availability signal
# TYPE snsd_service_up gauge
snsd_service_up{service="api-gateway"} 1
snsd_service_up{service="database"} 1
snsd_service_up{service="message-queue"} 1
snsd_service_up{service="load-balancer"} 1

# HELP snsd_api_latency_seconds Mock API latency signal
# TYPE snsd_api_latency_seconds gauge
snsd_api_latency_seconds{service="api-gateway"} 0.184

# HELP snsd_certificate_days_remaining Mock certificate expiration signal
# TYPE snsd_certificate_days_remaining gauge
snsd_certificate_days_remaining{service="api-gateway"} 21

# HELP snsd_storage_usage_percent Mock storage capacity signal
# TYPE snsd_storage_usage_percent gauge
snsd_storage_usage_percent{volume="primary"} 72

# HELP snsd_database_up Mock database health signal
# TYPE snsd_database_up gauge
snsd_database_up{database="primary"} 1

# HELP snsd_message_queue_depth Mock message queue backlog signal
# TYPE snsd_message_queue_depth gauge
snsd_message_queue_depth{queue="orders"} 42

# HELP snsd_scrape_latency_seconds Mock scrape latency signal
# TYPE snsd_scrape_latency_seconds gauge
snsd_scrape_latency_seconds{target="scenario-mock-exporter"} 0.037

# HELP snsd_runtime_timestamp Mock runtime timestamp
# TYPE snsd_runtime_timestamp gauge
snsd_runtime_timestamp {timestamp}
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ["/metrics", "/"]:
            self.send_response(404)
            self.end_headers()
            return

        timestamp = int(datetime.now(timezone.utc).timestamp())
        body = METRICS.format(timestamp=timestamp).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 9106), Handler)
    print("[INFO] SNSD scenario mock exporter listening on :9106")
    server.serve_forever()
