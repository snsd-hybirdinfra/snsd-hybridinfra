DEFAULT_SEVERITY = "WARNING"


CATEGORY_SEVERITY = {

    "missing-recommended-diagram": "WARNING",
    "missing-required-diagram": "ERROR",
    "lifecycle-semantic-leakage": "WARNING",
    "missing-runtime-artifact": "ERROR",
    "gold-reference-violation": "CRITICAL",
    "invalid-lifecycle-transition": "ERROR",
    "missing-related-scenario": "WARNING",
    "taxonomy-violation": "ERROR",
    "capability-boundary-violation": "ERROR"
}


SEVERITY_RANK = {
    "INFO": 0,
    "WARNING": 1,
    "ERROR": 2,
    "CRITICAL": 3
}


def normalize_severity(
    category: str,
    fallback: str = DEFAULT_SEVERITY
):

    return CATEGORY_SEVERITY.get(
        category,
        fallback
    )


def highest_severity(
    severities: list
):

    if not severities:

        return "INFO"

    return max(
        severities,
        key=lambda severity: SEVERITY_RANK.get(
            severity,
            0
        )
    )


def status_from_severity(
    severity: str
):

    if severity == "CRITICAL":

        return "FAILED"

    if severity in [
        "WARNING",
        "ERROR"
    ]:

        return "WARNING"

    return "COMPLETED"

