from pathlib import Path

BUILD_ROOT = Path("builds")
OUTPUT = BUILD_ROOT / "README.md"

BUILD_DESCRIPTIONS = {
    "hybrid-vpc-foundation": "Baseline hybrid VPC, subnet, routing, gateway, and connectivity foundation",
    "private-web-tier-with-bastion": "Private web tier with bastion-controlled administrative access",
    "nat-gateway-egress-architecture": "Private subnet outbound access through NAT gateway routing",
    "alb-based-web-service-routing": "Application load balancing, listener routing, and target health structure",
    "security-boundary-baseline": "Security groups, access boundaries, and baseline network controls",
    "observability-stack-deployment": "Metrics, exporters, dashboards, and operational visibility foundation",
    "ansible-server-bootstrap": "Server bootstrap automation for packages, users, services, and configuration",
    "log-pipeline-foundation": "Log collection, forwarding, indexing, retention, and review pipeline",
    "backup-automation-foundation": "Backup job automation, repository target, retention, and validation boundary",
    "recovery-validation-lab": "Controlled recovery validation environment and evidence workflow",
}

def title(slug: str) -> str:
    return " ".join(part.upper() if part in {"vpc", "nat", "alb"} else part.capitalize() for part in slug.split("-"))

rows = []

for path in sorted(BUILD_ROOT.iterdir()):
    if not path.is_dir():
        continue

    slug = path.name
    rows.append({
        "slug": slug,
        "title": title(slug),
        "purpose": BUILD_DESCRIPTIONS.get(slug, "Infrastructure build and readiness scenario"),
    })

lines = [
    "# Infrastructure Build Scenarios",
    "",
    "This directory contains build-oriented infrastructure scenarios.",
    "",
    "Build scenarios document how infrastructure foundations are designed, provisioned, configured, secured, instrumented, and prepared for operational use.",
    "",
    "---",
    "",
    "## Build Scenario Catalog",
    "",
    "| Build Scenario | Purpose |",
    "|---|---|",
]

for row in rows:
    lines.append(f"| [{row['title']}]({row['slug']}/) | {row['purpose']} |")

lines += [
    "",
    "---",
    "",
    "## Build Flow",
    "",
    "Infrastructure Build  ",
    "→ Baseline Configuration  ",
    "→ Security Boundary  ",
    "→ Observability Setup  ",
    "→ Automation Readiness  ",
    "→ Operational Scenario Integration",
    "",
    "---",
    "",
    "## Relationship to Operational Scenarios",
    "",
    "Build scenarios answer how the infrastructure foundation is created.",
    "",
    "Operational scenarios answer how that foundation is monitored, analyzed, recovered, validated, and governed.",
    "",
]

OUTPUT.write_text("\n".join(lines), encoding="utf-8")
print(f"[OK] generated {OUTPUT}")
print(f"[OK] build count: {len(rows)}")
