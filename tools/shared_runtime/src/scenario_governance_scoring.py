from pathlib import Path
import json
from collections import defaultdict, Counter


BASE_SCORE = 100


SEVERITY_PENALTY = {
    "INFO": 0,
    "WARNING": 2,
    "ERROR": 5,
    "CRITICAL": 20
}


def resolve_repo_root():

    return Path(__file__).resolve().parents[3]


def findings_root():

    return (
        resolve_repo_root()
        / "reports"
        / "validators"
        / "findings"
    )


def output_path():

    path = (
        resolve_repo_root()
        / "reports"
        / "toolchain"
    )

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    return (
        path
        / "scenario-governance-score.json"
    )


def load_all_findings():

    findings = []

    root = findings_root()

    if not root.exists():

        return findings

    for path in sorted(
        root.glob("*.json")
    ):

        payload = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        for finding in payload.get(
            "findings",
            []
        ):

            findings.append(
                finding
            )

    return findings


def calculate_score(
    severity_summary: dict
):

    score = BASE_SCORE

    for severity, count in severity_summary.items():

        score -= (
            SEVERITY_PENALTY.get(
                severity,
                0
            )
            * count
        )

    return max(
        score,
        0
    )


def base_grade_from_score(
    score: int
):

    if score >= 95:

        return "A"

    if score >= 85:

        return "B"

    if score >= 70:

        return "C"

    if score >= 50:

        return "D"

    return "F"


def cap_grade(
    grade: str,
    severity_summary: dict,
    category_summary: dict
):

    grade_order = [
        "A",
        "B",
        "C",
        "D",
        "F"
    ]

    caps = []

    if severity_summary.get(
        "ERROR",
        0
    ) > 0:

        caps.append(
            "B"
        )

    if severity_summary.get(
        "CRITICAL",
        0
    ) > 0:

        caps.append(
            "D"
        )

    if category_summary.get(
        "missing-required-diagram",
        0
    ) > 0:

        caps.append(
            "B"
        )

    if category_summary.get(
        "gold-reference-violation",
        0
    ) > 0:

        caps.append(
            "D"
        )

    if not caps:

        return grade

    worst_allowed = max(
        caps,
        key=lambda item: grade_order.index(
            item
        )
    )

    if grade_order.index(
        grade
    ) < grade_order.index(
        worst_allowed
    ):

        return worst_allowed

    return grade


def determine_grade(
    score: int,
    severity_summary: dict,
    category_summary: dict
):

    base_grade = base_grade_from_score(
        score
    )

    return cap_grade(
        base_grade,
        severity_summary,
        category_summary
    )


def generate_scenario_governance_score():

    findings = load_all_findings()

    scenario_findings = defaultdict(list)

    for finding in findings:

        scenario = finding.get(
            "scenario"
        )

        if not scenario:

            continue

        scenario_findings[
            scenario
        ].append(
            finding
        )

    scenarios = {}

    for scenario, items in sorted(
        scenario_findings.items()
    ):

        severity_summary = Counter()
        category_summary = Counter()

        for finding in items:

            severity_summary.update(
                [
                    finding.get(
                        "severity",
                        "INFO"
                    )
                ]
            )

            category_summary.update(
                [
                    finding.get(
                        "category",
                        "uncategorized"
                    )
                ]
            )

        score = calculate_score(
            dict(
                severity_summary
            )
        )

        scenarios[scenario] = {
            "score": score,
            "grade": determine_grade(
                score,
                dict(
                    severity_summary
                ),
                dict(
                    category_summary
                )
            ),
            "finding_count": len(
                items
            ),
            "severity_summary": dict(
                severity_summary
            ),
            "category_summary": dict(
                category_summary
            )
        }

    payload = {
        "scenario_count": len(
            scenarios
        ),
        "scenarios": scenarios
    }

    path = output_path()

    path.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return path


