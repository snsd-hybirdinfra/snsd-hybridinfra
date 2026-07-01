from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
SCENARIOS = ROOT / "scenarios"

START = "<!-- SCENARIO_INVENTORY_START -->"
END = "<!-- SCENARIO_INVENTORY_END -->"

LEVELS = [
    ("level-1-visibility", "Level 1 Visibility"),
    ("level-2-correlation", "Level 2 Correlation"),
    ("level-3-recovery", "Level 3 Recovery"),
    ("level-4-resilience", "Level 4 Resilience"),
    ("level-5-continuity", "Level 5 Continuity"),
]

def count_scenarios(level_dir: str) -> int:
    path = SCENARIOS / level_dir
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_dir())

def build_block() -> str:
    rows = []
    total = 0

    rows.append(START)
    rows.append("| Lifecycle Level | Scenario Count |")
    rows.append("|---|---:|")

    for dirname, label in LEVELS:
        count = count_scenarios(dirname)
        total += count
        rows.append(f"| {label} | {count} |")

    rows.append(f"| Total | {total} |")
    rows.append(END)

    return "\n".join(rows)

def main() -> int:
    if not README.exists():
        print("[FAIL] README.md not found")
        return 1

    text = README.read_text(encoding="utf-8", errors="ignore")
    block = build_block()

    if START not in text or END not in text:
        append = "\n\n## Scenario Inventory\n\n" + block + "\n"
        README.write_text(text.rstrip() + append, encoding="utf-8")
        print("[OK] README scenario inventory block added")
        return 0

    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)

    new_text = before.rstrip() + "\n\n" + block + after
    README.write_text(new_text, encoding="utf-8")

    print("[OK] README scenario inventory updated")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
