from pathlib import Path

ROOT = Path(".").resolve()
MODULES_ROOT = ROOT / "modules"
OUT = MODULES_ROOT / "README.md"

module_dirs = sorted([p for p in MODULES_ROOT.iterdir() if p.is_dir()])

def titleize(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()

lines = []
lines.append("# Operational Modules")
lines.append("")
lines.append("This directory contains reusable operational capability modules used by scenario workflows across the SNSD Hybrid Infrastructure portfolio.")
lines.append("")
lines.append("Modules represent platform-level operational capabilities, not one-off scenario logic. They are intended to be reused across visibility, correlation, recovery, resilience, and continuity scenarios.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Module Design Principles")
lines.append("")
lines.append("- Each module represents a reusable operational capability.")
lines.append("- Modules should avoid vendor-specific or implementation-only naming.")
lines.append("- Modules support scenario orchestration, evidence generation, validation, or reporting.")
lines.append("- Scenario READMEs reference modules as capability dependencies.")
lines.append("- Module boundaries should remain lifecycle-aware and operationally meaningful.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Module Inventory")
lines.append("")
lines.append(f"Total modules: {len(module_dirs)}")
lines.append("")
lines.append("| Module | Purpose |")
lines.append("|---|---|")

for module in module_dirs:
    readme = module / "README.md"
    link = f"./{module.name}/README.md"

    purpose = "Reusable operational capability module."

    if readme.exists():
        text = readme.read_text(encoding="utf-8", errors="replace").splitlines()
        for line in text:
            clean = line.strip()
            if clean and not clean.startswith("#"):
                purpose = clean.replace("|", "\\|")
                break

    lines.append(f"| [{titleize(module.name)}]({link}) | {purpose} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## Capability Role")
lines.append("")
lines.append("Operational modules provide reusable building blocks for:")
lines.append("")
lines.append("- telemetry collection")
lines.append("- health signal normalization")
lines.append("- dependency correlation")
lines.append("- incident context preparation")
lines.append("- recovery orchestration")
lines.append("- automation execution")
lines.append("- recovery validation")
lines.append("- dashboard and evidence reporting")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("The module layer supports the repository's platform-oriented structure by separating reusable operational capabilities from scenario-specific workflows.")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")

print(f"[OK] wrote {OUT}")
print(f"[OK] module count: {len(module_dirs)}")
