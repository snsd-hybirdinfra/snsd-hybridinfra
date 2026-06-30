from pathlib import Path
import yaml

ROOT = Path(".").resolve()
SCENARIOS = ROOT / "scenarios"

DOMAIN_RULES = [
    (["vpn"], "Network / VPN"),
    (["routing", "route", "bgp", "wan", "network", "connectivity"], "Network / Routing"),
    (["kubernetes", "k8s"], "Kubernetes / Cluster"),
    (["cluster"], "Cluster / Platform"),
    (["database", "db"], "Database"),
    (["replication"], "Database / Replication"),
    (["storage", "volume", "object"], "Storage"),
    (["backup", "restoration"], "Backup / Recovery"),
    (["compute", "resource"], "Compute / Resource"),
    (["container"], "Container / Runtime"),
    (["identity", "access"], "Identity / Access"),
    (["security", "threat", "policy"], "Security / Telemetry"),
    (["certificate", "tls"], "TLS / Certificate"),
    (["dns"], "DNS / Name Resolution"),
    (["load-balancer", "load balancer"], "Load Balancing"),
    (["cloud-instance"], "Cloud Instance"),
    (["service-mesh"], "Service Mesh"),
    (["traffic"], "Traffic / Flow"),
    (["configuration", "config", "drift"], "Configuration / Change"),
    (["change", "rollback"], "Configuration / Change"),
    (["control-plane", "control plane"], "Control Plane"),
    (["inter-region", "cross-region", "multi-region"], "Multi-Region Operations"),
    (["data-protection", "data protection"], "Data Protection"),
    (["platform"], "Cluster / Platform"),
]

def infer_domain(name: str) -> str:
    normalized = name.lower().replace("_", "-")
    spaced = normalized.replace("-", " ")

    for keywords, domain in DOMAIN_RULES:
        for keyword in keywords:
            if keyword in normalized or keyword in spaced:
                return domain

    return "General Infrastructure"

updated = []

for metadata_path in sorted(SCENARIOS.glob("*/*/metadata.yaml")):
    text = metadata_path.read_text(encoding="utf-8-sig", errors="replace")
    data = yaml.safe_load(text) or {}

    current = data.get("primary_domain") or data.get("domain") or "Unknown"

    if str(current).strip().lower() not in ["", "unknown", "none", "null"]:
        continue

    scenario_name = data.get("scenario_name") or metadata_path.parent.name
    inferred = infer_domain(scenario_name)

    data["primary_domain"] = inferred

    metadata_path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    updated.append((metadata_path.parent.name, inferred))

print(f"[OK] updated unknown domains: {len(updated)}")
for name, domain in updated:
    print(f"- {name}: {domain}")
