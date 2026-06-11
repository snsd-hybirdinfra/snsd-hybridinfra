# Linux Observability Lab Execution Boundary Note

## Execution Modes

This lab supports four execution modes.

| Mode | Purpose | Git Policy |
|---|---|---|
| local-node | Validate Ansible and parser workflow against WSL local execution | Documentation only |
| remote-password | Validate SSH-based execution against a Linux VM using password authentication | Runtime evidence remains local-only |
| remote-key-single-node | Validate SSH key-based execution against a single Linux VM | Runtime evidence remains local-only |
| remote-key-two-node | Validate SSH key-based execution across two Linux VM targets | Runtime evidence remains local-only |

## Local Execution Boundary

The local-node mode uses the WSL Ubuntu environment as the Ansible execution target.

This validates:

- Ansible inventory parsing
- Playbook syntax
- Local connection execution
- Privilege escalation behavior
- Validation playbook execution
- Evidence parser execution
- Generated local evidence structure

## Remote Password Execution Boundary

The remote-password mode uses WSL Ubuntu as the Ansible control node and a Linux VM as the managed target.

This validates:

- SSH reachability from WSL to the Linux VM
- Ansible remote inventory execution
- Password-based SSH authentication
- Become privilege escalation
- Remote setup playbook execution
- Remote validation playbook execution

## Remote Key Single-Node Boundary

The remote-key single-node mode validates passwordless SSH automation against one Linux VM target.

This validates:

- SSH key-based Ansible connectivity
- Remote Linux target execution
- Passwordless SSH access
- Become privilege escalation readiness
- Remote setup workflow execution
- Remote validation workflow execution
- Evidence parser execution from captured Ansible output

## Remote Key Two-Node Boundary

The remote-key two-node mode validates that the lab can manage multiple Linux targets using the same Ansible execution workflow.

This validates:

- Multi-host inventory parsing
- SSH key-based access across two Linux targets
- Become privilege readiness across multiple targets
- Setup workflow execution across multiple targets
- Validation workflow execution across multiple targets
- Local-only evidence parsing from multi-host Ansible output

This does not validate:

- Production-scale dynamic inventory
- Prometheus scrape lifecycle
- Grafana dashboard publishing
- Long-running alert lifecycle validation
- Centralized telemetry retention

## Current Execution Status

| Item | Status |
|---|---|
| Inventory mode | local-node, remote-password, remote-key-single-node, and remote-key-two-node supported |
| Ansible inventory check | validated |
| Ansible ping | validated |
| Become privilege path | validated |
| setup.sh | supports local, remote-password, and remote-key mode |
| validate.sh | supports local, remote-password, and remote-key mode |
| Evidence parser | supported |
| Generated evidence | local-only |

## Evidence Policy

Generated evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside the repository commit history.

## Next Execution Target

The next implementation step is to connect Linux observability outputs to a monitoring stack, starting with Prometheus-oriented telemetry collection.