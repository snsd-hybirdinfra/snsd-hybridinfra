from pathlib import Path
import json
import hashlib
import base64
import yaml

# 1x1 transparent PNG
PLACEHOLDER_PNG_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
    "/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_metadata(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}

scenario_dirs = sorted(p for p in Path("scenarios").glob("level-*/*") if p.is_dir())
count = 0

for scenario_dir in scenario_dirs:
    metadata = load_metadata(scenario_dir / "metadata.yaml")

    scenario_name = metadata.get("scenario_name", scenario_dir.name)
    scenario_title = metadata.get("scenario_title", scenario_dir.name)
    lifecycle_level = metadata.get("lifecycle_level", scenario_dir.parent.name)
    primary_domain = metadata.get("primary_domain", "Infrastructure Operations")

    diagrams_dir = scenario_dir / "diagrams"
    evidence_dir = scenario_dir / "evidence" / "generated"

    diagrams_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    poster_path = diagrams_dir / "operational-poster.png"
    if not poster_path.exists():
        poster_path.write_bytes(base64.b64decode(PLACEHOLDER_PNG_BASE64))

    summary_path = evidence_dir / "summary.md"
    execution_path = evidence_dir / "execution-evidence.md"
    validation_path = evidence_dir / "validation-evidence.md"
    manifest_path = evidence_dir / "artifact-manifest.json"
    checksums_path = evidence_dir / "artifact-checksums.json"

    summary_path.write_text(f"""# Evidence Summary

## Scenario

| Field | Value |
|---|---|
| Scenario Name | {scenario_name} |
| Scenario Title | {scenario_title} |
| Lifecycle Level | {lifecycle_level} |
| Primary Domain | {primary_domain} |

## Summary

This placeholder evidence file confirms that the scenario has a reviewable evidence location.

Detailed runtime evidence can be added when the scenario is executed or demonstrated.
""", encoding="utf-8")

    execution_path.write_text(f"""# Execution Evidence

## Scenario

{scenario_title}

## Execution Status

Placeholder evidence generated for repository link integrity.

## Notes

This file should be replaced or extended with command output, workflow execution logs, screenshots, or generated artifacts when the scenario is executed.
""", encoding="utf-8")

    validation_path.write_text(f"""# Validation Evidence

## Scenario

{scenario_title}

## Validation Status

Placeholder validation evidence generated for repository link integrity.

## Notes

This file should be replaced or extended with validation results, health checks, recovery confirmation, monitoring screenshots, or reviewer-safe proof artifacts.
""", encoding="utf-8")

    manifest = {
        "scenario_name": scenario_name,
        "scenario_title": scenario_title,
        "lifecycle_level": lifecycle_level,
        "primary_domain": primary_domain,
        "artifacts": [
            "diagrams/operational-poster.png",
            "evidence/generated/summary.md",
            "evidence/generated/execution-evidence.md",
            "evidence/generated/validation-evidence.md",
            "evidence/generated/artifact-manifest.json",
            "evidence/generated/artifact-checksums.json"
        ],
        "status": "placeholder-generated"
    }

    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    checksums = {
        "diagrams/operational-poster.png": sha256(poster_path),
        "evidence/generated/summary.md": sha256(summary_path),
        "evidence/generated/execution-evidence.md": sha256(execution_path),
        "evidence/generated/validation-evidence.md": sha256(validation_path),
        "evidence/generated/artifact-manifest.json": sha256(manifest_path),
    }

    checksums_path.write_text(json.dumps(checksums, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    count += 1

print(f"[OK] generated placeholder artifacts for scenarios: {count}")
