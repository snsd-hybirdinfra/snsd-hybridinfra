# Kolla OpenStack Lab Scripts

This directory contains lab-local execution entrypoints for the Kolla OpenStack Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare Kolla-Ansible, OpenStack validation, and evidence boundaries |
| validate.sh | Execute Kolla, OpenStack API, endpoint, compute, network, service container, recovery, and evidence validation checks |
| cleanup.sh | Clean temporary OpenStack validation outputs while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/05-kolla-openstack-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- Kolla-Ansible configuration readiness checks
- OpenStack service container validation
- OpenStack API availability checks
- service catalog and endpoint validation
- compute service visibility checks
- network service validation checks
- service recovery workflow validation
- OpenStack evidence generation
