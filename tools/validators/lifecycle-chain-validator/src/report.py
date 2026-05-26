from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]

REPORT_PATH = (
    REPO_ROOT
    / "reports"
    / "validators"
    / "lifecycle-chain-validation-report.md"
)


def write_report(
    findings
):

    REPORT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    lines = [
        "# Lifecycle Chain Validation Report",
        "",
        f"Findings: {len(findings)}",
        ""
    ]

    if not findings:

        lines.append(
            "Lifecycle chain validation passed."
        )

    else:

        lines.extend(
            [
                "| File | Scenario | Lifecycle | Related Path | Related Level | Severity | Message |",
                "|---|---|---|---|---|---|---|"
            ]
        )

        for finding in findings:

            lines.append(
                f"| {finding['file']} | "
                f"{finding['scenario']} | "
                f"{finding['lifecycle']} | "
                f"{finding['related_path']} | "
                f"{finding['related_level']} | "
                f"{finding['severity']} | "
                f"{finding['message']} |"
            )

    REPORT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Lifecycle chain validation report generated: {REPORT_PATH}"
    )
