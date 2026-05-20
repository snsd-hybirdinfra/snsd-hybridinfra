from pathlib import Path
import shutil
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

POLICY_PATH = (
    REPO_ROOT
    / "governance"
    / "runtime-cleanup-governance.yaml"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def main():

    policy = load_yaml(
        POLICY_PATH
    )

    retention = policy[
        "runtime_cleanup_policy"
    ][
        "retention"
    ]

    keep_latest = retention[
        "keep_latest_runs"
    ]

    runtime_root = (
        REPO_ROOT
        / "tools"
        / "runtime-workspace"
    )

    if not runtime_root.exists():

        print(
            "Runtime workspace does not exist."
        )

        return

    runs = sorted(
        [
            path for path in runtime_root.iterdir()
            if path.is_dir()
        ],
        key=lambda path: path.stat().st_mtime,
        reverse=True
    )

    protected_runs = runs[:keep_latest]

    removable_runs = runs[keep_latest:]

    print(
        f"Protected runs: "
        f"{len(protected_runs)}"
    )

    print(
        f"Removable runs: "
        f"{len(removable_runs)}"
    )

    for run_path in removable_runs:

        print(
            f"Removing: {run_path.name}"
        )

        shutil.rmtree(
            run_path,
            ignore_errors=True
        )

    print(
        "Runtime cleanup completed."
    )


if __name__ == "__main__":
    main()
