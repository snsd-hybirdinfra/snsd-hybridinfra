from pathlib import Path
import sys
import yaml


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[1]
SCENARIOS_ROOT = REPO_ROOT / "scenarios"


LEVEL_CONFIG = {
    "level-1-visibility": {
        "lifecycle": "level-1-visibility",
        "workflow_title": "Visibility Workflow",
        "sections": [
            ("observed-domain", "Observed Infrastructure Domain", "OBSERVED DOMAIN"),
            ("telemetry-platform", "Telemetry Collection & Visibility Platform", "SIGNALS ACTIVE"),
            ("visibility-output", "Operational Visibility Outputs", "VISIBILITY READY"),
            ("validation-status", "Validation & Current Status", "STATUS VERIFIED"),
        ],
        "workflow_steps": [
            ("Detect", "Observe infrastructure health and service state.", "Ready"),
            ("Collect", "Collect telemetry, logs, and probe signals.", "Active"),
            ("Visualize", "Expose status through monitoring dashboards.", "Visible"),
            ("Validate", "Confirm operational visibility and health state.", "Verified"),
        ],
        "legend": [
            ("Observed Infrastructure", "blue"),
            ("Telemetry Collection", "cyan"),
            ("Visibility Output", "green"),
            ("Validation Status", "yellow"),
        ],
    },
    "level-2-correlation": {
        "lifecycle": "level-2-correlation",
        "workflow_title": "Correlation Workflow",
        "sections": [
            ("signal-domain", "Signal & Service Domains", "SIGNAL DOMAINS"),
            ("correlation-platform", "Monitoring & Correlation Platform", "CORRELATION ACTIVE"),
            ("impact-analysis", "Dependency & Impact Analysis", "IMPACT MAPPED"),
            ("operational-insight", "Operational Insight & Decision Support", "INSIGHT READY"),
        ],
        "workflow_steps": [
            ("Detect", "Capture symptoms and abnormal operational signals.", "Ready"),
            ("Correlate", "Join infrastructure, service, and dependency signals.", "Analyzing"),
            ("Map Impact", "Identify affected services and dependent paths.", "Mapped"),
            ("Prioritize", "Assign operational severity and response priority.", "Calculated"),
            ("Escalate", "Prepare incident context and reviewer evidence.", "Ready"),
        ],
        "legend": [
            ("Signal Domain", "blue"),
            ("Correlation Platform", "purple"),
            ("Impact Analysis", "red"),
            ("Operational Insight", "green"),
            ("Operational Decision Point", "yellow"),
        ],
    },
    "level-3-recovery": {
        "lifecycle": "level-3-recovery",
        "workflow_title": "Recovery Workflow",
        "sections": [
            ("incident-trigger", "Incident Trigger & Recovery Signal", "TRIGGER DETECTED"),
            ("recovery-control", "Recovery Decision & Orchestration", "RECOVERY CONTROL"),
            ("automation-execution", "Automation Execution", "ACTION READY"),
            ("recovery-validation", "Post-Recovery Validation", "VALIDATION READY"),
        ],
        "workflow_steps": [
            ("Detect", "Identify degradation and recovery trigger.", "Detected"),
            ("Evaluate", "Check policy, dependency, and recovery eligibility.", "Evaluating"),
            ("Execute", "Run approved recovery automation actions.", "Ready"),
            ("Validate", "Confirm service restoration and stability.", "Verified"),
            ("Report", "Prepare recovery evidence and operational summary.", "Prepared"),
        ],
        "legend": [
            ("Incident Trigger", "red"),
            ("Recovery Control", "purple"),
            ("Automation Execution", "cyan"),
            ("Recovery Validation", "green"),
            ("Core Recovery Capability", "purple"),
            ("Automation Action Point", "cyan"),
        ],
    },
    "level-4-resilience": {
        "lifecycle": "level-4-resilience",
        "workflow_title": "Resilience Workflow",
        "sections": [
            ("failure-domain", "Failure Domain & Resilience Signal", "FAILURE DOMAIN"),
            ("resilience-coordination", "Resilience Coordination", "COORDINATION ACTIVE"),
            ("failover-execution", "Failover Execution", "FAILOVER READY"),
            ("survivability-validation", "Survivability Validation", "SURVIVABILITY VERIFIED"),
        ],
        "workflow_steps": [
            ("Detect", "Identify site, path, or service degradation.", "Detected"),
            ("Coordinate", "Evaluate topology, policy, and continuity targets.", "Evaluating"),
            ("Failover", "Move traffic to healthy site or route path.", "Ready"),
            ("Stabilize", "Confirm route and service stability.", "Normal"),
            ("Validate", "Collect survivability evidence and report state.", "Verified"),
        ],
        "legend": [
            ("Failure Domain", "red"),
            ("Resilience Coordination", "purple"),
            ("Failover Execution", "cyan"),
            ("Survivability Validation", "green"),
            ("Core Resilience Capability", "purple"),
            ("Failover Decision Point", "cyan"),
        ],
    },
    "level-5-continuity": {
        "lifecycle": "level-5-continuity",
        "workflow_title": "Continuity Governance Workflow",
        "sections": [
            ("continuity-scope", "Continuity Scope", "ENTERPRISE SCOPE"),
            ("governance-control", "Governance Control", "GOVERNANCE ACTIVE"),
            ("executive-coordination", "Executive Coordination", "DECISION READY"),
            ("evidence-reporting", "Evidence Reporting", "REPORTING READY"),
        ],
        "workflow_steps": [
            ("Assess", "Define enterprise continuity scope and affected services.", "Assessed"),
            ("Govern", "Evaluate risk, policy, and escalation authority.", "Evaluating"),
            ("Decide", "Authorize continuity recovery decision.", "Ready"),
            ("Report", "Prepare evidence and executive recovery report.", "Prepared"),
            ("Review", "Complete governance review and audit trail.", "Verified"),
        ],
        "legend": [
            ("Continuity Scope", "blue"),
            ("Governance Control", "purple"),
            ("Executive Coordination", "cyan"),
            ("Evidence Reporting", "green"),
            ("Core Governance Capability", "purple"),
            ("Executive Decision Point", "cyan"),
        ],
    },
}


SCENARIO_PROFILES = {
    "resource-rebalancing": {
        "title": "Resource Rebalancing Automation",
        "subtitle": "Recovery Automation Board for Resource Rebalancing and Stabilization",
        "sections": {
            "incident-trigger": {
                "title": "Resource Pressure & Recovery Trigger",
                "summary": "PRESSURE DETECTED",
                "description": "Operational resource signals that indicate imbalance, saturation, or recovery automation eligibility.",
                "cards": [
                    ("CPU Pressure", "Compute utilization threshold", "metric", "Warning", "📈", False, None),
                    ("Memory Saturation", "Workload memory pressure signal", "metric", "Observed", "🧠", False, None),
                    ("Storage Hotspot", "Capacity or I/O imbalance", "storage", "Detected", "💾", False, None),
                    ("Alert Candidate", "Recovery evaluation trigger", "alert", "Ready", "🚨", False, None),
                ],
            },
            "recovery-control": {
                "title": "Capacity Analysis & Rebalancing Decision",
                "summary": "ANALYSIS ACTIVE",
                "description": "Analysis layer responsible for workload placement, utilization correlation, and recovery decision support.",
                "cards": [
                    ("Capacity Analyzer", "Resource imbalance analysis", "analysis", "Analyzing", "🧠", True, "CORE"),
                    ("Workload Mapping", "Service-to-resource dependency", "dependency", "Mapped", "🕸️", False, None),
                    ("Policy Guard", "Automation safety constraint", "policy", "Checked", "🛡️", False, None),
                    ("Rebalancing Plan", "Approved resource movement plan", "plan", "Prepared", "📋", False, None),
                ],
            },
            "automation-execution": {
                "title": "Automation Execution",
                "summary": "ACTION READY",
                "description": "Controlled automation actions used to redistribute resource pressure and restore operational stability.",
                "cards": [
                    ("Scale Action", "Increase available resource capacity", "automation", "Ready", "⚙️", False, None),
                    ("Workload Shift", "Move workload away from constrained node", "rebalance", "Available", "🔀", True, "ACTION"),
                    ("Resource Throttle", "Limit noisy or unstable workload", "control", "Ready", "🚦", False, None),
                    ("Operator Notice", "Automation activity notification", "notification", "Prepared", "📣", False, None),
                ],
            },
            "recovery-validation": {
                "title": "Post-Rebalancing Validation",
                "summary": "VALIDATION READY",
                "description": "Validation checks confirming resource distribution and service stability after automation.",
                "cards": [
                    ("Resource Normalization", "Utilization returned to expected range", "validation", "Normal", "✅", False, None),
                    ("Service Stability", "Application health remains stable", "validation", "Verified", "🟢", False, None),
                    ("Telemetry Continuity", "Signals remain available after recovery", "validation", "Healthy", "📡", False, None),
                    ("Recovery Evidence", "Recovery validation package", "evidence", "Prepared", "📦", True, "VERIFY"),
                ],
            },
        },
        "dashboard": [
            ("Recovery State", "Ready", "normal"),
            ("CPU Pressure", "Warning", "warning"),
            ("Memory", "Observed", "normal"),
            ("Plan", "Prepared", "verified"),
            ("Automation", "Available", "normal"),
            ("Validation", "Verified", "healthy"),
        ],
    }
}


def title_from_slug(value: str) -> str:
    return value.replace("-", " ").title()


def load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def write_yaml(path: Path, data: dict):
    path.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )


def find_profile(scenario_name: str):
    for key, profile in SCENARIO_PROFILES.items():
        if key in scenario_name:
            return profile
    return None


def make_card(item):
    title, subtitle, card_type, status, icon, emphasis, emphasis_label = item

    data = {
        "title": title,
        "subtitle": subtitle,
        "type": card_type,
        "status": status,
        "icon": icon,
    }

    if emphasis:
        data["emphasis"] = True

    if emphasis_label:
        data["emphasis_label"] = emphasis_label

    return data


def generic_cards(scenario_title: str):
    return [
        make_card(("Operational Signal", f"{scenario_title} signal source", "signal", "Observed", "📡", False, None)),
        make_card(("Control Point", f"{scenario_title} operational control", "control", "Ready", "⚙️", False, None)),
        make_card(("Validation Output", f"{scenario_title} validation output", "validation", "Verified", "✅", False, None)),
        make_card(("Evidence Artifact", f"{scenario_title} reviewer evidence", "evidence", "Prepared", "📦", False, None)),
    ]


def build_sections(level: str, metadata: dict, config: dict, profile: dict | None):
    scenario_name = metadata.get("scenario_name") or "scenario"
    scenario_title = metadata.get("scenario_title") or title_from_slug(scenario_name)

    sections = []

    for section_id, default_title, default_summary in config["sections"]:
        profile_section = (profile or {}).get("sections", {}).get(section_id)

        if profile_section:
            sections.append(
                {
                    "id": section_id,
                    "title": profile_section["title"],
                    "summary": profile_section["summary"],
                    "description": profile_section["description"],
                    "cards": [make_card(item) for item in profile_section["cards"]],
                }
            )
        else:
            sections.append(
                {
                    "id": section_id,
                    "title": default_title,
                    "summary": default_summary,
                    "description": f"{default_title} for {scenario_title}.",
                    "cards": generic_cards(scenario_title),
                }
            )

    return sections


def build_workflow(config: dict):
    return {
        "title": config["workflow_title"],
        "steps": [
            {
                "title": title,
                "description": description,
                "status": status,
            }
            for title, description, status in config["workflow_steps"]
        ],
    }


def build_dashboards(metadata: dict, profile: dict | None):
    scenario_name = metadata.get("scenario_name") or "scenario"
    scenario_title = metadata.get("scenario_title") or title_from_slug(scenario_name)

    widgets = (profile or {}).get(
        "dashboard",
        [
            ("State", "Ready", "normal"),
            ("Signal", "Observed", "normal"),
            ("Control", "Prepared", "verified"),
            ("Action", "Available", "normal"),
            ("Validation", "Verified", "healthy"),
            ("Evidence", "Prepared", "verified"),
        ],
    )

    return [
        {
            "title": f"{scenario_title} Status",
            "widgets": [
                {
                    "label": label,
                    "value": value,
                    "status": status,
                }
                for label, value, status in widgets
            ],
        }
    ]


def build_legend(config: dict):
    return [
        {
            "label": label,
            "color": color,
        }
        for label, color in config["legend"]
    ]


def build_poster(metadata_path: Path):
    metadata = load_yaml(metadata_path)

    level = metadata.get("lifecycle_level") or metadata_path.parent.parent.name
    config = LEVEL_CONFIG.get(level)

    if not config:
        raise RuntimeError(f"Unsupported lifecycle level: {level}")

    scenario_name = metadata.get("scenario_name") or metadata_path.parent.name
    scenario_title = metadata.get("scenario_title") or title_from_slug(scenario_name)
    lifecycle_name = metadata.get("lifecycle_name") or config["lifecycle"]
    domain = metadata.get("operational_scope") or "Infrastructure Operations"

    profile = find_profile(scenario_name)

    poster_title = profile.get("title") if profile else scenario_title
    poster_subtitle = profile.get("subtitle") if profile else f"{lifecycle_name} Board for {scenario_title}"

    return {
        "poster": {
            "title": poster_title,
            "subtitle": poster_subtitle,
            "lifecycle": config["lifecycle"],
            "domain": domain,
            "width": 2600,
            "height": 1900,
        },
        "sections": build_sections(level, metadata, config, profile),
        "workflow": build_workflow(config),
        "dashboards": build_dashboards(metadata, profile),
        "legend": build_legend(config),
    }


def main():
    force = "--force" in sys.argv
    only = None

    for arg in sys.argv:
        if arg.startswith("--only="):
            only = arg.split("=", 1)[1].strip()

    targets = sorted(SCENARIOS_ROOT.glob("*/*/metadata.yaml"))

    created = 0
    skipped = 0
    updated = 0

    for metadata_path in targets:
        scenario_name = metadata_path.parent.name

        if only and only not in scenario_name:
            continue

        poster_path = metadata_path.parent / "poster.yaml"

        if poster_path.exists() and not force:
            skipped += 1
            print(f"[SKIP] poster.yaml exists: {poster_path}")
            continue

        poster_data = build_poster(metadata_path)
        existed_before = poster_path.exists()
        write_yaml(poster_path, poster_data)

        if existed_before:
            updated += 1
            print(f"[UPDATE] poster.yaml: {poster_path}")
        else:
            created += 1
            print(f"[CREATE] poster.yaml: {poster_path}")

    print()
    print("[OK] poster seed completed")
    print(f"[OK] created={created}")
    print(f"[OK] updated={updated}")
    print(f"[OK] skipped={skipped}")


if __name__ == "__main__":
    main()
