from pathlib import Path
import json
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

TOOLS_ROOT = (
    REPO_ROOT
    / "tools"
)

OUTPUT_PATH = (
    REPO_ROOT
    / "tools"
    / "runtime-registry.json"
)


def load_yaml(path: Path):

    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():

    registry = []

    for manifest_path in TOOLS_ROOT.rglob("manifest.yaml"):

        manifest = load_yaml(manifest_path)
        tool = manifest["tool"]

        registry.append({

    "name":
        tool["name"],

    "category":
        tool["category"],

    "runtime":
        tool["runtime"],

    "entrypoint":
        tool["entrypoint"],

    "bootstrap":
        tool["bootstrap"],

    "orchestration":
        tool["orchestration"],

    "state":
        tool.get(
            "state",
            "active"
        ),

    "order":
        tool["order"],

    "path":
        str(
            manifest_path.parent.relative_to(REPO_ROOT)
        )
})

    registry = sorted(
        registry,
        key=lambda item: item["order"]
    )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        json.dump(registry, file, indent=2)

    print(f"Runtime registry exported: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
