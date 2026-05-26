EXCLUSION_CONTEXT = [

    "excluded",
    "intentionally excluded",
    "not introduced",
    "does not",
    "without",
    "remain intentionally excluded",
    "excluded from",
    "intentionally avoids",
    "outside lifecycle scope",
    "not part of",
    "not responsible for",
    "is not responsible for",
    "not included",
    "not performed",
    "not executed",
    "not triggered",
    "avoid",
    "avoids"
]


def detect_lifecycle_level(
    readme_path
):

    return readme_path.parent.parent.name


def detect_scenario_name(
    readme_path
):

    return readme_path.parent.name


def is_excluded_context(
    content,
    term
):

    term_index = content.find(
        term.lower()
    )

    if term_index == -1:

        return False

    start = max(
        0,
        term_index - 120
    )

    context = content[
        start:term_index
    ]

    for exclusion in EXCLUSION_CONTEXT:

        if exclusion.lower() in context:

            return True

    return False


def validate_readme(
    readme_path,
    rules
):

    lifecycle_level = detect_lifecycle_level(
        readme_path
    )

    scenario = detect_scenario_name(
        readme_path
    )

    lifecycle_rules = rules.get(
        lifecycle_level,
        {}
    )

    forbidden_terms = lifecycle_rules.get(
        "forbidden",
        []
    )

    content = readme_path.read_text(
        encoding="utf-8"
    ).lower()

    findings = []

    for term in forbidden_terms:

        if term.lower() not in content:

            continue

        if is_excluded_context(
            content,
            term
        ):

            continue

        findings.append(
            {
                "severity": "WARNING",
                "category": "lifecycle-semantic-leakage",
                "scenario": scenario,
                "lifecycle": lifecycle_level,
                "term": term,
                "file": str(readme_path),
                "message": (
                    f"Forbidden lifecycle term '{term}' "
                    f"found in {lifecycle_level} scenario "
                    f"{scenario}"
                )
            }
        )

    return findings
