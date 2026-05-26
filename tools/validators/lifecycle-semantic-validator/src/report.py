from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]

REPORT_PATH = (
    REPO_ROOT
    / "reports"
    / "validators"
    / "lifecycle-semantic-validation-report.md"
)


def write_report(
    findings
):

    REPORT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    lines = [
        "# Lifecycle Semantic Validation Report",
        "",
        f"Findings: {len(findings)}",
        ""
    ]

    if not findings:

        lines.append(
            "Lifecycle semantic validation passed."
        )

    else:

        lines.extend(
            [
                "| File | Lifecycle | Forbidden Term | Severity |",
                "|---|---|---|---|"
            ]
        )

        for finding in findings:

            lines.append(
                f"| {finding['file']} | "
                f"{finding['lifecycle']} | "
                f"{finding['term']} | "
                f"{finding['severity']} |"
            )

    REPORT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Lifecycle semantic validation report generated: {REPORT_PATH}"
    )
