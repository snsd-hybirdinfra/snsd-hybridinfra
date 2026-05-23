from pathlib import Path
from datetime import datetime
from collections import Counter


REPO_ROOT = Path(__file__).resolve().parents[3]

REPORT_DIR = (
    REPO_ROOT
    / "reports"
    / "toolchain"
)


REPORT_PATH = (
    REPORT_DIR
    / "latest-toolchain-execution-report.md"
)


def count_statuses(
    results: list
):

    counter = Counter()

    for result in results:

        counter[
            result.get(
                "status",
                "UNKNOWN"
            )
        ] += 1

    return counter


def write_execution_report(
    results: list
):

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    status_counts = count_statuses(
        results
    )

    lines = [
        "# Toolchain Execution Report",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|---|---:|",
        f"| COMPLETED | {status_counts.get('COMPLETED', 0)} |",
        f"| WARNING | {status_counts.get('WARNING', 0)} |",
        f"| FAILED | {status_counts.get('FAILED', 0)} |",
        f"| BLOCKED | {status_counts.get('BLOCKED', 0)} |",
        f"| SKIPPED | {status_counts.get('SKIPPED', 0)} |",
        "",
        "## Tool Results",
        "",
        "| Tool | Status | Notes |",
        "|---|---|---|"
    ]

    for result in results:

        lines.append(
            f"| {result.get('tool')} | "
            f"{result.get('status')} | "
            f"{result.get('notes', '')} |"
        )

    REPORT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Execution report generated: {REPORT_PATH}"
    )
