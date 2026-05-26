from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parents[3]
        / "tools"
    )
)

from shared_runtime.src.runtime_encoding import (
    configure_runtime_encoding
)

from shared_runtime.src.validator_findings import (
    write_validator_findings
)

configure_runtime_encoding()

import re
import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

SCENARIOS_ROOT = (
    REPO_ROOT
    / "scenarios"
)

POLICY_PATH = (
    Path(__file__).resolve().parent
    / "rules"
    / "diagram-policy.yaml"
)


IMAGE_PATTERN = re.compile(
    r"!\[[^\]]*\]\((\.\/diagrams\/[^)]+)\)"
)


def is_strict_golden_scenario(
    readme_path: Path
):

    return "vpn-latency-visibility" in str(
        readme_path
    )


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def extract_lifecycle(
    readme_path: Path
):

    for part in readme_path.parts:

        if part.startswith(
            "level-"
        ):

            return part

    return None


def extract_scenario_name(
    readme_path: Path
):

    return readme_path.parent.name


def extract_diagram_references(
    readme_path: Path
):

    content = readme_path.read_text(
        encoding="utf-8"
    )

    return IMAGE_PATTERN.findall(
        content
    )


def extract_diagram_name(
    reference: str
):

    return (
        Path(reference)
        .stem
    )


def validate_missing_diagram(
    findings: list,
    readme_path: Path,
    diagram_path: Path,
    diagram_name: str,
    policy: dict
):

    lifecycle = extract_lifecycle(
        readme_path
    )

    scenario = extract_scenario_name(
        readme_path
    )

    requirement = (
        policy
        .get(lifecycle, {})
        .get(
            diagram_name,
            "optional"
        )
    )

    if requirement == "optional":

        return

    category = (
        "missing-recommended-diagram"
        if requirement == "recommended"
        else "missing-required-diagram"
    )

    message = (
        f"Missing {requirement} diagram: "
        f"{diagram_path}"
    )

    findings.append(
        {
            "severity": "WARNING",
            "category": category,
            "scenario": scenario,
            "lifecycle": lifecycle,
            "diagram": diagram_name,
            "path": str(diagram_path),
            "message": message
        }
    )

    print(
        f"WARNING: {message}"
    )


def validate_readme_diagrams(
    readme_path: Path,
    policy: dict,
    findings: list
):

    scenario_dir = readme_path.parent

    references = extract_diagram_references(
        readme_path
    )

    for reference in references:

        diagram_name = extract_diagram_name(
            reference
        )

        diagram_path = (
            scenario_dir
            / reference.replace(
                "./",
                ""
            )
        )

        if not diagram_path.exists():

            if is_strict_golden_scenario(
                readme_path
            ):

                raise FileNotFoundError(
                    f"Missing referenced diagram: "
                    f"{diagram_path}"
                )

            validate_missing_diagram(
                findings,
                readme_path,
                diagram_path,
                diagram_name,
                policy
            )

            continue

        if (
            diagram_path.suffix == ".png"
            and is_strict_golden_scenario(
                readme_path
            )
        ):

            svg_path = diagram_path.with_suffix(
                ".svg"
            )

            spec_path = diagram_path.with_suffix(
                ".spec.yaml"
            )

            if not svg_path.exists():

                raise FileNotFoundError(
                    f"Missing SVG source for PNG: "
                    f"{svg_path}"
                )

            if not spec_path.exists():

                raise FileNotFoundError(
                    f"Missing diagram spec for PNG: "
                    f"{spec_path}"
                )

    return len(
        references
    )


def main():

    policy = load_yaml(
        POLICY_PATH
    )

    readmes = sorted(
        SCENARIOS_ROOT.rglob(
            "README.md"
        )
    )

    findings = []
    checked = 0
    references = 0

    for readme in readmes:

        checked += 1

        references += validate_readme_diagrams(
            readme,
            policy,
            findings
        )

    output_path, status = write_validator_findings(
        "diagram-consistency-validator",
        findings
    )

    print(
        f"Diagram consistency validation completed. "
        f"README files checked: {checked}, "
        f"diagram references checked: {references}, "
        f"findings: {len(findings)}"
    )

    print(
        f"Validator findings written: {output_path}"
    )

    print(
        f"Validator status: {status}"
    )


if __name__ == "__main__":
    main()
