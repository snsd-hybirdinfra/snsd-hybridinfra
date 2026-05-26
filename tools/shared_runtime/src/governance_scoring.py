from pathlib import Path
import json


BASE_SCORE = 100


SEVERITY_PENALTY = {

    "INFO": 0,
    "WARNING": 2,
    "ERROR": 5,
    "CRITICAL": 20
}


def resolve_repo_root():

    return Path(__file__).resolve().parents[3]


def governance_summary_path():

    return (
        resolve_repo_root()
        / "reports"
        / "toolchain"
        / "governance-summary.json"
    )


def governance_score_path():

    return (
        resolve_repo_root()
        / "reports"
        / "toolchain"
        / "governance-score.json"
    )


def load_governance_summary():

    path = governance_summary_path()

    if not path.exists():

        raise FileNotFoundError(
            f"Missing governance summary: {path}"
        )

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def calculate_score(
    severity_summary: dict
):

    score = BASE_SCORE

    for severity, count in severity_summary.items():

        penalty = (
            SEVERITY_PENALTY.get(
                severity,
                0
            )
            * count
        )

        score -= penalty

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


def generate_governance_score():

    summary = load_governance_summary()

    severity_summary = summary.get(
        "severity_summary",
        {}
    )

    score = calculate_score(
        severity_summary
    )

    grade = determine_grade(
        score,
        severity_summary,
        summary.get(
            "category_summary",
            {}
        )
    )

    payload = {
        "run_id": summary.get(
            "run_id"
        ),
        "status": summary.get(
            "status"
        ),
        "score": score,
        "grade": grade,
        "severity_summary": severity_summary,
        "category_summary": summary.get(
            "category_summary",
            {}
        )
    }

    output_path = governance_score_path()

    output_path.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return output_path



