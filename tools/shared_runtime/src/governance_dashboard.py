from pathlib import Path
import json


def resolve_repo_root():

    return Path(__file__).resolve().parents[3]


def toolchain_report_root():

    return (
        resolve_repo_root()
        / "reports"
        / "toolchain"
    )


def load_json(
    path: Path
):

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def dashboard_path():

    return (
        toolchain_report_root()
        / "governance-dashboard.md"
    )


def generate_governance_dashboard():

    root = toolchain_report_root()

    governance_score = load_json(
        root / "governance-score.json"
    )

    scenario_score = load_json(
        root / "scenario-governance-score.json"
    )

    scenarios = scenario_score.get(
        "scenarios",
        {}
    )

    sorted_scenarios = sorted(
        scenarios.items(),
        key=lambda item: item[1].get(
            "score",
            0
        )
    )

    lines = []

    lines.append(
        "# Governance Dashboard"
    )

    lines.append(
        ""
    )

    lines.append(
        "## Governance Overview"
    )

    lines.append(
        ""
    )

    lines.append(
        "| Metric | Value |"
    )

    lines.append(
        "|---|---:|"
    )

    lines.append(
        f"| Overall Status | {governance_score.get('status')} |"
    )

    lines.append(
        f"| Overall Score | {governance_score.get('score')} |"
    )

    lines.append(
        f"| Overall Grade | {governance_score.get('grade')} |"
    )

    lines.append(
        f"| Scenario Count | {scenario_score.get('scenario_count')} |"
    )

    lines.append(
        ""
    )

    lines.append(
        "## Severity Distribution"
    )

    lines.append(
        ""
    )

    lines.append(
        "| Severity | Count |"
    )

    lines.append(
        "|---|---:|"
    )

    for severity, count in governance_score.get(
        "severity_summary",
        {}
    ).items():

        lines.append(
            f"| {severity} | {count} |"
        )

    lines.append(
        ""
    )

    lines.append(
        "## Governance Debt Categories"
    )

    lines.append(
        ""
    )

    lines.append(
        "| Category | Count |"
    )

    lines.append(
        "|---|---:|"
    )

    for category, count in governance_score.get(
        "category_summary",
        {}
    ).items():

        lines.append(
            f"| {category} | {count} |"
        )

    lines.append(
        ""
    )

    lines.append(
        "## Top Risk Scenarios"
    )

    lines.append(
        ""
    )

    lines.append(
        "| Scenario | Score | Grade | Findings |"
    )

    lines.append(
        "|---|---:|---:|---:|"
    )

    for scenario, data in sorted_scenarios[:10]:

        lines.append(
            f"| {scenario} | {data.get('score')} | {data.get('grade')} | {data.get('finding_count')} |"
        )

    lines.append(
        ""
    )

    lines.append(
        "## Gold Reference Candidates"
    )

    lines.append(
        ""
    )

    lines.append(
        "| Scenario | Score | Grade |"
    )

    lines.append(
        "|---|---:|---:|"
    )

    for scenario, data in sorted(
        scenarios.items(),
        key=lambda item: item[1].get(
            "score",
            0
        ),
        reverse=True
    ):

        if (
            data.get(
                "grade"
            ) == "A"
            and data.get(
                "finding_count"
            ) == 0
        ):

            lines.append(
                f"| {scenario} | {data.get('score')} | {data.get('grade')} |"
            )

    lines.append(
        ""
    )

    lines.append(
        "## Remediation Priority"
    )

    lines.append(
        ""
    )

    lines.append(
        "| Priority | Category | Action |"
    )

    lines.append(
        "|---|---|---|"
    )

    category_summary = governance_score.get(
        "category_summary",
        {}
    )

    if category_summary.get(
        "missing-required-diagram",
        0
    ) > 0:

        lines.append(
            "| P1 | missing-required-diagram | Generate required architecture diagrams for L3-L5 scenarios |"
        )

    if category_summary.get(
        "lifecycle-semantic-leakage",
        0
    ) > 0:

        lines.append(
            "| P2 | lifecycle-semantic-leakage | Refine lifecycle wording or semantic validation exclusions |"
        )

    if category_summary.get(
        "missing-recommended-diagram",
        0
    ) > 0:

        lines.append(
            "| P3 | missing-recommended-diagram | Generate recommended diagrams for L2 scenarios |"
        )

    output = dashboard_path()

    output.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

    return output



