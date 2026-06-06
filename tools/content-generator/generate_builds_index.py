from pathlib import Path

ROOT = Path(".").resolve()
BUILDS_ROOT = ROOT / "builds"
OUT = BUILDS_ROOT / "README.md"

BUILDS_ROOT.mkdir(exist_ok=True)

build_dirs = sorted([p for p in BUILDS_ROOT.iterdir() if p.is_dir()])

def titleize(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()

def infer_purpose(name: str) -> str:
    lowered = name.lower()

    if "backup" in lowered:
        return "Provides backup automation and recovery preparation foundation."
    if "network" in lowered:
        return "Supports network infrastructure build, validation, or automation foundation."
    if "observability" in lowered or "monitoring" in lowered:
        return "Supports monitoring, visibility, and observability foundation."
    if "security" in lowered:
        return "Supports security control, telemetry, or governance foundation."
    if "automation" in lowered:
        return "Provides automation foundation for repeatable infrastructure operations."

    return "Provides reusable build foundation for infrastructure operations workflows."

lines = []
lines.append("# Build Foundations")
lines.append("")
lines.append("This directory contains build-level foundations that support the SNSD Hybrid Infrastructure operational capability platform.")
lines.append("")
lines.append("Build foundations represent reusable setup, automation, or enablement layers that support scenarios, modules, adapters, and shared runtime workflows.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Build Design Principles")
lines.append("")
lines.append("- Build foundations should support repeatable infrastructure operations.")
lines.append("- Build content should avoid scenario-only assumptions.")
lines.append("- Build outputs should support operational validation, automation, or evidence generation.")
lines.append("- Build foundations may support multiple lifecycle levels and infrastructure domains.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Build Inventory")
lines.append("")
lines.append(f"Total build foundations: {len(build_dirs)}")
lines.append("")
lines.append("| Build Foundation | Purpose |")
lines.append("|---|---|")

for build in build_dirs:
    readme = build / "README.md"
    link = f"./{build.name}/README.md"
    purpose = infer_purpose(build.name)

    if readme.exists():
        text = readme.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        for line in text:
            clean = line.strip()
            if clean and not clean.startswith("#"):
                purpose = clean.replace("|", "\\|")
                break

    lines.append(f"| [{titleize(build.name)}]({link}) | {purpose} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## Platform Role")
lines.append("")
lines.append("Build foundations support the repository by providing reusable implementation groundwork for:")
lines.append("")
lines.append("- automation preparation")
lines.append("- infrastructure setup")
lines.append("- validation workflows")
lines.append("- recovery readiness")
lines.append("- operational evidence generation")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("The builds layer provides reusable foundation assets that support the operational capability platform without replacing scenario-level workflows.")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")

print(f"[OK] wrote {OUT}")
print(f"[OK] build count: {len(build_dirs)}")
