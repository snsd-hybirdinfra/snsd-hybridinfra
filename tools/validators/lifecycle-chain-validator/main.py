from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parents[3]
        / "tools"
    )
)

from shared_runtime.src.runtime_encoding import (
    configure_runtime_encoding
)

configure_runtime_encoding()

from src.loader import (
    load_rules,
    discover_scenario_readmes
)

from src.validator import (
    validate_relationships
)

from src.report import (
    write_report
)


def main():

    rules = load_rules()

    readmes = discover_scenario_readmes()

    findings = []

    for readme in readmes:

        findings.extend(
            validate_relationships(
                readme,
                rules
            )
        )

    write_report(
        findings
    )

    if findings:

        print(
            f"Lifecycle chain validation completed with warnings: {len(findings)}"
        )

    else:

        print(
            "Lifecycle chain validation passed."
        )


if __name__ == "__main__":
    main()


