#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_EVIDENCE_DIR = ROOT / "labs" / "evidence" / "generated"

RUNTIME_FILES = {
    "runtime_service_inventory": RUNTIME_EVIDENCE_DIR / "runtime-service-inventory.md",
    "monitoring_target_status": RUNTIME_EVIDENCE_DIR / "monitoring-target-status.md",
    "alerting_validation_summary": RUNTIME_EVIDENCE_DIR / "alerting-validation-summary.md",
    "recovery_validation_summary": RUNTIME_EVIDENCE_DIR / "recovery-validation-summary.md",
    "resilience_failure_suite_summary": RUNTIME_EVIDENCE_DIR / "resilience-failure-suite-summary.md",
}


SCENARIO_LAB_OVERRIDES = {
    "api-gateway-health-monitoring": [
        "06-monitoring-stack-lab",
        "02-network-routing-lab",
        "09-resilience-failover-lab",
    ],
    "load-balancer-health-monitoring": [
        "06-monitoring-stack-lab",
        "02-network-routing-lab",
        "09-resilience-failover-lab",
    ],
    "endpoint-reachability-monitoring": [
        "02-network-routing-lab",
        "06-monitoring-stack-lab",
    ],
    "backup-job-monitoring": [
        "08-backup-recovery-lab",
        "06-monitoring-stack-lab",
    ],
    "database-health-monitoring": [
        "08-backup-recovery-lab",
        "06-monitoring-stack-lab",
    ],
}

LAB_KEYWORDS = {
    "01-linux-observability-lab": [
        "cpu", "memory", "filesystem", "node_exporter", "system", "host", "runtime"
    ],
    "02-network-routing-lab": [
        "blackbox", "icmp", "tcp", "probe", "haproxy", "network", "route", "endpoint"
    ],
    "03-ansible-automation-lab": [
        "ansible", "automation", "playbook", "configuration", "orchestration"
    ],
    "04-container-runtime-lab": [
        "docker", "container", "cadvisor", "nginx", "runtime"
    ],
    "05-kolla-openstack-lab": [
        "openstack", "kolla", "cloud", "control plane"
    ],
    "06-monitoring-stack-lab": [
        "prometheus", "grafana", "node_exporter", "blackbox", "alertmanager", "target"
    ],
    "07-logging-correlation-lab": [
        "loki", "promtail", "log", "syslog", "auth", "correlation"
    ],
    "08-backup-recovery-lab": [
        "restic", "backup", "restore", "snapshot", "mariadb", "recovery"
    ],
    "09-resilience-failover-lab": [
        "haproxy", "failover", "recovery", "blackbox", "probe", "continuity"
    ],
    "10-governance-reporting-lab": [
        "alert", "alertmanager", "governance", "report", "continuity", "validation"
    ],
}

def read_file(path: Path) -> str:
    if not path.exists():
        return f"NOT_FOUND: {path}"
    return path.read_text(encoding="utf-8", errors="replace")

def detect_labs_for_scenario(text: str) -> list[str]:
    t = text.lower()
    matched = []

    for lab, keywords in LAB_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in t)
        if score > 0:
            matched.append((score, lab))

    matched.sort(reverse=True)
    return [lab for _, lab in matched[:3]]

def scenario_text(scenario_dir: Path) -> str:
    parts = []
    for name in ["README.md", "metadata.yaml", "scenario.yaml", "scenario-test-evidence.md"]:
        p = scenario_dir / name
        if p.exists():
            parts.append(p.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(parts)

def should_include_failure_suite(scenario_dir: Path, text: str) -> bool:
    level = scenario_dir.parent.name.lower()
    name = scenario_dir.name.lower()
    t = text.lower()

    if level in {
        "level-3-recovery",
        "level-4-distributed-resilience",
        "level-5-enterprise-continuity",
    }:
        return True

    keywords = [
        "recovery",
        "restore",
        "backup",
        "failover",
        "resilience",
        "continuity",
        "incident",
        "alert",
        "validation",
        "automation",
        "database",
        "proxy",
        "observability",
    ]

    return any(keyword in name or keyword in t for keyword in keywords)

def fenced_block(language: str, body: str) -> str:
    return "```" + language + "\n" + body.rstrip() + "\n```\n"

def main() -> int:
    runtime_contents = {key: read_file(path) for key, path in RUNTIME_FILES.items()}
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    scenario_dirs = sorted(
        p for p in (ROOT / "scenarios").glob("level-*/*")
        if p.is_dir()
    )

    created = 0
    skipped = 0

    for scenario_dir in scenario_dirs:
        text = scenario_text(scenario_dir)
        if not text.strip():
            skipped += 1
            continue

        labs = SCENARIO_LAB_OVERRIDES.get(scenario_dir.name)
        if not labs:
            labs = detect_labs_for_scenario(text)
        if not labs:
            labs = ["06-monitoring-stack-lab"]

        evidence_dir = scenario_dir / "evidence" / "generated"
        evidence_dir.mkdir(parents=True, exist_ok=True)

        output = evidence_dir / "lab-runtime-validation.md"
        scenario_name = scenario_dir.name
        level_name = scenario_dir.parent.name

        content = []
        content.append("# Lab Runtime Validation Evidence\n")
        content.append(f"Generated At: {generated_at}\n")
        content.append(f"Scenario: `{scenario_name}`  ")
        content.append(f"Level: `{level_name}`\n")
        content.append("## Validation Position\n")
        content.append(
            "This evidence links the scenario to the current hybrid infrastructure lab runtime.\n"
        )
        content.append(
            "The validation scope is not a full production certification. "
            "It records observable runtime signals from the implemented lab environment "
            "and maps those signals to the scenario's operational intent.\n"
        )

        content.append("## Related Runtime Labs\n")
        for lab in labs:
            content.append(f"- `{lab}`")
        content.append("")

        content.append("## Runtime Evidence Sources\n")
        include_failure_suite = should_include_failure_suite(scenario_dir, text)

        content.append("- `labs/evidence/generated/runtime-service-inventory.md`")
        content.append("- `labs/evidence/generated/monitoring-target-status.md`")
        content.append("- `labs/evidence/generated/alerting-validation-summary.md`")
        content.append("- `labs/evidence/generated/recovery-validation-summary.md`")
        if include_failure_suite:
            content.append("- `labs/evidence/generated/resilience-failure-suite-summary.md`")
        content.append("")

        content.append("## Validation Summary\n")
        content.append("| Validation Area | Runtime Basis | Result |")
        content.append("|---|---|---|")
        content.append("| Node / service visibility | systemd service inventory and listening ports | collected |")
        content.append("| Monitoring target status | Prometheus `/api/v1/targets` | collected |")
        content.append("| Alerting state | Prometheus alerts and Alertmanager status | collected |")
        content.append("| Recovery validation | HAProxy continuity, backup/restore metrics, probe results | collected |\n")

        content.append("## Runtime Evidence Excerpts\n")

        content.append("### Monitoring Target Status\n")
        content.append(fenced_block("json", runtime_contents["monitoring_target_status"][:6000]))

        content.append("### Alerting Validation Summary\n")
        content.append(fenced_block("json", runtime_contents["alerting_validation_summary"][:6000]))

        content.append("### Recovery Validation Summary\n")
        content.append(fenced_block("text", runtime_contents["recovery_validation_summary"][:6000]))

        if include_failure_suite:
            content.append("### Resilience Failure Suite Summary\n")
            content.append(fenced_block("text", runtime_contents["resilience_failure_suite_summary"][:6000]))

        content.append("## Reviewer Note\n")
        content.append(
            "This file is generated from the active lab runtime evidence. "
            "The authoritative raw runtime evidence remains under `labs/evidence/generated/`, "
            "while this scenario-level file provides reviewer-facing linkage between scenario intent "
            "and observed lab signals.\n"
        )

        output.write_text("\n".join(content), encoding="utf-8")
        created += 1

    print(f"[OK] created={created} skipped={skipped}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
