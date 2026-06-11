# Linux Observability Lab Scripts

This directory contains lab-local execution entrypoints for the Linux Observability Lab.

## Script Roles

| Script | Purpose |
|---|---|
| preflight.sh | Validate local execution prerequisites before setup or validation |
| setup.sh | Prepare required packages and target evidence boundary |
| validate.sh | Execute Linux observability validation and generate evidence |
| cleanup.sh | Clean temporary runtime files while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/01-linux-observability-lab/

They coordinate inventory, Ansible playbooks, runtime workspace, and generated evidence outputs.

## Execution Order

1. preflight.sh
2. setup.sh
3. validate.sh
4. cleanup.sh

## Output Boundaries

Runtime logs:

- runtime-workspace/logs/

Generated evidence:

- evidence/generated/raw/
- evidence/generated/processed/
- evidence/generated/summary/

---

## Evidence Parser

| Script | Purpose |
|---|---|
| parse_evidence.py | Parses raw Ansible validation logs into processed and summary evidence |
## Execution Modes

### Local Node Execution

Use this mode when the inventory uses ansible_connection=local.

Command:

    bash scripts/setup.sh
    bash scripts/validate.sh

### Remote Password Execution

Use this mode when the inventory points to a remote Linux VM and SSH password authentication is required.

Command:

    ANSIBLE_ASK_PASS=true ANSIBLE_ASK_BECOME_PASS=true bash scripts/setup.sh
    ANSIBLE_ASK_PASS=true ANSIBLE_ASK_BECOME_PASS=true bash scripts/validate.sh

### Future Remote Key Execution

Use this mode after SSH key authentication is configured for the target VM.

Command:

    bash scripts/setup.sh
    bash scripts/validate.sh
