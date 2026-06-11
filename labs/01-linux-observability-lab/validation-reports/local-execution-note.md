# Local Execution Note

## Execution Mode

This lab was validated first using local-node execution mode.

The local-node mode uses the WSL Ubuntu environment as the Ansible execution target.

## Execution Boundary

This execution mode validates:

- Ansible inventory parsing
- Playbook syntax
- Local connection execution
- Privilege escalation behavior
- Validation playbook execution
- Evidence parser execution
- Generated local evidence structure

This execution mode does not validate:

- Remote SSH target connectivity
- Multi-node inventory execution
- External VM or server reachability
- Production network observability

## Current Local Execution Status

| Item | Status |
|---|---|
| Inventory mode | local-node |
| Ansible inventory check | validated |
| Ansible ping | validated |
| Become privilege path | validated with NOPASSWD sudo |
| setup.sh | executed locally |
| validate.sh | executed locally |
| Evidence parser | executed locally |
| Generated evidence | local-only |

## Evidence Policy

Generated evidence under evidence/generated/ is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary, while raw local runtime evidence remains outside the repository commit history.

## Next Execution Target

The next implementation step is to replace local-node mode with a real Linux target inventory using SSH-based Ansible execution.