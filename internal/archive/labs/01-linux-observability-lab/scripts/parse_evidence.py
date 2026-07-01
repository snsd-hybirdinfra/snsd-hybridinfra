from pathlib import Path
from datetime import datetime

LAB_ROOT = Path(__file__).resolve().parents[1]
RAW_LOG = LAB_ROOT / "evidence" / "generated" / "raw" / "ansible-validate.log"
PROCESSED_DIR = LAB_ROOT / "evidence" / "generated" / "processed"
SUMMARY_DIR = LAB_ROOT / "evidence" / "generated" / "summary"

PROCESSED_OUT = PROCESSED_DIR / "linux-observability-processed-summary.md"
SUMMARY_OUT = SUMMARY_DIR / "linux-observability-execution-summary.md"

def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")

def detect_status(text: str) -> str:
    lowered = text.lower()

    if not text.strip():
        return "NO_RAW_LOG"

    if "failed=" in lowered:
        failed_markers = []
        for line in text.splitlines():
            if "failed=" in line.lower():
                failed_markers.append(line.strip())

        for marker in failed_markers:
            if "failed=0" not in marker.lower():
                return "CHECK"

    if "unreachable=" in lowered:
        unreachable_markers = []
        for line in text.splitlines():
            if "unreachable=" in line.lower():
                unreachable_markers.append(line.strip())

        for marker in unreachable_markers:
            if "unreachable=0" not in marker.lower():
                return "CHECK"

    if "ok:" in lowered or "play recap" in lowered:
        return "PASS"

    return "UNKNOWN"

def extract_lines(text: str, keywords: list[str]) -> list[str]:
    results = []
    for line in text.splitlines():
        lowered = line.lower()
        if any(keyword.lower() in lowered for keyword in keywords):
            results.append(line.strip())
    return results

def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

    raw = read_text(RAW_LOG)
    status = detect_status(raw)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    recap_lines = extract_lines(raw, ["PLAY RECAP", "ok=", "changed=", "unreachable=", "failed="])
    task_lines = extract_lines(raw, ["TASK [", "PLAY ["])

    processed = []
    processed.append("# Linux Observability Processed Validation Summary")
    processed.append("")
    processed.append(f"Generated At: {generated_at}")
    processed.append(f"Raw Log: {RAW_LOG.relative_to(LAB_ROOT)}")
    processed.append(f"Detected Status: {status}")
    processed.append("")
    processed.append("## Task Markers")
    processed.append("")
    if task_lines:
        for item in task_lines:
            processed.append(f"- {item}")
    else:
        processed.append("- No task markers found")
    processed.append("")
    processed.append("## Recap Markers")
    processed.append("")
    if recap_lines:
        for item in recap_lines:
            processed.append(f"- {item}")
    else:
        processed.append("- No recap markers found")
    processed.append("")

    summary = []
    summary.append("# Linux Observability Execution Summary")
    summary.append("")
    summary.append(f"Generated At: {generated_at}")
    summary.append("")
    summary.append("## Execution Status")
    summary.append("")
    summary.append(f"- Status: {status}")
    summary.append("- Source: Ansible validation log")
    summary.append("")
    summary.append("## Evidence Files")
    summary.append("")
    summary.append("- evidence/generated/raw/ansible-validate.log")
    summary.append("- evidence/generated/processed/linux-observability-processed-summary.md")
    summary.append("- evidence/generated/summary/linux-observability-execution-summary.md")
    summary.append("")
    summary.append("## Interpretation")
    summary.append("")
    if status == "PASS":
        summary.append("The validation log indicates successful Linux observability validation execution.")
    elif status == "CHECK":
        summary.append("The validation log indicates failed or unreachable task markers and requires review.")
    elif status == "NO_RAW_LOG":
        summary.append("No raw validation log was found. Run scripts/validate.sh first.")
    else:
        summary.append("The validation log could not be conclusively interpreted.")
    summary.append("")

    PROCESSED_OUT.write_text("\n".join(processed), encoding="utf-8")
    SUMMARY_OUT.write_text("\n".join(summary), encoding="utf-8")

    print(f"[OK] wrote {PROCESSED_OUT.relative_to(LAB_ROOT)}")
    print(f"[OK] wrote {SUMMARY_OUT.relative_to(LAB_ROOT)}")
    print(f"[OK] status={status}")

if __name__ == "__main__":
    main()
