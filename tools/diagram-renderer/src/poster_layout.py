def build_l1_visibility_layout(
    poster: dict
):

    width = poster.get("width", 2600)
    height = poster.get("height", 1900)

    return {
        "canvas": {"width": width, "height": height},
        "header": {"x": 60, "y": 40, "width": width - 120, "height": 130},
        "main": {"x": 60, "y": 200, "width": 1880, "height": 1120},
        "workflow": {"x": 1990, "y": 200, "width": 550, "height": 760},
        "summary": {"x": 1990, "y": 990, "width": 550, "height": 300},
        "legend": {"x": 1990, "y": 1320, "width": 550, "height": 330},
        "dashboard": {"x": 60, "y": 1345, "width": 1880, "height": 320},
        "sections": {
            "observed-domain": {"x": 80, "y": 220, "width": 1840, "height": 230},
            "telemetry-platform": {"x": 80, "y": 490, "width": 1840, "height": 230},
            "visibility-output": {"x": 80, "y": 760, "width": 1840, "height": 230},
            "validation-status": {"x": 80, "y": 1030, "width": 1840, "height": 230}
        }
    }


def build_l2_correlation_layout(
    poster: dict
):

    width = poster.get("width", 2600)
    height = poster.get("height", 1900)

    return {
        "canvas": {"width": width, "height": height},
        "header": {"x": 60, "y": 40, "width": width - 120, "height": 130},
        "main": {"x": 60, "y": 200, "width": 1880, "height": 1120},
        "workflow": {"x": 1990, "y": 200, "width": 550, "height": 760},
        "summary": {"x": 1990, "y": 990, "width": 550, "height": 300},
        "legend": {"x": 1990, "y": 1320, "width": 550, "height": 330},
        "dashboard": {"x": 60, "y": 1345, "width": 1880, "height": 320},
        "sections": {
            "signal-domain": {"x": 80, "y": 220, "width": 1840, "height": 220},
            "correlation-platform": {"x": 80, "y": 480, "width": 1840, "height": 280},
            "impact-analysis": {"x": 80, "y": 800, "width": 1840, "height": 220},
            "operational-insight": {"x": 80, "y": 1060, "width": 1840, "height": 220}
        }
    }


def build_l3_recovery_layout(
    poster: dict
):

    width = poster.get("width", 2600)
    height = poster.get("height", 1900)

    return {
        "canvas": {"width": width, "height": height},
        "header": {"x": 60, "y": 40, "width": width - 120, "height": 130},
        "main": {"x": 60, "y": 200, "width": 1880, "height": 1120},
        "workflow": {"x": 1990, "y": 200, "width": 550, "height": 760},
        "summary": {"x": 1990, "y": 990, "width": 550, "height": 300},
        "legend": {"x": 1990, "y": 1320, "width": 550, "height": 420},
        "dashboard": {"x": 60, "y": 1345, "width": 1880, "height": 420},
        "sections": {
            "incident-trigger": {"x": 80, "y": 220, "width": 1840, "height": 220},
            "recovery-control": {"x": 80, "y": 470, "width": 1840, "height": 280},
            "automation-execution": {"x": 80, "y": 780, "width": 1840, "height": 270},
            "recovery-validation": {"x": 80, "y": 1080, "width": 1840, "height": 220}
        }
    }


def build_l4_resilience_layout(
    poster: dict
):

    width = poster.get("width", 2600)
    height = poster.get("height", 1900)

    return {
        "canvas": {"width": width, "height": height},
        "header": {"x": 60, "y": 40, "width": width - 120, "height": 130},
        "main": {"x": 60, "y": 200, "width": 1880, "height": 1120},
        "workflow": {"x": 1990, "y": 200, "width": 550, "height": 760},
        "summary": {"x": 1990, "y": 990, "width": 550, "height": 300},
        "legend": {"x": 1990, "y": 1320, "width": 550, "height": 420},
        "dashboard": {"x": 60, "y": 1345, "width": 1880, "height": 420},
        "sections": {
            "failure-domain": {"x": 80, "y": 220, "width": 1840, "height": 220},
            "resilience-coordination": {"x": 80, "y": 470, "width": 1840, "height": 280},
            "failover-execution": {"x": 80, "y": 780, "width": 1840, "height": 270},
            "survivability-validation": {"x": 80, "y": 1080, "width": 1840, "height": 220}
        }
    }


def build_l5_governance_layout(
    poster: dict
):

    width = poster.get("width", 2600)
    height = poster.get("height", 1900)

    return {
        "canvas": {"width": width, "height": height},
        "header": {"x": 60, "y": 40, "width": width - 120, "height": 130},
        "main": {"x": 60, "y": 200, "width": 1880, "height": 1120},
        "workflow": {"x": 1990, "y": 200, "width": 550, "height": 760},
        "summary": {"x": 1990, "y": 990, "width": 550, "height": 300},
        "legend": {"x": 1990, "y": 1320, "width": 550, "height": 420},
        "dashboard": {"x": 60, "y": 1345, "width": 1880, "height": 420},
        "sections": {
            "continuity-scope": {"x": 80, "y": 220, "width": 1840, "height": 220},
            "governance-control": {"x": 80, "y": 470, "width": 1840, "height": 280},
            "executive-coordination": {"x": 80, "y": 780, "width": 1840, "height": 270},
            "evidence-reporting": {"x": 80, "y": 1080, "width": 1840, "height": 220}
        }
    }


def build_layout(
    poster: dict
):

    lifecycle = poster.get(
        "lifecycle",
        ""
    )

    if lifecycle == "level-1-visibility":
        return build_l1_visibility_layout(poster)

    if lifecycle == "level-2-correlation":
        return build_l2_correlation_layout(poster)

    if lifecycle == "level-3-recovery":
        return build_l3_recovery_layout(poster)

    if lifecycle == "level-4-resilience":
        return build_l4_resilience_layout(poster)

    if lifecycle in ("level-5-continuity", "level-5-governance"):
        return build_l5_governance_layout(poster)

    return build_l1_visibility_layout(poster)


