#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
RUNTIME_DIR="${LAB_DIR}/runtime-workspace"
LOG_DIR="${RUNTIME_DIR}/logs"

mkdir -p "${RAW_DIR}" "${LOG_DIR}"

echo "[INFO] logging correlation setup started"

python3 --version > "${LOG_DIR}/python-version.log" 2>&1 || true

cat > "${LOG_DIR}/operational-events.log" <<LOGS
2026-06-15T08:00:01Z level=INFO service=edge-gateway correlation_id=INC-2026-0701 event=request_received status=started
2026-06-15T08:00:03Z level=WARN service=app-api correlation_id=INC-2026-0701 event=latency_threshold_exceeded latency_ms=1380 status=degraded
2026-06-15T08:00:05Z level=ERROR service=app-api correlation_id=INC-2026-0701 event=upstream_timeout status=failed
2026-06-15T08:00:07Z level=WARN service=worker correlation_id=INC-2026-0701 event=retry_started attempt=1 status=recovering
2026-06-15T08:00:11Z level=INFO service=worker correlation_id=INC-2026-0701 event=retry_completed status=recovered
2026-06-15T08:00:14Z level=INFO service=edge-gateway correlation_id=INC-2026-0701 event=request_completed status=ok
2026-06-15T08:01:00Z level=INFO service=batch-worker correlation_id=INC-2026-0702 event=scheduled_job_started status=ok
2026-06-15T08:01:05Z level=INFO service=batch-worker correlation_id=INC-2026-0702 event=scheduled_job_completed status=ok
LOGS

cat > "${RAW_DIR}/logging-correlation-setup.log" <<SETUP
SNSD_LOGGING_CORRELATION_SETUP=ready
LAB=07-logging-correlation-lab
RUNTIME=local-log-correlation
SOURCE_LOG=${LOG_DIR}/operational-events.log
SETUP

echo "[INFO] logging correlation setup completed"