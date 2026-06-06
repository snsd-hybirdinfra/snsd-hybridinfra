import subprocess
import sys
from pathlib import Path

ROOT = Path(".").resolve()

commands = [
    ["python", "tools/content-generator/check_markdown_links.py"],
    ["python", "tools/content-generator/check_top_level_structure.py"],
    ["python", "tools/content-generator/check_repository_quality.py"],
    ["python", "tools/content-generator/generate_portfolio_health_summary.py"],
    ["python", "tools/content-generator/cleanup_temporary_files.py"],
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
