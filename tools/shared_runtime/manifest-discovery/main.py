from pathlib import Path
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

TOOLS_ROOT = (
    REPO_ROOT
    / "tools"
)

MANIFEST_NAME = "manifest.yaml"


def discover_manifests():

    manifests = []

    for manifest_path in TOOLS_ROOT.rglob(
        MANIFEST_NAME
    ):

        manifests.append(
            manifest_path
        )

    return sorted(manifests)


def load_manifest(
    manifest_path: Path
):

    with open(
        manifest_path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def validate_manifest(
    manifest: dict,
    manifest_path: Path
):

    if "tool" not in manifest:

        raise ValueError(
            f"Missing tool section: "
            f"{manifest_path}"
        )

    required_fields = [

        "name",
        "category",
        "runtime",
        "entrypoint",
        "bootstrap",
        "orchestration",
        "order"
    ]

    tool = manifest["tool"]

    for field in required_fields:

        if field not in tool:

            raise ValueError(
                f"Missing manifest field "
                f"'{field}' in "
                f"{manifest_path}"
            )


def build_runtime_registry():

    runtime_registry = []

    manifests = discover_manifests()

    print(
        f"Discovered manifests: "
        f"{len(manifests)}"
    )

    for manifest_path in manifests:

        manifest = load_manifest(
            manifest_path
        )

        validate_manifest(
            manifest,
            manifest_path
        )

        tool = manifest["tool"]

        runtime_registry.append({

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

            "order":
                tool["order"],

            "path":
                str(
                    manifest_path.parent
                )
        })

    return sorted(
        runtime_registry,
        key=lambda item: item["order"]
    )


def main():

    registry = build_runtime_registry()

    print(
        "Runtime registry:"
    )

    for tool in registry:

        print(
            f"[{tool['order']}] "
            f"{tool['name']} "
            f"({tool['category']})"
        )


if __name__ == "__main__":
    main()
