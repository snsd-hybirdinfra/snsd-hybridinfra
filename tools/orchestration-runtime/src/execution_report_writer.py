from pathlib import Path
from datetime import datetime


REPO_ROOT = Path(__file__).resolve().parents[3]

REPORT_DIR = (
    REPO_ROOT
    / "reports"
    / "toolchain"
)


def write_execution_report(
    results: list
):

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    report_path = (
        REPORT_DIR
        / "latest-toolchain-execution-report.md"
    )

    lines = [
        "# Toolchain Execution Report",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
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

    report_path.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Execution report generated: {report_path}"
    )
