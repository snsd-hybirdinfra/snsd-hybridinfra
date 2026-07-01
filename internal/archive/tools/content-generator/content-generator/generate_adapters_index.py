from pathlib import Path

ROOT = Path(".").resolve()
ADAPTERS_ROOT = ROOT / "adapters"
OUT = ADAPTERS_ROOT / "README.md"

adapter_dirs = sorted([p for p in ADAPTERS_ROOT.iterdir() if p.is_dir()])

def titleize(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()

def infer_role(name: str) -> str:
    lowered = name.lower()

    if "prometheus" in lowered:
        return "Collects and exposes infrastructure metrics for visibility and alerting workflows."
    if "grafana" in lowered:
        return "Supports dashboard visualization and operational reporting."
    if "ansible" in lowered:
        return "Executes infrastructure automation and recovery workflows."
    if "kubernetes" in lowered:
        return "Connects Kubernetes cluster signals and operational control points."
    if "opensearch" in lowered or "elastic" in lowered:
        return "Indexes and queries logs, events, and operational evidence."
    if "python" in lowered or "exporter" in lowered:
        return "Provides custom telemetry export or integration logic."

    return "Provides an integration boundary between platform workflows and external operational systems."

lines = []
lines.append("# Operational Adapters")
lines.append("")
lines.append("This directory contains adapter components used to connect operational scenarios and platform modules with external infrastructure, observability, automation, and reporting systems.")
lines.append("")
lines.append("Adapters are not scenario logic. They represent integration boundaries that allow reusable operational modules to interact with telemetry sources, automation engines, dashboards, and runtime platforms.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Adapter Design Principles")
lines.append("")
lines.append("- Adapters provide external system integration boundaries.")
lines.append("- Adapters should remain reusable across multiple scenarios.")
lines.append("- Adapters should avoid embedding scenario-specific workflow logic.")
lines.append("- Adapters support telemetry ingestion, automation execution, dashboard integration, or evidence retrieval.")
lines.append("- Operational modules consume adapter capabilities through platform workflows.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Adapter Inventory")
lines.append("")
lines.append(f"Total adapters: {len(adapter_dirs)}")
lines.append("")
lines.append("| Adapter | Integration Role |")
lines.append("|---|---|")

for adapter in adapter_dirs:
    readme = adapter / "README.md"
    link = f"./{adapter.name}/README.md"
    role = infer_role(adapter.name)

    if readme.exists():
        text = readme.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        for line in text:
            clean = line.strip()
            if clean and not clean.startswith("#"):
                role = clean.replace("|", "\\|")
                break

    lines.append(f"| [{titleize(adapter.name)}]({link}) | {role} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## Integration Role")
lines.append("")
lines.append("Adapters support operational workflows by connecting platform capabilities to:")
lines.append("")
lines.append("- metric collection systems")
lines.append("- log and event platforms")
lines.append("- dashboard and visualization tools")
lines.append("- automation execution engines")
lines.append("- Kubernetes and container platforms")
lines.append("- validation and evidence sources")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("The adapter layer keeps external integration concerns separate from reusable operational modules and scenario orchestration logic.")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")

print(f"[OK] wrote {OUT}")
print(f"[OK] adapter count: {len(adapter_dirs)}")

