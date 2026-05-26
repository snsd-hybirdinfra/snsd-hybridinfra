from pathlib import Path
import json

from shared_runtime.src.governance_severity import (
    normalize_severity,
    highest_severity,
    status_from_severity
)


def resolve_repo_root():

    return Path(__file__).resolve().parents[3]


def findings_root():

    path = (
        resolve_repo_root()
        / "reports"
        / "validators"
        / "findings"
    )

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    return path


def normalize_findings(
    findings: list
):

    normalized = []

    for finding in findings:

        category = finding.get(
            "category",
            "uncategorized"
        )

        severity = normalize_severity(
            category,
            finding.get(
                "severity",
                "WARNING"
            )
        )

        normalized_finding = dict(
            finding
        )

        normalized_finding[
            "severity"
        ] = severity

        normalized.append(
            normalized_finding
        )

    return normalized


def determine_status(
    findings: list
):

    severities = [
        finding.get(
            "severity",
            "INFO"
        )
        for finding in findings
    ]

    highest = highest_severity(
        severities
    )

    return status_from_severity(
        highest
    )


def write_validator_findings(
    validator_name: str,
    findings: list
):

    normalized_findings = normalize_findings(
        findings
    )

    status = determine_status(
        normalized_findings
    )

    payload = {
        "validator": validator_name,
        "status": status,
        "finding_count": len(
            normalized_findings
        ),
        "findings": normalized_findings
    }

    output_path = (
        findings_root()
        / f"{validator_name}.json"
    )

    output_path.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return output_path, status
