from pathlib import Path
import re


SCENARIO_LINK_PATTERN = re.compile(
    r"/scenarios/(level-[^/\s|)]+)/([^/\s|)]+)"
)


SECTION_PATTERN = re.compile(
    r"## Related Scenarios(?P<body>.*?)(?:\n## |\Z)",
    re.DOTALL
)


PREVIOUS_PATTERN = re.compile(
    r"(?:Previous|Previous Scenarios|Previous Scenario)(?P<body>.*?)(?:Next|Next Scenarios|Next Scenario|$)",
    re.DOTALL | re.IGNORECASE
)


NEXT_PATTERN = re.compile(
    r"(?:Next|Next Scenarios|Next Scenario)(?P<body>.*)",
    re.DOTALL | re.IGNORECASE
)


def detect_lifecycle_level(
    readme_path: Path
):

    return readme_path.parent.parent.name


def detect_scenario_name(
    readme_path: Path
):

    return readme_path.parent.name


def extract_related_section(
    content: str
):

    match = SECTION_PATTERN.search(
        content
    )

    if not match:

        return ""

    return match.group(
        "body"
    )


def extract_links(
    content: str
):

    links = []

    for match in SCENARIO_LINK_PATTERN.finditer(
        content
    ):

        links.append(
            {
                "level": match.group(1).strip(),
                "scenario": match.group(2).strip(),
                "path": match.group(0).strip()
            }
        )

    return links


def extract_previous_links(
    related_section: str
):

    match = PREVIOUS_PATTERN.search(
        related_section
    )

    if not match:

        return []

    return extract_links(
        match.group(
            "body"
        )
    )


def extract_next_links(
    related_section: str
):

    match = NEXT_PATTERN.search(
        related_section
    )

    if not match:

        return []

    return extract_links(
        match.group(
            "body"
        )
    )


def target_readme_path(
    readme_path: Path,
    related_level: str,
    related_scenario: str
):

    scenarios_root = readme_path.parents[2]

    return (
        scenarios_root
        / related_level
        / related_scenario
        / "README.md"
    )


def validate_path_exists(
    findings: list,
    readme_path: Path,
    scenario: str,
    lifecycle: str,
    relationship: dict
):

    target_path = target_readme_path(
        readme_path,
        relationship["level"],
        relationship["scenario"]
    )

    if target_path.exists():

        return

    findings.append(
        {
            "file": str(readme_path),
            "scenario": scenario,
            "lifecycle": lifecycle,
            "related_path": relationship["path"],
            "related_level": relationship["level"],
            "severity": "WARNING",
            "message": "Related scenario path does not exist"
        }
    )


def validate_previous_relationship(
    findings: list,
    readme_path: Path,
    scenario: str,
    lifecycle: str,
    relationship: dict,
    rules: dict
):

    previous_allowed = (
        rules
        .get("allowed_transitions", {})
        .get(relationship["level"], {})
        .get("next", [])
    )

    if lifecycle not in previous_allowed:

        findings.append(
            {
                "file": str(readme_path),
                "scenario": scenario,
                "lifecycle": lifecycle,
                "related_path": relationship["path"],
                "related_level": relationship["level"],
                "severity": "WARNING",
                "message": (
                    f"Invalid previous lifecycle transition: "
                    f"{relationship['level']} -> {lifecycle}"
                )
            }
        )


def validate_next_relationship(
    findings: list,
    readme_path: Path,
    scenario: str,
    lifecycle: str,
    relationship: dict,
    rules: dict
):

    next_allowed = (
        rules
        .get("allowed_transitions", {})
        .get(lifecycle, {})
        .get("next", [])
    )

    if relationship["level"] not in next_allowed:

        findings.append(
            {
                "file": str(readme_path),
                "scenario": scenario,
                "lifecycle": lifecycle,
                "related_path": relationship["path"],
                "related_level": relationship["level"],
                "severity": "WARNING",
                "message": (
                    f"Invalid next lifecycle transition: "
                    f"{lifecycle} -> {relationship['level']}"
                )
            }
        )


def validate_relationships(
    readme_path: Path,
    rules: dict
):

    findings = []

    lifecycle = detect_lifecycle_level(
        readme_path
    )

    scenario = detect_scenario_name(
        readme_path
    )

    content = readme_path.read_text(
        encoding="utf-8"
    )

    related_section = extract_related_section(
        content
    )

    previous_links = extract_previous_links(
        related_section
    )

    next_links = extract_next_links(
        related_section
    )

    for relationship in previous_links:

        validate_path_exists(
            findings,
            readme_path,
            scenario,
            lifecycle,
            relationship
        )

        validate_previous_relationship(
            findings,
            readme_path,
            scenario,
            lifecycle,
            relationship,
            rules
        )

    for relationship in next_links:

        validate_path_exists(
            findings,
            readme_path,
            scenario,
            lifecycle,
            relationship
        )

        validate_next_relationship(
            findings,
            readme_path,
            scenario,
            lifecycle,
            relationship,
            rules
        )

    return findings
