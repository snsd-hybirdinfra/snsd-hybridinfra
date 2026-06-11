#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

DOC_GENERATORS = [
    "tools/content-generator/generate_lab_runtime_summary.py",
    "tools/content-generator/generate_lab_readiness_summary.py",
    "tools/content-generator/generate_labs_readme.py",
    "tools/content-generator/generate_scenarios_readme.py",
    "tools/content-generator/generate_lab_coverage_matrix.py",
    "tools/content-generator/generate_root_readme.py",
]

def run_script(script):
    script_path = REPO / script

    if not script_path.exists():
        print(f"[ERROR] missing generator: {script}")
        return 1

    print(f"[RUN] {script}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(REPO),
        text=True,
    )

    if result.returncode != 0:
        print(f"[FAIL] {script}")
        return result.returncode

    print(f"[OK] {script}")
    return 0

def main():
    failures = []

    for script in DOC_GENERATORS:
        rc = run_script(script)
        if rc != 0:
            failures.append((script, rc))

    if failures:
        print("")
        print("[SUMMARY] document generation failed")
        for script, rc in failures:
            print(f"- {script}: exit {rc}")
        raise SystemExit(1)

    print("")
    print("[SUMMARY] repository documentation generated successfully")
    print(f"[INFO] generator_count={len(DOC_GENERATORS)}")

if __name__ == "__main__":
    main()