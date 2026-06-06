from src.text_utils import escape_truncated
from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED


def count_cards(
    data: dict,
    section_id: str
):

    for section in data.get(
        "sections",
        []
    ):

        if section.get(
            "id"
        ) == section_id:

            return len(
                section.get(
                    "cards",
                    []
                )
            )

    return 0


def get_summary_title(
    data: dict
):

    lifecycle = data.get(
        "poster",
        {}
    ).get(
        "lifecycle",
        ""
    )

    if lifecycle == "level-1-visibility":

        return "Visibility Summary"

    if lifecycle == "level-2-correlation":

        return "Correlation Summary"

    if lifecycle == "level-3-recovery":

        return "Recovery Summary"

    if lifecycle == "level-4-resilience":

        return "Resilience Summary"

    if lifecycle == "level-5-governance":

        return "Governance Summary"

    return "Operational Summary"


def get_summary_subtitle(
    data: dict
):

    lifecycle = data.get(
        "poster",
        {}
    ).get(
        "lifecycle",
        ""
    )

    if lifecycle == "level-1-visibility":

        return "Telemetry, detection, and validation coverage"

    if lifecycle == "level-2-correlation":

        return "Signals, dependency, impact, and insight coverage"

    if lifecycle == "level-3-recovery":

        return "Trigger, control, automation, and validation coverage"

    if lifecycle == "level-4-resilience":

        return "Failure, coordination, failover, and survivability coverage"

    if lifecycle == "level-5-governance":

        return "Scope, governance, decision, and evidence coverage"

    return "Scenario coverage overview"


def get_summary_items(
    data: dict
):

    lifecycle = data.get(
        "poster",
        {}
    ).get(
        "lifecycle",
        ""
    )

    if lifecycle == "level-1-visibility":

        return [
            {
                "label": "Domains",
                "value": count_cards(
                    data,
                    "observed-domain"
                )
            },
            {
                "label": "Telemetry",
                "value": count_cards(
                    data,
                    "telemetry-platform"
                )
            },
            {
                "label": "Outputs",
                "value": count_cards(
                    data,
                    "visibility-output"
                )
            },
            {
                "label": "Validation",
                "value": count_cards(
                    data,
                    "validation-status"
                )
            }
        ]

    if lifecycle == "level-2-correlation":

        return [
            {
                "label": "Signals",
                "value": count_cards(
                    data,
                    "signal-domain"
                )
            },
            {
                "label": "Correlation",
                "value": count_cards(
                    data,
                    "correlation-platform"
                )
            },
            {
                "label": "Impact",
                "value": count_cards(
                    data,
                    "impact-analysis"
                )
            },
            {
                "label": "Insights",
                "value": count_cards(
                    data,
                    "operational-insight"
                )
            }
        ]

    if lifecycle == "level-3-recovery":

        return [
            {
                "label": "Triggers",
                "value": count_cards(
                    data,
                    "incident-trigger"
                )
            },
            {
                "label": "Controls",
                "value": count_cards(
                    data,
                    "recovery-control"
                )
            },
            {
                "label": "Actions",
                "value": count_cards(
                    data,
                    "automation-execution"
                )
            },
            {
                "label": "Validation",
                "value": count_cards(
                    data,
                    "recovery-validation"
                )
            }
        ]

    if lifecycle == "level-4-resilience":

        return [
            {
                "label": "Failures",
                "value": count_cards(
                    data,
                    "failure-domain"
                )
            },
            {
                "label": "Coordination",
                "value": count_cards(
                    data,
                    "resilience-coordination"
                )
            },
            {
                "label": "Failover",
                "value": count_cards(
                    data,
                    "failover-execution"
                )
            },
            {
                "label": "Survivability",
                "value": count_cards(
                    data,
                    "survivability-validation"
                )
            }
        ]

    if lifecycle == "level-5-governance":

        return [
            {
                "label": "Scope",
                "value": count_cards(
                    data,
                    "continuity-scope"
                )
            },
            {
                "label": "Governance",
                "value": count_cards(
                    data,
                    "governance-control"
                )
            },
            {
                "label": "Decision",
                "value": count_cards(
                    data,
                    "executive-coordination"
                )
            },
            {
                "label": "Evidence",
                "value": count_cards(
                    data,
                    "evidence-reporting"
                )
            }
        ]

    return []


def render_summary(
    data: dict,
    layout: dict
):

    summary_layout = layout.get(
        "summary",
        layout
    )

    x = summary_layout["x"]
    y = summary_layout["y"]
    width = summary_layout["width"]
    height = summary_layout["height"]

    title = escape_truncated(
        get_summary_title(
            data
        ),
        26
    )

    subtitle = escape_truncated(
        get_summary_subtitle(
            data
        ),
        48
    )

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="26" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 28}" y="{y + 42}" '
        f'fill="{TEXT_PRIMARY}" font-size="22" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 28}" y="{y + 70}" '
        f'fill="{TEXT_SECONDARY}" font-size="13">'
        f'{subtitle}</text>'
    ]

    items = get_summary_items(
        data
    )

    item_y = y + 108

    for index, item in enumerate(
        items
    ):

        current_y = item_y + index * 42

        label = escape_truncated(
            item.get(
                "label",
                ""
            ),
            16
        )

        value = escape_truncated(
            item.get(
                "value",
                ""
            ),
            6
        )

        elements.extend(
            [
                f'<rect x="{x + 28}" y="{current_y - 22}" '
                f'width="{width - 56}" height="32" rx="16" '
                f'fill="#020617" stroke="#334155" stroke-width="1" />',

                f'<text x="{x + 50}" y="{current_y}" '
                f'fill="{TEXT_MUTED}" font-size="13" font-weight="bold">'
                f'{label}</text>',

                f'<text x="{x + width - 54}" y="{current_y}" '
                f'fill="{TEXT_PRIMARY}" font-size="16" text-anchor="end" font-weight="bold">'
                f'{value}</text>'
            ]
        )

    return elements


def render_summary_panel(
    data: dict,
    layout: dict
):

    return render_summary(
        data,
        layout
    )


