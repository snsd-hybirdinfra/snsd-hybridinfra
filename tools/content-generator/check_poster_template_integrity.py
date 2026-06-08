from pathlib import Path
import sys
import yaml

EXPECTED = {
    "level-1-visibility": {
        "count": 45,
        "template_like": ["poster", "sections", "workflow", "dashboards", "legend"],
    },
    "level-2-correlation": {
        "count": 41,
        "template_like": ["poster", "sections", "workflow", "dashboards", "legend"],
    },
    "level-3-recovery": {
        "count": 33,
        "template_like": ["poster", "sections", "workflow", "dashboards", "legend"],
    },
    "level-4-resilience": {
        "count": 21,
        "template_like": ["poster", "sections", "workflow", "dashboards", "legend"],
    },
    "level-5-continuity": {
        "count": 10,
        "template_like": ["poster", "sections", "workflow", "dashboards", "legend"],
    },
}

errors = []

for level, spec in EXPECTED.items():
    scenario_dirs = sorted(Path("scenarios", level).glob("*"))
    scenario_dirs = [p for p in scenario_dirs if p.is_dir()]

    print(f"{level}: scenarios={len(scenario_dirs)} expected={spec['count']}")

    if len(scenario_dirs) != spec["count"]:
        errors.append(f"{level}: expected {spec['count']} scenarios, found {len(scenario_dirs)}")

    for scenario_dir in scenario_dirs:
        poster_path = scenario_dir / "poster.yaml"
        svg_path = scenario_dir / "diagrams" / "operational-poster.svg"
        png_path = scenario_dir / "diagrams" / "operational-poster.png"

        if not poster_path.exists():
            errors.append(f"missing poster.yaml: {poster_path}")
            continue

        try:
            data = yaml.safe_load(poster_path.read_text(encoding="utf-8-sig")) or {}
        except Exception as exc:
            errors.append(f"invalid poster yaml: {poster_path} :: {exc}")
            continue

        for key in spec["template_like"]:
            if key not in data:
                errors.append(f"missing poster key: {poster_path} :: {key}")

        poster = data.get("poster", {})
        lifecycle = poster.get("lifecycle")

        if lifecycle != level:
            errors.append(f"lifecycle mismatch: {poster_path} :: {lifecycle} != {level}")

        sections = data.get("sections", [])
        if not isinstance(sections, list) or len(sections) < 3:
            errors.append(f"insufficient sections: {poster_path}")

        for section in sections:
            cards = section.get("cards", []) if isinstance(section, dict) else []
            if not cards:
                errors.append(f"section has no cards: {poster_path} :: {section.get('id') if isinstance(section, dict) else 'unknown'}")

        if not svg_path.exists():
            errors.append(f"missing svg: {svg_path}")

        if not png_path.exists():
            errors.append(f"missing png: {png_path}")
        elif png_path.stat().st_size < 1000:
            errors.append(f"small png: {png_path} :: {png_path.stat().st_size} bytes")

print()

if errors:
    print("POSTER VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("POSTER VALIDATION PASS")
