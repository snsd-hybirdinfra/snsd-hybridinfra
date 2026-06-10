import subprocess
import sys
from pathlib import Path

ROOT = Path(".").resolve()

commands = [
    ["python", "tools/content-generator/cleanup_temporary_files.py"],

    ["python", "tools/content-generator/repair_missing_scenario_artifacts.py"],
    ["python", "tools/content-generator/generate_related_scenarios.py"],
    ["python", "tools/content-generator/generate_scenarios_index.py"],
    ["python", "tools/content-generator/generate_modules_index.py"],
    ["python", "tools/content-generator/generate_adapters_index.py"],
    ["python", "tools/content-generator/generate_builds_index.py"],

    ["python", "tools/content-generator/check_repository_quality.py"],
    ["python", "tools/content-generator/update_root_readme_inventory.py"],

    ["python", "tools/content-generator/check_lab_structure.py"],

    ["python", "tools/content-generator/check_markdown_links.py"],
    ["python", "tools/content-generator/check_top_level_structure.py"],
    ["python", "tools/content-generator/check_root_readme_alignment.py"],
    ["python", "tools/content-generator/check_repository_language.py"],

    ["python", "tools/content-generator/generate_portfolio_health_summary.py"],
    ["python", "tools/content-generator/generate_repository_summary_report.py"],
]

print("[INFO] Running repository validation workflow")
print(f"[INFO] Repository root: {ROOT}")
print("")

for command in commands:
    print("[RUN]", " ".join(command))
    result = subprocess.run(command, cwd=ROOT)

    if result.returncode != 0:
        print("")
        print("[FAIL]", " ".join(command))
        sys.exit(result.returncode)

    print("[OK]", " ".join(command))
    print("")

print("[OK] repository validation workflow completed")
