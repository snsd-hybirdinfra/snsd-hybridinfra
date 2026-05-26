from pathlib import Path
from datetime import datetime, timedelta
import shutil


REPO_ROOT = Path(__file__).resolve().parents[3]

RUNTIME_ROOT = (
    REPO_ROOT
    / "tools"
    / "runtime-workspace"
)

RETENTION_DAYS = 7

MAX_RUN_DIRECTORIES = 20


def remove_old_directories():

    if not RUNTIME_ROOT.exists():

        return

    now = datetime.utcnow()

    for directory in RUNTIME_ROOT.iterdir():

        if not directory.is_dir():

            continue

        modified = datetime.utcfromtimestamp(
            directory.stat().st_mtime
        )

        age = now - modified

        if age > timedelta(days=RETENTION_DAYS):

            print(
                f"[CLEANUP] removing expired runtime: "
                f"{directory.name}"
            )

            shutil.rmtree(
                directory,
                ignore_errors=True
            )


def enforce_directory_limit():

    if not RUNTIME_ROOT.exists():

        return

    directories = sorted(
        [
            item
            for item in RUNTIME_ROOT.iterdir()
            if item.is_dir()
        ],
        key=lambda item: item.stat().st_mtime,
        reverse=True
    )

    if len(directories) < MAX_RUN_DIRECTORIES:

        return

    overflow = directories[
        MAX_RUN_DIRECTORIES:
    ]

    for directory in overflow:

        print(
            f"[CLEANUP] removing overflow runtime: "
            f"{directory.name}"
        )

        shutil.rmtree(
            directory,
            ignore_errors=True
        )


def cleanup_runtime_workspace():

    remove_old_directories()

    enforce_directory_limit()
