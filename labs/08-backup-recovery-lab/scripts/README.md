# Backup Recovery Lab Scripts

This directory contains lab-local execution entrypoints for the Backup Recovery Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare backup source, repository, restore target, and evidence boundaries |
| validate.sh | Execute backup job, artifact, metadata, restore, integrity, service recovery, and evidence validation checks |
| cleanup.sh | Clean temporary backup recovery validation outputs while preserving evidence |

## Execution Boundary

These scripts belong only to:

labs/08-backup-recovery-lab/

They coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- backup source readiness checks
- backup repository readiness checks
- backup job execution checks
- backup artifact validation
- backup metadata validation
- restore workflow validation
- checksum and integrity validation
- service recovery validation
- backup recovery evidence generation
