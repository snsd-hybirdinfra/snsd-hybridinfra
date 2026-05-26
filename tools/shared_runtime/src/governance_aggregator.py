from pathlib import Path
import json
from collections import Counter


def resolve_repo_root():

    return Path(__file__).resolve().parents[3]


def findings_root():

    return (
        resolve_repo_root()
        / "reports"
        / "validators"
        / "findings"
    )


def governance_summary_path():

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
        / "governance-summary.json"
    )


def load_validator_findings():

    root = findings_root()

    if not root.exists():

        return []

    payloads = []

    for path in sorted(
        root.glob("*.json")
    ):

        payloads.append(
            json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )
        )

    return payloads


def aggregate_governance_summary(
    run_id: str
):

    payloads = load_validator_findings()

    validators = {}
    severity_summary = Counter()
    category_summary = Counter()

    overall_status = "COMPLETED"

    for payload in payloads:

        validator = payload.get(
            "validator"
        )

        status = payload.get(
            "status",
            "COMPLETED"
        )

        findings = payload.get(
            "findings",
            []
        )

        validators[validator] = {
            "status": status,
            "finding_count": len(findings)
        }

        if status == "FAILED":

            overall_status = "FAILED"

        elif (
            status == "WARNING"
            and overall_status != "FAILED"
        ):

            overall_status = "WARNING"

        for finding in findings:

            severity_summary.update(
                [
                    finding.get(
                        "severity",
                        "UNKNOWN"
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

    summary = {
        "run_id": run_id,
        "status": overall_status,
        "validators": validators,
        "severity_summary": dict(
            severity_summary
        ),
        "category_summary": dict(
            category_summary
        )
    }

    output_path = governance_summary_path()

    output_path.write_text(
        json.dumps(
            summary,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return output_path
