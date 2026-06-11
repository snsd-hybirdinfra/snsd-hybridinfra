# Linux Observability Lab Execution Boundary Note

## Execution Modes

This lab supports two execution modes.

| Mode | Purpose | Git Policy |
|---|---|---|
| local-node | Validate Ansible and parser workflow against WSL local execution | Documentation only |
| remote-password | Validate SSH-based execution against a Linux VM using password authentication | Runtime evidence remains local-only |
| remote-key | Future target mode using SSH private key authentication | Runtime evidence remains local-only |

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

This does not validate:

- Remote SSH target connectivity
- Multi-node inventory execution
- External VM or server reachability
- Production network observability

## Remote Password Execution Boundary

The remote-password mode uses WSL Ubuntu as the Ansible control node and a VMware Ubuntu VM as the managed target.

This validates:

- SSH reachability from WSL to the Linux VM
- Ansible remote inventory execution
- Password-based SSH authentication
- Become privilege escalation
- Remote setup playbook execution
- Remote validation playbook execution
- Local-only evidence parsing from captured Ansible output

This does not validate:

- SSH key-based automation
- Multi-node production inventory
- Prometheus scrape integration
- Grafana dashboard integration
- Long-running observability telemetry collection

## Current Execution Status

| Item | Status |
|---|---|
| Inventory mode | local-node and remote-password supported |
| Ansible inventory check | validated |
| Ansible ping | validated |
| Become privilege path | validated |
| setup.sh | supports local and remote password mode |
| validate.sh | supports local and remote password mode |
| Evidence parser | supported |
| Generated evidence | local-only |

## Evidence Policy

Generated evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside the repository commit history.

## Next Execution Target

The next implementation step is to move from remote-password execution to remote-key execution using SSH key-based Ansible access.