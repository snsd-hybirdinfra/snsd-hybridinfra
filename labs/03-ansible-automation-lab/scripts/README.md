# Ansible Automation Lab Scripts

This directory contains lab-local execution entrypoints for the Ansible Automation Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare Ansible automation lab prerequisites |
| validate.sh | Execute inventory, SSH, playbook, rollback, recovery, and evidence validation checks |
| cleanup.sh | Clean temporary automation lab execution outputs |

## Execution Boundary

These scripts belong only to:

labs/03-ansible-automation-lab/

They are intended to coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- Ansible control node preparation
- inventory validation
- SSH reachability checks
- playbook syntax checks
- setup workflow execution
- rollback workflow execution
- recovery workflow execution
- post-execution validation
- evidence generation
