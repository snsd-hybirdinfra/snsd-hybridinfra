from __future__ import annotations

from pathlib import Path
from collections import Counter, defaultdict
import re


REPO_ROOT = Path(__file__).resolve().parents[2]
SCENARIOS_DIR = REPO_ROOT / "scenarios"
LABS_DIR = REPO_ROOT / "labs"

TRACEABILITY_DOC = REPO_ROOT / "docs" / "scenario-to-lab-traceability.md"
PHASE3_REPORT = REPO_ROOT / "validation-reports" / "phase-3-traceability-report.md"


LABS = {
    "01-linux-observability-lab": {
        "title": "Linux Observability Lab",
        "keywords": [
            "linux", "host", "process", "filesystem", "file system", "system event",
            "hardware", "cpu", "memory", "disk", "compute resource", "server service"
        ],
    },
    "02-network-routing-lab": {
        "title": "Network Routing Lab",
        "keywords": [
            "network", "routing", "route", "vpn", "wan", "dns", "bgp", "packet",
            "latency", "connectivity", "endpoint", "gateway", "load balancer",
            "traffic", "inter-region routing", "cross-site network"
        ],
    },
    "03-ansible-automation-lab": {
        "title": "Ansible Automation Lab",
        "keywords": [
            "ansible", "automation", "rollback", "remediation", "configuration",
            "change", "orchestration", "playbook", "rebalancing"
        ],
    },
    "04-container-runtime-lab": {
        "title": "Container Runtime Lab",
        "keywords": [
            "container", "runtime", "docker", "pod", "kubernetes", "workload",
            "cluster", "service mesh"
        ],
    },
    "05-kolla-openstack-lab": {
        "title": "Kolla OpenStack Lab",
        "keywords": [
            "openstack", "kolla", "cloud", "instance", "vm", "virtual machine",
            "hypervisor", "control plane", "object storage", "compute service",
            "service catalog", "endpoint readiness"
        ],
    },
    "06-monitoring-stack-lab": {
        "title": "Monitoring Stack Lab",
        "keywords": [
            "monitoring", "visibility", "telemetry", "metric", "prometheus",
            "grafana", "alert", "dashboard", "health", "exporter"
        ],
    },
    "07-logging-correlation-lab": {
        "title": "Logging Correlation Lab",
        "keywords": [
            "log", "logging", "audit", "event", "correlation", "analysis",
            "anomaly", "authentication", "security", "threat", "identity risk",
            "query lock"
        ],
    },
    "08-backup-recovery-lab": {
        "title": "Backup Recovery Lab",
        "keywords": [
            "backup", "restore", "restoration", "recovery point", "repository",
            "data recovery", "replication", "integrity", "protected workload"
        ],
    },
    "09-resilience-failover-lab": {
        "title": "Resilience Failover Lab",
        "keywords": [
            "resilience", "failover", "failback", "survivability", "multi-site",
            "multi-region", "cross-region", "distributed", "traffic shift",
            "secondary service"
        ],
    },
    "10-governance-reporting-lab": {
        "title": "Governance Reporting Lab",
        "keywords": [
            "governance", "reporting", "policy", "compliance", "quality",
            "continuity", "enterprise", "evidence", "reviewer"
        ],
    },
}


LIFECYCLE_FALLBACK = {
    "level-1-visibility": "06-monitoring-stack-lab",
    "level-2-correlation": "07-logging-correlation-lab",
    "level-3-recovery": "03-ansible-automation-lab",
    "level-4-resilience": "09-resilience-failover-lab",
    "level-5-continuity": "10-governance-reporting-lab",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_scalar(text: str, key: str, default: str = "") -> str:
    pattern = rf"^{re.escape(key)}:\s*(.*)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return default
    value = match.group(1).strip()
    value = value.strip('"').strip("'")
    return value


def extract_list(text: str, key: str) -> list[str]:
    lines = text.splitlines()
    values: list[str] = []
    capture = False

    for line in lines:
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            capture = True
            continue

        if capture:
            if re.match(r"^[A-Za-z0-9_-]+:", line):
                break

            item = re.match(r"^\s*-\s+(.*)$", line)
            if item:
                values.append(item.group(1).strip().strip('"').strip("'"))

    return values


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def score_lab(search_text: str, lab_name: str) -> int:
    score = 0
    for keyword in LABS[lab_name]["keywords"]:
        keyword_norm = normalize(keyword)
        if keyword_norm and keyword_norm in search_text:
            score += 3 if " " in keyword_norm else 2
    return score


def choose_lab(metadata: dict[str, object]) -> tuple[str, str]:
    lifecycle = str(metadata.get("lifecycle_level", ""))
    scenario_name = normalize(str(metadata.get("scenario_name", "")))
    scenario_title = normalize(str(metadata.get("scenario_title", "")))
    scenario_type = normalize(str(metadata.get("scenario_type", "")))
    primary_domain = normalize(str(metadata.get("primary_domain", "")))
    target_resource = normalize(str(metadata.get("target_resource", "")))

    telemetry = normalize(" ".join(metadata.get("telemetry_signals", [])))
    components = normalize(" ".join(metadata.get("infrastructure_components", [])))
    modules = normalize(" ".join(metadata.get("used_modules", [])))
    adapters = normalize(" ".join(metadata.get("used_adapters", [])))

    search_text = normalize(
        " ".join([
            scenario_name,
            scenario_title,
            scenario_type,
            primary_domain,
            target_resource,
            telemetry,
            components,
            modules,
            adapters,
        ])
    )

    def has_any(*keywords: str) -> bool:
        return any(normalize(keyword) in search_text for keyword in keywords)

    def name_has_any(*keywords: str) -> bool:
        return any(normalize(keyword) in scenario_name for keyword in keywords)

    def domain_has_any(*keywords: str) -> bool:
        return any(normalize(keyword) in primary_domain for keyword in keywords)

    # Lifecycle-level routing has the highest priority for advanced operational stages.
    if lifecycle == "level-4-resilience":
        return "09-resilience-failover-lab", "Lifecycle priority: level-4-resilience"

    if lifecycle == "level-5-continuity":
        return "10-governance-reporting-lab", "Lifecycle priority: level-5-continuity"

    # Strong domain-specific implementation boundaries.
    if name_has_any("openstack", "cloud-instance", "virtual-machine", "hypervisor", "object-storage", "control-plane") or \
       domain_has_any("cloud", "virtual machine", "virtualization", "openstack", "control plane"):
        return "05-kolla-openstack-lab", "Domain priority: cloud/openstack/control-plane"

    if name_has_any("backup", "restore", "restoration", "replication", "data-recovery") or \
       domain_has_any("backup", "recovery", "replication", "data protection"):
        return "08-backup-recovery-lab", "Domain priority: backup/recovery"

    if name_has_any("container", "docker", "pod", "kubernetes", "cluster", "service-mesh") or \
       domain_has_any("container", "kubernetes", "cluster", "service mesh"):
        return "04-container-runtime-lab", "Domain priority: container/kubernetes/runtime"

    if name_has_any("vpn", "wan", "bgp", "dns", "routing", "route", "network", "connectivity", "latency", "packet-loss", "load-balancer") or \
       domain_has_any("network", "routing", "vpn", "wan", "dns", "load balancing", "endpoint"):
        return "02-network-routing-lab", "Domain priority: network/routing/connectivity"

    # Linux observability must be checked before generic monitoring.
    if name_has_any("filesystem", "process", "system-event", "hardware", "compute-resource", "server-service") or \
       domain_has_any("filesystem", "process", "system event", "hardware", "compute", "server service"):
        return "01-linux-observability-lab", "Domain priority: linux host observability"

    # Correlation-specific routing. Avoid broad words such as analysis/event by themselves.
    if lifecycle == "level-2-correlation":
        if name_has_any("security", "identity", "authentication", "audit", "log", "threat", "anomaly", "query-lock"):
            return "07-logging-correlation-lab", "Lifecycle/domain priority: correlation logging/security"
        return "07-logging-correlation-lab", "Lifecycle priority: level-2-correlation"

    # Recovery-specific routing.
    if lifecycle == "level-3-recovery":
        if name_has_any("backup", "restore", "restoration", "replication", "data-recovery", "database-recovery"):
            return "08-backup-recovery-lab", "Lifecycle/domain priority: recovery data protection"
        if name_has_any("network", "route", "routing", "vpn", "dns", "load-balancer", "traffic"):
            return "02-network-routing-lab", "Lifecycle/domain priority: recovery network path"
        if name_has_any("container", "kubernetes", "cluster"):
            return "04-container-runtime-lab", "Lifecycle/domain priority: recovery container platform"
        if name_has_any("cloud", "instance", "virtual-machine", "control-plane"):
            return "05-kolla-openstack-lab", "Lifecycle/domain priority: recovery cloud control plane"
        return "03-ansible-automation-lab", "Lifecycle priority: level-3-recovery automation"

    # Visibility-specific routing. Generic visibility/monitoring belongs to the monitoring lab.
    if lifecycle == "level-1-visibility":
        return "06-monitoring-stack-lab", "Lifecycle priority: level-1-visibility monitoring"

    scores = {lab_name: score_lab(search_text, lab_name) for lab_name in LABS}
    selected_lab, selected_score = max(scores.items(), key=lambda item: item[1])

    if selected_score <= 0:
        selected_lab = LIFECYCLE_FALLBACK.get(lifecycle, "10-governance-reporting-lab")
        reason = f"Lifecycle fallback: {lifecycle}"
    else:
        reason = f"Keyword match score: {selected_score}"

    return selected_lab, reason

def load_scenarios() -> list[dict[str, object]]:
    scenarios: list[dict[str, object]] = []

    for metadata_path in sorted(SCENARIOS_DIR.glob("level-*/*/metadata.yaml")):
        text = read_text(metadata_path)

        metadata = {
            "scenario_name": extract_scalar(text, "scenario_name", metadata_path.parent.name),
            "scenario_title": extract_scalar(text, "scenario_title", metadata_path.parent.name),
            "lifecycle_level": extract_scalar(text, "lifecycle_level", metadata_path.parent.parent.name),
            "scenario_path": extract_scalar(
                text,
                "scenario_path",
                str(metadata_path.parent.relative_to(REPO_ROOT)).replace("\\", "/"),
            ),
            "scenario_type": extract_scalar(text, "scenario_type", ""),
            "primary_domain": extract_scalar(text, "primary_domain", ""),
            "target_resource": extract_scalar(text, "target_resource", ""),
            "telemetry_signals": extract_list(text, "telemetry_signals"),
            "infrastructure_components": extract_list(text, "infrastructure_components"),
            "used_modules": extract_list(text, "used_modules"),
            "used_adapters": extract_list(text, "used_adapters"),
        }

        lab_name, reason = choose_lab(metadata)
        metadata["mapped_lab"] = lab_name
        metadata["mapped_lab_title"] = LABS[lab_name]["title"]
        metadata["mapping_reason"] = reason

        scenarios.append(metadata)

    return scenarios


def markdown_table_row(values: list[object]) -> str:
    cleaned = []
    for value in values:
        text = str(value).replace("|", "/").replace("\n", " ").strip()
        cleaned.append(text)
    return "| " + " | ".join(cleaned) + " |"


def write_traceability_doc(scenarios: list[dict[str, object]]) -> None:
    by_lifecycle = Counter(str(item["lifecycle_level"]) for item in scenarios)
    by_lab = Counter(str(item["mapped_lab"]) for item in scenarios)

    lines: list[str] = []
    lines.append("# Scenario to Lab Traceability")
    lines.append("")
    lines.append("## 1. Purpose")
    lines.append("")
    lines.append(
        "This document maps operational scenarios to implementation labs so reviewers can trace each "
        "scenario to a concrete runtime validation boundary."
    )
    lines.append("")
    lines.append("## 2. Traceability Model")
    lines.append("")
    lines.append("| Layer | Meaning |")
    lines.append("|---|---|")
    lines.append("| Scenario | Operational capability validation workflow |")
    lines.append("| Lab | Implementation and runtime validation boundary |")
    lines.append("| Evidence | Local generated runtime validation output |")
    lines.append("| Report | Reviewer-readable validation or governance summary |")
    lines.append("")
    lines.append("## 3. Coverage Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---:|")
    lines.append(f"| Total scenarios | {len(scenarios)} |")
    lines.append(f"| Total labs | {len(LABS)} |")
    lines.append(f"| Mapped scenarios | {len([s for s in scenarios if s.get('mapped_lab')])} |")
    lines.append("")
    lines.append("## 4. Lifecycle Coverage")
    lines.append("")
    lines.append("| Lifecycle | Scenario Count |")
    lines.append("|---|---:|")
    for lifecycle, count in sorted(by_lifecycle.items()):
        lines.append(f"| {lifecycle} | {count} |")
    lines.append("")
    lines.append("## 5. Lab Coverage")
    lines.append("")
    lines.append("| Lab | Runtime Boundary | Scenario Count |")
    lines.append("|---|---|---:|")
    for lab_name in sorted(LABS):
        lines.append(
            markdown_table_row([
                lab_name,
                LABS[lab_name]["title"],
                by_lab.get(lab_name, 0),
            ])
        )
    lines.append("")
    lines.append("## 6. Scenario Mapping")
    lines.append("")
    lines.append("| Lifecycle | Scenario | Primary Domain | Mapped Lab | Mapping Reason |")
    lines.append("|---|---|---|---|---|")
    for item in scenarios:
        scenario_link = f"[{item['scenario_name']}](../{item['scenario_path']})"
        lines.append(
            markdown_table_row([
                item["lifecycle_level"],
                scenario_link,
                item["primary_domain"],
                item["mapped_lab"],
                item["mapping_reason"],
            ])
        )
    lines.append("")
    lines.append("## 7. Reviewer Interpretation")
    lines.append("")
    lines.append(
        "The mapping is intentionally implementation-oriented. A scenario may describe an operational "
        "capability at a higher level, while the mapped lab provides the concrete runtime boundary used "
        "to validate a representative implementation path."
    )
    lines.append("")

    TRACEABILITY_DOC.parent.mkdir(parents=True, exist_ok=True)
    TRACEABILITY_DOC.write_text("\n".join(lines), encoding="utf-8")


def write_phase3_report(scenarios: list[dict[str, object]]) -> None:
    by_lab = Counter(str(item["mapped_lab"]) for item in scenarios)
    unmapped = [item for item in scenarios if not item.get("mapped_lab")]

    status = "PASS" if len(scenarios) > 0 and not unmapped and len(by_lab) == len(LABS) else "CHECK"

    lines: list[str] = []
    lines.append("# Phase 3 Traceability Report")
    lines.append("")
    lines.append("## 1. Status")
    lines.append("")
    lines.append(f"Phase 3 traceability status: **{status}**")
    lines.append("")
    lines.append("## 2. Validation Matrix")
    lines.append("")
    lines.append("| Signal | Status |")
    lines.append("|---|---|")
    lines.append(f"| Scenario metadata discovered | {'PASS' if len(scenarios) > 0 else 'FAIL'} |")
    lines.append(f"| Scenario-to-lab mapping generated | {'PASS' if len(scenarios) > 0 else 'FAIL'} |")
    lines.append(f"| All scenarios mapped | {'PASS' if not unmapped else 'FAIL'} |")
    lines.append(f"| All 10 labs referenced | {'PASS' if len(by_lab) == len(LABS) else 'CHECK'} |")
    lines.append("| Traceability document generated | PASS |")
    lines.append("")
    lines.append("## 3. Coverage")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---:|")
    lines.append(f"| Total scenarios | {len(scenarios)} |")
    lines.append(f"| Total mapped scenarios | {len(scenarios) - len(unmapped)} |")
    lines.append(f"| Total labs referenced | {len(by_lab)} |")
    lines.append("")
    lines.append("## 4. Lab Coverage")
    lines.append("")
    lines.append("| Lab | Scenario Count |")
    lines.append("|---|---:|")
    for lab_name in sorted(LABS):
        lines.append(f"| {lab_name} | {by_lab.get(lab_name, 0)} |")
    lines.append("")
    lines.append("## 5. Generated Artifacts")
    lines.append("")
    lines.append("| Artifact | Path |")
    lines.append("|---|---|")
    lines.append("| Scenario-to-lab traceability | docs/scenario-to-lab-traceability.md |")
    lines.append("| Phase 3 traceability report | validation-reports/phase-3-traceability-report.md |")
    lines.append("")
    lines.append("## 6. Final Statement")
    lines.append("")
    lines.append(
        "Phase 3 establishes reviewer-readable traceability between operational scenarios and "
        "implementation lab runtime boundaries."
    )
    lines.append("")

    PHASE3_REPORT.parent.mkdir(parents=True, exist_ok=True)
    PHASE3_REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    scenarios = load_scenarios()
    write_traceability_doc(scenarios)
    write_phase3_report(scenarios)

    by_lab = Counter(str(item["mapped_lab"]) for item in scenarios)

    print("Scenario-to-lab traceability generated")
    print(f"Total scenarios: {len(scenarios)}")
    print(f"Total labs referenced: {len(by_lab)}")
    print(f"Traceability doc: {TRACEABILITY_DOC.relative_to(REPO_ROOT)}")
    print(f"Phase 3 report: {PHASE3_REPORT.relative_to(REPO_ROOT)}")

    for lab_name in sorted(LABS):
        print(f"{lab_name}: {by_lab.get(lab_name, 0)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())