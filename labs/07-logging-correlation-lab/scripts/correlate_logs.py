#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import re

BASE = Path(__file__).resolve().parents[1]
RAW_DIR = BASE / "evidence" / "generated" / "raw"
SUMMARY_DIR = BASE / "evidence" / "generated" / "summary"

DATASET = BASE / "datasets" / "sample-events.log"
NORMALIZED = RAW_DIR / "normalized-events.tsv"
TIMELINE = RAW_DIR / "correlation-timeline.md"
SUMMARY = SUMMARY_DIR / "logging-correlation-execution-summary.md"

RAW_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

REQUIRED_CHAINS = {
    "linux_observability_chain": [
        "login_success",
        "metrics_scrape",
        "playbook_task_ok",
    ],
    "container_runtime_recovery_chain": [
        "container_started",
        "container_health",
        "container_restart",
        "container_recovered",
    ],
    "monitoring_stack_visibility_chain": [
        "target_up",
        "dashboard_loaded",
    ],
    "end_to_end_runtime_correlation": [
        "playbook_task_ok",
        "container_recovered",
        "target_up",
        "correlation_completed",
    ],
}

def parse_line(line):
    parts = line.strip().split()
    if not parts:
        return None

    timestamp = parts[0]
    fields = {"timestamp": timestamp}

    for part in parts[1:]:
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        fields[key] = value

    return fields

def main():
    if not DATASET.exists():
        raise SystemExit(f"dataset missing: {DATASET}")

    events = []
    for line in DATASET.read_text(encoding="utf-8").splitlines():
        event = parse_line(line)
        if event:
            events.append(event)

    event_names = [event.get("event", "") for event in events]
    severity_counts = {}
    service_counts = {}

    for event in events:
        severity = event.get("severity", "UNKNOWN")
        service = event.get("service", "unknown")
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
        service_counts[service] = service_counts.get(service, 0) + 1

    chain_results = {}
    for chain_name, required_events in REQUIRED_CHAINS.items():
        missing = [event for event in required_events if event not in event_names]
        chain_results[chain_name] = {
            "status": "PASS" if not missing else "CHECK",
            "missing": missing,
        }

    overall_status = "PASS" if all(result["status"] == "PASS" for result in chain_results.values()) else "CHECK"

    normalized_lines = ["timestamp\thost\tservice\tseverity\tevent\tstatus"]
    for event in events:
        normalized_lines.append(
            "\t".join([
                event.get("timestamp", ""),
                event.get("host", ""),
                event.get("service", ""),
                event.get("severity", ""),
                event.get("event", ""),
                event.get("status", ""),
            ])
        )

    NORMALIZED.write_text("\n".join(normalized_lines) + "\n", encoding="utf-8")

    timeline_lines = [
        "# Logging Correlation Timeline",
        "",
        "| Timestamp | Host | Service | Severity | Event |",
        "|---|---|---|---|---|",
    ]

    for event in events:
        timeline_lines.append(
            f"| {event.get('timestamp', '')} | {event.get('host', '')} | {event.get('service', '')} | {event.get('severity', '')} | {event.get('event', '')} |"
        )

    TIMELINE.write_text("\n".join(timeline_lines) + "\n", encoding="utf-8")

    summary_lines = [
        "# Logging Correlation Execution Summary",
        "",
        "Execution Mode: file-based-log-correlation",
        "Evidence Policy: local-only",
        f"Overall Status: {overall_status}",
        "",
        "## Validation Signals",
        "",
        "| Signal | Status |",
        "|---|---|",
        f"| Log dataset readable | {'PASS' if events else 'CHECK'} |",
        f"| Normalized event output generated | {'PASS' if NORMALIZED.exists() else 'CHECK'} |",
        f"| Timeline reconstruction generated | {'PASS' if TIMELINE.exists() else 'CHECK'} |",
    ]

    for chain_name, result in chain_results.items():
        summary_lines.append(f"| Correlation rule {chain_name} | {result['status']} |")

    summary_lines.extend([
        "",
        "## Event Counters",
        "",
        f"- Total events: {len(events)}",
    ])

    for severity, count in sorted(severity_counts.items()):
        summary_lines.append(f"- Severity {severity}: {count}")

    summary_lines.extend([
        "",
        "## Service Counters",
        "",
    ])

    for service, count in sorted(service_counts.items()):
        summary_lines.append(f"- {service}: {count}")

    summary_lines.extend([
        "",
        "## Boundary",
        "",
        "This summary records local-only runtime validation for the Logging Correlation Lab.",
    ])

    SUMMARY.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print(f"[INFO] events={len(events)}")
    print(f"[INFO] overall_status={overall_status}")
    print(f"[INFO] summary={SUMMARY}")

if __name__ == "__main__":
    main()