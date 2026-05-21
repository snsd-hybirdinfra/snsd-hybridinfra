from pathlib import Path
import re
import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

SCENARIOS_ROOT = (
    REPO_ROOT
    / "scenarios"
)

RULES_PATH = (
    Path(__file__).resolve().parent
    / "rules"
    / "lifecycle-semantic-rules.yaml"
)


IMAGE_PATTERN = re.compile(
    r"!\[[^\]]*\]\((\.\/diagrams\/[^)]+)\)"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def is_strict_golden_scenario(readme_path: Path):

    return "vpn-latency-visibility" in str(readme_path)


def extract_lifecycle(readme_path: Path):

    parts = readme_path.parts

    for part in parts:

        if part.startswith("level-"):

            return part

    return None


def extract_diagram_references(readme_path: Path):

    content = readme_path.read_text(
        encoding="utf-8"
    )

    return IMAGE_PATTERN.findall(
        content
    )


def validate_lifecycle_semantics(
    readme_path: Path,
    rules: dict
):

    lifecycle = extract_lifecycle(
        readme_path
    )

    if lifecycle is None:

        return

    lifecycle_rules = (
        rules
        .get("lifecycle_rules", {})
        .get(lifecycle, {})
    )

    forbidden_terms = lifecycle_rules.get(
        "forbidden",
        []
    )

    content = readme_path.read_text(
        encoding="utf-8"
    ).lower()

    for term in forbidden_terms:

        if term.lower() in content:

            print(
                f"WARNING: Lifecycle semantic term found in "
                f"{readme_path}: '{term}' for {lifecycle}"
            )


def validate_readme_diagrams(readme_path: Path):

    scenario_dir = readme_path.parent

    references = extract_diagram_references(
        readme_path
    )

    for reference in references:

        diagram_path = (
            scenario_dir
            / reference.replace(
                "./",
                ""
            )
        )

        if not diagram_path.exists():

            if is_strict_golden_scenario(readme_path):

                raise FileNotFoundError(
                    f"Missing referenced diagram: "
                    f"{diagram_path}"
                )

            print(
                f"WARNING: Missing non-strict diagram: "
                f"{diagram_path}"
            )

            continue

        if (
            diagram_path.suffix == ".png"
            and is_strict_golden_scenario(readme_path)
        ):

            svg_path = diagram_path.with_suffix(".svg")
            spec_path = diagram_path.with_suffix(".spec.yaml")

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

    return len(references)


def main():

    rules = load_yaml(
        RULES_PATH
    )

    readmes = sorted(
        SCENARIOS_ROOT.rglob("README.md")
    )

    checked = 0
    references = 0

    for readme in readmes:

        checked += 1

        validate_lifecycle_semantics(
            readme,
            rules
        )

        references += validate_readme_diagrams(
            readme
        )

    print(
        f"Diagram and lifecycle semantic validation completed. "
        f"README files checked: {checked}, "
        f"diagram references checked: {references}"
    )


if __name__ == "__main__":
    main()

