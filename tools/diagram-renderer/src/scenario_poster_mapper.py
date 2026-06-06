from __future__ import annotations

from pathlib import Path


LEVEL_ALIASES = {
    "level-1-visibility": "level-1-visibility",
    "level-2-correlation": "level-2-correlation",
    "level-3-recovery": "level-3-recovery",
    "level-4-resilience": "level-4-resilience",
    "level-5-continuity": "level-5-governance",
    "level-5-governance": "level-5-governance",
}


LEVEL_NAMES = {
    "level-1-visibility": "Visibility and Detection",
    "level-2-correlation": "Correlation and Analysis",
    "level-3-recovery": "Recovery and Automation",
    "level-4-resilience": "Resilience and Failover",
    "level-5-governance": "Continuity and Governance",
}


def title_from_slug(value: str) -> str:
    return value.replace("-", " ").title()


def normalize_lifecycle(level: str) -> str:
    return LEVEL_ALIASES.get(level, "level-1-visibility")


def as_list(value) -> list:
    if isinstance(value, list):
        return value

    if value is None:
        return []

    return [str(value)]


def first_text(items: list, fallback: str) -> str:
    if not items:
        return fallback

    first = items[0]

    if isinstance(first, dict):
        return str(first.get("title") or first.get("summary") or fallback)

    return str(first)


def make_card(title: str, subtitle: str, card_type: str, status: str, icon: str) -> dict:
    return {
        "title": title,
        "subtitle": subtitle,
        "type": card_type,
        "status": status,
        "icon": icon,
    }


def build_level_sections(lifecycle: str, metadata: dict) -> list[dict]:
    detection = as_list(metadata.get("detection_workflow"))
    correlation = as_list(metadata.get("correlation_and_analysis"))
    recovery = as_list(metadata.get("recovery_and_automation"))
    validation = as_list(metadata.get("recovery_validation"))
    components = as_list(metadata.get("infrastructure_components"))

    if lifecycle == "level-1-visibility":
        return [
            {
                "id": "observed-domain",
                "title": "Observed Domain",
                "summary": "SIGNAL SOURCE",
                "description": first_text(components, "Infrastructure component under observation."),
                "cards": [
                    make_card("Infrastructure Target", first_text(components, "Observed infrastructure target"), "target", "Observed", "🧩"),
                    make_card("Health Signal", first_text(detection, "Health and status signal collection"), "signal", "Collecting", "📡"),
                    make_card("Operational State", "Visibility condition is classified", "state", "Visible", "👁️"),
                ],
            },
            {
                "id": "telemetry-platform",
                "title": "Telemetry Platform",
                "summary": "TELEMETRY READY",
                "description": "Signals are collected, normalized, and prepared for operational visibility.",
                "cards": [
                    make_card("Metric Collection", "Metrics and health indicators", "telemetry", "Streaming", "📈"),
                    make_card("Event Collection", "Logs and event signals", "logging", "Active", "🧾"),
                    make_card("Status View", "Dashboard-ready visibility output", "dashboard", "Ready", "📊"),
                ],
            },
            {
                "id": "visibility-output",
                "title": "Visibility Output",
                "summary": "VISIBLE",
                "description": "Operational status becomes reviewer-readable through generated artifacts.",
                "cards": [
                    make_card("Detection Output", first_text(detection, "Detected operational condition"), "output", "Ready", "🚨"),
                    make_card("README Evidence", "Scenario documentation generated", "evidence", "Generated", "📄"),
                    make_card("Poster Artifact", "Operational poster rendered", "diagram", "Generated", "🖼️"),
                ],
            },
            {
                "id": "validation-status",
                "title": "Validation Status",
                "summary": "VALIDATED",
                "description": "Generated artifacts are checked for portfolio readiness.",
                "cards": [
                    make_card("Artifact Check", "README and poster references validated", "validation", "Checked", "✅"),
                    make_card("Evidence Check", "Generated evidence files prepared", "validation", "Ready", "🟢"),
                    make_card("Review State", "Portfolio-facing scenario output", "review", "Reviewable", "🔎"),
                ],
            },
        ]

    if lifecycle == "level-2-correlation":
        return [
            {
                "id": "signal-domain",
                "title": "Signal Domain",
                "summary": "MULTI-SIGNAL",
                "description": first_text(detection, "Related operational signals are collected."),
                "cards": [
                    make_card("Primary Signal", first_text(detection, "Primary symptom detected"), "signal", "Observed", "📡"),
                    make_card("Related Signal", "Additional dependency signal collected", "signal", "Collected", "📈"),
                    make_card("Component Scope", first_text(components, "Affected component identified"), "scope", "Mapped", "🧩"),
                ],
            },
            {
                "id": "correlation-platform",
                "title": "Correlation Platform",
                "summary": "CORRELATION",
                "description": first_text(correlation, "Related signals are compared and interpreted."),
                "cards": [
                    make_card("Signal Join", "Symptoms are connected across dependencies", "correlation", "Active", "🔗"),
                    make_card("Noise Reduction", "Unrelated signals are filtered", "analysis", "Filtered", "🧠"),
                    make_card("Dependency Map", "Impact path is reviewed", "dependency", "Mapped", "🗺️"),
                ],
            },
            {
                "id": "impact-analysis",
                "title": "Impact Analysis",
                "summary": "IMPACT REVIEW",
                "description": "Affected service or infrastructure scope is estimated.",
                "cards": [
                    make_card("Impact Scope", first_text(correlation, "Possible operational impact reviewed"), "impact", "Reviewed", "📊"),
                    make_card("Propagation Path", "Likely dependency path documented", "path", "Identified", "🧭"),
                    make_card("Priority Context", "Incident or response priority supported", "priority", "Prepared", "🚦"),
                ],
            },
            {
                "id": "operational-insight",
                "title": "Operational Insight",
                "summary": "INSIGHT READY",
                "description": "Correlation output becomes reviewer-readable operational insight.",
                "cards": [
                    make_card("Root Context", "Probable cause context summarized", "insight", "Ready", "💡"),
                    make_card("Evidence Output", "Analysis evidence generated", "evidence", "Generated", "📄"),
                    make_card("Review State", "Scenario reasoning is documented", "review", "Reviewable", "🔎"),
                ],
            },
        ]

    if lifecycle == "level-3-recovery":
        return [
            {
                "id": "incident-trigger",
                "title": "Incident Trigger",
                "summary": "TRIGGERED",
                "description": first_text(detection, "Operational condition requires response."),
                "cards": [
                    make_card("Trigger Signal", first_text(detection, "Incident or recovery trigger detected"), "alert", "Detected", "🚨"),
                    make_card("Affected Target", first_text(components, "Infrastructure target affected"), "target", "Impacted", "🧩"),
                    make_card("Response Need", "Recovery workflow is required", "incident", "Qualified", "⚠️"),
                ],
            },
            {
                "id": "recovery-control",
                "title": "Recovery Control",
                "summary": "CONTROL READY",
                "description": first_text(recovery, "Recovery action is selected and controlled."),
                "cards": [
                    make_card("Recovery Policy", "Recovery decision criteria reviewed", "policy", "Checked", "📋"),
                    make_card("Execution Plan", first_text(recovery, "Recovery workflow selected"), "plan", "Prepared", "🧭"),
                    make_card("Operator Control", "Manual or automation control path defined", "control", "Ready", "🎛️"),
                ],
            },
            {
                "id": "automation-execution",
                "title": "Automation Execution",
                "summary": "EXECUTING",
                "description": "Recovery workflow is executed and tracked.",
                "cards": [
                    make_card("Automation Runbook", "Operator-guided or automated action executed", "automation", "Running", "🤖"),
                    make_card("State Change", "Infrastructure state change tracked", "change", "Tracked", "🔁"),
                    make_card("Execution Result", "Execution result recorded", "result", "Recorded", "🧾"),
                ],
            },
            {
                "id": "recovery-validation",
                "title": "Recovery Validation",
                "summary": "RECOVERY READY",
                "description": first_text(validation, "Restored infrastructure state is validated."),
                "cards": [
                    make_card("Health Recheck", first_text(validation, "Health state confirmed"), "validation", "Passed", "✅"),
                    make_card("Service State", "Restored or stable state verified", "service", "Stable", "🟢"),
                    make_card("Evidence Record", "Recovery evidence summarized", "evidence", "Generated", "📄"),
                ],
            },
        ]

    if lifecycle == "level-4-resilience":
        return [
            {
                "id": "failure-domain",
                "title": "Failure Domain",
                "summary": "FAILURE SCOPE",
                "description": first_text(detection, "Failure or degradation domain is identified."),
                "cards": [
                    make_card("Failure Signal", first_text(detection, "Failure signal detected"), "failure", "Detected", "🚨"),
                    make_card("Affected Domain", first_text(components, "Affected resilience domain"), "domain", "Mapped", "🧩"),
                    make_card("Survivability Risk", "Service survivability risk recognized", "risk", "Reviewed", "⚠️"),
                ],
            },
            {
                "id": "resilience-coordination",
                "title": "Resilience Coordination",
                "summary": "COORDINATED",
                "description": "Failover or resilience response is coordinated.",
                "cards": [
                    make_card("Alternate Path", "Redundant path or site evaluated", "path", "Evaluated", "🛣️"),
                    make_card("Decision Point", "Failover decision coordinated", "decision", "Ready", "🎯"),
                    make_card("Ownership", "Operational ownership clarified", "owner", "Assigned", "👥"),
                ],
            },
            {
                "id": "failover-execution",
                "title": "Failover Execution",
                "summary": "FAILOVER ACTIVE",
                "description": first_text(recovery, "Traffic, service, or infrastructure path is shifted."),
                "cards": [
                    make_card("Routing Shift", "Traffic or service path changed", "failover", "Executed", "🔁"),
                    make_card("Continuity State", "Service continuity maintained", "continuity", "Maintained", "🟢"),
                    make_card("Execution Monitor", "Failover state monitored", "monitor", "Active", "📊"),
                ],
            },
            {
                "id": "survivability-validation",
                "title": "Survivability Validation",
                "summary": "SURVIVABLE",
                "description": first_text(validation, "Alternate path or site is validated."),
                "cards": [
                    make_card("Availability Check", "Service availability confirmed", "validation", "Passed", "✅"),
                    make_card("Path Validation", "Alternate path validated", "path", "Verified", "🔎"),
                    make_card("Evidence Report", "Resilience outcome documented", "evidence", "Generated", "📄"),
                ],
            },
        ]

    return [
        {
            "id": "continuity-scope",
            "title": "Continuity Scope",
            "summary": "SCOPE DEFINED",
            "description": "Business or service continuity scope is defined.",
            "cards": [
                make_card("Critical Service", first_text(components, "Critical infrastructure dependency"), "service", "Identified", "🏢"),
                make_card("Continuity Risk", "Operational continuity risk framed", "risk", "Reviewed", "⚠️"),
                make_card("Governance Scope", "Governance review scope defined", "governance", "Defined", "📋"),
            ],
        },
        {
            "id": "governance-control",
            "title": "Governance Control",
            "summary": "CONTROLLED",
            "description": "Decision criteria and escalation context are documented.",
            "cards": [
                make_card("Decision Criteria", "Continuity decision criteria documented", "policy", "Ready", "📋"),
                make_card("Risk Ownership", "Risk ownership clarified", "owner", "Assigned", "👥"),
                make_card("Operational Guardrail", "Governance guardrail referenced", "control", "Active", "🛡️"),
            ],
        },
        {
            "id": "executive-coordination",
            "title": "Executive Coordination",
            "summary": "COORDINATED",
            "description": "Cross-team continuity status is summarized.",
            "cards": [
                make_card("Status Summary", "Continuity status prepared", "summary", "Ready", "📊"),
                make_card("Communication", "Coordination context prepared", "communication", "Prepared", "📣"),
                make_card("Decision Support", "Reviewer-facing interpretation produced", "decision", "Ready", "🎯"),
            ],
        },
        {
            "id": "evidence-reporting",
            "title": "Evidence Reporting",
            "summary": "REPORTED",
            "description": "Continuity evidence is prepared for portfolio review.",
            "cards": [
                make_card("Evidence Summary", "Scenario artifacts summarized", "evidence", "Generated", "📄"),
                make_card("Validation Record", "Validation status recorded", "validation", "Ready", "✅"),
                make_card("Portfolio Output", "Continuity artifact reviewable", "review", "Reviewable", "🔎"),
            ],
        },
    ]


def build_workflow_steps(lifecycle: str, metadata: dict) -> dict:
    steps_by_level = {
        "level-1-visibility": [
            ("Collect", "Collect telemetry and health signals.", "Collecting"),
            ("Detect", "Identify visibility gaps or degraded state.", "Detected"),
            ("Publish", "Expose dashboard and evidence output.", "Published"),
            ("Validate", "Confirm signal freshness and coverage.", "Validated"),
        ],
        "level-2-correlation": [
            ("Collect", "Collect related operational signals.", "Collected"),
            ("Correlate", "Map dependency and symptom relationships.", "Correlated"),
            ("Assess", "Estimate service impact and priority.", "Assessed"),
            ("Prepare", "Prepare incident context and evidence.", "Prepared"),
        ],
        "level-3-recovery": [
            ("Trigger", "Confirm recovery trigger and affected target.", "Triggered"),
            ("Select", "Select controlled recovery workflow.", "Selected"),
            ("Execute", "Run automation or operator action.", "Executed"),
            ("Validate", "Confirm restored and stable state.", "Validated"),
        ],
        "level-4-resilience": [
            ("Scope", "Identify failure domain and risk boundary.", "Scoped"),
            ("Decide", "Select alternate path or failover action.", "Decided"),
            ("Failover", "Coordinate distributed resilience execution.", "Active"),
            ("Validate", "Confirm survivability and continuity state.", "Validated"),
        ],
        "level-5-governance": [
            ("Scope", "Define continuity scope and critical service.", "Scoped"),
            ("Review", "Review operational risk and ownership.", "Reviewed"),
            ("Decide", "Coordinate governance decision and approval.", "Approved"),
            ("Report", "Publish continuity evidence and summary.", "Reported"),
        ],
    }

    selected_steps = steps_by_level.get(
        lifecycle,
        steps_by_level["level-1-visibility"]
    )

    return {
        "title": "Operational Workflow",
        "steps": [
            {
                "title": title,
                "description": description,
                "status": status,
            }
            for title, description, status in selected_steps
        ],
    }


def build_dashboards(metadata: dict) -> list[dict]:
    modules = as_list(metadata.get("used_modules"))
    adapters = as_list(metadata.get("used_adapters"))

    return [
        {
            "title": "Scenario Readiness",
            "widgets": [
                {
                    "label": "Modules",
                    "value": str(len(modules)),
                    "status": "normal",
                },
                {
                    "label": "Adapters",
                    "value": str(len(adapters)),
                    "status": "normal",
                },
                {
                    "label": "README",
                    "value": "Generated",
                    "status": "verified",
                },
                {
                    "label": "Poster",
                    "value": "Generated",
                    "status": "verified",
                },
                {
                    "label": "Evidence",
                    "value": "Ready",
                    "status": "healthy",
                },
            ],
        }
    ]


def build_legend(lifecycle: str) -> list[dict]:
    if lifecycle == "level-3-recovery":
        return [
            {"label": "Incident Trigger", "color": "red"},
            {"label": "Recovery Control", "color": "purple"},
            {"label": "Automation Execution", "color": "cyan"},
            {"label": "Recovery Validation", "color": "green"},
        ]

    if lifecycle == "level-4-resilience":
        return [
            {"label": "Failure Domain", "color": "red"},
            {"label": "Resilience Coordination", "color": "purple"},
            {"label": "Failover Execution", "color": "cyan"},
            {"label": "Survivability Validation", "color": "green"},
        ]

    if lifecycle == "level-2-correlation":
        return [
            {"label": "Signal Domain", "color": "blue"},
            {"label": "Correlation Platform", "color": "purple"},
            {"label": "Impact Analysis", "color": "cyan"},
            {"label": "Operational Insight", "color": "green"},
        ]

    if lifecycle == "level-5-governance":
        return [
            {"label": "Continuity Scope", "color": "blue"},
            {"label": "Governance Control", "color": "purple"},
            {"label": "Executive Coordination", "color": "cyan"},
            {"label": "Evidence Reporting", "color": "green"},
        ]

    return [
        {"label": "Observed Domain", "color": "blue"},
        {"label": "Telemetry Platform", "color": "cyan"},
        {"label": "Visibility Output", "color": "green"},
        {"label": "Validation Status", "color": "yellow"},
    ]


def build_poster_data_from_scenario_metadata(
    metadata_path: Path,
    metadata: dict,
) -> dict:
    scenario_name = metadata.get("scenario_name") or metadata_path.parent.name
    lifecycle_raw = metadata.get("lifecycle_level") or metadata_path.parent.parent.name
    lifecycle = normalize_lifecycle(lifecycle_raw)

    title = (
        metadata.get("scenario_title")
        or metadata.get("title")
        or title_from_slug(scenario_name)
    )

    summary = metadata.get("summary") or f"{title} operational scenario."

    return {
        "poster": {
            "title": title,
            "subtitle": "Scenario-driven Infrastructure Operations Portfolio",
            "scenario": scenario_name,
            "lifecycle": lifecycle,
            "level": LEVEL_NAMES.get(lifecycle, lifecycle_raw),
            "scope": metadata.get("operational_scope") or "Infrastructure Operations",
            "environment": metadata.get("environment") or "Hybrid Infrastructure",
            "width": 2600,
            "height": 1900,
        },
        "sections": build_level_sections(lifecycle, metadata),
        "workflow": build_workflow_steps(lifecycle, metadata),
        "summary": {
            "title": "Scenario Summary",
            "items": [
                summary,
                f"Lifecycle: {LEVEL_NAMES.get(lifecycle, lifecycle_raw)}",
                f"Scenario: {scenario_name}",
                "Artifact: operational-poster",
            ],
        },
        "dashboards": build_dashboards(metadata),
        "legend": build_legend(lifecycle),
    }

def map_metadata_to_poster(metadata):
    return build_poster_data(metadata)






def map_metadata_to_poster(metadata):
    lifecycle = (
        metadata.get("lifecycle_level")
        or metadata.get("lifecycle")
        or metadata.get("level")
        or ""
    )

    return build_poster_data_from_scenario_metadata(
        lifecycle,
        metadata
    )

