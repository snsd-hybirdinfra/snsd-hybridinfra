from pathlib import Path
import json


def resolve_repo_root():

    return Path(__file__).resolve().parents[3]


def validator_findings_path(
    validator_name: str
):

    return (
        resolve_repo_root()
        / "reports"
        / "validators"
        / "findings"
        / f"{validator_name}.json"
    )


def read_validator_findings_status(
    validator_name: str
):

    path = validator_findings_path(
        validator_name
    )

    if not path.exists():

        return None

    payload = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    return payload.get(
        "status"
    )
