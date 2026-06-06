import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "main.py"
EXAMPLES = ROOT / "examples"


def render_example(yaml_path: Path) -> bool:
    print(f"[RENDER] {yaml_path.name}")

    result = subprocess.run(
        [
            sys.executable,
            str(MAIN),
            str(yaml_path)
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"[FAIL] {yaml_path.name}")
        print(result.stdout)
        print(result.stderr)
        return False

    svg_path = yaml_path.with_suffix(".svg")

    if not svg_path.exists():
        print(f"[FAIL] SVG not generated: {svg_path.name}")
        return False

    if svg_path.stat().st_size < 1000:
        print(f"[FAIL] SVG too small: {svg_path.name}")
        return False

    print(f"[OK] {svg_path.name}")
    return True


def main():
    yaml_files = sorted(EXAMPLES.glob("*.yaml"))

    if not yaml_files:
        print("[FAIL] No YAML examples found")
        sys.exit(1)

    failed = []

    for yaml_path in yaml_files:
        if not render_example(yaml_path):
            failed.append(yaml_path.name)

    if failed:
        print()
        print("[SUMMARY] Failed examples:")
        for name in failed:
            print(f"- {name}")
        sys.exit(1)

    print()
    print("[SUMMARY] All poster examples rendered successfully")


if __name__ == "__main__":
    main()

