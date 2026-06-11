# Ansible Automation Execution Boundary Note

## Execution Mode

The Ansible Automation Lab validates automation execution against Linux targets prepared by the Linux Observability Lab.

This lab uses Ansible inventory, SSH key-based access, playbook execution, validation playbooks, and cleanup playbooks to demonstrate repeatable operational automation.

## Upstream Dependency

Upstream lab:

- 01-linux-observability-lab

Required upstream state:

- Linux target nodes are reachable
- SSH key-based access is available
- Passwordless sudo is configured for the automation user
- Python 3 is available on the managed nodes

## Automation Boundary

This lab validates:

- Ansible inventory resolution
- SSH connectivity
- Privilege escalation through sudo
- Package management automation
- Service state automation
- Managed file creation
- Validation playbook execution
- Cleanup playbook execution
- Local runtime summary generation

This lab does not validate:

- Enterprise secrets management
- AWX or Ansible Automation Platform
- Production RBAC
- Multi-environment promotion
- Long-running orchestration workflows
- External approval gates

## Evidence Policy

Generated runtime evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside repository commit history.

## Runtime Summary

Local runtime execution produces:

- evidence/generated/summary/ansible-automation-execution-summary.md

This summary is consumed by the local repository executive summary generator when present.